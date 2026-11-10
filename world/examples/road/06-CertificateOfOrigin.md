# Certificate of Origin: Valdara Industries to Ferrano Chamber of Commerce

*Example 6 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Certificate of Origin in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CERTIFICATE-OF-ORIGIN-SCHEMA)*

The goods qualify for preferential duty in Bayvarra; the manufacturer applies to its chamber of commerce for a certificate of origin.

[The XML file](06-CertificateOfOrigin.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **FCC-CO-26-0157**  
  The number of the certificate, given by the chamber.
- `IssueDate` = **2026-03-20**  
  The day the exporter applies, before the goods leave.
- `Description` = **Certificate of origin for park benches and castings made in Urvania.**  
  What the certificate is for.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address; identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits); identity of Valdara Industries (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries**  
  The name under which the party is registered; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Contact/Name` = **Order desk**  
  The department that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits); identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution**  
  The name under which the party is registered; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `Contact/Name` = **Customer service**  
  The department that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Endorser Party

Inside `EndorserParty`:

- `RoleCode` = **Chamber**  
  The endorser is the chamber of commerce of the exporting country.
- `SequenceNumeric` = **1**  
  The first and only endorsement.
- `Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/StreetName` = **Piazza del Mercato**  
  Street of the postal address; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **XU007376017**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105370**  
  Number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Name` = **Certificates office**  
  The department that handles this document; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

### Certificate of Origin Application

Inside `CertificateOfOriginApplication`:

- `ReferenceID` = **VI-AP-26-0158**  
  The exporter's reference for its application.
- `CertificateType` = **Preferential**  
  The goods qualify for the preferential duty rate in Bayvarra; the importer needs this certificate to claim it.
- `ApplicationStatusCode` = **Submitted**  
  The exporter submits the application.
- `OriginalJobID` = **LD-PO-26-0149**  
  The order the goods are for.
- `Shipment/ID` = **CL-SH-26-0154**  
  The shipment the certificate covers.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **4790400** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **96** (unitCode `H87`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.**  
  The seller's description; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **71760** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `H87`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, cast steel, galvanised.**  
  The seller's description; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting**  
  The item's short name; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **VI-C180**  
  The seller's own item number; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **7325.99** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-casting of Valdara Industries (world/items.json).
- `EndorserParty/RoleCode` = **Chamber**  
  The endorser is the chamber of commerce of the exporting country.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.
- `PreparationParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PreparationParty/PartyName/Name` = **Valdara Industries**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `IssuingCountry/IdentificationCode` = **XU**  
  The goods were made in Urvania, and the certificate is issued there.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC-CO-26-0157**  
  The certificate this endorsement belongs to.
- `ApprovalStatus` = **Pending**  
  Not yet endorsed: the application is with the chamber.
- `EndorserParty/RoleCode` = **Chamber**  
  The endorser is the chamber of commerce of the exporting country.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CertificateOfOrigin xmlns="urn:oasis:names:specification:ubl:schema:xsd:CertificateOfOrigin-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>FCC-CO-26-0157</cbc:ID>
  <cbc:IssueDate>2026-03-20</cbc:IssueDate>
  <cbc:Description>Certificate of origin for park benches and castings made in Urvania.</cbc:Description>
  <cac:ExporterParty>
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
  </cac:ExporterParty>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>UL-1230822</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeway Distribution</cbc:RegistrationName>
      <cbc:CompanyID>20410274</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:EndorserParty>
    <cbc:RoleCode>Chamber</cbc:RoleCode>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Piazza del Mercato</cbc:StreetName>
        <cbc:BuildingNumber>15</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4110</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>XU007376017</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105370</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Certificates office</cbc:Name>
        <cbc:ElectronicMail>certificates@camera-ferrano.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105370</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
    <cac:SignatoryContact>
      <cbc:Name>Certificates office</cbc:Name>
    </cac:SignatoryContact>
  </cac:EndorserParty>
  <cac:CertificateOfOriginApplication>
    <cbc:ReferenceID>VI-AP-26-0158</cbc:ReferenceID>
    <cbc:CertificateType>Preferential</cbc:CertificateType>
    <cbc:ApplicationStatusCode>Submitted</cbc:ApplicationStatusCode>
    <cbc:OriginalJobID>LD-PO-26-0149</cbc:OriginalJobID>
    <cac:Shipment>
      <cbc:ID>CL-SH-26-0154</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Park bench Serra 180</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">4790400</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="H87">96</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>VI-B180</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Bench side frame casting</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">71760</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="H87">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Replacement side frame for the Serra bench, cast steel, galvanised.</cbc:Description>
          <cbc:Name>Bench side frame casting</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>VI-C180</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:ItemClassificationCode listID="HS">7325.99</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:Shipment>
    <cac:EndorserParty>
      <cbc:RoleCode>Chamber</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:PreparationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:PreparationParty>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:IssuingCountry>
      <cbc:IdentificationCode>XU</cbc:IdentificationCode>
    </cac:IssuingCountry>
  </cac:CertificateOfOriginApplication>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>FCC-CO-26-0157</cbc:DocumentID>
    <cbc:ApprovalStatus>Pending</cbc:ApprovalStatus>
    <cac:EndorserParty>
      <cbc:RoleCode>Chamber</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
  </cac:IssuerEndorsement>
</CertificateOfOrigin>
```
