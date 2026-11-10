# Forecast Revision: Lumeport Textile Mill to Selanu Cotton Ginnery

*Example 6 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Forecast Revision in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORECAST-REVISION-SCHEMA)*

Demand for clothing is up; the mill revises its forecast upwards.

[The XML file](06-ForecastRevision.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **LTM-FR-26-0196**  
  The revision's number.
- `IssueDate` = **2026-02-22**  
  Demand for clothing has risen.
- `SequenceNumberID` = **1**  
  The first revision of the forecast.

### Forecast Period

Inside `ForecastPeriod`:

- `StartDate` = **2026-02-16**  
  The same period.
- `EndDate` = **2026-06-02**  
  Its end.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address; identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address; identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits); identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **CO-1237809**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Textile Mill (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Lumeport Textile Mill**  
  The name under which the party is registered; identity of Lumeport Textile Mill (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412603**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json).
- `Contact/Name` = **Purchasing**  
  The department that handles this document; identity of Lumeport Textile Mill (world/parties.json).
- `Contact/ElectronicMail` = **purchasing@lumeporttextile.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Textile Mill (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Textile Mill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

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

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Forecast Revision Line

Inside `ForecastRevisionLine`:

- `ID` = **1**  
  The only line.
- `RevisedForecastLineID` = **1**  
  The forecast line revised.
- `SourceForecastIssueDate` = **2026-02-02**  
  The issue date of the forecast revised.
- `SourceForecastIssueTime` = **09:00:00**  
  Its issue time.
- `SalesItem/Quantity` = **30000** (unitCode `KGM`)  
  Raised to five containers.
- `SalesItem/Item/Description` = **Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.**  
  The seller's description; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `SalesItem/Item/Name` = **Cotton lint, compressed bale**  
  The item's short name; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `SalesItem/Item/SellersItemIdentification/ID` = **SCG-LINT**  
  The seller's own item number; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `SalesItem/Item/StandardItemIdentification/ID` = **773020000137** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `SalesItem/Item/OriginCountry/IdentificationCode` = **XL**  
  Where the item was produced; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `SalesItem/Item/CommodityClassification/ItemClassificationCode` = **5201.00** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item cotton-bale of Selanu Cotton Ginnery (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForecastRevision xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForecastRevision-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>LTM-FR-26-0196</cbc:ID>
  <cbc:IssueDate>2026-02-22</cbc:IssueDate>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cac:ForecastPeriod>
    <cbc:StartDate>2026-02-16</cbc:StartDate>
    <cbc:EndDate>2026-06-02</cbc:EndDate>
  </cac:ForecastPeriod>
  <cac:SenderParty>
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
  </cac:SenderParty>
  <cac:ReceiverParty>
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
  </cac:ReceiverParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ForecastRevisionLine>
    <cbc:ID>1</cbc:ID>
    <cbc:RevisedForecastLineID>1</cbc:RevisedForecastLineID>
    <cbc:SourceForecastIssueDate>2026-02-02</cbc:SourceForecastIssueDate>
    <cbc:SourceForecastIssueTime>09:00:00</cbc:SourceForecastIssueTime>
    <cac:SalesItem>
      <cbc:Quantity unitCode="KGM">30000</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.</cbc:Description>
        <cbc:Name>Cotton lint, compressed bale</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>SCG-LINT</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">773020000137</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">5201.00</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:SalesItem>
  </cac:ForecastRevisionLine>
</ForecastRevision>
```
