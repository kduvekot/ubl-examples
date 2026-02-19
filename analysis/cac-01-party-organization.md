# UBL Element Reference — Party & Organization

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **15** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [PartyType](#PartyType)
  - [BranchType](#BranchType)
  - [CapabilityType](#CapabilityType)
  - [ContactType](#ContactType)
  - [ContractingPartyType](#ContractingPartyType)
  - [CustomerPartyType](#CustomerPartyType)
  - [EconomicOperatorPartyType](#EconomicOperatorPartyType)
  - [EndorserPartyType](#EndorserPartyType)
  - [ParticipantPartyType](#ParticipantPartyType)
  - [PartyIdentificationType](#PartyIdentificationType)
  - [PartyLegalEntityType](#PartyLegalEntityType)
  - [PartyNameType](#PartyNameType)
  - [PartyTaxSchemeType](#PartyTaxSchemeType)
  - [PersonType](#PersonType)
  - [SupplierPartyType](#SupplierPartyType)

---

## cac Elements — Party & Organization

### `PartyType`

**Used as:** `cac:AgentParty` · `cac:BusinessParty` · `cac:CarrierParty` · `cac:ConsigneeParty` · `cac:ConsignorParty` · `cac:CustomsParty` · `cac:DeliveryParty` · `cac:DespatchParty` · `cac:ExporterParty` · `cac:ExportingGuarantorParty` · `cac:FinalDeliveryParty` · `cac:FreightForwarderParty` · `cac:GovernorParty` · `cac:HolderParty` · `cac:ImporterParty` · `cac:ImportingCustomsParty` · `cac:ImportingGuarantorParty` · `cac:InventoryReportingParty` · `cac:IssuerParty` · `cac:ManufacturerParty` · `cac:NotifierParty` · `cac:NotifyParty` · `cac:OriginatorParty` · `cac:Party` · `cac:PayeeParty` · `cac:ReceiverParty` · `cac:ReporterParty` · `cac:RepresentativeParty` · `cac:ResponsibleParty` · `cac:SenderParty` · `cac:SendingLogisticsOperatorParty` · `cac:SignatoryParty` · `cac:SourceIssuerParty` · `cac:TransitExporterParty` · `cac:TransportServiceProviderParty` · `cac:TransportUserParty` · `cac:WeighingParty`

_576 instances across 37 elements, with 111 unique structures_

**Structure 1** — 3 instances

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>North American Veeblefetzer</cbc:Name>
  </cac:PartyName>
</cac:Party>
```

**Structure 2** — 48 instances

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>6903148000007</cbc:ID>
  </cac:PartyIdentification>
</cac:Party>
```

**Structure 3** — 4 instances

```xml
<cac:DespatchParty>
  <cac:PartyName>
    <cbc:Name>Consortial</cbc:Name>
  </cac:PartyName>
</cac:DespatchParty>
```

**Structure 4** — 5 instances

```xml
<cac:SignatoryParty>
  <cac:PartyIdentification>
    <cbc:ID>MyParty</cbc:ID>
  </cac:PartyIdentification>
</cac:SignatoryParty>
```

**Structure 5** — 2 instances

```xml
<cac:AgentParty>
  <cac:PartyName>
    <cbc:Name>Ylermi Huisi 09-55555555</cbc:Name>
  </cac:PartyName>
</cac:AgentParty>
```

**Structure 6** — 4 instances

```xml
<cac:CustomsParty>
  <cac:PartyIdentification>
    <cbc:ID>0245442-8</cbc:ID>
  </cac:PartyIdentification>
</cac:CustomsParty>
```

**Structure 7** — 3 instances

```xml
<cac:IssuerParty>
  <cac:PartyIdentification>
    <cbc:ID>1</cbc:ID>
  </cac:PartyIdentification>
</cac:IssuerParty>
```

**Structure 8** — 6 instances

```xml
<cac:IssuerParty>
  <cac:PartyName>
    <cbc:Name>Boston Road</cbc:Name>
  </cac:PartyName>
</cac:IssuerParty>
```

**Structure 9** — 2 instances

```xml
<cac:NotifierParty>
  <cac:PartyIdentification>
    <cbc:ID>FI1234567-8</cbc:ID>
  </cac:PartyIdentification>
</cac:NotifierParty>
```

**Structure 10** — 1 instance

```xml
<cac:NotifyParty>
  <cbc:WebsiteURI>http://www.CONSIGNEE.no/statusreceptioninterface#2</cbc:WebsiteURI>
  <cac:PartyName>
    <cbc:Name>CONSIGNEE</cbc:Name>
  </cac:PartyName>
</cac:NotifyParty>
```

**Structure 11** — 1 instance

```xml
<cac:SenderParty>
  <cbc:IndustryClassificationCode>Public Rail Authorities</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>DB</cbc:Name>
  </cac:PartyName>
</cac:SenderParty>
```

**Structure 12** — 1 instance

```xml
<cac:SourceIssuerParty>
  <cbc:IndustryClassificationCode>Public Rail Authorities</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>DB</cbc:Name>
  </cac:PartyName>
</cac:SourceIssuerParty>
```

**Structure 13** — 4 instances

```xml
<cac:CarrierParty>
  <cac:PartyName>
    <cbc:Name>Keep On Trucking</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Telephone>+1 36222 33847</cbc:Telephone>
  </cac:Contact>
</cac:CarrierParty>
```

**Structure 14** — 1 instance

```xml
<cac:ReceiverParty>
  <cac:PartyIdentification>
    <cbc:ID>4058675698641</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Lisboa Harbour</cbc:Name>
  </cac:PartyName>
</cac:ReceiverParty>
```

**Structure 15** — 6 instances

```xml
<cac:OriginatorParty>
  <cac:PartyIdentification>
    <cbc:ID>EmployeeXXX</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Josef K.</cbc:Name>
  </cac:PartyName>
</cac:OriginatorParty>
```

**Structure 16** — 9 instances

```xml
<cac:Party>
  <cbc:EndpointID>7302347231111</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>SellerPartyID123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Moderna Produkter AB</cbc:Name>
  </cac:PartyName>
</cac:Party>
```

**Structure 17** — 8 instances

```xml
<cac:NotifyParty>
  <cbc:EndpointID>www.consignor.cn/statusnotifications/</cbc:EndpointID>
  <cac:PartyName>
    <cbc:Name>Consignor</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:ElectronicMail>someName@consignor.cn</cbc:ElectronicMail>
  </cac:Contact>
</cac:NotifyParty>
```

**Structure 18** — 2 instances

```xml
<cac:TransitExporterParty>
  <cac:PartyIdentification>
    <cbc:ID>1234567-8</cbc:ID>
  </cac:PartyIdentification>
  <cac:PhysicalLocation>
    <cac:Address>
      <cbc:CityName>Espoo</cbc:CityName>
    </cac:Address>
  </cac:PhysicalLocation>
</cac:TransitExporterParty>
```

**Structure 19** — 5 instances

```xml
<cac:PayeeParty>
  <cac:PartyIdentification>
    <cbc:ID>098740918237</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Ebeneser Scrooge Inc.</cbc:Name>
  </cac:PartyName>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>6411982340</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:PayeeParty>
```

**Structure 20** — 8 instances

```xml
<cac:CarrierParty>
  <cac:PartyName>
    <cbc:Name>United Airfreight</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:ID>Freight Bookings</cbc:ID>
    <cbc:Telephone>+1 3362 4788</cbc:Telephone>
    <cbc:ElectronicMail>bookings@unitedfreight.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:CarrierParty>
```

**Structure 21** — 1 instance

```xml
<cac:CarrierParty>
  <cac:PartyName>
    <cbc:Name>MAERSK</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+4598786765</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@maersk.dk</cbc:ElectronicMail>
  </cac:Contact>
</cac:CarrierParty>
```

**Structure 22** — 4 instances

```xml
<cac:TransportServiceProviderParty>
  <cac:PartyName>
    <cbc:Name>RAIL CARRIER</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>Anders Stock</cbc:Name>
    <cbc:Telephone>+4987676234</cbc:Telephone>
    <cbc:ElectronicMail>anders@RAILCARRIER.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:TransportServiceProviderParty>
```

**Structure 23** — 2 instances

```xml
<cac:AgentParty>
  <cac:PartyIdentification>
    <cbc:ID>FI1234569-8</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Huolitsija Oy</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>Tuula Tullaaja 02 13 4567</cbc:Name>
  </cac:Contact>
</cac:AgentParty>
```

**Structure 24** — 2 instances

```xml
<cac:GovernorParty>
  <cac:PartyName>
    <cbc:Name>OpenPEPPOL AISBL</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>Brussels</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>BE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:GovernorParty>
```

**Structure 25** — 9 instances

```xml
<cac:Party>
  <cbc:EndpointID>7300072311115</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>7300070011115</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyIdentification>
    <cbc:ID>PartyID123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Johnssons byggvaror</cbc:Name>
  </cac:PartyName>
</cac:Party>
```

**Structure 26** — 2 instances

```xml
<cac:Party>
  <cbc:EndpointID>01841111111111</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>5398000392577</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>FirstAgency</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>Ole Ellerbæk Madsen</cbc:Name>
  </cac:Contact>
</cac:Party>
```

**Structure 27** — 4 instances

```xml
<cac:DeliveryParty>
  <cac:PartyName>
    <cbc:Name>The Terminus</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>S Massiah</cbc:Name>
    <cbc:Telephone>+ 44 127 98876545</cbc:Telephone>
    <cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
    <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:DeliveryParty>
```

**Structure 28** — 1 instance

```xml
<cac:TransportServiceProviderParty>
  <cac:PartyName>
    <cbc:Name>CARRIER SERVICE LTD</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Telephone>+324005588588</cbc:Telephone>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>RAUL</cbc:FirstName>
    <cbc:FamilyName>GONZALES</cbc:FamilyName>
  </cac:Person>
</cac:TransportServiceProviderParty>
```

**Structure 29** — 1 instance

```xml
<cac:TransportUserParty>
  <cac:PartyName>
    <cbc:Name>CUSTOMER SERVICE LTD</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Telephone>+324488588578</cbc:Telephone>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>DAVID</cbc:FirstName>
    <cbc:FamilyName>VILLA</cbc:FamilyName>
  </cac:Person>
</cac:TransportUserParty>
```

**Structure 30** — 8 instances

```xml
<cac:Party>
  <cbc:EndpointID>9994567987654</cbc:EndpointID>
  <cac:PartyName>
    <cbc:Name>Buyer GmbH</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>Munchen</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:Party>
```

**Structure 31** — 2 instances

```xml
<cac:ConsigneeParty>
  <cac:PartyName>
    <cbc:Name>Yang Mei Electronic Ltd</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Export Str. 143</cbc:StreetName>
    <cbc:CityName>Yang Mei</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>TH</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ConsigneeParty>
```

**Structure 32** — 1 instance

```xml
<cac:ConsignorParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827000</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Disfruta</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+212687878763</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@disfruta.ma</cbc:ElectronicMail>
  </cac:Contact>
</cac:ConsignorParty>
```

**Structure 33** — 2 instances

```xml
<cac:ConsigneeParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Consignee</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+4987878763</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@consignee.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:ConsigneeParty>
```

**Structure 34** — 7 instances

```xml
<cac:SenderParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827641</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>NECOSS</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+49450557000</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@necoss.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:SenderParty>
```

**Structure 35** — 7 instances

```xml
<cac:ReceiverParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827641</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>NECOSS</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+49450557000</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@necoss.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReceiverParty>
```

**Structure 36** — 6 instances

```xml
<cac:TransportServiceProviderParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827641</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>NECOSS</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+49450557000</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@necoss.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:TransportServiceProviderParty>
```

**Structure 37** — 2 instances

```xml
<cac:TransportUserParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827000</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Consignor</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+8687878763</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@consignor.cn</cbc:ElectronicMail>
  </cac:Contact>
</cac:TransportUserParty>
```

**Structure 38** — 1 instance

```xml
<cac:SourceIssuerParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673821325</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ARRIVA</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+49450557888</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@arriva.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:SourceIssuerParty>
```

**Structure 39** — 1 instance

```xml
<cac:ReporterParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827641</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>D2D GmbH</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+49450557000</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@d2d.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReporterParty>
```

**Structure 40** — 2 instances

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>Supp123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Example Supplies Ltd.</cbc:Name>
  </cac:PartyName>
  <cac:PartyTaxScheme>
    <cbc:CompanyID>DK123456789</cbc:CompanyID>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
</cac:Party>
```

**Structure 41** — 3 instances

```xml
<cac:ConsigneeParty>
  <cac:PartyName>
    <cbc:Name>Automat AG</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Stahlstrass 5</cbc:StreetName>
    <cbc:CityName>Bern</cbc:CityName>
    <cbc:PostalZone>CH-3007</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ConsigneeParty>
```

**Structure 42** — 3 instances

```xml
<cac:ReceiverParty>
  <cbc:EndpointID>9994567987654</cbc:EndpointID>
  <cbc:IndustryClassificationCode>TR</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>La Spezia Container Terminal</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>La Spezia</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ReceiverParty>
```

**Structure 43** — 2 instances

```xml
<cac:DeliveryParty>
  <cac:PartyIdentification>
    <cbc:ID>67654328394567</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Swedish trucking</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Name>Per</cbc:Name>
    <cbc:Telephone>987098709</cbc:Telephone>
    <cbc:Telefax>34673435</cbc:Telefax>
    <cbc:ElectronicMail>bill@svetruck.se</cbc:ElectronicMail>
  </cac:Contact>
</cac:DeliveryParty>
```

**Structure 44** — 2 instances

```xml
<cac:AgentParty>
  <cac:PartyIdentification>
    <cbc:ID>DK10035643</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Told Service A/S</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Vesterbrogade</cbc:StreetName>
    <cbc:BuildingNumber>78</cbc:BuildingNumber>
    <cbc:CityName>København K</cbc:CityName>
    <cbc:PostalZone>1258</cbc:PostalZone>
  </cac:PostalAddress>
</cac:AgentParty>
```

**Structure 45** — 2 instances

```xml
<cac:ReceiverParty>
  <cbc:EndpointID>9994567987654</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>GB999999973</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>World Events Ltd.</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>London</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ReceiverParty>
```

**Structure 46** — 2 instances

```xml
<cac:BusinessParty>
  <cbc:EndpointID>9994567987654</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>GB999999973</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>World Events Ltd.</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>London</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:BusinessParty>
```

**Structure 47** — 2 instances

```xml
<cac:ImportingCustomsParty>
  <cac:PartyName>
    <cbc:Name>Zollamt</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Tollbrettkoppel</cbc:StreetName>
    <cbc:BuildingNumber>8</cbc:BuildingNumber>
    <cbc:CityName>Heiligenhafen</cbc:CityName>
    <cbc:PostalZone>23774</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ImportingCustomsParty>
```

**Structure 48** — 2 instances

```xml
<cac:ConsignorParty>
  <cac:PartyIdentification>
    <cbc:ID>4058673827000</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Consignor</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>4058673827000</cbc:ID>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+8676576456</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@consignor.cn</cbc:ElectronicMail>
  </cac:Contact>
</cac:ConsignorParty>
```

**Structure 49** — 2 instances

```xml
<cac:ConsignorParty>
  <cac:PartyIdentification>
    <cbc:ID>FI1234567-1</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Elektroniikka Oy</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Vastuskatu 12</cbc:StreetName>
    <cbc:CityName>Helsinki</cbc:CityName>
    <cbc:PostalZone>00140</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>FI</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ConsignorParty>
```

**Structure 50** — 1 instance

```xml
<cac:ConsignorParty>
  <cac:PartyIdentification>
    <cbc:ID>1080</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ExampleName</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>ExampleStreet</cbc:StreetName>
    <cbc:CityName>Viby J</cbc:CityName>
    <cbc:PostalZone>8260</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
</cac:ConsignorParty>
```

**Structure 51** — 2 instances

```xml
<cac:ConsignorParty>
  <cac:PartyName>
    <cbc:Name>AOO Tehnika</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Komsomolskaja pl., 158</cbc:StreetName>
    <cbc:CityName>Moskva</cbc:CityName>
    <cbc:PostalZone>107842</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>RU</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:AgentParty>
    <cac:PartyName>
      <cbc:Name>Ylermi Huisi 09-55555555</cbc:Name>
    </cac:PartyName>
  </cac:AgentParty>
</cac:ConsignorParty>
```

**Structure 52** — 1 instance

```xml
<cac:ConsigneeParty>
  <cac:PartyIdentification>
    <cbc:ID>0004424005</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ConsigneeExample</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>StreetName Example</cbc:StreetName>
    <cbc:AdditionalStreetName>AdditionalStreet Example</cbc:AdditionalStreetName>
    <cbc:CityName>El Dorado</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>PA</cbc:IdentificationCode>
      <cbc:Name>Panama</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
</cac:ConsigneeParty>
```

**Structure 53** — 2 instances

```xml
<cac:SenderParty>
  <cbc:EndpointID>1234567987654</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>DK12345678</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Papirøen Food ApS</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Trangravsvej</cbc:StreetName>
    <cbc:BuildingNumber>12</cbc:BuildingNumber>
    <cbc:CityName>Copenhagen</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:SenderParty>
```

**Structure 54** — 3 instances

```xml
<cac:WeighingParty>
  <cbc:IndustryClassificationCode>WPA</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>LEONARDO</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>La Spezia</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Person>
    <cbc:FirstName>GIORGIO</cbc:FirstName>
    <cbc:FamilyName>VERDI</cbc:FamilyName>
    <cbc:RoleCode>BN</cbc:RoleCode>
  </cac:Person>
</cac:WeighingParty>
```

**Structure 55** — 3 instances

```xml
<cac:ResponsibleParty>
  <cbc:IndustryClassificationCode>SPC</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>LEONARDO</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>La Spezia</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Person>
    <cbc:FirstName>STEFANO</cbc:FirstName>
    <cbc:FamilyName>ROSSI</cbc:FamilyName>
    <cbc:RoleCode>RP</cbc:RoleCode>
  </cac:Person>
</cac:ResponsibleParty>
```

**Structure 56** — 2 instances

```xml
<cac:CustomsParty>
  <cac:PartyIdentification>
    <cbc:ID>DK003102</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Toldstyrelsen</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Slet Parkvej</cbc:StreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:CityName>Nørre Alslev</cbc:CityName>
    <cbc:PostalZone>4840</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:CustomsParty>
```

**Structure 57** — 4 instances

```xml
<cac:ExportingGuarantorParty>
  <cac:PartyName>
    <cbc:Name>Dansk Erhverv</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Slotsholmsgade</cbc:StreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:CityName>København K</cbc:CityName>
    <cbc:PostalZone>1216</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>43232010</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:ExportingGuarantorParty>
```

**Structure 58** — 3 instances

```xml
<cac:ImportingGuarantorParty>
  <cac:PartyName>
    <cbc:Name>Deutscher Industrie- und Handelskammertag e.V.</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Breite Straße</cbc:StreetName>
    <cbc:BuildingNumber>29</cbc:BuildingNumber>
    <cbc:CityName>Berlin</cbc:CityName>
    <cbc:PostalZone>10178</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>DE122125278</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:ImportingGuarantorParty>
```

**Structure 59** — 1 instance

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>Dansk Industri</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>6916</cbc:ID>
    <cbc:StreetName>Vesterbrogade 1L, 1.sal</cbc:StreetName>
    <cbc:CityName>København V.</cbc:CityName>
    <cbc:PostalZone>1620</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>16077593</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:Party>
```

**Structure 60** — 3 instances

```xml
<cac:SenderParty>
  <cbc:EndpointID>1234567987654</cbc:EndpointID>
  <cbc:IndustryClassificationCode>CA</cbc:IndustryClassificationCode>
  <cac:PartyIdentification>
    <cbc:ID>XXX</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ACME Ltd.</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>One Hundred Road</cbc:StreetName>
    <cbc:BuildingNumber>100</cbc:BuildingNumber>
    <cbc:CityName>London</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:SenderParty>
```

**Structure 61** — 1 instance

```xml
<cac:SenderParty>
  <cac:PartyName>
    <cbc:Name>Declarant Inc</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Declarant Street</cbc:StreetName>
    <cbc:CityName>Declarant City</cbc:CityName>
    <cbc:PostalZone>Declarant Post Code</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>SomeName</cbc:Name>
    <cbc:Telephone>+49450557000</cbc:Telephone>
    <cbc:ElectronicMail>SomeName@d2d.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:SenderParty>
```

**Structure 62** — 1 instance

```xml
<cac:IssuerParty>
  <cac:PartyName>
    <cbc:Name>Dansk Industri</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>6916</cbc:ID>
    <cbc:StreetName>Vesterbrogade 1L, 1.sal</cbc:StreetName>
    <cbc:CityName>København V.</cbc:CityName>
    <cbc:PostalZone>1620</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>16077593</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:IssuerParty>
```

**Structure 63** — 2 instances

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>0987678321123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Moderna Produkter AB</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:Telephone>346788</cbc:Telephone>
    <cbc:Telefax>8567443</cbc:Telefax>
    <cbc:ElectronicMail>sven@moderna.se</cbc:ElectronicMail>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>Sven</cbc:FirstName>
    <cbc:FamilyName>Pereson</cbc:FamilyName>
    <cbc:MiddleName>N</cbc:MiddleName>
    <cbc:JobTitle>Stuffuser</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

**Structure 64** — 2 instances

```xml
<cac:SignatoryParty>
  <cac:PartyIdentification>
    <cbc:ID>8596</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Gedevang Mejeri</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Stribevangen</cbc:StreetName>
    <cbc:BuildingNumber>89</cbc:BuildingNumber>
    <cbc:CityName>Gedser</cbc:CityName>
    <cbc:PostalZone>4874</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>45789034</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:SignatoryParty>
```

**Structure 65** — 1 instance

```xml
<cac:HolderParty>
  <cac:PartyName>
    <cbc:Name>STEFCO A/S</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Industrivej 3</cbc:StreetName>
    <cbc:CityName>Ørum Djurs</cbc:CityName>
    <cbc:PostalZone>8586</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>DK89343487</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:Name>Andreas Andersen</cbc:Name>
  </cac:Contact>
</cac:HolderParty>
```

**Structure 66** — 2 instances

```xml
<cac:ConsignorParty>
  <cac:PartyIdentification>
    <cbc:ID>8596</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Gedevang Mejeri</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Stribevangen</cbc:StreetName>
    <cbc:BuildingNumber>89</cbc:BuildingNumber>
    <cbc:CityName>Gedser</cbc:CityName>
    <cbc:PostalZone>4874</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>45789034</cbc:CompanyID>
    <cbc:RegistrationDate>1957-08-13</cbc:RegistrationDate>
  </cac:PartyLegalEntity>
</cac:ConsignorParty>
```

**Structure 67** — 7 instances

```xml
<cac:FreightForwarderParty>
  <cac:PartyName>
    <cbc:Name>One-Stop Forwarders</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Postbox>99043</cbc:Postbox>
    <cbc:CityName>Boston</cbc:CityName>
    <cbc:PostalZone>02210</cbc:PostalZone>
    <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Con Solidador</cbc:Name>
    <cbc:Telephone>+1 343 1453654</cbc:Telephone>
    <cbc:Telefax>+1 343 1453655</cbc:Telefax>
    <cbc:ElectronicMail>ctanner@onestopfreight.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:FreightForwarderParty>
```

**Structure 68** — 1 instance

```xml
<cac:FreightForwarderParty>
  <cac:PartyIdentification>
    <cbc:ID>13234212</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Example Shipping</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Street</cbc:StreetName>
    <cbc:CityName>City</cbc:CityName>
    <cbc:PostalZone>Post</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>1323421212</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>11</cbc:ID>
  </cac:Contact>
</cac:FreightForwarderParty>
```

**Structure 69** — 2 instances

```xml
<cac:SenderParty>
  <cac:PartyIdentification>
    <cbc:ID>987654321</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>FORWARDER</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Schonestrasse 1</cbc:StreetName>
    <cbc:CityName>Munich</cbc:CityName>
    <cbc:PostalZone>80331</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Hans Weisser</cbc:Name>
    <cbc:Telephone>+4992894481</cbc:Telephone>
    <cbc:ElectronicMail>hans.weisser@FORWARDER.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:SenderParty>
```

**Structure 70** — 1 instance

```xml
<cac:ReceiverParty>
  <cac:PartyIdentification>
    <cbc:ID>987654321</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>FORWARDER</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Schonestrasse 1</cbc:StreetName>
    <cbc:CityName>Munich</cbc:CityName>
    <cbc:PostalZone>80331</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Hans Weisser</cbc:Name>
    <cbc:Telephone>+4992894481</cbc:Telephone>
    <cbc:ElectronicMail>hans.weisser@FORWARDER.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReceiverParty>
```

**Structure 71** — 1 instance

```xml
<cac:ManufacturerParty>
  <cbc:IndustryClassificationCode>Dairy</cbc:IndustryClassificationCode>
  <cac:PartyIdentification>
    <cbc:ID>M165</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ExampleName</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>ExampleStreet 1</cbc:StreetName>
    <cbc:CityName>Videbæk</cbc:CityName>
    <cbc:PostalZone>6920</cbc:PostalZone>
    <cac:AddressLine>
      <cbc:Line>ExampleStreet 1, DK-6920 Videbæk</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
</cac:ManufacturerParty>
```

**Structure 72** — 1 instance

```xml
<cac:IssuerParty>
  <cac:PartyName>
    <cbc:Name>ConsignorExample</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>ExampleStreet</cbc:StreetName>
    <cbc:CityName>Example City</cbc:CityName>
    <cbc:PostalZone>1234</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>DK12345678</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>8447</cbc:ID>
    <cbc:Name>Document Robot</cbc:Name>
  </cac:Contact>
</cac:IssuerParty>
```

**Structure 73** — 1 instance

```xml
<cac:RepresentativeParty>
  <cac:PartyName>
    <cbc:Name>Grenå Tools</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Højdevej 18</cbc:StreetName>
    <cbc:CityName>Grenå</cbc:CityName>
    <cbc:PostalZone>8500</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Person>
    <cbc:FirstName>Kirsten</cbc:FirstName>
    <cbc:FamilyName>Jensen</cbc:FamilyName>
    <cac:IdentityDocumentReference>
      <cbc:ID>325334535</cbc:ID>
    </cac:IdentityDocumentReference>
  </cac:Person>
</cac:RepresentativeParty>
```

**Structure 74** — 2 instances

```xml
<cac:SendingLogisticsOperatorParty>
  <cac:PartyName>
    <cbc:Name>One-Stop Forwarders</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Postbox>99043</cbc:Postbox>
    <cbc:CityName>Boston</cbc:CityName>
    <cbc:PostalZone>02210</cbc:PostalZone>
    <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Con Solidador</cbc:Name>
    <cbc:Telephone>+1 343 1453654</cbc:Telephone>
    <cbc:Telefax>+1 343 1453655</cbc:Telefax>
    <cbc:ElectronicMail>ctanner@onestopfreight.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:SendingLogisticsOperatorParty>
```

**Structure 75** — 2 instances

```xml
<cac:FreightForwarderParty>
  <cac:PartyIdentification>
    <ext:UBLExtensions>
      <ext:UBLExtension>
        <ext:ExtensionContent>
          <ext:IDExtension>T0002</ext:IDExtension>
        </ext:ExtensionContent>
      </ext:UBLExtension>
    </ext:UBLExtensions>
    <cbc:ID>FI1234567-8</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Huisin Huolinta Oy</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Tiilitie 5</cbc:StreetName>
    <cbc:CityName>Espoo</cbc:CityName>
    <cbc:PostalZone>02340</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>FI</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:FreightForwarderParty>
```

**Structure 76** — 10 instances

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>Arancio Forniture spa</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
    <cbc:BuildingNumber>403</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Rossi</cbc:Name>
    <cbc:Telephone>0039 051 23000000</cbc:Telephone>
    <cbc:Telefax>0039 051 23000023</cbc:Telefax>
    <cbc:ElectronicMail>rossi@arancioforniture.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

**Structure 77** — 1 instance

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>123456789</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Gadgets R Us, Inc.</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>High Street</cbc:StreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:CityName>Copenhagen</cbc:CityName>
    <cbc:PostalZone>1001</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:CompanyID>DK12345</cbc:CompanyID>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
</cac:Party>
```

**Structure 78** — 2 instances

```xml
<cac:SenderParty>
  <cac:PartyName>
    <cbc:Name>Beta Shop</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Via Emilia</cbc:StreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:CityName>Modena</cbc:CityName>
    <cbc:PostalZone>41121</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Delta</cbc:Name>
    <cbc:Telephone>0039 059 33000000</cbc:Telephone>
    <cbc:Telefax>0039 059 33000055</cbc:Telefax>
    <cbc:ElectronicMail>delta@betashop.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:SenderParty>
```

**Structure 79** — 1 instance

```xml
<cac:ReceiverParty>
  <cac:PartyName>
    <cbc:Name>Arancio Forniture spa</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
    <cbc:BuildingNumber>403</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Rossi</cbc:Name>
    <cbc:Telephone>0039 051 23000000</cbc:Telephone>
    <cbc:Telefax>0039 051 23000023</cbc:Telefax>
    <cbc:ElectronicMail>rossi@arancioforniture.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReceiverParty>
```

**Structure 80** — 2 instances

```xml
<cac:ReceiverParty>
  <cac:PartyIdentification>
    <cbc:ID>123456789</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>CONSIGNEE</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Postbox>456</cbc:Postbox>
    <cbc:StreetName>Jordbærstien 2</cbc:StreetName>
    <cbc:CityName>Hamar</cbc:CityName>
    <cbc:PostalZone>2321</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>NO</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Jon Persen</cbc:Name>
    <cbc:Telephone>+4793656656</cbc:Telephone>
    <cbc:ElectronicMail>jonp@CONSIGNEE.no</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReceiverParty>
```

**Structure 81** — 1 instance

```xml
<cac:ManufacturerParty>
  <cac:PartyName>
    <cbc:Name>AZ Outsourcing srl</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Via Bolognese</cbc:StreetName>
    <cbc:BuildingNumber>199</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Verdi</cbc:Name>
    <cbc:Telephone>0039 051 25400000</cbc:Telephone>
    <cbc:Telefax>0039 051 25400023</cbc:Telefax>
    <cbc:ElectronicMail>verdi@azoutsourcing.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:ManufacturerParty>
```

**Structure 82** — 1 instance

```xml
<cac:TransportUserParty>
  <cac:PartyIdentification>
    <cbc:ID>123456789</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>CONSIGNEE</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Postbox>456</cbc:Postbox>
    <cbc:StreetName>Jordbærstien 2</cbc:StreetName>
    <cbc:CityName>Hamar</cbc:CityName>
    <cbc:PostalZone>2321</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>NO</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Jon Persen</cbc:Name>
    <cbc:Telephone>+4793656656</cbc:Telephone>
    <cbc:ElectronicMail>jonp@CONSIGNEE.no</cbc:ElectronicMail>
  </cac:Contact>
</cac:TransportUserParty>
```

**Structure 83** — 1 instance

```xml
<cac:ConsignorParty>
  <cac:PartyIdentification>
    <cbc:ID>1234</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ConsignorExample</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>ExampleStreet</cbc:StreetName>
    <cbc:CityName>Example City</cbc:CityName>
    <cbc:PostalZone>1234</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>DK12345678</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>8447</cbc:ID>
    <cbc:Name>Document Robot</cbc:Name>
  </cac:Contact>
</cac:ConsignorParty>
```

**Structure 84** — 2 instances

```xml
<cac:ConsigneeParty>
  <cac:PartyIdentification>
    <cbc:ID>STD14037</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Coop Extra Bergen</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Marken</cbc:StreetName>
    <cbc:BuildingNumber>13</cbc:BuildingNumber>
    <cbc:CityName>Bergen</cbc:CityName>
    <cbc:PostalZone>5017</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>NO</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>945030345</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>1928</cbc:ID>
    <cbc:Name>*ULLA GJERSTRUP</cbc:Name>
  </cac:Contact>
</cac:ConsigneeParty>
```

**Structure 85** — 2 instances

```xml
<cac:InventoryReportingParty>
  <cac:PartyName>
    <cbc:Name>Arancio Forniture spa</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
    <cbc:BuildingNumber>405</cbc:BuildingNumber>
    <cbc:Department>Sales and Planning Department</cbc:Department>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Bianchi</cbc:Name>
    <cbc:Telephone>0039 051 23000008</cbc:Telephone>
    <cbc:Telefax>0039 051 23000025</cbc:Telefax>
    <cbc:ElectronicMail>bianchi@arancioforniture.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:InventoryReportingParty>
```

**Structure 86** — 7 instances

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>Consortial</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Boston Road</cbc:StreetName>
    <cbc:BuildingName>Suite M-102</cbc:BuildingName>
    <cbc:BuildingNumber>630</cbc:BuildingNumber>
    <cbc:CityName>Billerica</cbc:CityName>
    <cbc:PostalZone>01821</cbc:PostalZone>
    <cbc:CountrySubentity>Massachusetts</cbc:CountrySubentity>
    <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mrs Bouquet</cbc:Name>
    <cbc:Telephone>+1 158 1233714</cbc:Telephone>
    <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
    <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

**Structure 87** — 9 instances

```xml
<cac:ConsignorParty>
  <cac:PartyName>
    <cbc:Name>Consortial</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Boston Road</cbc:StreetName>
    <cbc:BuildingName>Suite M-102</cbc:BuildingName>
    <cbc:BuildingNumber>630</cbc:BuildingNumber>
    <cbc:CityName>Billerica</cbc:CityName>
    <cbc:PostalZone>01821</cbc:PostalZone>
    <cbc:CountrySubentity>Massachusetts</cbc:CountrySubentity>
    <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mrs Bouquet</cbc:Name>
    <cbc:Telephone>+1 158 1233714</cbc:Telephone>
    <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
    <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:ConsignorParty>
```

**Structure 88** — 2 instances

```xml
<cac:InventoryReportingParty>
  <cac:PartyName>
    <cbc:Name>Beta Shop</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Floor>2</cbc:Floor>
    <cbc:Room>309</cbc:Room>
    <cbc:StreetName>Via Emilia</cbc:StreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:CityName>Modena</cbc:CityName>
    <cbc:PostalZone>41121</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Gamma</cbc:Name>
    <cbc:Telephone>0039 059 33000022</cbc:Telephone>
    <cbc:Telefax>0039 059 33000057</cbc:Telefax>
    <cbc:ElectronicMail>gamma@betashop.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:InventoryReportingParty>
```

**Structure 89** — 1 instance

```xml
<cac:TransportServiceProviderParty>
  <cac:PartyIdentification>
    <cbc:ID>987654321</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>FORWARDER</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Schonestrasse 1</cbc:StreetName>
    <cbc:CityName>Munich</cbc:CityName>
    <cbc:PostalZone>80331</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Hans Weisser</cbc:Name>
    <cbc:Telephone>+4992894481</cbc:Telephone>
    <cbc:ElectronicMail>hans.weisser@FORWARDER.de</cbc:ElectronicMail>
  </cac:Contact>
  <cac:FinancialAccount>
    <cbc:ID>8601.12.11189</cbc:ID>
    <cbc:PaymentNote>Deutsche Bank</cbc:PaymentNote>
  </cac:FinancialAccount>
</cac:TransportServiceProviderParty>
```

**Structure 90** — 7 instances

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>IYT Corporation</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Avon Way</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Bridgtow</cbc:CityName>
    <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
    <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>3rd Floor, Room 5</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Fred Churchill</cbc:Name>
    <cbc:Telephone>+44 127 2653214</cbc:Telephone>
    <cbc:Telefax>+44 127 2653215</cbc:Telefax>
    <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

**Structure 91** — 10 instances

```xml
<cac:ConsigneeParty>
  <cac:PartyName>
    <cbc:Name>IYT Corporation</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Avon Way</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Bridgtow</cbc:CityName>
    <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
    <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>3rd Floor, Room 5</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Fred Churchill</cbc:Name>
    <cbc:Telephone>+44 127 2653214</cbc:Telephone>
    <cbc:Telefax>+44 127 2653215</cbc:Telefax>
    <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:ConsigneeParty>
```

**Structure 92** — 8 instances

```xml
<cac:NotifyParty>
  <cac:PartyName>
    <cbc:Name>IYT Corporation</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Avon Way</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Bridgtow</cbc:CityName>
    <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
    <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>3rd Floor, Room 5</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Fred Churchill</cbc:Name>
    <cbc:Telephone>+44 127 2653214</cbc:Telephone>
    <cbc:Telefax>+44 127 2653215</cbc:Telefax>
    <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:NotifyParty>
```

**Structure 93** — 8 instances

```xml
<cac:FinalDeliveryParty>
  <cac:PartyName>
    <cbc:Name>The Terminus</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Avon Way</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Bridgtow</cbc:CityName>
    <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
    <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>3rd Floor, Room 5</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>S Massiah</cbc:Name>
    <cbc:Telephone>+ 44 127 98876545</cbc:Telephone>
    <cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
    <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:FinalDeliveryParty>
```

**Structure 94** — 1 instance

```xml
<cac:ReceiverParty>
  <cac:PartyName>
    <cbc:Name>Arancio Forniture spa</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Floor>5</cbc:Floor>
    <cbc:Room>29</cbc:Room>
    <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
    <cbc:BuildingNumber>403</cbc:BuildingNumber>
    <cbc:Department>Marketing Office</cbc:Department>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:Contact>
    <cbc:Name>Mr Rossi</cbc:Name>
    <cbc:Telephone>0039 051 23000000</cbc:Telephone>
    <cbc:Telefax>0039 051 23000023</cbc:Telefax>
    <cbc:ElectronicMail>rossi@arancioforniture.it</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReceiverParty>
```

**Structure 95** — 2 instances

```xml
<cac:ImporterParty>
  <cac:PartyIdentification>
    <cbc:ID>FI1234567-1</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Elektroniikka Oy</cbc:Name>
  </cac:PartyName>
  <cac:Language>
    <cbc:ID>fi</cbc:ID>
  </cac:Language>
  <cac:PostalAddress>
    <cbc:StreetName>Vastuskatu 12</cbc:StreetName>
    <cbc:CityName>Helsinki</cbc:CityName>
    <cbc:PostalZone>00140</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>FI</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:AgentParty>
    <cac:PartyIdentification>
      <cbc:ID>FI1234569-8</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Huolitsija Oy</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>Tuula Tullaaja 02 13 4567</cbc:Name>
    </cac:Contact>
  </cac:AgentParty>
</cac:ImporterParty>
```

**Structure 96** — 2 instances

```xml
<cac:Party>
  <cbc:EndpointID>DK18296799</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>DK18296799</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Delcomputer A/S</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
    <cbc:StreetName>Arne Jacobsens Allé</cbc:StreetName>
    <cbc:BuildingNumber>15</cbc:BuildingNumber>
    <cbc:CityName>København S</cbc:CityName>
    <cbc:PostalZone>2300</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:CompanyID>DK18296799</cbc:CompanyID>
    <cac:TaxScheme>
      <cbc:ID>63</cbc:ID>
      <cbc:Name>Moms</cbc:Name>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
    <cbc:CompanyID>18296799</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:Party>
```

**Structure 97** — 1 instance

```xml
<cac:Party>
  <cbc:WebsiteURI>http://super.company.dk</cbc:WebsiteURI>
  <cbc:EndpointID>01842222222222</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>5790000127777</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>SuperCompany</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:AddressFormatCode>Structured</cbc:AddressFormatCode>
    <cbc:StreetName>Korsbygade 34</cbc:StreetName>
    <cbc:CityName>Aalborg</cbc:CityName>
    <cbc:PostalZone>9000</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>SuperCompany</cbc:RegistrationName>
    <cbc:CompanyID>DK59873677</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>7778</cbc:ID>
    <cbc:Name>Ole Hansen</cbc:Name>
    <cbc:Telephone>4526532147</cbc:Telephone>
    <cbc:Telefax>4526532146</cbc:Telefax>
    <cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

**Structure 98** — 1 instance

```xml
<cac:Party>
  <cbc:WebsiteURI>http://super.company.dk</cbc:WebsiteURI>
  <cbc:EndpointID>01842222222222</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>5790000127777</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>SuperCompany</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:AddressFormatCode>Structured</cbc:AddressFormatCode>
    <cbc:StreetName>Korsbygade 34</cbc:StreetName>
    <cbc:CityName>Aalborg</cbc:CityName>
    <cbc:PostalZone>9000</cbc:PostalZone>
    <cbc:CountrySubentity></cbc:CountrySubentity>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>SuperCompany</cbc:RegistrationName>
    <cbc:CompanyID>DK59873677</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>7778</cbc:ID>
    <cbc:Name>Ole Hansen</cbc:Name>
    <cbc:Telephone>4526532147</cbc:Telephone>
    <cbc:Telefax>4526532146</cbc:Telefax>
    <cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

**Structure 99** — 2 instances

```xml
<cac:ExporterParty>
  <cac:PartyIdentification>
    <cbc:ID>8596</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Gedevang Mejeri</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Stribevangen</cbc:StreetName>
    <cbc:BuildingNumber>89</cbc:BuildingNumber>
    <cbc:CityName>Gedser</cbc:CityName>
    <cbc:PostalZone>4874</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:CompanyID>45789034</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:AgentParty>
    <cac:PartyIdentification>
      <cbc:ID>DK10035643</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Told Service A/S</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Vesterbrogade</cbc:StreetName>
      <cbc:BuildingNumber>78</cbc:BuildingNumber>
      <cbc:CityName>København K</cbc:CityName>
      <cbc:PostalZone>1258</cbc:PostalZone>
    </cac:PostalAddress>
  </cac:AgentParty>
</cac:ExporterParty>
```

**Structure 100** — 2 instances

```xml
<cac:Party>
  <cbc:EndpointID>5798000416604</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>5798000416604</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Gentofte Kommune</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
    <cbc:StreetName>Bernstorffsvej</cbc:StreetName>
    <cbc:BuildingNumber>161</cbc:BuildingNumber>
    <cbc:CityName>Charlottenlund</cbc:CityName>
    <cbc:PostalZone>2920</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:CompanyID>DK12345678</cbc:CompanyID>
    <cac:TaxScheme>
      <cbc:ID>63</cbc:ID>
      <cbc:Name>Moms</cbc:Name>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>Gentofte Kommune</cbc:RegistrationName>
    <cbc:CompanyID>DK12345678</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:ID>12345678</cbc:ID>
    <cbc:Name>Sille Schyberg</cbc:Name>
  </cac:Contact>
</cac:Party>
```

**Structure 101** — 151 instances

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>The Terminus</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Avon Way</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Bridgtow</cbc:CityName>
    <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
    <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>3rd Floor, Room 5</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
    <cbc:CompanyID>12356478</cbc:CompanyID>
    <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
    <cac:TaxScheme>
      <cbc:ID>UK VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:Contact>
    <cbc:Name>S Massiah</cbc:Name>
    <cbc:Telephone>0127 98876545</cbc:Telephone>
    <cbc:Telefax>0127 98876546</cbc:Telefax>
    <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

**Structure 102** — 10 instances

```xml
<cac:PayeeParty>
  <cac:PartyName>
    <cbc:Name>Consortial</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Busy Street</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Farthing</cbc:CityName>
    <cbc:PostalZone>AA99 1BB</cbc:PostalZone>
    <cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>The Roundabout</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
    <cbc:CompanyID>175 269 2355</cbc:CompanyID>
    <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:Contact>
    <cbc:Name>Mrs Bouquet</cbc:Name>
    <cbc:Telephone>0158 1233714</cbc:Telephone>
    <cbc:Telefax>0158 1233856</cbc:Telefax>
    <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:PayeeParty>
```

**Structure 103** — 24 instances

```xml
<cac:SenderParty>
  <cac:PartyIdentification>
    <cbc:ID>6903148000007</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Consortial</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Busy Street</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Farthing</cbc:CityName>
    <cbc:PostalZone>AA99 1BB</cbc:PostalZone>
    <cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>The Roundabout</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:RegistrationName>Farthing Purchasing Consortium</cbc:RegistrationName>
    <cbc:CompanyID>175 269 2355</cbc:CompanyID>
    <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:Contact>
    <cbc:Name>Mrs Bouquet</cbc:Name>
    <cbc:Telephone>0158 1233714</cbc:Telephone>
    <cbc:Telefax>0158 1233856</cbc:Telefax>
    <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:SenderParty>
```

**Structure 104** — 24 instances

```xml
<cac:ReceiverParty>
  <cac:PartyIdentification>
    <cbc:ID>2203148000007</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>IYT Corporation</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Avon Way</cbc:StreetName>
    <cbc:BuildingName>Thereabouts</cbc:BuildingName>
    <cbc:BuildingNumber>56A</cbc:BuildingNumber>
    <cbc:CityName>Bridgtow</cbc:CityName>
    <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
    <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>3rd Floor, Room 5</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
    <cbc:CompanyID>12356478</cbc:CompanyID>
    <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
    <cac:TaxScheme>
      <cbc:ID>UK VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:Contact>
    <cbc:Name>Mr Fred Churchill</cbc:Name>
    <cbc:Telephone>0127 2653214</cbc:Telephone>
    <cbc:Telefax>0127 2653215</cbc:Telefax>
    <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:ReceiverParty>
```

**Structure 105** — 2 instances

```xml
<cac:Party>
  <cbc:EndpointID>7302347231111</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>SellerPartyID123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Moderna Produkter AB</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>0987654321123</cbc:ID>
    <cbc:Postbox>321</cbc:Postbox>
    <cbc:StreetName>Kungsgatan</cbc:StreetName>
    <cbc:AdditionalStreetName>suite12</cbc:AdditionalStreetName>
    <cbc:BuildingNumber>22</cbc:BuildingNumber>
    <cbc:Department>Sales department</cbc:Department>
    <cbc:CityName>Stockholm</cbc:CityName>
    <cbc:PostalZone>11000</cbc:PostalZone>
    <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
    <cac:Country>
      <cbc:IdentificationCode>SE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>Moderna Produkter AB</cbc:RegistrationName>
    <cbc:CompanyID>5532332283</cbc:CompanyID>
    <cac:RegistrationAddress>
      <cbc:CityName>Stockholm</cbc:CityName>
      <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>SE</cbc:IdentificationCode>
      </cac:Country>
    </cac:RegistrationAddress>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:Telephone>34557</cbc:Telephone>
    <cbc:Telefax>3456767</cbc:Telefax>
    <cbc:ElectronicMail>lars@moderna.se</cbc:ElectronicMail>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>Lars</cbc:FirstName>
    <cbc:FamilyName>Petersen</cbc:FamilyName>
    <cbc:MiddleName>M</cbc:MiddleName>
    <cbc:JobTitle>Sales manager</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

**Structure 106** — 7 instances

```xml
<cac:Party>
  <cbc:EndpointID>1234567890123</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>Supp123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Salescompany ltd.</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>1231412341324</cbc:ID>
    <cbc:Postbox>5467</cbc:Postbox>
    <cbc:StreetName>Main street</cbc:StreetName>
    <cbc:AdditionalStreetName>Suite 123</cbc:AdditionalStreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:Department>Revenue department</cbc:Department>
    <cbc:CityName>Big city</cbc:CityName>
    <cbc:PostalZone>54321</cbc:PostalZone>
    <cbc:CountrySubentityCode>RegionA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:CompanyID>DK12345</cbc:CompanyID>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>The Sellercompany Incorporated</cbc:RegistrationName>
    <cbc:CompanyID>5402697509</cbc:CompanyID>
    <cac:RegistrationAddress>
      <cbc:CityName>Big city</cbc:CityName>
      <cbc:CountrySubentity>RegionA</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:RegistrationAddress>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:Telephone>4621230</cbc:Telephone>
    <cbc:Telefax>4621231</cbc:Telefax>
    <cbc:ElectronicMail>antonio@salescompany.dk</cbc:ElectronicMail>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>Antonio</cbc:FirstName>
    <cbc:FamilyName>M</cbc:FamilyName>
    <cbc:MiddleName>Salemacher</cbc:MiddleName>
    <cbc:JobTitle>Sales manager</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

**Structure 107** — 7 instances

```xml
<cac:Party>
  <cbc:EndpointID>1234567987654</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>345KS5324</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Buyercompany ltd</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>1238764941386</cbc:ID>
    <cbc:Postbox>123</cbc:Postbox>
    <cbc:StreetName>Anystreet</cbc:StreetName>
    <cbc:AdditionalStreetName>Back door</cbc:AdditionalStreetName>
    <cbc:BuildingNumber>8</cbc:BuildingNumber>
    <cbc:Department>Accounting department</cbc:Department>
    <cbc:CityName>Anytown</cbc:CityName>
    <cbc:PostalZone>101</cbc:PostalZone>
    <cbc:CountrySubentity>RegionB</cbc:CountrySubentity>
    <cac:Country>
      <cbc:IdentificationCode>BE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:CompanyID>BE54321</cbc:CompanyID>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>The buyercompany inc.</cbc:RegistrationName>
    <cbc:CompanyID>5645342123</cbc:CompanyID>
    <cac:RegistrationAddress>
      <cbc:CityName>Mainplace</cbc:CityName>
      <cbc:CountrySubentity>RegionB</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>BE</cbc:IdentificationCode>
      </cac:Country>
    </cac:RegistrationAddress>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:Telephone>5121230</cbc:Telephone>
    <cbc:Telefax>5121231</cbc:Telefax>
    <cbc:ElectronicMail>john@buyercompany.eu</cbc:ElectronicMail>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>John</cbc:FirstName>
    <cbc:FamilyName>X</cbc:FamilyName>
    <cbc:MiddleName>Doe</cbc:MiddleName>
    <cbc:JobTitle>Purchasing manager</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

**Structure 108** — 1 instance

```xml
<cac:TransportServiceProviderParty>
  <cbc:WebsiteURI>www.ROADCARRIER.de</cbc:WebsiteURI>
  <cac:PartyIdentification>
    <cbc:ID>1236541</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>ROAD CARRIER</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:Postbox>148</cbc:Postbox>
    <cbc:StreetName>Blumestrasse 3</cbc:StreetName>
    <cbc:MarkAttention>Peter Janssen</cbc:MarkAttention>
    <cbc:CityName>Munich</cbc:CityName>
    <cbc:PostalZone>28001</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      <cbc:Name>Germany</cbc:Name>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PhysicalLocation>
    <cbc:ID>89767764</cbc:ID>
    <cac:Address>
      <cbc:StreetName>Blumestrasse 3</cbc:StreetName>
      <cbc:CityName>Munich</cbc:CityName>
      <cac:AddressLine>
        <cbc:Line>Customer entrance from the street</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        <cbc:Name>Germany</cbc:Name>
      </cac:Country>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure>53.4</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure>33</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode>North</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure>8.48</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure>27</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode>East</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:Address>
  </cac:PhysicalLocation>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>ROAD CARRIER GmbH</cbc:RegistrationName>
    <cbc:CompanyID>989987876</cbc:CompanyID>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:Name>Peter Janssen</cbc:Name>
    <cbc:Telephone>+4987675432</cbc:Telephone>
    <cbc:Telefax>+4987675431</cbc:Telefax>
    <cbc:ElectronicMail>peter@ROADCARRIER.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:TransportServiceProviderParty>
```

**Structure 109** — 2 instances

```xml
<cac:Party>
  <cbc:EndpointID>7300072311115</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>7300070011115</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyIdentification>
    <cbc:ID>PartyID123</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Johnssons byggvaror</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:ID>1234567890123</cbc:ID>
    <cbc:Postbox>PoBox123</cbc:Postbox>
    <cbc:StreetName>Rådhusgatan</cbc:StreetName>
    <cbc:AdditionalStreetName>2nd floor</cbc:AdditionalStreetName>
    <cbc:BuildingNumber>5</cbc:BuildingNumber>
    <cbc:Department>Purchasing department</cbc:Department>
    <cbc:CityName>Stockholm</cbc:CityName>
    <cbc:PostalZone>11000</cbc:PostalZone>
    <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
    <cac:Country>
      <cbc:IdentificationCode>SE</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PartyTaxScheme>
    <cbc:RegistrationName>Herra Johnssons byggvaror AS</cbc:RegistrationName>
    <cbc:CompanyID>SE1234567801</cbc:CompanyID>
    <cac:RegistrationAddress>
      <cbc:CityName>Stockholm</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>SE</cbc:IdentificationCode>
      </cac:Country>
    </cac:RegistrationAddress>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:PartyTaxScheme>
  <cac:PartyLegalEntity>
    <cbc:RegistrationName>Johnssons Byggvaror AB</cbc:RegistrationName>
    <cbc:CompanyID>5532331183</cbc:CompanyID>
    <cac:RegistrationAddress>
      <cbc:CityName>Stockholm</cbc:CityName>
      <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>SE</cbc:IdentificationCode>
      </cac:Country>
    </cac:RegistrationAddress>
  </cac:PartyLegalEntity>
  <cac:Contact>
    <cbc:Telephone>123456</cbc:Telephone>
    <cbc:Telefax>123456</cbc:Telefax>
    <cbc:ElectronicMail>pelle@johnsson.se</cbc:ElectronicMail>
  </cac:Contact>
  <cac:Person>
    <cbc:FirstName>Pelle</cbc:FirstName>
    <cbc:FamilyName>Svensson</cbc:FamilyName>
    <cbc:MiddleName>X</cbc:MiddleName>
    <cbc:JobTitle>Boss</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

**Structure 110** — 1 instance

```xml
<cac:SenderParty>
  <cbc:WebsiteURI>https://www.oasis-open.org</cbc:WebsiteURI>
  <cbc:LogoReferenceID>https://www.oasis-open.org/sites/www.oasis-open.org/files/logo.png</cbc:LogoReferenceID>
  <cac:PartyName>
    <cbc:Name>OASIS</cbc:Name>
  </cac:PartyName>
  <cac:PartyName>
    <cbc:Name>Organization for the Advancement of Structured Information Standards</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Corporate Drive Suite 150</cbc:StreetName>
    <cbc:BuildingNumber>35</cbc:BuildingNumber>
    <cbc:CityName>Burlington</cbc:CityName>
    <cbc:PostalZone>01803-4238</cbc:PostalZone>
    <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
  <cac:PhysicalLocation>
    <cbc:InformationURI>https://goo.gl/maps/2k242</cbc:InformationURI>
  </cac:PhysicalLocation>
  <cac:Contact>
    <cbc:ID>1</cbc:ID>
    <cbc:Telephone>+1 781 425 5073</cbc:Telephone>
    <cbc:Telefax>+1 781 425 5072</cbc:Telefax>
    <cbc:ElectronicMail>info@oasis-open.org</cbc:ElectronicMail>
  </cac:Contact>
  <cac:AdditionalWebSite>
    <cbc:ID>1</cbc:ID>
    <cbc:Name>RSS</cbc:Name>
    <cbc:URI>https://www.oasis-open.org/feed</cbc:URI>
  </cac:AdditionalWebSite>
  <cac:SocialMediaProfile>
    <cbc:ID>1</cbc:ID>
    <cbc:Name>LinkedIN</cbc:Name>
    <cbc:SocialMediaTypeCode>Business</cbc:SocialMediaTypeCode>
    <cbc:URI>https://www.linkedin.com/company/oasis</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>2</cbc:ID>
    <cbc:Name>Twitter</cbc:Name>
    <cbc:URI>http://twitter.com/OASISopen</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>3</cbc:ID>
    <cbc:Name>Facebook</cbc:Name>
    <cbc:URI>http://facebook.com/oasis.open</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>4</cbc:ID>
    <cbc:Name>YouTube</cbc:Name>
    <cbc:URI>http://www.youtube.com/oasisopen</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>5</cbc:ID>
    <cbc:Name>Google+</cbc:Name>
    <cbc:URI>https://plus.google.com/+Oasis-openOrg</cbc:URI>
  </cac:SocialMediaProfile>
</cac:SenderParty>
```

**Structure 111** — 1 instance

```xml
<cac:SenderParty>
  <cbc:WebsiteURI>https://www.oasis-open.org</cbc:WebsiteURI>
  <cbc:LogoReferenceID>https://www.oasis-open.org/sites/www.oasis-open.org/files/logo.png</cbc:LogoReferenceID>
  <cac:PartyName>
    <cbc:Name>OASIS</cbc:Name>
  </cac:PartyName>
  <cac:PartyName>
    <cbc:Name>Organization for the Advancement of Structured Information Standards</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:StreetName>Corporate Drive Suite 150</cbc:StreetName>
    <cbc:BuildingNumber>35</cbc:BuildingNumber>
    <cbc:CityName>Burlington</cbc:CityName>
    <cbc:PostalZone>01803-4238</cbc:PostalZone>
    <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
    <cac:Country>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:Country>
    <cac:LocationCoordinate></cac:LocationCoordinate>
  </cac:PostalAddress>
  <cac:PhysicalLocation>
    <cbc:InformationURI>https://goo.gl/maps/2k242</cbc:InformationURI>
  </cac:PhysicalLocation>
  <cac:Contact>
    <cbc:ID>1</cbc:ID>
    <cbc:Telephone>+1 781 425 5073</cbc:Telephone>
    <cbc:Telefax>+1 781 425 5072</cbc:Telefax>
    <cbc:ElectronicMail>info@oasis-open.org</cbc:ElectronicMail>
  </cac:Contact>
  <cac:AdditionalWebSite>
    <cbc:ID>1</cbc:ID>
    <cbc:Name>RSS</cbc:Name>
    <cbc:URI>https://www.oasis-open.org/feed</cbc:URI>
  </cac:AdditionalWebSite>
  <cac:SocialMediaProfile>
    <cbc:ID>1</cbc:ID>
    <cbc:Name>LinkedIN</cbc:Name>
    <cbc:SocialMediaTypeCode>Business</cbc:SocialMediaTypeCode>
    <cbc:URI>https://www.linkedin.com/company/oasis</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>2</cbc:ID>
    <cbc:Name>Twitter</cbc:Name>
    <cbc:URI>http://twitter.com/OASISopen</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>3</cbc:ID>
    <cbc:Name>Facebook</cbc:Name>
    <cbc:URI>http://facebook.com/oasis.open</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>4</cbc:ID>
    <cbc:Name>YouTube</cbc:Name>
    <cbc:URI>http://www.youtube.com/oasisopen</cbc:URI>
  </cac:SocialMediaProfile>
  <cac:SocialMediaProfile>
    <cbc:ID>5</cbc:ID>
    <cbc:Name>Google+</cbc:Name>
    <cbc:URI>https://plus.google.com/+Oasis-openOrg</cbc:URI>
  </cac:SocialMediaProfile>
</cac:SenderParty>
```

[↑ Back to contents](#contents)

### `BranchType`

**Used as:** `cac:FinancialInstitutionBranch`

_36 instances across 1 element, with 2 unique structures_

**Structure 1** — 3 instances

```xml
<cac:FinancialInstitutionBranch>
  <cac:FinancialInstitution>
    <cbc:ID>DKDKABCD</cbc:ID>
  </cac:FinancialInstitution>
</cac:FinancialInstitutionBranch>
```

**Structure 2** — 33 instances

```xml
<cac:FinancialInstitutionBranch>
  <cbc:ID>10-26-58</cbc:ID>
  <cbc:Name>Open Bank Ltd, Bridgstow Branch</cbc:Name>
  <cac:FinancialInstitution>
    <cbc:ID>10-26-58</cbc:ID>
    <cbc:Name>Open Bank Ltd</cbc:Name>
    <cac:Address>
      <cbc:StreetName>City Road</cbc:StreetName>
      <cbc:BuildingName>Banking House</cbc:BuildingName>
      <cbc:BuildingNumber>12</cbc:BuildingNumber>
      <cbc:CityName>London</cbc:CityName>
      <cbc:PostalZone>AQ1 6TH</cbc:PostalZone>
      <cbc:CountrySubentity>London</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>5th Floor</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:FinancialInstitution>
  <cac:Address>
    <cbc:StreetName>Busy Street</cbc:StreetName>
    <cbc:BuildingName>The Mall</cbc:BuildingName>
    <cbc:BuildingNumber>152</cbc:BuildingNumber>
    <cbc:CityName>Farthing</cbc:CityName>
    <cbc:PostalZone>AA99 1BB</cbc:PostalZone>
    <cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
    <cac:AddressLine>
      <cbc:Line>West Wing</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:FinancialInstitutionBranch>
```

[↑ Back to contents](#contents)

### `CapabilityType`

**Used as:** `cac:BusinessCapability`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:BusinessCapability>
  <cbc:CapabilityTypeCode>General</cbc:CapabilityTypeCode>
  <cbc:Description>Advancing open standards for the information society.</cbc:Description>
</cac:BusinessCapability>
```

[↑ Back to contents](#contents)

### `ContactType`

**Used as:** `cac:CashierContact` · `cac:CommercialContact` · `cac:Contact` · `cac:DeliveryContact` · `cac:LegalContact` · `cac:PointOfSaleContact` · `cac:SignatoryContact` · `cac:SupportContact` · `cac:TechnicalContact`

_437 instances across 9 elements, with 20 unique structures_

**Structure 1** — 6 instances

```xml
<cac:Contact>
  <cbc:Telephone>+1 36222 33847</cbc:Telephone>
</cac:Contact>
```

**Structure 2** — 8 instances

```xml
<cac:Contact>
  <cbc:ElectronicMail>someName@consignor.cn</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 3** — 6 instances

```xml
<cac:Contact>
  <cbc:Name>Andreas Andersen</cbc:Name>
</cac:Contact>
```

**Structure 4** — 1 instance

```xml
<cac:Contact>
  <cbc:ID>11</cbc:ID>
</cac:Contact>
```

**Structure 5** — 2 instances

```xml
<cac:Contact>
  <cbc:Name>John Smith</cbc:Name>
  <cbc:ElectronicMail>jsmith@example.com</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 6** — 6 instances

```xml
<cac:Contact>
  <cbc:ID>12345678</cbc:ID>
  <cbc:Name>Sille Schyberg</cbc:Name>
</cac:Contact>
```

**Structure 7** — 8 instances

```xml
<cac:LegalContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:LegalContact>
```

**Structure 8** — 8 instances

```xml
<cac:TechnicalContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:TechnicalContact>
```

**Structure 9** — 8 instances

```xml
<cac:SupportContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:SupportContact>
```

**Structure 10** — 8 instances

```xml
<cac:CommercialContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:CommercialContact>
```

**Structure 11** — 1 instance

```xml
<cac:SignatoryContact>
  <cbc:ID>ML</cbc:ID>
  <cbc:Name>Mette Lind</cbc:Name>
</cac:SignatoryContact>
```

**Structure 12** — 1 instance

```xml
<cac:CashierContact>
  <cbc:Name>John D. Salesman</cbc:Name>
  <cbc:Department>Gadgets</cbc:Department>
</cac:CashierContact>
```

**Structure 13** — 8 instances

```xml
<cac:Contact>
  <cbc:ID>Freight Bookings</cbc:ID>
  <cbc:Telephone>+1 3362 4788</cbc:Telephone>
  <cbc:ElectronicMail>bookings@unitedfreight.com</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 14** — 20 instances

```xml
<cac:Contact>
  <cbc:Telephone>5121230</cbc:Telephone>
  <cbc:Telefax>5121231</cbc:Telefax>
  <cbc:ElectronicMail>john@buyercompany.eu</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 15** — 42 instances

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+8687878763</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@consignor.cn</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 16** — 1 instance

```xml
<cac:PointOfSaleContact>
  <cbc:Name>Jane D.</cbc:Name>
  <cbc:JobTitle>Store manager</cbc:JobTitle>
  <cbc:ElectronicMail>shop37@GadgetsR.us</cbc:ElectronicMail>
</cac:PointOfSaleContact>
```

**Structure 17** — 297 instances

```xml
<cac:Contact>
  <cbc:Name>Mrs Bouquet</cbc:Name>
  <cbc:Telephone>0158 1233714</cbc:Telephone>
  <cbc:Telefax>0158 1233856</cbc:Telefax>
  <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 18** — 2 instances

```xml
<cac:Contact>
  <cbc:ID>1</cbc:ID>
  <cbc:Telephone>+1 781 425 5073</cbc:Telephone>
  <cbc:Telefax>+1 781 425 5072</cbc:Telefax>
  <cbc:ElectronicMail>info@oasis-open.org</cbc:ElectronicMail>
</cac:Contact>
```

**Structure 19** — 2 instances

```xml
<cac:DeliveryContact>
  <cbc:Name>Eva Johnsson</cbc:Name>
  <cbc:Telephone>1234356</cbc:Telephone>
  <cbc:Telefax>123455</cbc:Telefax>
  <cbc:ElectronicMail>eva@johnsson.se</cbc:ElectronicMail>
</cac:DeliveryContact>
```

**Structure 20** — 2 instances

```xml
<cac:Contact>
  <cbc:ID>7778</cbc:ID>
  <cbc:Name>Ole Hansen</cbc:Name>
  <cbc:Telephone>4526532147</cbc:Telephone>
  <cbc:Telefax>4526532146</cbc:Telefax>
  <cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
</cac:Contact>
```

[↑ Back to contents](#contents)

### `ContractingPartyType`

**Used as:** `cac:ContractingParty`

_4 instances across 1 element, with 2 unique structures_

**Structure 1** — 2 instances

```xml
<cac:ContractingParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>Other</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:ContractingParty>
```

**Structure 2** — 2 instances

```xml
<cac:ContractingParty>
  <cac:Party>
    <cbc:EndpointID>01841111111111</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>5398000392577</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>FirstAgency</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>Ole Ellerbæk Madsen</cbc:Name>
    </cac:Contact>
  </cac:Party>
</cac:ContractingParty>
```

[↑ Back to contents](#contents)

### `CustomerPartyType`

**Used as:** `cac:AccountingCustomerParty` · `cac:BuyerCustomerParty` · `cac:DeliveryCustomerParty` · `cac:OriginatorCustomerParty` · `cac:RetailerCustomerParty`

_142 instances across 5 elements, with 14 unique structures_

**Structure 1** — 1 instance

```xml
<cac:AccountingCustomerParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>North American Veeblefetzer</cbc:Name>
    </cac:PartyName>
  </cac:Party>
</cac:AccountingCustomerParty>
```

**Structure 2** — 23 instances

```xml
<cac:BuyerCustomerParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>0012345000359</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:BuyerCustomerParty>
```

**Structure 3** — 9 instances

```xml
<cac:BuyerCustomerParty>
  <cac:Party>
    <cbc:EndpointID>7300072311115</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>7300070011115</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyIdentification>
      <cbc:ID>PartyID123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Johnssons byggvaror</cbc:Name>
    </cac:PartyName>
  </cac:Party>
</cac:BuyerCustomerParty>
```

**Structure 4** — 1 instance

```xml
<cac:AccountingCustomerParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>345KS5324</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>ACME Corporation</cbc:Name>
    </cac:PartyName>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>BE987654321</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
  </cac:Party>
</cac:AccountingCustomerParty>
```

**Structure 5** — 2 instances

```xml
<cac:OriginatorCustomerParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>0987678321123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Moderna Produkter AB</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Telephone>346788</cbc:Telephone>
      <cbc:Telefax>8567443</cbc:Telefax>
      <cbc:ElectronicMail>sven@moderna.se</cbc:ElectronicMail>
    </cac:Contact>
    <cac:Person>
      <cbc:FirstName>Sven</cbc:FirstName>
      <cbc:FamilyName>Pereson</cbc:FamilyName>
      <cbc:MiddleName>N</cbc:MiddleName>
      <cbc:JobTitle>Stuffuser</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
</cac:OriginatorCustomerParty>
```

**Structure 6** — 5 instances

```xml
<cac:RetailerCustomerParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Beta Shop</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Via Emilia</cbc:StreetName>
      <cbc:BuildingNumber>1</cbc:BuildingNumber>
      <cbc:CityName>Modena</cbc:CityName>
      <cbc:PostalZone>41121</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Mr Delta</cbc:Name>
      <cbc:Telephone>0039 059 33000000</cbc:Telephone>
      <cbc:Telefax>0039 059 33000055</cbc:Telefax>
      <cbc:ElectronicMail>delta@betashop.it</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:RetailerCustomerParty>
```

**Structure 7** — 3 instances

```xml
<cac:BuyerCustomerParty>
  <cbc:CustomerAssignedAccountID>XFB01</cbc:CustomerAssignedAccountID>
  <cbc:SupplierAssignedAccountID>GT00978567</cbc:SupplierAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>IYT Corporation</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Avon Way</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Bridgtow</cbc:CityName>
      <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
      <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>3rd Floor, Room 5</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Mr Fred Churchill</cbc:Name>
      <cbc:Telephone>+44 127 2653214</cbc:Telephone>
      <cbc:Telefax>+44 127 2653215</cbc:Telefax>
      <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:BuyerCustomerParty>
```

**Structure 8** — 2 instances

```xml
<cac:OriginatorCustomerParty>
  <cac:Party>
    <cbc:EndpointID>5798000416604</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>5798000416604</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Gentofte Kommune</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
      <cbc:StreetName>Bernstorffsvej</cbc:StreetName>
      <cbc:BuildingNumber>161</cbc:BuildingNumber>
      <cbc:CityName>Charlottenlund</cbc:CityName>
      <cbc:PostalZone>2920</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>DK12345678</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>63</cbc:ID>
        <cbc:Name>Moms</cbc:Name>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Gentofte Kommune</cbc:RegistrationName>
      <cbc:CompanyID>DK12345678</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:ID>12345678</cbc:ID>
      <cbc:Name>Sille Schyberg</cbc:Name>
    </cac:Contact>
  </cac:Party>
</cac:OriginatorCustomerParty>
```

**Structure 9** — 33 instances

```xml
<cac:OriginatorCustomerParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>The Terminus</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Avon Way</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Bridgtow</cbc:CityName>
      <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
      <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>3rd Floor, Room 5</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
      <cbc:CompanyID>12356478</cbc:CompanyID>
      <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>UK VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>S Massiah</cbc:Name>
      <cbc:Telephone>0127 98876545</cbc:Telephone>
      <cbc:Telefax>0127 98876546</cbc:Telefax>
      <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:OriginatorCustomerParty>
```

**Structure 10** — 33 instances

```xml
<cac:AccountingCustomerParty>
  <cbc:CustomerAssignedAccountID>XFB01</cbc:CustomerAssignedAccountID>
  <cbc:SupplierAssignedAccountID>GT00978567</cbc:SupplierAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>IYT Corporation</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Avon Way</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Bridgtow</cbc:CityName>
      <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
      <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>3rd Floor, Room 5</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
      <cbc:CompanyID>12356478</cbc:CompanyID>
      <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>UK VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>Mr Fred Churchill</cbc:Name>
      <cbc:Telephone>0127 2653214</cbc:Telephone>
      <cbc:Telefax>0127 2653215</cbc:Telefax>
      <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:AccountingCustomerParty>
```

**Structure 11** — 10 instances

```xml
<cac:DeliveryCustomerParty>
  <cbc:CustomerAssignedAccountID>XFB01</cbc:CustomerAssignedAccountID>
  <cbc:SupplierAssignedAccountID>GT00978567</cbc:SupplierAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>IYT Corporation</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Avon Way</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Bridgtow</cbc:CityName>
      <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
      <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>3rd Floor, Room 5</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
      <cbc:CompanyID>12356478</cbc:CompanyID>
      <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>UK VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>Mr Fred Churchill</cbc:Name>
      <cbc:Telephone>0127 2653214</cbc:Telephone>
      <cbc:Telefax>0127 2653215</cbc:Telefax>
      <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:DeliveryCustomerParty>
```

**Structure 12** — 11 instances

```xml
<cac:BuyerCustomerParty>
  <cbc:CustomerAssignedAccountID>XFB01</cbc:CustomerAssignedAccountID>
  <cbc:SupplierAssignedAccountID>GT00978567</cbc:SupplierAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>IYT Corporation</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Avon Way</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Bridgtow</cbc:CityName>
      <cbc:PostalZone>ZZ99 1ZZ</cbc:PostalZone>
      <cbc:CountrySubentity>Avon</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>3rd Floor, Room 5</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
      <cbc:CompanyID>12356478</cbc:CompanyID>
      <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>UK VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>Mr Fred Churchill</cbc:Name>
      <cbc:Telephone>0127 2653214</cbc:Telephone>
      <cbc:Telefax>0127 2653215</cbc:Telefax>
      <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:BuyerCustomerParty>
```

**Structure 13** — 7 instances

```xml
<cac:AccountingCustomerParty>
  <cac:Party>
    <cbc:EndpointID>1234567987654</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>345KS5324</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Buyercompany ltd</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID>1238764941386</cbc:ID>
      <cbc:Postbox>123</cbc:Postbox>
      <cbc:StreetName>Anystreet</cbc:StreetName>
      <cbc:AdditionalStreetName>Back door</cbc:AdditionalStreetName>
      <cbc:BuildingNumber>8</cbc:BuildingNumber>
      <cbc:Department>Accounting department</cbc:Department>
      <cbc:CityName>Anytown</cbc:CityName>
      <cbc:PostalZone>101</cbc:PostalZone>
      <cbc:CountrySubentity>RegionB</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>BE</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>BE54321</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>The buyercompany inc.</cbc:RegistrationName>
      <cbc:CompanyID>5645342123</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Mainplace</cbc:CityName>
        <cbc:CountrySubentity>RegionB</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>BE</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Telephone>5121230</cbc:Telephone>
      <cbc:Telefax>5121231</cbc:Telefax>
      <cbc:ElectronicMail>john@buyercompany.eu</cbc:ElectronicMail>
    </cac:Contact>
    <cac:Person>
      <cbc:FirstName>John</cbc:FirstName>
      <cbc:FamilyName>Doe</cbc:FamilyName>
      <cbc:MiddleName>X</cbc:MiddleName>
      <cbc:JobTitle>Purchasing manager</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
</cac:AccountingCustomerParty>
```

**Structure 14** — 2 instances

```xml
<cac:BuyerCustomerParty>
  <cac:Party>
    <cbc:EndpointID>7300072311115</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>7300070011115</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyIdentification>
      <cbc:ID>PartyID123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Johnssons byggvaror</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID>1234567890123</cbc:ID>
      <cbc:Postbox>PoBox123</cbc:Postbox>
      <cbc:StreetName>Rådhusgatan</cbc:StreetName>
      <cbc:AdditionalStreetName>2nd floor</cbc:AdditionalStreetName>
      <cbc:BuildingNumber>5</cbc:BuildingNumber>
      <cbc:Department>Purchasing department</cbc:Department>
      <cbc:CityName>Stockholm</cbc:CityName>
      <cbc:PostalZone>11000</cbc:PostalZone>
      <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>SE</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Herra Johnssons byggvaror AS</cbc:RegistrationName>
      <cbc:CompanyID>SE1234567801</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Stockholm</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>SE</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Johnssons Byggvaror AB</cbc:RegistrationName>
      <cbc:CompanyID>5532331183</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Stockholm</cbc:CityName>
        <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>SE</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Telephone>123456</cbc:Telephone>
      <cbc:Telefax>123456</cbc:Telefax>
      <cbc:ElectronicMail>pelle@johnsson.se</cbc:ElectronicMail>
    </cac:Contact>
    <cac:Person>
      <cbc:FirstName>Pelle</cbc:FirstName>
      <cbc:FamilyName>Svensson</cbc:FamilyName>
      <cbc:MiddleName>X</cbc:MiddleName>
      <cbc:JobTitle>Boss</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
  <cac:DeliveryContact>
    <cbc:Name>Eva Johnsson</cbc:Name>
    <cbc:Telephone>1234356</cbc:Telephone>
    <cbc:Telefax>123455</cbc:Telefax>
    <cbc:ElectronicMail>eva@johnsson.se</cbc:ElectronicMail>
  </cac:DeliveryContact>
</cac:BuyerCustomerParty>
```

[↑ Back to contents](#contents)

### `EconomicOperatorPartyType`

**Used as:** `cac:EconomicOperatorParty`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:EconomicOperatorParty>
  <cac:Party>
    <cbc:WebsiteURI>http://super.company.dk</cbc:WebsiteURI>
    <cbc:EndpointID>01842222222222</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>5790000127777</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>SuperCompany</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>Structured</cbc:AddressFormatCode>
      <cbc:StreetName>Korsbygade 34</cbc:StreetName>
      <cbc:CityName>Aalborg</cbc:CityName>
      <cbc:PostalZone>9000</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>SuperCompany</cbc:RegistrationName>
      <cbc:CompanyID>DK59873677</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:ID>7778</cbc:ID>
      <cbc:Name>Ole Hansen</cbc:Name>
      <cbc:Telephone>4526532147</cbc:Telephone>
      <cbc:Telefax>4526532146</cbc:Telefax>
      <cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:EconomicOperatorParty>
```

**Structure 2** — 1 instance

```xml
<cac:EconomicOperatorParty>
  <cac:Party>
    <cbc:WebsiteURI>http://super.company.dk</cbc:WebsiteURI>
    <cbc:EndpointID>01842222222222</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>5790000127777</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>SuperCompany</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>Structured</cbc:AddressFormatCode>
      <cbc:StreetName>Korsbygade 34</cbc:StreetName>
      <cbc:CityName>Aalborg</cbc:CityName>
      <cbc:PostalZone>9000</cbc:PostalZone>
      <cbc:CountrySubentity></cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>SuperCompany</cbc:RegistrationName>
      <cbc:CompanyID>DK59873677</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:ID>7778</cbc:ID>
      <cbc:Name>Ole Hansen</cbc:Name>
      <cbc:Telephone>4526532147</cbc:Telephone>
      <cbc:Telefax>4526532146</cbc:Telefax>
      <cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:EconomicOperatorParty>
```

[↑ Back to contents](#contents)

### `EndorserPartyType`

**Used as:** `cac:EndorserParty`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:EndorserParty>
  <cbc:RoleCode>Champer</cbc:RoleCode>
  <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Dansk Industri</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID>6916</cbc:ID>
      <cbc:StreetName>Vesterbrogade 1L, 1.sal</cbc:StreetName>
      <cbc:CityName>København V.</cbc:CityName>
      <cbc:PostalZone>1620</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
        <cbc:Name>Denmark</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:CompanyID>16077593</cbc:CompanyID>
    </cac:PartyLegalEntity>
  </cac:Party>
  <cac:SignatoryContact>
    <cbc:ID>ML</cbc:ID>
    <cbc:Name>Mette Lind</cbc:Name>
  </cac:SignatoryContact>
</cac:EndorserParty>
```

[↑ Back to contents](#contents)

### `ParticipantPartyType`

**Used as:** `cac:ParticipantParty`

_8 instances across 1 element, with 2 unique structures_

**Structure 1** — 6 instances

```xml
<cac:ParticipantParty>
  <cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
  <cac:Party>
    <cbc:EndpointID>9994567987654</cbc:EndpointID>
    <cac:PartyName>
      <cbc:Name>Buyer GmbH</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:CityName>Munchen</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
  </cac:Party>
  <cac:LegalContact>
    <cbc:Name>Peter Gruen</cbc:Name>
    <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
  </cac:LegalContact>
  <cac:TechnicalContact>
    <cbc:Name>Peter Gruen</cbc:Name>
    <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
  </cac:TechnicalContact>
  <cac:SupportContact>
    <cbc:Name>Peter Gruen</cbc:Name>
    <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
  </cac:SupportContact>
  <cac:CommercialContact>
    <cbc:Name>Peter Gruen</cbc:Name>
    <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
  </cac:CommercialContact>
</cac:ParticipantParty>
```

**Structure 2** — 2 instances

```xml
<cac:ParticipantParty>
  <cbc:InitiatingPartyIndicator>true</cbc:InitiatingPartyIndicator>
  <cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
  <cac:Party>
    <cbc:EndpointID>1234567987654</cbc:EndpointID>
    <cac:PartyName>
      <cbc:Name>Vendor Inc.</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:CityName>New York</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
  </cac:Party>
  <cac:LegalContact>
    <cbc:Name>John Smith</cbc:Name>
    <cbc:ElectronicMail>john.smith@vendor.net</cbc:ElectronicMail>
  </cac:LegalContact>
  <cac:TechnicalContact>
    <cbc:Name>Paul McQueen</cbc:Name>
    <cbc:ElectronicMail>paul.mcqueen@vendor.net</cbc:ElectronicMail>
  </cac:TechnicalContact>
  <cac:SupportContact>
    <cbc:Name>Paul McQueen</cbc:Name>
    <cbc:ElectronicMail>paul.mcqueen@vendor.net</cbc:ElectronicMail>
  </cac:SupportContact>
  <cac:CommercialContact>
    <cbc:Name>Jennifer de Niro</cbc:Name>
    <cbc:ElectronicMail>jennifer.deniro@vendor.net</cbc:ElectronicMail>
  </cac:CommercialContact>
</cac:ParticipantParty>
```

[↑ Back to contents](#contents)

### `PartyIdentificationType`

**Used as:** `cac:PartyIdentification`

_257 instances across 1 element, with 2 unique structures_

**Structure 1** — 255 instances

```xml
<cac:PartyIdentification>
  <cbc:ID>345KS5324</cbc:ID>
</cac:PartyIdentification>
```

**Structure 2** — 2 instances

```xml
<cac:PartyIdentification>
  <ext:UBLExtensions>
    <ext:UBLExtension>
      <ext:ExtensionContent>
        <ext:IDExtension>T0002</ext:IDExtension>
      </ext:ExtensionContent>
    </ext:UBLExtension>
  </ext:UBLExtensions>
  <cbc:ID>FI1234567-8</cbc:ID>
</cac:PartyIdentification>
```

[↑ Back to contents](#contents)

### `PartyLegalEntityType`

**Used as:** `cac:PartyLegalEntity`

_51 instances across 1 element, with 4 unique structures_

**Structure 1** — 24 instances

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>DK43232010</cbc:CompanyID>
</cac:PartyLegalEntity>
```

**Structure 2** — 7 instances

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
  <cbc:CompanyID>DK18296799</cbc:CompanyID>
</cac:PartyLegalEntity>
```

**Structure 3** — 2 instances

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>45789034</cbc:CompanyID>
  <cbc:RegistrationDate>1957-08-13</cbc:RegistrationDate>
</cac:PartyLegalEntity>
```

**Structure 4** — 18 instances

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>Moderna Produkter AB</cbc:RegistrationName>
  <cbc:CompanyID>5532332283</cbc:CompanyID>
  <cac:RegistrationAddress>
    <cbc:CityName>Stockholm</cbc:CityName>
    <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
    <cac:Country>
      <cbc:IdentificationCode>SE</cbc:IdentificationCode>
    </cac:Country>
  </cac:RegistrationAddress>
</cac:PartyLegalEntity>
```

[↑ Back to contents](#contents)

### `PartyNameType`

**Used as:** `cac:PartyName`

_514 instances across 1 element, with 1 unique structure_

**Structure 1** — 514 instances

```xml
<cac:PartyName>
  <cbc:Name>Gedevang Mejeri</cbc:Name>
</cac:PartyName>
```

[↑ Back to contents](#contents)

### `PartyTaxSchemeType`

**Used as:** `cac:PartyTaxScheme`

_232 instances across 1 element, with 4 unique structures_

**Structure 1** — 17 instances

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>BE54321</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

**Structure 2** — 4 instances

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>DK18296799</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>63</cbc:ID>
    <cbc:Name>Moms</cbc:Name>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

**Structure 3** — 209 instances

```xml
<cac:PartyTaxScheme>
  <cbc:RegistrationName>Farthing Purchasing Consortium</cbc:RegistrationName>
  <cbc:CompanyID>175 269 2355</cbc:CompanyID>
  <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
    <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

**Structure 4** — 2 instances

```xml
<cac:PartyTaxScheme>
  <cbc:RegistrationName>Herra Johnssons byggvaror AS</cbc:RegistrationName>
  <cbc:CompanyID>SE1234567801</cbc:CompanyID>
  <cac:RegistrationAddress>
    <cbc:CityName>Stockholm</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>SE</cbc:IdentificationCode>
    </cac:Country>
  </cac:RegistrationAddress>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

[↑ Back to contents](#contents)

### `PersonType`

**Used as:** `cac:Person`

_29 instances across 1 element, with 4 unique structures_

**Structure 1** — 2 instances

```xml
<cac:Person>
  <cbc:FirstName>RAUL</cbc:FirstName>
  <cbc:FamilyName>GONZALES</cbc:FamilyName>
</cac:Person>
```

**Structure 2** — 6 instances

```xml
<cac:Person>
  <cbc:FirstName>GIORGIO</cbc:FirstName>
  <cbc:FamilyName>VERDI</cbc:FamilyName>
  <cbc:RoleCode>BN</cbc:RoleCode>
</cac:Person>
```

**Structure 3** — 20 instances

```xml
<cac:Person>
  <cbc:FirstName>Sven</cbc:FirstName>
  <cbc:FamilyName>Pereson</cbc:FamilyName>
  <cbc:MiddleName>N</cbc:MiddleName>
  <cbc:JobTitle>Stuffuser</cbc:JobTitle>
</cac:Person>
```

**Structure 4** — 1 instance

```xml
<cac:Person>
  <cbc:FirstName>Kirsten</cbc:FirstName>
  <cbc:FamilyName>Jensen</cbc:FamilyName>
  <cac:IdentityDocumentReference>
    <cbc:ID>325334535</cbc:ID>
  </cac:IdentityDocumentReference>
</cac:Person>
```

[↑ Back to contents](#contents)

### `SupplierPartyType`

**Used as:** `cac:AccountingSupplierParty` · `cac:DespatchSupplierParty` · `cac:SellerSupplierParty`

_118 instances across 3 elements, with 13 unique structures_

**Structure 1** — 1 instance

```xml
<cac:AccountingSupplierParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Custom Cotter Pins</cbc:Name>
    </cac:PartyName>
  </cac:Party>
</cac:AccountingSupplierParty>
```

**Structure 2** — 23 instances

```xml
<cac:SellerSupplierParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>0012345000058</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 3** — 9 instances

```xml
<cac:SellerSupplierParty>
  <cac:Party>
    <cbc:EndpointID>7302347231111</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>SellerPartyID123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Moderna Produkter AB</cbc:Name>
    </cac:PartyName>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 4** — 1 instance

```xml
<cac:AccountingSupplierParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>Supp123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Example Supplies Ltd.</cbc:Name>
    </cac:PartyName>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>DK123456789</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
  </cac:Party>
</cac:AccountingSupplierParty>
```

**Structure 5** — 1 instance

```xml
<cac:AccountingSupplierParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>123456789</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Gadgets R Us, Inc.</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>High Street</cbc:StreetName>
      <cbc:BuildingNumber>1</cbc:BuildingNumber>
      <cbc:CityName>Copenhagen</cbc:CityName>
      <cbc:PostalZone>1001</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>DK12345</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
  </cac:Party>
</cac:AccountingSupplierParty>
```

**Structure 6** — 5 instances

```xml
<cac:SellerSupplierParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Arancio Forniture spa</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
      <cbc:BuildingNumber>403</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40129</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Mr Rossi</cbc:Name>
      <cbc:Telephone>0039 051 23000000</cbc:Telephone>
      <cbc:Telefax>0039 051 23000023</cbc:Telefax>
      <cbc:ElectronicMail>rossi@arancioforniture.it</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 7** — 3 instances

```xml
<cac:SellerSupplierParty>
  <cbc:CustomerAssignedAccountID>CO001</cbc:CustomerAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Consortial</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Boston Road</cbc:StreetName>
      <cbc:BuildingName>Suite M-102</cbc:BuildingName>
      <cbc:BuildingNumber>630</cbc:BuildingNumber>
      <cbc:CityName>Billerica</cbc:CityName>
      <cbc:PostalZone>01821</cbc:PostalZone>
      <cbc:CountrySubentity>Massachusetts</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
      <cac:Country>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Mrs Bouquet</cbc:Name>
      <cbc:Telephone>+1 158 1233714</cbc:Telephone>
      <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
      <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 8** — 2 instances

```xml
<cac:SellerSupplierParty>
  <cbc:CustomerAssignedAccountID>LEV00123</cbc:CustomerAssignedAccountID>
  <cac:Party>
    <cbc:EndpointID>DK18296799</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>DK18296799</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Delcomputer A/S</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
      <cbc:StreetName>Arne Jacobsens Allé</cbc:StreetName>
      <cbc:BuildingNumber>15</cbc:BuildingNumber>
      <cbc:CityName>København S</cbc:CityName>
      <cbc:PostalZone>2300</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>DK18296799</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>63</cbc:ID>
        <cbc:Name>Moms</cbc:Name>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
      <cbc:CompanyID>18296799</cbc:CompanyID>
    </cac:PartyLegalEntity>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 9** — 33 instances

```xml
<cac:AccountingSupplierParty>
  <cbc:CustomerAssignedAccountID>CO001</cbc:CustomerAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Consortial</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Busy Street</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Farthing</cbc:CityName>
      <cbc:PostalZone>AA99 1BB</cbc:PostalZone>
      <cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>The Roundabout</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
      <cbc:CompanyID>175 269 2355</cbc:CompanyID>
      <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>Mrs Bouquet</cbc:Name>
      <cbc:Telephone>0158 1233714</cbc:Telephone>
      <cbc:Telefax>0158 1233856</cbc:Telefax>
      <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:AccountingSupplierParty>
```

**Structure 10** — 10 instances

```xml
<cac:DespatchSupplierParty>
  <cbc:CustomerAssignedAccountID>CO001</cbc:CustomerAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Consortial</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Busy Street</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Farthing</cbc:CityName>
      <cbc:PostalZone>AA99 1BB</cbc:PostalZone>
      <cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>The Roundabout</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
      <cbc:CompanyID>175 269 2355</cbc:CompanyID>
      <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>Mrs Bouquet</cbc:Name>
      <cbc:Telephone>0158 1233714</cbc:Telephone>
      <cbc:Telefax>0158 1233856</cbc:Telefax>
      <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:DespatchSupplierParty>
```

**Structure 11** — 21 instances

```xml
<cac:SellerSupplierParty>
  <cbc:CustomerAssignedAccountID>CO001</cbc:CustomerAssignedAccountID>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Consortial</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Busy Street</cbc:StreetName>
      <cbc:BuildingName>Thereabouts</cbc:BuildingName>
      <cbc:BuildingNumber>56A</cbc:BuildingNumber>
      <cbc:CityName>Farthing</cbc:CityName>
      <cbc:PostalZone>AA99 1BB</cbc:PostalZone>
      <cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
      <cac:AddressLine>
        <cbc:Line>The Roundabout</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>GB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
      <cbc:CompanyID>175 269 2355</cbc:CompanyID>
      <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:Contact>
      <cbc:Name>Mrs Bouquet</cbc:Name>
      <cbc:Telephone>0158 1233714</cbc:Telephone>
      <cbc:Telefax>0158 1233856</cbc:Telefax>
      <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 12** — 2 instances

```xml
<cac:SellerSupplierParty>
  <cac:Party>
    <cbc:EndpointID>7302347231111</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>SellerPartyID123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Moderna Produkter AB</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID>0987654321123</cbc:ID>
      <cbc:Postbox>321</cbc:Postbox>
      <cbc:StreetName>Kungsgatan</cbc:StreetName>
      <cbc:AdditionalStreetName>suite12</cbc:AdditionalStreetName>
      <cbc:BuildingNumber>22</cbc:BuildingNumber>
      <cbc:Department>Sales department</cbc:Department>
      <cbc:CityName>Stockholm</cbc:CityName>
      <cbc:PostalZone>11000</cbc:PostalZone>
      <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>SE</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Moderna Produkter AB</cbc:RegistrationName>
      <cbc:CompanyID>5532332283</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Stockholm</cbc:CityName>
        <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>SE</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Telephone>34557</cbc:Telephone>
      <cbc:Telefax>3456767</cbc:Telefax>
      <cbc:ElectronicMail>lars@moderna.se</cbc:ElectronicMail>
    </cac:Contact>
    <cac:Person>
      <cbc:FirstName>Lars</cbc:FirstName>
      <cbc:FamilyName>Petersen</cbc:FamilyName>
      <cbc:MiddleName>M</cbc:MiddleName>
      <cbc:JobTitle>Sales manager</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
</cac:SellerSupplierParty>
```

**Structure 13** — 7 instances

```xml
<cac:AccountingSupplierParty>
  <cac:Party>
    <cbc:EndpointID>1234567890123</cbc:EndpointID>
    <cac:PartyIdentification>
      <cbc:ID>Supp123</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Salescompany ltd.</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID>1231412341324</cbc:ID>
      <cbc:Postbox>5467</cbc:Postbox>
      <cbc:StreetName>Main street</cbc:StreetName>
      <cbc:AdditionalStreetName>Suite 123</cbc:AdditionalStreetName>
      <cbc:BuildingNumber>1</cbc:BuildingNumber>
      <cbc:Department>Revenue department</cbc:Department>
      <cbc:CityName>Big city</cbc:CityName>
      <cbc:PostalZone>54321</cbc:PostalZone>
      <cbc:CountrySubentityCode>RegionA</cbc:CountrySubentityCode>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>DK12345</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>The Sellercompany Incorporated</cbc:RegistrationName>
      <cbc:CompanyID>5402697509</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Big city</cbc:CityName>
        <cbc:CountrySubentity>RegionA</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>DK</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Telephone>4621230</cbc:Telephone>
      <cbc:Telefax>4621231</cbc:Telefax>
      <cbc:ElectronicMail>antonio@salescompany.dk</cbc:ElectronicMail>
    </cac:Contact>
    <cac:Person>
      <cbc:FirstName>Antonio</cbc:FirstName>
      <cbc:FamilyName>M</cbc:FamilyName>
      <cbc:MiddleName>Salemacher</cbc:MiddleName>
      <cbc:JobTitle>Sales manager</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
</cac:AccountingSupplierParty>
```

[↑ Back to contents](#contents)

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)