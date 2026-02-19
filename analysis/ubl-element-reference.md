# UBL Element Reference

Values, attributes, and composite instances observed across all official UBL example documents (2.0 – 2.5), grouped using the UBL 2.5 CSD02 XSD as the authoritative type reference.

## Contents

- [Summary](#summary)
- [cbc Elements](#cbc-elements)
  - [Amount](#udtAmountType)
  - [Binary Object](#udtBinaryObjectType)
  - [Code](#udtCodeType)
  - [Date](#udtDateType)
  - [Identifier](#udtIdentifierType)
  - [Indicator](#udtIndicatorType)
  - [Measure](#udtMeasureType)
  - [Name](#udtNameType)
  - [Numeric](#udtNumericType)
  - [Percent](#udtPercentType)
  - [Quantity](#udtQuantityType)
  - [Rate](#udtRateType)
  - [Text](#udtTextType)
  - [Time](#udtTimeType)
- [cac Elements](#cac-elements)
  - [ActivityDataLineType](#ActivityDataLineType)
  - [AddressLineType](#AddressLineType)
  - [AddressType](#AddressType)
  - [AirTransportType](#AirTransportType)
  - [AllowanceChargeType](#AllowanceChargeType)
  - [AttachmentType](#AttachmentType)
  - [AttestationLineType](#AttestationLineType)
  - [AttestationType](#AttestationType)
  - [BillingReferenceType](#BillingReferenceType)
  - [BranchType](#BranchType)
  - [CapabilityType](#CapabilityType)
  - [CashRegisterType](#CashRegisterType)
  - [CommodityClassificationType](#CommodityClassificationType)
  - [ConsignmentType](#ConsignmentType)
  - [ContactType](#ContactType)
  - [ContractType](#ContractType)
  - [ContractingPartyType](#ContractingPartyType)
  - [CountryType](#CountryType)
  - [CreditNoteLineType](#CreditNoteLineType)
  - [CustomerPartyType](#CustomerPartyType)
  - [CustomsDeclarationType](#CustomsDeclarationType)
  - [DebitNoteLineType](#DebitNoteLineType)
  - [DeliveryChannelType](#DeliveryChannelType)
  - [DeliveryTermsType](#DeliveryTermsType)
  - [DeliveryType](#DeliveryType)
  - [DespatchLineType](#DespatchLineType)
  - [DespatchType](#DespatchType)
  - [DigitalAgreementTermsType](#DigitalAgreementTermsType)
  - [DigitalCollaborationType](#DigitalCollaborationType)
  - [DigitalProcessType](#DigitalProcessType)
  - [DigitalServiceType](#DigitalServiceType)
  - [DimensionType](#DimensionType)
  - [DocumentDistributionType](#DocumentDistributionType)
  - [DocumentMetadataType](#DocumentMetadataType)
  - [DocumentReferenceType](#DocumentReferenceType)
  - [EconomicOperatorPartyType](#EconomicOperatorPartyType)
  - [EncryptionCertificatePathChainType](#EncryptionCertificatePathChainType)
  - [EncryptionDataType](#EncryptionDataType)
  - [EncryptionSymmetricAlgorithmType](#EncryptionSymmetricAlgorithmType)
  - [EndorsementType](#EndorsementType)
  - [EndorserPartyType](#EndorserPartyType)
  - [EnvironmentalEmissionType](#EnvironmentalEmissionType)
  - [EventLineItemType](#EventLineItemType)
  - [EventTacticEnumerationType](#EventTacticEnumerationType)
  - [EventTacticType](#EventTacticType)
  - [EvidenceType](#EvidenceType)
  - [ExceptionCriteriaLineType](#ExceptionCriteriaLineType)
  - [ExceptionNotificationLineType](#ExceptionNotificationLineType)
  - [ExchangeRateType](#ExchangeRateType)
  - [ExternalReferenceType](#ExternalReferenceType)
  - [FinancialAccountType](#FinancialAccountType)
  - [FinancialInstitutionType](#FinancialInstitutionType)
  - [ForecastExceptionCriterionLineType](#ForecastExceptionCriterionLineType)
  - [ForecastExceptionType](#ForecastExceptionType)
  - [ForecastLineType](#ForecastLineType)
  - [ForecastRevisionLineType](#ForecastRevisionLineType)
  - [GoodsItemPassportCounterfoilType](#GoodsItemPassportCounterfoilType)
  - [GoodsItemType](#GoodsItemType)
  - [InstructionForReturnsLineType](#InstructionForReturnsLineType)
  - [InventoryReportLineType](#InventoryReportLineType)
  - [InvoiceLineType](#InvoiceLineType)
  - [ItemIdentificationType](#ItemIdentificationType)
  - [ItemInstanceType](#ItemInstanceType)
  - [ItemLocationQuantityType](#ItemLocationQuantityType)
  - [ItemManagementProfileType](#ItemManagementProfileType)
  - [ItemPropertyType](#ItemPropertyType)
  - [ItemType](#ItemType)
  - [LanguageType](#LanguageType)
  - [LineItemType](#LineItemType)
  - [LocationCoordinateType](#LocationCoordinateType)
  - [LocationType](#LocationType)
  - [LotIdentificationType](#LotIdentificationType)
  - [MaritimeTransportType](#MaritimeTransportType)
  - [MessageDeliveryType](#MessageDeliveryType)
  - [MonetaryTotalType](#MonetaryTotalType)
  - [NotificationRequirementType](#NotificationRequirementType)
  - [OrderLineReferenceType](#OrderLineReferenceType)
  - [OrderLineType](#OrderLineType)
  - [OrderReferenceType](#OrderReferenceType)
  - [PackageType](#PackageType)
  - [ParticipantPartyType](#ParticipantPartyType)
  - [PartyIdentificationType](#PartyIdentificationType)
  - [PartyLegalEntityType](#PartyLegalEntityType)
  - [PartyNameType](#PartyNameType)
  - [PartyTaxSchemeType](#PartyTaxSchemeType)
  - [PartyType](#PartyType)
  - [PaymentMeansType](#PaymentMeansType)
  - [PaymentTermsType](#PaymentTermsType)
  - [PaymentType](#PaymentType)
  - [PerformanceDataLineType](#PerformanceDataLineType)
  - [PeriodType](#PeriodType)
  - [PersonType](#PersonType)
  - [PickupType](#PickupType)
  - [PriceType](#PriceType)
  - [ProcurementProjectLotReferenceType](#ProcurementProjectLotReferenceType)
  - [ProcurementProjectType](#ProcurementProjectType)
  - [PromotionalEventLineItemType](#PromotionalEventLineItemType)
  - [PromotionalEventType](#PromotionalEventType)
  - [PromotionalSpecificationType](#PromotionalSpecificationType)
  - [PurchaseReceiptLineType](#PurchaseReceiptLineType)
  - [PurchaseReferenceType](#PurchaseReferenceType)
  - [QuotationLineType](#QuotationLineType)
  - [RailTransportType](#RailTransportType)
  - [ReceiptLineType](#ReceiptLineType)
  - [ReminderLineType](#ReminderLineType)
  - [RemittanceAdviceLineType](#RemittanceAdviceLineType)
  - [RequestForQuotationLineType](#RequestForQuotationLineType)
  - [ResponseType](#ResponseType)
  - [RetailPlannedImpactType](#RetailPlannedImpactType)
  - [RoadTransportType](#RoadTransportType)
  - [SalesItemType](#SalesItemType)
  - [ServiceLevelAgreementType](#ServiceLevelAgreementType)
  - [ShipmentStageType](#ShipmentStageType)
  - [ShipmentType](#ShipmentType)
  - [SignatureType](#SignatureType)
  - [SocialMediaProfileType](#SocialMediaProfileType)
  - [StatementLineType](#StatementLineType)
  - [StatusType](#StatusType)
  - [StockAvailabilityReportLineType](#StockAvailabilityReportLineType)
  - [SupplierPartyType](#SupplierPartyType)
  - [TaxCategoryType](#TaxCategoryType)
  - [TaxSchemeType](#TaxSchemeType)
  - [TaxSubtotalType](#TaxSubtotalType)
  - [TaxTotalType](#TaxTotalType)
  - [TemperatureType](#TemperatureType)
  - [TenderPreparationType](#TenderPreparationType)
  - [TenderingTermsType](#TenderingTermsType)
  - [TransactionConditionsType](#TransactionConditionsType)
  - [TransportEquipmentSealType](#TransportEquipmentSealType)
  - [TransportEquipmentType](#TransportEquipmentType)
  - [TransportEventType](#TransportEventType)
  - [TransportExecutionTermsType](#TransportExecutionTermsType)
  - [TransportHandlingUnitType](#TransportHandlingUnitType)
  - [TransportMeansType](#TransportMeansType)
  - [TransportScheduleType](#TransportScheduleType)
  - [TransportationSegmentType](#TransportationSegmentType)
  - [TransportationServiceType](#TransportationServiceType)
  - [Unknown](#Unknown)
  - [VerifiedGrossMassType](#VerifiedGrossMassType)
  - [WebSiteType](#WebSiteType)

---

## Summary

| | Count |
|---|---|
| `cbc` elements (in examples) | **388** |
| `cbc` unique values | **2272** |
| `cbc` elements with attributes | **104** |
| `cac` elements (in examples) | **317** |
| `cac` unique ABIE types used | **140** |
| `cac` unique instances | **7428** |

[↑ Back to contents](#contents)

---

## cbc Elements

_Grouped by UN/CEFACT base data type from `UBL-CommonBasicComponents-2.5.xsd`._

### Amount (`udt:AmountType`)

_34 elements_

#### `cbc:AllowanceTotalAmount`

```xml
<cbc:AllowanceTotalAmount>10.00</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount>100</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount>5.00</cbc:AllowanceTotalAmount>
```

**`@currencyID`**

```xml
<cbc:AllowanceTotalAmount currencyID="EUR">100</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount currencyID="GBP">10.00</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount currencyID="SEK">100</cbc:AllowanceTotalAmount>
```

#### `cbc:Amount`

```xml
<cbc:Amount>0.275</cbc:Amount>
<cbc:Amount>1.00</cbc:Amount>
<cbc:Amount>100</cbc:Amount>
<cbc:Amount>100.0</cbc:Amount>
<cbc:Amount>12</cbc:Amount>
```
_10 more values in examples_

**`@currencyID`**

```xml
<cbc:Amount currencyID="DKK">0.00</cbc:Amount>
<cbc:Amount currencyID="EUR">0.275</cbc:Amount>
<cbc:Amount currencyID="USD">12.70</cbc:Amount>
```

#### `cbc:BalanceAmount`

```xml
<cbc:BalanceAmount>-107.50</cbc:BalanceAmount>
<cbc:BalanceAmount>107.50</cbc:BalanceAmount>
```

**`@currencyID`**

```xml
<cbc:BalanceAmount currencyID="GBP">-107.50</cbc:BalanceAmount>
```

#### `cbc:BaseAmount`

```xml
<cbc:BaseAmount>1500</cbc:BaseAmount>
<cbc:BaseAmount>2.75</cbc:BaseAmount>
<cbc:BaseAmount>254.00</cbc:BaseAmount>
```

**`@currencyID`**

```xml
<cbc:BaseAmount currencyID="EUR">1500</cbc:BaseAmount>
<cbc:BaseAmount currencyID="USD">254.00</cbc:BaseAmount>
```

#### `cbc:CashChangeAmount`

```xml
<cbc:CashChangeAmount>5.00</cbc:CashChangeAmount>
```

**`@currencyID`**

```xml
<cbc:CashChangeAmount currencyID="EUR">5.00</cbc:CashChangeAmount>
```

#### `cbc:ChargeTotalAmount`

```xml
<cbc:ChargeTotalAmount>1.00</cbc:ChargeTotalAmount>
<cbc:ChargeTotalAmount>10.00</cbc:ChargeTotalAmount>
<cbc:ChargeTotalAmount>100</cbc:ChargeTotalAmount>
```

**`@currencyID`**

```xml
<cbc:ChargeTotalAmount currencyID="EUR">1.00</cbc:ChargeTotalAmount>
<cbc:ChargeTotalAmount currencyID="SEK">100</cbc:ChargeTotalAmount>
```

#### `cbc:CreditLineAmount`

```xml
<cbc:CreditLineAmount>0.00</cbc:CreditLineAmount>
<cbc:CreditLineAmount>107.50</cbc:CreditLineAmount>
```

**`@currencyID`**

```xml
<cbc:CreditLineAmount currencyID="GBP">0.00</cbc:CreditLineAmount>
```

#### `cbc:DebitLineAmount`

```xml
<cbc:DebitLineAmount>0.00</cbc:DebitLineAmount>
<cbc:DebitLineAmount>107.50</cbc:DebitLineAmount>
```

**`@currencyID`**

```xml
<cbc:DebitLineAmount currencyID="GBP">0.00</cbc:DebitLineAmount>
```

#### `cbc:DeclaredCarriageValueAmount`

```xml
<cbc:DeclaredCarriageValueAmount>1500.00</cbc:DeclaredCarriageValueAmount>
```

**`@currencyID`**

```xml
<cbc:DeclaredCarriageValueAmount currencyID="USD">1500.00</cbc:DeclaredCarriageValueAmount>
```

#### `cbc:DeclaredCustomsValueAmount`

```xml
<cbc:DeclaredCustomsValueAmount>0.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>2500.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>3000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>500.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>5000.00</cbc:DeclaredCustomsValueAmount>
```
_6 more values in examples_

**`@currencyID`**

```xml
<cbc:DeclaredCustomsValueAmount currencyID="DKK">0.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="EUR">0.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="GBP">524.80</cbc:DeclaredCustomsValueAmount>
```

#### `cbc:DeclaredStatisticsValueAmount`

```xml
<cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>10050.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>2500.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>3000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>34800.00</cbc:DeclaredStatisticsValueAmount>
```
_9 more values in examples_

**`@currencyID`**

```xml
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">1000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="EUR">182.62</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="USD">1000.00</cbc:DeclaredStatisticsValueAmount>
```

#### `cbc:FreeOnBoardValueAmount`

```xml
<cbc:FreeOnBoardValueAmount>1200.00</cbc:FreeOnBoardValueAmount>
<cbc:FreeOnBoardValueAmount>1241.30</cbc:FreeOnBoardValueAmount>
```

**`@currencyID`**

```xml
<cbc:FreeOnBoardValueAmount currencyID="USD">1200.00</cbc:FreeOnBoardValueAmount>
```

#### `cbc:InsuranceValueAmount`

```xml
<cbc:InsuranceValueAmount>1000.00</cbc:InsuranceValueAmount>
<cbc:InsuranceValueAmount>1241.30</cbc:InsuranceValueAmount>
```

**`@currencyID`**

```xml
<cbc:InsuranceValueAmount currencyID="USD">1000.00</cbc:InsuranceValueAmount>
```

#### `cbc:InventoryValueAmount`

```xml
<cbc:InventoryValueAmount>200</cbc:InventoryValueAmount>
<cbc:InventoryValueAmount>300</cbc:InventoryValueAmount>
<cbc:InventoryValueAmount>750</cbc:InventoryValueAmount>
```

**`@currencyID`**

```xml
<cbc:InventoryValueAmount currencyID="EUR">200</cbc:InventoryValueAmount>
```

#### `cbc:LineExtensionAmount`

```xml
<cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>1750.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>197750.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>6225</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>7.20</cbc:LineExtensionAmount>
```
_17 more values in examples_

**`@currencyID`**

```xml
<cbc:LineExtensionAmount currencyID="GBP">100.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="SEK">12000</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="USD">1000.00</cbc:LineExtensionAmount>
```

#### `cbc:PaidAmount`

```xml
<cbc:PaidAmount>25.00</cbc:PaidAmount>
```

**`@currencyID`**

```xml
<cbc:PaidAmount currencyID="EUR">25.00</cbc:PaidAmount>
```

#### `cbc:PaidCashAmount`

```xml
<cbc:PaidCashAmount>30.00</cbc:PaidCashAmount>
```

**`@currencyID`**

```xml
<cbc:PaidCashAmount currencyID="EUR">30.00</cbc:PaidCashAmount>
```

#### `cbc:PayableAmount`

```xml
<cbc:PayableAmount>100.00</cbc:PayableAmount>
<cbc:PayableAmount>1000.00</cbc:PayableAmount>
<cbc:PayableAmount>247187.50</cbc:PayableAmount>
<cbc:PayableAmount>300</cbc:PayableAmount>
<cbc:PayableAmount>6225</cbc:PayableAmount>
```
_5 more values in examples_

**`@currencyID`**

```xml
<cbc:PayableAmount currencyID="DKK">247187.50</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">2000</cbc:PayableAmount>
<cbc:PayableAmount currencyID="USD">1000.00</cbc:PayableAmount>
```

#### `cbc:PayableRoundingAmount`

```xml
<cbc:PayableRoundingAmount>0.30</cbc:PayableRoundingAmount>
```

**`@currencyID`**

```xml
<cbc:PayableRoundingAmount currencyID="EUR">0.30</cbc:PayableRoundingAmount>
```

#### `cbc:PrepaidAmount`

```xml
<cbc:PrepaidAmount>1000</cbc:PrepaidAmount>
```

**`@currencyID`**

```xml
<cbc:PrepaidAmount currencyID="EUR">1000</cbc:PrepaidAmount>
```

#### `cbc:PriceAmount`

```xml
<cbc:PriceAmount>10.00</cbc:PriceAmount>
<cbc:PriceAmount>100.00</cbc:PriceAmount>
<cbc:PriceAmount>1273</cbc:PriceAmount>
<cbc:PriceAmount>25</cbc:PriceAmount>
<cbc:PriceAmount>50.00</cbc:PriceAmount>
```
_12 more values in examples_

**`@currencyID`**

```xml
<cbc:PriceAmount currencyID="DKK">1250.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="GBP">1.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="SEK">15</cbc:PriceAmount>
```

#### `cbc:TaxAmount`

```xml
<cbc:TaxAmount>-0.396</cbc:TaxAmount>
<cbc:TaxAmount>0.496</cbc:TaxAmount>
<cbc:TaxAmount>1.80</cbc:TaxAmount>
<cbc:TaxAmount>4.00</cbc:TaxAmount>
<cbc:TaxAmount>5.80</cbc:TaxAmount>
```
_10 more values in examples_

**`@currencyID`**

```xml
<cbc:TaxAmount currencyID="EUR">-0.396</cbc:TaxAmount>
<cbc:TaxAmount currencyID="GBP">17.50</cbc:TaxAmount>
<cbc:TaxAmount currencyID="SEK">100</cbc:TaxAmount>
```

#### `cbc:TaxExclusiveAmount`

```xml
<cbc:TaxExclusiveAmount>1436.5</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount>205.00</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount>23.20</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount>49437.50</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
```

**`@currencyID`**

```xml
<cbc:TaxExclusiveAmount currencyID="DKK">49437.50</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount currencyID="EUR">1436.5</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount currencyID="GBP">90.00</cbc:TaxExclusiveAmount>
```

#### `cbc:TaxInclusiveAmount`

```xml
<cbc:TaxInclusiveAmount>1729</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>247.55</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>247187.50</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>29.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>6.00</cbc:TaxInclusiveAmount>
```
_4 more values in examples_

**`@currencyID`**

```xml
<cbc:TaxInclusiveAmount currencyID="DKK">247187.50</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">1.00</cbc:TaxInclusiveAmount>
```

#### `cbc:TaxInclusiveLineExtensionAmount`

```xml
<cbc:TaxInclusiveLineExtensionAmount>20.00</cbc:TaxInclusiveLineExtensionAmount>
<cbc:TaxInclusiveLineExtensionAmount>9.00</cbc:TaxInclusiveLineExtensionAmount>
```

**`@currencyID`**

```xml
<cbc:TaxInclusiveLineExtensionAmount currencyID="EUR">20.00</cbc:TaxInclusiveLineExtensionAmount>
```

#### `cbc:TaxInclusivePriceAmount`

```xml
<cbc:TaxInclusivePriceAmount>15.00</cbc:TaxInclusivePriceAmount>
<cbc:TaxInclusivePriceAmount>20.00</cbc:TaxInclusivePriceAmount>
```

**`@currencyID`**

```xml
<cbc:TaxInclusivePriceAmount currencyID="EUR">15.00</cbc:TaxInclusivePriceAmount>
```

#### `cbc:TaxableAmount`

```xml
<cbc:TaxableAmount>1</cbc:TaxableAmount>
<cbc:TaxableAmount>1.00</cbc:TaxableAmount>
<cbc:TaxableAmount>1460.5</cbc:TaxableAmount>
<cbc:TaxableAmount>202.50</cbc:TaxableAmount>
<cbc:TaxableAmount>23.20</cbc:TaxableAmount>
```
_4 more values in examples_

**`@currencyID`**

```xml
<cbc:TaxableAmount currencyID="EUR">-25</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="GBP">100.00</cbc:TaxableAmount>
```

#### `cbc:TotalBalanceAmount`

```xml
<cbc:TotalBalanceAmount>-107.50</cbc:TotalBalanceAmount>
```

**`@currencyID`**

```xml
<cbc:TotalBalanceAmount currencyID="GBP">-107.50</cbc:TotalBalanceAmount>
```

#### `cbc:TotalCreditAmount`

```xml
<cbc:TotalCreditAmount>0.00</cbc:TotalCreditAmount>
<cbc:TotalCreditAmount>107.50</cbc:TotalCreditAmount>
```

**`@currencyID`**

```xml
<cbc:TotalCreditAmount currencyID="GBP">0.00</cbc:TotalCreditAmount>
```

#### `cbc:TotalDebitAmount`

```xml
<cbc:TotalDebitAmount>0.00</cbc:TotalDebitAmount>
<cbc:TotalDebitAmount>107.50</cbc:TotalDebitAmount>
```

**`@currencyID`**

```xml
<cbc:TotalDebitAmount currencyID="GBP">0.00</cbc:TotalDebitAmount>
```

#### `cbc:TotalInvoiceAmount`

```xml
<cbc:TotalInvoiceAmount>10500.00</cbc:TotalInvoiceAmount>
<cbc:TotalInvoiceAmount>44250.00</cbc:TotalInvoiceAmount>
```

**`@currencyID`**

```xml
<cbc:TotalInvoiceAmount currencyID="DKK">44250.00</cbc:TotalInvoiceAmount>
<cbc:TotalInvoiceAmount currencyID="EUR">10500.00</cbc:TotalInvoiceAmount>
```

#### `cbc:TotalPaymentAmount`

```xml
<cbc:TotalPaymentAmount>107.50</cbc:TotalPaymentAmount>
```

**`@currencyID`**

```xml
<cbc:TotalPaymentAmount currencyID="GBP">107.50</cbc:TotalPaymentAmount>
```

#### `cbc:TotalTaxAmount`

```xml
<cbc:TotalTaxAmount>10</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>17.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>20</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>37625.00</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>437.50</cbc:TotalTaxAmount>
```
_1 more value in examples_

**`@currencyID`**

```xml
<cbc:TotalTaxAmount currencyID="DKK">10937.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="GBP">17.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="SEK">10</cbc:TotalTaxAmount>
```

#### `cbc:ValueAmount`

```xml
<cbc:ValueAmount>1000.00</cbc:ValueAmount>
<cbc:ValueAmount>10500.00</cbc:ValueAmount>
<cbc:ValueAmount>250</cbc:ValueAmount>
```

**`@currencyID`**

```xml
<cbc:ValueAmount currencyID="DKK">10500.00</cbc:ValueAmount>
<cbc:ValueAmount currencyID="USD">1000.00</cbc:ValueAmount>
```

[↑ Back to contents](#contents)

### Binary Object (`udt:BinaryObjectType`)

_1 elements_

#### `cbc:EmbeddedDocumentBinaryObject`

```xml
<cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxN...RU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
```

**`@mimeCode`**

```xml
<cbc:EmbeddedDocumentBinaryObject mimeCode="application/CSTAdata+xml">UjBsR09EbGhjZ0dTQUxN...RU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
<cbc:EmbeddedDocumentBinaryObject mimeCode="application/pdf">UjBsR09EbGhjZ0dTQUxN...RU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
```

[↑ Back to contents](#contents)

### Code (`udt:CodeType`)

_84 elements_

#### `cbc:AccountTypeCode`

```xml
<cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
```

#### `cbc:AccountingCostCode`

```xml
<cbc:AccountingCostCode>Project123</cbc:AccountingCostCode>
<cbc:AccountingCostCode>ProjectID123</cbc:AccountingCostCode>
```

#### `cbc:AddressFormatCode`

```xml
<cbc:AddressFormatCode>Structured</cbc:AddressFormatCode>
<cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
```

**`@listAgencyID`**

```xml
<cbc:AddressFormatCode listAgencyID="320">StructuredDK</cbc:AddressFormatCode>
<cbc:AddressFormatCode listAgencyID="700">Structured</cbc:AddressFormatCode>
```

**`@listID`**

```xml
<cbc:AddressFormatCode listID="CENBII3">Structured</cbc:AddressFormatCode>
<cbc:AddressFormatCode listID="urn:oioubl:codelist:addressformatcode-1.1">StructuredDK</cbc:AddressFormatCode>
```

#### `cbc:AdjustmentReasonCode`

```xml
<cbc:AdjustmentReasonCode>REVISED_PROMOTION</cbc:AdjustmentReasonCode>
```

#### `cbc:AgreementTypeCode`

```xml
<cbc:AgreementTypeCode>Bilateral</cbc:AgreementTypeCode>
<cbc:AgreementTypeCode>Multilateral</cbc:AgreementTypeCode>
```

#### `cbc:AllowanceChargeReasonCode`

```xml
<cbc:AllowanceChargeReasonCode>17</cbc:AllowanceChargeReasonCode>
<cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
```

#### `cbc:AvailabilityStatusCode`

```xml
<cbc:AvailabilityStatusCode>1</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode>2</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode>8</cbc:AvailabilityStatusCode>
```

**`@listAgencyName`**

```xml
<cbc:AvailabilityStatusCode listAgencyName="UN/ECE">1</cbc:AvailabilityStatusCode>
```

**`@listID`**

```xml
<cbc:AvailabilityStatusCode listID="7011">1</cbc:AvailabilityStatusCode>
```

**`@listURI`**

```xml
<cbc:AvailabilityStatusCode listURI="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm">1</cbc:AvailabilityStatusCode>
```

#### `cbc:CapabilityTypeCode`

```xml
<cbc:CapabilityTypeCode>General</cbc:CapabilityTypeCode>
```

#### `cbc:CargoTypeCode`

```xml
<cbc:CargoTypeCode>12</cbc:CargoTypeCode>
<cbc:CargoTypeCode>14</cbc:CargoTypeCode>
```

#### `cbc:CollaborationPriorityCode`

```xml
<cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
```

#### `cbc:CommodityCode`

```xml
<cbc:CommodityCode>19011000</cbc:CommodityCode>
<cbc:CommodityCode>8</cbc:CommodityCode>
<cbc:CommodityCode>84195000</cbc:CommodityCode>
```

#### `cbc:ComparisonDataSourceCode`

```xml
<cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
```

#### `cbc:ConditionCode`

```xml
<cbc:ConditionCode>31</cbc:ConditionCode>
<cbc:ConditionCode>4</cbc:ConditionCode>
```

#### `cbc:CoordinateSystemCode`

```xml
<cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
```

#### `cbc:CountrySubentityCode`

```xml
<cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
<cbc:CountrySubentityCode>RegionA</cbc:CountrySubentityCode>
```

#### `cbc:CurrencyCode`

```xml
<cbc:CurrencyCode>GBP</cbc:CurrencyCode>
```

#### `cbc:CustomsProcedureCode`

```xml
<cbc:CustomsProcedureCode>1011</cbc:CustomsProcedureCode>
```

#### `cbc:CustomsStatusCode`

```xml
<cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
```

#### `cbc:DataSourceCode`

```xml
<cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
```

#### `cbc:DespatchAdviceTypeCode`

```xml
<cbc:DespatchAdviceTypeCode>delivery</cbc:DespatchAdviceTypeCode>
```

#### `cbc:DisplayTacticTypeCode`

```xml
<cbc:DisplayTacticTypeCode>DISPLAY_GENERAL</cbc:DisplayTacticTypeCode>
```

#### `cbc:DocumentCurrencyCode`

```xml
<cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>
<cbc:DocumentCurrencyCode>GBP</cbc:DocumentCurrencyCode>
<cbc:DocumentCurrencyCode>SEK</cbc:DocumentCurrencyCode>
```

**`@listAgencyID`**

```xml
<cbc:DocumentCurrencyCode listAgencyID="6">EUR</cbc:DocumentCurrencyCode>
```

**`@listID`**

```xml
<cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">EUR</cbc:DocumentCurrencyCode>
```

#### `cbc:DocumentStatusCode`

```xml
<cbc:DocumentStatusCode>Confirmed</cbc:DocumentStatusCode>
<cbc:DocumentStatusCode>NoStatus</cbc:DocumentStatusCode>
<cbc:DocumentStatusCode>NotConfirmed</cbc:DocumentStatusCode>
```

#### `cbc:DocumentTypeCode`

```xml
<cbc:DocumentTypeCode>315</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>381</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>704</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>741</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>CONTRACT</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>Certificate of shipment</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>N380</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode>normalizedString</cbc:DocumentTypeCode>
```

**`@listAgencyID`**

```xml
<cbc:DocumentTypeCode listAgencyID="306">SM1</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listAgencyID="6">380</cbc:DocumentTypeCode>
```

**`@listAgencyName`**

```xml
<cbc:DocumentTypeCode listAgencyName="SMDG">SM1</cbc:DocumentTypeCode>
```

**`@listID`**

```xml
<cbc:DocumentTypeCode listID="UN/ECE 1001">380</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listID="UN/ECE 1153">BN</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listID="VGM">SM1</cbc:DocumentTypeCode>
```

#### `cbc:EnvironmentalEmissionTypeCode`

```xml
<cbc:EnvironmentalEmissionTypeCode>CO2</cbc:EnvironmentalEmissionTypeCode>
```

#### `cbc:EvidenceTypeCode`

```xml
<cbc:EvidenceTypeCode>mail</cbc:EvidenceTypeCode>
```

#### `cbc:ExceptionStatusCode`

```xml
<cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
```

#### `cbc:ExportReasonCode`

```xml
<cbc:ExportReasonCode>EXA</cbc:ExportReasonCode>
```

#### `cbc:ExportTypeCode`

```xml
<cbc:ExportTypeCode>20</cbc:ExportTypeCode>
```

#### `cbc:ForecastPurposeCode`

```xml
<cbc:ForecastPurposeCode>ORDER_FORECAST</cbc:ForecastPurposeCode>
<cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
```

#### `cbc:ForecastTypeCode`

```xml
<cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
<cbc:ForecastTypeCode>PROMOTIONAL</cbc:ForecastTypeCode>
<cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
```

#### `cbc:FullnessIndicationCode`

```xml
<cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
<cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
<cbc:FullnessIndicationCode>FTL</cbc:FullnessIndicationCode>
```

**`@listAgencyID`**

```xml
<cbc:FullnessIndicationCode listAgencyID="6">5</cbc:FullnessIndicationCode>
```

**`@listID`**

```xml
<cbc:FullnessIndicationCode listID="UN/ECE 8169">5</cbc:FullnessIndicationCode>
```

#### `cbc:HandlingCode`

```xml
<cbc:HandlingCode>23</cbc:HandlingCode>
```

#### `cbc:IdentificationCode`

```xml
<cbc:IdentificationCode>AT</cbc:IdentificationCode>
<cbc:IdentificationCode>BE</cbc:IdentificationCode>
<cbc:IdentificationCode>CH</cbc:IdentificationCode>
<cbc:IdentificationCode>CN</cbc:IdentificationCode>
<cbc:IdentificationCode>DE</cbc:IdentificationCode>
<cbc:IdentificationCode>DK</cbc:IdentificationCode>
<cbc:IdentificationCode>FI</cbc:IdentificationCode>
<cbc:IdentificationCode>GB</cbc:IdentificationCode>
<cbc:IdentificationCode>IT</cbc:IdentificationCode>
<cbc:IdentificationCode>MA</cbc:IdentificationCode>
<cbc:IdentificationCode>MX</cbc:IdentificationCode>
<cbc:IdentificationCode>NO</cbc:IdentificationCode>
<cbc:IdentificationCode>PA</cbc:IdentificationCode>
<cbc:IdentificationCode>RU</cbc:IdentificationCode>
<cbc:IdentificationCode>SE</cbc:IdentificationCode>
<cbc:IdentificationCode>TH</cbc:IdentificationCode>
<cbc:IdentificationCode>US</cbc:IdentificationCode>
```

**`@listAgencyID`**

```xml
<cbc:IdentificationCode listAgencyID="6">BE</cbc:IdentificationCode>
```

**`@listID`**

```xml
<cbc:IdentificationCode listID="ISO3166-1">BE</cbc:IdentificationCode>
```

#### `cbc:IndustryClassificationCode`

```xml
<cbc:IndustryClassificationCode>CA</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode>Dairy</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode>Public Rail Authorities</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode>SPC</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode>TR</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode>WPA</cbc:IndustryClassificationCode>
```

**`@listAgencyID`**

```xml
<cbc:IndustryClassificationCode listAgencyID="6">CA</cbc:IndustryClassificationCode>
```

**`@listID`**

```xml
<cbc:IndustryClassificationCode listID="UN/ECE 3035">CA</cbc:IndustryClassificationCode>
```

#### `cbc:InvoiceTypeCode`

```xml
<cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
<cbc:InvoiceTypeCode>SalesInvoice</cbc:InvoiceTypeCode>
```

**`@listAgencyID`**

```xml
<cbc:InvoiceTypeCode listAgencyID="6">380</cbc:InvoiceTypeCode>
```

**`@listID`**

```xml
<cbc:InvoiceTypeCode listID="UN/ECE 1001 Subset">380</cbc:InvoiceTypeCode>
```

#### `cbc:ItemClassificationCode`

```xml
<cbc:ItemClassificationCode>12344321</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>12344322</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>65434564</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>65434565</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>65434566</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>65434567</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>65434568</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode>8518309590</cbc:ItemClassificationCode>
```

**`@listAgencyID`**

```xml
<cbc:ItemClassificationCode listAgencyID="113">12344321</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="2">65434564</cbc:ItemClassificationCode>
```

**`@listID`**

```xml
<cbc:ItemClassificationCode listID="CPV">65434564</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="UNSPSC">12344321</cbc:ItemClassificationCode>
```

#### `cbc:LatitudeDirectionCode`

```xml
<cbc:LatitudeDirectionCode>North</cbc:LatitudeDirectionCode>
```

#### `cbc:LineStatusCode`

```xml
<cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
<cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
<cbc:LineStatusCode>Revised</cbc:LineStatusCode>
```

**`@listAgencyID`**

```xml
<cbc:LineStatusCode listAgencyID="UBL">Disputed</cbc:LineStatusCode>
```

**`@listName`**

```xml
<cbc:LineStatusCode listName="Line Status">Disputed</cbc:LineStatusCode>
```

#### `cbc:LocationTypeCode`

```xml
<cbc:LocationTypeCode>13</cbc:LocationTypeCode>
<cbc:LocationTypeCode>24</cbc:LocationTypeCode>
<cbc:LocationTypeCode>34</cbc:LocationTypeCode>
<cbc:LocationTypeCode>41</cbc:LocationTypeCode>
<cbc:LocationTypeCode>7</cbc:LocationTypeCode>
<cbc:LocationTypeCode>Baseport of discharge</cbc:LocationTypeCode>
<cbc:LocationTypeCode>Baseport of loading</cbc:LocationTypeCode>
<cbc:LocationTypeCode>CUSTOMS OFFICE</cbc:LocationTypeCode>
<cbc:LocationTypeCode>L</cbc:LocationTypeCode>
<cbc:LocationTypeCode>P</cbc:LocationTypeCode>
<cbc:LocationTypeCode>Place of delivery</cbc:LocationTypeCode>
<cbc:LocationTypeCode>Place of despatch</cbc:LocationTypeCode>
<cbc:LocationTypeCode>Place of transhipment</cbc:LocationTypeCode>
<cbc:LocationTypeCode>RAILWAY STATION</cbc:LocationTypeCode>
```

**`@listAgencyName`**

```xml
<cbc:LocationTypeCode listAgencyName="UN">34</cbc:LocationTypeCode>
```

**`@listName`**

```xml
<cbc:LocationTypeCode listName="UN/EDIFACT 3227">34</cbc:LocationTypeCode>
```

#### `cbc:LongitudeDirectionCode`

```xml
<cbc:LongitudeDirectionCode>East</cbc:LongitudeDirectionCode>
```

#### `cbc:MathematicOperatorCode`

```xml
<cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
```

#### `cbc:NatureCode`

```xml
<cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
```

#### `cbc:NatureOfTransactionCode`

```xml
<cbc:NatureOfTransactionCode>11</cbc:NatureOfTransactionCode>
<cbc:NatureOfTransactionCode>T1</cbc:NatureOfTransactionCode>
```

#### `cbc:NotificationTypeCode`

```xml
<cbc:NotificationTypeCode>ITEM_CONDITION_DEVIATIONS</cbc:NotificationTypeCode>
<cbc:NotificationTypeCode>Status Notifications, schedule deviations</cbc:NotificationTypeCode>
<cbc:NotificationTypeCode>TIME_SCHEDULE_DEVIATIONS</cbc:NotificationTypeCode>
```

#### `cbc:PackageLevelCode`

```xml
<cbc:PackageLevelCode>NoStacking</cbc:PackageLevelCode>
```

#### `cbc:PackagingTypeCode`

```xml
<cbc:PackagingTypeCode>CS</cbc:PackagingTypeCode>
<cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
<cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
<cbc:PackagingTypeCode>PX</cbc:PackagingTypeCode>
<cbc:PackagingTypeCode>TB</cbc:PackagingTypeCode>
```

**`@listAgencyID`**

```xml
<cbc:PackagingTypeCode listAgencyID="6">TB</cbc:PackagingTypeCode>
```

**`@listID`**

```xml
<cbc:PackagingTypeCode listID="UN/ECE rec 21">TB</cbc:PackagingTypeCode>
```

#### `cbc:PaymentChannelCode`

```xml
<cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
```

#### `cbc:PaymentMeansCode`

```xml
<cbc:PaymentMeansCode>10</cbc:PaymentMeansCode>
<cbc:PaymentMeansCode>20</cbc:PaymentMeansCode>
<cbc:PaymentMeansCode>31</cbc:PaymentMeansCode>
```

**`@listID`**

```xml
<cbc:PaymentMeansCode listID="UN/ECE 4461">10</cbc:PaymentMeansCode>
```

#### `cbc:PerformanceMetricTypeCode`

```xml
<cbc:PerformanceMetricTypeCode>GROSS_MARGIN</cbc:PerformanceMetricTypeCode>
<cbc:PerformanceMetricTypeCode>SUPPLY</cbc:PerformanceMetricTypeCode>
```

#### `cbc:PreferenceCriterionCode`

```xml
<cbc:PreferenceCriterionCode>100</cbc:PreferenceCriterionCode>
```

#### `cbc:PricingCurrencyCode`

```xml
<cbc:PricingCurrencyCode>DKK</cbc:PricingCurrencyCode>
```

#### `cbc:ProcedureCode`

```xml
<cbc:ProcedureCode>A-letter</cbc:ProcedureCode>
```

#### `cbc:ProfileStatusCode`

```xml
<cbc:ProfileStatusCode>NEW</cbc:ProfileStatusCode>
```

#### `cbc:PromotionalEventTypeCode`

```xml
<cbc:PromotionalEventTypeCode>STORE_OPENING</cbc:PromotionalEventTypeCode>
```

#### `cbc:PurposeCode`

```xml
<cbc:PurposeCode>ORDER_FORECAST</cbc:PurposeCode>
```

#### `cbc:ResolutionCode`

```xml
<cbc:ResolutionCode>LOCAL_INTERPOLATED_VALUE</cbc:ResolutionCode>
```

#### `cbc:RetailEventStatusCode`

```xml
<cbc:RetailEventStatusCode>PLANNED</cbc:RetailEventStatusCode>
```

#### `cbc:RevisionStatusCode`

```xml
<cbc:RevisionStatusCode>NEW</cbc:RevisionStatusCode>
```

#### `cbc:RoleCode`

```xml
<cbc:RoleCode>BN</cbc:RoleCode>
<cbc:RoleCode>Champer</cbc:RoleCode>
<cbc:RoleCode>RP</cbc:RoleCode>
```

**`@listAgencyID`**

```xml
<cbc:RoleCode listAgencyID="6">BN</cbc:RoleCode>
```

**`@listID`**

```xml
<cbc:RoleCode listID="UN/ECE 3139">BN</cbc:RoleCode>
```

#### `cbc:ServiceTypeCode`

```xml
<cbc:ServiceTypeCode>AP</cbc:ServiceTypeCode>
```

#### `cbc:ShipmentStageTypeCode`

```xml
<cbc:ShipmentStageTypeCode>1</cbc:ShipmentStageTypeCode>
```

#### `cbc:SizeTypeCode`

```xml
<cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
```

**`@listAgencyID`**

```xml
<cbc:SizeTypeCode listAgencyID="5">22G1</cbc:SizeTypeCode>
```

**`@listID`**

```xml
<cbc:SizeTypeCode listID="ISO 6346">22G1</cbc:SizeTypeCode>
```

#### `cbc:SocialMediaTypeCode`

```xml
<cbc:SocialMediaTypeCode>Business</cbc:SocialMediaTypeCode>
```

#### `cbc:SourceCurrencyCode`

```xml
<cbc:SourceCurrencyCode>USD</cbc:SourceCurrencyCode>
```

#### `cbc:StatusCode`

```xml
<cbc:StatusCode>ISSUED</cbc:StatusCode>
```

#### `cbc:StatusReasonCode`

```xml
<cbc:StatusReasonCode>23</cbc:StatusReasonCode>
```

#### `cbc:SubTypeCode`

```xml
<cbc:SubTypeCode>IM</cbc:SubTypeCode>
```

#### `cbc:SupplyChainActivityTypeCode`

```xml
<cbc:SupplyChainActivityTypeCode>SALES</cbc:SupplyChainActivityTypeCode>
<cbc:SupplyChainActivityTypeCode>SHIPMENTS</cbc:SupplyChainActivityTypeCode>
```

#### `cbc:TargetCurrencyCode`

```xml
<cbc:TargetCurrencyCode>GBP</cbc:TargetCurrencyCode>
```

#### `cbc:TariffCode`

```xml
<cbc:TariffCode>15219000</cbc:TariffCode>
```

#### `cbc:TaxExemptionReasonCode`

```xml
<cbc:TaxExemptionReasonCode>AAM</cbc:TaxExemptionReasonCode>
```

**`@listAgencyID`**

```xml
<cbc:TaxExemptionReasonCode listAgencyID="ZZZ">AAM</cbc:TaxExemptionReasonCode>
```

**`@listID`**

```xml
<cbc:TaxExemptionReasonCode listID="CWA 15577">AAM</cbc:TaxExemptionReasonCode>
```

#### `cbc:TaxTypeCode`

```xml
<cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
```

#### `cbc:ThresholdValueComparisonCode`

```xml
<cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
```

#### `cbc:TransportEquipmentTypeCode`

```xml
<cbc:TransportEquipmentTypeCode>AD</cbc:TransportEquipmentTypeCode>
<cbc:TransportEquipmentTypeCode>AE</cbc:TransportEquipmentTypeCode>
<cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
<cbc:TransportEquipmentTypeCode>EFP</cbc:TransportEquipmentTypeCode>
<cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
<cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
```

**`@listAgencyID`**

```xml
<cbc:TransportEquipmentTypeCode listAgencyID="6">CN</cbc:TransportEquipmentTypeCode>
```

**`@listID`**

```xml
<cbc:TransportEquipmentTypeCode listID="UN/ECE 8053">CN</cbc:TransportEquipmentTypeCode>
```

#### `cbc:TransportExecutionStatusCode`

```xml
<cbc:TransportExecutionStatusCode>35</cbc:TransportExecutionStatusCode>
```

#### `cbc:TransportHandlingUnitTypeCode`

```xml
<cbc:TransportHandlingUnitTypeCode>122</cbc:TransportHandlingUnitTypeCode>
<cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
<cbc:TransportHandlingUnitTypeCode>PA</cbc:TransportHandlingUnitTypeCode>
<cbc:TransportHandlingUnitTypeCode>Palletized cargo</cbc:TransportHandlingUnitTypeCode>
```

**`@listAgencyName`**

```xml
<cbc:TransportHandlingUnitTypeCode listAgencyName="United Nations Economic Commission for Europe">PA</cbc:TransportHandlingUnitTypeCode>
```

**`@listID`**

```xml
<cbc:TransportHandlingUnitTypeCode listID="TRED 8053">PA</cbc:TransportHandlingUnitTypeCode>
```

#### `cbc:TransportMeansTypeCode`

```xml
<cbc:TransportMeansTypeCode>230</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>2305</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>31</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>Container vessel</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>Plane</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>Train, with more than 20 wagons</cbc:TransportMeansTypeCode>
<cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
```

#### `cbc:TransportModeCode`

```xml
<cbc:TransportModeCode>1</cbc:TransportModeCode>
<cbc:TransportModeCode>2</cbc:TransportModeCode>
<cbc:TransportModeCode>3</cbc:TransportModeCode>
<cbc:TransportModeCode>4</cbc:TransportModeCode>
```

**`@listAgencyID`**

```xml
<cbc:TransportModeCode listAgencyID="6">3</cbc:TransportModeCode>
```

**`@listID`**

```xml
<cbc:TransportModeCode listID="UN/ECE rec 16">3</cbc:TransportModeCode>
```

**`@name`**

```xml
<cbc:TransportModeCode name="Sea">1</cbc:TransportModeCode>
```

#### `cbc:TransportServiceCode`

```xml
<cbc:TransportServiceCode>12</cbc:TransportServiceCode>
<cbc:TransportServiceCode>3</cbc:TransportServiceCode>
<cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
<cbc:TransportServiceCode>Insurance</cbc:TransportServiceCode>
<cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
<cbc:TransportServiceCode>Status notification</cbc:TransportServiceCode>
<cbc:TransportServiceCode>Transport</cbc:TransportServiceCode>
```

#### `cbc:TransportationStatusTypeCode`

```xml
<cbc:TransportationStatusTypeCode>All deviations</cbc:TransportationStatusTypeCode>
```

#### `cbc:TypeCode`

```xml
<cbc:TypeCode>ChinaFish</cbc:TypeCode>
<cbc:TypeCode>X</cbc:TypeCode>
```

#### `cbc:WeighingMethodCode`

```xml
<cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
```

**`@listAgencyID`**

```xml
<cbc:WeighingMethodCode listAgencyID="54">SM1</cbc:WeighingMethodCode>
```

**`@listID`**

```xml
<cbc:WeighingMethodCode listID="IMO SOLAS">SM1</cbc:WeighingMethodCode>
```

#### `cbc:WeightStatementTypeCode`

```xml
<cbc:WeightStatementTypeCode>749</cbc:WeightStatementTypeCode>
```

**`@listAgencyID`**

```xml
<cbc:WeightStatementTypeCode listAgencyID="6">749</cbc:WeightStatementTypeCode>
```

**`@listID`**

```xml
<cbc:WeightStatementTypeCode listID="UN/ECE 1001">749</cbc:WeightStatementTypeCode>
```

**`@listVersionID`**

```xml
<cbc:WeightStatementTypeCode listVersionID="d16a">749</cbc:WeightStatementTypeCode>
```

[↑ Back to contents](#contents)

### Date (`udt:DateType`)

_25 elements_

#### `cbc:ActualDeliveryDate`

```xml
<cbc:ActualDeliveryDate>2005-06-20</cbc:ActualDeliveryDate>
<cbc:ActualDeliveryDate>2009-12-15</cbc:ActualDeliveryDate>
```

#### `cbc:ActualDespatchDate`

```xml
<cbc:ActualDespatchDate>2005-06-25</cbc:ActualDespatchDate>
<cbc:ActualDespatchDate>2013-09-15</cbc:ActualDespatchDate>
```

#### `cbc:AvailabilityDate`

```xml
<cbc:AvailabilityDate>2010-04-11</cbc:AvailabilityDate>
<cbc:AvailabilityDate>2010-04-20</cbc:AvailabilityDate>
```

#### `cbc:BestBeforeDate`

```xml
<cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
```

#### `cbc:Date`

```xml
<cbc:Date>1967-08-13</cbc:Date>
```

#### `cbc:EndDate`

```xml
<cbc:EndDate>2005-07-20</cbc:EndDate>
<cbc:EndDate>2010-01-31</cbc:EndDate>
<cbc:EndDate>2010-06-12</cbc:EndDate>
<cbc:EndDate>2012-01-01</cbc:EndDate>
<cbc:EndDate>2020-02-20</cbc:EndDate>
```
_41 more values in examples_

#### `cbc:ExpiryDate`

```xml
<cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
<cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
```

#### `cbc:IssueDate`

```xml
<cbc:IssueDate>2008-05-01</cbc:IssueDate>
<cbc:IssueDate>2010-01-10</cbc:IssueDate>
<cbc:IssueDate>2011-03-13</cbc:IssueDate>
<cbc:IssueDate>2011-10-03</cbc:IssueDate>
<cbc:IssueDate>2025-07-01</cbc:IssueDate>
```
_53 more values in examples_

#### `cbc:LatestDeliveryDate`

```xml
<cbc:LatestDeliveryDate>2005-06-30</cbc:LatestDeliveryDate>
```

#### `cbc:LatestPickupDate`

```xml
<cbc:LatestPickupDate>2016-08-02</cbc:LatestPickupDate>
```

#### `cbc:LatestProposalAcceptanceDate`

```xml
<cbc:LatestProposalAcceptanceDate>2010-01-06</cbc:LatestProposalAcceptanceDate>
```

#### `cbc:ManufactureDate`

```xml
<cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
```

#### `cbc:NominationDate`

```xml
<cbc:NominationDate>2011-03-13</cbc:NominationDate>
```

#### `cbc:OccurrenceDate`

```xml
<cbc:OccurrenceDate>2013-05-25</cbc:OccurrenceDate>
```

#### `cbc:PaymentDueDate`

```xml
<cbc:PaymentDueDate>2005-07-21</cbc:PaymentDueDate>
<cbc:PaymentDueDate>2009-12-31</cbc:PaymentDueDate>
<cbc:PaymentDueDate>2011-11-06</cbc:PaymentDueDate>
```

#### `cbc:PurchaseDate`

```xml
<cbc:PurchaseDate>2023-01-27</cbc:PurchaseDate>
```

#### `cbc:ReferenceDate`

```xml
<cbc:ReferenceDate>2010-04-30</cbc:ReferenceDate>
<cbc:ReferenceDate>2011-03-13</cbc:ReferenceDate>
```

#### `cbc:RegistrationDate`

```xml
<cbc:RegistrationDate>1957-08-13</cbc:RegistrationDate>
```

#### `cbc:SourceForecastIssueDate`

```xml
<cbc:SourceForecastIssueDate>2005-02-17</cbc:SourceForecastIssueDate>
```

#### `cbc:StartDate`

```xml
<cbc:StartDate>2010-05-01</cbc:StartDate>
<cbc:StartDate>2010-05-12</cbc:StartDate>
<cbc:StartDate>2011-03-14</cbc:StartDate>
<cbc:StartDate>2011-09-12</cbc:StartDate>
<cbc:StartDate>2011-10-06</cbc:StartDate>
```
_36 more values in examples_

#### `cbc:SubmissionDate`

```xml
<cbc:SubmissionDate>2009-12-01</cbc:SubmissionDate>
```

#### `cbc:SubmissionDueDate`

```xml
<cbc:SubmissionDueDate>2008-04-24</cbc:SubmissionDueDate>
```

#### `cbc:TaxPointDate`

```xml
<cbc:TaxPointDate>2005-06-21</cbc:TaxPointDate>
<cbc:TaxPointDate>2009-11-30</cbc:TaxPointDate>
```

#### `cbc:TransactionDate`

```xml
<cbc:TransactionDate>2023-01-27</cbc:TransactionDate>
```

#### `cbc:WeighingDate`

```xml
<cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
```

[↑ Back to contents](#contents)

### Identifier (`udt:IdentifierType`)

_54 elements_

#### `cbc:AircraftID`

```xml
<cbc:AircraftID>A-127763-747</cbc:AircraftID>
<cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
```

#### `cbc:AttributeID`

```xml
<cbc:AttributeID>Length</cbc:AttributeID>
<cbc:AttributeID>LineNetWeight</cbc:AttributeID>
<cbc:AttributeID>OuterDepth</cbc:AttributeID>
<cbc:AttributeID>TC</cbc:AttributeID>
<cbc:AttributeID>Width</cbc:AttributeID>
```
_7 more values in examples_

#### `cbc:CarrierAssignedID`

```xml
<cbc:CarrierAssignedID>123456789987654321</cbc:CarrierAssignedID>
```

#### `cbc:CompanyID`

```xml
<cbc:CompanyID>1323421212</cbc:CompanyID>
<cbc:CompanyID>6411982340</cbc:CompanyID>
<cbc:CompanyID>DK12345</cbc:CompanyID>
<cbc:CompanyID>DK18296799</cbc:CompanyID>
<cbc:CompanyID>DK43232010</cbc:CompanyID>
```
_20 more values in examples_

**`@schemeAgencyID`**

```xml
<cbc:CompanyID schemeAgencyID="ZZZ">5402697509</cbc:CompanyID>
```

**`@schemeID`**

```xml
<cbc:CompanyID schemeID="BEVAT">BE54321</cbc:CompanyID>
<cbc:CompanyID schemeID="CVR">5402697509</cbc:CompanyID>
<cbc:CompanyID schemeID="DKVAT">DK12345</cbc:CompanyID>
```

#### `cbc:ContractFolderID`

```xml
<cbc:ContractFolderID>2017/S 214-3792289</cbc:ContractFolderID>
```

#### `cbc:CustomerAssignedAccountID`

```xml
<cbc:CustomerAssignedAccountID>CO001</cbc:CustomerAssignedAccountID>
<cbc:CustomerAssignedAccountID>LEV00123</cbc:CustomerAssignedAccountID>
<cbc:CustomerAssignedAccountID>XFB01</cbc:CustomerAssignedAccountID>
```

#### `cbc:CustomizationID`

```xml
<cbc:CustomizationID>Common Framework</cbc:CustomizationID>
<cbc:CustomizationID>UBL-2.3</cbc:CustomizationID>
<cbc:CustomizationID>urn:oasis:names:specification:ubl:default</cbc:CustomizationID>
<cbc:CustomizationID>urn:oasis:names:specification:ubl:xpath:DespatchAdvice-2.0:sbs-1.0-draft</cbc:CustomizationID>
<cbc:CustomizationID>urn:www.cenbii.eu:transaction:biitrns010:ver2.0:extended:urn:www.peppol.eu:bis:peppol5a:ver2.0</cbc:CustomizationID>
```
_22 more values in examples_

#### `cbc:DocumentID`

```xml
<cbc:DocumentID>33006</cbc:DocumentID>
```

#### `cbc:EndpointID`

```xml
<cbc:EndpointID>01842222222222</cbc:EndpointID>
<cbc:EndpointID>1234567987654</cbc:EndpointID>
<cbc:EndpointID>DK18296799</cbc:EndpointID>
<cbc:EndpointID>www.consignee.com/statusnotifications/</cbc:EndpointID>
<cbc:EndpointID>www.consignee.de/statusnotifications/</cbc:EndpointID>
```
_7 more values in examples_

**`@schemeAgencyID`**

```xml
<cbc:EndpointID schemeAgencyID="9">01842222222222</cbc:EndpointID>
```

**`@schemeID`**

```xml
<cbc:EndpointID schemeID="DK:CVR">DK18296799</cbc:EndpointID>
<cbc:EndpointID schemeID="FI:OVT">01841111111111</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">1234567890123</cbc:EndpointID>
```

#### `cbc:EndpointURI`

```xml
<cbc:EndpointURI>http://as2.buyer.biz</cbc:EndpointURI>
<cbc:EndpointURI>http://as2.buyer.de</cbc:EndpointURI>
<cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
<cbc:EndpointURI>http://as2.vendor.biz</cbc:EndpointURI>
```

#### `cbc:FormatID`

```xml
<cbc:FormatID>UBL</cbc:FormatID>
```

#### `cbc:GoodsItemPassportID`

```xml
<cbc:GoodsItemPassportID>234222</cbc:GoodsItemPassportID>
<cbc:GoodsItemPassportID>ata01661</cbc:GoodsItemPassportID>
```

#### `cbc:ID`

```xml
<cbc:ID>00123450000583</cbc:ID>
<cbc:ID>6903148000007</cbc:ID>
<cbc:ID>CON_2</cbc:ID>
<cbc:ID>DH019</cbc:ID>
<cbc:ID>TEP_1</cbc:ID>
```
_345 more values in examples_

**`@schemeAgencyID`**

```xml
<cbc:ID schemeAgencyID="306">XXX</cbc:ID>
<cbc:ID schemeAgencyID="320">63</cbc:ID>
<cbc:ID schemeAgencyID="5">TRHU1652173</cbc:ID>
```

**`@schemeAgencyName`**

```xml
<cbc:ID schemeAgencyName="GS1">12345698</cbc:ID>
<cbc:ID schemeAgencyName="INCOTERMS">EXW</cbc:ID>
<cbc:ID schemeAgencyName="SMDG">XXX</cbc:ID>
```

**`@schemeID`**

```xml
<cbc:ID schemeID="GLN">098740918237</cbc:ID>
<cbc:ID schemeID="UN/ECE 5153">VAT</cbc:ID>
<cbc:ID schemeID="UN/LOCODE">GBBRS</cbc:ID>
```

**`@schemeName`**

```xml
<cbc:ID schemeName="GLN">123465</cbc:ID>
<cbc:ID schemeName="UN/LOCODE">CNSHA</cbc:ID>
<cbc:ID schemeName="Unique Consignment Reference">2005US12345678998765432112345678</cbc:ID>
```

#### `cbc:InformationURI`

```xml
<cbc:InformationURI>https://goo.gl/maps/2k242</cbc:InformationURI>
```

#### `cbc:JourneyID`

```xml
<cbc:JourneyID>00344</cbc:JourneyID>
<cbc:JourneyID>M22</cbc:JourneyID>
<cbc:JourneyID>RHamBrem</cbc:JourneyID>
<cbc:JourneyID>TM1</cbc:JourneyID>
<cbc:JourneyID>UA 1234</cbc:JourneyID>
```

#### `cbc:LicensePlateID`

```xml
<cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
<cbc:LicensePlateID>KA04401</cbc:LicensePlateID>
<cbc:LicensePlateID>PBB-123</cbc:LicensePlateID>
<cbc:LicensePlateID>VE80044</cbc:LicensePlateID>
<cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
```

#### `cbc:LineID`

```xml
<cbc:LineID>1</cbc:LineID>
<cbc:LineID>2</cbc:LineID>
<cbc:LineID>3</cbc:LineID>
<cbc:LineID>4</cbc:LineID>
<cbc:LineID>5</cbc:LineID>
```

#### `cbc:LogoReferenceID`

```xml
<cbc:LogoReferenceID>https://www.oasis-open.org/sites/www.oasis-open.org/files/logo.png</cbc:LogoReferenceID>
```

#### `cbc:LotNumberID`

```xml
<cbc:LotNumberID>546378239</cbc:LotNumberID>
<cbc:LotNumberID>9390000757</cbc:LotNumberID>
```

#### `cbc:NetworkID`

```xml
<cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
```

#### `cbc:OID`

```xml
<cbc:OID>2.16.840.1.101.3.4.1.2</cbc:OID>
<cbc:OID>2.16.840.1.101.3.4.1.42</cbc:OID>
```

#### `cbc:ParticipantID`

```xml
<cbc:ParticipantID>1234567987654</cbc:ParticipantID>
```

**`@schemeAgencyID`**

```xml
<cbc:ParticipantID schemeAgencyID="9">1234567987654</cbc:ParticipantID>
```

**`@schemeID`**

```xml
<cbc:ParticipantID schemeID="GLN">1234567987654</cbc:ParticipantID>
```

#### `cbc:PaymentID`

```xml
<cbc:PaymentID>1</cbc:PaymentID>
<cbc:PaymentID>Payref1</cbc:PaymentID>
```

#### `cbc:PaymentMeansID`

```xml
<cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
```

#### `cbc:PaymentTermsDetailsURI`

```xml
<cbc:PaymentTermsDetailsURI>www.ROADCARRIER.de/prices.html</cbc:PaymentTermsDetailsURI>
```

#### `cbc:PreviousVersionID`

```xml
<cbc:PreviousVersionID>1.0</cbc:PreviousVersionID>
```

#### `cbc:ProfileID`

```xml
<cbc:ProfileID>FWF</cbc:ProfileID>
<cbc:ProfileID>bpid:urn:oasis:names:draft:bpss:ubl-2-cpfr-exception-criteria-draft</cbc:ProfileID>
<cbc:ProfileID>bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-despatch-advice-notification-draft</cbc:ProfileID>
<cbc:ProfileID>bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-receipt-advice-notification-draft</cbc:ProfileID>
<cbc:ProfileID>urn:X-demo:CoreElement</cbc:ProfileID>
```
_25 more values in examples_

**`@schemeAgencyID`**

```xml
<cbc:ProfileID schemeAgencyID="320">Procurement-QuoSim-1.0</cbc:ProfileID>
<cbc:ProfileID schemeAgencyID="BII">urn:www.cenbii.eu:profile:BII01:ver1.0</cbc:ProfileID>
```

**`@schemeID`**

```xml
<cbc:ProfileID schemeID="Profile">urn:www.cenbii.eu:profile:BII01:ver1.0</cbc:ProfileID>
<cbc:ProfileID schemeID="urn:oioubl:id:profileid-1.2">Procurement-QuoSim-1.0</cbc:ProfileID>
```

#### `cbc:ProtocolID`

```xml
<cbc:ProtocolID>AS2</cbc:ProtocolID>
```

#### `cbc:RailCarID`

```xml
<cbc:RailCarID>101-21</cbc:RailCarID>
```

#### `cbc:ReferenceID`

```xml
<cbc:ReferenceID>A00095678</cbc:ReferenceID>
```

#### `cbc:RegistrationNationalityID`

```xml
<cbc:RegistrationNationalityID>DE</cbc:RegistrationNationalityID>
<cbc:RegistrationNationalityID>DK</cbc:RegistrationNationalityID>
<cbc:RegistrationNationalityID>EE</cbc:RegistrationNationalityID>
<cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
<cbc:RegistrationNationalityID>IT</cbc:RegistrationNationalityID>
```

#### `cbc:RequiredCustomsID`

```xml
<cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
```

#### `cbc:RevisedForecastLineID`

```xml
<cbc:RevisedForecastLineID>RFL1</cbc:RevisedForecastLineID>
```

#### `cbc:SalesOrderID`

```xml
<cbc:SalesOrderID>A</cbc:SalesOrderID>
<cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
```

#### `cbc:SalesOrderLineID`

```xml
<cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
```

#### `cbc:SchemaURI`

```xml
<cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2</cbc:SchemaURI>
<cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:Invoice-2</cbc:SchemaURI>
```

#### `cbc:SequenceID`

```xml
<cbc:SequenceID>203</cbc:SequenceID>
<cbc:SequenceID>204</cbc:SequenceID>
```

#### `cbc:SequenceNumberID`

```xml
<cbc:SequenceNumberID>1</cbc:SequenceNumberID>
<cbc:SequenceNumberID>2</cbc:SequenceNumberID>
<cbc:SequenceNumberID>3</cbc:SequenceNumberID>
<cbc:SequenceNumberID>4</cbc:SequenceNumberID>
```

#### `cbc:SerialNumberID`

```xml
<cbc:SerialNumberID>7f49b2b8-9e75-11ed-a8fc-0242ac120002</cbc:SerialNumberID>
```

#### `cbc:ShippingOrderID`

```xml
<cbc:ShippingOrderID>KHN23-44044</cbc:ShippingOrderID>
```

#### `cbc:SpecificationID`

```xml
<cbc:SpecificationID>ACME_STROP_0023823</cbc:SpecificationID>
```

#### `cbc:SupplierAssignedAccountID`

```xml
<cbc:SupplierAssignedAccountID>GT00978567</cbc:SupplierAssignedAccountID>
```

#### `cbc:TenderEnvelopeID`

```xml
<cbc:TenderEnvelopeID>abc</cbc:TenderEnvelopeID>
```

#### `cbc:TraceID`

```xml
<cbc:TraceID>12345678914111</cbc:TraceID>
<cbc:TraceID>12345678914112</cbc:TraceID>
<cbc:TraceID>12345678914542</cbc:TraceID>
<cbc:TraceID>12345678914543</cbc:TraceID>
<cbc:TraceID>12345678914565</cbc:TraceID>
```
_2 more values in examples_

#### `cbc:TrackingID`

```xml
<cbc:TrackingID>NKH7712289-03339-000128</cbc:TrackingID>
```

#### `cbc:TrainID`

```xml
<cbc:TrainID>101</cbc:TrainID>
<cbc:TrainID>RID01235</cbc:TrainID>
<cbc:TrainID>VF80145</cbc:TrainID>
```

#### `cbc:TransportExecutionPlanReferenceID`

```xml
<cbc:TransportExecutionPlanReferenceID>TEPID_1</cbc:TransportExecutionPlanReferenceID>
<cbc:TransportExecutionPlanReferenceID>TEPID_1_1</cbc:TransportExecutionPlanReferenceID>
<cbc:TransportExecutionPlanReferenceID>TEPID_1_2</cbc:TransportExecutionPlanReferenceID>
<cbc:TransportExecutionPlanReferenceID>TEPID_1_3</cbc:TransportExecutionPlanReferenceID>
<cbc:TransportExecutionPlanReferenceID>TEP_1</cbc:TransportExecutionPlanReferenceID>
```
_3 more values in examples_

#### `cbc:UBLVersionID`

```xml
<cbc:UBLVersionID>2.0</cbc:UBLVersionID>
<cbc:UBLVersionID>2.0-prd3</cbc:UBLVersionID>
<cbc:UBLVersionID>2.1</cbc:UBLVersionID>
<cbc:UBLVersionID>2.3</cbc:UBLVersionID>
<cbc:UBLVersionID>2.5</cbc:UBLVersionID>
```
_2 more values in examples_

#### `cbc:URI`

```xml
<cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
<cbc:URI>http://www.suppliersite.eu/sheet001.html</cbc:URI>
<cbc:URI>http://www.youtube.com/oasisopen</cbc:URI>
<cbc:URI>https://www.linkedin.com/company/oasis</cbc:URI>
<cbc:URI>normalizedString</cbc:URI>
```
_6 more values in examples_

#### `cbc:UUID`

```xml
<cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
<cbc:UUID>569ED478-0EBE-4817-A234-DFB9ACA81218</cbc:UUID>
<cbc:UUID>6E09886B-DC6E-439F-82D1-7C83746352B1</cbc:UUID>
<cbc:UUID>84E081CE-F9D1-94C5-40F9-94C5FF9D1AC3</cbc:UUID>
<cbc:UUID>8D076867-AE6D-439F-8281-5AAFC7F4E3B1</cbc:UUID>
```
_11 more values in examples_

#### `cbc:VersionID`

```xml
<cbc:VersionID>1</cbc:VersionID>
<cbc:VersionID>1.1</cbc:VersionID>
<cbc:VersionID>2.2</cbc:VersionID>
```

#### `cbc:VesselID`

```xml
<cbc:VesselID>3852664</cbc:VesselID>
<cbc:VesselID>Eestiship</cbc:VesselID>
<cbc:VesselID>IMO1234567</cbc:VesselID>
<cbc:VesselID>SomeIMONr</cbc:VesselID>
```

#### `cbc:WebsiteURI`

```xml
<cbc:WebsiteURI>http://super.company.dk</cbc:WebsiteURI>
<cbc:WebsiteURI>http://www.CONSIGNEE.no/statusreceptioninterface#2</cbc:WebsiteURI>
<cbc:WebsiteURI>https://www.oasis-open.org</cbc:WebsiteURI>
<cbc:WebsiteURI>www.ROADCARRIER.de</cbc:WebsiteURI>
```

#### `cbc:WeighingDeviceID`

```xml
<cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
```

[↑ Back to contents](#contents)

### Indicator (`udt:IndicatorType`)

_27 elements_

#### `cbc:AcceptanceIndicator`

```xml
<cbc:AcceptanceIndicator>false</cbc:AcceptanceIndicator>
<cbc:AcceptanceIndicator>true</cbc:AcceptanceIndicator>
```

#### `cbc:AcceptedIndicator`

```xml
<cbc:AcceptedIndicator>true</cbc:AcceptedIndicator>
```

#### `cbc:AdValoremIndicator`

```xml
<cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
```

#### `cbc:BalanceBroughtForwardIndicator`

```xml
<cbc:BalanceBroughtForwardIndicator>false</cbc:BalanceBroughtForwardIndicator>
```

#### `cbc:BasedOnConsensusIndicator`

```xml
<cbc:BasedOnConsensusIndicator>true</cbc:BasedOnConsensusIndicator>
```

#### `cbc:ChargeIndicator`

```xml
<cbc:ChargeIndicator>false</cbc:ChargeIndicator>
<cbc:ChargeIndicator>true</cbc:ChargeIndicator>
```

#### `cbc:ContainerizedIndicator`

```xml
<cbc:ContainerizedIndicator>0</cbc:ContainerizedIndicator>
<cbc:ContainerizedIndicator>true</cbc:ContainerizedIndicator>
```

#### `cbc:CopyIndicator`

```xml
<cbc:CopyIndicator>false</cbc:CopyIndicator>
```

#### `cbc:FridayAvailabilityIndicator`

```xml
<cbc:FridayAvailabilityIndicator>true</cbc:FridayAvailabilityIndicator>
```

#### `cbc:HazardousRiskIndicator`

```xml
<cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
```

#### `cbc:InitiatingPartyIndicator`

```xml
<cbc:InitiatingPartyIndicator>true</cbc:InitiatingPartyIndicator>
```

#### `cbc:MondayAvailabilityIndicator`

```xml
<cbc:MondayAvailabilityIndicator>true</cbc:MondayAvailabilityIndicator>
```

#### `cbc:OnCarriageIndicator`

```xml
<cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
```

#### `cbc:PartialDeliveryIndicator`

```xml
<cbc:PartialDeliveryIndicator>false</cbc:PartialDeliveryIndicator>
```

#### `cbc:PowerIndicator`

```xml
<cbc:PowerIndicator>false</cbc:PowerIndicator>
<cbc:PowerIndicator>true</cbc:PowerIndicator>
```

#### `cbc:PreCarriageIndicator`

```xml
<cbc:PreCarriageIndicator>false</cbc:PreCarriageIndicator>
<cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
```

#### `cbc:PrivatePartyIndicator`

```xml
<cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
```

#### `cbc:RefrigeratedIndicator`

```xml
<cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
<cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
```

#### `cbc:ReturnabilityIndicator`

```xml
<cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
```

#### `cbc:SaturdayAvailabilityIndicator`

```xml
<cbc:SaturdayAvailabilityIndicator>true</cbc:SaturdayAvailabilityIndicator>
```

#### `cbc:StatusAvailableIndicator`

```xml
<cbc:StatusAvailableIndicator>true</cbc:StatusAvailableIndicator>
```

#### `cbc:SundayAvailabilityIndicator`

```xml
<cbc:SundayAvailabilityIndicator>true</cbc:SundayAvailabilityIndicator>
```

#### `cbc:TaxEvidenceIndicator`

```xml
<cbc:TaxEvidenceIndicator>false</cbc:TaxEvidenceIndicator>
<cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
```

#### `cbc:TestIndicator`

```xml
<cbc:TestIndicator>true</cbc:TestIndicator>
```

#### `cbc:ThursdayAvailabilityIndicator`

```xml
<cbc:ThursdayAvailabilityIndicator>true</cbc:ThursdayAvailabilityIndicator>
```

#### `cbc:TuesdayAvailabilityIndicator`

```xml
<cbc:TuesdayAvailabilityIndicator>true</cbc:TuesdayAvailabilityIndicator>
```

#### `cbc:WednesdayAvailabilityIndicator`

```xml
<cbc:WednesdayAvailabilityIndicator>true</cbc:WednesdayAvailabilityIndicator>
```

[↑ Back to contents](#contents)

### Measure (`udt:MeasureType`)

_23 elements_

#### `cbc:ComparedValueMeasure`

```xml
<cbc:ComparedValueMeasure>2</cbc:ComparedValueMeasure>
```

**`@unitCode`**

```xml
<cbc:ComparedValueMeasure unitCode="KGM">2</cbc:ComparedValueMeasure>
```

#### `cbc:DurationMeasure`

```xml
<cbc:DurationMeasure>30</cbc:DurationMeasure>
<cbc:DurationMeasure>90</cbc:DurationMeasure>
```

**`@unitCode`**

```xml
<cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
<cbc:DurationMeasure unitCode="MIN">30</cbc:DurationMeasure>
```

#### `cbc:GrossMassMeasure`

```xml
<cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
```

**`@unitCode`**

```xml
<cbc:GrossMassMeasure unitCode="KGM">25730</cbc:GrossMassMeasure>
```

#### `cbc:GrossVolumeMeasure`

```xml
<cbc:GrossVolumeMeasure>0.336</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure>1.536</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure>78</cbc:GrossVolumeMeasure>
```

**`@unitCode`**

```xml
<cbc:GrossVolumeMeasure unitCode="MTQ">0.336</cbc:GrossVolumeMeasure>
```

#### `cbc:GrossWeightMeasure`

```xml
<cbc:GrossWeightMeasure>1.5</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure>1000.0</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure>12</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure>230.80</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure>600</cbc:GrossWeightMeasure>
```
_7 more values in examples_

**`@unitCode`**

```xml
<cbc:GrossWeightMeasure unitCode="KG">774.14400</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">1.5</cbc:GrossWeightMeasure>
```

#### `cbc:LatitudeDegreesMeasure`

```xml
<cbc:LatitudeDegreesMeasure>53.33</cbc:LatitudeDegreesMeasure>
<cbc:LatitudeDegreesMeasure>53.4</cbc:LatitudeDegreesMeasure>
<cbc:LatitudeDegreesMeasure>58</cbc:LatitudeDegreesMeasure>
```

**`@unitCode`**

```xml
<cbc:LatitudeDegreesMeasure unitCode="DD">53.33</cbc:LatitudeDegreesMeasure>
```

#### `cbc:LatitudeMinutesMeasure`

```xml
<cbc:LatitudeMinutesMeasure>33</cbc:LatitudeMinutesMeasure>
<cbc:LatitudeMinutesMeasure>49</cbc:LatitudeMinutesMeasure>
```

**`@unitCode`**

```xml
<cbc:LatitudeMinutesMeasure unitCode="DD">33</cbc:LatitudeMinutesMeasure>
```

#### `cbc:LeadTimeMeasure`

```xml
<cbc:LeadTimeMeasure>3</cbc:LeadTimeMeasure>
```

**`@unitCode`**

```xml
<cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
```

#### `cbc:LoadingLengthMeasure`

```xml
<cbc:LoadingLengthMeasure>0</cbc:LoadingLengthMeasure>
<cbc:LoadingLengthMeasure>12</cbc:LoadingLengthMeasure>
```

**`@unitCode`**

```xml
<cbc:LoadingLengthMeasure unitCode="MTR">0</cbc:LoadingLengthMeasure>
```

#### `cbc:LongitudeDegreesMeasure`

```xml
<cbc:LongitudeDegreesMeasure>10</cbc:LongitudeDegreesMeasure>
<cbc:LongitudeDegreesMeasure>8.33</cbc:LongitudeDegreesMeasure>
<cbc:LongitudeDegreesMeasure>8.48</cbc:LongitudeDegreesMeasure>
```

**`@unitCode`**

```xml
<cbc:LongitudeDegreesMeasure unitCode="DD">8.33</cbc:LongitudeDegreesMeasure>
```

#### `cbc:LongitudeMinutesMeasure`

```xml
<cbc:LongitudeMinutesMeasure>27</cbc:LongitudeMinutesMeasure>
<cbc:LongitudeMinutesMeasure>49</cbc:LongitudeMinutesMeasure>
```

**`@unitCode`**

```xml
<cbc:LongitudeMinutesMeasure unitCode="DD">27</cbc:LongitudeMinutesMeasure>
```

#### `cbc:MaximumDataLossDurationMeasure`

```xml
<cbc:MaximumDataLossDurationMeasure>24</cbc:MaximumDataLossDurationMeasure>
```

**`@unitCode`**

```xml
<cbc:MaximumDataLossDurationMeasure unitCode="HUR">24</cbc:MaximumDataLossDurationMeasure>
```

#### `cbc:MaximumIncidentNotificationDurationMeasure`

```xml
<cbc:MaximumIncidentNotificationDurationMeasure>4</cbc:MaximumIncidentNotificationDurationMeasure>
```

**`@unitCode`**

```xml
<cbc:MaximumIncidentNotificationDurationMeasure unitCode="HUR">4</cbc:MaximumIncidentNotificationDurationMeasure>
```

#### `cbc:MeanTimeToRecoverDurationMeasure`

```xml
<cbc:MeanTimeToRecoverDurationMeasure>3</cbc:MeanTimeToRecoverDurationMeasure>
```

**`@unitCode`**

```xml
<cbc:MeanTimeToRecoverDurationMeasure unitCode="HUR">3</cbc:MeanTimeToRecoverDurationMeasure>
```

#### `cbc:Measure`

```xml
<cbc:Measure>12.288</cbc:Measure>
<cbc:Measure>2.44</cbc:Measure>
<cbc:Measure>2.6</cbc:Measure>
<cbc:Measure>60</cbc:Measure>
<cbc:Measure>9.6</cbc:Measure>
```
_12 more values in examples_

**`@unitCode`**

```xml
<cbc:Measure unitCode="CEL">3.00</cbc:Measure>
<cbc:Measure unitCode="KGM">88</cbc:Measure>
<cbc:Measure unitCode="MTQ">0.336</cbc:Measure>
```

#### `cbc:MinimumDownTimeScheduleDurationMeasure`

```xml
<cbc:MinimumDownTimeScheduleDurationMeasure>3</cbc:MinimumDownTimeScheduleDurationMeasure>
```

**`@unitCode`**

```xml
<cbc:MinimumDownTimeScheduleDurationMeasure unitCode="DAY">3</cbc:MinimumDownTimeScheduleDurationMeasure>
```

#### `cbc:MinimumResponseTimeDurationMeasure`

```xml
<cbc:MinimumResponseTimeDurationMeasure>300</cbc:MinimumResponseTimeDurationMeasure>
```

**`@unitCode`**

```xml
<cbc:MinimumResponseTimeDurationMeasure unitCode="SEC">300</cbc:MinimumResponseTimeDurationMeasure>
```

#### `cbc:NetNetWeightMeasure`

```xml
<cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
```

**`@unitCode`**

```xml
<cbc:NetNetWeightMeasure unitCode="KGM">100</cbc:NetNetWeightMeasure>
```

#### `cbc:NetVolumeMeasure`

```xml
<cbc:NetVolumeMeasure>0.336000</cbc:NetVolumeMeasure>
<cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
```

**`@unitCode`**

```xml
<cbc:NetVolumeMeasure unitCode="MTQ">0.336000</cbc:NetVolumeMeasure>
```

#### `cbc:NetWeightMeasure`

```xml
<cbc:NetWeightMeasure>1</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure>3000</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure>76.00</cbc:NetWeightMeasure>
```

**`@unitCode`**

```xml
<cbc:NetWeightMeasure unitCode="KG">604.80000</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure unitCode="KGM">1</cbc:NetWeightMeasure>
```

#### `cbc:PostEventNotificationDurationMeasure`

```xml
<cbc:PostEventNotificationDurationMeasure>10</cbc:PostEventNotificationDurationMeasure>
```

**`@unitCode`**

```xml
<cbc:PostEventNotificationDurationMeasure unitCode="MIN">10</cbc:PostEventNotificationDurationMeasure>
```

#### `cbc:SourceValueMeasure`

```xml
<cbc:SourceValueMeasure>2.1</cbc:SourceValueMeasure>
```

**`@unitCode`**

```xml
<cbc:SourceValueMeasure unitCode="KGM">2.1</cbc:SourceValueMeasure>
```

#### `cbc:ValueMeasure`

```xml
<cbc:ValueMeasure>0.2</cbc:ValueMeasure>
```

**`@unitCode`**

```xml
<cbc:ValueMeasure unitCode="KGM">0.2</cbc:ValueMeasure>
```

[↑ Back to contents](#contents)

### Name (`udt:NameType`)

_14 elements_

#### `cbc:AdditionalStreetName`

```xml
<cbc:AdditionalStreetName>2nd floor</cbc:AdditionalStreetName>
<cbc:AdditionalStreetName>AdditionalStreet Example</cbc:AdditionalStreetName>
<cbc:AdditionalStreetName>Back door</cbc:AdditionalStreetName>
<cbc:AdditionalStreetName>Side door</cbc:AdditionalStreetName>
<cbc:AdditionalStreetName>Suite 123</cbc:AdditionalStreetName>
```
_1 more value in examples_

#### `cbc:BrandName`

```xml
<cbc:BrandName>Canon</cbc:BrandName>
```

#### `cbc:BuildingName`

```xml
<cbc:BuildingName>Banking House</cbc:BuildingName>
<cbc:BuildingName>Suite M-102</cbc:BuildingName>
<cbc:BuildingName>The Mall</cbc:BuildingName>
<cbc:BuildingName>Thereabouts</cbc:BuildingName>
```

#### `cbc:CityName`

```xml
<cbc:CityName>Billerica</cbc:CityName>
<cbc:CityName>Copenhagen</cbc:CityName>
<cbc:CityName>Hamburg</cbc:CityName>
<cbc:CityName>Helsinki</cbc:CityName>
<cbc:CityName>Munchen</cbc:CityName>
```
_48 more values in examples_

#### `cbc:FamilyName`

```xml
<cbc:FamilyName>GONZALES</cbc:FamilyName>
<cbc:FamilyName>Pereson</cbc:FamilyName>
<cbc:FamilyName>Petersen</cbc:FamilyName>
<cbc:FamilyName>ROSSI</cbc:FamilyName>
<cbc:FamilyName>Svensson</cbc:FamilyName>
```
_7 more values in examples_

#### `cbc:FirstName`

```xml
<cbc:FirstName>Antonio</cbc:FirstName>
<cbc:FirstName>GIORGIO</cbc:FirstName>
<cbc:FirstName>John</cbc:FirstName>
<cbc:FirstName>Kirsten</cbc:FirstName>
<cbc:FirstName>Lars</cbc:FirstName>
```
_5 more values in examples_

#### `cbc:MiddleName`

```xml
<cbc:MiddleName>Doe</cbc:MiddleName>
<cbc:MiddleName>M</cbc:MiddleName>
<cbc:MiddleName>N</cbc:MiddleName>
<cbc:MiddleName>Salemacher</cbc:MiddleName>
<cbc:MiddleName>X</cbc:MiddleName>
```

#### `cbc:ModelName`

```xml
<cbc:ModelName>MPX2000</cbc:ModelName>
<cbc:ModelName>ModelName28</cbc:ModelName>
```

#### `cbc:Name`

```xml
<cbc:Name>D2D GmbH</cbc:Name>
<cbc:Name>Delcomputer A/S</cbc:Name>
<cbc:Name>Disfruta</cbc:Name>
<cbc:Name>FirstAgency</cbc:Name>
<cbc:Name>Shop 37</cbc:Name>
```
_175 more values in examples_

#### `cbc:RegistrationName`

```xml
<cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
<cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
<cbc:RegistrationName>Moderna Produkter AB</cbc:RegistrationName>
<cbc:RegistrationName>The Sellercompany Incorporated</cbc:RegistrationName>
<cbc:RegistrationName>The buyercompany inc.</cbc:RegistrationName>
```
_7 more values in examples_

#### `cbc:RetailEventName`

```xml
<cbc:RetailEventName>ACME NEW BRANCH OPENNING</cbc:RetailEventName>
```

#### `cbc:ServiceName`

```xml
<cbc:ServiceName>Road transport service in Bavaria area</cbc:ServiceName>
```

#### `cbc:StreetName`

```xml
<cbc:StreetName>One Hundred Road</cbc:StreetName>
<cbc:StreetName>Slet Parkvej</cbc:StreetName>
<cbc:StreetName>Slotsholmsgade</cbc:StreetName>
<cbc:StreetName>Street</cbc:StreetName>
<cbc:StreetName>Via Emilia</cbc:StreetName>
```
_54 more values in examples_

#### `cbc:VesselName`

```xml
<cbc:VesselName>MS Enova</cbc:VesselName>
<cbc:VesselName>SomeVesselName</cbc:VesselName>
<cbc:VesselName>Vessel Name</cbc:VesselName>
```

[↑ Back to contents](#contents)

### Numeric (`udt:NumericType`)

_6 elements_

#### `cbc:FrozenPeriodDaysNumeric`

```xml
<cbc:FrozenPeriodDaysNumeric>3</cbc:FrozenPeriodDaysNumeric>
```

#### `cbc:LineNumberNumeric`

```xml
<cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
```

#### `cbc:MaximumCopiesNumeric`

```xml
<cbc:MaximumCopiesNumeric>4</cbc:MaximumCopiesNumeric>
<cbc:MaximumCopiesNumeric>5</cbc:MaximumCopiesNumeric>
```

#### `cbc:MultiplierFactorNumeric`

```xml
<cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
<cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
<cbc:MultiplierFactorNumeric>0.10</cbc:MultiplierFactorNumeric>
<cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
```

#### `cbc:OrderIntervalDaysNumeric`

```xml
<cbc:OrderIntervalDaysNumeric>3</cbc:OrderIntervalDaysNumeric>
```

#### `cbc:SequenceNumeric`

```xml
<cbc:SequenceNumeric>1</cbc:SequenceNumeric>
<cbc:SequenceNumeric>2</cbc:SequenceNumeric>
<cbc:SequenceNumeric>3</cbc:SequenceNumeric>
```

[↑ Back to contents](#contents)

### Percent (`udt:PercentType`)

_4 elements_

#### `cbc:AvailabilityTimePercent`

```xml
<cbc:AvailabilityTimePercent>94.0</cbc:AvailabilityTimePercent>
<cbc:AvailabilityTimePercent>98.5</cbc:AvailabilityTimePercent>
```

#### `cbc:Percent`

```xml
<cbc:Percent>0</cbc:Percent>
<cbc:Percent>10</cbc:Percent>
<cbc:Percent>17.5</cbc:Percent>
<cbc:Percent>21.00</cbc:Percent>
<cbc:Percent>25</cbc:Percent>
```
_1 more value in examples_

#### `cbc:ReliabilityPercent`

```xml
<cbc:ReliabilityPercent>100.0</cbc:ReliabilityPercent>
<cbc:ReliabilityPercent>80</cbc:ReliabilityPercent>
```

#### `cbc:TargetServicePercent`

```xml
<cbc:TargetServicePercent>1</cbc:TargetServicePercent>
```

[↑ Back to contents](#contents)

### Quantity (`udt:QuantityType`)

_24 elements_

#### `cbc:BackorderQuantity`

```xml
<cbc:BackorderQuantity>10</cbc:BackorderQuantity>
```

**`@unitCode`**

```xml
<cbc:BackorderQuantity unitCode="KG">10</cbc:BackorderQuantity>
<cbc:BackorderQuantity unitCode="KGM">10</cbc:BackorderQuantity>
```

#### `cbc:BaseQuantity`

```xml
<cbc:BaseQuantity>1</cbc:BaseQuantity>
```

**`@unitCode`**

```xml
<cbc:BaseQuantity unitCode="KG">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="LTR">1</cbc:BaseQuantity>
```

#### `cbc:CreditedQuantity`

```xml
<cbc:CreditedQuantity>-1</cbc:CreditedQuantity>
<cbc:CreditedQuantity>1</cbc:CreditedQuantity>
<cbc:CreditedQuantity>100</cbc:CreditedQuantity>
<cbc:CreditedQuantity>2</cbc:CreditedQuantity>
<cbc:CreditedQuantity>250</cbc:CreditedQuantity>
```

**`@unitCode`**

```xml
<cbc:CreditedQuantity unitCode="C62">-1</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="KG">100</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="KGM">100</cbc:CreditedQuantity>
```

#### `cbc:CustomsTariffQuantity`

```xml
<cbc:CustomsTariffQuantity>100</cbc:CustomsTariffQuantity>
<cbc:CustomsTariffQuantity>1000</cbc:CustomsTariffQuantity>
```

#### `cbc:DebitedQuantity`

```xml
<cbc:DebitedQuantity>-1</cbc:DebitedQuantity>
<cbc:DebitedQuantity>1</cbc:DebitedQuantity>
<cbc:DebitedQuantity>2</cbc:DebitedQuantity>
<cbc:DebitedQuantity>250</cbc:DebitedQuantity>
```

**`@unitCode`**

```xml
<cbc:DebitedQuantity unitCode="C62">-1</cbc:DebitedQuantity>
<cbc:DebitedQuantity unitCode="EA">1</cbc:DebitedQuantity>
```

#### `cbc:DeliveredQuantity`

```xml
<cbc:DeliveredQuantity>90</cbc:DeliveredQuantity>
```

**`@unitCode`**

```xml
<cbc:DeliveredQuantity unitCode="KG">90</cbc:DeliveredQuantity>
<cbc:DeliveredQuantity unitCode="KGM">90</cbc:DeliveredQuantity>
```

#### `cbc:InvoicedQuantity`

```xml
<cbc:InvoicedQuantity>-1</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity>1</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity>100</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity>2</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity>250</cbc:InvoicedQuantity>
```

**`@unitCode`**

```xml
<cbc:InvoicedQuantity unitCode="C62">-1</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="KG">100</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="KGM">100</cbc:InvoicedQuantity>
```

#### `cbc:MinimumInventoryQuantity`

```xml
<cbc:MinimumInventoryQuantity>8</cbc:MinimumInventoryQuantity>
```

#### `cbc:MinimumQuantity`

```xml
<cbc:MinimumQuantity>2</cbc:MinimumQuantity>
```

#### `cbc:MultipleOrderQuantity`

```xml
<cbc:MultipleOrderQuantity>1</cbc:MultipleOrderQuantity>
```

#### `cbc:PackQuantity`

```xml
<cbc:PackQuantity>1</cbc:PackQuantity>
<cbc:PackQuantity>63</cbc:PackQuantity>
```

**`@unitCode`**

```xml
<cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
```

#### `cbc:PerformanceValueQuantity`

```xml
<cbc:PerformanceValueQuantity>120</cbc:PerformanceValueQuantity>
<cbc:PerformanceValueQuantity>160</cbc:PerformanceValueQuantity>
```

**`@unitCode`**

```xml
<cbc:PerformanceValueQuantity unitCode="EA">120</cbc:PerformanceValueQuantity>
```

#### `cbc:Quantity`

```xml
<cbc:Quantity>10</cbc:Quantity>
<cbc:Quantity>120</cbc:Quantity>
<cbc:Quantity>20</cbc:Quantity>
<cbc:Quantity>200</cbc:Quantity>
<cbc:Quantity>3</cbc:Quantity>
```
_15 more values in examples_

**`@unitCode`**

```xml
<cbc:Quantity unitCode="CT">63.000</cbc:Quantity>
<cbc:Quantity unitCode="EA">1</cbc:Quantity>
<cbc:Quantity unitCode="KGM">100</cbc:Quantity>
```

#### `cbc:ReceivedQuantity`

```xml
<cbc:ReceivedQuantity>90</cbc:ReceivedQuantity>
```

**`@unitCode`**

```xml
<cbc:ReceivedQuantity unitCode="KG">90</cbc:ReceivedQuantity>
<cbc:ReceivedQuantity unitCode="KGM">90</cbc:ReceivedQuantity>
```

#### `cbc:ShortQuantity`

```xml
<cbc:ShortQuantity>10</cbc:ShortQuantity>
```

**`@unitCode`**

```xml
<cbc:ShortQuantity unitCode="KG">10</cbc:ShortQuantity>
<cbc:ShortQuantity unitCode="KGM">10</cbc:ShortQuantity>
```

#### `cbc:TargetInventoryQuantity`

```xml
<cbc:TargetInventoryQuantity>20</cbc:TargetInventoryQuantity>
```

**`@unitCode`**

```xml
<cbc:TargetInventoryQuantity unitCode="KGM">20</cbc:TargetInventoryQuantity>
```

#### `cbc:ThresholdQuantity`

```xml
<cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
```

**`@unitCode`**

```xml
<cbc:ThresholdQuantity unitCode="KGM">120000</cbc:ThresholdQuantity>
```

#### `cbc:TimeDeltaDaysQuantity`

```xml
<cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
```

#### `cbc:TotalGoodsItemQuantity`

```xml
<cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
<cbc:TotalGoodsItemQuantity>10</cbc:TotalGoodsItemQuantity>
<cbc:TotalGoodsItemQuantity>1500</cbc:TotalGoodsItemQuantity>
<cbc:TotalGoodsItemQuantity>23</cbc:TotalGoodsItemQuantity>
<cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
```
_1 more value in examples_

**`@unitCode`**

```xml
<cbc:TotalGoodsItemQuantity unitCode="EA">2</cbc:TotalGoodsItemQuantity>
```

#### `cbc:TotalPackageQuantity`

```xml
<cbc:TotalPackageQuantity>1</cbc:TotalPackageQuantity>
<cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
<cbc:TotalPackageQuantity>2</cbc:TotalPackageQuantity>
```

**`@unitCode`**

```xml
<cbc:TotalPackageQuantity unitCode="EA">1</cbc:TotalPackageQuantity>
```

#### `cbc:TotalPackagesQuantity`

```xml
<cbc:TotalPackagesQuantity>1</cbc:TotalPackagesQuantity>
<cbc:TotalPackagesQuantity>5</cbc:TotalPackagesQuantity>
```

#### `cbc:TotalTransportHandlingUnitQuantity`

```xml
<cbc:TotalTransportHandlingUnitQuantity>1</cbc:TotalTransportHandlingUnitQuantity>
<cbc:TotalTransportHandlingUnitQuantity>10</cbc:TotalTransportHandlingUnitQuantity>
<cbc:TotalTransportHandlingUnitQuantity>2</cbc:TotalTransportHandlingUnitQuantity>
```

**`@unitCode`**

```xml
<cbc:TotalTransportHandlingUnitQuantity unitCode="EA">1</cbc:TotalTransportHandlingUnitQuantity>
```

#### `cbc:ValueQuantity`

```xml
<cbc:ValueQuantity>604.8</cbc:ValueQuantity>
<cbc:ValueQuantity>63.000</cbc:ValueQuantity>
<cbc:ValueQuantity>774.144</cbc:ValueQuantity>
```

**`@unitCode`**

```xml
<cbc:ValueQuantity unitCode="CT">63.000</cbc:ValueQuantity>
<cbc:ValueQuantity unitCode="KG">604.8</cbc:ValueQuantity>
```

#### `cbc:VarianceQuantity`

```xml
<cbc:VarianceQuantity>20</cbc:VarianceQuantity>
```

**`@unitCode`**

```xml
<cbc:VarianceQuantity unitCode="KGM">20</cbc:VarianceQuantity>
```

[↑ Back to contents](#contents)

### Rate (`udt:RateType`)

_3 elements_

#### `cbc:CalculationRate`

```xml
<cbc:CalculationRate>1.8947</cbc:CalculationRate>
```

#### `cbc:SourceCurrencyBaseRate`

```xml
<cbc:SourceCurrencyBaseRate>1.00</cbc:SourceCurrencyBaseRate>
```

#### `cbc:TargetCurrencyBaseRate`

```xml
<cbc:TargetCurrencyBaseRate>1.00</cbc:TargetCurrencyBaseRate>
```

[↑ Back to contents](#contents)

### Text (`udt:TextType`)

_75 elements_

#### `cbc:AccountingCost`

```xml
<cbc:AccountingCost>BookingCode001</cbc:AccountingCost>
<cbc:AccountingCost>BookingCode002</cbc:AccountingCost>
<cbc:AccountingCost>Project cost code 123</cbc:AccountingCost>
```

#### `cbc:ActualArrivalDate`

```xml
<cbc:ActualArrivalDate>2010-04-30</cbc:ActualArrivalDate>
```

#### `cbc:ActualArrivalTime`

```xml
<cbc:ActualArrivalTime>13:20:00.0Z</cbc:ActualArrivalTime>
```

#### `cbc:ActualDepartureDate`

```xml
<cbc:ActualDepartureDate>2010-04-30</cbc:ActualDepartureDate>
```

#### `cbc:ActualDepartureTime`

```xml
<cbc:ActualDepartureTime>14:20:00.0Z</cbc:ActualDepartureTime>
```

#### `cbc:AllowanceChargeReason`

```xml
<cbc:AllowanceChargeReason>Donation to the Red Cross</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Handling fee</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Remove previously granted discount</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Transport documents</cbc:AllowanceChargeReason>
```
_9 more values in examples_

#### `cbc:ApprovalStatus`

```xml
<cbc:ApprovalStatus>Issued</cbc:ApprovalStatus>
```

#### `cbc:BackorderReason`

```xml
<cbc:BackorderReason>lack of stock as explained on telephone today</cbc:BackorderReason>
```

#### `cbc:BriefDescription`

```xml
<cbc:BriefDescription>OASIS is a nonprofit consortium that drives the development, convergence and adoption of open standards for the global information society.  OASIS promotes industry consensus and produces worldwide standards for security, Internet of Things, cloud computing, energy, content technologies, emergency management, and other areas. OASIS open standards offer the potential to lower cost, stimulate innovation, grow global markets, and protect the right of free choice of technology.  OASIS members broadly represent the marketplace of public and private sector technology leaders, users and influencers. The consortium has more than 5,000 participants representing over 600 organizations and individual members in more than 65 countries.  OASIS is distinguished by its transparent governance and operating procedures. Members themselves set the OASIS technical agenda, using a lightweight process expressly designed to promote industry consensus and unite disparate efforts. Completed work is ratified by open ballot. Governance is accountable and unrestricted. Officers of both the OASIS Board of Directors and Technical Advisory Board are chosen by democratic election to serve two-year terms. Consortium leadership is based on individual merit and is not tied to financial contribution, corporate standing, or special appointment.  OASIS Member Sections include AMQP, Emergency, IDtrust, LegalXML, Open CSA, OSLC, and WS-I.</cbc:BriefDescription>
```

#### `cbc:BuildingNumber`

```xml
<cbc:BuildingNumber>152</cbc:BuildingNumber>
<cbc:BuildingNumber>161</cbc:BuildingNumber>
<cbc:BuildingNumber>29</cbc:BuildingNumber>
<cbc:BuildingNumber>35</cbc:BuildingNumber>
<cbc:BuildingNumber>5</cbc:BuildingNumber>
```
_19 more values in examples_

#### `cbc:CancellationNote`

```xml
<cbc:CancellationNote>The quality check has detected that the beeswax doesn't become liquid at the
        expected temperature.</cbc:CancellationNote>
<cbc:CancellationNote>With reference to phone call</cbc:CancellationNote>
```

#### `cbc:Condition`

```xml
<cbc:Condition>IN_RIGHT_CONDITION</cbc:Condition>
```

#### `cbc:ConditionDeviationIndicator`

```xml
<cbc:ConditionDeviationIndicator>false</cbc:ConditionDeviationIndicator>
```

#### `cbc:ContractType`

```xml
<cbc:ContractType>Continuing Transport Contract</cbc:ContractType>
<cbc:ContractType>Forwarding Instructions</cbc:ContractType>
<cbc:ContractType>FrameworkAgreementID123</cbc:ContractType>
```

#### `cbc:CountrySubentity`

```xml
<cbc:CountrySubentity>Avon</cbc:CountrySubentity>
<cbc:CountrySubentity>Heremouthshire</cbc:CountrySubentity>
<cbc:CountrySubentity>London</cbc:CountrySubentity>
<cbc:CountrySubentity>Massachusetts</cbc:CountrySubentity>
<cbc:CountrySubentity>RegionA</cbc:CountrySubentity>
```
_3 more values in examples_

#### `cbc:DeliveryInstructions`

```xml
<cbc:DeliveryInstructions>El Dorado</cbc:DeliveryInstructions>
<cbc:DeliveryInstructions>Test</cbc:DeliveryInstructions>
<cbc:DeliveryInstructions>abcd</cbc:DeliveryInstructions>
```

#### `cbc:Department`

```xml
<cbc:Department>Accounting department</cbc:Department>
<cbc:Department>Gadgets</cbc:Department>
<cbc:Department>Marketing Office</cbc:Department>
<cbc:Department>Purchasing department</cbc:Department>
<cbc:Department>Sales department</cbc:Department>
```
_2 more values in examples_

#### `cbc:Description`

```xml
<cbc:Description>Acme knitwear scarf</cbc:Description>
<cbc:Description>METABO GE700, Pinolsliber</cbc:Description>
<cbc:Description>MOTOR CYCLE</cbc:Description>
<cbc:Description>Office Printer 1</cbc:Description>
<cbc:Description>Shop in the city center</cbc:Description>
```
_87 more values in examples_

**`@languageID`**

```xml
<cbc:Description languageID="CN">本国海域或公海捕捞的鱼类或水生无脊椎动物或养殖水生动物</cbc:Description>
<cbc:Description languageID="DK">fisk eller havdyr, der ikke er pattedyr, som er fanget enten i landets eller reg</cbc:Description>
<cbc:Description languageID="EN">Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:
				3MB. Screen 1440x900</cbc:Description>
```

#### `cbc:DocumentDescription`

```xml
<cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
<cbc:DocumentDescription>Framework Agreement between Consignor and NECOSS</cbc:DocumentDescription>
```

#### `cbc:DocumentHash`

```xml
<cbc:DocumentHash>String</cbc:DocumentHash>
```

#### `cbc:DocumentType`

```xml
<cbc:DocumentType>Annual Contract</cbc:DocumentType>
<cbc:DocumentType>Drawing</cbc:DocumentType>
<cbc:DocumentType>Preliminary sales receipt</cbc:DocumentType>
<cbc:DocumentType>Shipment reference</cbc:DocumentType>
<cbc:DocumentType>Timesheet</cbc:DocumentType>
```
_9 more values in examples_

#### `cbc:ElectronicMail`

```xml
<cbc:ElectronicMail>SomeName@consignee.de</cbc:ElectronicMail>
<cbc:ElectronicMail>SomeName@necoss.de</cbc:ElectronicMail>
<cbc:ElectronicMail>SomeName@ntt.de</cbc:ElectronicMail>
<cbc:ElectronicMail>delta@betashop.it</cbc:ElectronicMail>
<cbc:ElectronicMail>jsmith@example.com</cbc:ElectronicMail>
```
_38 more values in examples_

#### `cbc:EmbeddedDocument`

```xml
<cbc:EmbeddedDocument>;lkajdf;lkasd;ljkasdf;lkja;sdlfkja;sldfkja;sdlfjkas;dlkfjas;dlfjas;dlkfjas;dlkfja;slkdjf</cbc:EmbeddedDocument>
```

#### `cbc:EstimatedArrivalDate`

```xml
<cbc:EstimatedArrivalDate>2010-04-30</cbc:EstimatedArrivalDate>
```

#### `cbc:EstimatedArrivalTime`

```xml
<cbc:EstimatedArrivalTime>12:20:00.0Z</cbc:EstimatedArrivalTime>
```

#### `cbc:EstimatedDepartureDate`

```xml
<cbc:EstimatedDepartureDate>2010-04-30</cbc:EstimatedDepartureDate>
```

#### `cbc:EstimatedDepartureTime`

```xml
<cbc:EstimatedDepartureTime>13:20:00.0Z</cbc:EstimatedDepartureTime>
```

#### `cbc:ExemptionReason`

```xml
<cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
<cbc:ExemptionReason>N/A</cbc:ExemptionReason>
```

#### `cbc:Floor`

```xml
<cbc:Floor>1</cbc:Floor>
<cbc:Floor>2</cbc:Floor>
<cbc:Floor>4</cbc:Floor>
<cbc:Floor>5</cbc:Floor>
```

#### `cbc:HandlingInstructions`

```xml
<cbc:HandlingInstructions>HANDLE WITH CARE</cbc:HandlingInstructions>
```

#### `cbc:Information`

```xml
<cbc:Information>Professional equipment</cbc:Information>
```

#### `cbc:JobTitle`

```xml
<cbc:JobTitle>Boss</cbc:JobTitle>
<cbc:JobTitle>Purchasing manager</cbc:JobTitle>
<cbc:JobTitle>Sales manager</cbc:JobTitle>
<cbc:JobTitle>Store manager</cbc:JobTitle>
<cbc:JobTitle>Stuffuser</cbc:JobTitle>
```

#### `cbc:Line`

```xml
<cbc:Line>1. sal</cbc:Line>
<cbc:Line>3rd Floor, Room 5</cbc:Line>
<cbc:Line>IT-afdelingen</cbc:Line>
<cbc:Line>Ueberseetor 2</cbc:Line>
<cbc:Line>West Wing</cbc:Line>
```
_6 more values in examples_

#### `cbc:MarkAttention`

```xml
<cbc:MarkAttention>Peter Janssen</cbc:MarkAttention>
```

#### `cbc:MessageFormat`

```xml
<cbc:MessageFormat>1.2.840.113549.1.9.16.0.1</cbc:MessageFormat>
```

#### `cbc:Note`

```xml
<cbc:Note>Information text for the whole order change</cbc:Note>
<cbc:Note>PER THIRTY DAYS</cbc:Note>
<cbc:Note>Penalty percentage 10% from due date</cbc:Note>
<cbc:Note>as agreed on phone, the invoice should have been cancelled earlier, apologies</cbc:Note>
<cbc:Note>sample</cbc:Note>
```
_34 more values in examples_

**`@languageID`**

```xml
<cbc:Note languageID="da-dk">Bestilling af computere</cbc:Note>
<cbc:Note languageID="en">Ordered in our booth at the convention.</cbc:Note>
```

#### `cbc:OperationStatusCode`

```xml
<cbc:OperationStatusCode>AWAITING CUSTOMS</cbc:OperationStatusCode>
<cbc:OperationStatusCode>Delayed, in the course of transportation</cbc:OperationStatusCode>
```

#### `cbc:PackingMaterial`

```xml
<cbc:PackingMaterial>other</cbc:PackingMaterial>
```

#### `cbc:PaymentMeansDescription`

```xml
<cbc:PaymentMeansDescription>Cash</cbc:PaymentMeansDescription>
```

#### `cbc:PaymentNote`

```xml
<cbc:PaymentNote>Deutsche Bank</cbc:PaymentNote>
```

#### `cbc:PostalZone`

```xml
<cbc:PostalZone>02340</cbc:PostalZone>
<cbc:PostalZone>40128</cbc:PostalZone>
<cbc:PostalZone>6920</cbc:PostalZone>
<cbc:PostalZone>80331</cbc:PostalZone>
<cbc:PostalZone>80334</cbc:PostalZone>
```
_42 more values in examples_

#### `cbc:Postbox`

```xml
<cbc:Postbox>123</cbc:Postbox>
<cbc:Postbox>148</cbc:Postbox>
<cbc:Postbox>5467</cbc:Postbox>
<cbc:Postbox>99043</cbc:Postbox>
<cbc:Postbox>PoBox123</cbc:Postbox>
```
_2 more values in examples_

#### `cbc:PrintQualifier`

```xml
<cbc:PrintQualifier>Copies allowed</cbc:PrintQualifier>
```

#### `cbc:Region`

```xml
<cbc:Region>Bavaria</cbc:Region>
```

#### `cbc:RegistrationNationality`

```xml
<cbc:RegistrationNationality>Denmark</cbc:RegistrationNationality>
```

#### `cbc:Remarks`

```xml
<cbc:Remarks>DELAYED BY ONE HOUR</cbc:Remarks>
```

#### `cbc:ReplenishmentOwnerDescription`

```xml
<cbc:ReplenishmentOwnerDescription>Ownere-321</cbc:ReplenishmentOwnerDescription>
```

#### `cbc:Room`

```xml
<cbc:Room>29</cbc:Room>
<cbc:Room>309</cbc:Room>
```

#### `cbc:SequenceNumber`

```xml
<cbc:SequenceNumber>1</cbc:SequenceNumber>
```

#### `cbc:ShippingMarks`

```xml
<cbc:ShippingMarks>Agricultural products</cbc:ShippingMarks>
<cbc:ShippingMarks>General Cargo</cbc:ShippingMarks>
```

#### `cbc:SignatureMethod`

```xml
<cbc:SignatureMethod>urn:oasis:names:specification:ubl:dsig:detached</cbc:SignatureMethod>
<cbc:SignatureMethod>urn:oasis:names:specification:ubl:dsig:enveloped</cbc:SignatureMethod>
<cbc:SignatureMethod>urn:oasis:names:specification:ubl:profile:dsig:signature</cbc:SignatureMethod>
```

#### `cbc:SpecialInstructions`

```xml
<cbc:SpecialInstructions>1234</cbc:SpecialInstructions>
<cbc:SpecialInstructions>Beeswax becomes liquid at 50'C</cbc:SpecialInstructions>
<cbc:SpecialInstructions>Test</cbc:SpecialInstructions>
```

#### `cbc:SpecialTerms`

```xml
<cbc:SpecialTerms>1% deduction for late delivery as per contract</cbc:SpecialTerms>
<cbc:SpecialTerms>1% reduktion i kontraktsummen pr. dags forsinkelse jf. SKI kontrakt</cbc:SpecialTerms>
<cbc:SpecialTerms>CAD</cbc:SpecialTerms>
```

#### `cbc:StatusReason`

```xml
<cbc:StatusReason>Reefer container lost power - cargo of fish destroyed</cbc:StatusReason>
```

#### `cbc:SubsetID`

```xml
<cbc:SubsetID>urn:oasis:names:specification:ubl:schema:xsd:Quotation-2-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:DespatchAdvice-2.0:sbs-1.0-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:OrderResponseSimple-2.0:sbs-1.0-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:RemittanceAdvice-2.0:sbs-1.0-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:RequestForQuotation-2.0:sbs-1.0-draft</cbc:SubsetID>
```
_5 more values in examples_

#### `cbc:SummaryDescription`

```xml
<cbc:SummaryDescription>1 other</cbc:SummaryDescription>
<cbc:SummaryDescription>Electronic components</cbc:SummaryDescription>
```

#### `cbc:TariffDescription`

```xml
<cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
```

#### `cbc:TaxExemptionReason`

```xml
<cbc:TaxExemptionReason>Exempt New Means of Transport</cbc:TaxExemptionReason>
```

#### `cbc:Telefax`

```xml
<cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
<cbc:Telefax>0039 051 23000023</cbc:Telefax>
<cbc:Telefax>0039 059 33000055</cbc:Telefax>
<cbc:Telefax>0039 059 33000057</cbc:Telefax>
<cbc:Telefax>3456767</cbc:Telefax>
```
_17 more values in examples_

#### `cbc:Telephone`

```xml
<cbc:Telephone>+1 3362 4788</cbc:Telephone>
<cbc:Telephone>+49450557888</cbc:Telephone>
<cbc:Telephone>0039 051 23000008</cbc:Telephone>
<cbc:Telephone>0127 98876545</cbc:Telephone>
<cbc:Telephone>34557</cbc:Telephone>
```
_35 more values in examples_

#### `cbc:TimeDeviationIndicator`

```xml
<cbc:TimeDeviationIndicator>true</cbc:TimeDeviationIndicator>
```

#### `cbc:TimezoneOffset`

```xml
<cbc:TimezoneOffset>GMT+1</cbc:TimezoneOffset>
```

#### `cbc:TransportItemConditionDeviationIndicator`

```xml
<cbc:TransportItemConditionDeviationIndicator>false</cbc:TransportItemConditionDeviationIndicator>
```

#### `cbc:TransportItemTimeDeviationIndicator`

```xml
<cbc:TransportItemTimeDeviationIndicator>true</cbc:TransportItemTimeDeviationIndicator>
```

#### `cbc:TransportServiceProviderCancellationIndicator`

```xml
<cbc:TransportServiceProviderCancellationIndicator>false</cbc:TransportServiceProviderCancellationIndicator>
```

#### `cbc:TransportServiceProviderCompletionIndicator`

```xml
<cbc:TransportServiceProviderCompletionIndicator>false</cbc:TransportServiceProviderCompletionIndicator>
```

#### `cbc:TransportServiceProviderReadyForExecutionIndicator`

```xml
<cbc:TransportServiceProviderReadyForExecutionIndicator>true</cbc:TransportServiceProviderReadyForExecutionIndicator>
```

#### `cbc:TransportUserCancellationIndicator`

```xml
<cbc:TransportUserCancellationIndicator>false</cbc:TransportUserCancellationIndicator>
```

#### `cbc:TransportUserCompletionIndicator`

```xml
<cbc:TransportUserCompletionIndicator>false</cbc:TransportUserCompletionIndicator>
```

#### `cbc:TransportUserReadyForExecutionIndicator`

```xml
<cbc:TransportUserReadyForExecutionIndicator>true</cbc:TransportUserReadyForExecutionIndicator>
```

#### `cbc:TransportUserRemarks`

```xml
<cbc:TransportUserRemarks>DROP OFF AT RECEPTION</cbc:TransportUserRemarks>
```

#### `cbc:TransportationServiceDescription`

```xml
<cbc:TransportationServiceDescription>Complete D2D service from Munich, Germany to Hamar, Norway</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Insurance of goods during transportation</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Rail transport service from Bremen to Nurnberg</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Rail transport service from Hamburg to Bremen</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Road transport service from Hamburg to Bremen</cbc:TransportationServiceDescription>
```
_4 more values in examples_

#### `cbc:Value`

```xml
<cbc:Value>0</cbc:Value>
<cbc:Value>Black</cbc:Value>
<cbc:Value>Bovine</cbc:Value>
<cbc:Value>Cat5</cbc:Value>
<cbc:Value>TRUST2408 OCES Primary CA – TRUST2408 OCES CA II</cbc:Value>
```
_4 more values in examples_

#### `cbc:WeighingDeviceType`

```xml
<cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
```

#### `cbc:XPath`

```xml
<cbc:XPath>String</cbc:XPath>
```

[↑ Back to contents](#contents)

### Time (`udt:TimeType`)

_14 elements_

#### `cbc:ActualDeliveryTime`

```xml
<cbc:ActualDeliveryTime>11:30:00.0Z</cbc:ActualDeliveryTime>
```

#### `cbc:ActualDespatchTime`

```xml
<cbc:ActualDespatchTime>11:35:00.0Z</cbc:ActualDespatchTime>
<cbc:ActualDespatchTime>16:00:00</cbc:ActualDespatchTime>
<cbc:ActualDespatchTime>16:00:00Z</cbc:ActualDespatchTime>
```

#### `cbc:EndTime`

```xml
<cbc:EndTime>09:30:10+01:00</cbc:EndTime>
<cbc:EndTime>09:30:47.0Z</cbc:EndTime>
<cbc:EndTime>14:00:00.0Z</cbc:EndTime>
<cbc:EndTime>15:30:00</cbc:EndTime>
<cbc:EndTime>18:35:10+01:00</cbc:EndTime>
```
_22 more values in examples_

#### `cbc:ExpiryTime`

```xml
<cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
```

#### `cbc:IssueTime`

```xml
<cbc:IssueTime>09:00:00.0Z</cbc:IssueTime>
<cbc:IssueTime>10:00:30+01:00</cbc:IssueTime>
<cbc:IssueTime>14:00:00.0Z</cbc:IssueTime>
<cbc:IssueTime>15:30:00.0Z</cbc:IssueTime>
<cbc:IssueTime>15:31:00</cbc:IssueTime>
```
_29 more values in examples_

#### `cbc:LatestDeliveryTime`

```xml
<cbc:LatestDeliveryTime>18:00:00.0Z</cbc:LatestDeliveryTime>
```

#### `cbc:NominationTime`

```xml
<cbc:NominationTime>09:30:00.0Z</cbc:NominationTime>
```

#### `cbc:OccurrenceTime`

```xml
<cbc:OccurrenceTime>18:00:00+01:00</cbc:OccurrenceTime>
```

#### `cbc:PurchaseTime`

```xml
<cbc:PurchaseTime>11:10:00Z</cbc:PurchaseTime>
```

#### `cbc:ReferenceTime`

```xml
<cbc:ReferenceTime>14:20:00.0Z</cbc:ReferenceTime>
<cbc:ReferenceTime>18:55:00.0Z</cbc:ReferenceTime>
```

#### `cbc:SourceForecastIssueTime`

```xml
<cbc:SourceForecastIssueTime>10:00:00.000</cbc:SourceForecastIssueTime>
<cbc:SourceForecastIssueTime>10:00:00.000Z</cbc:SourceForecastIssueTime>
```

#### `cbc:StartTime`

```xml
<cbc:StartTime>01:00:00.0Z</cbc:StartTime>
<cbc:StartTime>08:00:00Z</cbc:StartTime>
<cbc:StartTime>15:30:00.0Z</cbc:StartTime>
<cbc:StartTime>16:30:00.0Z</cbc:StartTime>
<cbc:StartTime>22:00:00Z</cbc:StartTime>
```
_24 more values in examples_

#### `cbc:TransactionTime`

```xml
<cbc:TransactionTime>11:10:00Z</cbc:TransactionTime>
```

#### `cbc:WeighingTime`

```xml
<cbc:WeighingTime>00:30:00</cbc:WeighingTime>
<cbc:WeighingTime>00:30:00Z</cbc:WeighingTime>
```

[↑ Back to contents](#contents)

---

## cac Elements

_Grouped by ABIE type from `UBL-CommonAggregateComponents-2.5.xsd`. Structures are ordered from simplest to most complex._

### `ActivityDataLineType`

**Used as:** `cac:SupplyChainActivityDataLine`

_7 instances across 1 element, with 4 unique structures_

**Structure 1** — 4 instances

```xml
<cac:SupplyChainActivityDataLine>
  <cbc:ID>SCADL_SHIPMENT001</cbc:ID>
  <cbc:SupplyChainActivityTypeCode>SHIPMENTS</cbc:SupplyChainActivityTypeCode>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID>2203148000007</cbc:ID>
      </cac:PartyIdentification>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID>6903148000007</cbc:ID>
      </cac:PartyIdentification>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ActivityOriginLocation>
    <cbc:ID></cbc:ID>
  </cac:ActivityOriginLocation>
  <cac:SalesItem>
    <cbc:Quantity>20</cbc:Quantity>
    <cac:Item>
      <cac:StandardItemIdentification>
        <cbc:ID>06110123456784</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:SalesItem>
</cac:SupplyChainActivityDataLine>
```

**Structure 2** — 1 instance

```xml
<cac:SupplyChainActivityDataLine>
  <cbc:ID>1</cbc:ID>
  <cbc:SupplyChainActivityTypeCode>SALES</cbc:SupplyChainActivityTypeCode>
  <cac:ActivityOriginLocation>
    <cbc:Description>Shop in the city center</cbc:Description>
    <cac:Address>
      <cbc:StreetName>Via Rizzoli</cbc:StreetName>
      <cbc:BuildingNumber>208</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40121</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:ActivityOriginLocation>
  <cac:SalesItem>
    <cbc:Quantity>8</cbc:Quantity>
    <cac:Item>
      <cbc:Description>shirt</cbc:Description>
      <cac:BuyersItemIdentification>
        <cbc:ID>SH009</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>DD88</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:SalesItem>
  <cac:SalesItem>
    <cbc:Quantity>3</cbc:Quantity>
    <cac:Item>
      <cbc:Description>trousers</cbc:Description>
      <cac:BuyersItemIdentification>
        <cbc:ID>TH009</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>DA008</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:SalesItem>
</cac:SupplyChainActivityDataLine>
```

**Structure 3** — 1 instance

```xml
<cac:SupplyChainActivityDataLine>
  <cbc:ID>1</cbc:ID>
  <cbc:SupplyChainActivityTypeCode>SHIPMENTS</cbc:SupplyChainActivityTypeCode>
  <cac:ActivityOriginLocation>
    <cac:Address>
      <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
      <cbc:BuildingNumber>403</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40129</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:ActivityOriginLocation>
  <cac:ActivityFinalLocation>
    <cbc:Description>Shop in the city center</cbc:Description>
    <cac:Address>
      <cbc:StreetName>Via Rizzoli</cbc:StreetName>
      <cbc:BuildingNumber>208</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40121</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:ActivityFinalLocation>
  <cac:SalesItem>
    <cbc:Quantity>20</cbc:Quantity>
    <cac:Item>
      <cbc:Description>shirt</cbc:Description>
      <cac:BuyersItemIdentification>
        <cbc:ID>SH009</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>DD88</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:SalesItem>
</cac:SupplyChainActivityDataLine>
```

**Structure 4** — 1 instance

```xml
<cac:SupplyChainActivityDataLine>
  <cbc:ID>2</cbc:ID>
  <cbc:SupplyChainActivityTypeCode>SHIPMENTS</cbc:SupplyChainActivityTypeCode>
  <cac:ActivityOriginLocation>
    <cac:Address>
      <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
      <cbc:BuildingNumber>403</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40129</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:ActivityOriginLocation>
  <cac:ActivityFinalLocation>
    <cbc:Description>Store</cbc:Description>
    <cac:Address>
      <cbc:StreetName>Via Delle Fonti</cbc:StreetName>
      <cbc:BuildingNumber>209</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40128</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:ActivityFinalLocation>
  <cac:SalesItem>
    <cbc:Quantity>200</cbc:Quantity>
    <cac:Item>
      <cbc:Description>shirt</cbc:Description>
      <cac:BuyersItemIdentification>
        <cbc:ID>SH009</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>DD88</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:SalesItem>
  <cac:SalesItem>
    <cbc:Quantity>150</cbc:Quantity>
    <cac:Item>
      <cbc:Description>trousers</cbc:Description>
      <cac:BuyersItemIdentification>
        <cbc:ID>TH009</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>DA008</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:SalesItem>
</cac:SupplyChainActivityDataLine>
```

[↑ Back to contents](#contents)

### `AddressLineType`

**Used as:** `cac:AddressLine`

_364 instances across 1 element, with 1 unique structure_

**Structure 1** — 364 instances

```xml
<cac:AddressLine>
  <cbc:Line>3rd Floor, Room 5</cbc:Line>
</cac:AddressLine>
```

[↑ Back to contents](#contents)

### `AddressType`

**Used as:** `cac:Address` · `cac:DeliveryAddress` · `cac:DespatchAddress` · `cac:OriginAddress` · `cac:PostalAddress` · `cac:RegistrationAddress`

_621 instances across 6 elements, with 60 unique structures_

**Structure 1** — 2 instances

```xml
<cac:PostalAddress>
  <cbc:ID>4058673827000</cbc:ID>
</cac:PostalAddress>
```

**Structure 2** — 5 instances

```xml
<cac:Address>
  <cbc:CityName>Espoo</cbc:CityName>
</cac:Address>
```

**Structure 3** — 2 instances

```xml
<cac:DeliveryAddress>
  <cac:Country>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
  </cac:Country>
</cac:DeliveryAddress>
```

**Structure 4** — 4 instances

```xml
<cac:Address>
  <cac:Country>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 5** — 2 instances

```xml
<cac:DespatchAddress>
  <cac:Country>
    <cbc:IdentificationCode>RU</cbc:IdentificationCode>
  </cac:Country>
</cac:DespatchAddress>
```

**Structure 6** — 2 instances

```xml
<cac:OriginAddress>
  <cac:Country>
    <cbc:IdentificationCode>TH</cbc:IdentificationCode>
  </cac:Country>
</cac:OriginAddress>
```

**Structure 7** — 23 instances

```xml
<cac:PostalAddress>
  <cbc:CityName>London</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 8** — 1 instance

```xml
<cac:Address>
  <cbc:CityName>Tanger</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>MA</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 9** — 1 instance

```xml
<cac:Address>
  <cac:Country>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    <cbc:Name>Swiss</cbc:Name>
  </cac:Country>
</cac:Address>
```

**Structure 10** — 1 instance

```xml
<cac:OriginAddress>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:Country>
</cac:OriginAddress>
```

**Structure 11** — 2 instances

```xml
<cac:RegistrationAddress>
  <cbc:CityName>Stockholm</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>SE</cbc:IdentificationCode>
  </cac:Country>
</cac:RegistrationAddress>
```

**Structure 12** — 2 instances

```xml
<cac:PostalAddress>
  <cbc:StreetName>Vesterbrogade</cbc:StreetName>
  <cbc:BuildingNumber>78</cbc:BuildingNumber>
  <cbc:CityName>København K</cbc:CityName>
  <cbc:PostalZone>1258</cbc:PostalZone>
</cac:PostalAddress>
```

**Structure 13** — 2 instances

```xml
<cac:PostalAddress>
  <cbc:StreetName>Export Str. 143</cbc:StreetName>
  <cbc:CityName>Yang Mei</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>TH</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 14** — 1 instance

```xml
<cac:Address>
  <cbc:CityName>STORLIEN</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>SE</cbc:IdentificationCode>
    <cbc:Name>SWEDEN</cbc:Name>
  </cac:Country>
</cac:Address>
```

**Structure 15** — 14 instances

```xml
<cac:Address>
  <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
  <cbc:CityName>Nurnberg</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 16** — 1 instance

```xml
<cac:Address>
  <cbc:Region>Bavaria</cbc:Region>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    <cbc:Name>Germany</cbc:Name>
  </cac:Country>
</cac:Address>
```

**Structure 17** — 18 instances

```xml
<cac:RegistrationAddress>
  <cbc:CityName>Stockholm</cbc:CityName>
  <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
  <cac:Country>
    <cbc:IdentificationCode>SE</cbc:IdentificationCode>
  </cac:Country>
</cac:RegistrationAddress>
```

**Structure 18** — 17 instances

```xml
<cac:PostalAddress>
  <cbc:StreetName>Tiilitie 5</cbc:StreetName>
  <cbc:CityName>Espoo</cbc:CityName>
  <cbc:PostalZone>02340</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>FI</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 19** — 5 instances

```xml
<cac:PostalAddress>
  <cbc:StreetName>Trangravsvej</cbc:StreetName>
  <cbc:BuildingNumber>12</cbc:BuildingNumber>
  <cbc:CityName>Copenhagen</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 20** — 9 instances

```xml
<cac:Address>
  <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
  <cbc:CityName>Nurnberg</cbc:CityName>
  <cbc:PostalZone>28400</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 21** — 9 instances

```xml
<cac:Address>
  <cbc:ID>4568763527610</cbc:ID>
  <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
  <cbc:CityName>Bremen</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 22** — 1 instance

```xml
<cac:Address>
  <cbc:StreetName>StreetName Example</cbc:StreetName>
  <cbc:CityName>El Dorado</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>PA</cbc:IdentificationCode>
    <cbc:Name>Panama</cbc:Name>
  </cac:Country>
</cac:Address>
```

**Structure 23** — 9 instances

```xml
<cac:PostalAddress>
  <cbc:Postbox>99043</cbc:Postbox>
  <cbc:CityName>Boston</cbc:CityName>
  <cbc:PostalZone>02210</cbc:PostalZone>
  <cbc:CountrySubentityCode>MA</cbc:CountrySubentityCode>
  <cac:Country>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 24** — 3 instances

```xml
<cac:PostalAddress>
  <cbc:Postbox>456</cbc:Postbox>
  <cbc:StreetName>Jordbærstien 2</cbc:StreetName>
  <cbc:CityName>Hamar</cbc:CityName>
  <cbc:PostalZone>2321</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 25** — 20 instances

```xml
<cac:PostalAddress>
  <cbc:StreetName>Slotsholmsgade</cbc:StreetName>
  <cbc:BuildingNumber>1</cbc:BuildingNumber>
  <cbc:CityName>København K</cbc:CityName>
  <cbc:PostalZone>1216</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 26** — 1 instance

```xml
<cac:PostalAddress>
  <cbc:AddressFormatCode>Structured</cbc:AddressFormatCode>
  <cbc:StreetName>Korsbygade 34</cbc:StreetName>
  <cbc:CityName>Aalborg</cbc:CityName>
  <cbc:PostalZone>9000</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 27** — 5 instances

```xml
<cac:PostalAddress>
  <cbc:StreetName>Højdevej 18</cbc:StreetName>
  <cbc:CityName>Grenå</cbc:CityName>
  <cbc:PostalZone>8500</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 28** — 1 instance

```xml
<cac:PostalAddress>
  <cbc:StreetName>StreetName Example</cbc:StreetName>
  <cbc:AdditionalStreetName>AdditionalStreet Example</cbc:AdditionalStreetName>
  <cbc:CityName>El Dorado</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>PA</cbc:IdentificationCode>
    <cbc:Name>Panama</cbc:Name>
  </cac:Country>
</cac:PostalAddress>
```

**Structure 29** — 2 instances

```xml
<cac:Address>
  <cbc:Floor>4</cbc:Floor>
  <cbc:StreetName>CALLE SERPIS</cbc:StreetName>
  <cbc:CityName>VALENCIA</cbc:CityName>
  <cbc:PostalZone>460019</cbc:PostalZone>
  <cac:AddressLine>
    <cbc:Line>Calle Serpis 64</cbc:Line>
  </cac:AddressLine>
</cac:Address>
```

**Structure 30** — 5 instances

```xml
<cac:Address>
  <cbc:ID>DEHAM</cbc:ID>
  <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
  <cbc:CityName>Hamburg</cbc:CityName>
  <cbc:PostalZone>29400</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 31** — 8 instances

```xml
<cac:Address>
  <cbc:StreetName>Giessereistrasse</cbc:StreetName>
  <cbc:BuildingNumber>18</cbc:BuildingNumber>
  <cbc:CityName>Zürich</cbc:CityName>
  <cbc:PostalZone>CH-8005</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 32** — 14 instances

```xml
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
```

**Structure 33** — 4 instances

```xml
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
```

**Structure 34** — 1 instance

```xml
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
```

**Structure 35** — 1 instance

```xml
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
```

**Structure 36** — 2 instances

```xml
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
```

**Structure 37** — 1 instance

```xml
<cac:DeliveryAddress>
  <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
  <cbc:BuildingNumber>403</cbc:BuildingNumber>
  <cbc:CityName>Bologna</cbc:CityName>
  <cbc:PostalZone>40129</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    <cbc:Name>Italy</cbc:Name>
  </cac:Country>
</cac:DeliveryAddress>
```

**Structure 38** — 5 instances

```xml
<cac:Address>
  <cbc:StreetName>Via Rizzoli</cbc:StreetName>
  <cbc:BuildingNumber>208</cbc:BuildingNumber>
  <cbc:CityName>Bologna</cbc:CityName>
  <cbc:PostalZone>40121</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    <cbc:Name>Italy</cbc:Name>
  </cac:Country>
</cac:Address>
```

**Structure 39** — 1 instance

```xml
<cac:DespatchAddress>
  <cbc:StreetName>Via Emilia</cbc:StreetName>
  <cbc:BuildingNumber>1</cbc:BuildingNumber>
  <cbc:CityName>Modena</cbc:CityName>
  <cbc:PostalZone>41121</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    <cbc:Name>Italy</cbc:Name>
  </cac:Country>
</cac:DespatchAddress>
```

**Structure 40** — 2 instances

```xml
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
```

**Structure 41** — 1 instance

```xml
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
```

**Structure 42** — 1 instance

```xml
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
```

**Structure 43** — 1 instance

```xml
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
```

**Structure 44** — 2 instances

```xml
<cac:Address>
  <cbc:StreetName>Deliverystreet</cbc:StreetName>
  <cbc:AdditionalStreetName>Side door</cbc:AdditionalStreetName>
  <cbc:BuildingNumber>12</cbc:BuildingNumber>
  <cbc:CityName>DeliveryCity</cbc:CityName>
  <cbc:PostalZone>523427</cbc:PostalZone>
  <cbc:CountrySubentity>RegionC</cbc:CountrySubentity>
  <cac:Country>
    <cbc:IdentificationCode>BE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

**Structure 45** — 1 instance

```xml
<cac:Address>
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
</cac:Address>
```

**Structure 46** — 16 instances

```xml
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
```

**Structure 47** — 2 instances

```xml
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
```

**Structure 48** — 4 instances

```xml
<cac:DespatchAddress>
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
</cac:DespatchAddress>
```

**Structure 49** — 4 instances

```xml
<cac:OriginAddress>
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
</cac:OriginAddress>
```

**Structure 50** — 242 instances

```xml
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
```

**Structure 51** — 1 instance

```xml
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
```

**Structure 52** — 45 instances

```xml
<cac:DeliveryAddress>
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
</cac:DeliveryAddress>
```

**Structure 53** — 66 instances

```xml
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
```

**Structure 54** — 7 instances

```xml
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
```

**Structure 55** — 11 instances

```xml
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
```

**Structure 56** — 2 instances

```xml
<cac:DeliveryAddress>
  <cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
  <cbc:StreetName>Bernstorffsvej</cbc:StreetName>
  <cbc:BuildingNumber>161</cbc:BuildingNumber>
  <cbc:CityName>Charlottenlund</cbc:CityName>
  <cbc:PostalZone>2920</cbc:PostalZone>
  <cac:AddressLine>
    <cbc:Line>IT-afdelingen</cbc:Line>
  </cac:AddressLine>
  <cac:AddressLine>
    <cbc:Line>1. sal</cbc:Line>
  </cac:AddressLine>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:DeliveryAddress>
```

**Structure 57** — 2 instances

```xml
<cac:Address>
  <cbc:ID>1234567890123</cbc:ID>
  <cbc:Postbox>123</cbc:Postbox>
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
</cac:Address>
```

**Structure 58** — 1 instance

```xml
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
```

**Structure 59** — 1 instance

```xml
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
```

**Structure 60** — 2 instances

```xml
<cac:Address>
  <cbc:StreetName>Hansestadt Bremisches</cbc:StreetName>
  <cbc:CityName>Bremen</cbc:CityName>
  <cac:AddressLine>
    <cbc:Line>Ueberseetor 2</cbc:Line>
  </cac:AddressLine>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    <cbc:Name>Germany</cbc:Name>
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
```

[↑ Back to contents](#contents)

### `AirTransportType`

**Used as:** `cac:AirTransport`

_6 instances across 1 element, with 1 unique structure_

**Structure 1** — 6 instances

```xml
<cac:AirTransport>
  <cbc:AircraftID>A-127763-747</cbc:AircraftID>
</cac:AirTransport>
```

[↑ Back to contents](#contents)

### `AllowanceChargeType`

**Used as:** `cac:AllowanceCharge` · `cac:FreightAllowanceCharge`

_85 instances across 2 elements, with 9 unique structures_

**Structure 1** — 1 instance

```xml
<cac:FreightAllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:Amount>0.00</cbc:Amount>
</cac:FreightAllowanceCharge>
```

**Structure 2** — 20 instances

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Packing cost</cbc:AllowanceChargeReason>
  <cbc:Amount>100</cbc:Amount>
</cac:AllowanceCharge>
```

**Structure 3** — 23 instances

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReasonCode>17</cbc:AllowanceChargeReasonCode>
  <cbc:MultiplierFactorNumeric>0.10</cbc:MultiplierFactorNumeric>
  <cbc:Amount>10.00</cbc:Amount>
</cac:AllowanceCharge>
```

**Structure 4** — 2 instances

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Paid 10,000 loyalty points = €5</cbc:AllowanceChargeReason>
  <cbc:Amount>5.00</cbc:Amount>
  <cbc:TaxInclusiveAmount>5.00</cbc:TaxInclusiveAmount>
</cac:AllowanceCharge>
```

**Structure 5** — 12 instances

```xml
<cac:FreightAllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
  <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
  <cbc:Amount>254.00</cbc:Amount>
</cac:FreightAllowanceCharge>
```

**Structure 6** — 12 instances

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
  <cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
  <cbc:Amount>225</cbc:Amount>
  <cbc:BaseAmount>1500</cbc:BaseAmount>
</cac:AllowanceCharge>
```

**Structure 7** — 12 instances

```xml
<cac:FreightAllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
  <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
  <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
  <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
  <cbc:Amount>12.70</cbc:Amount>
  <cbc:BaseAmount>254.00</cbc:BaseAmount>
</cac:FreightAllowanceCharge>
```

**Structure 8** — 1 instance

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Donation to the Red Cross</cbc:AllowanceChargeReason>
  <cbc:Amount>1.00</cbc:Amount>
  <cbc:TaxInclusiveAmount>1.00</cbc:TaxInclusiveAmount>
  <cac:TaxCategory>
    <cbc:ID>O</cbc:ID>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:AllowanceCharge>
```

**Structure 9** — 2 instances

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Remove previously granted discount</cbc:AllowanceChargeReason>
  <cbc:Amount>5.00</cbc:Amount>
  <cac:TaxCategory>
    <cbc:ID>S</cbc:ID>
    <cbc:Percent>21.00</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:AllowanceCharge>
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

### `AttestationLineType`

**Used as:** `cac:AttestationLine`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:AttestationLine>
  <cbc:Description>fish meal or fish oil from countries other than Denmark from establishments approved the AQSIQ. The fish meal or fish oil
						in question ____________________________________________(indicate name of product) is approved for export from said
						country to China and were only produced at ____________________________________________(indicate name and address
						of the producer as identified in the approval of AQSIQ) and were only exported to Denmark from 
						____________________________________________ (indicate name and address of the producer/exporter as identified in the
						import permit)</cbc:Description>
  <cbc:Description>fiskemel eller fiskeolie fra andre lande, fra virksomheder, der er godkendt af AQSIQ. Det pågældende produkt
						(fiskemel eller fiskeolie)____________________________________________ (angiv produktets navn) er godkendt til eksport fra
						det pågældende land til Kina og er udelukkende forarbejdet på ____________________________________________(angiv navn
						og adresse på producenten/eksportøren, således som denne er angivet i godkendelsen fra AQSIQ) og er udelukkende eksporteret til
						Danmark fra ____________________________________________ (angiv navn og adresse på eksportøren, således som denne er
						angivet i godkendelsen fra AQSIQ )</cbc:Description>
  <cbc:Description>经中国国家质量监督检验检疫总局批准的，丹麦以外其他国家的企业生产的鱼粉或鱼
						油。该鱼粉或鱼油____________________________________________（标明产品名称）已被准予从上述国家向中国出口
						且仅在____________________________________________（标明AQSIQ注册批准的生产商名称与地址）生产并仅从
						____________________________________________（标明进口许可中认定的生产商/出口商名称与地址）向丹麦出口。</cbc:Description>
</cac:AttestationLine>
```

[↑ Back to contents](#contents)

### `AttestationType`

**Used as:** `cac:Attestation`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:Attestation>
  <cbc:ID>3</cbc:ID>
  <cbc:AcceptanceIndicator>false</cbc:AcceptanceIndicator>
  <cac:IssuerParty>
    <cac:PartyIdentification>
      <cbc:ID>1</cbc:ID>
    </cac:PartyIdentification>
  </cac:IssuerParty>
  <cac:AttestationLine>
    <cbc:Description>fish meal or fish oil from countries other than Denmark from establishments approved the AQSIQ. The fish meal or fish oil
						in question ____________________________________________(indicate name of product) is approved for export from said
						country to China and were only produced at ____________________________________________(indicate name and address
						of the producer as identified in the approval of AQSIQ) and were only exported to Denmark from 
						____________________________________________ (indicate name and address of the producer/exporter as identified in the
						import permit)</cbc:Description>
    <cbc:Description>fiskemel eller fiskeolie fra andre lande, fra virksomheder, der er godkendt af AQSIQ. Det pågældende produkt
						(fiskemel eller fiskeolie)____________________________________________ (angiv produktets navn) er godkendt til eksport fra
						det pågældende land til Kina og er udelukkende forarbejdet på ____________________________________________(angiv navn
						og adresse på producenten/eksportøren, således som denne er angivet i godkendelsen fra AQSIQ) og er udelukkende eksporteret til
						Danmark fra ____________________________________________ (angiv navn og adresse på eksportøren, således som denne er
						angivet i godkendelsen fra AQSIQ )</cbc:Description>
    <cbc:Description>经中国国家质量监督检验检疫总局批准的，丹麦以外其他国家的企业生产的鱼粉或鱼
						油。该鱼粉或鱼油____________________________________________（标明产品名称）已被准予从上述国家向中国出口
						且仅在____________________________________________（标明AQSIQ注册批准的生产商名称与地址）生产并仅从
						____________________________________________（标明进口许可中认定的生产商/出口商名称与地址）向丹麦出口。</cbc:Description>
  </cac:AttestationLine>
</cac:Attestation>
```

[↑ Back to contents](#contents)

### `BillingReferenceType`

**Used as:** `cac:BillingReference`

_17 instances across 1 element, with 4 unique structures_

**Structure 1** — 1 instance

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID>TOSL108</cbc:ID>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

**Structure 2** — 1 instance

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID>INV000123</cbc:ID>
    <cbc:IssueDate>2025-07-01</cbc:IssueDate>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

**Structure 3** — 10 instances

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID>A00095678</cbc:ID>
    <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
    <cbc:IssueDate>2005-06-21</cbc:IssueDate>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

**Structure 4** — 5 instances

```xml
<cac:BillingReference>
  <cac:CreditNoteDocumentReference>
    <cbc:ID>CN758494</cbc:ID>
    <cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
    <cbc:IssueDate>2005-06-25</cbc:IssueDate>
  </cac:CreditNoteDocumentReference>
</cac:BillingReference>
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

### `CashRegisterType`

**Used as:** `cac:CashRegister`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:CashRegister>
  <cbc:ID>7</cbc:ID>
  <cbc:SerialNumberID>7f49b2b8-9e75-11ed-a8fc-0242ac120002</cbc:SerialNumberID>
</cac:CashRegister>
```

[↑ Back to contents](#contents)

### `CommodityClassificationType`

**Used as:** `cac:CommodityClassification`

_75 instances across 1 element, with 5 unique structures_

**Structure 1** — 62 instances

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

**Structure 2** — 2 instances

```xml
<cac:CommodityClassification>
  <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
</cac:CommodityClassification>
```

**Structure 3** — 6 instances

```xml
<cac:CommodityClassification>
  <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
</cac:CommodityClassification>
```

**Structure 4** — 3 instances

```xml
<cac:CommodityClassification>
  <cbc:CommodityCode>19011000</cbc:CommodityCode>
</cac:CommodityClassification>
```

**Structure 5** — 2 instances

```xml
<cac:CommodityClassification>
  <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
  <cbc:CommodityCode>8</cbc:CommodityCode>
</cac:CommodityClassification>
```

[↑ Back to contents](#contents)

### `ConsignmentType`

**Used as:** `cac:Consignment` · `cac:ReferencedConsignment`

_38 instances across 2 elements, with 16 unique structures_

**Structure 1** — 13 instances

```xml
<cac:Consignment>
  <cbc:ID>1</cbc:ID>
</cac:Consignment>
```

**Structure 2** — 2 instances

```xml
<cac:Consignment>
  <cbc:ID>XYZ987</cbc:ID>
  <cbc:SummaryDescription>Electronic components</cbc:SummaryDescription>
</cac:Consignment>
```

**Structure 3** — 2 instances

```xml
<cac:Consignment>
  <cbc:ID>C1</cbc:ID>
  <cbc:ContainerizedIndicator>0</cbc:ContainerizedIndicator>
  <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
  <cbc:TotalPackagesQuantity>1</cbc:TotalPackagesQuantity>
  <cac:CustomsDeclaration>
    <cbc:ID>10158209175014500</cbc:ID>
  </cac:CustomsDeclaration>
</cac:Consignment>
```

**Structure 4** — 2 instances

```xml
<cac:Consignment>
  <cbc:ID>C1</cbc:ID>
  <cbc:ContainerizedIndicator>true</cbc:ContainerizedIndicator>
  <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
  <cbc:TotalPackagesQuantity>5</cbc:TotalPackagesQuantity>
  <cac:TransportHandlingUnit>
    <cbc:ID>ABCD123456-7</cbc:ID>
  </cac:TransportHandlingUnit>
</cac:Consignment>
```

**Structure 5** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>CON_1</cbc:ID>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_1</cbc:ID>
    <cac:TransportEquipment>
      <cbc:ID>CON_TE_1</cbc:ID>
    </cac:TransportEquipment>
    <cac:Status>
      <cbc:ConditionCode>4</cbc:ConditionCode>
      <cbc:StatusReasonCode>23</cbc:StatusReasonCode>
      <cbc:StatusReason>Reefer container lost power - cargo of fish destroyed</cbc:StatusReason>
    </cac:Status>
  </cac:TransportHandlingUnit>
</cac:Consignment>
```

**Structure 6** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>1</cbc:ID>
  <cbc:TotalInvoiceAmount>44250.00</cbc:TotalInvoiceAmount>
  <cbc:GrossWeightMeasure>230.80</cbc:GrossWeightMeasure>
  <cbc:Information>Professional equipment</cbc:Information>
  <cbc:TotalGoodsItemQuantity>23</cbc:TotalGoodsItemQuantity>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
  <cac:TransitCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:TransitCountry>
  <cac:FirstArrivalPortLocation>
    <cbc:Name>Padborg</cbc:Name>
  </cac:FirstArrivalPortLocation>
  <cac:LastExitPortLocation>
    <cbc:Name>Bietingen</cbc:Name>
  </cac:LastExitPortLocation>
</cac:Consignment>
```

**Structure 7** — 2 instances

```xml
<cac:ReferencedConsignment>
  <cbc:ID>CON_1</cbc:ID>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_1</cbc:ID>
    <cac:TransportEquipment>
      <cbc:ID>CON_1</cbc:ID>
      <cac:ContainedInTransportEquipment>
        <cbc:ID>NEC_TE_1</cbc:ID>
        <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
        <cbc:TraceID>12345678914542</cbc:TraceID>
      </cac:ContainedInTransportEquipment>
      <cac:Package>
        <cbc:ID>CON_1</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
      </cac:Package>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_2</cbc:ID>
    <cac:TransportEquipment>
      <cbc:ID>CON_2</cbc:ID>
      <cac:ContainedInTransportEquipment>
        <cbc:ID>NEC_TE_2</cbc:ID>
        <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
        <cbc:TraceID>12345678914543</cbc:TraceID>
      </cac:ContainedInTransportEquipment>
      <cac:Package>
        <cbc:ID>CON_2</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
      </cac:Package>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
</cac:ReferencedConsignment>
```

**Structure 8** — 1 instance

```xml
<cac:ReferencedConsignment>
  <cbc:ID>EXT_1</cbc:ID>
  <cac:TransportHandlingUnit>
    <cbc:ID>EXT_THU_1</cbc:ID>
    <cac:TransportEquipment>
      <cbc:ID>CON_1</cbc:ID>
      <cac:ContainedInTransportEquipment>
        <cbc:ID>EXT_TE_1</cbc:ID>
        <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
        <cbc:TraceID>12345678914111</cbc:TraceID>
      </cac:ContainedInTransportEquipment>
      <cac:Package>
        <cbc:ID>CON_1</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
      </cac:Package>
    </cac:TransportEquipment>
    <cac:TransportMeans>
      <cac:RoadTransport>
        <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
      </cac:RoadTransport>
    </cac:TransportMeans>
  </cac:TransportHandlingUnit>
  <cac:TransportHandlingUnit>
    <cbc:ID>EXT_THU_2</cbc:ID>
    <cac:TransportEquipment>
      <cbc:ID>CON_2</cbc:ID>
      <cac:ContainedInTransportEquipment>
        <cbc:ID>EXT_TE_2</cbc:ID>
        <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
        <cbc:TraceID>12345678914112</cbc:TraceID>
      </cac:ContainedInTransportEquipment>
      <cac:Package>
        <cbc:ID>CON_2</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
      </cac:Package>
    </cac:TransportEquipment>
    <cac:TransportMeans>
      <cac:RoadTransport>
        <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
      </cac:RoadTransport>
    </cac:TransportMeans>
  </cac:TransportHandlingUnit>
</cac:ReferencedConsignment>
```

**Structure 9** — 4 instances

```xml
<cac:Consignment>
  <cbc:ID>CONS-0001</cbc:ID>
  <cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
  <cbc:TariffCode>15219000</cbc:TariffCode>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginalDepartureCountry>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
  <cac:DeliveryTerms>
    <cbc:ID>FOB Destination</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID>GBBRS</cbc:ID>
      <cbc:Description>Bristol</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cbc:Amount>254.00</cbc:Amount>
  </cac:FreightAllowanceCharge>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
    <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
    <cbc:Amount>12.70</cbc:Amount>
    <cbc:BaseAmount>254.00</cbc:BaseAmount>
  </cac:FreightAllowanceCharge>
</cac:Consignment>
```

**Structure 10** — 2 instances

```xml
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
```

**Structure 11** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>2005US12345678998765432112345678</cbc:ID>
  <cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
  <cbc:TariffCode>15219000</cbc:TariffCode>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginalDepartureCountry>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
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
  <cac:OriginalDespatchTransportationService>
    <cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
  </cac:OriginalDespatchTransportationService>
  <cac:FinalDeliveryTransportationService>
    <cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
  </cac:FinalDeliveryTransportationService>
  <cac:DeliveryTerms>
    <cbc:ID>FOB Destination</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID>GBBRS</cbc:ID>
      <cbc:Description>Bristol</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:PaymentTerms>
    <cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
  </cac:PaymentTerms>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cbc:Amount>254.00</cbc:Amount>
  </cac:FreightAllowanceCharge>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
    <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
    <cbc:Amount>12.70</cbc:Amount>
    <cbc:BaseAmount>254.00</cbc:BaseAmount>
  </cac:FreightAllowanceCharge>
</cac:Consignment>
```

**Structure 12** — 3 instances

```xml
<cac:Consignment>
  <cbc:ID>2005US12345678998765432112345678</cbc:ID>
  <cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
  <cbc:TariffCode>15219000</cbc:TariffCode>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginalDepartureCountry>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
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
  <cac:OriginalDespatchTransportationService>
    <cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
  </cac:OriginalDespatchTransportationService>
  <cac:FinalDeliveryTransportationService>
    <cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
  </cac:FinalDeliveryTransportationService>
  <cac:DeliveryTerms>
    <cbc:ID>FOB Destination</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID>GBBRS</cbc:ID>
      <cbc:Description>Bristol</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:PaymentTerms>
    <cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
  </cac:PaymentTerms>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cbc:Amount>254.00</cbc:Amount>
  </cac:FreightAllowanceCharge>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
    <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
    <cbc:Amount>12.70</cbc:Amount>
    <cbc:BaseAmount>254.00</cbc:BaseAmount>
  </cac:FreightAllowanceCharge>
</cac:Consignment>
```

**Structure 13** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>CON_1</cbc:ID>
  <cbc:GrossWeightMeasure>50000</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>3000</cbc:NetWeightMeasure>
  <cbc:GrossVolumeMeasure>78</cbc:GrossVolumeMeasure>
  <cbc:LoadingLengthMeasure>12</cbc:LoadingLengthMeasure>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:TotalTransportHandlingUnitQuantity>2</cbc:TotalTransportHandlingUnitQuantity>
  <cac:ConsolidatedShipment>
    <cbc:ID>GSIN_1</cbc:ID>
  </cac:ConsolidatedShipment>
  <cac:ConsolidatedShipment>
    <cbc:ID>GSIN_2</cbc:ID>
  </cac:ConsolidatedShipment>
  <cac:RequestedPickupTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:ID>DEHAM</cbc:ID>
        <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
        <cbc:CityName>Hamburg</cbc:CityName>
        <cbc:PostalZone>29400</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:RequestedPickupTransportEvent>
  <cac:RequestedDeliveryTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cbc:PostalZone>28400</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-06</cbc:StartDate>
      <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-06</cbc:EndDate>
      <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:RequestedDeliveryTransportEvent>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>CN</cbc:IdentificationCode>
  </cac:OriginalDepartureCountry>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_1</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
    <cbc:ShippingMarks>General Cargo</cbc:ShippingMarks>
    <cac:TransportEquipment>
      <cbc:ID>CON_TE_1</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
      <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
      <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
      <cbc:Description>SomeDescription</cbc:Description>
      <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
      <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
      <cbc:PowerIndicator>false</cbc:PowerIndicator>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure>6.1</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure>2.6</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure>2.44</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:ID>CON_P_1</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
        <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
        <cac:GoodsItem>
          <cac:Item>
            <cac:CommodityClassification>
              <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
            </cac:CommodityClassification>
          </cac:Item>
        </cac:GoodsItem>
      </cac:Package>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_2</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
    <cbc:ShippingMarks>General Cargo</cbc:ShippingMarks>
    <cac:TransportEquipment>
      <cbc:ID>CON_TE_2</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
      <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
      <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
      <cbc:Description>SomeDescription</cbc:Description>
      <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
      <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
      <cbc:PowerIndicator>false</cbc:PowerIndicator>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure>6.1</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure>2.6</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure>2.44</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:ID>CON_P_2</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
        <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
        <cac:GoodsItem>
          <cac:Item>
            <cac:CommodityClassification>
              <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
            </cac:CommodityClassification>
          </cac:Item>
        </cac:GoodsItem>
      </cac:Package>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
</cac:Consignment>
```

**Structure 14** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>7365566156191234567</cbc:ID>
  <cbc:GrossWeightMeasure>600</cbc:GrossWeightMeasure>
  <cbc:TotalGoodsItemQuantity>1500</cbc:TotalGoodsItemQuantity>
  <cbc:TotalTransportHandlingUnitQuantity>2</cbc:TotalTransportHandlingUnitQuantity>
  <cac:PlannedPickupTransportEvent>
    <cac:Location>
      <cbc:ID>MAPTM</cbc:ID>
      <cac:Address>
        <cbc:CityName>Tanger</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>MA</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
  </cac:PlannedPickupTransportEvent>
  <cac:PlannedDeliveryTransportEvent>
    <cac:Location>
      <cbc:ID>ITGOA</cbc:ID>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
  </cac:PlannedDeliveryTransportEvent>
  <cac:ConsigneeParty>
    <cac:PartyName>
      <cbc:Name>Consignee W</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Consignee W Street</cbc:StreetName>
      <cbc:CityName>Munich</cbc:CityName>
      <cbc:PostalZone>231</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ConsigneeParty>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>MA</cbc:IdentificationCode>
  </cac:OriginalDepartureCountry>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
  <cac:TransitCountry>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  </cac:TransitCountry>
  <cac:TransitCountry>
    <cbc:IdentificationCode>AT</cbc:IdentificationCode>
  </cac:TransitCountry>
  <cac:MainCarriageShipmentStage>
    <cbc:ShipmentStageTypeCode>1</cbc:ShipmentStageTypeCode>
    <cbc:TransportModeCode>1</cbc:TransportModeCode>
    <cac:TransportMeans>
      <cbc:JourneyID>00344</cbc:JourneyID>
      <cbc:RegistrationNationalityID>IT</cbc:RegistrationNationalityID>
      <cac:MaritimeTransport>
        <cbc:VesselID>3852664</cbc:VesselID>
        <cbc:VesselName>Vessel Name</cbc:VesselName>
      </cac:MaritimeTransport>
    </cac:TransportMeans>
    <cac:EstimatedArrivalTransportEvent>
      <cbc:OccurrenceDate>2013-05-25</cbc:OccurrenceDate>
      <cbc:OccurrenceTime>18:00:00+01:00</cbc:OccurrenceTime>
      <cac:Location>
        <cbc:ID>ITGOA</cbc:ID>
        <cbc:LocationTypeCode>24</cbc:LocationTypeCode>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode>IT</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
    </cac:EstimatedArrivalTransportEvent>
  </cac:MainCarriageShipmentStage>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_1</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:ShippingMarks>Agricultural products</cbc:ShippingMarks>
    <cac:TransportEquipment>
      <cbc:ID>BFCU4040001</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
      <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
      <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
      <cbc:Description>Should have a temperature between 2-4 degrees celcius</cbc:Description>
      <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
      <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
      <cbc:PowerIndicator>true</cbc:PowerIndicator>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure>6.1</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure>2.6</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure>2.44</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:GoodsItem>
        <cac:Item>
          <cac:CommodityClassification>
            <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
            <cbc:CommodityCode>8</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_2</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:ShippingMarks>Agricultural products</cbc:ShippingMarks>
    <cac:TransportEquipment>
      <cbc:ID>BFCU4040002</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
      <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
      <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
      <cbc:Description>Should have a temperature between 2-4 degrees celcius</cbc:Description>
      <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
      <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
      <cbc:PowerIndicator>true</cbc:PowerIndicator>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure>6.1</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure>2.6</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure>2.44</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:GoodsItem>
        <cac:Item>
          <cac:CommodityClassification>
            <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
            <cbc:CommodityCode>8</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
  <cac:FirstArrivalPortLocation>
    <cbc:ID>ITGOA</cbc:ID>
    <cbc:LocationTypeCode>41</cbc:LocationTypeCode>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:FirstArrivalPortLocation>
  <cac:OfficeOfEntryLocation>
    <cbc:ID>DE000396</cbc:ID>
    <cbc:LocationTypeCode>41</cbc:LocationTypeCode>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:OfficeOfEntryLocation>
</cac:Consignment>
```

**Structure 15** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>2076084807</cbc:ID>
  <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
  <cbc:SequenceID>203</cbc:SequenceID>
  <cbc:DeliveryInstructions>El Dorado</cbc:DeliveryInstructions>
  <cac:RequestedPickupTransportEvent>
    <cac:Contact>
      <cbc:Name>ExampleName</cbc:Name>
    </cac:Contact>
    <cac:Location>
      <cbc:ID>M165</cbc:ID>
      <cac:Address>
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
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2020-06-02</cbc:StartDate>
      <cbc:EndDate>2020-06-02</cbc:EndDate>
    </cac:Period>
  </cac:RequestedPickupTransportEvent>
  <cac:RequestedDeliveryTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:StreetName>StreetName Example</cbc:StreetName>
        <cbc:CityName>El Dorado</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>PA</cbc:IdentificationCode>
          <cbc:Name>Panama</cbc:Name>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2020-07-01</cbc:StartDate>
      <cbc:EndDate>2020-07-01</cbc:EndDate>
    </cac:Period>
  </cac:RequestedDeliveryTransportEvent>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:OriginalDepartureCountry>
  <cac:DeliveryTerms>
    <cbc:ID>CIP</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Name>Balboa Port</cbc:Name>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:Amount>0.00</cbc:Amount>
  </cac:FreightAllowanceCharge>
  <cac:MainCarriageShipmentStage>
    <cbc:TransportModeCode>1</cbc:TransportModeCode>
    <cac:LoadingPortLocation>
      <cbc:ID>Aarhus</cbc:ID>
    </cac:LoadingPortLocation>
    <cac:UnloadingPortLocation>
      <cbc:ID>Balboa Port</cbc:ID>
    </cac:UnloadingPortLocation>
  </cac:MainCarriageShipmentStage>
  <cac:TransportHandlingUnit>
    <cbc:ID>USRM3656679</cbc:ID>
    <cbc:TotalPackageQuantity>1</cbc:TotalPackageQuantity>
    <cac:TransportEquipment>
      <cac:TransportEquipmentSeal>
        <cbc:ID>7654321</cbc:ID>
      </cac:TransportEquipmentSeal>
    </cac:TransportEquipment>
    <cac:MaximumTemperature>
      <cbc:AttributeID>TC</cbc:AttributeID>
      <cbc:Measure>3.00</cbc:Measure>
      <cbc:Description>Chilled</cbc:Description>
    </cac:MaximumTemperature>
    <cac:Package>
      <cbc:ID>2076084807</cbc:ID>
      <cbc:Quantity>1</cbc:Quantity>
      <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
      <cac:GoodsItem>
        <cbc:ID>000010</cbc:ID>
        <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
        <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
        <cbc:Quantity>63.000</cbc:Quantity>
        <cac:Item>
          <cbc:Description>ItemExample</cbc:Description>
          <cbc:PackQuantity>63</cbc:PackQuantity>
          <cbc:Name>Dairy Products</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>123456</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode>DK</cbc:IdentificationCode>
            <cbc:Name>Denmark</cbc:Name>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:CommodityCode>19011000</cbc:CommodityCode>
          </cac:CommodityClassification>
          <cac:AdditionalItemProperty>
            <cbc:Name>AnimalSpecies</cbc:Name>
            <cbc:Value>Bovine</cbc:Value>
          </cac:AdditionalItemProperty>
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
          <cac:ItemInstance>
            <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
            <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
            <cac:AdditionalItemProperty>
              <cbc:Name>LineNetWeight</cbc:Name>
              <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
            </cac:AdditionalItemProperty>
            <cac:AdditionalItemProperty>
              <cbc:Name>LineGrossWeight</cbc:Name>
              <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
            </cac:AdditionalItemProperty>
            <cac:AdditionalItemProperty>
              <cbc:Name>Quantity</cbc:Name>
              <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
            </cac:AdditionalItemProperty>
            <cac:LotIdentification>
              <cbc:LotNumberID>9390000757</cbc:LotNumberID>
            </cac:LotIdentification>
          </cac:ItemInstance>
          <cac:Dimension>
            <cbc:AttributeID>NetWeight</cbc:AttributeID>
            <cbc:Measure>9.6</cbc:Measure>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
            <cbc:Measure>604.8</cbc:Measure>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID>GrossWeight</cbc:AttributeID>
            <cbc:Measure>12.288</cbc:Measure>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
            <cbc:Measure>774.144</cbc:Measure>
          </cac:Dimension>
        </cac:Item>
        <cac:Despatch>
          <cbc:ID>000010</cbc:ID>
        </cac:Despatch>
        <cac:MaximumTemperature>
          <cbc:AttributeID>TC</cbc:AttributeID>
          <cbc:Measure>3.00</cbc:Measure>
          <cbc:Description>Chilled</cbc:Description>
        </cac:MaximumTemperature>
      </cac:GoodsItem>
      <cac:MeasurementDimension>
        <cbc:AttributeID>GrossWeight</cbc:AttributeID>
        <cbc:Measure>774.14400</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>NetWeight</cbc:AttributeID>
        <cbc:Measure>604.80000</cbc:Measure>
      </cac:MeasurementDimension>
    </cac:Package>
  </cac:TransportHandlingUnit>
</cac:Consignment>
```

**Structure 16** — 1 instance

```xml
<cac:Consignment>
  <cbc:ID>CON_1</cbc:ID>
  <cbc:GrossWeightMeasure>50000</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>3000</cbc:NetWeightMeasure>
  <cbc:GrossVolumeMeasure>78</cbc:GrossVolumeMeasure>
  <cbc:LoadingLengthMeasure>12</cbc:LoadingLengthMeasure>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:TotalTransportHandlingUnitQuantity>2</cbc:TotalTransportHandlingUnitQuantity>
  <cac:ConsolidatedShipment>
    <cbc:ID>GSIN_1</cbc:ID>
  </cac:ConsolidatedShipment>
  <cac:ConsolidatedShipment>
    <cbc:ID>GSIN_2</cbc:ID>
  </cac:ConsolidatedShipment>
  <cac:PlannedPickupTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:ID>DEHAM</cbc:ID>
        <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
        <cbc:CityName>Hamburg</cbc:CityName>
        <cbc:PostalZone>29400</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedPickupTransportEvent>
  <cac:PlannedDeliveryTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cbc:PostalZone>28400</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-06</cbc:StartDate>
      <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-06</cbc:EndDate>
      <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDeliveryTransportEvent>
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
  <cac:OriginalDepartureCountry>
    <cbc:IdentificationCode>CN</cbc:IdentificationCode>
  </cac:OriginalDepartureCountry>
  <cac:FinalDestinationCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:FinalDestinationCountry>
  <cac:MainCarriageShipmentStage>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:ID>DEHAM</cbc:ID>
          <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
          <cbc:CityName>Hamburg</cbc:CityName>
          <cbc:PostalZone>29400</cbc:PostalZone>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-03</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-03</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cbc:PostalZone>28400</cbc:PostalZone>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-06</cbc:StartDate>
        <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-06</cbc:EndDate>
        <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:MainCarriageShipmentStage>
  <cac:PreCarriageShipmentStage>
    <cbc:TransportModeCode>1</cbc:TransportModeCode>
    <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
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
    <cac:TransportMeans>
      <cbc:JourneyID>M22</cbc:JourneyID>
      <cbc:RegistrationNationalityID>DK</cbc:RegistrationNationalityID>
      <cbc:RegistrationNationality>Denmark</cbc:RegistrationNationality>
      <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
      <cac:MaritimeTransport>
        <cbc:VesselID>SomeIMONr</cbc:VesselID>
        <cbc:VesselName>SomeVesselName</cbc:VesselName>
      </cac:MaritimeTransport>
    </cac:TransportMeans>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cbc:ID>CNSHA</cbc:ID>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-09-20</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-09-20</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cbc:ID>DEHAM</cbc:ID>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-01</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-01</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:PreCarriageShipmentStage>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_1</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
    <cbc:ShippingMarks>General Cargo</cbc:ShippingMarks>
    <cac:TransportEquipment>
      <cbc:ID>CON_TE_1</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
      <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
      <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
      <cbc:Description>SomeDescription</cbc:Description>
      <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
      <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
      <cbc:PowerIndicator>false</cbc:PowerIndicator>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure>6.1</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure>2.6</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure>2.44</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:ID>CON_P_1</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
        <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
        <cac:GoodsItem>
          <cac:Item>
            <cac:CommodityClassification>
              <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
            </cac:CommodityClassification>
          </cac:Item>
        </cac:GoodsItem>
      </cac:Package>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
  <cac:TransportHandlingUnit>
    <cbc:ID>CON_THU_2</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
    <cbc:ShippingMarks>General Cargo</cbc:ShippingMarks>
    <cac:TransportEquipment>
      <cbc:ID>CON_TE_2</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
      <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
      <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
      <cbc:Description>SomeDescription</cbc:Description>
      <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
      <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
      <cbc:PowerIndicator>false</cbc:PowerIndicator>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure>6.1</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure>2.6</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure>2.44</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:ID>CON_P_2</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
        <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
        <cac:GoodsItem>
          <cac:Item>
            <cac:CommodityClassification>
              <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
            </cac:CommodityClassification>
          </cac:Item>
        </cac:GoodsItem>
      </cac:Package>
    </cac:TransportEquipment>
  </cac:TransportHandlingUnit>
</cac:Consignment>
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

### `CountryType`

**Used as:** `cac:AgreementCountry` · `cac:Country` · `cac:DestinationCountry` · `cac:ExportCountry` · `cac:FinalDestinationCountry` · `cac:OriginCountry` · `cac:OriginalDepartureCountry` · `cac:TransitCountry`

_731 instances across 8 elements, with 11 unique structures_

**Structure 1** — 598 instances

```xml
<cac:Country>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
</cac:Country>
```

**Structure 2** — 13 instances

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:OriginalDepartureCountry>
```

**Structure 3** — 12 instances

```xml
<cac:FinalDestinationCountry>
  <cbc:IdentificationCode>GB</cbc:IdentificationCode>
</cac:FinalDestinationCountry>
```

**Structure 4** — 22 instances

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
</cac:OriginCountry>
```

**Structure 5** — 6 instances

```xml
<cac:ExportCountry>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:ExportCountry>
```

**Structure 6** — 16 instances

```xml
<cac:AgreementCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
</cac:AgreementCountry>
```

**Structure 7** — 3 instances

```xml
<cac:TransitCountry>
  <cbc:IdentificationCode>IT</cbc:IdentificationCode>
</cac:TransitCountry>
```

**Structure 8** — 45 instances

```xml
<cac:Country>
  <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  <cbc:Name>Italy</cbc:Name>
</cac:Country>
```

**Structure 9** — 10 instances

```xml
<cac:DestinationCountry>
  <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  <cbc:Name>Great Britain</cbc:Name>
</cac:DestinationCountry>
```

**Structure 10** — 1 instance

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  <cbc:Name>Denmark</cbc:Name>
</cac:OriginalDepartureCountry>
```

**Structure 11** — 5 instances

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  <cbc:Name>Denmark</cbc:Name>
</cac:OriginCountry>
```

[↑ Back to contents](#contents)

### `CreditNoteLineType`

**Used as:** `cac:CreditNoteLine`

_15 instances across 1 element, with 7 unique structures_

**Structure 1** — 2 instances

```xml
<cac:CreditNoteLine>
  <cbc:ID>4</cbc:ID>
  <cbc:CreditedQuantity>-1</cbc:CreditedQuantity>
  <cbc:LineExtensionAmount>-25</cbc:LineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>0</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Returned IBM 5150 desktop</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB010</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890127</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344322</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434565</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>E</cbc:ID>
      <cbc:Percent>0</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>25</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:CreditNoteLine>
```

**Structure 2** — 1 instance

```xml
<cac:CreditNoteLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>as agreed on phone, the invoice should have been cancelled earlier, apologies</cbc:Note>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxPointDate>2005-06-21</cbc:TaxPointDate>
  <cac:DiscrepancyResponse>
    <cbc:ReferenceID>A00095678</cbc:ReferenceID>
    <cbc:Description>invoice cancelation</cbc:Description>
  </cac:DiscrepancyResponse>
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>A00095678</cbc:ID>
      <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
      <cbc:IssueDate>2005-06-21</cbc:IssueDate>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>17.50</cbc:TaxAmount>
    <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
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
  </cac:TaxTotal>
</cac:CreditNoteLine>
```

**Structure 3** — 2 instances

```xml
<cac:CreditNoteLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Note>Cover is slightly damaged.</cbc:Note>
  <cbc:CreditedQuantity>-1</cbc:CreditedQuantity>
  <cbc:LineExtensionAmount>-3.96</cbc:LineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>-0.396</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Returned "Advanced computing" book</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB008</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890125</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434567</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>3.96</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:CreditNoteLine>
```

**Structure 4** — 2 instances

```xml
<cac:CreditNoteLine>
  <cbc:ID>5</cbc:ID>
  <cbc:CreditedQuantity>250</cbc:CreditedQuantity>
  <cbc:LineExtensionAmount>187.5</cbc:LineExtensionAmount>
  <cbc:AccountingCost>BookingCode002</cbc:AccountingCost>
  <cac:TaxTotal>
    <cbc:TaxAmount>37.5</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Network cable</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB011</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890128</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434564</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
    <cac:AdditionalItemProperty>
      <cbc:Name>Type</cbc:Name>
      <cbc:Value>Cat5</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>0.75</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:CreditNoteLine>
```

**Structure 5** — 2 instances

```xml
<cac:CreditNoteLine>
  <cbc:ID>3</cbc:ID>
  <cbc:CreditedQuantity>2</cbc:CreditedQuantity>
  <cbc:LineExtensionAmount>4.96</cbc:LineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>0.496</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>"Computing for dummies" book</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB009</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890126</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434566</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>2.48</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
      <cbc:Amount>0.275</cbc:Amount>
      <cbc:BaseAmount>2.75</cbc:BaseAmount>
    </cac:AllowanceCharge>
  </cac:Price>
</cac:CreditNoteLine>
```

**Structure 6** — 2 instances

```xml
<cac:CreditNoteLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Scratch on box</cbc:Note>
  <cbc:CreditedQuantity>1</cbc:CreditedQuantity>
  <cbc:LineExtensionAmount>1273</cbc:LineExtensionAmount>
  <cbc:AccountingCost>BookingCode001</cbc:AccountingCost>
  <cac:TaxTotal>
    <cbc:TaxAmount>254.6</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Description>Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:
				3MB. Screen 1440x900</cbc:Description>
    <cbc:Name>Labtop computer</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB007</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890124</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344321</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434568</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
    <cac:AdditionalItemProperty>
      <cbc:Name>Color</cbc:Name>
      <cbc:Value>black</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>1273</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
      <cbc:Amount>225</cbc:Amount>
      <cbc:BaseAmount>1500</cbc:BaseAmount>
    </cac:AllowanceCharge>
  </cac:Price>
</cac:CreditNoteLine>
```

**Structure 7** — 4 instances

```xml
<cac:CreditNoteLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>as agreed on phone, the invoice should have been cancelled earlier, apologies</cbc:Note>
  <cbc:CreditedQuantity>100</cbc:CreditedQuantity>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxPointDate>2005-06-21</cbc:TaxPointDate>
  <cac:DiscrepancyResponse>
    <cbc:ReferenceID>A00095678</cbc:ReferenceID>
    <cbc:Description>invoice cancelation</cbc:Description>
  </cac:DiscrepancyResponse>
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>A00095678</cbc:ID>
      <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
      <cbc:IssueDate>2005-06-21</cbc:IssueDate>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>17.50</cbc:TaxAmount>
    <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount>100.00</cbc:TaxableAmount>
      <cbc:TaxAmount>17.50</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>A</cbc:ID>
        <cac:TaxScheme>
          <cbc:ID>UK VAT</cbc:ID>
          <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:ItemInstance>
      <cac:LotIdentification>
        <cbc:LotNumberID>546378239</cbc:LotNumberID>
        <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
      </cac:LotIdentification>
    </cac:ItemInstance>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>1.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:CreditNoteLine>
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

### `DebitNoteLineType`

**Used as:** `cac:DebitNoteLine`

_7 instances across 1 element, with 6 unique structures_

**Structure 1** — 2 instances

```xml
<cac:DebitNoteLine>
  <cbc:ID>1</cbc:ID>
  <cbc:DebitedQuantity>1</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>120.00</cbc:LineExtensionAmount>
  <cac:Item>
    <cbc:Name>High-grade Widget</cbc:Name>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>120.00</cbc:PriceAmount>
  </cac:Price>
</cac:DebitNoteLine>
```

**Structure 2** — 1 instance

```xml
<cac:DebitNoteLine>
  <cbc:ID>4</cbc:ID>
  <cbc:DebitedQuantity>-1</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>-25</cbc:LineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>0</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Returned IBM 5150 desktop</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB010</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890127</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344322</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434565</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>E</cbc:ID>
      <cbc:Percent>0</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>25</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:DebitNoteLine>
```

**Structure 3** — 1 instance

```xml
<cac:DebitNoteLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Note>Cover is slightly damaged.</cbc:Note>
  <cbc:DebitedQuantity>-1</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>-3.96</cbc:LineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>-0.396</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Returned "Advanced computing" book</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB008</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890125</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434567</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>3.96</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:DebitNoteLine>
```

**Structure 4** — 1 instance

```xml
<cac:DebitNoteLine>
  <cbc:ID>5</cbc:ID>
  <cbc:DebitedQuantity>250</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>187.5</cbc:LineExtensionAmount>
  <cbc:AccountingCost>BookingCode002</cbc:AccountingCost>
  <cac:TaxTotal>
    <cbc:TaxAmount>37.5</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Network cable</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB011</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890128</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434564</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
    <cac:AdditionalItemProperty>
      <cbc:Name>Type</cbc:Name>
      <cbc:Value>Cat5</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>0.75</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:DebitNoteLine>
```

**Structure 5** — 1 instance

```xml
<cac:DebitNoteLine>
  <cbc:ID>3</cbc:ID>
  <cbc:DebitedQuantity>2</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>4.96</cbc:LineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>0.496</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>"Computing for dummies" book</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB009</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890126</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434566</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>2.48</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
      <cbc:Amount>0.275</cbc:Amount>
      <cbc:BaseAmount>2.75</cbc:BaseAmount>
    </cac:AllowanceCharge>
  </cac:Price>
</cac:DebitNoteLine>
```

**Structure 6** — 1 instance

```xml
<cac:DebitNoteLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Scratch on box</cbc:Note>
  <cbc:DebitedQuantity>1</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>1273</cbc:LineExtensionAmount>
  <cbc:AccountingCost>BookingCode001</cbc:AccountingCost>
  <cac:TaxTotal>
    <cbc:TaxAmount>254.6</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Description>Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:
				3MB. Screen 1440x900</cbc:Description>
    <cbc:Name>Labtop computer</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB007</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890124</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344321</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434568</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
    <cac:AdditionalItemProperty>
      <cbc:Name>Color</cbc:Name>
      <cbc:Value>black</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>1273</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
      <cbc:Amount>225</cbc:Amount>
      <cbc:BaseAmount>1500</cbc:BaseAmount>
    </cac:AllowanceCharge>
  </cac:Price>
</cac:DebitNoteLine>
```

[↑ Back to contents](#contents)

### `DeliveryChannelType`

**Used as:** `cac:DigitalDeliveryChannel`

_12 instances across 1 element, with 2 unique structures_

**Structure 1** — 6 instances

```xml
<cac:DigitalDeliveryChannel>
  <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
  <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
  <cac:DigitalMessageDelivery>
    <cbc:ProtocolID>AS2</cbc:ProtocolID>
    <cbc:EndpointURI>http://as2.vendor.biz</cbc:EndpointURI>
  </cac:DigitalMessageDelivery>
</cac:DigitalDeliveryChannel>
```

**Structure 2** — 6 instances

```xml
<cac:DigitalDeliveryChannel>
  <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
  <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
  <cbc:TestIndicator>true</cbc:TestIndicator>
  <cac:DigitalMessageDelivery>
    <cbc:ProtocolID>AS2</cbc:ProtocolID>
    <cbc:EndpointURI>http://as2.buyer.biz</cbc:EndpointURI>
  </cac:DigitalMessageDelivery>
</cac:DigitalDeliveryChannel>
```

[↑ Back to contents](#contents)

### `DeliveryTermsType`

**Used as:** `cac:DeliveryTerms`

_38 instances across 1 element, with 5 unique structures_

**Structure 1** — 17 instances

```xml
<cac:DeliveryTerms>
  <cbc:SpecialTerms>1% deduction for late delivery as per contract</cbc:SpecialTerms>
</cac:DeliveryTerms>
```

**Structure 2** — 5 instances

```xml
<cac:DeliveryTerms>
  <cbc:ID>CIP</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:Name>Balboa Port</cbc:Name>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

**Structure 3** — 11 instances

```xml
<cac:DeliveryTerms>
  <cbc:ID>FOB Destination</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:ID>GBFXT</cbc:ID>
    <cbc:Description>Felixstowe</cbc:Description>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

**Structure 4** — 2 instances

```xml
<cac:DeliveryTerms>
  <cbc:ID>FOT</cbc:ID>
  <cbc:SpecialTerms>CAD</cbc:SpecialTerms>
  <cac:DeliveryLocation>
    <cbc:ID>STO</cbc:ID>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

**Structure 5** — 3 instances

```xml
<cac:DeliveryTerms>
  <cbc:ID>EXW</cbc:ID>
  <cac:DeliveryLocation>
    <cac:Address>
      <cbc:CityName>Munich</cbc:CityName>
    </cac:Address>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

[↑ Back to contents](#contents)

### `DeliveryType`

**Used as:** `cac:Delivery`

_67 instances across 1 element, with 11 unique structures_

**Structure 1** — 6 instances

```xml
<cac:Delivery>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2010-02-10</cbc:StartDate>
    <cbc:EndDate>2010-02-25</cbc:EndDate>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

**Structure 2** — 2 instances

```xml
<cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID>FOB</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Name>BANGKOK</cbc:Name>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
</cac:Delivery>
```

**Structure 3** — 5 instances

```xml
<cac:Delivery>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>90</cbc:Quantity>
  <cbc:ActualDeliveryDate>2005-06-20</cbc:ActualDeliveryDate>
  <cbc:ActualDeliveryTime>11:30:00.0Z</cbc:ActualDeliveryTime>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2005-06-20</cbc:StartDate>
    <cbc:StartTime>10:30:47.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-21</cbc:EndDate>
    <cbc:EndTime>10:30:47.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

**Structure 4** — 2 instances

```xml
<cac:Delivery>
  <cac:DeliveryAddress>
    <cac:Country>
      <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    </cac:Country>
  </cac:DeliveryAddress>
  <cac:Despatch>
    <cbc:ActualDespatchDate>2013-09-15</cbc:ActualDespatchDate>
    <cbc:ActualDespatchTime>16:00:00Z</cbc:ActualDespatchTime>
    <cac:DespatchAddress>
      <cac:Country>
        <cbc:IdentificationCode>RU</cbc:IdentificationCode>
      </cac:Country>
    </cac:DespatchAddress>
  </cac:Despatch>
</cac:Delivery>
```

**Structure 5** — 2 instances

```xml
<cac:Delivery>
  <cbc:ActualDeliveryDate>2009-12-15</cbc:ActualDeliveryDate>
  <cac:DeliveryLocation>
    <cbc:ID>6754238987648</cbc:ID>
    <cac:Address>
      <cbc:StreetName>Deliverystreet</cbc:StreetName>
      <cbc:AdditionalStreetName>Side door</cbc:AdditionalStreetName>
      <cbc:BuildingNumber>12</cbc:BuildingNumber>
      <cbc:CityName>DeliveryCity</cbc:CityName>
      <cbc:PostalZone>523427</cbc:PostalZone>
      <cbc:CountrySubentity>RegionC</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>BE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:DeliveryLocation>
</cac:Delivery>
```

**Structure 6** — 18 instances

```xml
<cac:Delivery>
  <cbc:ActualDeliveryDate>2005-06-20</cbc:ActualDeliveryDate>
  <cbc:ActualDeliveryTime>11:30:00.0Z</cbc:ActualDeliveryTime>
  <cac:DeliveryAddress>
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
  </cac:DeliveryAddress>
</cac:Delivery>
```

**Structure 7** — 23 instances

```xml
<cac:Delivery>
  <cac:DeliveryAddress>
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
  </cac:DeliveryAddress>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2005-06-20</cbc:StartDate>
    <cbc:StartTime>10:30:47.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-21</cbc:EndDate>
    <cbc:EndTime>10:30:47.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

**Structure 8** — 2 instances

```xml
<cac:Delivery>
  <cac:DeliveryAddress>
    <cbc:AddressFormatCode>StructuredDK</cbc:AddressFormatCode>
    <cbc:StreetName>Bernstorffsvej</cbc:StreetName>
    <cbc:BuildingNumber>161</cbc:BuildingNumber>
    <cbc:CityName>Charlottenlund</cbc:CityName>
    <cbc:PostalZone>2920</cbc:PostalZone>
    <cac:AddressLine>
      <cbc:Line>1. sal</cbc:Line>
    </cac:AddressLine>
    <cac:AddressLine>
      <cbc:Line>IT-afdelingen</cbc:Line>
    </cac:AddressLine>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:DeliveryAddress>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2008-05-06</cbc:StartDate>
    <cbc:StartTime>09:30:47.0Z</cbc:StartTime>
    <cbc:EndDate>2008-05-10</cbc:EndDate>
    <cbc:EndTime>09:30:47.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

**Structure 9** — 1 instance

```xml
<cac:Delivery>
  <cac:DeliveryAddress>
    <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
    <cbc:BuildingNumber>403</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:DeliveryAddress>
  <cac:Despatch>
    <cac:DespatchAddress>
      <cbc:StreetName>Via Emilia</cbc:StreetName>
      <cbc:BuildingNumber>1</cbc:BuildingNumber>
      <cbc:CityName>Modena</cbc:CityName>
      <cbc:PostalZone>41121</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:DespatchAddress>
  </cac:Despatch>
</cac:Delivery>
```

**Structure 10** — 2 instances

```xml
<cac:Delivery>
  <cac:DeliveryLocation>
    <cac:Address>
      <cbc:ID>1234567890123</cbc:ID>
      <cbc:Postbox>123</cbc:Postbox>
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
    </cac:Address>
  </cac:DeliveryLocation>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2010-02-10</cbc:StartDate>
    <cbc:EndDate>2010-02-25</cbc:EndDate>
  </cac:RequestedDeliveryPeriod>
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
</cac:Delivery>
```

**Structure 11** — 4 instances

```xml
<cac:Delivery>
  <cbc:Quantity>1</cbc:Quantity>
  <cbc:LatestDeliveryDate>2005-06-30</cbc:LatestDeliveryDate>
  <cbc:LatestDeliveryTime>18:00:00.0Z</cbc:LatestDeliveryTime>
  <cbc:TrackingID>NKH7712289-03339-000128</cbc:TrackingID>
  <cac:DeliveryAddress>
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
  </cac:DeliveryAddress>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2005-06-29</cbc:StartDate>
    <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-30</cbc:EndDate>
    <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
  <cac:EstimatedDeliveryPeriod>
    <cbc:StartDate>2005-06-30</cbc:StartDate>
    <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
  </cac:EstimatedDeliveryPeriod>
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
  <cac:Despatch>
    <cbc:ActualDespatchDate>2005-06-25</cbc:ActualDespatchDate>
    <cbc:ActualDespatchTime>11:35:00.0Z</cbc:ActualDespatchTime>
    <cac:DespatchAddress>
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
    </cac:DespatchAddress>
    <cac:DespatchParty>
      <cac:PartyName>
        <cbc:Name>Consortial</cbc:Name>
      </cac:PartyName>
    </cac:DespatchParty>
    <cac:Contact>
      <cbc:Name>Mrs Bouquet</cbc:Name>
      <cbc:Telephone>+1 158 1233714</cbc:Telephone>
      <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
      <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Despatch>
</cac:Delivery>
```

[↑ Back to contents](#contents)

### `DespatchLineType`

**Used as:** `cac:DespatchLine`

_5 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:DespatchLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Mrs Green agreed to waive charge</cbc:Note>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cbc:DeliveredQuantity>90</cbc:DeliveredQuantity>
  <cbc:BackorderQuantity>10</cbc:BackorderQuantity>
  <cbc:BackorderReason>lack of stock as explained on telephone today</cbc:BackorderReason>
  <cac:OrderLineReference>
    <cbc:LineID>1</cbc:LineID>
    <cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
    <cac:OrderReference>
      <cbc:ID>AEG012345</cbc:ID>
      <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
      <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
      <cbc:IssueDate>2005-06-20</cbc:IssueDate>
    </cac:OrderReference>
  </cac:OrderLineReference>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:LotIdentification>
      <cbc:LotNumberID>546378239</cbc:LotNumberID>
      <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
    </cac:LotIdentification>
  </cac:Item>
</cac:DespatchLine>
```

**Structure 2** — 4 instances

```xml
<cac:DespatchLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Mrs Green agreed to waive charge</cbc:Note>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cbc:DeliveredQuantity>90</cbc:DeliveredQuantity>
  <cbc:BackorderQuantity>10</cbc:BackorderQuantity>
  <cbc:BackorderReason>lack of stock as explained on telephone today</cbc:BackorderReason>
  <cac:OrderLineReference>
    <cbc:LineID>1</cbc:LineID>
    <cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
    <cac:OrderReference>
      <cbc:ID>AEG012345</cbc:ID>
      <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
      <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
      <cbc:IssueDate>2005-06-20</cbc:IssueDate>
    </cac:OrderReference>
  </cac:OrderLineReference>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:ItemInstance>
      <cac:LotIdentification>
        <cbc:LotNumberID>546378239</cbc:LotNumberID>
        <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
      </cac:LotIdentification>
    </cac:ItemInstance>
  </cac:Item>
</cac:DespatchLine>
```

[↑ Back to contents](#contents)

### `DespatchType`

**Used as:** `cac:Despatch`

_12 instances across 1 element, with 4 unique structures_

**Structure 1** — 5 instances

```xml
<cac:Despatch>
  <cbc:ID>28833-2661-144</cbc:ID>
</cac:Despatch>
```

**Structure 2** — 2 instances

```xml
<cac:Despatch>
  <cbc:ActualDespatchDate>2013-09-15</cbc:ActualDespatchDate>
  <cbc:ActualDespatchTime>16:00:00Z</cbc:ActualDespatchTime>
  <cac:DespatchAddress>
    <cac:Country>
      <cbc:IdentificationCode>RU</cbc:IdentificationCode>
    </cac:Country>
  </cac:DespatchAddress>
</cac:Despatch>
```

**Structure 3** — 1 instance

```xml
<cac:Despatch>
  <cac:DespatchAddress>
    <cbc:StreetName>Via Emilia</cbc:StreetName>
    <cbc:BuildingNumber>1</cbc:BuildingNumber>
    <cbc:CityName>Modena</cbc:CityName>
    <cbc:PostalZone>41121</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:DespatchAddress>
</cac:Despatch>
```

**Structure 4** — 4 instances

```xml
<cac:Despatch>
  <cbc:ActualDespatchDate>2005-06-25</cbc:ActualDespatchDate>
  <cbc:ActualDespatchTime>11:35:00.0Z</cbc:ActualDespatchTime>
  <cac:DespatchAddress>
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
  </cac:DespatchAddress>
  <cac:DespatchParty>
    <cac:PartyName>
      <cbc:Name>Consortial</cbc:Name>
    </cac:PartyName>
  </cac:DespatchParty>
  <cac:Contact>
    <cbc:Name>Mrs Bouquet</cbc:Name>
    <cbc:Telephone>+1 158 1233714</cbc:Telephone>
    <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
    <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:Despatch>
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

### `DimensionType`

**Used as:** `cac:Dimension` · `cac:MeasurementDimension`

_52 instances across 2 elements, with 2 unique structures_

**Structure 1** — 48 instances

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>OuterHeight</cbc:AttributeID>
  <cbc:Measure>70</cbc:Measure>
</cac:MeasurementDimension>
```

**Structure 2** — 4 instances

```xml
<cac:Dimension>
  <cbc:AttributeID>NetWeight</cbc:AttributeID>
  <cbc:Measure>9.6</cbc:Measure>
</cac:Dimension>
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

### `EnvironmentalEmissionType`

**Used as:** `cac:EnvironmentalEmission`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:EnvironmentalEmission>
  <cbc:EnvironmentalEmissionTypeCode>CO2</cbc:EnvironmentalEmissionTypeCode>
  <cbc:ValueMeasure>0.2</cbc:ValueMeasure>
  <cbc:Description>200 grams of Carbon Dioxide per km</cbc:Description>
</cac:EnvironmentalEmission>
```

[↑ Back to contents](#contents)

### `EventLineItemType`

**Used as:** `cac:EventLineItem`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:EventLineItem>
  <cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
  <cac:ParticipatingLocationsLocation>
    <cbc:ID>ACME_BR_BE_0023</cbc:ID>
  </cac:ParticipatingLocationsLocation>
  <cac:RetailPlannedImpact>
    <cbc:Amount>0.0</cbc:Amount>
    <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
    <cbc:ForecastTypeCode>PROMOTIONAL</cbc:ForecastTypeCode>
    <cac:Period>
      <cbc:StartDate>2010-05-12</cbc:StartDate>
      <cbc:EndDate>2010-06-12</cbc:EndDate>
    </cac:Period>
  </cac:RetailPlannedImpact>
  <cac:SupplyItem>
    <cbc:Description>Acme knitwear scarf</cbc:Description>
    <cbc:Name>scarf</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000584</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:SupplyItem>
</cac:EventLineItem>
```

[↑ Back to contents](#contents)

### `EventTacticEnumerationType`

**Used as:** `cac:EventTacticEnumeration`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:EventTacticEnumeration>
  <cbc:DisplayTacticTypeCode>DISPLAY_GENERAL</cbc:DisplayTacticTypeCode>
</cac:EventTacticEnumeration>
```

[↑ Back to contents](#contents)

### `EventTacticType`

**Used as:** `cac:EventTactic`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:EventTactic>
  <cac:EventTacticEnumeration>
    <cbc:DisplayTacticTypeCode>DISPLAY_GENERAL</cbc:DisplayTacticTypeCode>
  </cac:EventTacticEnumeration>
  <cac:Period>
    <cbc:StartDate>2010-04-01</cbc:StartDate>
    <cbc:EndDate>2010-06-12</cbc:EndDate>
  </cac:Period>
</cac:EventTactic>
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

### `ExceptionCriteriaLineType`

**Used as:** `cac:ExceptionCriteriaLine`

_8 instances across 1 element, with 6 unique structures_

**Structure 1** — 2 instances

```xml
<cac:ExceptionCriteriaLine>
  <cbc:ID>exceptionCriteriaLineID</cbc:ID>
  <cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
  <cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cbc:PerformanceMetricTypeCode>SUPPLY</cbc:PerformanceMetricTypeCode>
  <cac:EffectivePeriod>
    <cbc:StartDate>2010-03-28</cbc:StartDate>
    <cbc:EndDate>2010-05-29</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:SupplyItem>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000581</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:SupplyItem>
</cac:ExceptionCriteriaLine>
```

**Structure 2** — 1 instance

```xml
<cac:ExceptionCriteriaLine>
  <cbc:ID>exceptionCriteriaLineID</cbc:ID>
  <cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
  <cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cac:EffectivePeriod>
    <cbc:StartDate>2010-04-28</cbc:StartDate>
    <cbc:EndDate>2010-06-29</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:SupplyItem>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000580</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:SupplyItem>
  <cac:ForecastExceptionCriteriaLine>
    <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
    <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
    <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
    <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
  </cac:ForecastExceptionCriteriaLine>
</cac:ExceptionCriteriaLine>
```

**Structure 3** — 1 instance

```xml
<cac:ExceptionCriteriaLine>
  <cbc:ID>exceptionCriteriaLineID</cbc:ID>
  <cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
  <cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cac:EffectivePeriod>
    <cbc:StartDate>2010-04-28</cbc:StartDate>
    <cbc:EndDate>2010-06-29</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:SupplyItem>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000580</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:SupplyItem>
  <cac:ForecastExceptionCriterionLine>
    <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
    <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
    <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
    <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
  </cac:ForecastExceptionCriterionLine>
</cac:ExceptionCriteriaLine>
```

**Structure 4** — 1 instance

```xml
<cac:ExceptionCriteriaLine>
  <cbc:ID>exceptionCriteriaLineID</cbc:ID>
  <cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
  <cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cac:EffectivePeriod>
    <cbc:StartDate>2010-04-28</cbc:StartDate>
    <cbc:EndDate>2010-06-29</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:SupplyItem>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000582</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:SupplyItem>
  <cac:ForecastExceptionCriteriaLine>
    <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
    <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
    <cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
    <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
    <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
  </cac:ForecastExceptionCriteriaLine>
</cac:ExceptionCriteriaLine>
```

**Structure 5** — 1 instance

```xml
<cac:ExceptionCriteriaLine>
  <cbc:ID>exceptionCriteriaLineID</cbc:ID>
  <cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
  <cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cac:EffectivePeriod>
    <cbc:StartDate>2010-04-28</cbc:StartDate>
    <cbc:EndDate>2010-06-29</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:SupplyItem>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000582</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:SupplyItem>
  <cac:ForecastExceptionCriterionLine>
    <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
    <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
    <cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
    <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
    <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
  </cac:ForecastExceptionCriterionLine>
</cac:ExceptionCriteriaLine>
```

**Structure 6** — 2 instances

```xml
<cac:ExceptionCriteriaLine>
  <cbc:ID>exceptionCriteriaLineID</cbc:ID>
  <cbc:ThresholdValueComparisonCode>EXCEEDS_EXCEPTION_VALUE</cbc:ThresholdValueComparisonCode>
  <cbc:ThresholdQuantity>120000</cbc:ThresholdQuantity>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cbc:SupplyChainActivityTypeCode>SALES</cbc:SupplyChainActivityTypeCode>
  <cac:EffectivePeriod>
    <cbc:StartDate>2010-03-28</cbc:StartDate>
    <cbc:EndDate>2010-08-29</cbc:EndDate>
  </cac:EffectivePeriod>
  <cac:SupplyItem>
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
  </cac:SupplyItem>
</cac:ExceptionCriteriaLine>
```

[↑ Back to contents](#contents)

### `ExceptionNotificationLineType`

**Used as:** `cac:ExceptionNotificationLine`

_4 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:ExceptionNotificationLine>
  <cbc:ID>exceptionNotificationLineID</cbc:ID>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cbc:ResolutionCode>LOCAL_INTERPOLATED_VALUE</cbc:ResolutionCode>
  <cbc:ComparedValueMeasure>2</cbc:ComparedValueMeasure>
  <cbc:SourceValueMeasure>2.1</cbc:SourceValueMeasure>
  <cbc:VarianceQuantity>20</cbc:VarianceQuantity>
  <cac:ExceptionObservationPeriod>
    <cbc:StartDate>2010-03-26</cbc:StartDate>
    <cbc:EndDate>2010-04-10</cbc:EndDate>
  </cac:ExceptionObservationPeriod>
  <cac:ForecastException>
    <cbc:PurposeCode>ORDER_FORECAST</cbc:PurposeCode>
    <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
    <cbc:IssueDate>2010-04-17</cbc:IssueDate>
    <cbc:IssueTime>10:00:00.000</cbc:IssueTime>
    <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  </cac:ForecastException>
  <cac:SupplyItem>
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
  </cac:SupplyItem>
</cac:ExceptionNotificationLine>
```

**Structure 2** — 3 instances

```xml
<cac:ExceptionNotificationLine>
  <cbc:ID>exceptionNotificationLineID</cbc:ID>
  <cbc:ExceptionStatusCode>NEW</cbc:ExceptionStatusCode>
  <cbc:CollaborationPriorityCode>HIGH</cbc:CollaborationPriorityCode>
  <cbc:ResolutionCode>LOCAL_INTERPOLATED_VALUE</cbc:ResolutionCode>
  <cbc:ComparedValueMeasure>2</cbc:ComparedValueMeasure>
  <cbc:SourceValueMeasure>2.1</cbc:SourceValueMeasure>
  <cbc:VarianceQuantity>20</cbc:VarianceQuantity>
  <cac:ExceptionObservationPeriod>
    <cbc:StartDate>2010-03-26</cbc:StartDate>
    <cbc:EndDate>2010-04-10</cbc:EndDate>
  </cac:ExceptionObservationPeriod>
  <cac:ForecastException>
    <cbc:ForecastPurposeCode>ORDER_FORECAST</cbc:ForecastPurposeCode>
    <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
    <cbc:IssueDate>2010-04-17</cbc:IssueDate>
    <cbc:IssueTime>10:00:00.000Z</cbc:IssueTime>
    <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  </cac:ForecastException>
  <cac:SupplyItem>
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
  </cac:SupplyItem>
</cac:ExceptionNotificationLine>
```

[↑ Back to contents](#contents)

### `ExchangeRateType`

**Used as:** `cac:ExchangeRate`

_4 instances across 1 element, with 1 unique structure_

**Structure 1** — 4 instances

```xml
<cac:ExchangeRate>
  <cbc:SourceCurrencyCode>USD</cbc:SourceCurrencyCode>
  <cbc:SourceCurrencyBaseRate>1.00</cbc:SourceCurrencyBaseRate>
  <cbc:TargetCurrencyCode>GBP</cbc:TargetCurrencyCode>
  <cbc:TargetCurrencyBaseRate>1.00</cbc:TargetCurrencyBaseRate>
  <cbc:CalculationRate>1.8947</cbc:CalculationRate>
  <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
  <cbc:Date>1967-08-13</cbc:Date>
</cac:ExchangeRate>
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

### `FinancialAccountType`

**Used as:** `cac:FinancialAccount` · `cac:PayeeFinancialAccount`

_37 instances across 2 elements, with 3 unique structures_

**Structure 1** — 1 instance

```xml
<cac:FinancialAccount>
  <cbc:ID>8601.12.11189</cbc:ID>
  <cbc:PaymentNote>Deutsche Bank</cbc:PaymentNote>
</cac:FinancialAccount>
```

**Structure 2** — 3 instances

```xml
<cac:PayeeFinancialAccount>
  <cbc:ID>DK1212341234123412</cbc:ID>
  <cac:FinancialInstitutionBranch>
    <cac:FinancialInstitution>
      <cbc:ID>DKDKABCD</cbc:ID>
    </cac:FinancialInstitution>
  </cac:FinancialInstitutionBranch>
</cac:PayeeFinancialAccount>
```

**Structure 3** — 33 instances

```xml
<cac:PayeeFinancialAccount>
  <cbc:ID>12345678</cbc:ID>
  <cbc:Name>Farthing Purchasing Consortium</cbc:Name>
  <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
  <cbc:CurrencyCode>GBP</cbc:CurrencyCode>
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
  <cac:Country>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:Country>
</cac:PayeeFinancialAccount>
```

[↑ Back to contents](#contents)

### `FinancialInstitutionType`

**Used as:** `cac:FinancialInstitution`

_36 instances across 1 element, with 2 unique structures_

**Structure 1** — 3 instances

```xml
<cac:FinancialInstitution>
  <cbc:ID>DKDKABCD</cbc:ID>
</cac:FinancialInstitution>
```

**Structure 2** — 33 instances

```xml
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
```

[↑ Back to contents](#contents)

### `ForecastExceptionCriterionLineType`

**Used as:** `cac:ForecastExceptionCriterionLine`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:ForecastExceptionCriterionLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriterionLine>
```

**Structure 2** — 1 instance

```xml
<cac:ForecastExceptionCriterionLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriterionLine>
```

[↑ Back to contents](#contents)

### `ForecastExceptionType`

**Used as:** `cac:ForecastException`

_4 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:ForecastException>
  <cbc:PurposeCode>ORDER_FORECAST</cbc:PurposeCode>
  <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
  <cbc:IssueDate>2010-04-17</cbc:IssueDate>
  <cbc:IssueTime>10:00:00.000</cbc:IssueTime>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
</cac:ForecastException>
```

**Structure 2** — 3 instances

```xml
<cac:ForecastException>
  <cbc:ForecastPurposeCode>ORDER_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
  <cbc:IssueDate>2010-04-17</cbc:IssueDate>
  <cbc:IssueTime>10:00:00.000</cbc:IssueTime>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
</cac:ForecastException>
```

[↑ Back to contents](#contents)

### `ForecastLineType`

**Used as:** `cac:ForecastLine`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:ForecastLine>
  <cbc:ID>forecastLineID</cbc:ID>
  <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
  <cac:ForecastPeriod>
    <cbc:StartDate>2010-02-01</cbc:StartDate>
    <cbc:EndDate>2010-05-26</cbc:EndDate>
  </cac:ForecastPeriod>
  <cac:SalesItem>
    <cbc:Quantity>20</cbc:Quantity>
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
  </cac:SalesItem>
</cac:ForecastLine>
```

[↑ Back to contents](#contents)

### `ForecastRevisionLineType`

**Used as:** `cac:ForecastRevisionLine`

_4 instances across 1 element, with 1 unique structure_

**Structure 1** — 4 instances

```xml
<cac:ForecastRevisionLine>
  <cbc:ID></cbc:ID>
  <cbc:RevisedForecastLineID></cbc:RevisedForecastLineID>
  <cbc:SourceForecastIssueDate>2005-02-17</cbc:SourceForecastIssueDate>
  <cbc:SourceForecastIssueTime>10:00:00.000</cbc:SourceForecastIssueTime>
  <cbc:AdjustmentReasonCode>REVISED_PROMOTION</cbc:AdjustmentReasonCode>
  <cac:ForecastPeriod>
    <cbc:StartDate>2005-02-26</cbc:StartDate>
    <cbc:EndDate>2005-12-26</cbc:EndDate>
  </cac:ForecastPeriod>
  <cac:SalesItem>
    <cbc:Quantity>20</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Acme beeswax</cbc:Description>
      <cbc:Name>beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:SalesItem>
</cac:ForecastRevisionLine>
```

[↑ Back to contents](#contents)

### `GoodsItemPassportCounterfoilType`

**Used as:** `cac:GoodsItemPassportCounterfoil`

_5 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:GoodsItemPassportCounterfoil>
  <cbc:ID>645634567</cbc:ID>
  <cbc:GoodsItemPassportID>ata01661</cbc:GoodsItemPassportID>
  <cac:VoucherDocumentReference>
    <cbc:ID>23445567</cbc:ID>
  </cac:VoucherDocumentReference>
</cac:GoodsItemPassportCounterfoil>
```

**Structure 2** — 4 instances

```xml
<cac:GoodsItemPassportCounterfoil>
  <cbc:ID>634563324</cbc:ID>
  <cbc:GoodsItemPassportID>ata01661</cbc:GoodsItemPassportID>
  <cac:CustomsOfficeLocation>
    <cbc:Name>Bietingen</cbc:Name>
  </cac:CustomsOfficeLocation>
  <cac:VoucherDocumentReference>
    <cbc:ID>52345423423</cbc:ID>
  </cac:VoucherDocumentReference>
</cac:GoodsItemPassportCounterfoil>
```

[↑ Back to contents](#contents)

### `GoodsItemType`

**Used as:** `cac:GoodsItem`

_47 instances across 1 element, with 13 unique structures_

**Structure 1** — 6 instances

```xml
<cac:GoodsItem>
  <cac:Item>
    <cac:CommodityClassification>
      <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
    </cac:CommodityClassification>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 2** — 2 instances

```xml
<cac:GoodsItem>
  <cbc:ID>GID_1</cbc:ID>
  <cac:Item>
    <cbc:Description>MOTOR CYCLE</cbc:Description>
    <cbc:Name>YAMAHA</cbc:Name>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 3** — 2 instances

```xml
<cac:GoodsItem>
  <cac:Item>
    <cac:CommodityClassification>
      <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
      <cbc:CommodityCode>8</cbc:CommodityCode>
    </cac:CommodityClassification>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 4** — 1 instance

```xml
<cac:GoodsItem>
  <cbc:ID>5</cbc:ID>
  <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
  <cbc:Quantity>1</cbc:Quantity>
  <cac:Item>
    <cbc:Description>METABO GE700, Pinolsliber</cbc:Description>
    <cac:OriginCountry>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:OriginCountry>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 5** — 18 instances

```xml
<cac:GoodsItem>
  <cbc:ID>15</cbc:ID>
  <cbc:DeclaredCustomsValueAmount>1500.00</cbc:DeclaredCustomsValueAmount>
  <cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
  <cbc:Quantity>1</cbc:Quantity>
  <cac:Item>
    <cbc:Description>MILWAUKEE HD18PD, Akkuboremaskine</cbc:Description>
    <cac:OriginCountry>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:OriginCountry>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 6** — 2 instances

```xml
<cac:GoodsItem>
  <cbc:ID>GoodsItemID1</cbc:ID>
  <cbc:Description>Office Printer 1</cbc:Description>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:Quantity>1</cbc:Quantity>
  <cac:Item>
    <cbc:Name>Office Printer 1</cbc:Name>
    <cbc:BrandName>Canon</cbc:BrandName>
    <cbc:ModelName>ModelName28</cbc:ModelName>
    <cac:CommodityClassification>
      <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
    </cac:CommodityClassification>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 7** — 2 instances

```xml
<cac:GoodsItem>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:Description>kattovalaisimia lasia</cbc:Description>
  <cbc:GrossWeightMeasure>30</cbc:GrossWeightMeasure>
  <cac:Pickup>
    <cac:PickupLocation>
      <cbc:ID>FI1234567-8R0001</cbc:ID>
      <cbc:LocationTypeCode>L</cbc:LocationTypeCode>
    </cac:PickupLocation>
  </cac:Pickup>
  <cac:ContainingPackage>
    <cbc:ID>567-3456</cbc:ID>
    <cbc:Quantity>5</cbc:Quantity>
    <cbc:PackagingTypeCode>CS</cbc:PackagingTypeCode>
  </cac:ContainingPackage>
</cac:GoodsItem>
```

**Structure 8** — 1 instance

```xml
<cac:GoodsItem>
  <cbc:ID>1</cbc:ID>
  <cbc:DeclaredCustomsValueAmount>0.00</cbc:DeclaredCustomsValueAmount>
  <cbc:DeclaredStatisticsValueAmount>4500.00</cbc:DeclaredStatisticsValueAmount>
  <cbc:Quantity>2</cbc:Quantity>
  <cac:Item>
    <cbc:Description>HILTI TE2 + TE35 Boremaskiner</cbc:Description>
    <cac:OriginCountry>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:OriginCountry>
    <cac:AdditionalItemProperty>
      <cbc:Name>AlcoholPercentage</cbc:Name>
      <cbc:Value>0</cbc:Value>
    </cac:AdditionalItemProperty>
    <cac:AdditionalItemProperty>
      <cbc:Name>DegreeOfPlato</cbc:Name>
      <cbc:Value>0</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 9** — 2 instances

```xml
<cac:GoodsItem>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:DeclaredStatisticsValueAmount>182.62</cbc:DeclaredStatisticsValueAmount>
  <cbc:ValueAmount>250</cbc:ValueAmount>
  <cbc:NetWeightMeasure>1</cbc:NetWeightMeasure>
  <cbc:PreferenceCriterionCode>100</cbc:PreferenceCriterionCode>
  <cbc:CustomsProcedureCode>1011</cbc:CustomsProcedureCode>
  <cac:Item>
    <cbc:Description>Kuulokkeita</cbc:Description>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>8518309590</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
  </cac:Item>
  <cac:Pickup>
    <cac:PickupLocation>
      <cbc:ID>01530</cbc:ID>
      <cbc:LocationTypeCode>P</cbc:LocationTypeCode>
    </cac:PickupLocation>
  </cac:Pickup>
  <cac:ContainingPackage>
    <cbc:ID>YangMei</cbc:ID>
    <cbc:Quantity>1</cbc:Quantity>
    <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
  </cac:ContainingPackage>
</cac:GoodsItem>
```

**Structure 10** — 2 instances

```xml
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
```

**Structure 11** — 4 instances

```xml
<cac:GoodsItem>
  <cbc:ID>1</cbc:ID>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:Description>Acme beeswax</cbc:Description>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
  <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
  <cbc:FreeOnBoardValueAmount>1241.30</cbc:FreeOnBoardValueAmount>
  <cbc:InsuranceValueAmount>1241.30</cbc:InsuranceValueAmount>
  <cbc:ValueAmount>1000.00</cbc:ValueAmount>
  <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
  <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
  <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
  <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
  <cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
  <cbc:CustomsTariffQuantity>100</cbc:CustomsTariffQuantity>
  <cac:Item>
    <cbc:Description>Beeswax</cbc:Description>
    <cbc:Name>Acme Beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 12** — 4 instances

```xml
<cac:GoodsItem>
  <cbc:ID>1</cbc:ID>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:Description>Acme beeswax</cbc:Description>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
  <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
  <cbc:FreeOnBoardValueAmount>1241.30</cbc:FreeOnBoardValueAmount>
  <cbc:InsuranceValueAmount>1241.30</cbc:InsuranceValueAmount>
  <cbc:ValueAmount>1000.00</cbc:ValueAmount>
  <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
  <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
  <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
  <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
  <cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
  <cbc:CustomsTariffQuantity>1000</cbc:CustomsTariffQuantity>
  <cac:Item>
    <cbc:Description>Beeswax</cbc:Description>
    <cbc:Name>Acme Beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:OriginCountry>
      <cbc:IdentificationCode>MX</cbc:IdentificationCode>
      <cbc:Name>Mexico</cbc:Name>
    </cac:OriginCountry>
  </cac:Item>
</cac:GoodsItem>
```

**Structure 13** — 1 instance

```xml
<cac:GoodsItem>
  <cbc:ID>000010</cbc:ID>
  <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
  <cbc:Quantity>63.000</cbc:Quantity>
  <cac:Item>
    <cbc:Description>ItemExample</cbc:Description>
    <cbc:PackQuantity>63</cbc:PackQuantity>
    <cbc:Name>Dairy Products</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>123456</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:OriginCountry>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:OriginCountry>
    <cac:CommodityClassification>
      <cbc:CommodityCode>19011000</cbc:CommodityCode>
    </cac:CommodityClassification>
    <cac:AdditionalItemProperty>
      <cbc:Name>AnimalSpecies</cbc:Name>
      <cbc:Value>Bovine</cbc:Value>
    </cac:AdditionalItemProperty>
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
    <cac:ItemInstance>
      <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
      <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
      <cac:AdditionalItemProperty>
        <cbc:Name>LineNetWeight</cbc:Name>
        <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>LineGrossWeight</cbc:Name>
        <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Quantity</cbc:Name>
        <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
      <cac:LotIdentification>
        <cbc:LotNumberID>9390000757</cbc:LotNumberID>
      </cac:LotIdentification>
    </cac:ItemInstance>
    <cac:Dimension>
      <cbc:AttributeID>NetWeight</cbc:AttributeID>
      <cbc:Measure>9.6</cbc:Measure>
    </cac:Dimension>
    <cac:Dimension>
      <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
      <cbc:Measure>604.8</cbc:Measure>
    </cac:Dimension>
    <cac:Dimension>
      <cbc:AttributeID>GrossWeight</cbc:AttributeID>
      <cbc:Measure>12.288</cbc:Measure>
    </cac:Dimension>
    <cac:Dimension>
      <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
      <cbc:Measure>774.144</cbc:Measure>
    </cac:Dimension>
  </cac:Item>
  <cac:Despatch>
    <cbc:ID>000010</cbc:ID>
  </cac:Despatch>
  <cac:MaximumTemperature>
    <cbc:AttributeID>TC</cbc:AttributeID>
    <cbc:Measure>3.00</cbc:Measure>
    <cbc:Description>Chilled</cbc:Description>
  </cac:MaximumTemperature>
</cac:GoodsItem>
```

[↑ Back to contents](#contents)

### `InstructionForReturnsLineType`

**Used as:** `cac:InstructionForReturnsLine`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:InstructionForReturnsLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Quantity>5</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Leather Jacket</cbc:Description>
    <cbc:Name>Leather Jacket man</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>AA128</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>YX233</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:InstructionForReturnsLine>
```

[↑ Back to contents](#contents)

### `InventoryReportLineType`

**Used as:** `cac:InventoryReportLine`

_6 instances across 1 element, with 1 unique structure_

**Structure 1** — 6 instances

```xml
<cac:InventoryReportLine>
  <cbc:ID>3</cbc:ID>
  <cbc:Quantity>5</cbc:Quantity>
  <cbc:InventoryValueAmount>300</cbc:InventoryValueAmount>
  <cac:Item>
    <cbc:Description>woman's dress</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>DH019</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>BA058</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:InventoryReportLine>
```

[↑ Back to contents](#contents)

### `InvoiceLineType`

**Used as:** `cac:InvoiceLine`

_34 instances across 1 element, with 8 unique structures_

**Structure 1** — 1 instance

```xml
<cac:InvoiceLine>
  <cbc:ID>1</cbc:ID>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cac:Item>
    <cbc:Description>Cotter pin, MIL-SPEC</cbc:Description>
  </cac:Item>
</cac:InvoiceLine>
```

**Structure 2** — 3 instances

```xml
<cac:InvoiceLine>
  <cbc:ID>4</cbc:ID>
  <cbc:InvoicedQuantity>-1</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>-25</cbc:LineExtensionAmount>
  <cac:OrderLineReference>
    <cbc:LineID>2</cbc:LineID>
  </cac:OrderLineReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>0</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Returned IBM 5150 desktop</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB010</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890127</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344322</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434565</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>E</cbc:ID>
      <cbc:Percent>0</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>25</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:InvoiceLine>
```

**Structure 3** — 3 instances

```xml
<cac:InvoiceLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Note>Cover is slightly damaged.</cbc:Note>
  <cbc:InvoicedQuantity>-1</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>-3.96</cbc:LineExtensionAmount>
  <cac:OrderLineReference>
    <cbc:LineID>5</cbc:LineID>
  </cac:OrderLineReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>-0.396</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Returned "Advanced computing" book</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB008</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890125</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434567</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>3.96</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:InvoiceLine>
```

**Structure 4** — 3 instances

```xml
<cac:InvoiceLine>
  <cbc:ID>5</cbc:ID>
  <cbc:InvoicedQuantity>250</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>187.5</cbc:LineExtensionAmount>
  <cbc:AccountingCost>BookingCode002</cbc:AccountingCost>
  <cac:OrderLineReference>
    <cbc:LineID>4</cbc:LineID>
  </cac:OrderLineReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>37.5</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Network cable</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB011</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890128</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434564</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
    <cac:AdditionalItemProperty>
      <cbc:Name>Type</cbc:Name>
      <cbc:Value>Cat5</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>0.75</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:InvoiceLine>
```

**Structure 5** — 3 instances

```xml
<cac:InvoiceLine>
  <cbc:ID>3</cbc:ID>
  <cbc:InvoicedQuantity>2</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>4.96</cbc:LineExtensionAmount>
  <cac:OrderLineReference>
    <cbc:LineID>3</cbc:LineID>
  </cac:OrderLineReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>0.496</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>"Computing for dummies" book</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB009</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890126</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434566</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>2.48</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
      <cbc:Amount>0.275</cbc:Amount>
      <cbc:BaseAmount>2.75</cbc:BaseAmount>
    </cac:AllowanceCharge>
  </cac:Price>
</cac:InvoiceLine>
```

**Structure 6** — 1 instance

```xml
<cac:InvoiceLine>
  <cbc:ID>A</cbc:ID>
  <cbc:InvoicedQuantity>100</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cac:OrderLineReference>
    <cbc:LineID>1</cbc:LineID>
    <cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cac:OrderReference>
      <cbc:ID>AEG012345</cbc:ID>
      <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
      <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
      <cbc:IssueDate>2005-06-20</cbc:IssueDate>
    </cac:OrderReference>
  </cac:OrderLineReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>17.50</cbc:TaxAmount>
    <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
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
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:LotIdentification>
      <cbc:LotNumberID>546378239</cbc:LotNumberID>
      <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
    </cac:LotIdentification>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>1.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:InvoiceLine>
```

**Structure 7** — 17 instances

```xml
<cac:InvoiceLine>
  <cbc:ID>A</cbc:ID>
  <cbc:InvoicedQuantity>100</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cac:OrderLineReference>
    <cbc:LineID>1</cbc:LineID>
    <cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cac:OrderReference>
      <cbc:ID>AEG012345</cbc:ID>
      <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
      <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
      <cbc:IssueDate>2005-06-20</cbc:IssueDate>
    </cac:OrderReference>
  </cac:OrderLineReference>
  <cac:TaxTotal>
    <cbc:TaxAmount>17.50</cbc:TaxAmount>
    <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
    <cac:TaxSubtotal>
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
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:ItemInstance>
      <cac:LotIdentification>
        <cbc:LotNumberID>546378239</cbc:LotNumberID>
        <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
      </cac:LotIdentification>
    </cac:ItemInstance>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>1.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:InvoiceLine>
```

**Structure 8** — 3 instances

```xml
<cac:InvoiceLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Scratch on box</cbc:Note>
  <cbc:InvoicedQuantity>1</cbc:InvoicedQuantity>
  <cbc:LineExtensionAmount>1273</cbc:LineExtensionAmount>
  <cbc:AccountingCost>BookingCode001</cbc:AccountingCost>
  <cac:OrderLineReference>
    <cbc:LineID>1</cbc:LineID>
  </cac:OrderLineReference>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Damage</cbc:AllowanceChargeReason>
    <cbc:Amount>12</cbc:Amount>
  </cac:AllowanceCharge>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Testing</cbc:AllowanceChargeReason>
    <cbc:Amount>10</cbc:Amount>
  </cac:AllowanceCharge>
  <cac:TaxTotal>
    <cbc:TaxAmount>254.6</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Description>Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:
				3MB. Screen 1440x900</cbc:Description>
    <cbc:Name>Labtop computer</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>JB007</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890124</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>12344321</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode>65434568</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:ClassifiedTaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:ClassifiedTaxCategory>
    <cac:AdditionalItemProperty>
      <cbc:Name>Color</cbc:Name>
      <cbc:Value>black</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>1273</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
      <cbc:Amount>225</cbc:Amount>
      <cbc:BaseAmount>1500</cbc:BaseAmount>
    </cac:AllowanceCharge>
  </cac:Price>
</cac:InvoiceLine>
```

[↑ Back to contents](#contents)

### `ItemIdentificationType`

**Used as:** `cac:BuyersItemIdentification` · `cac:SellersItemIdentification` · `cac:StandardItemIdentification`

_300 instances across 3 elements, with 3 unique structures_

**Structure 1** — 98 instances

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>6578489</cbc:ID>
</cac:BuyersItemIdentification>
```

**Structure 2** — 139 instances

```xml
<cac:SellersItemIdentification>
  <cbc:ID>17589683</cbc:ID>
</cac:SellersItemIdentification>
```

**Structure 3** — 63 instances

```xml
<cac:StandardItemIdentification>
  <cbc:ID>00123450000584</cbc:ID>
</cac:StandardItemIdentification>
```

[↑ Back to contents](#contents)

### `ItemInstanceType`

**Used as:** `cac:ItemInstance`

_30 instances across 1 element, with 2 unique structures_

**Structure 1** — 29 instances

```xml
<cac:ItemInstance>
  <cac:LotIdentification>
    <cbc:LotNumberID>546378239</cbc:LotNumberID>
    <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
  </cac:LotIdentification>
</cac:ItemInstance>
```

**Structure 2** — 1 instance

```xml
<cac:ItemInstance>
  <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
  <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
  <cac:AdditionalItemProperty>
    <cbc:Name>LineNetWeight</cbc:Name>
    <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
  </cac:AdditionalItemProperty>
  <cac:AdditionalItemProperty>
    <cbc:Name>LineGrossWeight</cbc:Name>
    <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
  </cac:AdditionalItemProperty>
  <cac:AdditionalItemProperty>
    <cbc:Name>Quantity</cbc:Name>
    <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
  </cac:AdditionalItemProperty>
  <cac:LotIdentification>
    <cbc:LotNumberID>9390000757</cbc:LotNumberID>
  </cac:LotIdentification>
</cac:ItemInstance>
```

[↑ Back to contents](#contents)

### `ItemLocationQuantityType`

**Used as:** `cac:ItemLocationQuantity`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:ItemLocationQuantity>
  <cbc:LeadTimeMeasure>3</cbc:LeadTimeMeasure>
  <cbc:MinimumQuantity>2</cbc:MinimumQuantity>
</cac:ItemLocationQuantity>
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

### `ItemPropertyType`

**Used as:** `cac:AdditionalItemProperty`

_30 instances across 1 element, with 2 unique structures_

**Structure 1** — 27 instances

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Type</cbc:Name>
  <cbc:Value>Cat5</cbc:Value>
</cac:AdditionalItemProperty>
```

**Structure 2** — 3 instances

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>LineNetWeight</cbc:Name>
  <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
</cac:AdditionalItemProperty>
```

[↑ Back to contents](#contents)

### `ItemType`

**Used as:** `cac:Item` · `cac:SupplyItem`

_200 instances across 2 elements, with 26 unique structures_

**Structure 1** — 2 instances

```xml
<cac:Item></cac:Item>
```

**Structure 2** — 5 instances

```xml
<cac:Item>
  <cbc:Description>Red paint</cbc:Description>
</cac:Item>
```

**Structure 3** — 2 instances

```xml
<cac:Item>
  <cbc:Name>High-grade Widget</cbc:Name>
</cac:Item>
```

**Structure 4** — 10 instances

```xml
<cac:Item>
  <cbc:Description>Mus</cbc:Description>
  <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
</cac:Item>
```

**Structure 5** — 4 instances

```xml
<cac:Item>
  <cac:StandardItemIdentification>
    <cbc:ID>06110123456784</cbc:ID>
  </cac:StandardItemIdentification>
</cac:Item>
```

**Structure 6** — 6 instances

```xml
<cac:Item>
  <cac:CommodityClassification>
    <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
  </cac:CommodityClassification>
</cac:Item>
```

**Structure 7** — 6 instances

```xml
<cac:SupplyItem>
  <cac:StandardItemIdentification>
    <cbc:ID>00123450000580</cbc:ID>
  </cac:StandardItemIdentification>
</cac:SupplyItem>
```

**Structure 8** — 2 instances

```xml
<cac:Item>
  <cac:CommodityClassification>
    <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
    <cbc:CommodityCode>8</cbc:CommodityCode>
  </cac:CommodityClassification>
</cac:Item>
```

**Structure 9** — 19 instances

```xml
<cac:Item>
  <cbc:Description>BOSCH GLL 3-80P Lasernivilering</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

**Structure 10** — 2 instances

```xml
<cac:Item>
  <cbc:Description>Kuulokkeita</cbc:Description>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>8518309590</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
</cac:Item>
```

**Structure 11** — 2 instances

```xml
<cac:Item>
  <cbc:Name>Magic cloak</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>MC002</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

**Structure 12** — 17 instances

```xml
<cac:Item>
  <cbc:Description>skirt</cbc:Description>
  <cac:BuyersItemIdentification>
    <cbc:ID>TS893</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>PK009</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

**Structure 13** — 2 instances

```xml
<cac:Item>
  <cbc:Name>Office Printer 2</cbc:Name>
  <cbc:BrandName>Canon</cbc:BrandName>
  <cbc:ModelName>MPX2000</cbc:ModelName>
  <cac:CommodityClassification>
    <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
  </cac:CommodityClassification>
</cac:Item>
```

**Structure 14** — 28 instances

```xml
<cac:Item>
  <cbc:Description>Acme beeswax</cbc:Description>
  <cbc:Name>beeswax</cbc:Name>
  <cac:BuyersItemIdentification>
    <cbc:ID>6578489</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>17589683</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

**Structure 15** — 8 instances

```xml
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
```

**Structure 16** — 9 instances

```xml
<cac:SupplyItem>
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
</cac:SupplyItem>
```

**Structure 17** — 3 instances

```xml
<cac:Item>
  <cbc:Description>Acme beeswax</cbc:Description>
  <cbc:Name>beeswax</cbc:Name>
  <cac:BuyersItemIdentification>
    <cbc:ID>6578489</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>17589683</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:LotIdentification>
    <cbc:LotNumberID>546378239</cbc:LotNumberID>
    <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
  </cac:LotIdentification>
</cac:Item>
```

**Structure 18** — 4 instances

```xml
<cac:Item>
  <cbc:Description>Beeswax</cbc:Description>
  <cbc:Name>Acme Beeswax</cbc:Name>
  <cac:BuyersItemIdentification>
    <cbc:ID>6578489</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>17589683</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:OriginCountry>
    <cbc:IdentificationCode>MX</cbc:IdentificationCode>
    <cbc:Name>Mexico</cbc:Name>
  </cac:OriginCountry>
</cac:Item>
```

**Structure 19** — 2 instances

```xml
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
```

**Structure 20** — 1 instance

```xml
<cac:Item>
  <cbc:Description>HILTI TE2 + TE35 Boremaskiner</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
  <cac:AdditionalItemProperty>
    <cbc:Name>AlcoholPercentage</cbc:Name>
    <cbc:Value>0</cbc:Value>
  </cac:AdditionalItemProperty>
  <cac:AdditionalItemProperty>
    <cbc:Name>DegreeOfPlato</cbc:Name>
    <cbc:Value>0</cbc:Value>
  </cac:AdditionalItemProperty>
</cac:Item>
```

**Structure 21** — 29 instances

```xml
<cac:Item>
  <cbc:Description>Acme beeswax</cbc:Description>
  <cbc:Name>beeswax</cbc:Name>
  <cac:BuyersItemIdentification>
    <cbc:ID>6578489</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>17589683</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:ItemInstance>
    <cac:LotIdentification>
      <cbc:LotNumberID>546378239</cbc:LotNumberID>
      <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
    </cac:LotIdentification>
  </cac:ItemInstance>
</cac:Item>
```

**Structure 22** — 6 instances

```xml
<cac:Item>
  <cbc:Description>Red paint</cbc:Description>
  <cbc:Name>Falu Rödfärg</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>SItemNo001</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:StandardItemIdentification>
    <cbc:ID>1234567890123</cbc:ID>
  </cac:StandardItemIdentification>
  <cac:AdditionalItemProperty>
    <cbc:Name>Paint type</cbc:Name>
    <cbc:Value>Acrylic</cbc:Value>
  </cac:AdditionalItemProperty>
  <cac:AdditionalItemProperty>
    <cbc:Name>Solvant</cbc:Name>
    <cbc:Value>Water</cbc:Value>
  </cac:AdditionalItemProperty>
</cac:Item>
```

**Structure 23** — 18 instances

```xml
<cac:Item>
  <cbc:Name>Returned "Advanced computing" book</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>JB008</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:StandardItemIdentification>
    <cbc:ID>1234567890125</cbc:ID>
  </cac:StandardItemIdentification>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>65434567</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
  <cac:ClassifiedTaxCategory>
    <cbc:ID>AA</cbc:ID>
    <cbc:Percent>10</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:ClassifiedTaxCategory>
</cac:Item>
```

**Structure 24** — 6 instances

```xml
<cac:Item>
  <cbc:Name>Network cable</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>JB011</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:StandardItemIdentification>
    <cbc:ID>1234567890128</cbc:ID>
  </cac:StandardItemIdentification>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>65434564</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
  <cac:ClassifiedTaxCategory>
    <cbc:ID>S</cbc:ID>
    <cbc:Percent>20</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:ClassifiedTaxCategory>
  <cac:AdditionalItemProperty>
    <cbc:Name>Type</cbc:Name>
    <cbc:Value>Cat5</cbc:Value>
  </cac:AdditionalItemProperty>
</cac:Item>
```

**Structure 25** — 6 instances

```xml
<cac:Item>
  <cbc:Description>Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:
				3MB. Screen 1440x900</cbc:Description>
  <cbc:Name>Labtop computer</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>JB007</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:StandardItemIdentification>
    <cbc:ID>1234567890124</cbc:ID>
  </cac:StandardItemIdentification>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>12344321</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>65434568</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
  <cac:ClassifiedTaxCategory>
    <cbc:ID>S</cbc:ID>
    <cbc:Percent>20</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:ClassifiedTaxCategory>
  <cac:AdditionalItemProperty>
    <cbc:Name>Color</cbc:Name>
    <cbc:Value>black</cbc:Value>
  </cac:AdditionalItemProperty>
</cac:Item>
```

**Structure 26** — 1 instance

```xml
<cac:Item>
  <cbc:Description>ItemExample</cbc:Description>
  <cbc:PackQuantity>63</cbc:PackQuantity>
  <cbc:Name>Dairy Products</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>123456</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:OriginCountry>
  <cac:CommodityClassification>
    <cbc:CommodityCode>19011000</cbc:CommodityCode>
  </cac:CommodityClassification>
  <cac:AdditionalItemProperty>
    <cbc:Name>AnimalSpecies</cbc:Name>
    <cbc:Value>Bovine</cbc:Value>
  </cac:AdditionalItemProperty>
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
  <cac:ItemInstance>
    <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
    <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
    <cac:AdditionalItemProperty>
      <cbc:Name>LineNetWeight</cbc:Name>
      <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
    </cac:AdditionalItemProperty>
    <cac:AdditionalItemProperty>
      <cbc:Name>LineGrossWeight</cbc:Name>
      <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
    </cac:AdditionalItemProperty>
    <cac:AdditionalItemProperty>
      <cbc:Name>Quantity</cbc:Name>
      <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
    </cac:AdditionalItemProperty>
    <cac:LotIdentification>
      <cbc:LotNumberID>9390000757</cbc:LotNumberID>
    </cac:LotIdentification>
  </cac:ItemInstance>
  <cac:Dimension>
    <cbc:AttributeID>NetWeight</cbc:AttributeID>
    <cbc:Measure>9.6</cbc:Measure>
  </cac:Dimension>
  <cac:Dimension>
    <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
    <cbc:Measure>604.8</cbc:Measure>
  </cac:Dimension>
  <cac:Dimension>
    <cbc:AttributeID>GrossWeight</cbc:AttributeID>
    <cbc:Measure>12.288</cbc:Measure>
  </cac:Dimension>
  <cac:Dimension>
    <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
    <cbc:Measure>774.144</cbc:Measure>
  </cac:Dimension>
</cac:Item>
```

[↑ Back to contents](#contents)

### `LanguageType`

**Used as:** `cac:Language`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:Language>
  <cbc:ID>fi</cbc:ID>
</cac:Language>
```

[↑ Back to contents](#contents)

### `LineItemType`

**Used as:** `cac:LineItem`

_38 instances across 1 element, with 10 unique structures_

**Structure 1** — 2 instances

```xml
<cac:LineItem>
  <cbc:ID>2</cbc:ID>
  <cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
  <cac:Item></cac:Item>
</cac:LineItem>
```

**Structure 2** — 4 instances

```xml
<cac:LineItem>
  <cbc:ID>2</cbc:ID>
  <cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
  <cac:Item>
    <cbc:Description>Very good pencils for red paint.</cbc:Description>
  </cac:Item>
</cac:LineItem>
```

**Structure 3** — 4 instances

```xml
<cac:LineItem>
  <cbc:ID>DELL2363463</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Fladskærm</cbc:Description>
    <cbc:Name>FP/BL 1908WFP</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

**Structure 4** — 5 instances

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>100</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:LineItem>
```

**Structure 5** — 4 instances

```xml
<cac:LineItem>
  <cbc:ID>DELL8436783</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cbc:LineExtensionAmount>1750.00</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>437.50</cbc:TotalTaxAmount>
  <cac:Price>
    <cbc:PriceAmount>50.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Tastatur</cbc:Description>
    <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

**Structure 6** — 5 instances

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>100</cbc:Quantity>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>17.50</cbc:TotalTaxAmount>
  <cac:Price>
    <cbc:PriceAmount>100.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:LineItem>
```

**Structure 7** — 3 instances

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:SalesOrderID>A</cbc:SalesOrderID>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cbc:Quantity>100</cbc:Quantity>
  <cbc:LineExtensionAmount>1000.00</cbc:LineExtensionAmount>
  <cac:Price>
    <cbc:PriceAmount>10.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Beeswax</cbc:Description>
    <cbc:Name>Acme Beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:LineItem>
```

**Structure 8** — 5 instances

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:SalesOrderID>A</cbc:SalesOrderID>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cbc:Quantity>100</cbc:Quantity>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>17.50</cbc:TotalTaxAmount>
  <cac:Price>
    <cbc:PriceAmount>100.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:LineItem>
```

**Structure 9** — 4 instances

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>120</cbc:Quantity>
  <cbc:LineExtensionAmount>6000</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>10</cbc:TotalTaxAmount>
  <cbc:PartialDeliveryIndicator>false</cbc:PartialDeliveryIndicator>
  <cbc:AccountingCostCode>ProjectID123</cbc:AccountingCostCode>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2010-02-10</cbc:StartDate>
      <cbc:EndDate>2010-02-25</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
  <cac:OriginatorParty>
    <cac:PartyIdentification>
      <cbc:ID>EmployeeXXX</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Josef K.</cbc:Name>
    </cac:PartyName>
  </cac:OriginatorParty>
  <cac:Price>
    <cbc:PriceAmount>50</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Red paint</cbc:Description>
    <cbc:Name>Falu Rödfärg</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>SItemNo001</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890123</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:AdditionalItemProperty>
      <cbc:Name>Paint type</cbc:Name>
      <cbc:Value>Acrylic</cbc:Value>
    </cac:AdditionalItemProperty>
    <cac:AdditionalItemProperty>
      <cbc:Name>Solvant</cbc:Name>
      <cbc:Value>Water</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
</cac:LineItem>
```

**Structure 10** — 2 instances

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:LineStatusCode>Revised</cbc:LineStatusCode>
  <cbc:Quantity>240</cbc:Quantity>
  <cbc:LineExtensionAmount>12000</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>20</cbc:TotalTaxAmount>
  <cbc:PartialDeliveryIndicator>false</cbc:PartialDeliveryIndicator>
  <cbc:AccountingCostCode>ProjectID123</cbc:AccountingCostCode>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2010-02-10</cbc:StartDate>
      <cbc:EndDate>2010-02-25</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
  <cac:OriginatorParty>
    <cac:PartyIdentification>
      <cbc:ID>EmployeeXXX</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Josef K.</cbc:Name>
    </cac:PartyName>
  </cac:OriginatorParty>
  <cac:Price>
    <cbc:PriceAmount>50</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Red paint</cbc:Description>
    <cbc:Name>Falu Rödfärg</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>SItemNo001</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>1234567890123</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:AdditionalItemProperty>
      <cbc:Name>Paint type</cbc:Name>
      <cbc:Value>Acrylic</cbc:Value>
    </cac:AdditionalItemProperty>
    <cac:AdditionalItemProperty>
      <cbc:Name>Solvant</cbc:Name>
      <cbc:Value>Water</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
</cac:LineItem>
```

[↑ Back to contents](#contents)

### `LocationCoordinateType`

**Used as:** `cac:LocationCoordinate`

_5 instances across 1 element, with 3 unique structures_

**Structure 1** — 1 instance

```xml
<cac:LocationCoordinate></cac:LocationCoordinate>
```

**Structure 2** — 1 instance

```xml
<cac:LocationCoordinate>
  <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
  <cbc:LatitudeDegreesMeasure>58</cbc:LatitudeDegreesMeasure>
  <cbc:LongitudeDegreesMeasure>10</cbc:LongitudeDegreesMeasure>
</cac:LocationCoordinate>
```

**Structure 3** — 3 instances

```xml
<cac:LocationCoordinate>
  <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
  <cbc:LatitudeDegreesMeasure>53.4</cbc:LatitudeDegreesMeasure>
  <cbc:LatitudeMinutesMeasure>33</cbc:LatitudeMinutesMeasure>
  <cbc:LatitudeDirectionCode>North</cbc:LatitudeDirectionCode>
  <cbc:LongitudeDegreesMeasure>8.48</cbc:LongitudeDegreesMeasure>
  <cbc:LongitudeMinutesMeasure>27</cbc:LongitudeMinutesMeasure>
  <cbc:LongitudeDirectionCode>East</cbc:LongitudeDirectionCode>
</cac:LocationCoordinate>
```

[↑ Back to contents](#contents)

### `LocationType`

**Used as:** `cac:ActivityFinalLocation` · `cac:ActivityOriginLocation` · `cac:CustomsExitOfficeLocation` · `cac:CustomsOfficeLocation` · `cac:DeliveryLocation` · `cac:FirstArrivalPortLocation` · `cac:FromLocation` · `cac:ImportCustomsExitOfficeLocation` · `cac:LastExitPortLocation` · `cac:LoadingPortLocation` · `cac:Location` · `cac:OfficeOfEntryLocation` · `cac:ParticipatingLocationsLocation` · `cac:PhysicalLocation` · `cac:PickupLocation` · `cac:PointOfSaleLocation` · `cac:ReportingLocation` · `cac:StatusLocation` · `cac:ToLocation` · `cac:TransitCustomsExitOfficeLocation` · `cac:TransshipPortLocation` · `cac:UnloadingPortLocation`

_142 instances across 22 elements, with 62 unique structures_

**Structure 1** — 2 instances

```xml
<cac:DeliveryLocation>
  <cbc:ID>STO</cbc:ID>
</cac:DeliveryLocation>
```

**Structure 2** — 5 instances

```xml
<cac:DeliveryLocation>
  <cbc:Name>BANGKOK</cbc:Name>
</cac:DeliveryLocation>
```

**Structure 3** — 1 instance

```xml
<cac:LoadingPortLocation>
  <cbc:ID>Aarhus</cbc:ID>
</cac:LoadingPortLocation>
```

**Structure 4** — 1 instance

```xml
<cac:UnloadingPortLocation>
  <cbc:ID>Balboa Port</cbc:ID>
</cac:UnloadingPortLocation>
```

**Structure 5** — 2 instances

```xml
<cac:FirstArrivalPortLocation>
  <cbc:Name>Padborg</cbc:Name>
</cac:FirstArrivalPortLocation>
```

**Structure 6** — 2 instances

```xml
<cac:FirstArrivalPortLocation>
  <cbc:ID>FI015300</cbc:ID>
</cac:FirstArrivalPortLocation>
```

**Structure 7** — 1 instance

```xml
<cac:LastExitPortLocation>
  <cbc:Name>Bietingen</cbc:Name>
</cac:LastExitPortLocation>
```

**Structure 8** — 4 instances

```xml
<cac:ActivityOriginLocation>
  <cbc:ID></cbc:ID>
</cac:ActivityOriginLocation>
```

**Structure 9** — 3 instances

```xml
<cac:ParticipatingLocationsLocation>
  <cbc:ID>ACME_BR_BE_0023</cbc:ID>
</cac:ParticipatingLocationsLocation>
```

**Structure 10** — 2 instances

```xml
<cac:Location>
  <cbc:ID>CNSHA</cbc:ID>
</cac:Location>
```

**Structure 11** — 2 instances

```xml
<cac:PhysicalLocation>
  <cbc:InformationURI>https://goo.gl/maps/2k242</cbc:InformationURI>
</cac:PhysicalLocation>
```

**Structure 12** — 4 instances

```xml
<cac:CustomsOfficeLocation>
  <cbc:Name>Bietingen</cbc:Name>
</cac:CustomsOfficeLocation>
```

**Structure 13** — 2 instances

```xml
<cac:TransitCustomsExitOfficeLocation>
  <cbc:ID>FI001800</cbc:ID>
</cac:TransitCustomsExitOfficeLocation>
```

**Structure 14** — 2 instances

```xml
<cac:ImportCustomsExitOfficeLocation>
  <cbc:ID>CH002621</cbc:ID>
</cac:ImportCustomsExitOfficeLocation>
```

**Structure 15** — 11 instances

```xml
<cac:DeliveryLocation>
  <cbc:ID>GBBRS</cbc:ID>
  <cbc:Description>Bristol</cbc:Description>
</cac:DeliveryLocation>
```

**Structure 16** — 4 instances

```xml
<cac:LoadingPortLocation>
  <cbc:ID>USBOS</cbc:ID>
  <cbc:Description>Boston Airport</cbc:Description>
</cac:LoadingPortLocation>
```

**Structure 17** — 4 instances

```xml
<cac:UnloadingPortLocation>
  <cbc:ID>GBBRS</cbc:ID>
  <cbc:Description>Bristol Airport</cbc:Description>
</cac:UnloadingPortLocation>
```

**Structure 18** — 4 instances

```xml
<cac:TransshipPortLocation>
  <cbc:ID>GBLHR</cbc:ID>
  <cbc:Description>Heathrow Apt/London</cbc:Description>
</cac:TransshipPortLocation>
```

**Structure 19** — 4 instances

```xml
<cac:FirstArrivalPortLocation>
  <cbc:ID>GBBRS</cbc:ID>
  <cbc:Description>Bristol</cbc:Description>
</cac:FirstArrivalPortLocation>
```

**Structure 20** — 4 instances

```xml
<cac:LastExitPortLocation>
  <cbc:ID>USBOS</cbc:ID>
  <cbc:Description>Boston</cbc:Description>
</cac:LastExitPortLocation>
```

**Structure 21** — 4 instances

```xml
<cac:PickupLocation>
  <cbc:ID>01530</cbc:ID>
  <cbc:LocationTypeCode>P</cbc:LocationTypeCode>
</cac:PickupLocation>
```

**Structure 22** — 3 instances

```xml
<cac:DeliveryLocation>
  <cac:Address>
    <cbc:CityName>Munich</cbc:CityName>
  </cac:Address>
</cac:DeliveryLocation>
```

**Structure 23** — 2 instances

```xml
<cac:PhysicalLocation>
  <cac:Address>
    <cbc:CityName>Espoo</cbc:CityName>
  </cac:Address>
</cac:PhysicalLocation>
```

**Structure 24** — 1 instance

```xml
<cac:UnloadingPortLocation>
  <cac:Address>
    <cac:Country>
      <cbc:IdentificationCode>CH</cbc:IdentificationCode>
      <cbc:Name>Swiss</cbc:Name>
    </cac:Country>
  </cac:Address>
</cac:UnloadingPortLocation>
```

**Structure 25** — 1 instance

```xml
<cac:Location>
  <cbc:ID>ITGOA</cbc:ID>
  <cac:Address>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 26** — 1 instance

```xml
<cac:FirstArrivalPortLocation>
  <cbc:ID>ITGOA</cbc:ID>
  <cbc:LocationTypeCode>41</cbc:LocationTypeCode>
  <cac:Address>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:FirstArrivalPortLocation>
```

**Structure 27** — 3 instances

```xml
<cac:Location>
  <cac:Address>
    <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
    <cbc:CityName>Nurnberg</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 28** — 1 instance

```xml
<cac:Location>
  <cbc:ID>MAPTM</cbc:ID>
  <cac:Address>
    <cbc:CityName>Tanger</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>MA</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 29** — 1 instance

```xml
<cac:Location>
  <cbc:ID>ITGOA</cbc:ID>
  <cbc:LocationTypeCode>24</cbc:LocationTypeCode>
  <cac:Address>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 30** — 1 instance

```xml
<cac:OfficeOfEntryLocation>
  <cbc:ID>DE000396</cbc:ID>
  <cbc:LocationTypeCode>41</cbc:LocationTypeCode>
  <cac:Address>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:OfficeOfEntryLocation>
```

**Structure 31** — 1 instance

```xml
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
```

**Structure 32** — 3 instances

```xml
<cac:Location>
  <cac:Address>
    <cbc:ID>DEHAM</cbc:ID>
    <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
    <cbc:CityName>Hamburg</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 33** — 4 instances

```xml
<cac:Location>
  <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
    <cbc:CityName>Nurnberg</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 34** — 3 instances

```xml
<cac:Location>
  <cac:Address>
    <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
    <cbc:CityName>Nurnberg</cbc:CityName>
    <cbc:PostalZone>28400</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 35** — 1 instance

```xml
<cac:Location>
  <cac:Address>
    <cbc:StreetName>StreetName Example</cbc:StreetName>
    <cbc:CityName>El Dorado</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>PA</cbc:IdentificationCode>
      <cbc:Name>Panama</cbc:Name>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 36** — 1 instance

```xml
<cac:ReportingLocation>
  <cac:Address>
    <cbc:StreetName>Declarant Street</cbc:StreetName>
    <cbc:CityName>Declarant City</cbc:CityName>
    <cbc:PostalZone>Declarant Post Code</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:ReportingLocation>
```

**Structure 37** — 1 instance

```xml
<cac:ToLocation>
  <cac:Address>
    <cbc:Floor>4</cbc:Floor>
    <cbc:StreetName>CALLE SERPIS</cbc:StreetName>
    <cbc:CityName>VALENCIA</cbc:CityName>
    <cbc:PostalZone>460019</cbc:PostalZone>
    <cac:AddressLine>
      <cbc:Line>Calle Serpis 64</cbc:Line>
    </cac:AddressLine>
  </cac:Address>
</cac:ToLocation>
```

**Structure 38** — 1 instance

```xml
<cac:ToLocation>
  <cbc:ID>43125678</cbc:ID>
  <cbc:LocationTypeCode>Place of delivery</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:StreetName>Heissestrasse 45</cbc:StreetName>
    <cbc:CityName>Munich</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:ToLocation>
```

**Structure 39** — 2 instances

```xml
<cac:ToLocation>
  <cbc:LocationTypeCode>7</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
    <cbc:CityName>Nurnberg</cbc:CityName>
    <cbc:PostalZone>28400</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:ToLocation>
```

**Structure 40** — 1 instance

```xml
<cac:FromLocation>
  <cac:Address>
    <cbc:Floor>1</cbc:Floor>
    <cbc:StreetName>AVD BLASCO IBANEZ</cbc:StreetName>
    <cbc:CityName>VALENCIA</cbc:CityName>
    <cbc:PostalZone>460019</cbc:PostalZone>
    <cac:AddressLine>
      <cbc:Line>AVD BLASCO IBANEZ 36</cbc:Line>
    </cac:AddressLine>
  </cac:Address>
</cac:FromLocation>
```

**Structure 41** — 1 instance

```xml
<cac:FromLocation>
  <cbc:ID>123465</cbc:ID>
  <cbc:LocationTypeCode>Place of despatch</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:StreetName>Jordbærstien 2</cbc:StreetName>
    <cbc:CityName>Hamar</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>NO</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:FromLocation>
```

**Structure 42** — 2 instances

```xml
<cac:StatusLocation>
  <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:ID>4568763527610</cbc:ID>
    <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
    <cbc:CityName>Bremen</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:StatusLocation>
```

**Structure 43** — 2 instances

```xml
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
```

**Structure 44** — 4 instances

```xml
<cac:Location>
  <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:ID>4568763527610</cbc:ID>
    <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
    <cbc:CityName>Bremen</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 45** — 3 instances

```xml
<cac:Location>
  <cac:Address>
    <cbc:ID>DEHAM</cbc:ID>
    <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
    <cbc:CityName>Hamburg</cbc:CityName>
    <cbc:PostalZone>29400</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 46** — 4 instances

```xml
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
```

**Structure 47** — 1 instance

```xml
<cac:LastExitPortLocation>
  <cbc:Description>ART INTERNATIONAL ZURICH 2019</cbc:Description>
  <cac:Address>
    <cbc:StreetName>Giessereistrasse</cbc:StreetName>
    <cbc:BuildingNumber>18</cbc:BuildingNumber>
    <cbc:CityName>Zürich</cbc:CityName>
    <cbc:PostalZone>CH-8005</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:LastExitPortLocation>
```

**Structure 48** — 2 instances

```xml
<cac:ActivityOriginLocation>
  <cac:Address>
    <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
    <cbc:BuildingNumber>403</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40129</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:Address>
</cac:ActivityOriginLocation>
```

**Structure 49** — 2 instances

```xml
<cac:FromLocation>
  <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:ID>DEHAM</cbc:ID>
    <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
    <cbc:CityName>Hamburg</cbc:CityName>
    <cbc:PostalZone>29400</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:FromLocation>
```

**Structure 50** — 3 instances

```xml
<cac:Location>
  <cbc:ID>987456123</cbc:ID>
  <cbc:LocationTypeCode>Place of transhipment</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:StreetName>Volkerstrasse 6</cbc:StreetName>
    <cbc:CityName>Munich</cbc:CityName>
    <cbc:PostalZone>80334</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 51** — 3 instances

```xml
<cac:Location>
  <cbc:ID>DEBREV</cbc:ID>
  <cbc:Description>Port of Bremerhaven</cbc:Description>
  <cbc:LocationTypeCode>34</cbc:LocationTypeCode>
  <cac:Address>
    <cbc:StreetName>Hansestadt Bremisches</cbc:StreetName>
    <cbc:CityName>Bremen</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:Location>
```

**Structure 52** — 2 instances

```xml
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
```

**Structure 53** — 1 instance

```xml
<cac:ActivityOriginLocation>
  <cbc:Description>Shop in the city center</cbc:Description>
  <cac:Address>
    <cbc:StreetName>Via Rizzoli</cbc:StreetName>
    <cbc:BuildingNumber>208</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40121</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:Address>
</cac:ActivityOriginLocation>
```

**Structure 54** — 2 instances

```xml
<cac:ActivityFinalLocation>
  <cbc:Description>Shop in the city center</cbc:Description>
  <cac:Address>
    <cbc:StreetName>Via Rizzoli</cbc:StreetName>
    <cbc:BuildingNumber>208</cbc:BuildingNumber>
    <cbc:CityName>Bologna</cbc:CityName>
    <cbc:PostalZone>40121</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      <cbc:Name>Italy</cbc:Name>
    </cac:Country>
  </cac:Address>
</cac:ActivityFinalLocation>
```

**Structure 55** — 2 instances

```xml
<cac:DeliveryLocation>
  <cbc:ID>6754238987648</cbc:ID>
  <cac:Address>
    <cbc:StreetName>Deliverystreet</cbc:StreetName>
    <cbc:AdditionalStreetName>Side door</cbc:AdditionalStreetName>
    <cbc:BuildingNumber>12</cbc:BuildingNumber>
    <cbc:CityName>DeliveryCity</cbc:CityName>
    <cbc:PostalZone>523427</cbc:PostalZone>
    <cbc:CountrySubentity>RegionC</cbc:CountrySubentity>
    <cac:Country>
      <cbc:IdentificationCode>BE</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:DeliveryLocation>
```

**Structure 56** — 1 instance

```xml
<cac:Location>
  <cbc:ID>M165</cbc:ID>
  <cac:Address>
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
  </cac:Address>
</cac:Location>
```

**Structure 57** — 1 instance

```xml
<cac:PointOfSaleLocation>
  <cbc:ID>37</cbc:ID>
  <cbc:Description>Shop number #37 at H.C. Andersens Boulevard, Copenhagen</cbc:Description>
  <cbc:Name>Shop 37</cbc:Name>
  <cac:Address>
    <cbc:StreetName>Hans Christian Andersens Boulevard</cbc:StreetName>
    <cbc:BuildingNumber>777</cbc:BuildingNumber>
    <cbc:CityName>Copenhagen</cbc:CityName>
    <cbc:PostalZone>1234</cbc:PostalZone>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    </cac:Country>
  </cac:Address>
</cac:PointOfSaleLocation>
```

**Structure 58** — 2 instances

```xml
<cac:DeliveryLocation>
  <cac:Address>
    <cbc:ID>1234567890123</cbc:ID>
    <cbc:Postbox>123</cbc:Postbox>
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
  </cac:Address>
</cac:DeliveryLocation>
```

**Structure 59** — 1 instance

```xml
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
```

**Structure 60** — 1 instance

```xml
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
```

**Structure 61** — 1 instance

```xml
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
```

**Structure 62** — 1 instance

```xml
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
      <cbc:Name>Germany</cbc:Name>
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
```

[↑ Back to contents](#contents)

### `LotIdentificationType`

**Used as:** `cac:LotIdentification`

_33 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:LotIdentification>
  <cbc:LotNumberID>9390000757</cbc:LotNumberID>
</cac:LotIdentification>
```

**Structure 2** — 32 instances

```xml
<cac:LotIdentification>
  <cbc:LotNumberID>546378239</cbc:LotNumberID>
  <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
</cac:LotIdentification>
```

[↑ Back to contents](#contents)

### `MaritimeTransportType`

**Used as:** `cac:MaritimeTransport`

_5 instances across 1 element, with 2 unique structures_

**Structure 1** — 2 instances

```xml
<cac:MaritimeTransport>
  <cbc:VesselID>Eestiship</cbc:VesselID>
</cac:MaritimeTransport>
```

**Structure 2** — 3 instances

```xml
<cac:MaritimeTransport>
  <cbc:VesselID>IMO1234567</cbc:VesselID>
  <cbc:VesselName>MS Enova</cbc:VesselName>
</cac:MaritimeTransport>
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

### `MonetaryTotalType`

**Used as:** `cac:AnticipatedMonetaryTotal` · `cac:LegalMonetaryTotal` · `cac:QuotedMonetaryTotal` · `cac:RequestedMonetaryTotal`

_45 instances across 4 elements, with 10 unique structures_

**Structure 1** — 1 instance

```xml
<cac:LegalMonetaryTotal>
  <cbc:PayableAmount>100.00</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

**Structure 2** — 7 instances

```xml
<cac:AnticipatedMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:PayableAmount>100.00</cbc:PayableAmount>
</cac:AnticipatedMonetaryTotal>
```

**Structure 3** — 4 instances

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

**Structure 4** — 4 instances

```xml
<cac:QuotedMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:QuotedMonetaryTotal>
```

**Structure 5** — 17 instances

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:AllowanceTotalAmount>10.00</cbc:AllowanceTotalAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

**Structure 6** — 2 instances

```xml
<cac:AnticipatedMonetaryTotal>
  <cbc:LineExtensionAmount>6225</cbc:LineExtensionAmount>
  <cbc:AllowanceTotalAmount>100</cbc:AllowanceTotalAmount>
  <cbc:ChargeTotalAmount>100</cbc:ChargeTotalAmount>
  <cbc:PayableAmount>6225</cbc:PayableAmount>
</cac:AnticipatedMonetaryTotal>
```

**Structure 7** — 1 instance

```xml
<cac:QuotedMonetaryTotal>
  <cbc:LineExtensionAmount>197750.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>49437.50</cbc:TaxExclusiveAmount>
  <cbc:TaxInclusiveAmount>247187.50</cbc:TaxInclusiveAmount>
  <cbc:PayableAmount>247187.50</cbc:PayableAmount>
</cac:QuotedMonetaryTotal>
```

**Structure 8** — 2 instances

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>200.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>205.00</cbc:TaxExclusiveAmount>
  <cbc:TaxInclusiveAmount>247.55</cbc:TaxInclusiveAmount>
  <cbc:AllowanceTotalAmount>5.00</cbc:AllowanceTotalAmount>
  <cbc:ChargeTotalAmount>10.00</cbc:ChargeTotalAmount>
  <cbc:PayableAmount>247.55</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

**Structure 9** — 6 instances

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>1436.5</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>1436.5</cbc:TaxExclusiveAmount>
  <cbc:TaxInclusiveAmount>1729</cbc:TaxInclusiveAmount>
  <cbc:AllowanceTotalAmount>100</cbc:AllowanceTotalAmount>
  <cbc:ChargeTotalAmount>100</cbc:ChargeTotalAmount>
  <cbc:PrepaidAmount>1000</cbc:PrepaidAmount>
  <cbc:PayableRoundingAmount>0.30</cbc:PayableRoundingAmount>
  <cbc:PayableAmount>729</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

**Structure 10** — 1 instance

```xml
<cac:RequestedMonetaryTotal>
  <cbc:LineExtensionAmount>1436.5</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>1436.5</cbc:TaxExclusiveAmount>
  <cbc:TaxInclusiveAmount>1729</cbc:TaxInclusiveAmount>
  <cbc:AllowanceTotalAmount>100</cbc:AllowanceTotalAmount>
  <cbc:ChargeTotalAmount>100</cbc:ChargeTotalAmount>
  <cbc:PrepaidAmount>1000</cbc:PrepaidAmount>
  <cbc:PayableRoundingAmount>0.30</cbc:PayableRoundingAmount>
  <cbc:PayableAmount>729</cbc:PayableAmount>
</cac:RequestedMonetaryTotal>
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

### `OrderLineReferenceType`

**Used as:** `cac:OrderLineReference`

_38 instances across 1 element, with 3 unique structures_

**Structure 1** — 15 instances

```xml
<cac:OrderLineReference>
  <cbc:LineID>5</cbc:LineID>
</cac:OrderLineReference>
```

**Structure 2** — 5 instances

```xml
<cac:OrderLineReference>
  <cbc:LineID>1</cbc:LineID>
  <cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
  <cac:OrderReference>
    <cbc:ID>AEG012345</cbc:ID>
    <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
    <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
    <cbc:IssueDate>2005-06-20</cbc:IssueDate>
  </cac:OrderReference>
</cac:OrderLineReference>
```

**Structure 3** — 18 instances

```xml
<cac:OrderLineReference>
  <cbc:LineID>1</cbc:LineID>
  <cbc:SalesOrderLineID>A</cbc:SalesOrderLineID>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cac:OrderReference>
    <cbc:ID>AEG012345</cbc:ID>
    <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
    <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
    <cbc:IssueDate>2005-06-20</cbc:IssueDate>
  </cac:OrderReference>
</cac:OrderLineReference>
```

[↑ Back to contents](#contents)

### `OrderLineType`

**Used as:** `cac:OrderLine`

_20 instances across 1 element, with 6 unique structures_

**Structure 1** — 2 instances

```xml
<cac:OrderLine>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cac:Item></cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

**Structure 2** — 4 instances

```xml
<cac:OrderLine>
  <cac:LineItem>
    <cbc:ID>2</cbc:ID>
    <cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
    <cac:Item>
      <cbc:Description>Very good pencils for red paint.</cbc:Description>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

**Structure 3** — 3 instances

```xml
<cac:OrderLine>
  <cbc:Note>this is an illustrative order line</cbc:Note>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:SalesOrderID>A</cbc:SalesOrderID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cbc:Quantity>100</cbc:Quantity>
    <cbc:LineExtensionAmount>1000.00</cbc:LineExtensionAmount>
    <cac:Price>
      <cbc:PriceAmount>10.00</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Beeswax</cbc:Description>
      <cbc:Name>Acme Beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

**Structure 4** — 5 instances

```xml
<cac:OrderLine>
  <cbc:Note>this is an illustrative order line</cbc:Note>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:SalesOrderID>A</cbc:SalesOrderID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cbc:Quantity>100</cbc:Quantity>
    <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>17.50</cbc:TotalTaxAmount>
    <cac:Price>
      <cbc:PriceAmount>100.00</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Acme beeswax</cbc:Description>
      <cbc:Name>beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

**Structure 5** — 4 instances

```xml
<cac:OrderLine>
  <cbc:Note>Freetext note on line 1</cbc:Note>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity>120</cbc:Quantity>
    <cbc:LineExtensionAmount>6000</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>10</cbc:TotalTaxAmount>
    <cbc:PartialDeliveryIndicator>false</cbc:PartialDeliveryIndicator>
    <cbc:AccountingCostCode>ProjectID123</cbc:AccountingCostCode>
    <cac:Delivery>
      <cac:RequestedDeliveryPeriod>
        <cbc:StartDate>2010-02-10</cbc:StartDate>
        <cbc:EndDate>2010-02-25</cbc:EndDate>
      </cac:RequestedDeliveryPeriod>
    </cac:Delivery>
    <cac:OriginatorParty>
      <cac:PartyIdentification>
        <cbc:ID>EmployeeXXX</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Josef K.</cbc:Name>
      </cac:PartyName>
    </cac:OriginatorParty>
    <cac:Price>
      <cbc:PriceAmount>50</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Red paint</cbc:Description>
      <cbc:Name>Falu Rödfärg</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>SItemNo001</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID>1234567890123</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Paint type</cbc:Name>
        <cbc:Value>Acrylic</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Solvant</cbc:Name>
        <cbc:Value>Water</cbc:Value>
      </cac:AdditionalItemProperty>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

**Structure 6** — 2 instances

```xml
<cac:OrderLine>
  <cbc:Note>Freetext note on line 1</cbc:Note>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:LineStatusCode>Revised</cbc:LineStatusCode>
    <cbc:Quantity>240</cbc:Quantity>
    <cbc:LineExtensionAmount>12000</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>20</cbc:TotalTaxAmount>
    <cbc:PartialDeliveryIndicator>false</cbc:PartialDeliveryIndicator>
    <cbc:AccountingCostCode>ProjectID123</cbc:AccountingCostCode>
    <cac:Delivery>
      <cac:RequestedDeliveryPeriod>
        <cbc:StartDate>2010-02-10</cbc:StartDate>
        <cbc:EndDate>2010-02-25</cbc:EndDate>
      </cac:RequestedDeliveryPeriod>
    </cac:Delivery>
    <cac:OriginatorParty>
      <cac:PartyIdentification>
        <cbc:ID>EmployeeXXX</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Josef K.</cbc:Name>
      </cac:PartyName>
    </cac:OriginatorParty>
    <cac:Price>
      <cbc:PriceAmount>50</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Red paint</cbc:Description>
      <cbc:Name>Falu Rödfärg</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>SItemNo001</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID>1234567890123</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Paint type</cbc:Name>
        <cbc:Value>Acrylic</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Solvant</cbc:Name>
        <cbc:Value>Water</cbc:Value>
      </cac:AdditionalItemProperty>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

[↑ Back to contents](#contents)

### `OrderReferenceType`

**Used as:** `cac:OrderReference`

_71 instances across 1 element, with 2 unique structures_

**Structure 1** — 14 instances

```xml
<cac:OrderReference>
  <cbc:ID>123</cbc:ID>
</cac:OrderReference>
```

**Structure 2** — 57 instances

```xml
<cac:OrderReference>
  <cbc:ID>AEG012345</cbc:ID>
  <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
  <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
  <cbc:IssueDate>2005-06-20</cbc:IssueDate>
</cac:OrderReference>
```

[↑ Back to contents](#contents)

### `PackageType`

**Used as:** `cac:ActualPackage` · `cac:ContainingPackage` · `cac:Package`

_23 instances across 3 elements, with 7 unique structures_

**Structure 1** — 4 instances

```xml
<cac:ActualPackage>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:PackagingTypeCode>TB</cbc:PackagingTypeCode>
</cac:ActualPackage>
```

**Structure 2** — 6 instances

```xml
<cac:Package>
  <cbc:ID>CON_1</cbc:ID>
  <cbc:Quantity>10</cbc:Quantity>
</cac:Package>
```

**Structure 3** — 4 instances

```xml
<cac:ContainingPackage>
  <cbc:ID>YangMei</cbc:ID>
  <cbc:Quantity>1</cbc:Quantity>
  <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
</cac:ContainingPackage>
```

**Structure 4** — 2 instances

```xml
<cac:Package>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:PackagingTypeCode>PX</cbc:PackagingTypeCode>
  <cac:GoodsItem>
    <cac:Item>
      <cac:CommodityClassification>
        <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:GoodsItem>
</cac:Package>
```

**Structure 5** — 4 instances

```xml
<cac:Package>
  <cbc:ID>CON_P_1</cbc:ID>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
  <cac:GoodsItem>
    <cac:Item>
      <cac:CommodityClassification>
        <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:GoodsItem>
</cac:Package>
```

**Structure 6** — 2 instances

```xml
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
```

**Structure 7** — 1 instance

```xml
<cac:Package>
  <cbc:ID>2076084807</cbc:ID>
  <cbc:Quantity>1</cbc:Quantity>
  <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
  <cac:GoodsItem>
    <cbc:ID>000010</cbc:ID>
    <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
    <cbc:Quantity>63.000</cbc:Quantity>
    <cac:Item>
      <cbc:Description>ItemExample</cbc:Description>
      <cbc:PackQuantity>63</cbc:PackQuantity>
      <cbc:Name>Dairy Products</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>123456</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
        <cbc:Name>Denmark</cbc:Name>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode>19011000</cbc:CommodityCode>
      </cac:CommodityClassification>
      <cac:AdditionalItemProperty>
        <cbc:Name>AnimalSpecies</cbc:Name>
        <cbc:Value>Bovine</cbc:Value>
      </cac:AdditionalItemProperty>
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
      <cac:ItemInstance>
        <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
        <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>LineNetWeight</cbc:Name>
          <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>LineGrossWeight</cbc:Name>
          <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quantity</cbc:Name>
          <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>9390000757</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
      <cac:Dimension>
        <cbc:AttributeID>NetWeight</cbc:AttributeID>
        <cbc:Measure>9.6</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
        <cbc:Measure>604.8</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID>GrossWeight</cbc:AttributeID>
        <cbc:Measure>12.288</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
        <cbc:Measure>774.144</cbc:Measure>
      </cac:Dimension>
    </cac:Item>
    <cac:Despatch>
      <cbc:ID>000010</cbc:ID>
    </cac:Despatch>
    <cac:MaximumTemperature>
      <cbc:AttributeID>TC</cbc:AttributeID>
      <cbc:Measure>3.00</cbc:Measure>
      <cbc:Description>Chilled</cbc:Description>
    </cac:MaximumTemperature>
  </cac:GoodsItem>
  <cac:MeasurementDimension>
    <cbc:AttributeID>GrossWeight</cbc:AttributeID>
    <cbc:Measure>774.14400</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>NetWeight</cbc:AttributeID>
    <cbc:Measure>604.80000</cbc:Measure>
  </cac:MeasurementDimension>
</cac:Package>
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

### `PaymentMeansType`

**Used as:** `cac:PaymentMeans`

_37 instances across 1 element, with 4 unique structures_

**Structure 1** — 1 instance

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>10</cbc:PaymentMeansCode>
  <cbc:PaymentMeansDescription>Cash</cbc:PaymentMeansDescription>
  <cbc:PaymentID>1</cbc:PaymentID>
</cac:PaymentMeans>
```

**Structure 2** — 3 instances

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>31</cbc:PaymentMeansCode>
  <cbc:PaymentDueDate>2009-12-31</cbc:PaymentDueDate>
  <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
  <cbc:PaymentID>Payref1</cbc:PaymentID>
  <cac:PayeeFinancialAccount>
    <cbc:ID>DK1212341234123412</cbc:ID>
    <cac:FinancialInstitutionBranch>
      <cac:FinancialInstitution>
        <cbc:ID>DKDKABCD</cbc:ID>
      </cac:FinancialInstitution>
    </cac:FinancialInstitutionBranch>
  </cac:PayeeFinancialAccount>
</cac:PaymentMeans>
```

**Structure 3** — 5 instances

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>20</cbc:PaymentMeansCode>
  <cac:PayeeFinancialAccount>
    <cbc:ID>12345678</cbc:ID>
    <cbc:Name>Farthing Purchasing Consortia</cbc:Name>
    <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
    <cbc:CurrencyCode>GBP</cbc:CurrencyCode>
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
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PayeeFinancialAccount>
</cac:PaymentMeans>
```

**Structure 4** — 28 instances

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>20</cbc:PaymentMeansCode>
  <cbc:PaymentDueDate>2005-07-21</cbc:PaymentDueDate>
  <cac:PayeeFinancialAccount>
    <cbc:ID>12345678</cbc:ID>
    <cbc:Name>Farthing Purchasing Consortia</cbc:Name>
    <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
    <cbc:CurrencyCode>GBP</cbc:CurrencyCode>
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
    <cac:Country>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:Country>
  </cac:PayeeFinancialAccount>
</cac:PaymentMeans>
```

[↑ Back to contents](#contents)

### `PaymentTermsType`

**Used as:** `cac:PaymentTerms` · `cac:ServiceChargePaymentTerms`

_34 instances across 2 elements, with 5 unique structures_

**Structure 1** — 27 instances

```xml
<cac:PaymentTerms>
  <cbc:Note>Payable within 1 calendar month from the invoice date</cbc:Note>
</cac:PaymentTerms>
```

**Structure 2** — 4 instances

```xml
<cac:PaymentTerms>
  <cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
</cac:PaymentTerms>
```

**Structure 3** — 1 instance

```xml
<cac:ServiceChargePaymentTerms>
  <cbc:Amount>2500</cbc:Amount>
  <cbc:PaymentDueDate>2011-11-06</cbc:PaymentDueDate>
</cac:ServiceChargePaymentTerms>
```

**Structure 4** — 1 instance

```xml
<cac:PaymentTerms>
  <cbc:Note>Per thirty days</cbc:Note>
  <cbc:Note>See web site for price scheme</cbc:Note>
  <cbc:PaymentTermsDetailsURI>www.ROADCARRIER.de/prices.html</cbc:PaymentTermsDetailsURI>
</cac:PaymentTerms>
```

**Structure 5** — 1 instance

```xml
<cac:PaymentTerms>
  <cbc:Note>Per thirty days</cbc:Note>
  <cac:SettlementPeriod>
    <cbc:StartDate>2011-03-13</cbc:StartDate>
    <cbc:StartTime>14:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-04-12</cbc:EndDate>
    <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
  </cac:SettlementPeriod>
</cac:PaymentTerms>
```

[↑ Back to contents](#contents)

### `PaymentType`

**Used as:** `cac:Payment`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:Payment>
  <cbc:ID>1</cbc:ID>
  <cbc:PaidAmount>25.00</cbc:PaidAmount>
  <cbc:PaidCashAmount>30.00</cbc:PaidCashAmount>
  <cbc:CashChangeAmount>5.00</cbc:CashChangeAmount>
</cac:Payment>
```

[↑ Back to contents](#contents)

### `PerformanceDataLineType`

**Used as:** `cac:PerformanceDataLine`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:PerformanceDataLine>
  <cbc:ID>PDL_2009_01</cbc:ID>
  <cbc:PerformanceValueQuantity>120</cbc:PerformanceValueQuantity>
  <cbc:PerformanceMetricTypeCode>GROSS_MARGIN</cbc:PerformanceMetricTypeCode>
  <cac:Period>
    <cbc:StartDate>2009-01-01</cbc:StartDate>
    <cbc:EndDate>2009-07-31</cbc:EndDate>
  </cac:Period>
  <cac:Item>
    <cbc:Description>Acme knitwear scarf</cbc:Description>
    <cbc:Name>scarf</cbc:Name>
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
</cac:PerformanceDataLine>
```

[↑ Back to contents](#contents)

### `PeriodType`

**Used as:** `cac:ActivityPeriod` · `cac:AdoptionPeriod` · `cac:EffectivePeriod` · `cac:EstimatedDeliveryPeriod` · `cac:ExceptionObservationPeriod` · `cac:ForecastPeriod` · `cac:InventoryPeriod` · `cac:InvoicePeriod` · `cac:Period` · `cac:RequestedDeliveryPeriod` · `cac:ServiceAvailabilityPeriod` · `cac:ServiceEndTimePeriod` · `cac:ServiceMaintenancePeriod` · `cac:ServiceStartTimePeriod` · `cac:SettlementPeriod` · `cac:StatementPeriod` · `cac:TransitPeriod` · `cac:TransportServiceProviderResponseDeadlinePeriod` · `cac:TransportUserResponseRequiredPeriod` · `cac:ValidityPeriod`

_213 instances across 20 elements, with 30 unique structures_

**Structure 1** — 4 instances

```xml
<cac:ValidityPeriod>
  <cbc:EndDate>1967-08-13</cbc:EndDate>
</cac:ValidityPeriod>
```

**Structure 2** — 2 instances

```xml
<cac:Period>
  <cbc:StartDate>2017-03-30</cbc:StartDate>
</cac:Period>
```

**Structure 3** — 2 instances

```xml
<cac:ActivityPeriod>
  <cbc:StartDate>2010-04-07</cbc:StartDate>
</cac:ActivityPeriod>
```

**Structure 4** — 4 instances

```xml
<cac:AdoptionPeriod>
  <cbc:DurationMeasure>90</cbc:DurationMeasure>
</cac:AdoptionPeriod>
```

**Structure 5** — 8 instances

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2010-02-10</cbc:StartDate>
  <cbc:EndDate>2010-02-25</cbc:EndDate>
</cac:RequestedDeliveryPeriod>
```

**Structure 6** — 15 instances

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2005-06-20</cbc:StartDate>
  <cbc:EndDate>2005-07-20</cbc:EndDate>
</cac:ValidityPeriod>
```

**Structure 7** — 12 instances

```xml
<cac:InvoicePeriod>
  <cbc:StartDate>2009-11-01</cbc:StartDate>
  <cbc:EndDate>2009-11-30</cbc:EndDate>
</cac:InvoicePeriod>
```

**Structure 8** — 4 instances

```xml
<cac:TransitPeriod>
  <cbc:StartDate>2005-06-25</cbc:StartDate>
  <cbc:StartTime>23:20:00.0Z</cbc:StartTime>
</cac:TransitPeriod>
```

**Structure 9** — 4 instances

```xml
<cac:EstimatedDeliveryPeriod>
  <cbc:StartDate>2005-06-30</cbc:StartDate>
  <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
</cac:EstimatedDeliveryPeriod>
```

**Structure 10** — 11 instances

```xml
<cac:EffectivePeriod>
  <cbc:StartDate>2010-03-28</cbc:StartDate>
  <cbc:EndDate>2010-08-29</cbc:EndDate>
</cac:EffectivePeriod>
```

**Structure 11** — 8 instances

```xml
<cac:ExceptionObservationPeriod>
  <cbc:StartDate>2010-03-26</cbc:StartDate>
  <cbc:EndDate>2010-04-10</cbc:EndDate>
</cac:ExceptionObservationPeriod>
```

**Structure 12** — 14 instances

```xml
<cac:ForecastPeriod>
  <cbc:StartDate>2010-02-01</cbc:StartDate>
  <cbc:EndDate>2010-05-26</cbc:EndDate>
</cac:ForecastPeriod>
```

**Structure 13** — 19 instances

```xml
<cac:Period>
  <cbc:StartDate>2005-02-26</cbc:StartDate>
  <cbc:EndDate>2005-12-26</cbc:EndDate>
</cac:Period>
```

**Structure 14** — 4 instances

```xml
<cac:ActivityPeriod>
  <cbc:StartDate>2005-02-26</cbc:StartDate>
  <cbc:EndDate>2005-12-26</cbc:EndDate>
</cac:ActivityPeriod>
```

**Structure 15** — 2 instances

```xml
<cac:ServiceEndTimePeriod>
  <cbc:EndDate>2011-10-06</cbc:EndDate>
  <cbc:EndTime>16:00:10+01:00</cbc:EndTime>
</cac:ServiceEndTimePeriod>
```

**Structure 16** — 1 instance

```xml
<cac:TransportUserResponseRequiredPeriod>
  <cbc:EndDate>2011-09-13</cbc:EndDate>
  <cbc:EndTime>12:00:10+01:00</cbc:EndTime>
</cac:TransportUserResponseRequiredPeriod>
```

**Structure 17** — 1 instance

```xml
<cac:TransportServiceProviderResponseDeadlinePeriod>
  <cbc:EndDate>2011-09-13</cbc:EndDate>
  <cbc:EndTime>11:00:10+01:00</cbc:EndTime>
</cac:TransportServiceProviderResponseDeadlinePeriod>
```

**Structure 18** — 8 instances

```xml
<cac:ServiceAvailabilityPeriod>
  <cbc:StartTime>09:00:00</cbc:StartTime>
  <cbc:EndTime>16:00:00</cbc:EndTime>
</cac:ServiceAvailabilityPeriod>
```

**Structure 19** — 8 instances

```xml
<cac:ServiceMaintenancePeriod>
  <cbc:StartTime>22:00:00Z</cbc:StartTime>
  <cbc:EndTime>06:00:00Z</cbc:EndTime>
</cac:ServiceMaintenancePeriod>
```

**Structure 20** — 1 instance

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2011-09-12</cbc:StartDate>
  <cbc:EndDate>2011-09-30</cbc:EndDate>
  <cbc:EndTime>16:00:00+01:00</cbc:EndTime>
</cac:ValidityPeriod>
```

**Structure 21** — 5 instances

```xml
<cac:StatementPeriod>
  <cbc:StartDate>2005-07-01</cbc:StartDate>
  <cbc:EndDate>2005-07-31</cbc:EndDate>
  <cbc:Description>July</cbc:Description>
</cac:StatementPeriod>
```

**Structure 22** — 4 instances

```xml
<cac:InventoryPeriod>
  <cbc:StartDate>2010-04-11</cbc:StartDate>
  <cbc:StartTime>08:00:00</cbc:StartTime>
  <cbc:EndDate>2011-04-11</cbc:EndDate>
</cac:InventoryPeriod>
```

**Structure 23** — 34 instances

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2005-06-20</cbc:StartDate>
  <cbc:StartTime>10:30:47.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-21</cbc:EndDate>
  <cbc:EndTime>10:30:47.0Z</cbc:EndTime>
</cac:RequestedDeliveryPeriod>
```

**Structure 24** — 4 instances

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2005-06-25</cbc:StartDate>
  <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-30</cbc:EndDate>
  <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
</cac:ValidityPeriod>
```

**Structure 25** — 4 instances

```xml
<cac:TransitPeriod>
  <cbc:StartDate>2005-06-25</cbc:StartDate>
  <cbc:StartTime>11:35:00.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-25</cbc:EndDate>
  <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
</cac:TransitPeriod>
```

**Structure 26** — 2 instances

```xml
<cac:EstimatedDeliveryPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>21:00:00.0Z</cbc:EndTime>
</cac:EstimatedDeliveryPeriod>
```

**Structure 27** — 23 instances

```xml
<cac:Period>
  <cbc:StartDate>2011-10-03</cbc:StartDate>
  <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-03</cbc:EndDate>
  <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
</cac:Period>
```

**Structure 28** — 2 instances

```xml
<cac:ServiceStartTimePeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:ServiceStartTimePeriod>
```

**Structure 29** — 2 instances

```xml
<cac:ServiceEndTimePeriod>
  <cbc:StartDate>2011-03-17</cbc:StartDate>
  <cbc:StartTime>15:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-17</cbc:EndDate>
  <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
</cac:ServiceEndTimePeriod>
```

**Structure 30** — 1 instance

```xml
<cac:SettlementPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>14:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-04-12</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:SettlementPeriod>
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

### `PickupType`

**Used as:** `cac:Pickup`

_6 instances across 1 element, with 2 unique structures_

**Structure 1** — 2 instances

```xml
<cac:Pickup>
  <cbc:LatestPickupDate>2016-08-02</cbc:LatestPickupDate>
</cac:Pickup>
```

**Structure 2** — 4 instances

```xml
<cac:Pickup>
  <cac:PickupLocation>
    <cbc:ID>01530</cbc:ID>
    <cbc:LocationTypeCode>P</cbc:LocationTypeCode>
  </cac:PickupLocation>
</cac:Pickup>
```

[↑ Back to contents](#contents)

### `PriceType`

**Used as:** `cac:Price`

_79 instances across 1 element, with 4 unique structures_

**Structure 1** — 2 instances

```xml
<cac:Price>
  <cbc:PriceAmount>120.00</cbc:PriceAmount>
</cac:Price>
```

**Structure 2** — 63 instances

```xml
<cac:Price>
  <cbc:PriceAmount>50</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

**Structure 3** — 2 instances

```xml
<cac:Price>
  <cbc:PriceAmount>16.00</cbc:PriceAmount>
  <cbc:TaxInclusivePriceAmount>20.00</cbc:TaxInclusivePriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

**Structure 4** — 12 instances

```xml
<cac:Price>
  <cbc:PriceAmount>1273</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
    <cbc:Amount>225</cbc:Amount>
    <cbc:BaseAmount>1500</cbc:BaseAmount>
  </cac:AllowanceCharge>
</cac:Price>
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

### `PromotionalEventLineItemType`

**Used as:** `cac:PromotionalEventLineItem`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:PromotionalEventLineItem>
  <cbc:Amount>100.0</cbc:Amount>
  <cac:EventLineItem>
    <cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
    <cac:ParticipatingLocationsLocation>
      <cbc:ID>ACME_BR_BE_0023</cbc:ID>
    </cac:ParticipatingLocationsLocation>
    <cac:RetailPlannedImpact>
      <cbc:Amount>0.0</cbc:Amount>
      <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
      <cbc:ForecastTypeCode>PROMOTIONAL</cbc:ForecastTypeCode>
      <cac:Period>
        <cbc:StartDate>2010-05-12</cbc:StartDate>
        <cbc:EndDate>2010-06-12</cbc:EndDate>
      </cac:Period>
    </cac:RetailPlannedImpact>
    <cac:SupplyItem>
      <cbc:Description>Acme knitwear scarf</cbc:Description>
      <cbc:Name>scarf</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID>00123450000584</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:SupplyItem>
  </cac:EventLineItem>
</cac:PromotionalEventLineItem>
```

[↑ Back to contents](#contents)

### `PromotionalEventType`

**Used as:** `cac:PromotionalEvent`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:PromotionalEvent>
  <cbc:PromotionalEventTypeCode>STORE_OPENING</cbc:PromotionalEventTypeCode>
  <cbc:SubmissionDate>2009-12-01</cbc:SubmissionDate>
  <cbc:LatestProposalAcceptanceDate>2010-01-06</cbc:LatestProposalAcceptanceDate>
  <cac:PromotionalSpecification>
    <cbc:SpecificationID>ACME_STROP_0023823</cbc:SpecificationID>
    <cac:PromotionalEventLineItem>
      <cbc:Amount>100.0</cbc:Amount>
      <cac:EventLineItem>
        <cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
        <cac:ParticipatingLocationsLocation>
          <cbc:ID>ACME_BR_BE_0023</cbc:ID>
        </cac:ParticipatingLocationsLocation>
        <cac:RetailPlannedImpact>
          <cbc:Amount>0.0</cbc:Amount>
          <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
          <cbc:ForecastTypeCode>PROMOTIONAL</cbc:ForecastTypeCode>
          <cac:Period>
            <cbc:StartDate>2010-05-12</cbc:StartDate>
            <cbc:EndDate>2010-06-12</cbc:EndDate>
          </cac:Period>
        </cac:RetailPlannedImpact>
        <cac:SupplyItem>
          <cbc:Description>Acme knitwear scarf</cbc:Description>
          <cbc:Name>scarf</cbc:Name>
          <cac:BuyersItemIdentification>
            <cbc:ID>6578489</cbc:ID>
          </cac:BuyersItemIdentification>
          <cac:SellersItemIdentification>
            <cbc:ID>17589683</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID>00123450000584</cbc:ID>
          </cac:StandardItemIdentification>
        </cac:SupplyItem>
      </cac:EventLineItem>
    </cac:PromotionalEventLineItem>
    <cac:EventTactic>
      <cac:EventTacticEnumeration>
        <cbc:DisplayTacticTypeCode>DISPLAY_GENERAL</cbc:DisplayTacticTypeCode>
      </cac:EventTacticEnumeration>
      <cac:Period>
        <cbc:StartDate>2010-04-01</cbc:StartDate>
        <cbc:EndDate>2010-06-12</cbc:EndDate>
      </cac:Period>
    </cac:EventTactic>
  </cac:PromotionalSpecification>
</cac:PromotionalEvent>
```

[↑ Back to contents](#contents)

### `PromotionalSpecificationType`

**Used as:** `cac:PromotionalSpecification`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:PromotionalSpecification>
  <cbc:SpecificationID>ACME_STROP_0023823</cbc:SpecificationID>
  <cac:PromotionalEventLineItem>
    <cbc:Amount>100.0</cbc:Amount>
    <cac:EventLineItem>
      <cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
      <cac:ParticipatingLocationsLocation>
        <cbc:ID>ACME_BR_BE_0023</cbc:ID>
      </cac:ParticipatingLocationsLocation>
      <cac:RetailPlannedImpact>
        <cbc:Amount>0.0</cbc:Amount>
        <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
        <cbc:ForecastTypeCode>PROMOTIONAL</cbc:ForecastTypeCode>
        <cac:Period>
          <cbc:StartDate>2010-05-12</cbc:StartDate>
          <cbc:EndDate>2010-06-12</cbc:EndDate>
        </cac:Period>
      </cac:RetailPlannedImpact>
      <cac:SupplyItem>
        <cbc:Description>Acme knitwear scarf</cbc:Description>
        <cbc:Name>scarf</cbc:Name>
        <cac:BuyersItemIdentification>
          <cbc:ID>6578489</cbc:ID>
        </cac:BuyersItemIdentification>
        <cac:SellersItemIdentification>
          <cbc:ID>17589683</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID>00123450000584</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:SupplyItem>
    </cac:EventLineItem>
  </cac:PromotionalEventLineItem>
  <cac:EventTactic>
    <cac:EventTacticEnumeration>
      <cbc:DisplayTacticTypeCode>DISPLAY_GENERAL</cbc:DisplayTacticTypeCode>
    </cac:EventTacticEnumeration>
    <cac:Period>
      <cbc:StartDate>2010-04-01</cbc:StartDate>
      <cbc:EndDate>2010-06-12</cbc:EndDate>
    </cac:Period>
  </cac:EventTactic>
</cac:PromotionalSpecification>
```

[↑ Back to contents](#contents)

### `PurchaseReceiptLineType`

**Used as:** `cac:PurchaseReceiptLine`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:PurchaseReceiptLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>1</cbc:Quantity>
  <cbc:LineExtensionAmount>16.00</cbc:LineExtensionAmount>
  <cbc:TaxInclusiveLineExtensionAmount>20.00</cbc:TaxInclusiveLineExtensionAmount>
  <cac:TaxTotal>
    <cbc:TaxAmount>4.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount>16.00</cbc:TaxableAmount>
      <cbc:TaxAmount>4.00</cbc:TaxAmount>
      <cbc:TaxInclusiveAmount>20.00</cbc:TaxInclusiveAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>25</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Philosophical lamp</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>PL001</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>16.00</cbc:PriceAmount>
    <cbc:TaxInclusivePriceAmount>20.00</cbc:TaxInclusivePriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:PurchaseReceiptLine>
```

**Structure 2** — 1 instance

```xml
<cac:PurchaseReceiptLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Quantity>1</cbc:Quantity>
  <cbc:LineExtensionAmount>7.20</cbc:LineExtensionAmount>
  <cbc:TaxInclusiveLineExtensionAmount>9.00</cbc:TaxInclusiveLineExtensionAmount>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Discount</cbc:AllowanceChargeReason>
    <cbc:Amount>4.80</cbc:Amount>
    <cbc:TaxInclusiveAmount>6.00</cbc:TaxInclusiveAmount>
  </cac:AllowanceCharge>
  <cac:TaxTotal>
    <cbc:TaxAmount>1.80</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount>7.20</cbc:TaxableAmount>
      <cbc:TaxAmount>1.80</cbc:TaxAmount>
      <cbc:TaxInclusiveAmount>9.00</cbc:TaxInclusiveAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>25</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:Item>
    <cbc:Name>Magic cloak</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>MC002</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>12.00</cbc:PriceAmount>
    <cbc:TaxInclusivePriceAmount>15.00</cbc:TaxInclusivePriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
</cac:PurchaseReceiptLine>
```

[↑ Back to contents](#contents)

### `PurchaseReferenceType`

**Used as:** `cac:PurchaseReference`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:PurchaseReference>
  <cbc:ID>321987</cbc:ID>
  <cbc:Description>Customer Loyalty Number</cbc:Description>
</cac:PurchaseReference>
```

[↑ Back to contents](#contents)

### `QuotationLineType`

**Used as:** `cac:QuotationLine`

_9 instances across 1 element, with 2 unique structures_

**Structure 1** — 4 instances

```xml
<cac:QuotationLine>
  <cbc:ID>3</cbc:ID>
  <cbc:Note>Mus</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL2367452</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cbc:LineExtensionAmount>1750.00</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>437.50</cbc:TotalTaxAmount>
    <cac:Price>
      <cbc:PriceAmount>50.00</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Mus</cbc:Description>
      <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:QuotationLine>
```

**Structure 2** — 5 instances

```xml
<cac:QuotationLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>sample</cbc:Note>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity>100</cbc:Quantity>
    <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>17.50</cbc:TotalTaxAmount>
    <cac:Price>
      <cbc:PriceAmount>100.00</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Acme beeswax</cbc:Description>
      <cbc:Name>beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:LineItem>
</cac:QuotationLine>
```

[↑ Back to contents](#contents)

### `RailTransportType`

**Used as:** `cac:RailTransport`

_5 instances across 1 element, with 2 unique structures_

**Structure 1** — 3 instances

```xml
<cac:RailTransport>
  <cbc:TrainID>RID01235</cbc:TrainID>
</cac:RailTransport>
```

**Structure 2** — 2 instances

```xml
<cac:RailTransport>
  <cbc:TrainID>101</cbc:TrainID>
  <cbc:RailCarID>101-21</cbc:RailCarID>
</cac:RailTransport>
```

[↑ Back to contents](#contents)

### `ReceiptLineType`

**Used as:** `cac:ReceiptLine`

_5 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:ReceiptLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>SAMPLE</cbc:Note>
  <cbc:ReceivedQuantity>90</cbc:ReceivedQuantity>
  <cbc:ShortQuantity>10</cbc:ShortQuantity>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:LotIdentification>
      <cbc:LotNumberID>546378239</cbc:LotNumberID>
      <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
    </cac:LotIdentification>
  </cac:Item>
</cac:ReceiptLine>
```

**Structure 2** — 4 instances

```xml
<cac:ReceiptLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>SAMPLE</cbc:Note>
  <cbc:ReceivedQuantity>90</cbc:ReceivedQuantity>
  <cbc:ShortQuantity>10</cbc:ShortQuantity>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:ItemInstance>
      <cac:LotIdentification>
        <cbc:LotNumberID>546378239</cbc:LotNumberID>
        <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
      </cac:LotIdentification>
    </cac:ItemInstance>
  </cac:Item>
</cac:ReceiptLine>
```

[↑ Back to contents](#contents)

### `ReminderLineType`

**Used as:** `cac:ReminderLine`

_1 instances across 1 element, with 1 unique structure_

**Structure 1** — 1 instance

```xml
<cac:ReminderLine>
  <cbc:ID>1</cbc:ID>
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>TOSL108</cbc:ID>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
</cac:ReminderLine>
```

[↑ Back to contents](#contents)

### `RemittanceAdviceLineType`

**Used as:** `cac:RemittanceAdviceLine`

_5 instances across 1 element, with 1 unique structure_

**Structure 1** — 5 instances

```xml
<cac:RemittanceAdviceLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>please note that local offices will close for recess for the next three weeks - please send their invoices to central offices for that time</cbc:Note>
  <cbc:DebitLineAmount>107.50</cbc:DebitLineAmount>
  <cbc:CreditLineAmount>0.00</cbc:CreditLineAmount>
  <cbc:BalanceAmount>107.50</cbc:BalanceAmount>
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
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>A00095678</cbc:ID>
      <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
      <cbc:IssueDate>2005-06-21</cbc:IssueDate>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
</cac:RemittanceAdviceLine>
```

[↑ Back to contents](#contents)

### `RequestForQuotationLineType`

**Used as:** `cac:RequestForQuotationLine`

_9 instances across 1 element, with 2 unique structures_

**Structure 1** — 4 instances

```xml
<cac:RequestForQuotationLine>
  <cbc:ID>3</cbc:ID>
  <cbc:Note>Mus</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL2367452</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Mus</cbc:Description>
      <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:RequestForQuotationLine>
```

**Structure 2** — 5 instances

```xml
<cac:RequestForQuotationLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>sample</cbc:Note>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity>100</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Acme beeswax</cbc:Description>
      <cbc:Name>beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:LineItem>
</cac:RequestForQuotationLine>
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

### `RetailPlannedImpactType`

**Used as:** `cac:RetailPlannedImpact`

_3 instances across 1 element, with 1 unique structure_

**Structure 1** — 3 instances

```xml
<cac:RetailPlannedImpact>
  <cbc:Amount>0.0</cbc:Amount>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>PROMOTIONAL</cbc:ForecastTypeCode>
  <cac:Period>
    <cbc:StartDate>2010-05-12</cbc:StartDate>
    <cbc:EndDate>2010-06-12</cbc:EndDate>
  </cac:Period>
</cac:RetailPlannedImpact>
```

[↑ Back to contents](#contents)

### `RoadTransportType`

**Used as:** `cac:RoadTransport`

_10 instances across 1 element, with 1 unique structure_

**Structure 1** — 10 instances

```xml
<cac:RoadTransport>
  <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
</cac:RoadTransport>
```

[↑ Back to contents](#contents)

### `SalesItemType`

**Used as:** `cac:SalesItem`

_16 instances across 1 element, with 4 unique structures_

**Structure 1** — 4 instances

```xml
<cac:SalesItem>
  <cbc:Quantity>20</cbc:Quantity>
  <cac:Item>
    <cac:StandardItemIdentification>
      <cbc:ID>06110123456784</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:Item>
</cac:SalesItem>
```

**Structure 2** — 5 instances

```xml
<cac:SalesItem>
  <cbc:Quantity>200</cbc:Quantity>
  <cac:Item>
    <cbc:Description>shirt</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>SH009</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>DD88</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:SalesItem>
```

**Structure 3** — 4 instances

```xml
<cac:SalesItem>
  <cbc:Quantity>20</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:Name>beeswax</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578489</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589683</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:SalesItem>
```

**Structure 4** — 3 instances

```xml
<cac:SalesItem>
  <cbc:Quantity>20</cbc:Quantity>
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
</cac:SalesItem>
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

### `ShipmentStageType`

**Used as:** `cac:MainCarriageShipmentStage` · `cac:PreCarriageShipmentStage` · `cac:ShipmentStage`

_30 instances across 3 elements, with 17 unique structures_

**Structure 1** — 2 instances

```xml
<cac:MainCarriageShipmentStage>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
</cac:MainCarriageShipmentStage>
```

**Structure 2** — 2 instances

```xml
<cac:ShipmentStage>
  <cbc:TransportModeCode>4</cbc:TransportModeCode>
  <cac:TransportMeans>
    <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
  </cac:TransportMeans>
</cac:ShipmentStage>
```

**Structure 3** — 1 instance

```xml
<cac:MainCarriageShipmentStage>
  <cbc:TransportModeCode>1</cbc:TransportModeCode>
  <cac:LoadingPortLocation>
    <cbc:ID>Aarhus</cbc:ID>
  </cac:LoadingPortLocation>
  <cac:UnloadingPortLocation>
    <cbc:ID>Balboa Port</cbc:ID>
  </cac:UnloadingPortLocation>
</cac:MainCarriageShipmentStage>
```

**Structure 4** — 2 instances

```xml
<cac:ShipmentStage>
  <cbc:TransportModeCode>4</cbc:TransportModeCode>
  <cac:TransportMeans>
    <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
    <cac:AirTransport>
      <cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
    </cac:AirTransport>
  </cac:TransportMeans>
</cac:ShipmentStage>
```

**Structure 5** — 2 instances

```xml
<cac:ShipmentStage>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
  <cac:TransportMeans>
    <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
    <cac:RoadTransport>
      <cbc:LicensePlateID>PBB-123</cbc:LicensePlateID>
    </cac:RoadTransport>
  </cac:TransportMeans>
</cac:ShipmentStage>
```

**Structure 6** — 1 instance

```xml
<cac:ShipmentStage>
  <cac:UnloadingPortLocation>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode>CH</cbc:IdentificationCode>
        <cbc:Name>Swiss</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:UnloadingPortLocation>
</cac:ShipmentStage>
```

**Structure 7** — 2 instances

```xml
<cac:ShipmentStage>
  <cbc:TransportModeCode>1</cbc:TransportModeCode>
  <cac:TransportMeans>
    <cbc:JourneyID>TM1</cbc:JourneyID>
    <cbc:RegistrationNationalityID>EE</cbc:RegistrationNationalityID>
    <cac:MaritimeTransport>
      <cbc:VesselID>Eestiship</cbc:VesselID>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
</cac:ShipmentStage>
```

**Structure 8** — 1 instance

```xml
<cac:MainCarriageShipmentStage>
  <cbc:ShipmentStageTypeCode>1</cbc:ShipmentStageTypeCode>
  <cbc:TransportModeCode>1</cbc:TransportModeCode>
  <cac:TransportMeans>
    <cbc:JourneyID>00344</cbc:JourneyID>
    <cbc:RegistrationNationalityID>IT</cbc:RegistrationNationalityID>
    <cac:MaritimeTransport>
      <cbc:VesselID>3852664</cbc:VesselID>
      <cbc:VesselName>Vessel Name</cbc:VesselName>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
  <cac:EstimatedArrivalTransportEvent>
    <cbc:OccurrenceDate>2013-05-25</cbc:OccurrenceDate>
    <cbc:OccurrenceTime>18:00:00+01:00</cbc:OccurrenceTime>
    <cac:Location>
      <cbc:ID>ITGOA</cbc:ID>
      <cbc:LocationTypeCode>24</cbc:LocationTypeCode>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
  </cac:EstimatedArrivalTransportEvent>
</cac:MainCarriageShipmentStage>
```

**Structure 9** — 4 instances

```xml
<cac:ShipmentStage>
  <cbc:ID>1</cbc:ID>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
  <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
  <cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
  <cac:TransitPeriod>
    <cbc:StartDate>2005-06-25</cbc:StartDate>
    <cbc:StartTime>11:35:00.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-25</cbc:EndDate>
    <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
  </cac:TransitPeriod>
  <cac:CarrierParty>
    <cac:PartyName>
      <cbc:Name>Keep On Trucking</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Telephone>+1 36222 33847</cbc:Telephone>
    </cac:Contact>
  </cac:CarrierParty>
  <cac:TransportMeans>
    <cac:RoadTransport>
      <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
    </cac:RoadTransport>
  </cac:TransportMeans>
</cac:ShipmentStage>
```

**Structure 10** — 1 instance

```xml
<cac:ShipmentStage>
  <cbc:ID>1</cbc:ID>
  <cac:RequestedDepartureTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:ID>DEHAM</cbc:ID>
        <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
        <cbc:CityName>Hamburg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
    </cac:Period>
  </cac:RequestedDepartureTransportEvent>
  <cac:RequestedArrivalTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-06</cbc:StartDate>
      <cbc:EndDate>2011-10-06</cbc:EndDate>
    </cac:Period>
  </cac:RequestedArrivalTransportEvent>
</cac:ShipmentStage>
```

**Structure 11** — 2 instances

```xml
<cac:ShipmentStage>
  <cbc:ID>3</cbc:ID>
  <cac:PlannedDepartureTransportEvent>
    <cac:Location>
      <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-06</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-06</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDepartureTransportEvent>
  <cac:PlannedArrivalTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-06</cbc:StartDate>
      <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-06</cbc:EndDate>
      <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedArrivalTransportEvent>
</cac:ShipmentStage>
```

**Structure 12** — 1 instance

```xml
<cac:MainCarriageShipmentStage>
  <cac:PlannedDepartureTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:ID>DEHAM</cbc:ID>
        <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
        <cbc:CityName>Hamburg</cbc:CityName>
        <cbc:PostalZone>29400</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDepartureTransportEvent>
  <cac:PlannedArrivalTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cbc:PostalZone>28400</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-06</cbc:StartDate>
      <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-06</cbc:EndDate>
      <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedArrivalTransportEvent>
</cac:MainCarriageShipmentStage>
```

**Structure 13** — 4 instances

```xml
<cac:ShipmentStage>
  <cbc:ID>2</cbc:ID>
  <cbc:TransportModeCode>4</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>Plane</cbc:TransportMeansTypeCode>
  <cbc:PreCarriageIndicator>false</cbc:PreCarriageIndicator>
  <cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
  <cac:TransitPeriod>
    <cbc:StartDate>2005-06-25</cbc:StartDate>
    <cbc:StartTime>23:20:00.0Z</cbc:StartTime>
  </cac:TransitPeriod>
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
  <cac:TransportMeans>
    <cbc:JourneyID>UA 1234</cbc:JourneyID>
    <cac:AirTransport>
      <cbc:AircraftID>A-127763-747</cbc:AircraftID>
    </cac:AirTransport>
  </cac:TransportMeans>
  <cac:LoadingPortLocation>
    <cbc:ID>USBOS</cbc:ID>
    <cbc:Description>Boston Airport</cbc:Description>
  </cac:LoadingPortLocation>
  <cac:UnloadingPortLocation>
    <cbc:ID>GBBRS</cbc:ID>
    <cbc:Description>Bristol Airport</cbc:Description>
  </cac:UnloadingPortLocation>
  <cac:TransshipPortLocation>
    <cbc:ID>GBLHR</cbc:ID>
    <cbc:Description>Heathrow Apt/London</cbc:Description>
  </cac:TransshipPortLocation>
</cac:ShipmentStage>
```

**Structure 14** — 2 instances

```xml
<cac:ShipmentStage>
  <cbc:ID>2</cbc:ID>
  <cac:PlannedDepartureTransportEvent>
    <cac:Location>
      <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:ID>4568763527610</cbc:ID>
        <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
        <cbc:CityName>Bremen</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-04</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-04</cbc:EndDate>
      <cbc:EndTime>09:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDepartureTransportEvent>
  <cac:PlannedArrivalTransportEvent>
    <cac:Location>
      <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
        <cbc:CityName>Nurnberg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-04</cbc:StartDate>
      <cbc:StartTime>15:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-04</cbc:EndDate>
      <cbc:EndTime>18:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedArrivalTransportEvent>
</cac:ShipmentStage>
```

**Structure 15** — 1 instance

```xml
<cac:ShipmentStage>
  <cbc:ID>1</cbc:ID>
  <cac:PlannedDepartureTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:ID>DEHAM</cbc:ID>
        <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
        <cbc:CityName>Hamburg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDepartureTransportEvent>
  <cac:PlannedArrivalTransportEvent>
    <cac:Location>
      <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:ID>4568763527610</cbc:ID>
        <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
        <cbc:CityName>Bremen</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>21:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedArrivalTransportEvent>
</cac:ShipmentStage>
```

**Structure 16** — 1 instance

```xml
<cac:ShipmentStage>
  <cbc:ID>1</cbc:ID>
  <cbc:TransportModeCode>2</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>230</cbc:TransportMeansTypeCode>
  <cac:PlannedDepartureTransportEvent>
    <cac:Location>
      <cac:Address>
        <cbc:ID>DEHAM</cbc:ID>
        <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
        <cbc:CityName>Hamburg</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDepartureTransportEvent>
  <cac:PlannedArrivalTransportEvent>
    <cac:Location>
      <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:ID>4568763527610</cbc:ID>
        <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
        <cbc:CityName>Bremen</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>21:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedArrivalTransportEvent>
</cac:ShipmentStage>
```

**Structure 17** — 1 instance

```xml
<cac:PreCarriageShipmentStage>
  <cbc:TransportModeCode>1</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
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
  <cac:TransportMeans>
    <cbc:JourneyID>M22</cbc:JourneyID>
    <cbc:RegistrationNationalityID>DK</cbc:RegistrationNationalityID>
    <cbc:RegistrationNationality>Denmark</cbc:RegistrationNationality>
    <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
    <cac:MaritimeTransport>
      <cbc:VesselID>SomeIMONr</cbc:VesselID>
      <cbc:VesselName>SomeVesselName</cbc:VesselName>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
  <cac:PlannedDepartureTransportEvent>
    <cac:Location>
      <cbc:ID>CNSHA</cbc:ID>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-09-20</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-09-20</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedDepartureTransportEvent>
  <cac:PlannedArrivalTransportEvent>
    <cac:Location>
      <cbc:ID>DEHAM</cbc:ID>
    </cac:Location>
    <cac:Period>
      <cbc:StartDate>2011-10-01</cbc:StartDate>
      <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-01</cbc:EndDate>
      <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:PlannedArrivalTransportEvent>
</cac:PreCarriageShipmentStage>
```

[↑ Back to contents](#contents)

### `ShipmentType`

**Used as:** `cac:ConsolidatedShipment` · `cac:Shipment`

_36 instances across 2 elements, with 16 unique structures_

**Structure 1** — 4 instances

```xml
<cac:ConsolidatedShipment>
  <cbc:ID>GSIN_1</cbc:ID>
</cac:ConsolidatedShipment>
```

**Structure 2** — 1 instance

```xml
<cac:Shipment>
  <cbc:ID>123</cbc:ID>
  <cbc:GrossWeightMeasure>12</cbc:GrossWeightMeasure>
  <cbc:TotalTransportHandlingUnitQuantity>1</cbc:TotalTransportHandlingUnitQuantity>
  <cbc:SpecialInstructions>1234</cbc:SpecialInstructions>
  <cbc:DeliveryInstructions>abcd</cbc:DeliveryInstructions>
  <cac:Consignment>
    <cbc:ID>123</cbc:ID>
  </cac:Consignment>
</cac:Shipment>
```

**Structure 3** — 5 instances

```xml
<cac:Shipment>
  <cbc:ID>1</cbc:ID>
  <cac:Consignment>
    <cbc:ID>1</cbc:ID>
  </cac:Consignment>
  <cac:Delivery>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity>90</cbc:Quantity>
    <cbc:ActualDeliveryDate>2005-06-20</cbc:ActualDeliveryDate>
    <cbc:ActualDeliveryTime>11:30:00.0Z</cbc:ActualDeliveryTime>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2005-06-20</cbc:StartDate>
      <cbc:StartTime>10:30:47.0Z</cbc:StartTime>
      <cbc:EndDate>2005-06-21</cbc:EndDate>
      <cbc:EndTime>10:30:47.0Z</cbc:EndTime>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
</cac:Shipment>
```

**Structure 4** — 5 instances

```xml
<cac:Shipment>
  <cbc:ID>1</cbc:ID>
  <cac:Consignment>
    <cbc:ID>1</cbc:ID>
  </cac:Consignment>
  <cac:Delivery>
    <cac:DeliveryAddress>
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
    </cac:DeliveryAddress>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2005-06-20</cbc:StartDate>
      <cbc:StartTime>10:30:47.0Z</cbc:StartTime>
      <cbc:EndDate>2005-06-21</cbc:EndDate>
      <cbc:EndTime>10:30:47.0Z</cbc:EndTime>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
</cac:Shipment>
```

**Structure 5** — 1 instance

```xml
<cac:Shipment>
  <cbc:ID>51022</cbc:ID>
  <cac:Consignment>
    <cbc:ID>510</cbc:ID>
  </cac:Consignment>
  <cac:Delivery>
    <cac:DeliveryAddress>
      <cbc:StreetName>Via Dell'Arcoveggio</cbc:StreetName>
      <cbc:BuildingNumber>403</cbc:BuildingNumber>
      <cbc:CityName>Bologna</cbc:CityName>
      <cbc:PostalZone>40129</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        <cbc:Name>Italy</cbc:Name>
      </cac:Country>
    </cac:DeliveryAddress>
    <cac:Despatch>
      <cac:DespatchAddress>
        <cbc:StreetName>Via Emilia</cbc:StreetName>
        <cbc:BuildingNumber>1</cbc:BuildingNumber>
        <cbc:CityName>Modena</cbc:CityName>
        <cbc:PostalZone>41121</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>IT</cbc:IdentificationCode>
          <cbc:Name>Italy</cbc:Name>
        </cac:Country>
      </cac:DespatchAddress>
    </cac:Despatch>
  </cac:Delivery>
</cac:Shipment>
```

**Structure 6** — 2 instances

```xml
<cac:Shipment>
  <cbc:ID>123456</cbc:ID>
  <cac:TransportHandlingUnit>
    <cac:TransportEquipment>
      <cbc:ID>TRHU1652173</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
      <cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
      <cac:VerifiedGrossMass>
        <cbc:ID>123</cbc:ID>
        <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
        <cbc:WeighingTime>00:30:00</cbc:WeighingTime>
        <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
        <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
        <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
        <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
        <cac:DocumentReference>
          <cbc:ID>W123</cbc:ID>
          <cbc:IssueDate>2016-11-02</cbc:IssueDate>
          <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
          <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
        </cac:DocumentReference>
      </cac:VerifiedGrossMass>
    </cac:TransportEquipment>
    <cac:ShipmentDocumentReference>
      <cbc:ID>GOA294107</cbc:ID>
      <cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
    </cac:ShipmentDocumentReference>
  </cac:TransportHandlingUnit>
</cac:Shipment>
```

**Structure 7** — 1 instance

```xml
<cac:Shipment>
  <cbc:ID>123456</cbc:ID>
  <cac:TransportHandlingUnit>
    <cac:TransportEquipment>
      <cbc:ID>TRHU1652173</cbc:ID>
      <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
      <cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
      <cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
      <cac:VerifiedGrossMass>
        <cbc:ID>123</cbc:ID>
        <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
        <cbc:WeighingTime>00:30:00</cbc:WeighingTime>
        <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
        <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
        <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
        <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
        <cac:DocumentReference>
          <cbc:ID>W123</cbc:ID>
          <cbc:IssueDate>2016-11-02</cbc:IssueDate>
          <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
          <cbc:DocumentType></cbc:DocumentType>
          <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
        </cac:DocumentReference>
      </cac:VerifiedGrossMass>
    </cac:TransportEquipment>
    <cac:ShipmentDocumentReference>
      <cbc:ID>GOA294107</cbc:ID>
      <cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
    </cac:ShipmentDocumentReference>
  </cac:TransportHandlingUnit>
</cac:Shipment>
```

**Structure 8** — 2 instances

```xml
<cac:Shipment>
  <cbc:ID>S1</cbc:ID>
  <cbc:GrossWeightMeasure>30</cbc:GrossWeightMeasure>
  <cac:Consignment>
    <cbc:ID>C1</cbc:ID>
    <cbc:ContainerizedIndicator>true</cbc:ContainerizedIndicator>
    <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackagesQuantity>5</cbc:TotalPackagesQuantity>
    <cac:TransportHandlingUnit>
      <cbc:ID>ABCD123456-7</cbc:ID>
    </cac:TransportHandlingUnit>
  </cac:Consignment>
  <cac:GoodsItem>
    <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
    <cbc:Description>kattovalaisimia lasia</cbc:Description>
    <cbc:GrossWeightMeasure>30</cbc:GrossWeightMeasure>
    <cac:Pickup>
      <cac:PickupLocation>
        <cbc:ID>FI1234567-8R0001</cbc:ID>
        <cbc:LocationTypeCode>L</cbc:LocationTypeCode>
      </cac:PickupLocation>
    </cac:Pickup>
    <cac:ContainingPackage>
      <cbc:ID>567-3456</cbc:ID>
      <cbc:Quantity>5</cbc:Quantity>
      <cbc:PackagingTypeCode>CS</cbc:PackagingTypeCode>
    </cac:ContainingPackage>
  </cac:GoodsItem>
  <cac:ShipmentStage>
    <cbc:TransportModeCode>3</cbc:TransportModeCode>
    <cac:TransportMeans>
      <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
      <cac:RoadTransport>
        <cbc:LicensePlateID>PBB-123</cbc:LicensePlateID>
      </cac:RoadTransport>
    </cac:TransportMeans>
  </cac:ShipmentStage>
  <cac:ShipmentStage>
    <cbc:TransportModeCode>1</cbc:TransportModeCode>
    <cac:TransportMeans>
      <cbc:JourneyID>TM1</cbc:JourneyID>
      <cbc:RegistrationNationalityID>EE</cbc:RegistrationNationalityID>
      <cac:MaritimeTransport>
        <cbc:VesselID>Eestiship</cbc:VesselID>
      </cac:MaritimeTransport>
    </cac:TransportMeans>
  </cac:ShipmentStage>
  <cac:Delivery>
    <cac:DeliveryAddress>
      <cac:Country>
        <cbc:IdentificationCode>CH</cbc:IdentificationCode>
      </cac:Country>
    </cac:DeliveryAddress>
    <cac:Despatch>
      <cbc:ActualDespatchDate>2013-09-15</cbc:ActualDespatchDate>
      <cbc:ActualDespatchTime>16:00:00Z</cbc:ActualDespatchTime>
      <cac:DespatchAddress>
        <cac:Country>
          <cbc:IdentificationCode>RU</cbc:IdentificationCode>
        </cac:Country>
      </cac:DespatchAddress>
    </cac:Despatch>
  </cac:Delivery>
</cac:Shipment>
```

**Structure 9** — 2 instances

```xml
<cac:Shipment>
  <cbc:ID>S1</cbc:ID>
  <cbc:GrossWeightMeasure>1.5</cbc:GrossWeightMeasure>
  <cbc:DeclaredStatisticsValueAmount>250.00</cbc:DeclaredStatisticsValueAmount>
  <cac:Consignment>
    <cbc:ID>C1</cbc:ID>
    <cbc:ContainerizedIndicator>0</cbc:ContainerizedIndicator>
    <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackagesQuantity>1</cbc:TotalPackagesQuantity>
    <cac:CustomsDeclaration>
      <cbc:ID>10158209175014500</cbc:ID>
    </cac:CustomsDeclaration>
  </cac:Consignment>
  <cac:GoodsItem>
    <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
    <cbc:DeclaredStatisticsValueAmount>182.62</cbc:DeclaredStatisticsValueAmount>
    <cbc:ValueAmount>250</cbc:ValueAmount>
    <cbc:NetWeightMeasure>1</cbc:NetWeightMeasure>
    <cbc:PreferenceCriterionCode>100</cbc:PreferenceCriterionCode>
    <cbc:CustomsProcedureCode>1011</cbc:CustomsProcedureCode>
    <cac:Item>
      <cbc:Description>Kuulokkeita</cbc:Description>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode>8518309590</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
    </cac:Item>
    <cac:Pickup>
      <cac:PickupLocation>
        <cbc:ID>01530</cbc:ID>
        <cbc:LocationTypeCode>P</cbc:LocationTypeCode>
      </cac:PickupLocation>
    </cac:Pickup>
    <cac:ContainingPackage>
      <cbc:ID>YangMei</cbc:ID>
      <cbc:Quantity>1</cbc:Quantity>
      <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
    </cac:ContainingPackage>
  </cac:GoodsItem>
  <cac:ShipmentStage>
    <cbc:TransportModeCode>4</cbc:TransportModeCode>
    <cac:TransportMeans>
      <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
    </cac:TransportMeans>
  </cac:ShipmentStage>
  <cac:ShipmentStage>
    <cbc:TransportModeCode>4</cbc:TransportModeCode>
    <cac:TransportMeans>
      <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
      <cac:AirTransport>
        <cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
      </cac:AirTransport>
    </cac:TransportMeans>
  </cac:ShipmentStage>
  <cac:Delivery>
    <cac:DeliveryTerms>
      <cbc:ID>FOB</cbc:ID>
      <cac:DeliveryLocation>
        <cbc:Name>BANGKOK</cbc:Name>
      </cac:DeliveryLocation>
    </cac:DeliveryTerms>
  </cac:Delivery>
  <cac:OriginAddress>
    <cac:Country>
      <cbc:IdentificationCode>TH</cbc:IdentificationCode>
    </cac:Country>
  </cac:OriginAddress>
  <cac:FirstArrivalPortLocation>
    <cbc:ID>FI015300</cbc:ID>
  </cac:FirstArrivalPortLocation>
  <cac:ExportCountry>
    <cbc:IdentificationCode>TH</cbc:IdentificationCode>
  </cac:ExportCountry>
</cac:Shipment>
```

**Structure 10** — 2 instances

```xml
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
```

**Structure 11** — 4 instances

```xml
<cac:Shipment>
  <cbc:ID>CONS-0001</cbc:ID>
  <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
  <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
  <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
  <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
  <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
  <cbc:TotalTransportHandlingUnitQuantity>10</cbc:TotalTransportHandlingUnitQuantity>
  <cbc:InsuranceValueAmount>1000.00</cbc:InsuranceValueAmount>
  <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
  <cbc:FreeOnBoardValueAmount>1200.00</cbc:FreeOnBoardValueAmount>
  <cbc:SpecialInstructions>Beeswax becomes liquid at 50'C</cbc:SpecialInstructions>
  <cac:Consignment>
    <cbc:ID>CONS-0001</cbc:ID>
    <cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
    <cbc:TariffCode>15219000</cbc:TariffCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
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
    <cac:OriginalDepartureCountry>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:OriginalDepartureCountry>
    <cac:FinalDestinationCountry>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:FinalDestinationCountry>
    <cac:DeliveryTerms>
      <cbc:ID>FOB Destination</cbc:ID>
      <cac:DeliveryLocation>
        <cbc:ID>GBBRS</cbc:ID>
        <cbc:Description>Bristol</cbc:Description>
      </cac:DeliveryLocation>
    </cac:DeliveryTerms>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cbc:Amount>254.00</cbc:Amount>
    </cac:FreightAllowanceCharge>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
      <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
      <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
      <cbc:Amount>12.70</cbc:Amount>
      <cbc:BaseAmount>254.00</cbc:BaseAmount>
    </cac:FreightAllowanceCharge>
  </cac:Consignment>
  <cac:GoodsItem>
    <cbc:ID>1</cbc:ID>
    <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:FreeOnBoardValueAmount>1241.30</cbc:FreeOnBoardValueAmount>
    <cbc:InsuranceValueAmount>1241.30</cbc:InsuranceValueAmount>
    <cbc:ValueAmount>1000.00</cbc:ValueAmount>
    <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
    <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
    <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
    <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
    <cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
    <cbc:CustomsTariffQuantity>100</cbc:CustomsTariffQuantity>
    <cac:Item>
      <cbc:Description>Beeswax</cbc:Description>
      <cbc:Name>Acme Beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:GoodsItem>
</cac:Shipment>
```

**Structure 12** — 1 instance

```xml
<cac:Shipment>
  <cac:Consignment>
    <cbc:ID>7365566156191234567</cbc:ID>
    <cbc:GrossWeightMeasure>600</cbc:GrossWeightMeasure>
    <cbc:TotalGoodsItemQuantity>1500</cbc:TotalGoodsItemQuantity>
    <cbc:TotalTransportHandlingUnitQuantity>2</cbc:TotalTransportHandlingUnitQuantity>
    <cac:PlannedPickupTransportEvent>
      <cac:Location>
        <cbc:ID>MAPTM</cbc:ID>
        <cac:Address>
          <cbc:CityName>Tanger</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>MA</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
    </cac:PlannedPickupTransportEvent>
    <cac:PlannedDeliveryTransportEvent>
      <cac:Location>
        <cbc:ID>ITGOA</cbc:ID>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode>IT</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
    </cac:PlannedDeliveryTransportEvent>
    <cac:ConsigneeParty>
      <cac:PartyName>
        <cbc:Name>Consignee W</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Consignee W Street</cbc:StreetName>
        <cbc:CityName>Munich</cbc:CityName>
        <cbc:PostalZone>231</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
    </cac:ConsigneeParty>
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
    <cac:OriginalDepartureCountry>
      <cbc:IdentificationCode>MA</cbc:IdentificationCode>
    </cac:OriginalDepartureCountry>
    <cac:FinalDestinationCountry>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:FinalDestinationCountry>
    <cac:TransitCountry>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:TransitCountry>
    <cac:TransitCountry>
      <cbc:IdentificationCode>AT</cbc:IdentificationCode>
    </cac:TransitCountry>
    <cac:MainCarriageShipmentStage>
      <cbc:ShipmentStageTypeCode>1</cbc:ShipmentStageTypeCode>
      <cbc:TransportModeCode>1</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:JourneyID>00344</cbc:JourneyID>
        <cbc:RegistrationNationalityID>IT</cbc:RegistrationNationalityID>
        <cac:MaritimeTransport>
          <cbc:VesselID>3852664</cbc:VesselID>
          <cbc:VesselName>Vessel Name</cbc:VesselName>
        </cac:MaritimeTransport>
      </cac:TransportMeans>
      <cac:EstimatedArrivalTransportEvent>
        <cbc:OccurrenceDate>2013-05-25</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>18:00:00+01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID>ITGOA</cbc:ID>
          <cbc:LocationTypeCode>24</cbc:LocationTypeCode>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode>IT</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:EstimatedArrivalTransportEvent>
    </cac:MainCarriageShipmentStage>
    <cac:TransportHandlingUnit>
      <cbc:ID>CON_THU_1</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
      <cbc:ShippingMarks>Agricultural products</cbc:ShippingMarks>
      <cac:TransportEquipment>
        <cbc:ID>BFCU4040001</cbc:ID>
        <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
        <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
        <cbc:Description>Should have a temperature between 2-4 degrees celcius</cbc:Description>
        <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
        <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
        <cbc:PowerIndicator>true</cbc:PowerIndicator>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Length</cbc:AttributeID>
          <cbc:Measure>6.1</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Height</cbc:AttributeID>
          <cbc:Measure>2.6</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Width</cbc:AttributeID>
          <cbc:Measure>2.44</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:GoodsItem>
          <cac:Item>
            <cac:CommodityClassification>
              <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
              <cbc:CommodityCode>8</cbc:CommodityCode>
            </cac:CommodityClassification>
          </cac:Item>
        </cac:GoodsItem>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>CON_THU_2</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
      <cbc:ShippingMarks>Agricultural products</cbc:ShippingMarks>
      <cac:TransportEquipment>
        <cbc:ID>BFCU4040002</cbc:ID>
        <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
        <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
        <cbc:Description>Should have a temperature between 2-4 degrees celcius</cbc:Description>
        <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
        <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
        <cbc:PowerIndicator>true</cbc:PowerIndicator>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Length</cbc:AttributeID>
          <cbc:Measure>6.1</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Height</cbc:AttributeID>
          <cbc:Measure>2.6</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Width</cbc:AttributeID>
          <cbc:Measure>2.44</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:GoodsItem>
          <cac:Item>
            <cac:CommodityClassification>
              <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
              <cbc:CommodityCode>8</cbc:CommodityCode>
            </cac:CommodityClassification>
          </cac:Item>
        </cac:GoodsItem>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    <cac:FirstArrivalPortLocation>
      <cbc:ID>ITGOA</cbc:ID>
      <cbc:LocationTypeCode>41</cbc:LocationTypeCode>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode>IT</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:FirstArrivalPortLocation>
    <cac:OfficeOfEntryLocation>
      <cbc:ID>DE000396</cbc:ID>
      <cbc:LocationTypeCode>41</cbc:LocationTypeCode>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:OfficeOfEntryLocation>
  </cac:Consignment>
</cac:Shipment>
```

**Structure 13** — 1 instance

```xml
<cac:Shipment>
  <cbc:ID>381944545</cbc:ID>
  <cac:Consignment>
    <cbc:ID>2076084807</cbc:ID>
    <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
    <cbc:SequenceID>203</cbc:SequenceID>
    <cbc:DeliveryInstructions>El Dorado</cbc:DeliveryInstructions>
    <cac:RequestedPickupTransportEvent>
      <cac:Contact>
        <cbc:Name>ExampleName</cbc:Name>
      </cac:Contact>
      <cac:Location>
        <cbc:ID>M165</cbc:ID>
        <cac:Address>
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
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2020-06-02</cbc:StartDate>
        <cbc:EndDate>2020-06-02</cbc:EndDate>
      </cac:Period>
    </cac:RequestedPickupTransportEvent>
    <cac:RequestedDeliveryTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:StreetName>StreetName Example</cbc:StreetName>
          <cbc:CityName>El Dorado</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>PA</cbc:IdentificationCode>
            <cbc:Name>Panama</cbc:Name>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2020-07-01</cbc:StartDate>
        <cbc:EndDate>2020-07-01</cbc:EndDate>
      </cac:Period>
    </cac:RequestedDeliveryTransportEvent>
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
    <cac:OriginalDepartureCountry>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:OriginalDepartureCountry>
    <cac:DeliveryTerms>
      <cbc:ID>CIP</cbc:ID>
      <cac:DeliveryLocation>
        <cbc:Name>Balboa Port</cbc:Name>
      </cac:DeliveryLocation>
    </cac:DeliveryTerms>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
      <cbc:Amount>0.00</cbc:Amount>
    </cac:FreightAllowanceCharge>
    <cac:MainCarriageShipmentStage>
      <cbc:TransportModeCode>1</cbc:TransportModeCode>
      <cac:LoadingPortLocation>
        <cbc:ID>Aarhus</cbc:ID>
      </cac:LoadingPortLocation>
      <cac:UnloadingPortLocation>
        <cbc:ID>Balboa Port</cbc:ID>
      </cac:UnloadingPortLocation>
    </cac:MainCarriageShipmentStage>
    <cac:TransportHandlingUnit>
      <cbc:ID>USRM3656679</cbc:ID>
      <cbc:TotalPackageQuantity>1</cbc:TotalPackageQuantity>
      <cac:TransportEquipment>
        <cac:TransportEquipmentSeal>
          <cbc:ID>7654321</cbc:ID>
        </cac:TransportEquipmentSeal>
      </cac:TransportEquipment>
      <cac:MaximumTemperature>
        <cbc:AttributeID>TC</cbc:AttributeID>
        <cbc:Measure>3.00</cbc:Measure>
        <cbc:Description>Chilled</cbc:Description>
      </cac:MaximumTemperature>
      <cac:Package>
        <cbc:ID>2076084807</cbc:ID>
        <cbc:Quantity>1</cbc:Quantity>
        <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
        <cac:GoodsItem>
          <cbc:ID>000010</cbc:ID>
          <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
          <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
          <cbc:Quantity>63.000</cbc:Quantity>
          <cac:Item>
            <cbc:Description>ItemExample</cbc:Description>
            <cbc:PackQuantity>63</cbc:PackQuantity>
            <cbc:Name>Dairy Products</cbc:Name>
            <cac:SellersItemIdentification>
              <cbc:ID>123456</cbc:ID>
            </cac:SellersItemIdentification>
            <cac:OriginCountry>
              <cbc:IdentificationCode>DK</cbc:IdentificationCode>
              <cbc:Name>Denmark</cbc:Name>
            </cac:OriginCountry>
            <cac:CommodityClassification>
              <cbc:CommodityCode>19011000</cbc:CommodityCode>
            </cac:CommodityClassification>
            <cac:AdditionalItemProperty>
              <cbc:Name>AnimalSpecies</cbc:Name>
              <cbc:Value>Bovine</cbc:Value>
            </cac:AdditionalItemProperty>
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
            <cac:ItemInstance>
              <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
              <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
              <cac:AdditionalItemProperty>
                <cbc:Name>LineNetWeight</cbc:Name>
                <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
              </cac:AdditionalItemProperty>
              <cac:AdditionalItemProperty>
                <cbc:Name>LineGrossWeight</cbc:Name>
                <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
              </cac:AdditionalItemProperty>
              <cac:AdditionalItemProperty>
                <cbc:Name>Quantity</cbc:Name>
                <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
              </cac:AdditionalItemProperty>
              <cac:LotIdentification>
                <cbc:LotNumberID>9390000757</cbc:LotNumberID>
              </cac:LotIdentification>
            </cac:ItemInstance>
            <cac:Dimension>
              <cbc:AttributeID>NetWeight</cbc:AttributeID>
              <cbc:Measure>9.6</cbc:Measure>
            </cac:Dimension>
            <cac:Dimension>
              <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
              <cbc:Measure>604.8</cbc:Measure>
            </cac:Dimension>
            <cac:Dimension>
              <cbc:AttributeID>GrossWeight</cbc:AttributeID>
              <cbc:Measure>12.288</cbc:Measure>
            </cac:Dimension>
            <cac:Dimension>
              <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
              <cbc:Measure>774.144</cbc:Measure>
            </cac:Dimension>
          </cac:Item>
          <cac:Despatch>
            <cbc:ID>000010</cbc:ID>
          </cac:Despatch>
          <cac:MaximumTemperature>
            <cbc:AttributeID>TC</cbc:AttributeID>
            <cbc:Measure>3.00</cbc:Measure>
            <cbc:Description>Chilled</cbc:Description>
          </cac:MaximumTemperature>
        </cac:GoodsItem>
        <cac:MeasurementDimension>
          <cbc:AttributeID>GrossWeight</cbc:AttributeID>
          <cbc:Measure>774.14400</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID>NetWeight</cbc:AttributeID>
          <cbc:Measure>604.80000</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
    </cac:TransportHandlingUnit>
  </cac:Consignment>
</cac:Shipment>
```

**Structure 14** — 1 instance

```xml
<cac:Shipment>
  <cbc:ID>32453</cbc:ID>
  <cbc:DeclaredStatisticsValueAmount>34800.00</cbc:DeclaredStatisticsValueAmount>
  <cac:Consignment>
    <cbc:ID>1</cbc:ID>
    <cbc:TotalInvoiceAmount>44250.00</cbc:TotalInvoiceAmount>
    <cbc:GrossWeightMeasure>230.80</cbc:GrossWeightMeasure>
    <cbc:Information>Professional equipment</cbc:Information>
    <cbc:TotalGoodsItemQuantity>23</cbc:TotalGoodsItemQuantity>
    <cac:FinalDestinationCountry>
      <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    </cac:FinalDestinationCountry>
    <cac:TransitCountry>
      <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    </cac:TransitCountry>
    <cac:FirstArrivalPortLocation>
      <cbc:Name>Padborg</cbc:Name>
    </cac:FirstArrivalPortLocation>
    <cac:LastExitPortLocation>
      <cbc:Name>Bietingen</cbc:Name>
    </cac:LastExitPortLocation>
  </cac:Consignment>
  <cac:GoodsItem>
    <cbc:ID>1</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>0.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>4500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>2</cbc:Quantity>
    <cac:Item>
      <cbc:Description>HILTI TE2 + TE35 Boremaskiner</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:AdditionalItemProperty>
        <cbc:Name>AlcoholPercentage</cbc:Name>
        <cbc:Value>0</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>DegreeOfPlato</cbc:Name>
        <cbc:Value>0</cbc:Value>
      </cac:AdditionalItemProperty>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>2</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>0.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>BACHO S910, Topnøglesæt</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>3</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>0.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>DEWALT DC822, Boltspænder</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>4</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>1500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>DEWALT DC542, Fugepistol</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>5</cbc:ID>
    <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>METABO GE700, Pinolsliber</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>6</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>1000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>METABO SBE 1010, Boremaskine</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>7</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>2500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>2500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>KAMA AD 105S, Båndsav</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>8</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>2500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>2500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>LIFTKET 021/51, Talje</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>9</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>KING TONY 6316, Topnøglesæt</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>10</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>1000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>2</cbc:Quantity>
    <cac:Item>
      <cbc:Description>STAHL WILLE 730/02, Momentnøgle</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>11</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>HADEF 750kg, Talje</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>12</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>750.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>750.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>2</cbc:Quantity>
    <cac:Item>
      <cbc:Description>HADEF 250kg, Talje</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>13</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>1500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>DURA PRO 2000kg, Dunkraft</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>14</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>2000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>2000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>BY45A, Donkraft</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>15</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>1500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>MILWAUKEE HD18PD, Akkuboremaskine</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>US</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>16</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>1500.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>ESMOLADARA KH3105, Bænksliber</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>17</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>2000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>2000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>SCANTOOL 20AT, Søjleboremaskine</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>18</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>10000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>10000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>KEMPPI MASTER 2200, Tigsvejser</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>FI</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>19</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>5000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>5000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>VÆRKTØJSKASSE m/div. håndværktøj</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>20</cbc:ID>
    <cbc:DeclaredCustomsValueAmount>3000.00</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>3000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Description>BOSCH GLL 3-80P Lasernivilering</cbc:Description>
      <cac:OriginCountry>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:ShipmentStage>
    <cac:UnloadingPortLocation>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode>CH</cbc:IdentificationCode>
          <cbc:Name>Swiss</cbc:Name>
        </cac:Country>
      </cac:Address>
    </cac:UnloadingPortLocation>
  </cac:ShipmentStage>
  <cac:OriginAddress>
    <cac:Country>
      <cbc:IdentificationCode>DK</cbc:IdentificationCode>
      <cbc:Name>Denmark</cbc:Name>
    </cac:Country>
  </cac:OriginAddress>
  <cac:FirstArrivalPortLocation>
    <cbc:Name>Padborg</cbc:Name>
  </cac:FirstArrivalPortLocation>
  <cac:LastExitPortLocation>
    <cbc:Description>ART INTERNATIONAL ZURICH 2019</cbc:Description>
    <cac:Address>
      <cbc:StreetName>Giessereistrasse</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CityName>Zürich</cbc:CityName>
      <cbc:PostalZone>CH-8005</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>CH</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:LastExitPortLocation>
</cac:Shipment>
```

**Structure 15** — 1 instance

```xml
<cac:Shipment>
  <cbc:ID>CONS-0001</cbc:ID>
  <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
  <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
  <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
  <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
  <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
  <cbc:TotalTransportHandlingUnitQuantity>10</cbc:TotalTransportHandlingUnitQuantity>
  <cbc:InsuranceValueAmount>1000.00</cbc:InsuranceValueAmount>
  <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
  <cbc:FreeOnBoardValueAmount>1200.00</cbc:FreeOnBoardValueAmount>
  <cbc:SpecialInstructions>Beeswax becomes liquid at 50'C</cbc:SpecialInstructions>
  <cac:Consignment>
    <cbc:ID>2005US12345678998765432112345678</cbc:ID>
    <cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
    <cbc:TariffCode>15219000</cbc:TariffCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
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
    <cac:OriginalDepartureCountry>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:OriginalDepartureCountry>
    <cac:FinalDestinationCountry>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:FinalDestinationCountry>
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
    <cac:OriginalDespatchTransportationService>
      <cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
    </cac:OriginalDespatchTransportationService>
    <cac:FinalDeliveryTransportationService>
      <cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
    </cac:FinalDeliveryTransportationService>
    <cac:DeliveryTerms>
      <cbc:ID>FOB Destination</cbc:ID>
      <cac:DeliveryLocation>
        <cbc:ID>GBBRS</cbc:ID>
        <cbc:Description>Bristol</cbc:Description>
      </cac:DeliveryLocation>
    </cac:DeliveryTerms>
    <cac:PaymentTerms>
      <cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
    </cac:PaymentTerms>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cbc:Amount>254.00</cbc:Amount>
    </cac:FreightAllowanceCharge>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
      <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
      <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
      <cbc:Amount>12.70</cbc:Amount>
      <cbc:BaseAmount>254.00</cbc:BaseAmount>
    </cac:FreightAllowanceCharge>
  </cac:Consignment>
  <cac:GoodsItem>
    <cbc:ID>1</cbc:ID>
    <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:FreeOnBoardValueAmount>1241.30</cbc:FreeOnBoardValueAmount>
    <cbc:InsuranceValueAmount>1241.30</cbc:InsuranceValueAmount>
    <cbc:ValueAmount>1000.00</cbc:ValueAmount>
    <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
    <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
    <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
    <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
    <cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
    <cbc:CustomsTariffQuantity>1000</cbc:CustomsTariffQuantity>
    <cac:Item>
      <cbc:Description>Beeswax</cbc:Description>
      <cbc:Name>Acme Beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>MX</cbc:IdentificationCode>
        <cbc:Name>Mexico</cbc:Name>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:ShipmentStage>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportModeCode>3</cbc:TransportModeCode>
    <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
    <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
    <cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
    <cac:TransitPeriod>
      <cbc:StartDate>2005-06-25</cbc:StartDate>
      <cbc:StartTime>11:35:00.0Z</cbc:StartTime>
      <cbc:EndDate>2005-06-25</cbc:EndDate>
      <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
    </cac:TransitPeriod>
    <cac:CarrierParty>
      <cac:PartyName>
        <cbc:Name>Keep On Trucking</cbc:Name>
      </cac:PartyName>
      <cac:Contact>
        <cbc:Telephone>+1 36222 33847</cbc:Telephone>
      </cac:Contact>
    </cac:CarrierParty>
    <cac:TransportMeans>
      <cac:RoadTransport>
        <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
      </cac:RoadTransport>
    </cac:TransportMeans>
  </cac:ShipmentStage>
  <cac:ShipmentStage>
    <cbc:ID>2</cbc:ID>
    <cbc:TransportModeCode>4</cbc:TransportModeCode>
    <cbc:TransportMeansTypeCode>Plane</cbc:TransportMeansTypeCode>
    <cbc:PreCarriageIndicator>false</cbc:PreCarriageIndicator>
    <cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
    <cac:TransitPeriod>
      <cbc:StartDate>2005-06-25</cbc:StartDate>
      <cbc:StartTime>23:20:00.0Z</cbc:StartTime>
    </cac:TransitPeriod>
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
    <cac:TransportMeans>
      <cbc:JourneyID>UA 1234</cbc:JourneyID>
      <cac:AirTransport>
        <cbc:AircraftID>A-127763-747</cbc:AircraftID>
      </cac:AirTransport>
    </cac:TransportMeans>
    <cac:LoadingPortLocation>
      <cbc:ID>USBOS</cbc:ID>
      <cbc:Description>Boston Airport</cbc:Description>
    </cac:LoadingPortLocation>
    <cac:UnloadingPortLocation>
      <cbc:ID>GBBRS</cbc:ID>
      <cbc:Description>Bristol Airport</cbc:Description>
    </cac:UnloadingPortLocation>
    <cac:TransshipPortLocation>
      <cbc:ID>GBLHR</cbc:ID>
      <cbc:Description>Heathrow Apt/London</cbc:Description>
    </cac:TransshipPortLocation>
  </cac:ShipmentStage>
  <cac:Delivery>
    <cbc:Quantity>1</cbc:Quantity>
    <cbc:LatestDeliveryDate>2005-06-30</cbc:LatestDeliveryDate>
    <cbc:LatestDeliveryTime>18:00:00.0Z</cbc:LatestDeliveryTime>
    <cbc:TrackingID>NKH7712289-03339-000128</cbc:TrackingID>
    <cac:DeliveryAddress>
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
    </cac:DeliveryAddress>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2005-06-29</cbc:StartDate>
      <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
      <cbc:EndDate>2005-06-30</cbc:EndDate>
      <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
    </cac:RequestedDeliveryPeriod>
    <cac:EstimatedDeliveryPeriod>
      <cbc:StartDate>2005-06-30</cbc:StartDate>
      <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
    </cac:EstimatedDeliveryPeriod>
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
    <cac:Despatch>
      <cbc:ActualDespatchDate>2005-06-25</cbc:ActualDespatchDate>
      <cbc:ActualDespatchTime>11:35:00.0Z</cbc:ActualDespatchTime>
      <cac:DespatchAddress>
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
      </cac:DespatchAddress>
      <cac:DespatchParty>
        <cac:PartyName>
          <cbc:Name>Consortial</cbc:Name>
        </cac:PartyName>
      </cac:DespatchParty>
      <cac:Contact>
        <cbc:Name>Mrs Bouquet</cbc:Name>
        <cbc:Telephone>+1 158 1233714</cbc:Telephone>
        <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
        <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
      </cac:Contact>
    </cac:Despatch>
  </cac:Delivery>
  <cac:TransportHandlingUnit>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>PA</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:TotalGoodsItemQuantity>10</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
    <cac:ActualPackage>
      <cbc:Quantity>10</cbc:Quantity>
      <cbc:PackagingTypeCode>TB</cbc:PackagingTypeCode>
    </cac:ActualPackage>
  </cac:TransportHandlingUnit>
  <cac:OriginAddress>
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
  </cac:OriginAddress>
  <cac:FirstArrivalPortLocation>
    <cbc:ID>GBBRS</cbc:ID>
    <cbc:Description>Bristol</cbc:Description>
  </cac:FirstArrivalPortLocation>
  <cac:LastExitPortLocation>
    <cbc:ID>USBOS</cbc:ID>
    <cbc:Description>Boston</cbc:Description>
  </cac:LastExitPortLocation>
  <cac:ExportCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:ExportCountry>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cbc:Amount>254.00</cbc:Amount>
  </cac:FreightAllowanceCharge>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
    <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
    <cbc:Amount>12.70</cbc:Amount>
    <cbc:BaseAmount>254.00</cbc:BaseAmount>
  </cac:FreightAllowanceCharge>
</cac:Shipment>
```

**Structure 16** — 3 instances

```xml
<cac:Shipment>
  <cbc:ID>CONS-0001</cbc:ID>
  <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
  <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
  <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
  <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
  <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
  <cbc:TotalGoodsItemQuantity>1</cbc:TotalGoodsItemQuantity>
  <cbc:TotalTransportHandlingUnitQuantity>10</cbc:TotalTransportHandlingUnitQuantity>
  <cbc:InsuranceValueAmount>1000.00</cbc:InsuranceValueAmount>
  <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
  <cbc:FreeOnBoardValueAmount>1200.00</cbc:FreeOnBoardValueAmount>
  <cbc:SpecialInstructions>Beeswax becomes liquid at 50'C</cbc:SpecialInstructions>
  <cac:Consignment>
    <cbc:ID>2005US12345678998765432112345678</cbc:ID>
    <cbc:TariffDescription>Beeswax, other insect waxes and spermacetti</cbc:TariffDescription>
    <cbc:TariffCode>15219000</cbc:TariffCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
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
    <cac:OriginalDepartureCountry>
      <cbc:IdentificationCode>US</cbc:IdentificationCode>
    </cac:OriginalDepartureCountry>
    <cac:FinalDestinationCountry>
      <cbc:IdentificationCode>GB</cbc:IdentificationCode>
    </cac:FinalDestinationCountry>
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
    <cac:OriginalDespatchTransportationService>
      <cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
    </cac:OriginalDespatchTransportationService>
    <cac:FinalDeliveryTransportationService>
      <cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
    </cac:FinalDeliveryTransportationService>
    <cac:DeliveryTerms>
      <cbc:ID>FOB Destination</cbc:ID>
      <cac:DeliveryLocation>
        <cbc:ID>GBBRS</cbc:ID>
        <cbc:Description>Bristol</cbc:Description>
      </cac:DeliveryLocation>
    </cac:DeliveryTerms>
    <cac:PaymentTerms>
      <cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
    </cac:PaymentTerms>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cbc:Amount>254.00</cbc:Amount>
    </cac:FreightAllowanceCharge>
    <cac:FreightAllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
      <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
      <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
      <cbc:Amount>12.70</cbc:Amount>
      <cbc:BaseAmount>254.00</cbc:BaseAmount>
    </cac:FreightAllowanceCharge>
  </cac:Consignment>
  <cac:GoodsItem>
    <cbc:ID>1</cbc:ID>
    <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
    <cbc:Description>Acme beeswax</cbc:Description>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:DeclaredCustomsValueAmount>524.80</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount>1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:FreeOnBoardValueAmount>1241.30</cbc:FreeOnBoardValueAmount>
    <cbc:InsuranceValueAmount>1241.30</cbc:InsuranceValueAmount>
    <cbc:ValueAmount>1000.00</cbc:ValueAmount>
    <cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure>110</cbc:NetWeightMeasure>
    <cbc:NetNetWeightMeasure>100</cbc:NetNetWeightMeasure>
    <cbc:GrossVolumeMeasure>2</cbc:GrossVolumeMeasure>
    <cbc:NetVolumeMeasure>2.235</cbc:NetVolumeMeasure>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
    <cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
    <cbc:CustomsTariffQuantity>1000</cbc:CustomsTariffQuantity>
    <cac:Item>
      <cbc:Description>Beeswax</cbc:Description>
      <cbc:Name>Acme Beeswax</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>6578489</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>17589683</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>MX</cbc:IdentificationCode>
        <cbc:Name>Mexico</cbc:Name>
      </cac:OriginCountry>
    </cac:Item>
  </cac:GoodsItem>
  <cac:ShipmentStage>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportModeCode>3</cbc:TransportModeCode>
    <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
    <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
    <cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
    <cac:TransitPeriod>
      <cbc:StartDate>2005-06-25</cbc:StartDate>
      <cbc:StartTime>11:35:00.0Z</cbc:StartTime>
      <cbc:EndDate>2005-06-25</cbc:EndDate>
      <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
    </cac:TransitPeriod>
    <cac:CarrierParty>
      <cac:PartyName>
        <cbc:Name>Keep On Trucking</cbc:Name>
      </cac:PartyName>
      <cac:Contact>
        <cbc:Telephone>+1 36222 33847</cbc:Telephone>
      </cac:Contact>
    </cac:CarrierParty>
    <cac:TransportMeans>
      <cac:RoadTransport>
        <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
      </cac:RoadTransport>
    </cac:TransportMeans>
  </cac:ShipmentStage>
  <cac:ShipmentStage>
    <cbc:ID>2</cbc:ID>
    <cbc:TransportModeCode>4</cbc:TransportModeCode>
    <cbc:TransportMeansTypeCode>Plane</cbc:TransportMeansTypeCode>
    <cbc:PreCarriageIndicator>false</cbc:PreCarriageIndicator>
    <cbc:OnCarriageIndicator>false</cbc:OnCarriageIndicator>
    <cac:TransitPeriod>
      <cbc:StartDate>2005-06-25</cbc:StartDate>
      <cbc:StartTime>23:20:00.0Z</cbc:StartTime>
    </cac:TransitPeriod>
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
    <cac:TransportMeans>
      <cbc:JourneyID>UA 1234</cbc:JourneyID>
      <cac:AirTransport>
        <cbc:AircraftID>A-127763-747</cbc:AircraftID>
      </cac:AirTransport>
    </cac:TransportMeans>
    <cac:LoadingPortLocation>
      <cbc:ID>USBOS</cbc:ID>
      <cbc:Description>Boston Airport</cbc:Description>
    </cac:LoadingPortLocation>
    <cac:UnloadingPortLocation>
      <cbc:ID>GBBRS</cbc:ID>
      <cbc:Description>Bristol Airport</cbc:Description>
    </cac:UnloadingPortLocation>
    <cac:TransshipPortLocation>
      <cbc:ID>GBLHR</cbc:ID>
      <cbc:Description>Heathrow Apt/London</cbc:Description>
    </cac:TransshipPortLocation>
  </cac:ShipmentStage>
  <cac:Delivery>
    <cbc:Quantity>1</cbc:Quantity>
    <cbc:LatestDeliveryDate>2005-06-30</cbc:LatestDeliveryDate>
    <cbc:LatestDeliveryTime>18:00:00.0Z</cbc:LatestDeliveryTime>
    <cbc:TrackingID>NKH7712289-03339-000128</cbc:TrackingID>
    <cac:DeliveryAddress>
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
    </cac:DeliveryAddress>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2005-06-29</cbc:StartDate>
      <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
      <cbc:EndDate>2005-06-30</cbc:EndDate>
      <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
    </cac:RequestedDeliveryPeriod>
    <cac:EstimatedDeliveryPeriod>
      <cbc:StartDate>2005-06-30</cbc:StartDate>
      <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
    </cac:EstimatedDeliveryPeriod>
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
    <cac:Despatch>
      <cbc:ActualDespatchDate>2005-06-25</cbc:ActualDespatchDate>
      <cbc:ActualDespatchTime>11:35:00.0Z</cbc:ActualDespatchTime>
      <cac:DespatchAddress>
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
      </cac:DespatchAddress>
      <cac:DespatchParty>
        <cac:PartyName>
          <cbc:Name>Consortial</cbc:Name>
        </cac:PartyName>
      </cac:DespatchParty>
      <cac:Contact>
        <cbc:Name>Mrs Bouquet</cbc:Name>
        <cbc:Telephone>+1 158 1233714</cbc:Telephone>
        <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
        <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
      </cac:Contact>
    </cac:Despatch>
  </cac:Delivery>
  <cac:TransportHandlingUnit>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportHandlingUnitTypeCode>PA</cbc:TransportHandlingUnitTypeCode>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:TotalGoodsItemQuantity>10</cbc:TotalGoodsItemQuantity>
    <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
    <cac:ActualPackage>
      <cbc:Quantity>10</cbc:Quantity>
      <cbc:PackagingTypeCode>TB</cbc:PackagingTypeCode>
    </cac:ActualPackage>
  </cac:TransportHandlingUnit>
  <cac:OriginAddress>
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
  </cac:OriginAddress>
  <cac:FirstArrivalPortLocation>
    <cbc:ID>GBBRS</cbc:ID>
    <cbc:Description>Bristol</cbc:Description>
  </cac:FirstArrivalPortLocation>
  <cac:LastExitPortLocation>
    <cbc:ID>USBOS</cbc:ID>
    <cbc:Description>Boston</cbc:Description>
  </cac:LastExitPortLocation>
  <cac:ExportCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:ExportCountry>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cbc:Amount>254.00</cbc:Amount>
  </cac:FreightAllowanceCharge>
  <cac:FreightAllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode>79</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Sundry discount</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
    <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
    <cbc:Amount>12.70</cbc:Amount>
    <cbc:BaseAmount>254.00</cbc:BaseAmount>
  </cac:FreightAllowanceCharge>
</cac:Shipment>
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

### `SocialMediaProfileType`

**Used as:** `cac:SocialMediaProfile`

_10 instances across 1 element, with 2 unique structures_

**Structure 1** — 8 instances

```xml
<cac:SocialMediaProfile>
  <cbc:ID>4</cbc:ID>
  <cbc:Name>YouTube</cbc:Name>
  <cbc:URI>http://www.youtube.com/oasisopen</cbc:URI>
</cac:SocialMediaProfile>
```

**Structure 2** — 2 instances

```xml
<cac:SocialMediaProfile>
  <cbc:ID>1</cbc:ID>
  <cbc:Name>LinkedIN</cbc:Name>
  <cbc:SocialMediaTypeCode>Business</cbc:SocialMediaTypeCode>
  <cbc:URI>https://www.linkedin.com/company/oasis</cbc:URI>
</cac:SocialMediaProfile>
```

[↑ Back to contents](#contents)

### `StatementLineType`

**Used as:** `cac:StatementLine`

_5 instances across 1 element, with 1 unique structure_

**Structure 1** — 5 instances

```xml
<cac:StatementLine>
  <cbc:ID>normalizedString</cbc:ID>
  <cbc:Note>String</cbc:Note>
  <cbc:BalanceBroughtForwardIndicator>false</cbc:BalanceBroughtForwardIndicator>
  <cbc:DebitLineAmount>0.00</cbc:DebitLineAmount>
  <cbc:CreditLineAmount>107.50</cbc:CreditLineAmount>
  <cbc:BalanceAmount>-107.50</cbc:BalanceAmount>
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
  <cac:BillingReference>
    <cac:CreditNoteDocumentReference>
      <cbc:ID>CN758494</cbc:ID>
      <cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
      <cbc:IssueDate>2005-06-25</cbc:IssueDate>
    </cac:CreditNoteDocumentReference>
  </cac:BillingReference>
</cac:StatementLine>
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

### `StockAvailabilityReportLineType`

**Used as:** `cac:StockAvailabilityReportLine`

_6 instances across 1 element, with 2 unique structures_

**Structure 1** — 2 instances

```xml
<cac:StockAvailabilityReportLine>
  <cbc:ID>3</cbc:ID>
  <cbc:Quantity>0</cbc:Quantity>
  <cbc:AvailabilityStatusCode>8</cbc:AvailabilityStatusCode>
  <cac:Item>
    <cbc:Description>skirt</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>TS893</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>PK009</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:StockAvailabilityReportLine>
```

**Structure 2** — 4 instances

```xml
<cac:StockAvailabilityReportLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>50</cbc:Quantity>
  <cbc:AvailabilityDate>2010-04-20</cbc:AvailabilityDate>
  <cbc:AvailabilityStatusCode>1</cbc:AvailabilityStatusCode>
  <cac:Item>
    <cbc:Description>T-shirt</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>TT319</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>ZZ738</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:StockAvailabilityReportLine>
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

### `TaxCategoryType`

**Used as:** `cac:ClassifiedTaxCategory` · `cac:TaxCategory`

_107 instances across 2 elements, with 7 unique structures_

**Structure 1** — 2 instances

```xml
<cac:TaxCategory>
  <cbc:ID>O</cbc:ID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

**Structure 2** — 1 instance

```xml
<cac:TaxCategory>
  <cbc:Percent>21.00</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

**Structure 3** — 33 instances

```xml
<cac:TaxCategory>
  <cbc:ID>A</cbc:ID>
  <cac:TaxScheme>
    <cbc:ID>UK VAT</cbc:ID>
    <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
  </cac:TaxScheme>
</cac:TaxCategory>
```

**Structure 4** — 17 instances

```xml
<cac:TaxCategory>
  <cbc:ID>S</cbc:ID>
  <cbc:Percent>20</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

**Structure 5** — 30 instances

```xml
<cac:ClassifiedTaxCategory>
  <cbc:ID>S</cbc:ID>
  <cbc:Percent>20</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:ClassifiedTaxCategory>
```

**Structure 6** — 18 instances

```xml
<cac:TaxCategory>
  <cbc:ID>A</cbc:ID>
  <cbc:Percent>17.5</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>UK VAT</cbc:ID>
    <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
  </cac:TaxScheme>
</cac:TaxCategory>
```

**Structure 7** — 6 instances

```xml
<cac:TaxCategory>
  <cbc:ID>E</cbc:ID>
  <cbc:Percent>0</cbc:Percent>
  <cbc:TaxExemptionReasonCode>AAM</cbc:TaxExemptionReasonCode>
  <cbc:TaxExemptionReason>Exempt New Means of Transport</cbc:TaxExemptionReason>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

[↑ Back to contents](#contents)

### `TaxSchemeType`

**Used as:** `cac:TaxScheme`

_339 instances across 1 element, with 3 unique structures_

**Structure 1** — 75 instances

```xml
<cac:TaxScheme>
  <cbc:ID>VAT</cbc:ID>
</cac:TaxScheme>
```

**Structure 2** — 260 instances

```xml
<cac:TaxScheme>
  <cbc:ID>UK VAT</cbc:ID>
  <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
</cac:TaxScheme>
```

**Structure 3** — 4 instances

```xml
<cac:TaxScheme>
  <cbc:ID>63</cbc:ID>
  <cbc:Name>Moms</cbc:Name>
</cac:TaxScheme>
```

[↑ Back to contents](#contents)

### `TaxSubtotalType`

**Used as:** `cac:TaxSubtotal`

_69 instances across 1 element, with 7 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount>202.50</cbc:TaxableAmount>
  <cbc:TaxAmount>42.55</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:Percent>21.00</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

**Structure 2** — 29 instances

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount>100.00</cbc:TaxableAmount>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:ID>A</cbc:ID>
    <cac:TaxScheme>
      <cbc:ID>UK VAT</cbc:ID>
      <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

**Structure 3** — 12 instances

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount>1460.5</cbc:TaxableAmount>
  <cbc:TaxAmount>292.1</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:ID>S</cbc:ID>
    <cbc:Percent>20</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

**Structure 4** — 1 instance

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount>1.00</cbc:TaxableAmount>
  <cbc:TaxAmount>0.00</cbc:TaxAmount>
  <cbc:TaxInclusiveAmount>1.00</cbc:TaxInclusiveAmount>
  <cac:TaxCategory>
    <cbc:ID>O</cbc:ID>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

**Structure 5** — 17 instances

```xml
<cac:TaxSubtotal>
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
</cac:TaxSubtotal>
```

**Structure 6** — 3 instances

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount>23.20</cbc:TaxableAmount>
  <cbc:TaxAmount>5.80</cbc:TaxAmount>
  <cbc:TaxInclusiveAmount>29.00</cbc:TaxInclusiveAmount>
  <cac:TaxCategory>
    <cbc:ID>S</cbc:ID>
    <cbc:Percent>25</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

**Structure 7** — 6 instances

```xml
<cac:TaxSubtotal>
  <cbc:TaxableAmount>-25</cbc:TaxableAmount>
  <cbc:TaxAmount>0</cbc:TaxAmount>
  <cac:TaxCategory>
    <cbc:ID>E</cbc:ID>
    <cbc:Percent>0</cbc:Percent>
    <cbc:TaxExemptionReasonCode>AAM</cbc:TaxExemptionReasonCode>
    <cbc:TaxExemptionReason>Exempt New Means of Transport</cbc:TaxExemptionReason>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:TaxSubtotal>
```

[↑ Back to contents](#contents)

### `TaxTotalType`

**Used as:** `cac:TaxTotal`

_93 instances across 1 element, with 9 unique structures_

**Structure 1** — 32 instances

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>100</cbc:TaxAmount>
</cac:TaxTotal>
```

**Structure 2** — 1 instance

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>42.55</cbc:TaxAmount>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>202.50</cbc:TaxableAmount>
    <cbc:TaxAmount>42.55</cbc:TaxAmount>
    <cac:TaxCategory>
      <cbc:Percent>21.00</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
</cac:TaxTotal>
```

**Structure 3** — 4 instances

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
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
</cac:TaxTotal>
```

**Structure 4** — 29 instances

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>100.00</cbc:TaxableAmount>
    <cbc:TaxAmount>17.50</cbc:TaxAmount>
    <cac:TaxCategory>
      <cbc:ID>A</cbc:ID>
      <cac:TaxScheme>
        <cbc:ID>UK VAT</cbc:ID>
        <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
</cac:TaxTotal>
```

**Structure 5** — 2 instances

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>4.00</cbc:TaxAmount>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>16.00</cbc:TaxableAmount>
    <cbc:TaxAmount>4.00</cbc:TaxAmount>
    <cbc:TaxInclusiveAmount>20.00</cbc:TaxInclusiveAmount>
    <cac:TaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>25</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
</cac:TaxTotal>
```

**Structure 6** — 1 instance

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
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
</cac:TaxTotal>
```

**Structure 7** — 17 instances

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
  <cac:TaxSubtotal>
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
  </cac:TaxSubtotal>
</cac:TaxTotal>
```

**Structure 8** — 1 instance

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>5.80</cbc:TaxAmount>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>23.20</cbc:TaxableAmount>
    <cbc:TaxAmount>5.80</cbc:TaxAmount>
    <cbc:TaxInclusiveAmount>29.00</cbc:TaxInclusiveAmount>
    <cac:TaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>25</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>1.00</cbc:TaxableAmount>
    <cbc:TaxAmount>0.00</cbc:TaxAmount>
    <cbc:TaxInclusiveAmount>1.00</cbc:TaxInclusiveAmount>
    <cac:TaxCategory>
      <cbc:ID>O</cbc:ID>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
</cac:TaxTotal>
```

**Structure 9** — 6 instances

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>292.20</cbc:TaxAmount>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>1460.5</cbc:TaxableAmount>
    <cbc:TaxAmount>292.1</cbc:TaxAmount>
    <cac:TaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>1</cbc:TaxableAmount>
    <cbc:TaxAmount>0.1</cbc:TaxAmount>
    <cac:TaxCategory>
      <cbc:ID>AA</cbc:ID>
      <cbc:Percent>10</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
  <cac:TaxSubtotal>
    <cbc:TaxableAmount>-25</cbc:TaxableAmount>
    <cbc:TaxAmount>0</cbc:TaxAmount>
    <cac:TaxCategory>
      <cbc:ID>E</cbc:ID>
      <cbc:Percent>0</cbc:Percent>
      <cbc:TaxExemptionReasonCode>AAM</cbc:TaxExemptionReasonCode>
      <cbc:TaxExemptionReason>Exempt New Means of Transport</cbc:TaxExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:TaxSubtotal>
</cac:TaxTotal>
```

[↑ Back to contents](#contents)

### `TemperatureType`

**Used as:** `cac:MaximumTemperature`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:MaximumTemperature>
  <cbc:AttributeID>TC</cbc:AttributeID>
  <cbc:Measure>3.00</cbc:Measure>
  <cbc:Description>Chilled</cbc:Description>
</cac:MaximumTemperature>
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

### `TransactionConditionsType`

**Used as:** `cac:TransactionConditions`

_13 instances across 1 element, with 1 unique structure_

**Structure 1** — 13 instances

```xml
<cac:TransactionConditions>
  <cbc:Description>order response required; payment is by BACS or by cheque</cbc:Description>
</cac:TransactionConditions>
```

[↑ Back to contents](#contents)

### `TransportEquipmentSealType`

**Used as:** `cac:TransportEquipmentSeal`

_3 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TransportEquipmentSeal>
  <cbc:ID>7654321</cbc:ID>
</cac:TransportEquipmentSeal>
```

**Structure 2** — 2 instances

```xml
<cac:TransportEquipmentSeal>
  <cbc:ID>2_1</cbc:ID>
  <cbc:Condition>IN_RIGHT_CONDITION</cbc:Condition>
</cac:TransportEquipmentSeal>
```

[↑ Back to contents](#contents)

### `TransportEquipmentType`

**Used as:** `cac:ContainedInTransportEquipment` · `cac:ReferencedTransportEquipment` · `cac:SupportedTransportEquipment` · `cac:TransportEquipment`

_36 instances across 4 elements, with 15 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TransportEquipment>
  <cbc:ID>CON_TE_1</cbc:ID>
</cac:TransportEquipment>
```

**Structure 2** — 3 instances

```xml
<cac:ReferencedTransportEquipment>
  <cbc:ID>GRAI 12345698-1</cbc:ID>
</cac:ReferencedTransportEquipment>
```

**Structure 3** — 2 instances

```xml
<cac:TransportEquipment>
  <cbc:TransportEquipmentTypeCode>AD</cbc:TransportEquipmentTypeCode>
  <cbc:FullnessIndicationCode>FTL</cbc:FullnessIndicationCode>
</cac:TransportEquipment>
```

**Structure 4** — 1 instance

```xml
<cac:TransportEquipment>
  <cac:TransportEquipmentSeal>
    <cbc:ID>7654321</cbc:ID>
  </cac:TransportEquipmentSeal>
</cac:TransportEquipment>
```

**Structure 5** — 6 instances

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>NEC_TE_1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914542</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

**Structure 6** — 6 instances

```xml
<cac:TransportEquipment>
  <cbc:ID>CON_2</cbc:ID>
  <cac:ContainedInTransportEquipment>
    <cbc:ID>EXT_TE_2</cbc:ID>
    <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
    <cbc:TraceID>12345678914112</cbc:TraceID>
  </cac:ContainedInTransportEquipment>
  <cac:Package>
    <cbc:ID>CON_2</cbc:ID>
    <cbc:Quantity>10</cbc:Quantity>
  </cac:Package>
</cac:TransportEquipment>
```

**Structure 7** — 2 instances

```xml
<cac:TransportEquipment>
  <cbc:ID>1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Length</cbc:AttributeID>
    <cbc:Measure>6.1</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Height</cbc:AttributeID>
    <cbc:Measure>2.6</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Width</cbc:AttributeID>
    <cbc:Measure>2.44</cbc:Measure>
  </cac:MeasurementDimension>
</cac:TransportEquipment>
```

**Structure 8** — 2 instances

```xml
<cac:SupportedTransportEquipment>
  <cbc:ID>1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Length</cbc:AttributeID>
    <cbc:Measure>6.1</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Height</cbc:AttributeID>
    <cbc:Measure>2.6</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Width</cbc:AttributeID>
    <cbc:Measure>2.44</cbc:Measure>
  </cac:MeasurementDimension>
</cac:SupportedTransportEquipment>
```

**Structure 9** — 2 instances

```xml
<cac:ReferencedTransportEquipment>
  <cbc:ID>1</cbc:ID>
  <cac:TransportEquipmentSeal>
    <cbc:ID>1_1</cbc:ID>
    <cbc:Condition>IN_RIGHT_CONDITION</cbc:Condition>
  </cac:TransportEquipmentSeal>
  <cac:Package>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:PackagingTypeCode>PX</cbc:PackagingTypeCode>
    <cac:GoodsItem>
      <cac:Item>
        <cac:CommodityClassification>
          <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Package>
</cac:ReferencedTransportEquipment>
```

**Structure 10** — 1 instance

```xml
<cac:TransportEquipment>
  <cbc:ID>TE_1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>AE</cbc:TransportEquipmentTypeCode>
  <cbc:Description>BODY TRAILER</cbc:Description>
  <cbc:GrossWeightMeasure>1000.0</cbc:GrossWeightMeasure>
  <cac:GoodsItem>
    <cbc:ID>GID_1</cbc:ID>
    <cac:Item>
      <cbc:Description>MOTOR CYCLE</cbc:Description>
      <cbc:Name>YAMAHA</cbc:Name>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>GID_2</cbc:ID>
    <cac:Item>
      <cbc:Description>MOTOR CYCLE</cbc:Description>
      <cbc:Name>HONDA</cbc:Name>
    </cac:Item>
  </cac:GoodsItem>
</cac:TransportEquipment>
```

**Structure 11** — 2 instances

```xml
<cac:TransportEquipment>
  <cbc:ID>TRHU1652173</cbc:ID>
  <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
  <cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
  <cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
  <cac:VerifiedGrossMass>
    <cbc:ID>123</cbc:ID>
    <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
    <cbc:WeighingTime>00:30:00</cbc:WeighingTime>
    <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
    <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
    <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
    <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
    <cac:DocumentReference>
      <cbc:ID>W123</cbc:ID>
      <cbc:IssueDate>2016-11-02</cbc:IssueDate>
      <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
      <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
    </cac:DocumentReference>
  </cac:VerifiedGrossMass>
</cac:TransportEquipment>
```

**Structure 12** — 1 instance

```xml
<cac:TransportEquipment>
  <cbc:ID>TRHU1652173</cbc:ID>
  <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
  <cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
  <cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
  <cac:VerifiedGrossMass>
    <cbc:ID>123</cbc:ID>
    <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
    <cbc:WeighingTime>00:30:00</cbc:WeighingTime>
    <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
    <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
    <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
    <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
    <cac:DocumentReference>
      <cbc:ID>W123</cbc:ID>
      <cbc:IssueDate>2016-11-02</cbc:IssueDate>
      <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
      <cbc:DocumentType></cbc:DocumentType>
      <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
    </cac:DocumentReference>
  </cac:VerifiedGrossMass>
</cac:TransportEquipment>
```

**Structure 13** — 2 instances

```xml
<cac:TransportEquipment>
  <cbc:ID>BFCU4040001</cbc:ID>
  <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
  <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
  <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
  <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
  <cbc:Description>Should have a temperature between 2-4 degrees celcius</cbc:Description>
  <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
  <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
  <cbc:PowerIndicator>true</cbc:PowerIndicator>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Length</cbc:AttributeID>
    <cbc:Measure>6.1</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Height</cbc:AttributeID>
    <cbc:Measure>2.6</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Width</cbc:AttributeID>
    <cbc:Measure>2.44</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:GoodsItem>
    <cac:Item>
      <cac:CommodityClassification>
        <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
        <cbc:CommodityCode>8</cbc:CommodityCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:GoodsItem>
</cac:TransportEquipment>
```

**Structure 14** — 4 instances

```xml
<cac:TransportEquipment>
  <cbc:ID>CON_TE_2</cbc:ID>
  <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
  <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
  <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
  <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
  <cbc:Description>SomeDescription</cbc:Description>
  <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
  <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
  <cbc:PowerIndicator>false</cbc:PowerIndicator>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Length</cbc:AttributeID>
    <cbc:Measure>6.1</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Height</cbc:AttributeID>
    <cbc:Measure>2.6</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Width</cbc:AttributeID>
    <cbc:Measure>2.44</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:Package>
    <cbc:ID>CON_P_2</cbc:ID>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
    <cac:GoodsItem>
      <cac:Item>
        <cac:CommodityClassification>
          <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Package>
</cac:TransportEquipment>
```

**Structure 15** — 1 instance

```xml
<cac:TransportEquipment>
  <cbc:ID>12345698</cbc:ID>
  <cbc:TransportEquipmentTypeCode>EFP</cbc:TransportEquipmentTypeCode>
  <cbc:GrossWeightMeasure>400</cbc:GrossWeightMeasure>
  <cbc:GrossVolumeMeasure>1.536</cbc:GrossVolumeMeasure>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Width</cbc:AttributeID>
    <cbc:Measure>80</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Length</cbc:AttributeID>
    <cbc:Measure>120</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Height</cbc:AttributeID>
    <cbc:Measure>160</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:GoodsItem>
    <cbc:ID>GoodsItemID1</cbc:ID>
    <cbc:Description>Office Printer 1</cbc:Description>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Name>Office Printer 1</cbc:Name>
      <cbc:BrandName>Canon</cbc:BrandName>
      <cbc:ModelName>ModelName28</cbc:ModelName>
      <cac:CommodityClassification>
        <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:GoodsItem>
  <cac:GoodsItem>
    <cbc:ID>GoodsItemID2</cbc:ID>
    <cbc:Description>Office Printer 2</cbc:Description>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:Quantity>1</cbc:Quantity>
    <cac:Item>
      <cbc:Name>Office Printer 2</cbc:Name>
      <cbc:BrandName>Canon</cbc:BrandName>
      <cbc:ModelName>MPX2000</cbc:ModelName>
      <cac:CommodityClassification>
        <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:GoodsItem>
</cac:TransportEquipment>
```

[↑ Back to contents](#contents)

### `TransportEventType`

**Used as:** `cac:EstimatedArrivalTransportEvent` · `cac:PlannedArrivalTransportEvent` · `cac:PlannedDeliveryTransportEvent` · `cac:PlannedDepartureTransportEvent` · `cac:PlannedPickupTransportEvent` · `cac:RequestedArrivalTransportEvent` · `cac:RequestedDeliveryTransportEvent` · `cac:RequestedDepartureTransportEvent` · `cac:RequestedPickupTransportEvent` · `cac:TransportEvent`

_34 instances across 10 elements, with 25 unique structures_

**Structure 1** — 1 instance

```xml
<cac:EstimatedArrivalTransportEvent>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
    <cbc:EndTime>18:35:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:EstimatedArrivalTransportEvent>
```

**Structure 2** — 1 instance

```xml
<cac:PlannedDeliveryTransportEvent>
  <cac:Location>
    <cbc:ID>ITGOA</cbc:ID>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:PlannedDeliveryTransportEvent>
```

**Structure 3** — 2 instances

```xml
<cac:TransportEvent>
  <cac:CurrentStatus>
    <cbc:ConditionCode>31</cbc:ConditionCode>
    <cbc:Description>En route</cbc:Description>
  </cac:CurrentStatus>
  <cac:Contact>
    <cbc:Name>John Smith</cbc:Name>
    <cbc:ElectronicMail>jsmith@example.com</cbc:ElectronicMail>
  </cac:Contact>
</cac:TransportEvent>
```

**Structure 4** — 1 instance

```xml
<cac:PlannedPickupTransportEvent>
  <cac:Location>
    <cbc:ID>MAPTM</cbc:ID>
    <cac:Address>
      <cbc:CityName>Tanger</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>MA</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:PlannedPickupTransportEvent>
```

**Structure 5** — 1 instance

```xml
<cac:PlannedDepartureTransportEvent>
  <cac:Location>
    <cbc:ID>CNSHA</cbc:ID>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-09-20</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-09-20</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedDepartureTransportEvent>
```

**Structure 6** — 1 instance

```xml
<cac:PlannedArrivalTransportEvent>
  <cac:Location>
    <cbc:ID>DEHAM</cbc:ID>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-01</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-01</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedArrivalTransportEvent>
```

**Structure 7** — 1 instance

```xml
<cac:EstimatedArrivalTransportEvent>
  <cbc:OccurrenceDate>2013-05-25</cbc:OccurrenceDate>
  <cbc:OccurrenceTime>18:00:00+01:00</cbc:OccurrenceTime>
  <cac:Location>
    <cbc:ID>ITGOA</cbc:ID>
    <cbc:LocationTypeCode>24</cbc:LocationTypeCode>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode>IT</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
</cac:EstimatedArrivalTransportEvent>
```

**Structure 8** — 1 instance

```xml
<cac:RequestedArrivalTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-06</cbc:StartDate>
    <cbc:EndDate>2011-10-06</cbc:EndDate>
  </cac:Period>
</cac:RequestedArrivalTransportEvent>
```

**Structure 9** — 2 instances

```xml
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
```

**Structure 10** — 1 instance

```xml
<cac:RequestedDeliveryTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:StreetName>StreetName Example</cbc:StreetName>
      <cbc:CityName>El Dorado</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>PA</cbc:IdentificationCode>
        <cbc:Name>Panama</cbc:Name>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2020-07-01</cbc:StartDate>
    <cbc:EndDate>2020-07-01</cbc:EndDate>
  </cac:Period>
</cac:RequestedDeliveryTransportEvent>
```

**Structure 11** — 1 instance

```xml
<cac:RequestedDepartureTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:ID>DEHAM</cbc:ID>
      <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
      <cbc:CityName>Hamburg</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
  </cac:Period>
</cac:RequestedDepartureTransportEvent>
```

**Structure 12** — 2 instances

```xml
<cac:PlannedArrivalTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-06</cbc:StartDate>
    <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-06</cbc:EndDate>
    <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedArrivalTransportEvent>
```

**Structure 13** — 2 instances

```xml
<cac:PlannedDepartureTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:ID>DEHAM</cbc:ID>
      <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
      <cbc:CityName>Hamburg</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedDepartureTransportEvent>
```

**Structure 14** — 2 instances

```xml
<cac:PlannedDepartureTransportEvent>
  <cac:Location>
    <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-06</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-06</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedDepartureTransportEvent>
```

**Structure 15** — 2 instances

```xml
<cac:PlannedArrivalTransportEvent>
  <cac:Location>
    <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-04</cbc:StartDate>
    <cbc:StartTime>15:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-04</cbc:EndDate>
    <cbc:EndTime>18:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedArrivalTransportEvent>
```

**Structure 16** — 1 instance

```xml
<cac:PlannedArrivalTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cbc:PostalZone>28400</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-06</cbc:StartDate>
    <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-06</cbc:EndDate>
    <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedArrivalTransportEvent>
```

**Structure 17** — 1 instance

```xml
<cac:PlannedDeliveryTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cbc:PostalZone>28400</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-06</cbc:StartDate>
    <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-06</cbc:EndDate>
    <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedDeliveryTransportEvent>
```

**Structure 18** — 1 instance

```xml
<cac:RequestedDeliveryTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
      <cbc:CityName>Nurnberg</cbc:CityName>
      <cbc:PostalZone>28400</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-06</cbc:StartDate>
    <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-06</cbc:EndDate>
    <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:RequestedDeliveryTransportEvent>
```

**Structure 19** — 2 instances

```xml
<cac:PlannedDepartureTransportEvent>
  <cac:Location>
    <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:ID>4568763527610</cbc:ID>
      <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
      <cbc:CityName>Bremen</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-04</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-04</cbc:EndDate>
    <cbc:EndTime>09:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedDepartureTransportEvent>
```

**Structure 20** — 1 instance

```xml
<cac:PlannedDepartureTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:ID>DEHAM</cbc:ID>
      <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
      <cbc:CityName>Hamburg</cbc:CityName>
      <cbc:PostalZone>29400</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedDepartureTransportEvent>
```

**Structure 21** — 2 instances

```xml
<cac:PlannedArrivalTransportEvent>
  <cac:Location>
    <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:ID>4568763527610</cbc:ID>
      <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
      <cbc:CityName>Bremen</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
    <cbc:EndTime>21:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedArrivalTransportEvent>
```

**Structure 22** — 1 instance

```xml
<cac:PlannedPickupTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:ID>DEHAM</cbc:ID>
      <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
      <cbc:CityName>Hamburg</cbc:CityName>
      <cbc:PostalZone>29400</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:PlannedPickupTransportEvent>
```

**Structure 23** — 1 instance

```xml
<cac:RequestedPickupTransportEvent>
  <cac:Location>
    <cac:Address>
      <cbc:ID>DEHAM</cbc:ID>
      <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
      <cbc:CityName>Hamburg</cbc:CityName>
      <cbc:PostalZone>29400</cbc:PostalZone>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2011-10-03</cbc:StartDate>
    <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
    <cbc:EndDate>2011-10-03</cbc:EndDate>
    <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
  </cac:Period>
</cac:RequestedPickupTransportEvent>
```

**Structure 24** — 2 instances

```xml
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
    <cbc:StartTime>07:00:00Z</cbc:StartTime>
    <cbc:EndDate>2016-08-02</cbc:EndDate>
    <cbc:EndTime>15:30:00Z</cbc:EndTime>
  </cac:Period>
</cac:RequestedPickupTransportEvent>
```

**Structure 25** — 1 instance

```xml
<cac:RequestedPickupTransportEvent>
  <cac:Contact>
    <cbc:Name>ExampleName</cbc:Name>
  </cac:Contact>
  <cac:Location>
    <cbc:ID>M165</cbc:ID>
    <cac:Address>
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
    </cac:Address>
  </cac:Location>
  <cac:Period>
    <cbc:StartDate>2020-06-02</cbc:StartDate>
    <cbc:EndDate>2020-06-02</cbc:EndDate>
  </cac:Period>
</cac:RequestedPickupTransportEvent>
```

[↑ Back to contents](#contents)

### `TransportExecutionTermsType`

**Used as:** `cac:TransportExecutionTerms`

_4 instances across 1 element, with 3 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TransportExecutionTerms>
  <cac:PaymentTerms>
    <cbc:Note>PER THIRTY DAYS</cbc:Note>
  </cac:PaymentTerms>
</cac:TransportExecutionTerms>
```

**Structure 2** — 1 instance

```xml
<cac:TransportExecutionTerms>
  <cac:PaymentTerms>
    <cbc:Note>Per thirty days</cbc:Note>
    <cac:SettlementPeriod>
      <cbc:StartDate>2011-03-13</cbc:StartDate>
      <cbc:StartTime>14:00:00.0Z</cbc:StartTime>
      <cbc:EndDate>2011-04-12</cbc:EndDate>
      <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
    </cac:SettlementPeriod>
  </cac:PaymentTerms>
  <cac:DeliveryTerms>
    <cbc:ID>EXW</cbc:ID>
    <cac:DeliveryLocation>
      <cac:Address>
        <cbc:CityName>Munich</cbc:CityName>
      </cac:Address>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:EnvironmentalEmission>
    <cbc:EnvironmentalEmissionTypeCode>CO2</cbc:EnvironmentalEmissionTypeCode>
    <cbc:ValueMeasure>0.2</cbc:ValueMeasure>
    <cbc:Description>200 grams of Carbon Dioxide per km</cbc:Description>
  </cac:EnvironmentalEmission>
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
</cac:TransportExecutionTerms>
```

**Structure 3** — 2 instances

```xml
<cac:TransportExecutionTerms>
  <cac:DeliveryTerms>
    <cbc:ID>EXW</cbc:ID>
    <cac:DeliveryLocation>
      <cac:Address>
        <cbc:CityName>Hamburg</cbc:CityName>
      </cac:Address>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
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
</cac:TransportExecutionTerms>
```

[↑ Back to contents](#contents)

### `TransportHandlingUnitType`

**Used as:** `cac:TransportHandlingUnit`

_28 instances across 1 element, with 13 unique structures_

**Structure 1** — 3 instances

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>ABCD123456-7</cbc:ID>
</cac:TransportHandlingUnit>
```

**Structure 2** — 1 instance

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>CON_THU_1</cbc:ID>
  <cac:TransportEquipment>
    <cbc:ID>CON_TE_1</cbc:ID>
  </cac:TransportEquipment>
  <cac:Status>
    <cbc:ConditionCode>4</cbc:ConditionCode>
    <cbc:StatusReasonCode>23</cbc:StatusReasonCode>
    <cbc:StatusReason>Reefer container lost power - cargo of fish destroyed</cbc:StatusReason>
  </cac:Status>
</cac:TransportHandlingUnit>
```

**Structure 3** — 4 instances

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>1</cbc:ID>
  <cbc:TransportHandlingUnitTypeCode>PA</cbc:TransportHandlingUnitTypeCode>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:TotalGoodsItemQuantity>10</cbc:TotalGoodsItemQuantity>
  <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
  <cac:ActualPackage>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:PackagingTypeCode>TB</cbc:PackagingTypeCode>
  </cac:ActualPackage>
</cac:TransportHandlingUnit>
```

**Structure 4** — 4 instances

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>CON_THU_2</cbc:ID>
  <cac:TransportEquipment>
    <cbc:ID>CON_2</cbc:ID>
    <cac:ContainedInTransportEquipment>
      <cbc:ID>NEC_TE_2</cbc:ID>
      <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
      <cbc:TraceID>12345678914543</cbc:TraceID>
    </cac:ContainedInTransportEquipment>
    <cac:Package>
      <cbc:ID>CON_2</cbc:ID>
      <cbc:Quantity>10</cbc:Quantity>
    </cac:Package>
  </cac:TransportEquipment>
</cac:TransportHandlingUnit>
```

**Structure 5** — 2 instances

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>EXT_THU_2</cbc:ID>
  <cac:TransportEquipment>
    <cbc:ID>CON_2</cbc:ID>
    <cac:ContainedInTransportEquipment>
      <cbc:ID>EXT_TE_2</cbc:ID>
      <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
      <cbc:TraceID>12345678914112</cbc:TraceID>
    </cac:ContainedInTransportEquipment>
    <cac:Package>
      <cbc:ID>CON_2</cbc:ID>
      <cbc:Quantity>10</cbc:Quantity>
    </cac:Package>
  </cac:TransportEquipment>
  <cac:TransportMeans>
    <cac:RoadTransport>
      <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
    </cac:RoadTransport>
  </cac:TransportMeans>
</cac:TransportHandlingUnit>
```

**Structure 6** — 1 instance

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>THU_1</cbc:ID>
  <cbc:TransportHandlingUnitTypeCode>122</cbc:TransportHandlingUnitTypeCode>
  <cbc:HandlingCode>23</cbc:HandlingCode>
  <cbc:HandlingInstructions>HANDLE WITH CARE</cbc:HandlingInstructions>
  <cac:TransportEquipment>
    <cbc:ID>TE_1</cbc:ID>
    <cbc:TransportEquipmentTypeCode>AE</cbc:TransportEquipmentTypeCode>
    <cbc:Description>BODY TRAILER</cbc:Description>
    <cbc:GrossWeightMeasure>1000.0</cbc:GrossWeightMeasure>
    <cac:GoodsItem>
      <cbc:ID>GID_1</cbc:ID>
      <cac:Item>
        <cbc:Description>MOTOR CYCLE</cbc:Description>
        <cbc:Name>YAMAHA</cbc:Name>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>GID_2</cbc:ID>
      <cac:Item>
        <cbc:Description>MOTOR CYCLE</cbc:Description>
        <cbc:Name>HONDA</cbc:Name>
      </cac:Item>
    </cac:GoodsItem>
  </cac:TransportEquipment>
</cac:TransportHandlingUnit>
```

**Structure 7** — 2 instances

```xml
<cac:TransportHandlingUnit>
  <cac:TransportEquipment>
    <cbc:ID>TRHU1652173</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
    <cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
    <cac:VerifiedGrossMass>
      <cbc:ID>123</cbc:ID>
      <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
      <cbc:WeighingTime>00:30:00Z</cbc:WeighingTime>
      <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
      <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
      <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
      <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
      <cac:DocumentReference>
        <cbc:ID>W123</cbc:ID>
        <cbc:IssueDate>2016-11-02</cbc:IssueDate>
        <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
        <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
      </cac:DocumentReference>
    </cac:VerifiedGrossMass>
  </cac:TransportEquipment>
  <cac:ShipmentDocumentReference>
    <cbc:ID>GOA294107</cbc:ID>
    <cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
  </cac:ShipmentDocumentReference>
</cac:TransportHandlingUnit>
```

**Structure 8** — 1 instance

```xml
<cac:TransportHandlingUnit>
  <cac:TransportEquipment>
    <cbc:ID>TRHU1652173</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cbc:SizeTypeCode>22G1</cbc:SizeTypeCode>
    <cbc:FullnessIndicationCode>5</cbc:FullnessIndicationCode>
    <cac:VerifiedGrossMass>
      <cbc:ID>123</cbc:ID>
      <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
      <cbc:WeighingTime>00:30:00</cbc:WeighingTime>
      <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
      <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
      <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
      <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
      <cac:DocumentReference>
        <cbc:ID>W123</cbc:ID>
        <cbc:IssueDate>2016-11-02</cbc:IssueDate>
        <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
        <cbc:DocumentType></cbc:DocumentType>
        <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
      </cac:DocumentReference>
    </cac:VerifiedGrossMass>
  </cac:TransportEquipment>
  <cac:ShipmentDocumentReference>
    <cbc:ID>GOA294107</cbc:ID>
    <cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
  </cac:ShipmentDocumentReference>
</cac:TransportHandlingUnit>
```

**Structure 9** — 2 instances

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>CON_THU_1</cbc:ID>
  <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:ShippingMarks>Agricultural products</cbc:ShippingMarks>
  <cac:TransportEquipment>
    <cbc:ID>BFCU4040001</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
    <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
    <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
    <cbc:Description>Should have a temperature between 2-4 degrees celcius</cbc:Description>
    <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
    <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
    <cbc:PowerIndicator>true</cbc:PowerIndicator>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>6.1</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>2.6</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>2.44</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:GoodsItem>
      <cac:Item>
        <cac:CommodityClassification>
          <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
          <cbc:CommodityCode>8</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:TransportEquipment>
</cac:TransportHandlingUnit>
```

**Structure 10** — 4 instances

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>CON_THU_1</cbc:ID>
  <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
  <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
  <cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
  <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
  <cbc:ShippingMarks>General Cargo</cbc:ShippingMarks>
  <cac:TransportEquipment>
    <cbc:ID>CON_TE_1</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cbc:FullnessIndicationCode>1</cbc:FullnessIndicationCode>
    <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
    <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
    <cbc:Description>SomeDescription</cbc:Description>
    <cbc:GrossWeightMeasure>25000</cbc:GrossWeightMeasure>
    <cbc:GrossVolumeMeasure>39</cbc:GrossVolumeMeasure>
    <cbc:PowerIndicator>false</cbc:PowerIndicator>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>6.1</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>2.6</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>2.44</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:Package>
      <cbc:ID>CON_P_1</cbc:ID>
      <cbc:Quantity>10</cbc:Quantity>
      <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
      <cac:GoodsItem>
        <cac:Item>
          <cac:CommodityClassification>
            <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:Package>
  </cac:TransportEquipment>
</cac:TransportHandlingUnit>
```

**Structure 11** — 1 instance

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>THU1</cbc:ID>
  <cbc:TransportHandlingUnitTypeCode>Palletized cargo</cbc:TransportHandlingUnitTypeCode>
  <cbc:TotalGoodsItemQuantity>2</cbc:TotalGoodsItemQuantity>
  <cbc:TotalPackageQuantity>2</cbc:TotalPackageQuantity>
  <cac:TransportEquipment>
    <cbc:ID>12345698</cbc:ID>
    <cbc:TransportEquipmentTypeCode>EFP</cbc:TransportEquipmentTypeCode>
    <cbc:GrossWeightMeasure>400</cbc:GrossWeightMeasure>
    <cbc:GrossVolumeMeasure>1.536</cbc:GrossVolumeMeasure>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>80</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>120</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>160</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:GoodsItem>
      <cbc:ID>GoodsItemID1</cbc:ID>
      <cbc:Description>Office Printer 1</cbc:Description>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
      <cbc:Quantity>1</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Office Printer 1</cbc:Name>
        <cbc:BrandName>Canon</cbc:BrandName>
        <cbc:ModelName>ModelName28</cbc:ModelName>
        <cac:CommodityClassification>
          <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>GoodsItemID2</cbc:ID>
      <cbc:Description>Office Printer 2</cbc:Description>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
      <cbc:Quantity>1</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Office Printer 2</cbc:Name>
        <cbc:BrandName>Canon</cbc:BrandName>
        <cbc:ModelName>MPX2000</cbc:ModelName>
        <cac:CommodityClassification>
          <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:TransportEquipment>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Width</cbc:AttributeID>
    <cbc:Measure>80</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Length</cbc:AttributeID>
    <cbc:Measure>120</cbc:Measure>
  </cac:MeasurementDimension>
  <cac:MeasurementDimension>
    <cbc:AttributeID>Height</cbc:AttributeID>
    <cbc:Measure>160</cbc:Measure>
  </cac:MeasurementDimension>
</cac:TransportHandlingUnit>
```

**Structure 12** — 2 instances

```xml
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
```

**Structure 13** — 1 instance

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>USRM3656679</cbc:ID>
  <cbc:TotalPackageQuantity>1</cbc:TotalPackageQuantity>
  <cac:TransportEquipment>
    <cac:TransportEquipmentSeal>
      <cbc:ID>7654321</cbc:ID>
    </cac:TransportEquipmentSeal>
  </cac:TransportEquipment>
  <cac:MaximumTemperature>
    <cbc:AttributeID>TC</cbc:AttributeID>
    <cbc:Measure>3.00</cbc:Measure>
    <cbc:Description>Chilled</cbc:Description>
  </cac:MaximumTemperature>
  <cac:Package>
    <cbc:ID>2076084807</cbc:ID>
    <cbc:Quantity>1</cbc:Quantity>
    <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
    <cac:GoodsItem>
      <cbc:ID>000010</cbc:ID>
      <cbc:GrossWeightMeasure>774.14400</cbc:GrossWeightMeasure>
      <cbc:NetWeightMeasure>604.80000</cbc:NetWeightMeasure>
      <cbc:Quantity>63.000</cbc:Quantity>
      <cac:Item>
        <cbc:Description>ItemExample</cbc:Description>
        <cbc:PackQuantity>63</cbc:PackQuantity>
        <cbc:Name>Dairy Products</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>123456</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>DK</cbc:IdentificationCode>
          <cbc:Name>Denmark</cbc:Name>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode>19011000</cbc:CommodityCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>AnimalSpecies</cbc:Name>
          <cbc:Value>Bovine</cbc:Value>
        </cac:AdditionalItemProperty>
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
        <cac:ItemInstance>
          <cbc:ManufactureDate>2019-12-08</cbc:ManufactureDate>
          <cbc:BestBeforeDate>2022-12-08</cbc:BestBeforeDate>
          <cac:AdditionalItemProperty>
            <cbc:Name>LineNetWeight</cbc:Name>
            <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>LineGrossWeight</cbc:Name>
            <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>Quantity</cbc:Name>
            <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
          </cac:AdditionalItemProperty>
          <cac:LotIdentification>
            <cbc:LotNumberID>9390000757</cbc:LotNumberID>
          </cac:LotIdentification>
        </cac:ItemInstance>
        <cac:Dimension>
          <cbc:AttributeID>NetWeight</cbc:AttributeID>
          <cbc:Measure>9.6</cbc:Measure>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
          <cbc:Measure>604.8</cbc:Measure>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID>GrossWeight</cbc:AttributeID>
          <cbc:Measure>12.288</cbc:Measure>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
          <cbc:Measure>774.144</cbc:Measure>
        </cac:Dimension>
      </cac:Item>
      <cac:Despatch>
        <cbc:ID>000010</cbc:ID>
      </cac:Despatch>
      <cac:MaximumTemperature>
        <cbc:AttributeID>TC</cbc:AttributeID>
        <cbc:Measure>3.00</cbc:Measure>
        <cbc:Description>Chilled</cbc:Description>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:MeasurementDimension>
      <cbc:AttributeID>GrossWeight</cbc:AttributeID>
      <cbc:Measure>774.14400</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>NetWeight</cbc:AttributeID>
      <cbc:Measure>604.80000</cbc:Measure>
    </cac:MeasurementDimension>
  </cac:Package>
</cac:TransportHandlingUnit>
```

[↑ Back to contents](#contents)

### `TransportMeansType`

**Used as:** `cac:TransportMeans`

_25 instances across 1 element, with 12 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TransportMeans>
  <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
</cac:TransportMeans>
```

**Structure 2** — 2 instances

```xml
<cac:TransportMeans>
  <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
</cac:TransportMeans>
```

**Structure 3** — 6 instances

```xml
<cac:TransportMeans>
  <cac:RoadTransport>
    <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:TransportMeans>
```

**Structure 4** — 1 instance

```xml
<cac:TransportMeans>
  <cac:RailTransport>
    <cbc:TrainID>VF80145</cbc:TrainID>
  </cac:RailTransport>
</cac:TransportMeans>
```

**Structure 5** — 4 instances

```xml
<cac:TransportMeans>
  <cbc:JourneyID>UA 1234</cbc:JourneyID>
  <cac:AirTransport>
    <cbc:AircraftID>A-127763-747</cbc:AircraftID>
  </cac:AirTransport>
</cac:TransportMeans>
```

**Structure 6** — 2 instances

```xml
<cac:TransportMeans>
  <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
  <cac:AirTransport>
    <cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
  </cac:AirTransport>
</cac:TransportMeans>
```

**Structure 7** — 2 instances

```xml
<cac:TransportMeans>
  <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
  <cac:RoadTransport>
    <cbc:LicensePlateID>PBB-123</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:TransportMeans>
```

**Structure 8** — 1 instance

```xml
<cac:TransportMeans>
  <cbc:TransportMeansTypeCode>Train, with more than 20 wagons</cbc:TransportMeansTypeCode>
  <cac:RailTransport>
    <cbc:TrainID>101</cbc:TrainID>
    <cbc:RailCarID>101-21</cbc:RailCarID>
  </cac:RailTransport>
</cac:TransportMeans>
```

**Structure 9** — 2 instances

```xml
<cac:TransportMeans>
  <cbc:JourneyID>TM1</cbc:JourneyID>
  <cbc:RegistrationNationalityID>EE</cbc:RegistrationNationalityID>
  <cac:MaritimeTransport>
    <cbc:VesselID>Eestiship</cbc:VesselID>
  </cac:MaritimeTransport>
</cac:TransportMeans>
```

**Structure 10** — 2 instances

```xml
<cac:TransportMeans>
  <cbc:JourneyID>RHamBrem</cbc:JourneyID>
  <cbc:RegistrationNationalityID>DE</cbc:RegistrationNationalityID>
  <cbc:TransportMeansTypeCode>230</cbc:TransportMeansTypeCode>
  <cac:RailTransport>
    <cbc:TrainID>RID01235</cbc:TrainID>
  </cac:RailTransport>
</cac:TransportMeans>
```

**Structure 11** — 1 instance

```xml
<cac:TransportMeans>
  <cbc:JourneyID>00344</cbc:JourneyID>
  <cbc:RegistrationNationalityID>IT</cbc:RegistrationNationalityID>
  <cac:MaritimeTransport>
    <cbc:VesselID>3852664</cbc:VesselID>
    <cbc:VesselName>Vessel Name</cbc:VesselName>
  </cac:MaritimeTransport>
</cac:TransportMeans>
```

**Structure 12** — 1 instance

```xml
<cac:TransportMeans>
  <cbc:JourneyID>M22</cbc:JourneyID>
  <cbc:RegistrationNationalityID>DK</cbc:RegistrationNationalityID>
  <cbc:RegistrationNationality>Denmark</cbc:RegistrationNationality>
  <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
  <cac:MaritimeTransport>
    <cbc:VesselID>SomeIMONr</cbc:VesselID>
    <cbc:VesselName>SomeVesselName</cbc:VesselName>
  </cac:MaritimeTransport>
</cac:TransportMeans>
```

[↑ Back to contents](#contents)

### `TransportScheduleType`

**Used as:** `cac:TransportSchedule`

_2 instances across 1 element, with 2 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TransportSchedule>
  <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
  <cbc:ReliabilityPercent>80</cbc:ReliabilityPercent>
  <cac:StatusLocation>
    <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
    <cac:Address>
      <cbc:ID>4568763527610</cbc:ID>
      <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
      <cbc:CityName>Bremen</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>DE</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:StatusLocation>
  <cac:EstimatedArrivalTransportEvent>
    <cac:Period>
      <cbc:StartDate>2011-10-03</cbc:StartDate>
      <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
      <cbc:EndDate>2011-10-03</cbc:EndDate>
      <cbc:EndTime>18:35:10+01:00</cbc:EndTime>
    </cac:Period>
  </cac:EstimatedArrivalTransportEvent>
</cac:TransportSchedule>
```

**Structure 2** — 1 instance

```xml
<cac:TransportSchedule>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:ReferenceDate>2011-03-13</cbc:ReferenceDate>
  <cbc:ReferenceTime>18:55:00.0Z</cbc:ReferenceTime>
  <cbc:ReliabilityPercent>80</cbc:ReliabilityPercent>
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
        <cbc:Name>Germany</cbc:Name>
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
  <cac:EstimatedArrivalPeriod>
    <cbc:StartDate>2011-03-13</cbc:StartDate>
    <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-03-13</cbc:EndDate>
    <cbc:EndTime>21:10:00.0Z</cbc:EndTime>
  </cac:EstimatedArrivalPeriod>
</cac:TransportSchedule>
```

[↑ Back to contents](#contents)

### `TransportationSegmentType`

**Used as:** `cac:TransportationSegment`

_7 instances across 1 element, with 7 unique structures_

**Structure 1** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumberID>4</cbc:SequenceNumberID>
  <cbc:TransportExecutionPlanReferenceID>TEPID_1_4</cbc:TransportExecutionPlanReferenceID>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  </cac:TransportationService>
  <cac:TransportServiceProviderParty>
    <cac:PartyName>
      <cbc:Name>ROAD CARRIER 2</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>Jan Peter Clausen</cbc:Name>
      <cbc:Telephone>+4793774465</cbc:Telephone>
      <cbc:ElectronicMail>janpc@ROADCARRIER2.no</cbc:ElectronicMail>
    </cac:Contact>
  </cac:TransportServiceProviderParty>
  <cac:CarryingTransportMeans>
    <cbc:TransportMeansTypeCode>31</cbc:TransportMeansTypeCode>
    <cac:RoadTransport>
      <cbc:LicensePlateID>VE80044</cbc:LicensePlateID>
    </cac:RoadTransport>
  </cac:CarryingTransportMeans>
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
</cac:TransportationSegment>
```

**Structure 2** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:TransportExecutionPlanReferenceID>TEPID_1_1</cbc:TransportExecutionPlanReferenceID>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  </cac:TransportationService>
  <cac:TransportServiceProviderParty>
    <cac:PartyName>
      <cbc:Name>ROAD CARRIER</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>Peter Janssen</cbc:Name>
      <cbc:Telephone>+4987675432</cbc:Telephone>
      <cbc:ElectronicMail>peter@ROADCARRIER.de</cbc:ElectronicMail>
    </cac:Contact>
  </cac:TransportServiceProviderParty>
  <cac:CarryingTransportMeans>
    <cbc:TransportMeansTypeCode>31</cbc:TransportMeansTypeCode>
    <cac:RoadTransport>
      <cbc:LicensePlateID>KA04401</cbc:LicensePlateID>
    </cac:RoadTransport>
  </cac:CarryingTransportMeans>
  <cac:DepartureTransportLocation>
    <cac:PlannedDeparturePeriod>
      <cbc:StartDate>2011-03-13</cbc:StartDate>
      <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
      <cbc:EndDate>2011-03-13</cbc:EndDate>
      <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
    </cac:PlannedDeparturePeriod>
    <cac:Location>
      <cbc:ID>123465</cbc:ID>
      <cbc:LocationTypeCode>Place of despatch</cbc:LocationTypeCode>
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
</cac:TransportationSegment>
```

**Structure 3** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumberID>2</cbc:SequenceNumberID>
  <cbc:TransportExecutionPlanReferenceID>TEPID_1_2</cbc:TransportExecutionPlanReferenceID>
  <cbc:TransportModeCode>2</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>Train, with more than 20 wagons</cbc:TransportMeansTypeCode>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  </cac:TransportationService>
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
  <cac:CarryingTransportMeans>
    <cbc:TransportMeansTypeCode>2305</cbc:TransportMeansTypeCode>
    <cac:RailTransport>
      <cbc:TrainID>101</cbc:TrainID>
      <cbc:RailCarID>101-21</cbc:RailCarID>
    </cac:RailTransport>
  </cac:CarryingTransportMeans>
  <cac:DepartureTransportLocation>
    <cac:PlannedDeparturePeriod>
      <cbc:StartDate>2011-03-13</cbc:StartDate>
      <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
      <cbc:EndDate>2011-03-13</cbc:EndDate>
      <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
    </cac:PlannedDeparturePeriod>
    <cac:Location>
      <cbc:ID>987456123</cbc:ID>
      <cbc:LocationTypeCode>Place of transhipment</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:StreetName>Volkerstrasse 6</cbc:StreetName>
        <cbc:CityName>Munich</cbc:CityName>
        <cbc:PostalZone>80334</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
  </cac:DepartureTransportLocation>
  <cac:ArrivalTransportLocation>
    <cac:PlannedArrivalPeriod>
      <cbc:StartDate>2011-03-13</cbc:StartDate>
      <cbc:StartTime>20:00:00.0Z</cbc:StartTime>
      <cbc:EndDate>2011-03-13</cbc:EndDate>
      <cbc:EndTime>20:30:00.0Z</cbc:EndTime>
    </cac:PlannedArrivalPeriod>
    <cac:Location>
      <cbc:ID>DEBREV</cbc:ID>
      <cbc:Description>Port of Bremerhaven</cbc:Description>
      <cbc:LocationTypeCode>34</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:StreetName>Hansestadt Bremisches</cbc:StreetName>
        <cbc:CityName>Bremen</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
  </cac:ArrivalTransportLocation>
</cac:TransportationSegment>
```

**Structure 4** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumberID>3</cbc:SequenceNumberID>
  <cbc:TransportExecutionPlanReferenceID>TEPID_1_3</cbc:TransportExecutionPlanReferenceID>
  <cbc:TransportModeCode>1</cbc:TransportModeCode>
  <cbc:TransportMeansTypeCode>Container vessel</cbc:TransportMeansTypeCode>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  </cac:TransportationService>
  <cac:TransportServiceProviderParty>
    <cac:PartyName>
      <cbc:Name>SEA CARRIER</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>Horst Tappert</cbc:Name>
      <cbc:Telephone>+4987675652</cbc:Telephone>
      <cbc:ElectronicMail>horst@SEACARRIER.de</cbc:ElectronicMail>
    </cac:Contact>
  </cac:TransportServiceProviderParty>
  <cac:CarryingTransportMeans>
    <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
    <cac:MaritimeTransport>
      <cbc:VesselID>IMO1234567</cbc:VesselID>
      <cbc:VesselName>MS Enova</cbc:VesselName>
    </cac:MaritimeTransport>
  </cac:CarryingTransportMeans>
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
  <cac:ArrivalTransportLocation>
    <cac:PlannedArrivalPeriod>
      <cbc:StartDate>2011-03-14</cbc:StartDate>
      <cbc:StartTime>10:30:00.0Z</cbc:StartTime>
      <cbc:EndDate>2011-03-14</cbc:EndDate>
      <cbc:EndTime>11:00:00.0Z</cbc:EndTime>
    </cac:PlannedArrivalPeriod>
    <cac:Location>
      <cbc:ID>NOOSL</cbc:ID>
      <cbc:Description>Port of Oslo</cbc:Description>
      <cbc:LocationTypeCode>Baseport of discharge</cbc:LocationTypeCode>
      <cac:Address>
        <cbc:StreetName>Akershusstranda 19</cbc:StreetName>
        <cbc:CityName>Oslo</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>NO</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:Location>
  </cac:ArrivalTransportLocation>
</cac:TransportationSegment>
```

**Structure 5** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
  <cbc:TransportExecutionPlanReferenceID>TEP_1</cbc:TransportExecutionPlanReferenceID>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
    <cbc:TransportationServiceDescription>Rail transport service from Bremen to Nurnberg</cbc:TransportationServiceDescription>
  </cac:TransportationService>
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
  <cac:ReferencedConsignment>
    <cbc:ID>CON_1</cbc:ID>
    <cac:TransportHandlingUnit>
      <cbc:ID>CON_THU_1</cbc:ID>
      <cac:TransportEquipment>
        <cbc:ID>CON_1</cbc:ID>
        <cac:ContainedInTransportEquipment>
          <cbc:ID>NEC_TE_1</cbc:ID>
          <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
          <cbc:TraceID>12345678914542</cbc:TraceID>
        </cac:ContainedInTransportEquipment>
        <cac:Package>
          <cbc:ID>CON_1</cbc:ID>
          <cbc:Quantity>10</cbc:Quantity>
        </cac:Package>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>CON_THU_2</cbc:ID>
      <cac:TransportEquipment>
        <cbc:ID>CON_2</cbc:ID>
        <cac:ContainedInTransportEquipment>
          <cbc:ID>NEC_TE_2</cbc:ID>
          <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
          <cbc:TraceID>12345678914543</cbc:TraceID>
        </cac:ContainedInTransportEquipment>
        <cac:Package>
          <cbc:ID>CON_2</cbc:ID>
          <cbc:Quantity>10</cbc:Quantity>
        </cac:Package>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:ReferencedConsignment>
  <cac:ShipmentStage>
    <cbc:ID>2</cbc:ID>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:ID>4568763527610</cbc:ID>
          <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
          <cbc:CityName>Bremen</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-04</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-04</cbc:EndDate>
        <cbc:EndTime>09:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-04</cbc:StartDate>
        <cbc:StartTime>15:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-04</cbc:EndDate>
        <cbc:EndTime>18:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:ShipmentStage>
</cac:TransportationSegment>
```

**Structure 6** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
  <cbc:TransportExecutionPlanReferenceID>TEP_2</cbc:TransportExecutionPlanReferenceID>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
    <cbc:TransportationServiceDescription>Rail transport service from Hamburg to Bremen</cbc:TransportationServiceDescription>
  </cac:TransportationService>
  <cac:TransportServiceProviderParty>
    <cac:PartyIdentification>
      <cbc:ID>4058673827100</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>NTT</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>SomeName</cbc:Name>
      <cbc:Telephone>+49450557777</cbc:Telephone>
      <cbc:ElectronicMail>SomeName@ntt.de</cbc:ElectronicMail>
    </cac:Contact>
  </cac:TransportServiceProviderParty>
  <cac:ReferencedConsignment>
    <cbc:ID>NTT_1</cbc:ID>
    <cac:TransportHandlingUnit>
      <cbc:ID>NTT_THU_1</cbc:ID>
      <cac:TransportEquipment>
        <cbc:ID>NTT_THU_1</cbc:ID>
        <cac:ContainedInTransportEquipment>
          <cbc:ID>NTT_TE_1</cbc:ID>
          <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
          <cbc:TraceID>12345678914564</cbc:TraceID>
        </cac:ContainedInTransportEquipment>
        <cac:Package>
          <cbc:ID>CON_1</cbc:ID>
          <cbc:Quantity>10</cbc:Quantity>
        </cac:Package>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>NTT_THU_2</cbc:ID>
      <cac:TransportEquipment>
        <cbc:ID>CON_2</cbc:ID>
        <cac:ContainedInTransportEquipment>
          <cbc:ID>NTT_TE_2</cbc:ID>
          <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
          <cbc:TraceID>12345678914565</cbc:TraceID>
        </cac:ContainedInTransportEquipment>
        <cac:Package>
          <cbc:ID>CON_2</cbc:ID>
          <cbc:Quantity>10</cbc:Quantity>
        </cac:Package>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:ReferencedConsignment>
  <cac:ShipmentStage>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportModeCode>2</cbc:TransportModeCode>
    <cbc:TransportMeansTypeCode>230</cbc:TransportMeansTypeCode>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:ID>DEHAM</cbc:ID>
          <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
          <cbc:CityName>Hamburg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-03</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-03</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:ID>4568763527610</cbc:ID>
          <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
          <cbc:CityName>Bremen</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-03</cbc:StartDate>
        <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-03</cbc:EndDate>
        <cbc:EndTime>21:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:ShipmentStage>
</cac:TransportationSegment>
```

**Structure 7** — 1 instance

```xml
<cac:TransportationSegment>
  <cbc:SequenceNumeric>3</cbc:SequenceNumeric>
  <cbc:TransportExecutionPlanReferenceID>TEP_3</cbc:TransportExecutionPlanReferenceID>
  <cac:TransportationService>
    <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
    <cbc:TransportationServiceDescription>Road transport service from Hamburg to Bremen</cbc:TransportationServiceDescription>
  </cac:TransportationService>
  <cac:TransportServiceProviderParty>
    <cac:PartyIdentification>
      <cbc:ID>4058673827112</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>EXT-HAL</cbc:Name>
    </cac:PartyName>
    <cac:Contact>
      <cbc:Name>SomeName</cbc:Name>
      <cbc:Telephone>+49450557234</cbc:Telephone>
      <cbc:ElectronicMail>SomeName@ext-hal.de</cbc:ElectronicMail>
    </cac:Contact>
  </cac:TransportServiceProviderParty>
  <cac:ReferencedConsignment>
    <cbc:ID>EXT_1</cbc:ID>
    <cac:TransportHandlingUnit>
      <cbc:ID>EXT_THU_1</cbc:ID>
      <cac:TransportEquipment>
        <cbc:ID>CON_1</cbc:ID>
        <cac:ContainedInTransportEquipment>
          <cbc:ID>EXT_TE_1</cbc:ID>
          <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
          <cbc:TraceID>12345678914111</cbc:TraceID>
        </cac:ContainedInTransportEquipment>
        <cac:Package>
          <cbc:ID>CON_1</cbc:ID>
          <cbc:Quantity>10</cbc:Quantity>
        </cac:Package>
      </cac:TransportEquipment>
      <cac:TransportMeans>
        <cac:RoadTransport>
          <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
        </cac:RoadTransport>
      </cac:TransportMeans>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>EXT_THU_2</cbc:ID>
      <cac:TransportEquipment>
        <cbc:ID>CON_2</cbc:ID>
        <cac:ContainedInTransportEquipment>
          <cbc:ID>EXT_TE_2</cbc:ID>
          <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
          <cbc:TraceID>12345678914112</cbc:TraceID>
        </cac:ContainedInTransportEquipment>
        <cac:Package>
          <cbc:ID>CON_2</cbc:ID>
          <cbc:Quantity>10</cbc:Quantity>
        </cac:Package>
      </cac:TransportEquipment>
      <cac:TransportMeans>
        <cac:RoadTransport>
          <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
        </cac:RoadTransport>
      </cac:TransportMeans>
    </cac:TransportHandlingUnit>
  </cac:ReferencedConsignment>
  <cac:ShipmentStage>
    <cbc:ID>3</cbc:ID>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-06</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-06</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-06</cbc:StartDate>
        <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-06</cbc:EndDate>
        <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:ShipmentStage>
</cac:TransportationSegment>
```

[↑ Back to contents](#contents)

### `TransportationServiceType`

**Used as:** `cac:AdditionalTransportationService` · `cac:FinalDeliveryTransportationService` · `cac:MainTransportationService` · `cac:OriginalDespatchTransportationService` · `cac:TransportationService`

_24 instances across 5 elements, with 8 unique structures_

**Structure 1** — 4 instances

```xml
<cac:OriginalDespatchTransportationService>
  <cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
</cac:OriginalDespatchTransportationService>
```

**Structure 2** — 4 instances

```xml
<cac:FinalDeliveryTransportationService>
  <cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
</cac:FinalDeliveryTransportationService>
```

**Structure 3** — 4 instances

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
</cac:TransportationService>
```

**Structure 4** — 5 instances

```xml
<cac:MainTransportationService>
  <cbc:TransportServiceCode>12</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>CARRIER SERVICE</cbc:TransportationServiceDescription>
</cac:MainTransportationService>
```

**Structure 5** — 3 instances

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Rail transport service from Bremen to Nurnberg</cbc:TransportationServiceDescription>
</cac:TransportationService>
```

**Structure 6** — 2 instances

```xml
<cac:AdditionalTransportationService>
  <cbc:TransportServiceCode>Insurance</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Insurance of goods during transportation</cbc:TransportationServiceDescription>
</cac:AdditionalTransportationService>
```

**Structure 7** — 1 instance

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cac:TransportEquipment>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>6.1</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>2.6</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>2.44</cbc:Measure>
    </cac:MeasurementDimension>
  </cac:TransportEquipment>
  <cac:TransportEquipment>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>6.1</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>2.6</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>2.44</cbc:Measure>
    </cac:MeasurementDimension>
  </cac:TransportEquipment>
  <cac:ShipmentStage>
    <cbc:ID>1</cbc:ID>
    <cac:RequestedDepartureTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:ID>DEHAM</cbc:ID>
          <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
          <cbc:CityName>Hamburg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-03</cbc:StartDate>
        <cbc:EndDate>2011-10-03</cbc:EndDate>
      </cac:Period>
    </cac:RequestedDepartureTransportEvent>
    <cac:RequestedArrivalTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-06</cbc:StartDate>
        <cbc:EndDate>2011-10-06</cbc:EndDate>
      </cac:Period>
    </cac:RequestedArrivalTransportEvent>
  </cac:ShipmentStage>
</cac:TransportationService>
```

**Structure 8** — 1 instance

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cac:SupportedTransportEquipment>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>6.1</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>2.6</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>2.44</cbc:Measure>
    </cac:MeasurementDimension>
  </cac:SupportedTransportEquipment>
  <cac:SupportedTransportEquipment>
    <cbc:ID>1</cbc:ID>
    <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Length</cbc:AttributeID>
      <cbc:Measure>6.1</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Height</cbc:AttributeID>
      <cbc:Measure>2.6</cbc:Measure>
    </cac:MeasurementDimension>
    <cac:MeasurementDimension>
      <cbc:AttributeID>Width</cbc:AttributeID>
      <cbc:Measure>2.44</cbc:Measure>
    </cac:MeasurementDimension>
  </cac:SupportedTransportEquipment>
  <cac:ShipmentStage>
    <cbc:ID>1</cbc:ID>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:ID>DEHAM</cbc:ID>
          <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
          <cbc:CityName>Hamburg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-03</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-03</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:ID>4568763527610</cbc:ID>
          <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
          <cbc:CityName>Bremen</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-03</cbc:StartDate>
        <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-03</cbc:EndDate>
        <cbc:EndTime>21:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:ShipmentStage>
  <cac:ShipmentStage>
    <cbc:ID>2</cbc:ID>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:ID>4568763527610</cbc:ID>
          <cbc:StreetName>Ludwig-Erhard-Str. 15</cbc:StreetName>
          <cbc:CityName>Bremen</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-04</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-04</cbc:EndDate>
        <cbc:EndTime>09:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-04</cbc:StartDate>
        <cbc:StartTime>15:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-04</cbc:EndDate>
        <cbc:EndTime>18:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:ShipmentStage>
  <cac:ShipmentStage>
    <cbc:ID>3</cbc:ID>
    <cac:PlannedDepartureTransportEvent>
      <cac:Location>
        <cbc:LocationTypeCode>13</cbc:LocationTypeCode>
        <cac:Address>
          <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-06</cbc:StartDate>
        <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-06</cbc:EndDate>
        <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedDepartureTransportEvent>
    <cac:PlannedArrivalTransportEvent>
      <cac:Location>
        <cac:Address>
          <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
          <cbc:CityName>Nurnberg</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>DE</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
      <cac:Period>
        <cbc:StartDate>2011-10-06</cbc:StartDate>
        <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
        <cbc:EndDate>2011-10-06</cbc:EndDate>
        <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
      </cac:Period>
    </cac:PlannedArrivalTransportEvent>
  </cac:ShipmentStage>
</cac:TransportationService>
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

### `VerifiedGrossMassType`

**Used as:** `cac:VerifiedGrossMass`

_3 instances across 1 element, with 2 unique structures_

**Structure 1** — 2 instances

```xml
<cac:VerifiedGrossMass>
  <cbc:ID>123</cbc:ID>
  <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
  <cbc:WeighingTime>00:30:00Z</cbc:WeighingTime>
  <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
  <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
  <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
  <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
  <cac:DocumentReference>
    <cbc:ID>W123</cbc:ID>
    <cbc:IssueDate>2016-11-02</cbc:IssueDate>
    <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
  </cac:DocumentReference>
</cac:VerifiedGrossMass>
```

**Structure 2** — 1 instance

```xml
<cac:VerifiedGrossMass>
  <cbc:ID>123</cbc:ID>
  <cbc:WeighingDate>2016-11-01</cbc:WeighingDate>
  <cbc:WeighingTime>00:30:00</cbc:WeighingTime>
  <cbc:WeighingMethodCode>SM1</cbc:WeighingMethodCode>
  <cbc:WeighingDeviceID>TS12345</cbc:WeighingDeviceID>
  <cbc:WeighingDeviceType>Truck Scale</cbc:WeighingDeviceType>
  <cbc:GrossMassMeasure>25730</cbc:GrossMassMeasure>
  <cac:DocumentReference>
    <cbc:ID>W123</cbc:ID>
    <cbc:IssueDate>2016-11-02</cbc:IssueDate>
    <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
    <cbc:DocumentType></cbc:DocumentType>
    <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
  </cac:DocumentReference>
</cac:VerifiedGrossMass>
```

[↑ Back to contents](#contents)

### `WebSiteType`

**Used as:** `cac:AdditionalWebSite`

_2 instances across 1 element, with 1 unique structure_

**Structure 1** — 2 instances

```xml
<cac:AdditionalWebSite>
  <cbc:ID>1</cbc:ID>
  <cbc:Name>RSS</cbc:Name>
  <cbc:URI>https://www.oasis-open.org/feed</cbc:URI>
</cac:AdditionalWebSite>
```

[↑ Back to contents](#contents)
