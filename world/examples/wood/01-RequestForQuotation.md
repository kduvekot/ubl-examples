# Request For Quotation: Valdara Industries to Marrowdale Sawmill

*Example 1 of the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)" · [Request For Quotation in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REQUEST-FOR-QUOTATION-SCHEMA)*

Slats to the manufacturer's own dimensions and wood species: it asks the sawmill to quote before ordering.

[The XML file](01-RequestForQuotation.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **VI-DOC-26-0625**  
  The buyer's request number.
- `IssueDate` = **2026-02-16**  
  The manufacturer asks for slats to its own dimensions.
- `IssueTime` = **10:00:00**  
  The time of the request; quotations refer to it.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Marrowdale Sawmill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits); identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **UL-1236987**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyLegalEntity/RegistrationName` = **Marrowdale Sawmill**  
  The name under which the party is registered; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412329**  
  Number in the Federal business register of Bayvarra; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Name` = **Sales office**  
  The department that handles this document; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Marrowdale Sawmill (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Marrowdale Sawmill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries**  
  The name under which the party is registered; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Name` = **Order desk**  
  The department that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Request For Quotation Line

Inside `RequestForQuotationLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **4800** (unitCode `H87`)  
  Slats for 960 benches: five per bench, 96 bundles of 50.
- `LineItem/Item/Description` = **Sawn hardwood slat, 1800 × 95 × 38 mm, planed, kiln dried.**  
  The seller's description; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/Name` = **Hardwood bench slat 1800**  
  The item's short name; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **MS-SL-1800**  
  The seller's own item number; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **772010000058** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **4407.99** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item slat-1800 of Marrowdale Sawmill (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RequestForQuotation xmlns="urn:oasis:names:specification:ubl:schema:xsd:RequestForQuotation-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>VI-DOC-26-0625</cbc:ID>
  <cbc:IssueDate>2026-02-16</cbc:IssueDate>
  <cbc:IssueTime>10:00:00</cbc:IssueTime>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Timber Lane</cbc:StreetName>
        <cbc:BuildingNumber>7</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71202</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>UL-1236987</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Marrowdale Sawmill</cbc:RegistrationName>
        <cbc:CompanyID>20412329</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Sales office</cbc:Name>
        <cbc:ElectronicMail>sales@marrowdalesawmill.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
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
  </cac:BuyerCustomerParty>
  <cac:RequestForQuotationLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="H87">4800</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Sawn hardwood slat, 1800 × 95 × 38 mm, planed, kiln dried.</cbc:Description>
        <cbc:Name>Hardwood bench slat 1800</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>MS-SL-1800</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772010000058</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">4407.99</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:LineItem>
  </cac:RequestForQuotationLine>
</RequestForQuotation>
```
