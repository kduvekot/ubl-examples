# Export Customs Declaration: Rinova Recovery to Customs Administration of Urvania

*Example 5 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The granulate leaves Urvania; the waste processor declares the export.

[The XML file](05-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **RR-EX-26-0887**  
  The exporter's reference.
- `IssueDate` = **2026-04-19**  
  Declared the day the barge is loaded.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/StreetName` = **Via del Riciclo**  
  Street of the postal address; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **XU007318479**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Rinova Recovery (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyLegalEntity/RegistrationName` = **Rinova Recovery**  
  The name under which the party is registered; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104548**  
  Number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json).
- `Contact/Name` = **Customer service**  
  The department that handles this document; identity of Rinova Recovery (world/parties.json).
- `Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **RR-CD-26-0888**  
  The declaration as lodged with the customs of the exporting country.
- `Shipment/ID` = **RR-SH-26-0889**  
  The shipment declared.
- `Shipment/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight leaving the country.
- `Shipment/Consignment/ID` = **RR-CS-26-0885**  
  The consignment carried.
- `Shipment/Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/Consignment/CarrierParty/PartyName/Name` = **Fiumella Barges**  
  The trading name; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/StreetName` = **Banchina del Fiume**  
  Street of the postal address; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits); identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/CompanyID` = **XU007347248**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/RegistrationName` = **Fiumella Barges**  
  The name under which the party is registered; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104959**  
  Number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/Name` = **Chartering desk**  
  The department that handles this document; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/ElectronicMail` = **chartering@fiumella.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Shipment/Consignment/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Fiumella Barges (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **9984000** (currencyID `XUF`)  
  The value of the granulate, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.**  
  The seller's description; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Recycled PE granulate**  
  The item's short name; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **RR-PE-R1**  
  The seller's own item number; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771030000048** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **3901.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item granulate-pe of Rinova Recovery (world/items.json).
- `ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `ConsigneeParty/PartyTaxScheme/CompanyID` = **CO-1238220**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `ConsigneeParty/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging**  
  The name under which the party is registered; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **20412740**  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Name` = **Order desk**  
  The department that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `CustomsParty/PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/StreetName` = **Valico di Confine**  
  Street of the postal address; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits); identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CustomsParty/PartyTaxScheme/CompanyID` = **XU007385602**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `CustomsParty/PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyLegalEntity/CompanyID` = **XU-R-105507**  
  Number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/Name` = **Border office**  
  The department that handles this document; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/ElectronicMail` = **border@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs Administration of Urvania (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>RR-EX-26-0887</cbc:ID>
  <cbc:IssueDate>2026-04-19</cbc:IssueDate>
  <cac:ExporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>XU007318479</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Rinova Recovery</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104548</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:ElectronicMail>customer@rinova.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:CustomsDeclaration>
    <cbc:ID>RR-CD-26-0888</cbc:ID>
    <cac:Shipment>
      <cbc:ID>RR-SH-26-0889</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cac:Consignment>
        <cbc:ID>RR-CS-26-0885</cbc:ID>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Fiumella Barges</cbc:Name>
          </cac:PartyName>
          <cac:PostalAddress>
            <cbc:StreetName>Banchina del Fiume</cbc:StreetName>
            <cbc:BuildingNumber>52</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cbc:PostalZone>4170</cbc:PostalZone>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:PostalAddress>
          <cac:PartyTaxScheme>
            <cbc:CompanyID>XU007347248</cbc:CompanyID>
            <cac:TaxScheme>
              <cbc:ID>VAT</cbc:ID>
            </cac:TaxScheme>
          </cac:PartyTaxScheme>
          <cac:PartyLegalEntity>
            <cbc:RegistrationName>Fiumella Barges</cbc:RegistrationName>
            <cbc:CompanyID>XU-R-104959</cbc:CompanyID>
          </cac:PartyLegalEntity>
          <cac:Contact>
            <cbc:Name>Chartering desk</cbc:Name>
            <cbc:ElectronicMail>chartering@fiumella.example</cbc:ElectronicMail>
          </cac:Contact>
          <cac:ElectronicAddress>
            <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
            <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104959</cbc:ElectronicAddressID>
          </cac:ElectronicAddress>
        </cac:CarrierParty>
      </cac:Consignment>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Recycled PE granulate</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">9984000</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.</cbc:Description>
          <cbc:Name>Recycled PE granulate</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>RR-PE-R1</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771030000048</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:ItemClassificationCode listID="HS">3901.10</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:Shipment>
    <cac:ConsigneeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Estuary Road</cbc:StreetName>
        <cbc:BuildingNumber>28</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38505</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>CO-1238220</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Rivermouth Packaging</cbc:RegistrationName>
        <cbc:CompanyID>20412740</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:ElectronicMail>order@rivermouth.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:ConsigneeParty>
    <cac:CustomsParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Customs Administration of Urvania</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Valico di Confine</cbc:StreetName>
        <cbc:BuildingNumber>22</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>XU007385602</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Customs Administration of Urvania</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105507</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Border office</cbc:Name>
        <cbc:ElectronicMail>border@customs-xu.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105507</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
  </cac:CustomsDeclaration>
</ExportCustomsDeclaration>
```
