# Tenderer Qualification: Valdara Industries to Lumeport Public Works Department

*Example 5 of the flow "A public tender (Bayvarra)" · [Tenderer Qualification in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TENDERER-QUALIFICATION-SCHEMA)*

The manufacturer declares its qualifications and those of its consortium partner.

[The XML file](05-TendererQualification.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **VI-DOC-26-0191**  
  The tenderer's number for its declaration.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-02-25**  
  Submitted with the tender.

### Tenderer Party Qualification

Inside `TendererPartyQualification`:

- `MainQualifyingParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainQualifyingParty/Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits); identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `MainQualifyingParty/Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `MainQualifyingParty/Party/PartyLegalEntity/RegistrationName` = **Valdara Industries**  
  The name under which the party is registered; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/Name` = **Order desk**  
  The department that handles this document; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainQualifyingParty/Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `AdditionalQualifyingParty/Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalQualifyingParty/Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits); identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `AdditionalQualifyingParty/Party/PartyTaxScheme/CompanyID` = **UL-1232055**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CompanyID` = **20410685**  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/Name` = **Bids office**  
  The department that handles this document; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `AdditionalQualifyingParty/Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Contracting Party

Inside `ContractingParty`:

- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410548**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Name` = **Procurement office**  
  The department that handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TendererQualification xmlns="urn:oasis:names:specification:ubl:schema:xsd:TendererQualification-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>VI-DOC-26-0191</cbc:ID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-25</cbc:IssueDate>
  <cac:TendererPartyQualification>
    <cac:MainQualifyingParty>
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
    </cac:MainQualifyingParty>
    <cac:AdditionalQualifyingParty>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:StreetName>Foundry Road</cbc:StreetName>
          <cbc:BuildingNumber>13</cbc:BuildingNumber>
          <cbc:CityName>Marrowdale</cbc:CityName>
          <cbc:PostalZone>71218</cbc:PostalZone>
          <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:CompanyID>UL-1232055</cbc:CompanyID>
          <cac:TaxScheme>
            <cbc:ID>STT</cbc:ID>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
          <cbc:CompanyID>20410685</cbc:CompanyID>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Bids office</cbc:Name>
          <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:Party>
    </cac:AdditionalQualifyingParty>
  </cac:TendererPartyQualification>
  <cac:ContractingParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>20410548</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Procurement office</cbc:Name>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410548</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:ContractingParty>
</TendererQualification>
```
