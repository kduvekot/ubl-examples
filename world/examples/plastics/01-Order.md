# Order: Rivermouth Packaging to Rinova Recovery

*Example 1 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

A bulk lot of recycled granulate. Delivery terms CPT river quay: the seller books the barge.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **RP-PO-26-0882**  
  The buyer's order number.
- `IssueDate` = **2026-04-13**  
  The packaging maker orders for the next production run.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the seller's currency, in which the seller's prices are; it has no minor unit.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address; identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address; identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits); identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **CO-1238220**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging**  
  The name under which the party is registered; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412740**  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Name` = **Order desk**  
  The department that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via del Riciclo**  
  Street of the postal address; identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address; identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits); identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **XU007318479**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Rinova Recovery (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyLegalEntity/RegistrationName` = **Rinova Recovery**  
  The name under which the party is registered; identity of Rinova Recovery (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104548**  
  Number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/Name` = **Customer service**  
  The department that handles this document; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `DeliveryParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Rivermouth Packaging**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CPT** (schemeID `INCOTERMS`)  
  Carriage paid to the river quay: the seller books and pays the barge, the buyer bears the risk once the goods are on board.
- `DeliveryLocation/Description` = **River quay, Lumeport**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0** (currencyID `XUF`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **9984000** (currencyID `XUF`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0** (currencyID `XUF`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G**  
  Goods exported from Urvania: no value added tax is charged on an export (category G, free export item).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export of goods outside Urvania**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **9984000** (currencyID `XUF`)  
  The sum of the line amounts.
- `PayableAmount` = **9984000** (currencyID `XUF`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **120** (unitCode `TNE`)  
  One barge load of recycled granulate in jumbo bags.
- `LineItem/LineExtensionAmount` = **9984000** (currencyID `XUF`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **83200** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.**  
  The seller's description; item granulate-pe of Rinova Recovery (world/items.json).
- `LineItem/Item/Name` = **Recycled PE granulate**  
  The item's short name; item granulate-pe of Rinova Recovery (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **RR-PE-R1**  
  The seller's own item number; item granulate-pe of Rinova Recovery (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **771030000048** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item granulate-pe of Rinova Recovery (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item granulate-pe of Rinova Recovery (world/items.json).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **3901.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item granulate-pe of Rinova Recovery (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>RP-PO-26-0882</cbc:ID>
  <cbc:IssueDate>2026-04-13</cbc:IssueDate>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cac:BuyerCustomerParty>
    <cac:Party>
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
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
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
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CPT</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>River quay, Lumeport</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">0</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">9984000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">0</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Export of goods outside Urvania</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">9984000</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XUF">9984000</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XUF">9984000</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">83200</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
      </cac:Price>
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
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
