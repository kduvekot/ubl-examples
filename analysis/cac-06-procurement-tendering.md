# UBL Element Reference — Procurement & Tendering

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **6** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [ProcurementProjectType](#ProcurementProjectType)
  - [ProcurementProjectLotReferenceType](#ProcurementProjectLotReferenceType)
  - [TenderingTermsType](#TenderingTermsType)
  - [TenderPreparationType](#TenderPreparationType)
  - [EvidenceType](#EvidenceType)
  - [ItemManagementProfileType](#ItemManagementProfileType)

---

## cac Elements — Procurement & Tendering

### `ProcurementProjectType`

**Used as:** `cac:ProcurementProject`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:ProcurementProject>
  <cbc:ID>DP</cbc:ID>
  <cbc:Name>DigitalPost</cbc:Name>
  <cbc:Description>Only Lot2</cbc:Description>
</cac:ProcurementProject>
```

[↑ Back to contents](#contents)

### `ProcurementProjectLotReferenceType`

**Used as:** `cac:ProcurementProjectLotReference`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:ProcurementProjectLotReference>
  <cbc:ID>Lot2</cbc:ID>
</cac:ProcurementProjectLotReference>
```

[↑ Back to contents](#contents)

### `TenderingTermsType`

**Used as:** `cac:TenderingTerms`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TenderingTerms>
  <cac:TenderPreparation>
    <cbc:TenderEnvelopeID>abc</cbc:TenderEnvelopeID>
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
  </cac:TenderPreparation>
</cac:TenderingTerms>
```

**Structure 2** — 1 instance

```xml
<cac:TenderingTerms>
  <cac:TenderPreparation>
    <cbc:TenderEnvelopeID>abc</cbc:TenderEnvelopeID>
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
  </cac:TenderPreparation>
</cac:TenderingTerms>
```

[↑ Back to contents](#contents)

### `TenderPreparationType`

**Used as:** `cac:TenderPreparation`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TenderPreparation>
  <cbc:TenderEnvelopeID>abc</cbc:TenderEnvelopeID>
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
</cac:TenderPreparation>
```

**Structure 2** — 1 instance

```xml
<cac:TenderPreparation>
  <cbc:TenderEnvelopeID>abc</cbc:TenderEnvelopeID>
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
</cac:TenderPreparation>
```

[↑ Back to contents](#contents)

### `EvidenceType`

**Used as:** `cac:ReexportationEvidence`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:ReexportationEvidence>
  <cbc:EvidenceTypeCode>mail</cbc:EvidenceTypeCode>
  <cbc:Description>Received mail from Frau Gerlung</cbc:Description>
  <cac:DocumentReference>
    <cbc:ID>34563456</cbc:ID>
    <cbc:DocumentType>ATA carnet, paper</cbc:DocumentType>
  </cac:DocumentReference>
</cac:ReexportationEvidence>
```

[↑ Back to contents](#contents)

### `ItemManagementProfileType`

**Used as:** `cac:ItemManagementProfile`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:ItemManagementProfile>
  <cbc:FrozenPeriodDaysNumeric>3</cbc:FrozenPeriodDaysNumeric>
  <cbc:MinimumInventoryQuantity>8</cbc:MinimumInventoryQuantity>
  <cbc:MultipleOrderQuantity>1</cbc:MultipleOrderQuantity>
  <cbc:OrderIntervalDaysNumeric>3</cbc:OrderIntervalDaysNumeric>
  <cbc:ReplenishmentOwnerDescription>Ownere-321</cbc:ReplenishmentOwnerDescription>
  <cbc:TargetServicePercent>1</cbc:TargetServicePercent>
  <cbc:TargetInventoryQuantity>20</cbc:TargetInventoryQuantity>
  <cac:EffectivePeriod>
    <cbc:StartDate>2005-02-26</cbc:StartDate>
    <cbc:EndDate>2005-12-26</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000584</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:Item>
  <cac:ItemLocationQuantity>
    <cbc:LeadTimeMeasure>3</cbc:LeadTimeMeasure>
    <cbc:MinimumQuantity>2</cbc:MinimumQuantity>
  </cac:ItemLocationQuantity>
</cac:ItemManagementProfile>
```

[↑ Back to contents](#contents)

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)