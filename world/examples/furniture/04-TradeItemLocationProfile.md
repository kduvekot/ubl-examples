# Trade Item Location Profile: Brightmarket Stores to Brackenmere Furniture

*Example 4 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Trade Item Location Profile in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRADE-ITEM-LOCATION-PROFILE-SCHEMA)*

The store sets the replenishment policy per item and store.

[The XML file](04-TradeItemLocationProfile.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **BS-DOC-26-0570**  
  The sender's number for its location profile.
- `IssueDate` = **2026-03-14**  
  The store sets its replenishment policy for the line.

### Period

Inside `Period`:

- `StartDate` = **2026-03-16**  
  The policy holds for the season.
- `EndDate` = **2026-08-29**  
  Its end.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address; identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address; identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits); identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brightmarket Stores (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Brightmarket Stores**  
  The name under which the party is registered; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410411**  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `Contact/Name` = **Buying office**  
  The department that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits); identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **UL-1237398**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brackenmere Furniture (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Brackenmere Furniture**  
  The name under which the party is registered; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412466**  
  Number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Name` = **Trade sales**  
  The department that handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Item Management Profile

Inside `ItemManagementProfile`:

- `EffectivePeriod/StartDate` = **2026-03-16**  
  From the first delivery.
- `EffectivePeriod/EndDate` = **2026-08-29**  
  To the end of the season.
- `Item/Description` = **Garden bench and two chairs in hardwood, made for the department store's own line.**  
  The seller's description; item garden-set of Brackenmere Furniture (world/items.json).
- `Item/Name` = **Garden bench set Marrow**  
  The item's short name; item garden-set of Brackenmere Furniture (world/items.json).
- `Item/SellersItemIdentification/ID` = **BF-GS-01**  
  The seller's own item number; item garden-set of Brackenmere Furniture (world/items.json).
- `Item/StandardItemIdentification/ID` = **772020000079** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item garden-set of Brackenmere Furniture (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item garden-set of Brackenmere Furniture (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **9401.69** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item garden-set of Brackenmere Furniture (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TradeItemLocationProfile xmlns="urn:oasis:names:specification:ubl:schema:xsd:TradeItemLocationProfile-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>BS-DOC-26-0570</cbc:ID>
  <cbc:IssueDate>2026-03-14</cbc:IssueDate>
  <cac:Period>
    <cbc:StartDate>2026-03-16</cbc:StartDate>
    <cbc:EndDate>2026-08-29</cbc:EndDate>
  </cac:Period>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>CO-1231233</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Brightmarket Stores</cbc:RegistrationName>
      <cbc:CompanyID>20410411</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Buying office</cbc:Name>
      <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Joiners Row</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71203</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>UL-1237398</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Brackenmere Furniture</cbc:RegistrationName>
      <cbc:CompanyID>20412466</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Trade sales</cbc:Name>
      <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ItemManagementProfile>
    <cac:EffectivePeriod>
      <cbc:StartDate>2026-03-16</cbc:StartDate>
      <cbc:EndDate>2026-08-29</cbc:EndDate>
    </cac:EffectivePeriod>
    <cac:Item>
      <cbc:Description>Garden bench and two chairs in hardwood, made for the department store's own line.</cbc:Description>
      <cbc:Name>Garden bench set Marrow</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>BF-GS-01</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">772020000079</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">9401.69</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:ItemManagementProfile>
</TradeItemLocationProfile>
```
