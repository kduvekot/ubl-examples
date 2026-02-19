# UBL Element Reference — Digital Services & Security

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **9** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [DigitalServiceType](#DigitalServiceType)
  - [DigitalAgreementTermsType](#DigitalAgreementTermsType)
  - [DigitalProcessType](#DigitalProcessType)
  - [DigitalCollaborationType](#DigitalCollaborationType)
  - [ServiceLevelAgreementType](#ServiceLevelAgreementType)
  - [MessageDeliveryType](#MessageDeliveryType)
  - [EncryptionDataType](#EncryptionDataType)
  - [EncryptionCertificatePathChainType](#EncryptionCertificatePathChainType)
  - [EncryptionSymmetricAlgorithmType](#EncryptionSymmetricAlgorithmType)

---

## cac Elements — Digital Services & Security

### `DigitalServiceType`

**Used as:** `cac:ReceivingDigitalService` · `cac:SendingDigitalService`

_12 instances across 2 elements, with 2 unique structures_

**Structure 1** — 6 instances

```xml
<cac:ReceivingDigitalService>
  <cbc:ID>CreditNote</cbc:ID>
  <cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns014:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
  <cac:DigitalDocumentMetadata>
    <cbc:FormatID>UBL</cbc:FormatID>
    <cbc:VersionID>2.2</cbc:VersionID>
    <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2</cbc:SchemaURI>
    <cbc:DocumentTypeCode>381</cbc:DocumentTypeCode>
  </cac:DigitalDocumentMetadata>
  <cac:DigitalDeliveryChannel>
    <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
    <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
    <cac:DigitalMessageDelivery>
      <cbc:ProtocolID>AS2</cbc:ProtocolID>
      <cbc:EndpointURI>http://as2.vendor.biz</cbc:EndpointURI>
    </cac:DigitalMessageDelivery>
  </cac:DigitalDeliveryChannel>
</cac:ReceivingDigitalService>
```

**Structure 2** — 6 instances

```xml
<cac:SendingDigitalService>
  <cbc:ID>Invoice</cbc:ID>
  <cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns010:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
  <cac:DigitalDocumentMetadata>
    <cbc:FormatID>UBL</cbc:FormatID>
    <cbc:VersionID>2.2</cbc:VersionID>
    <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:Invoice-2</cbc:SchemaURI>
    <cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
  </cac:DigitalDocumentMetadata>
  <cac:DigitalDeliveryChannel>
    <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
    <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
    <cbc:TestIndicator>true</cbc:TestIndicator>
    <cac:DigitalMessageDelivery>
      <cbc:ProtocolID>AS2</cbc:ProtocolID>
      <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
    </cac:DigitalMessageDelivery>
  </cac:DigitalDeliveryChannel>
</cac:SendingDigitalService>
```

[↑ Back to contents](#contents)

### `DigitalAgreementTermsType`

**Used as:** `cac:DigitalAgreementTerms`

_4 instances across 1 element, with 1 unique structure_

**Structure 1** — 4 instances

```xml
<cac:DigitalAgreementTerms>
  <cbc:Description>Trading Partner Agreement Terms</cbc:Description>
  <cac:AdoptionPeriod>
    <cbc:DurationMeasure>90</cbc:DurationMeasure>
  </cac:AdoptionPeriod>
  <cac:ServiceLevelAgreement>
    <cbc:ID>1</cbc:ID>
    <cbc:ServiceTypeCode>AP</cbc:ServiceTypeCode>
    <cbc:AvailabilityTimePercent>98.5</cbc:AvailabilityTimePercent>
    <cbc:MondayAvailabilityIndicator>true</cbc:MondayAvailabilityIndicator>
    <cbc:TuesdayAvailabilityIndicator>true</cbc:TuesdayAvailabilityIndicator>
    <cbc:WednesdayAvailabilityIndicator>true</cbc:WednesdayAvailabilityIndicator>
    <cbc:ThursdayAvailabilityIndicator>true</cbc:ThursdayAvailabilityIndicator>
    <cbc:FridayAvailabilityIndicator>true</cbc:FridayAvailabilityIndicator>
    <cbc:MinimumResponseTimeDurationMeasure>300</cbc:MinimumResponseTimeDurationMeasure>
    <cbc:MinimumDownTimeScheduleDurationMeasure>3</cbc:MinimumDownTimeScheduleDurationMeasure>
    <cbc:MaximumIncidentNotificationDurationMeasure>4</cbc:MaximumIncidentNotificationDurationMeasure>
    <cbc:MaximumDataLossDurationMeasure>24</cbc:MaximumDataLossDurationMeasure>
    <cbc:MeanTimeToRecoverDurationMeasure>3</cbc:MeanTimeToRecoverDurationMeasure>
    <cac:ServiceAvailabilityPeriod>
      <cbc:StartTime>09:00:00</cbc:StartTime>
      <cbc:EndTime>16:00:00</cbc:EndTime>
    </cac:ServiceAvailabilityPeriod>
    <cac:ServiceMaintenancePeriod>
      <cbc:StartTime>22:00:00</cbc:StartTime>
      <cbc:EndTime>06:00:00</cbc:EndTime>
    </cac:ServiceMaintenancePeriod>
  </cac:ServiceLevelAgreement>
  <cac:ServiceLevelAgreement>
    <cbc:ID>2</cbc:ID>
    <cbc:ServiceTypeCode>AP</cbc:ServiceTypeCode>
    <cbc:AvailabilityTimePercent>94.0</cbc:AvailabilityTimePercent>
    <cbc:SaturdayAvailabilityIndicator>true</cbc:SaturdayAvailabilityIndicator>
    <cbc:SundayAvailabilityIndicator>true</cbc:SundayAvailabilityIndicator>
    <cac:ServiceAvailabilityPeriod>
      <cbc:StartTime>09:00:00</cbc:StartTime>
      <cbc:EndTime>16:00:00</cbc:EndTime>
    </cac:ServiceAvailabilityPeriod>
    <cac:ServiceMaintenancePeriod>
      <cbc:StartTime>22:00:00</cbc:StartTime>
      <cbc:EndTime>06:00:00</cbc:EndTime>
    </cac:ServiceMaintenancePeriod>
  </cac:ServiceLevelAgreement>
</cac:DigitalAgreementTerms>
```

[↑ Back to contents](#contents)

### `DigitalProcessType`

**Used as:** `cac:DigitalProcess`

_6 instances across 1 element, with 1 unique structure_

**Structure 1** — 6 instances

```xml
<cac:DigitalProcess>
  <cbc:ID>1</cbc:ID>
  <cbc:ProfileID>urn:www.cenbii.eu:profile:bii05:ver2.0</cbc:ProfileID>
  <cac:DigitalCollaboration>
    <cbc:ID>1</cbc:ID>
    <cac:SendingDigitalService>
      <cbc:ID>Invoice</cbc:ID>
      <cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns010:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
      <cac:DigitalDocumentMetadata>
        <cbc:FormatID>UBL</cbc:FormatID>
        <cbc:VersionID>2.2</cbc:VersionID>
        <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:Invoice-2</cbc:SchemaURI>
        <cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
      </cac:DigitalDocumentMetadata>
      <cac:DigitalDeliveryChannel>
        <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
        <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
        <cbc:TestIndicator>true</cbc:TestIndicator>
        <cac:DigitalMessageDelivery>
          <cbc:ProtocolID>AS2</cbc:ProtocolID>
          <cbc:EndpointURI>http://as2.buyer.de</cbc:EndpointURI>
        </cac:DigitalMessageDelivery>
      </cac:DigitalDeliveryChannel>
    </cac:SendingDigitalService>
    <cac:ReceivingDigitalService>
      <cbc:ID>CreditNote</cbc:ID>
      <cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns014:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
      <cac:DigitalDocumentMetadata>
        <cbc:FormatID>UBL</cbc:FormatID>
        <cbc:VersionID>2.2</cbc:VersionID>
        <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2</cbc:SchemaURI>
        <cbc:DocumentTypeCode>381</cbc:DocumentTypeCode>
      </cac:DigitalDocumentMetadata>
      <cac:DigitalDeliveryChannel>
        <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
        <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
        <cac:DigitalMessageDelivery>
          <cbc:ProtocolID>AS2</cbc:ProtocolID>
          <cbc:EndpointURI>http://as2.vendor.biz</cbc:EndpointURI>
        </cac:DigitalMessageDelivery>
      </cac:DigitalDeliveryChannel>
    </cac:ReceivingDigitalService>
  </cac:DigitalCollaboration>
</cac:DigitalProcess>
```

[↑ Back to contents](#contents)

### `DigitalCollaborationType`

**Used as:** `cac:DigitalCollaboration`

_6 instances across 1 element, with 1 unique structure_

**Structure 1** — 6 instances

```xml
<cac:DigitalCollaboration>
  <cbc:ID>1</cbc:ID>
  <cac:SendingDigitalService>
    <cbc:ID>Invoice</cbc:ID>
    <cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns010:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
    <cac:DigitalDocumentMetadata>
      <cbc:FormatID>UBL</cbc:FormatID>
      <cbc:VersionID>2.2</cbc:VersionID>
      <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:Invoice-2</cbc:SchemaURI>
      <cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
    </cac:DigitalDocumentMetadata>
    <cac:DigitalDeliveryChannel>
      <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
      <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
      <cbc:TestIndicator>true</cbc:TestIndicator>
      <cac:DigitalMessageDelivery>
        <cbc:ProtocolID>AS2</cbc:ProtocolID>
        <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
      </cac:DigitalMessageDelivery>
    </cac:DigitalDeliveryChannel>
  </cac:SendingDigitalService>
  <cac:ReceivingDigitalService>
    <cbc:ID>CreditNote</cbc:ID>
    <cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns014:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
    <cac:DigitalDocumentMetadata>
      <cbc:FormatID>UBL</cbc:FormatID>
      <cbc:VersionID>2.2</cbc:VersionID>
      <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2</cbc:SchemaURI>
      <cbc:DocumentTypeCode>381</cbc:DocumentTypeCode>
    </cac:DigitalDocumentMetadata>
    <cac:DigitalDeliveryChannel>
      <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
      <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
      <cac:DigitalMessageDelivery>
        <cbc:ProtocolID>AS2</cbc:ProtocolID>
        <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
      </cac:DigitalMessageDelivery>
    </cac:DigitalDeliveryChannel>
  </cac:ReceivingDigitalService>
</cac:DigitalCollaboration>
```

[↑ Back to contents](#contents)

### `ServiceLevelAgreementType`

**Used as:** `cac:ServiceLevelAgreement`

_8 instances across 1 element, with 2 unique structures_

**Structure 1** — 4 instances

```xml
<cac:ServiceLevelAgreement>
  <cbc:ID>2</cbc:ID>
  <cbc:ServiceTypeCode>AP</cbc:ServiceTypeCode>
  <cbc:AvailabilityTimePercent>94.0</cbc:AvailabilityTimePercent>
  <cbc:SaturdayAvailabilityIndicator>true</cbc:SaturdayAvailabilityIndicator>
  <cbc:SundayAvailabilityIndicator>true</cbc:SundayAvailabilityIndicator>
  <cac:ServiceAvailabilityPeriod>
    <cbc:StartTime>09:00:00Z</cbc:StartTime>
    <cbc:EndTime>16:00:00Z</cbc:EndTime>
  </cac:ServiceAvailabilityPeriod>
  <cac:ServiceMaintenancePeriod>
    <cbc:StartTime>22:00:00Z</cbc:StartTime>
    <cbc:EndTime>06:00:00Z</cbc:EndTime>
  </cac:ServiceMaintenancePeriod>
</cac:ServiceLevelAgreement>
```

**Structure 2** — 4 instances

```xml
<cac:ServiceLevelAgreement>
  <cbc:ID>1</cbc:ID>
  <cbc:ServiceTypeCode>AP</cbc:ServiceTypeCode>
  <cbc:AvailabilityTimePercent>98.5</cbc:AvailabilityTimePercent>
  <cbc:MondayAvailabilityIndicator>true</cbc:MondayAvailabilityIndicator>
  <cbc:TuesdayAvailabilityIndicator>true</cbc:TuesdayAvailabilityIndicator>
  <cbc:WednesdayAvailabilityIndicator>true</cbc:WednesdayAvailabilityIndicator>
  <cbc:ThursdayAvailabilityIndicator>true</cbc:ThursdayAvailabilityIndicator>
  <cbc:FridayAvailabilityIndicator>true</cbc:FridayAvailabilityIndicator>
  <cbc:MinimumResponseTimeDurationMeasure>300</cbc:MinimumResponseTimeDurationMeasure>
  <cbc:MinimumDownTimeScheduleDurationMeasure>3</cbc:MinimumDownTimeScheduleDurationMeasure>
  <cbc:MaximumIncidentNotificationDurationMeasure>4</cbc:MaximumIncidentNotificationDurationMeasure>
  <cbc:MaximumDataLossDurationMeasure>24</cbc:MaximumDataLossDurationMeasure>
  <cbc:MeanTimeToRecoverDurationMeasure>3</cbc:MeanTimeToRecoverDurationMeasure>
  <cac:ServiceAvailabilityPeriod>
    <cbc:StartTime>09:00:00Z</cbc:StartTime>
    <cbc:EndTime>16:00:00Z</cbc:EndTime>
  </cac:ServiceAvailabilityPeriod>
  <cac:ServiceMaintenancePeriod>
    <cbc:StartTime>22:00:00Z</cbc:StartTime>
    <cbc:EndTime>06:00:00Z</cbc:EndTime>
  </cac:ServiceMaintenancePeriod>
</cac:ServiceLevelAgreement>
```

[↑ Back to contents](#contents)

### `MessageDeliveryType`

**Used as:** `cac:DigitalMessageDelivery`

_12 instances across 1 element, with 1 unique structure_

**Structure 1** — 12 instances

```xml
<cac:DigitalMessageDelivery>
  <cbc:ProtocolID>AS2</cbc:ProtocolID>
  <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
</cac:DigitalMessageDelivery>
```

[↑ Back to contents](#contents)

### `EncryptionDataType`

**Used as:** `cac:TenderEncryptionData`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TenderEncryptionData>
  <cbc:MessageFormat>1.2.840.113549.1.9.16.0.1</cbc:MessageFormat>
  <cac:EncryptionCertificateAttachment>
    <cbc:EmbeddedDocument>;lkajdf;lkasd;ljkasdf;lkja;sdlfkja;sldfkja;sdlfjkas;dlkfjas;dlfjas;dlkfjas;dlkfja;slkdjf</cbc:EmbeddedDocument>
  </cac:EncryptionCertificateAttachment>
  <cac:EncryptionCertificatePathChain>
    <cbc:Value>TRUST2408 OCES Primary CA – TRUST2408 OCES CA II</cbc:Value>
  </cac:EncryptionCertificatePathChain>
  <cac:EncryptionSymmetricAlgorithm>
    <cbc:OID>2.16.840.1.101.3.4.1.2</cbc:OID>
  </cac:EncryptionSymmetricAlgorithm>
  <cac:EncryptionSymmetricAlgorithm>
    <cbc:OID>2.16.840.1.101.3.4.1.42</cbc:OID>
  </cac:EncryptionSymmetricAlgorithm>
</cac:TenderEncryptionData>
```

**Structure 2** — 1 instance

```xml
<cac:TenderEncryptionData>
  <cbc:MessageFormat>1.2.840.113549.1.9.16.0.1</cbc:MessageFormat>
  <cac:EncryptionCertificateAttachment>
    <cac:ExternalReference>
      <cbc:URI>www.digst.dk/udbud/NemID.cer</cbc:URI>
    </cac:ExternalReference>
  </cac:EncryptionCertificateAttachment>
  <cac:EncryptionCertificatePathChain>
    <cbc:URI>https://www.trust2408/certPaths/Trust2408_issuingCA12_chain.p7c</cbc:URI>
  </cac:EncryptionCertificatePathChain>
  <cac:EncryptionSymmetricAlgorithm>
    <cbc:OID>2.16.840.1.101.3.4.1.2</cbc:OID>
  </cac:EncryptionSymmetricAlgorithm>
  <cac:EncryptionSymmetricAlgorithm>
    <cbc:OID>2.16.840.1.101.3.4.1.42</cbc:OID>
  </cac:EncryptionSymmetricAlgorithm>
</cac:TenderEncryptionData>
```

[↑ Back to contents](#contents)

### `EncryptionCertificatePathChainType`

**Used as:** `cac:EncryptionCertificatePathChain`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:EncryptionCertificatePathChain>
  <cbc:Value>TRUST2408 OCES Primary CA – TRUST2408 OCES CA II</cbc:Value>
</cac:EncryptionCertificatePathChain>
```

**Structure 2** — 1 instance

```xml
<cac:EncryptionCertificatePathChain>
  <cbc:URI>https://www.trust2408/certPaths/Trust2408_issuingCA12_chain.p7c</cbc:URI>
</cac:EncryptionCertificatePathChain>
```

[↑ Back to contents](#contents)

### `EncryptionSymmetricAlgorithmType`

**Used as:** `cac:EncryptionSymmetricAlgorithm`

_4 instances across 1 element, with 1 unique structure_

**Structure 1** — 4 instances

```xml
<cac:EncryptionSymmetricAlgorithm>
  <cbc:OID>2.16.840.1.101.3.4.1.2</cbc:OID>
</cac:EncryptionSymmetricAlgorithm>
```

[↑ Back to contents](#contents)

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)