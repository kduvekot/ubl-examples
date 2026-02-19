# UBL Element Reference — Contract & Legal

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **5** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [ContractType](#ContractType)
  - [EndorsementType](#EndorsementType)
  - [SignatureType](#SignatureType)
  - [CustomsDeclarationType](#CustomsDeclarationType)
  - [NotificationRequirementType](#NotificationRequirementType)

---

## cac Elements — Contract & Legal

### `ContractType`

**Used as:** `cac:Contract` · `cac:TransportContract`

_15 instances across 2 elements, with 6 unique structures_

**Structure 1** — 2 instances

```xml
<cac:Contract>
  <cbc:ID>34322</cbc:ID>
  <cbc:ContractType>FrameworkAgreementID123</cbc:ContractType>
</cac:Contract>
```

**Structure 2** — 6 instances

```xml
<cac:Contract>
  <cac:ContractDocumentReference>
    <cbc:ID>GHJ76849</cbc:ID>
    <cbc:IssueDate>2002-08-13</cbc:IssueDate>
  </cac:ContractDocumentReference>
</cac:Contract>
```

**Structure 3** — 2 instances

```xml
<cac:TransportContract>
  <cbc:Note>Framework Agreement</cbc:Note>
  <cac:ContractDocumentReference>
    <cbc:ID>TC101</cbc:ID>
    <cbc:IssueDate>2010-01-01</cbc:IssueDate>
    <cbc:DocumentTypeCode>315</cbc:DocumentTypeCode>
    <cbc:DocumentType>Contract</cbc:DocumentType>
    <cbc:DocumentDescription>Framework Agreement between Consignor and NECOSS</cbc:DocumentDescription>
  </cac:ContractDocumentReference>
</cac:TransportContract>
```

**Structure 4** — 1 instance

```xml
<cac:TransportContract>
  <cbc:ID>101_3</cbc:ID>
  <cbc:IssueDate>2011-03-13</cbc:IssueDate>
  <cbc:IssueTime>08:20:00.0Z</cbc:IssueTime>
  <cbc:NominationDate>2011-03-13</cbc:NominationDate>
  <cbc:NominationTime>09:30:00.0Z</cbc:NominationTime>
  <cbc:ContractType>Continuing Transport Contract</cbc:ContractType>
  <cbc:Note>A call-off from the annual contract</cbc:Note>
  <cac:ValidityPeriod>
    <cbc:StartDate>2011-03-13</cbc:StartDate>
    <cbc:EndDate>2011-03-17</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ContractDocumentReference>
    <cbc:ID>101</cbc:ID>
    <cbc:DocumentType>Annual Contract</cbc:DocumentType>
    <cac:Attachment>
      <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
    </cac:Attachment>
  </cac:ContractDocumentReference>
</cac:TransportContract>
```

**Structure 5** — 1 instance

```xml
<cac:TransportContract>
  <cbc:ID>CONS-001</cbc:ID>
  <cbc:IssueDate>2005-06-24</cbc:IssueDate>
  <cbc:ContractType>Forwarding Instructions</cbc:ContractType>
  <cac:ValidityPeriod>
    <cbc:StartDate>2005-06-25</cbc:StartDate>
    <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-30</cbc:EndDate>
    <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
  </cac:ValidityPeriod>
  <cac:ContractDocumentReference>
    <cbc:ID>normalizedString</cbc:ID>
    <cbc:CopyIndicator>false</cbc:CopyIndicator>
    <cbc:UUID>normalizedString</cbc:UUID>
    <cbc:IssueDate>1967-08-13</cbc:IssueDate>
    <cbc:DocumentTypeCode>normalizedString</cbc:DocumentTypeCode>
    <cbc:DocumentType>String</cbc:DocumentType>
    <cbc:XPath>String</cbc:XPath>
    <cac:Attachment>
      <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
      <cac:ExternalReference>
        <cbc:URI>normalizedString</cbc:URI>
        <cbc:DocumentHash>String</cbc:DocumentHash>
        <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
        <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:ContractDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>normalizedString</cbc:ID>
    <cbc:CopyIndicator>false</cbc:CopyIndicator>
    <cbc:UUID>normalizedString</cbc:UUID>
    <cbc:IssueDate>1967-08-13</cbc:IssueDate>
    <cbc:DocumentTypeCode>normalizedString</cbc:DocumentTypeCode>
    <cbc:DocumentType>String</cbc:DocumentType>
    <cbc:XPath>String</cbc:XPath>
    <cac:Attachment>
      <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
      <cac:ExternalReference>
        <cbc:URI>normalizedString</cbc:URI>
        <cbc:DocumentHash>String</cbc:DocumentHash>
        <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
        <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:ContractDocumentReference>
</cac:TransportContract>
```

**Structure 6** — 3 instances

```xml
<cac:TransportContract>
  <cbc:ID>CONS-001</cbc:ID>
  <cbc:IssueDate>2005-06-24</cbc:IssueDate>
  <cbc:ContractType>Forwarding Instructions</cbc:ContractType>
  <cac:ValidityPeriod>
    <cbc:StartDate>2005-06-25</cbc:StartDate>
    <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-30</cbc:EndDate>
    <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
  </cac:ValidityPeriod>
  <cac:ContractDocumentReference>
    <cbc:ID>normalizedString</cbc:ID>
    <cbc:CopyIndicator>false</cbc:CopyIndicator>
    <cbc:UUID>normalizedString</cbc:UUID>
    <cbc:IssueDate>1967-08-13</cbc:IssueDate>
    <cbc:DocumentTypeCode>normalizedString</cbc:DocumentTypeCode>
    <cbc:DocumentType>String</cbc:DocumentType>
    <cbc:XPath>String</cbc:XPath>
    <cbc:XPath>String</cbc:XPath>
    <cac:Attachment>
      <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
      <cac:ExternalReference>
        <cbc:URI>normalizedString</cbc:URI>
        <cbc:DocumentHash>String</cbc:DocumentHash>
        <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
        <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:ContractDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>normalizedString</cbc:ID>
    <cbc:CopyIndicator>false</cbc:CopyIndicator>
    <cbc:UUID>normalizedString</cbc:UUID>
    <cbc:IssueDate>1967-08-13</cbc:IssueDate>
    <cbc:DocumentTypeCode>normalizedString</cbc:DocumentTypeCode>
    <cbc:DocumentType>String</cbc:DocumentType>
    <cbc:XPath>String</cbc:XPath>
    <cbc:XPath>String</cbc:XPath>
    <cac:Attachment>
      <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
      <cac:ExternalReference>
        <cbc:URI>normalizedString</cbc:URI>
        <cbc:DocumentHash>String</cbc:DocumentHash>
        <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
        <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:ContractDocumentReference>
</cac:TransportContract>
```

[↑ Back to contents](#contents)

### `EndorsementType`

**Used as:** `cac:IssuerEndorsement`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:IssuerEndorsement>
  <cbc:DocumentID>33006</cbc:DocumentID>
  <cbc:ApprovalStatus>Issued</cbc:ApprovalStatus>
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
</cac:IssuerEndorsement>
```

[↑ Back to contents](#contents)

### `SignatureType`

**Used as:** `cac:Signature`

_7 instances across 1 element, with 3 unique structures_

**Structure 1** — 3 instances

```xml
<cac:Signature>
  <cbc:ID>urn:oasis:names:specification:ubl:signatures</cbc:ID>
  <cbc:SignatureMethod>urn:oasis:names:specification:ubl:profile:dsig:signature</cbc:SignatureMethod>
  <cac:SignatoryParty>
    <cac:PartyIdentification>
      <cbc:ID>MyParty</cbc:ID>
    </cac:PartyIdentification>
  </cac:SignatoryParty>
</cac:Signature>
```

**Structure 2** — 2 instances

```xml
<cac:Signature>
  <cbc:ID>urn:oasis:names:specification:ubl:signature:Invoice</cbc:ID>
  <cbc:SignatureMethod>urn:oasis:names:specification:ubl:dsig:detached</cbc:SignatureMethod>
  <cac:SignatoryParty>
    <cac:PartyIdentification>
      <cbc:ID>MyParty</cbc:ID>
    </cac:PartyIdentification>
  </cac:SignatoryParty>
  <cac:DigitalSignatureAttachment>
    <cac:ExternalReference>
      <cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
    </cac:ExternalReference>
  </cac:DigitalSignatureAttachment>
</cac:Signature>
```

**Structure 3** — 2 instances

```xml
<cac:Signature>
  <cbc:ID>234664</cbc:ID>
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
</cac:Signature>
```

[↑ Back to contents](#contents)

### `CustomsDeclarationType`

**Used as:** `cac:CustomsDeclaration` · `cac:PreviousCustomsDeclaration`

_8 instances across 2 elements, with 3 unique structures_

**Structure 1** — 2 instances

```xml
<cac:CustomsDeclaration>
  <cbc:ID>10158209175014500</cbc:ID>
</cac:CustomsDeclaration>
```

**Structure 2** — 4 instances

```xml
<cac:PreviousCustomsDeclaration>
  <cbc:ID>HUISI000000002</cbc:ID>
</cac:PreviousCustomsDeclaration>
```

**Structure 3** — 2 instances

```xml
<cac:CustomsDeclaration>
  <cbc:ID>exi000073</cbc:ID>
  <cac:ValidityPeriod>
    <cbc:StartDate>2019-03-18</cbc:StartDate>
    <cbc:EndDate>2019-03-18</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:Shipment>
    <cbc:ID>ffi000861</cbc:ID>
    <cbc:SpecialInstructions>Test</cbc:SpecialInstructions>
    <cac:Consignment>
      <cbc:ID>1</cbc:ID>
      <cbc:SummaryDescription>1 other</cbc:SummaryDescription>
      <cbc:TotalInvoiceAmount>10500.00</cbc:TotalInvoiceAmount>
      <cbc:GrossWeightMeasure>88.00</cbc:GrossWeightMeasure>
      <cbc:NetWeightMeasure>76.00</cbc:NetWeightMeasure>
      <cbc:GrossVolumeMeasure>0.336</cbc:GrossVolumeMeasure>
      <cbc:NetVolumeMeasure>0.336000</cbc:NetVolumeMeasure>
      <cbc:LoadingLengthMeasure>0</cbc:LoadingLengthMeasure>
      <cbc:SequenceID>204</cbc:SequenceID>
      <cbc:TotalGoodsItemQuantity>2</cbc:TotalGoodsItemQuantity>
      <cbc:TotalTransportHandlingUnitQuantity>1</cbc:TotalTransportHandlingUnitQuantity>
      <cbc:DeliveryInstructions>Test</cbc:DeliveryInstructions>
      <cac:RequestedPickupTransportEvent>
        <cac:Location>
          <cac:Address>
            <cbc:StreetName>Stribevangen</cbc:StreetName>
            <cbc:BuildingNumber>89</cbc:BuildingNumber>
            <cbc:CityName>Gedser</cbc:CityName>
            <cbc:PostalZone>4874</cbc:PostalZone>
            <cac:Country>
              <cbc:IdentificationCode>DK</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
        <cac:Period>
          <cbc:StartDate>2016-08-02</cbc:StartDate>
          <cbc:StartTime>07:00:00</cbc:StartTime>
          <cbc:EndDate>2016-08-02</cbc:EndDate>
          <cbc:EndTime>15:30:00</cbc:EndTime>
        </cac:Period>
      </cac:RequestedPickupTransportEvent>
      <cac:RequestedDeliveryTransportEvent>
        <cac:Location>
          <cac:Address>
            <cbc:StreetName>Marken</cbc:StreetName>
            <cbc:BuildingNumber>13</cbc:BuildingNumber>
            <cbc:CityName>Bergen</cbc:CityName>
            <cbc:PostalZone>5017</cbc:PostalZone>
            <cac:Country>
              <cbc:IdentificationCode>NO</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
        <cac:Period>
          <cbc:StartDate>2017-03-30</cbc:StartDate>
        </cac:Period>
      </cac:RequestedDeliveryTransportEvent>
      <cac:OriginalDepartureCountry>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:DeliveryTerms>
        <cbc:ID>FCA</cbc:ID>
        <cac:DeliveryLocation>
          <cbc:Name>9000</cbc:Name>
        </cac:DeliveryLocation>
      </cac:DeliveryTerms>
      <cac:MainCarriageShipmentStage>
        <cbc:TransportModeCode>3</cbc:TransportModeCode>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cbc:TotalPackageQuantity>1</cbc:TotalPackageQuantity>
        <cac:TransportEquipment>
          <cbc:TransportEquipmentTypeCode>AD</cbc:TransportEquipmentTypeCode>
          <cbc:FullnessIndicationCode>FTL</cbc:FullnessIndicationCode>
        </cac:TransportEquipment>
        <cac:Package>
          <cbc:ID>FLGS339241</cbc:ID>
          <cbc:Quantity>1</cbc:Quantity>
          <cbc:PackageLevelCode>NoStacking</cbc:PackageLevelCode>
          <cbc:PackingMaterial>other</cbc:PackingMaterial>
          <cbc:TraceID>STD14037</cbc:TraceID>
          <cac:GoodsItem>
            <cbc:ID>636257218904553192</cbc:ID>
            <cbc:Description>Kløver Økologis gedeost 15%</cbc:Description>
            <cbc:DeclaredCustomsValueAmount>0.00</cbc:DeclaredCustomsValueAmount>
            <cbc:DeclaredStatisticsValueAmount>10050.00</cbc:DeclaredStatisticsValueAmount>
            <cbc:ValueAmount>10500.00</cbc:ValueAmount>
            <cbc:Quantity>150.00</cbc:Quantity>
            <cbc:TraceID>STD14037</cbc:TraceID>
            <cac:Item>
              <cbc:Description>Kløver Økologisk gedeost 15%</cbc:Description>
              <cbc:PackQuantity>1</cbc:PackQuantity>
              <cbc:Name>Gedesby Øko-ost</cbc:Name>
              <cac:SellersItemIdentification>
                <cbc:ID>100700011021</cbc:ID>
              </cac:SellersItemIdentification>
              <cac:OriginCountry>
                <cbc:IdentificationCode>DK</cbc:IdentificationCode>
              </cac:OriginCountry>
              <cac:CommodityClassification>
                <cbc:CommodityCode>84195000</cbc:CommodityCode>
              </cac:CommodityClassification>
            </cac:Item>
            <cac:Despatch>
              <cbc:ID>FLGS339241</cbc:ID>
            </cac:Despatch>
          </cac:GoodsItem>
          <cac:MeasurementDimension>
            <cbc:AttributeID>OuterHeight</cbc:AttributeID>
            <cbc:Measure>70</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID>OuterWidth</cbc:AttributeID>
            <cbc:Measure>60</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID>OuterDepth</cbc:AttributeID>
            <cbc:Measure>80</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID>GrossVolumen</cbc:AttributeID>
            <cbc:Measure>0.336</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID>GrossWeight</cbc:AttributeID>
            <cbc:Measure>88</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:Pickup>
            <cbc:LatestPickupDate>2016-08-02</cbc:LatestPickupDate>
          </cac:Pickup>
          <cac:Despatch>
            <cbc:ID>28833-2661-144</cbc:ID>
          </cac:Despatch>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
  </cac:Shipment>
  <cac:CustomsExitOfficeLocation>
    <cbc:ID>DK003102</cbc:ID>
    <cac:Address>
      <cbc:StreetName>Dalsagervej</cbc:StreetName>
      <cbc:BuildingNumber>7</cbc:BuildingNumber>
      <cbc:CityName>Hirtshals</cbc:CityName>
      <cbc:PostalZone>9850</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:CustomsExitOfficeLocation>
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
  <cac:AdditionalDocumentReference>
    <cbc:ID>34564645</cbc:ID>
  </cac:AdditionalDocumentReference>
</cac:CustomsDeclaration>
```

[↑ Back to contents](#contents)

### `NotificationRequirementType`

**Used as:** `cac:NotificationRequirement`

_5 instances across 1 element, with 3 unique structures_

**Structure 1** — 1 instance

```xml
<cac:NotificationRequirement>
  <cbc:NotificationTypeCode>Status Notifications, schedule deviations</cbc:NotificationTypeCode>
  <cac:NotifyParty>
    <cbc:WebsiteURI>http://www.CONSIGNEE.no/statusreceptioninterface#2</cbc:WebsiteURI>
    <cac:PartyName>
      <cbc:Name>CONSIGNEE</cbc:Name>
    </cac:PartyName>
  </cac:NotifyParty>
  <cac:PostEventPeriod>
    <cbc:DurationMeasure>30</cbc:DurationMeasure>
    <cbc:Description>Deviations shall be notified to the CONSIGNEE within max 30 minutes</cbc:Description>
  </cac:PostEventPeriod>
</cac:NotificationRequirement>
```

**Structure 2** — 2 instances

```xml
<cac:NotificationRequirement>
  <cbc:NotificationTypeCode>TIME_SCHEDULE_DEVIATIONS</cbc:NotificationTypeCode>
  <cac:NotifyParty>
    <cbc:EndpointID>www.consignee.de/statusnotifications/</cbc:EndpointID>
    <cac:PartyName>
      <cbc:Name>Consignee</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:ElectronicMail>someName@consignee.de</cbc:ElectronicMail>
    </cac:Contact>
  </cac:NotifyParty>
  <cac:NotifyParty>
    <cbc:EndpointID>www.consignor.cn/statusnotifications/</cbc:EndpointID>
    <cac:PartyName>
      <cbc:Name>Consignor</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:ElectronicMail>someName@consignor.cn</cbc:ElectronicMail>
    </cac:Contact>
  </cac:NotifyParty>
</cac:NotificationRequirement>
```

**Structure 3** — 2 instances

```xml
<cac:NotificationRequirement>
  <cbc:NotificationTypeCode>ITEM_CONDITION_DEVIATIONS</cbc:NotificationTypeCode>
  <cbc:PostEventNotificationDurationMeasure>10</cbc:PostEventNotificationDurationMeasure>
  <cac:NotifyParty>
    <cbc:EndpointID>www.consignee.com/statusnotifications/</cbc:EndpointID>
    <cac:PartyName>
      <cbc:Name>Consignee</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:ElectronicMail>someName@consignee.de</cbc:ElectronicMail>
    </cac:Contact>
  </cac:NotifyParty>
  <cac:NotifyParty>
    <cbc:EndpointID>www.consignor.cn/statusnotifications/</cbc:EndpointID>
    <cac:PartyName>
      <cbc:Name>Consignor</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:ElectronicMail>someName@consignor.cn</cbc:ElectronicMail>
    </cac:Contact>
  </cac:NotifyParty>
</cac:NotificationRequirement>
```

[↑ Back to contents](#contents)

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)