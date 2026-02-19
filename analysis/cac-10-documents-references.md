# UBL Element Reference — Documents, References & Responses

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **8** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [DocumentReferenceType](#DocumentReferenceType)
  - [DocumentDistributionType](#DocumentDistributionType)
  - [DocumentMetadataType](#DocumentMetadataType)
  - [ExternalReferenceType](#ExternalReferenceType)
  - [AttachmentType](#AttachmentType)
  - [ResponseType](#ResponseType)
  - [StatusType](#StatusType)
  - [Unknown](#Unknown)

---

## cac Elements — Documents, References & Responses

### `DocumentReferenceType`

**Used as:** `cac:AdditionalDocumentReference` · `cac:CatalogueDocumentReference` · `cac:ContractDocumentReference` · `cac:CreditNoteDocumentReference` · `cac:DespatchDocumentReference` · `cac:DocumentReference` · `cac:IdentityDocumentReference` · `cac:InvoiceDocumentReference` · `cac:OrderDocumentReference` · `cac:OriginatorDocumentReference` · `cac:ProofOfReexportationRequestDocumentReference` · `cac:QuotationDocumentReference` · `cac:ReceiptDocumentReference` · `cac:RequestForQuotationDocumentReference` · `cac:SalesDocumentReference` · `cac:ShipmentDocumentReference` · `cac:TransportExecutionPlanDocumentReference` · `cac:TransportProgressStatusRequestDocumentReference` · `cac:TransportServiceDescriptionDocumentReference` · `cac:TransportServiceDescriptionRequestDocumentReference` · `cac:VoucherDocumentReference`

_122 instances across 21 elements, with 38 unique structures_

**Structure 1** — 1 instance

```xml
<cac:InvoiceDocumentReference>
  <cbc:ID>TOSL108</cbc:ID>
</cac:InvoiceDocumentReference>
```

**Structure 2** — 2 instances

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>34564645</cbc:ID>
</cac:AdditionalDocumentReference>
```

**Structure 3** — 2 instances

```xml
<cac:QuotationDocumentReference>
  <cbc:ID>QuoteID123</cbc:ID>
</cac:QuotationDocumentReference>
```

**Structure 4** — 2 instances

```xml
<cac:OrderDocumentReference>
  <cbc:ID>RjectedOrderID123</cbc:ID>
</cac:OrderDocumentReference>
```

**Structure 5** — 2 instances

```xml
<cac:OriginatorDocumentReference>
  <cbc:ID>MAFO</cbc:ID>
</cac:OriginatorDocumentReference>
```

**Structure 6** — 3 instances

```xml
<cac:TransportExecutionPlanDocumentReference>
  <cbc:ID>TEPID_1</cbc:ID>
</cac:TransportExecutionPlanDocumentReference>
```

**Structure 7** — 2 instances

```xml
<cac:TransportServiceDescriptionDocumentReference>
  <cbc:ID>2</cbc:ID>
</cac:TransportServiceDescriptionDocumentReference>
```

**Structure 8** — 1 instance

```xml
<cac:TransportProgressStatusRequestDocumentReference>
  <cbc:ID>TPS_1</cbc:ID>
</cac:TransportProgressStatusRequestDocumentReference>
```

**Structure 9** — 1 instance

```xml
<cac:TransportServiceDescriptionRequestDocumentReference>
  <cbc:ID>TSD_REQ_1</cbc:ID>
</cac:TransportServiceDescriptionRequestDocumentReference>
```

**Structure 10** — 1 instance

```xml
<cac:IdentityDocumentReference>
  <cbc:ID>325334535</cbc:ID>
</cac:IdentityDocumentReference>
```

**Structure 11** — 5 instances

```xml
<cac:VoucherDocumentReference>
  <cbc:ID>52345423423</cbc:ID>
</cac:VoucherDocumentReference>
```

**Structure 12** — 1 instance

```xml
<cac:ProofOfReexportationRequestDocumentReference>
  <cbc:ID>A2344</cbc:ID>
</cac:ProofOfReexportationRequestDocumentReference>
```

**Structure 13** — 1 instance

```xml
<cac:InvoiceDocumentReference>
  <cbc:ID>INV000123</cbc:ID>
  <cbc:IssueDate>2025-07-01</cbc:IssueDate>
</cac:InvoiceDocumentReference>
```

**Structure 14** — 5 instances

```xml
<cac:CatalogueDocumentReference>
  <cbc:ID>2005-9A</cbc:ID>
  <cbc:IssueDate>2005-11-03</cbc:IssueDate>
</cac:CatalogueDocumentReference>
```

**Structure 15** — 6 instances

```xml
<cac:ContractDocumentReference>
  <cbc:ID>GHJ76849</cbc:ID>
  <cbc:IssueDate>2002-08-13</cbc:IssueDate>
</cac:ContractDocumentReference>
```

**Structure 16** — 5 instances

```xml
<cac:ContractDocumentReference>
  <cbc:ID>Contract321</cbc:ID>
  <cbc:DocumentType>Framework agreement</cbc:DocumentType>
</cac:ContractDocumentReference>
```

**Structure 17** — 1 instance

```xml
<cac:DocumentReference>
  <cbc:ID>224087496582335</cbc:ID>
  <cbc:DocumentTypeCode>704</cbc:DocumentTypeCode>
</cac:DocumentReference>
```

**Structure 18** — 1 instance

```xml
<cac:DocumentReference>
  <cbc:ID>34563456</cbc:ID>
  <cbc:DocumentType>ATA carnet, paper</cbc:DocumentType>
</cac:DocumentReference>
```

**Structure 19** — 3 instances

```xml
<cac:ShipmentDocumentReference>
  <cbc:ID>GOA294107</cbc:ID>
  <cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
</cac:ShipmentDocumentReference>
```

**Structure 20** — 1 instance

```xml
<cac:SalesDocumentReference>
  <cbc:ID>PROFORMA001</cbc:ID>
  <cbc:DocumentType>Preliminary sales receipt</cbc:DocumentType>
</cac:SalesDocumentReference>
```

**Structure 21** — 10 instances

```xml
<cac:InvoiceDocumentReference>
  <cbc:ID>A00095678</cbc:ID>
  <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
  <cbc:IssueDate>2005-06-21</cbc:IssueDate>
</cac:InvoiceDocumentReference>
```

**Structure 22** — 6 instances

```xml
<cac:RequestForQuotationDocumentReference>
  <cbc:ID>G867B</cbc:ID>
  <cbc:UUID>8D076867-AE6D-439F-8281-5AAFC7F4E3B1</cbc:UUID>
  <cbc:IssueDate>2005-06-19</cbc:IssueDate>
</cac:RequestForQuotationDocumentReference>
```

**Structure 23** — 6 instances

```xml
<cac:DespatchDocumentReference>
  <cbc:ID>565899</cbc:ID>
  <cbc:UUID>88C7280E-8F10-419F-9949-8EFFFA2842B8</cbc:UUID>
  <cbc:IssueDate>2005-06-20</cbc:IssueDate>
</cac:DespatchDocumentReference>
```

**Structure 24** — 5 instances

```xml
<cac:CreditNoteDocumentReference>
  <cbc:ID>CN758494</cbc:ID>
  <cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
  <cbc:IssueDate>2005-06-25</cbc:IssueDate>
</cac:CreditNoteDocumentReference>
```

**Structure 25** — 4 instances

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>0665/2003</cbc:ID>
  <cbc:IssueDate>2013-06-23</cbc:IssueDate>
  <cbc:DocumentTypeCode>N380</cbc:DocumentTypeCode>
</cac:AdditionalDocumentReference>
```

**Structure 26** — 1 instance

```xml
<cac:ShipmentDocumentReference>
  <cbc:ID>ID168</cbc:ID>
  <cbc:DocumentTypeCode>Certificate of shipment</cbc:DocumentTypeCode>
  <cbc:DocumentType>Shipment reference</cbc:DocumentType>
</cac:ShipmentDocumentReference>
```

**Structure 27** — 1 instance

```xml
<cac:ReceiptDocumentReference>
  <cbc:ID>658398</cbc:ID>
  <cbc:UUID>89F82FA6-5331-491D-83BC-7B6CA7FD047C</cbc:UUID>
  <cbc:IssueDate>2005-06-21</cbc:IssueDate>
</cac:ReceiptDocumentReference>
```

**Structure 28** — 8 instances

```xml
<cac:DocumentReference>
  <cbc:ID>AEG012345</cbc:ID>
  <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
  <cbc:IssueDate>2005-06-20</cbc:IssueDate>
  <cbc:DocumentType>Order</cbc:DocumentType>
</cac:DocumentReference>
```

**Structure 29** — 2 instances

```xml
<cac:DocumentReference>
  <cbc:ID>W123</cbc:ID>
  <cbc:IssueDate>2016-11-02</cbc:IssueDate>
  <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
  <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
</cac:DocumentReference>
```

**Structure 30** — 1 instance

```xml
<cac:ContractDocumentReference>
  <cbc:ID>101</cbc:ID>
  <cbc:DocumentType>Annual Contract</cbc:DocumentType>
  <cac:Attachment>
    <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
  </cac:Attachment>
</cac:ContractDocumentReference>
```

**Structure 31** — 7 instances

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>Doc2</cbc:ID>
  <cbc:DocumentType>Drawing</cbc:DocumentType>
  <cac:Attachment>
    <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
  </cac:Attachment>
</cac:AdditionalDocumentReference>
```

**Structure 32** — 2 instances

```xml
<cac:ContractDocumentReference>
  <cbc:ID>TC101</cbc:ID>
  <cbc:IssueDate>2010-01-01</cbc:IssueDate>
  <cbc:DocumentTypeCode>315</cbc:DocumentTypeCode>
  <cbc:DocumentType>Contract</cbc:DocumentType>
  <cbc:DocumentDescription>Framework Agreement between Consignor and NECOSS</cbc:DocumentDescription>
</cac:ContractDocumentReference>
```

**Structure 33** — 1 instance

```xml
<cac:DocumentReference>
  <cbc:ID>W123</cbc:ID>
  <cbc:IssueDate>2016-11-02</cbc:IssueDate>
  <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
  <cbc:DocumentType></cbc:DocumentType>
  <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
</cac:DocumentReference>
```

**Structure 34** — 6 instances

```xml
<cac:DocumentReference>
  <cbc:ID>XD534533</cbc:ID>
  <cbc:DocumentType>BOL</cbc:DocumentType>
  <cac:IssuerParty>
    <cac:PartyName>
      <cbc:Name>Maersk</cbc:Name>
    </cac:PartyName>
  </cac:IssuerParty>
</cac:DocumentReference>
```

**Structure 35** — 7 instances

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>Doc1</cbc:ID>
  <cbc:DocumentType>Timesheet</cbc:DocumentType>
  <cac:Attachment>
    <cac:ExternalReference>
      <cbc:URI>http://www.suppliersite.eu/sheet001.html</cbc:URI>
    </cac:ExternalReference>
  </cac:Attachment>
</cac:AdditionalDocumentReference>
```

**Structure 36** — 1 instance

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>CA_1</cbc:ID>
  <cbc:IssueDate>2010-01-01</cbc:IssueDate>
  <cbc:DocumentTypeCode>CONTRACT</cbc:DocumentTypeCode>
  <cbc:DocumentType>FRAMEWORK AGREEMENT</cbc:DocumentType>
  <cac:ValidityPeriod>
    <cbc:StartDate>2010-01-01</cbc:StartDate>
    <cbc:EndDate>2011-01-01</cbc:EndDate>
  </cac:ValidityPeriod>
</cac:AdditionalDocumentReference>
```

**Structure 37** — 2 instances

```xml
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
```

**Structure 38** — 6 instances

```xml
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
```

[↑ Back to contents](#contents)

### `DocumentDistributionType`

**Used as:** `cac:DocumentDistribution`

_8 instances across 1 element, with 2 unique structures_

**Structure 1** — 4 instances

```xml
<cac:DocumentDistribution>
  <cbc:PrintQualifier>Copies allowed</cbc:PrintQualifier>
  <cbc:MaximumCopiesNumeric>5</cbc:MaximumCopiesNumeric>
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
</cac:DocumentDistribution>
```

**Structure 2** — 4 instances

```xml
<cac:DocumentDistribution>
  <cbc:PrintQualifier>Copies allowed</cbc:PrintQualifier>
  <cbc:MaximumCopiesNumeric>4</cbc:MaximumCopiesNumeric>
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
</cac:DocumentDistribution>
```

[↑ Back to contents](#contents)

### `DocumentMetadataType`

**Used as:** `cac:DigitalDocumentMetadata`

_12 instances across 1 element, with 1 unique structure_

**Structure 1** — 12 instances

```xml
<cac:DigitalDocumentMetadata>
  <cbc:FormatID>UBL</cbc:FormatID>
  <cbc:VersionID>2.2</cbc:VersionID>
  <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:Invoice-2</cbc:SchemaURI>
  <cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
</cac:DigitalDocumentMetadata>
```

[↑ Back to contents](#contents)

### `ExternalReferenceType`

**Used as:** `cac:ExternalReference`

_18 instances across 1 element, with 2 unique structures_

**Structure 1** — 10 instances

```xml
<cac:ExternalReference>
  <cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
</cac:ExternalReference>
```

**Structure 2** — 8 instances

```xml
<cac:ExternalReference>
  <cbc:URI>normalizedString</cbc:URI>
  <cbc:DocumentHash>String</cbc:DocumentHash>
  <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
  <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
</cac:ExternalReference>
```

[↑ Back to contents](#contents)

### `AttachmentType`

**Used as:** `cac:Attachment` · `cac:DigitalSignatureAttachment` · `cac:EncryptionCertificateAttachment`

_27 instances across 3 elements, with 6 unique structures_

**Structure 1** — 8 instances

```xml
<cac:Attachment>
  <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
</cac:Attachment>
```

**Structure 2** — 1 instance

```xml
<cac:EncryptionCertificateAttachment>
  <cbc:EmbeddedDocument>;lkajdf;lkasd;ljkasdf;lkja;sdlfkja;sldfkja;sdlfjkas;dlkfjas;dlfjas;dlkfjas;dlkfja;slkdjf</cbc:EmbeddedDocument>
</cac:EncryptionCertificateAttachment>
```

**Structure 3** — 7 instances

```xml
<cac:Attachment>
  <cac:ExternalReference>
    <cbc:URI>http://www.suppliersite.eu/sheet001.html</cbc:URI>
  </cac:ExternalReference>
</cac:Attachment>
```

**Structure 4** — 2 instances

```xml
<cac:DigitalSignatureAttachment>
  <cac:ExternalReference>
    <cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
  </cac:ExternalReference>
</cac:DigitalSignatureAttachment>
```

**Structure 5** — 1 instance

```xml
<cac:EncryptionCertificateAttachment>
  <cac:ExternalReference>
    <cbc:URI>www.digst.dk/udbud/NemID.cer</cbc:URI>
  </cac:ExternalReference>
</cac:EncryptionCertificateAttachment>
```

**Structure 6** — 8 instances

```xml
<cac:Attachment>
  <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
  <cac:ExternalReference>
    <cbc:URI>normalizedString</cbc:URI>
    <cbc:DocumentHash>String</cbc:DocumentHash>
    <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
    <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
  </cac:ExternalReference>
</cac:Attachment>
```

[↑ Back to contents](#contents)

### `ResponseType`

**Used as:** `cac:DiscrepancyResponse`

_5 instances across 1 element, with 1 unique structure_

**Structure 1** — 5 instances

```xml
<cac:DiscrepancyResponse>
  <cbc:ReferenceID>A00095678</cbc:ReferenceID>
  <cbc:Description>invoice cancelation</cbc:Description>
</cac:DiscrepancyResponse>
```

[↑ Back to contents](#contents)

### `StatusType`

**Used as:** `cac:CurrentStatus` · `cac:Status`

_3 instances across 2 elements, with 2 unique structures_

**Structure 1** — 2 instances

```xml
<cac:CurrentStatus>
  <cbc:ConditionCode>31</cbc:ConditionCode>
  <cbc:Description>En route</cbc:Description>
</cac:CurrentStatus>
```

**Structure 2** — 1 instance

```xml
<cac:Status>
  <cbc:ConditionCode>4</cbc:ConditionCode>
  <cbc:StatusReasonCode>23</cbc:StatusReasonCode>
  <cbc:StatusReason>Reefer container lost power - cargo of fish destroyed</cbc:StatusReason>
</cac:Status>
```

[↑ Back to contents](#contents)

### `Unknown`

**Used as:** `cac:ArrivalTransportLocation` · `cac:CarryingTransportMeans` · `cac:DepartureTransportLocation` · `cac:EstimatedArrivalPeriod` · `cac:ForecastExceptionCriteriaLine` · `cac:LegalTotal` · `cac:PlannedArrivalPeriod` · `cac:PlannedDeparturePeriod` · `cac:PostEventPeriod` · `cac:PriceMonetaryTotal` · `cac:ReferencedTransportHandlingUnit` · `cac:ServicePoint` · `cac:ServicePointLocation` · `cac:TaxSubTotal` · `cac:TransportItemStatus` · `cac:TransportStatus` · `cac:UpdatedDelivery`

_45 instances across 17 elements, with 25 unique structures_

**Structure 1** — 2 instances

```xml
<cac:PriceMonetaryTotal>
  <cbc:PayableAmount>300</cbc:PayableAmount>
</cac:PriceMonetaryTotal>
```

**Structure 2** — 3 instances

```xml
<cac:ReferencedTransportHandlingUnit>
  <cbc:ID>THU#2</cbc:ID>
</cac:ReferencedTransportHandlingUnit>
```

**Structure 3** — 1 instance

```xml
<cac:LegalTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:PayableAmount>100.00</cbc:PayableAmount>
</cac:LegalTotal>
```

**Structure 4** — 1 instance

```xml
<cac:PostEventPeriod>
  <cbc:DurationMeasure>30</cbc:DurationMeasure>
  <cbc:Description>Deviations shall be notified to the CONSIGNEE within max 30 minutes</cbc:Description>
</cac:PostEventPeriod>
```

**Structure 5** — 3 instances

```xml
<cac:LegalTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:LegalTotal>
```

**Structure 6** — 2 instances

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>31</cbc:TransportMeansTypeCode>
  <cac:RoadTransport>
    <cbc:LicensePlateID>KA04401</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:CarryingTransportMeans>
```

**Structure 7** — 1 instance

```xml
<cac:ForecastExceptionCriteriaLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriteriaLine>
```

**Structure 8** — 4 instances

```xml
<cac:PlannedDeparturePeriod>
  <cbc:StartDate>2011-03-14</cbc:StartDate>
  <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-14</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:PlannedDeparturePeriod>
```

**Structure 9** — 4 instances

```xml
<cac:PlannedArrivalPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>16:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>17:00:00.0Z</cbc:EndTime>
</cac:PlannedArrivalPeriod>
```

**Structure 10** — 1 instance

```xml
<cac:EstimatedArrivalPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>21:10:00.0Z</cbc:EndTime>
</cac:EstimatedArrivalPeriod>
```

**Structure 11** — 1 instance

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>2305</cbc:TransportMeansTypeCode>
  <cac:RailTransport>
    <cbc:TrainID>101</cbc:TrainID>
    <cbc:RailCarID>101-21</cbc:RailCarID>
  </cac:RailTransport>
</cac:CarryingTransportMeans>
```

**Structure 12** — 1 instance

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
  <cac:MaritimeTransport>
    <cbc:VesselID>IMO1234567</cbc:VesselID>
    <cbc:VesselName>MS Enova</cbc:VesselName>
  </cac:MaritimeTransport>
</cac:CarryingTransportMeans>
```

**Structure 13** — 1 instance

```xml
<cac:ForecastExceptionCriteriaLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriteriaLine>
```

**Structure 14** — 2 instances

```xml
<cac:UpdatedDelivery>
  <cac:EstimatedDeliveryPeriod>
    <cbc:StartDate>2010-04-30</cbc:StartDate>
    <cbc:StartTime>20:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2010-04-30</cbc:EndDate>
    <cbc:EndTime>20:30:00.0Z</cbc:EndTime>
  </cac:EstimatedDeliveryPeriod>
</cac:UpdatedDelivery>
```

**Structure 15** — 1 instance

```xml
<cac:ServicePointLocation>
  <cbc:Description>Bavaria area</cbc:Description>
  <cac:Address>
    <cbc:Region>Bavaria</cbc:Region>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      <cbc:Name>Germany</cbc:Name>
    </cac:Country>
  </cac:Address>
</cac:ServicePointLocation>
```

**Structure 16** — 4 instances

```xml
<cac:TaxSubTotal>
  <cbc:TaxableAmount>100.00</cbc:TaxableAmount>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:ID>A</cbc:ID>
    <cac:TaxScheme>
      <cbc:ID>UK VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubTotal>
```

**Structure 17** — 1 instance

```xml
<cac:TaxSubTotal>
  <cbc:TaxableAmount>100.00</cbc:TaxableAmount>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:ID>A</cbc:ID>
    <cbc:Percent>17.5</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>UK VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubTotal>
```

**Structure 18** — 1 instance

```xml
<cac:ServicePoint>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
  <cac:ServicePointLocation>
    <cbc:Description>Bavaria area</cbc:Description>
    <cac:Address>
      <cbc:Region>Bavaria</cbc:Region>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        <cbc:Name>Germany</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:ServicePointLocation>
  <cac:TransportMeans>
    <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
  </cac:TransportMeans>
</cac:ServicePoint>
```

**Structure 19** — 1 instance

```xml
<cac:DepartureTransportLocation>
  <cac:PlannedDeparturePeriod>
    <cbc:StartDate>2011-03-14</cbc:StartDate>
    <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-03-14</cbc:EndDate>
    <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
  </cac:PlannedDeparturePeriod>
  <cac:Location>
    <cbc:ID>NOOSL</cbc:ID>
    <cbc:LocationTypeCode>Baseport of discharge</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Akershusstranda 19</cbc:StreetName>
      <cbc:CityName>Oslo</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>NO</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:DepartureTransportLocation>
```

**Structure 20** — 1 instance

```xml
<cac:ArrivalTransportLocation>
  <cac:PlannedArrivalPeriod>
    <cbc:StartDate>2011-03-14</cbc:StartDate>
    <cbc:StartTime>15:30:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-03-14</cbc:EndDate>
    <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
  </cac:PlannedArrivalPeriod>
  <cac:Location>
    <cbc:ID>43125678</cbc:ID>
    <cbc:LocationTypeCode>Place of delivery</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Jordbærstien 2</cbc:StreetName>
      <cbc:CityName>Hamar</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>NO</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:ArrivalTransportLocation>
```

**Structure 21** — 3 instances

```xml
<cac:DepartureTransportLocation>
  <cac:PlannedDeparturePeriod>
    <cbc:StartDate>2011-03-13</cbc:StartDate>
    <cbc:StartTime>22:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-03-13</cbc:EndDate>
    <cbc:EndTime>22:30:00.0Z</cbc:EndTime>
  </cac:PlannedDeparturePeriod>
  <cac:Location>
    <cbc:ID>DEBREV</cbc:ID>
    <cbc:LocationTypeCode>Baseport of loading</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Heissestrasse 45</cbc:StreetName>
      <cbc:CityName>Munich</cbc:CityName>
      <cbc:PostalZone>80334</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:DepartureTransportLocation>
```

**Structure 22** — 3 instances

```xml
<cac:ArrivalTransportLocation>
  <cac:PlannedArrivalPeriod>
    <cbc:StartDate>2011-03-13</cbc:StartDate>
    <cbc:StartTime>16:30:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-03-13</cbc:EndDate>
    <cbc:EndTime>17:00:00.0Z</cbc:EndTime>
  </cac:PlannedArrivalPeriod>
  <cac:Location>
    <cbc:ID>987456123</cbc:ID>
    <cbc:Description>FORWARDER distribution centre in Munich</cbc:Description>
    <cbc:LocationTypeCode>Place of transhipment</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Volkerstrasse 6</cbc:StreetName>
      <cbc:CityName>Munich</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:ArrivalTransportLocation>
```

**Structure 23** — 1 instance

```xml
<cac:TransportItemStatus>
  <cbc:TransportItemTimeDeviationIndicator>true</cbc:TransportItemTimeDeviationIndicator>
  <cbc:TransportItemConditionDeviationIndicator>false</cbc:TransportItemConditionDeviationIndicator>
  <cac:UpdatedDelivery>
    <cac:EstimatedDeliveryPeriod>
      <cbc:StartDate>2010-04-30</cbc:StartDate>
      <cbc:StartTime>20:00:00.0Z</cbc:StartTime>
      <cbc:EndDate>2010-04-30</cbc:EndDate>
      <cbc:EndTime>20:30:00.0Z</cbc:EndTime>
    </cac:EstimatedDeliveryPeriod>
  </cac:UpdatedDelivery>
  <cac:StatusLocation>
    <cbc:LocationTypeCode>CUSTOMS OFFICE</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:CityName>STORLIEN</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>SE</cbc:IdentificationCode>
        <cbc:Name>SWEDEN</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:StatusLocation>
  <cac:TransportHandlingUnit>
    <cbc:ID>TI_101</cbc:ID>
  </cac:TransportHandlingUnit>
</cac:TransportItemStatus>
```

**Structure 24** — 1 instance

```xml
<cac:TransportStatus>
  <cbc:EstimatedArrivalDate>2010-04-30</cbc:EstimatedArrivalDate>
  <cbc:EstimatedArrivalTime>12:20:00.0Z</cbc:EstimatedArrivalTime>
  <cbc:EstimatedDepartureDate>2010-04-30</cbc:EstimatedDepartureDate>
  <cbc:EstimatedDepartureTime>13:20:00.0Z</cbc:EstimatedDepartureTime>
  <cbc:ActualArrivalDate>2010-04-30</cbc:ActualArrivalDate>
  <cbc:ActualArrivalTime>13:20:00.0Z</cbc:ActualArrivalTime>
  <cbc:ActualDepartureDate>2010-04-30</cbc:ActualDepartureDate>
  <cbc:ActualDepartureTime>14:20:00.0Z</cbc:ActualDepartureTime>
  <cbc:Remarks>DELAYED BY ONE HOUR</cbc:Remarks>
  <cbc:ReferenceDate>2010-04-30</cbc:ReferenceDate>
  <cbc:ReferenceTime>14:20:00.0Z</cbc:ReferenceTime>
  <cbc:ReliabilityPercent>100.0</cbc:ReliabilityPercent>
  <cac:StatusLocation>
    <cbc:ID>144</cbc:ID>
    <cbc:Description>OSLO CENTRAL RAILWAY STATION</cbc:Description>
    <cbc:LocationTypeCode>RAILWAY STATION</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:ID>133</cbc:ID>
      <cbc:StreetName>VIPPETANGEN</cbc:StreetName>
      <cbc:CityName>OSLO</cbc:CityName>
      <cbc:TimezoneOffset>GMT+1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>NO</cbc:IdentificationCode>
        <cbc:Name>NORWAY</cbc:Name>
      </cac:Country>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure>58</cbc:LatitudeDegreesMeasure>
        <cbc:LongitudeDegreesMeasure>10</cbc:LongitudeDegreesMeasure>
      </cac:LocationCoordinate>
    </cac:Address>
  </cac:StatusLocation>
</cac:TransportStatus>
```

**Structure 25** — 1 instance

```xml
<cac:TransportStatus>
  <cbc:TimeDeviationIndicator>true</cbc:TimeDeviationIndicator>
  <cbc:ConditionDeviationIndicator>false</cbc:ConditionDeviationIndicator>
  <cac:UpdatedDelivery>
    <cac:EstimatedDeliveryPeriod>
      <cbc:StartDate>2011-03-13</cbc:StartDate>
      <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
      <cbc:EndDate>2011-03-13</cbc:EndDate>
      <cbc:EndTime>21:00:00.0Z</cbc:EndTime>
    </cac:EstimatedDeliveryPeriod>
  </cac:UpdatedDelivery>
  <cac:StatusLocation>
    <cbc:ID>DEBREV</cbc:ID>
    <cbc:Description>Port of Bremerhaven</cbc:Description>
    <cbc:LocationTypeCode>Baseport of loading</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Hansestadt Bremisches</cbc:StreetName>
      <cbc:CityName>Bremen</cbc:CityName>
      <cac:AddressLine>
        <cbc:Line>Ueberseetor 2</cbc:Line>
      </cac:AddressLine>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure>53.33</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure>49</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode>North</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure>8.33</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure>49</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode>East</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:Address>
  </cac:StatusLocation>
  <cac:ReferencedTransportHandlingUnit>
    <cbc:ID>THU#1</cbc:ID>
  </cac:ReferencedTransportHandlingUnit>
  <cac:ReferencedTransportHandlingUnit>
    <cbc:ID>THU#2</cbc:ID>
  </cac:ReferencedTransportHandlingUnit>
  <cac:ReferencedTransportHandlingUnit>
    <cbc:ID>THU#3</cbc:ID>
  </cac:ReferencedTransportHandlingUnit>
</cac:TransportStatus>
```

[↑ Back to contents](#contents)

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)