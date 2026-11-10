# Forwarding Instructions: Lumeport Textile Mill to Bayforth Forwarding

*Example 8 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

Under FOB the buyer books the main carriage: the mill instructs its forwarder.

[The XML file](08-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **LTM-FI-26-0198**  
  The mill's instruction number.
- `IssueDate` = **2026-02-25**  
  Under FOB the buyer instructs the forwarder for the main carriage.

### Consignor Party

Inside `ConsignorParty`:

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

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address; identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address; identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits); identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **CO-1234932**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Bayforth Forwarding**  
  The name under which the party is registered; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411644**  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Name` = **Export desk**  
  The department that handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **SCG-SH-26-0199**  
  The shipment to be booked.
- `GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the bales.
- `Consignment/ID` = **LTM-CS-26-0200**  
  The consignment.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits); identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/ConsigneeParty/PartyTaxScheme/CompanyID` = **CO-1237809**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Lumeport Textile Mill**  
  The name under which the party is registered; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **20412603**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Name` = **Purchasing**  
  The department that handles this document; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **purchasing@lumeporttextile.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Textile Mill (world/parties.json).
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Textile Mill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>LTM-FI-26-0198</cbc:ID>
  <cbc:IssueDate>2026-02-25</cbc:IssueDate>
  <cac:ConsignorParty>
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
  </cac:ConsignorParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>CO-1234932</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Bayforth Forwarding</cbc:RegistrationName>
      <cbc:CompanyID>20411644</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Export desk</cbc:Name>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>SCG-SH-26-0199</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">6190.29</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>LTM-CS-26-0200</cbc:ID>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Textile Mill</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:StreetName>Mill Street</cbc:StreetName>
          <cbc:BuildingNumber>21</cbc:BuildingNumber>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38504</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:CompanyID>CO-1237809</cbc:CompanyID>
          <cac:TaxScheme>
            <cbc:ID>STT</cbc:ID>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Lumeport Textile Mill</cbc:RegistrationName>
          <cbc:CompanyID>20412603</cbc:CompanyID>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Purchasing</cbc:Name>
          <cbc:ElectronicMail>purchasing@lumeporttextile.example</cbc:ElectronicMail>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
    </cac:Consignment>
  </cac:Shipment>
</ForwardingInstructions>
```
