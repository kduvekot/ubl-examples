# UBL Element Reference

Values, attributes, and composite instances observed across all official UBL example documents (2.0 – 2.5), grouped using the UBL 2.5 CSD02 XSD as the authoritative type reference.

## Summary

| | Count |
|---|---|
| `cbc` elements (in examples) | **388** |
| `cbc` unique values | **2272** |
| `cbc` elements with attributes | **104** |
| `cac` elements (in examples) | **317** |
| `cac` unique ABIE types used | **140** |
| `cac` unique instances | **1619** |

---

## `cbc` Elements

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
<cbc:Amount>0.0</cbc:Amount>
<cbc:Amount>0.00</cbc:Amount>
<cbc:Amount>0.275</cbc:Amount>
<cbc:Amount>1.00</cbc:Amount>
<cbc:Amount>10</cbc:Amount>
```
_10 more values in examples_

**`@currencyID`**

```xml
<cbc:Amount currencyID="DKK">0.00</cbc:Amount>
<cbc:Amount currencyID="EUR">0.275</cbc:Amount>
<cbc:Amount currencyID="GBP">0.0</cbc:Amount>
<cbc:Amount currencyID="SEK">100</cbc:Amount>
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
<cbc:DeclaredCustomsValueAmount>1000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>10000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>1500.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount>2000.00</cbc:DeclaredCustomsValueAmount>
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
<cbc:DeclaredStatisticsValueAmount>10000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>10050.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>1500.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount>182.62</cbc:DeclaredStatisticsValueAmount>
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
<cbc:LineExtensionAmount>-25</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>-3.96</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>1000.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount>120.00</cbc:LineExtensionAmount>
```
_17 more values in examples_

**`@currencyID`**

```xml
<cbc:LineExtensionAmount currencyID="CAD">100.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="DKK">150500.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">-25</cbc:LineExtensionAmount>
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
<cbc:PayableAmount>107.50</cbc:PayableAmount>
<cbc:PayableAmount>2000</cbc:PayableAmount>
<cbc:PayableAmount>247.55</cbc:PayableAmount>
```
_5 more values in examples_

**`@currencyID`**

```xml
<cbc:PayableAmount currencyID="CAD">100.00</cbc:PayableAmount>
<cbc:PayableAmount currencyID="DKK">247187.50</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">2000</cbc:PayableAmount>
<cbc:PayableAmount currencyID="GBP">100.00</cbc:PayableAmount>
<cbc:PayableAmount currencyID="SEK">6225</cbc:PayableAmount>
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
<cbc:PriceAmount>0.75</cbc:PriceAmount>
<cbc:PriceAmount>1.00</cbc:PriceAmount>
<cbc:PriceAmount>10.00</cbc:PriceAmount>
<cbc:PriceAmount>100.00</cbc:PriceAmount>
<cbc:PriceAmount>12.00</cbc:PriceAmount>
```
_12 more values in examples_

**`@currencyID`**

```xml
<cbc:PriceAmount currencyID="DKK">1250.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">0.75</cbc:PriceAmount>
<cbc:PriceAmount currencyID="GBP">1.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="SEK">15</cbc:PriceAmount>
<cbc:PriceAmount currencyID="USD">10.00</cbc:PriceAmount>
```

#### `cbc:TaxAmount`

```xml
<cbc:TaxAmount>-0.396</cbc:TaxAmount>
<cbc:TaxAmount>0</cbc:TaxAmount>
<cbc:TaxAmount>0.00</cbc:TaxAmount>
<cbc:TaxAmount>0.1</cbc:TaxAmount>
<cbc:TaxAmount>0.496</cbc:TaxAmount>
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
<cbc:TaxInclusiveAmount>1.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>1729</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>20.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>247.55</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount>247187.50</cbc:TaxInclusiveAmount>
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
<cbc:TaxableAmount>-25</cbc:TaxableAmount>
<cbc:TaxableAmount>1</cbc:TaxableAmount>
<cbc:TaxableAmount>1.00</cbc:TaxableAmount>
<cbc:TaxableAmount>100.00</cbc:TaxableAmount>
<cbc:TaxableAmount>1460.5</cbc:TaxableAmount>
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
<cbc:TotalTaxAmount>10937.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>17.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>20</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount>37625.00</cbc:TotalTaxAmount>
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
<cbc:EndDate>1967-08-13</cbc:EndDate>
<cbc:EndDate>2005-06-21</cbc:EndDate>
<cbc:EndDate>2005-06-25</cbc:EndDate>
<cbc:EndDate>2005-06-29</cbc:EndDate>
<cbc:EndDate>2005-06-30</cbc:EndDate>
```
_41 more values in examples_

#### `cbc:ExpiryDate`

```xml
<cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
<cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
```

#### `cbc:IssueDate`

```xml
<cbc:IssueDate>1967-08-13</cbc:IssueDate>
<cbc:IssueDate>2002-02-10</cbc:IssueDate>
<cbc:IssueDate>2002-08-13</cbc:IssueDate>
<cbc:IssueDate>2005-01-10</cbc:IssueDate>
<cbc:IssueDate>2005-06-19</cbc:IssueDate>
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
<cbc:StartDate>2005-02-26</cbc:StartDate>
<cbc:StartDate>2005-06-01</cbc:StartDate>
<cbc:StartDate>2005-06-20</cbc:StartDate>
<cbc:StartDate>2005-06-25</cbc:StartDate>
<cbc:StartDate>2005-06-29</cbc:StartDate>
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

### Identifier (`udt:IdentifierType`)

_54 elements_

#### `cbc:AircraftID`

```xml
<cbc:AircraftID>A-127763-747</cbc:AircraftID>
<cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
```

#### `cbc:AttributeID`

```xml
<cbc:AttributeID>GrossVolumen</cbc:AttributeID>
<cbc:AttributeID>GrossWeight</cbc:AttributeID>
<cbc:AttributeID>Height</cbc:AttributeID>
<cbc:AttributeID>Length</cbc:AttributeID>
<cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
```
_7 more values in examples_

#### `cbc:CarrierAssignedID`

```xml
<cbc:CarrierAssignedID>123456789987654321</cbc:CarrierAssignedID>
```

#### `cbc:CompanyID`

```xml
<cbc:CompanyID>12356478</cbc:CompanyID>
<cbc:CompanyID>1323421212</cbc:CompanyID>
<cbc:CompanyID>16077593</cbc:CompanyID>
<cbc:CompanyID>175 269 2355</cbc:CompanyID>
<cbc:CompanyID>18296799</cbc:CompanyID>
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
<cbc:CompanyID schemeID="DK:CVR">18296799</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:SE">DK12345678</cbc:CompanyID>
<cbc:CompanyID schemeID="DKVAT">DK12345</cbc:CompanyID>
<cbc:CompanyID schemeID="SE:ORGNR">5532331183</cbc:CompanyID>
<cbc:CompanyID schemeID="UK:CH">6411982340</cbc:CompanyID>
<cbc:CompanyID schemeID="ZZZ">5645342123</cbc:CompanyID>
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
<cbc:CustomizationID>AV</cbc:CustomizationID>
<cbc:CustomizationID>Common Framework</cbc:CustomizationID>
<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>
<cbc:CustomizationID>Sample-0.9</cbc:CustomizationID>
<cbc:CustomizationID>UBL-2.3</cbc:CustomizationID>
```
_22 more values in examples_

#### `cbc:DocumentID`

```xml
<cbc:DocumentID>33006</cbc:DocumentID>
```

#### `cbc:EndpointID`

```xml
<cbc:EndpointID>01841111111111</cbc:EndpointID>
<cbc:EndpointID>01842222222222</cbc:EndpointID>
<cbc:EndpointID>1234567890123</cbc:EndpointID>
<cbc:EndpointID>1234567987654</cbc:EndpointID>
<cbc:EndpointID>5798000416604</cbc:EndpointID>
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
<cbc:ID>000010</cbc:ID>
<cbc:ID>0004424005</cbc:ID>
<cbc:ID>001-00010123</cbc:ID>
<cbc:ID>0012345000058</cbc:ID>
<cbc:ID>00123450000580</cbc:ID>
```
_345 more values in examples_

**`@schemeAgencyID`**

```xml
<cbc:ID schemeAgencyID="306">XXX</cbc:ID>
<cbc:ID schemeAgencyID="320">63</cbc:ID>
<cbc:ID schemeAgencyID="5">TRHU1652173</cbc:ID>
<cbc:ID schemeAgencyID="6">123452340123</cbc:ID>
<cbc:ID schemeAgencyID="9">098740918237</cbc:ID>
<cbc:ID schemeAgencyID="ZZZ">EmployeeXXX</cbc:ID>
```

**`@schemeAgencyName`**

```xml
<cbc:ID schemeAgencyName="GS1">12345698</cbc:ID>
<cbc:ID schemeAgencyName="INCOTERMS">EXW</cbc:ID>
<cbc:ID schemeAgencyName="SMDG">XXX</cbc:ID>
<cbc:ID schemeAgencyName="UN">CNSHA</cbc:ID>
<cbc:ID schemeAgencyName="WCO">2005US12345678998765432112345678</cbc:ID>
```

**`@schemeID`**

```xml
<cbc:ID schemeID="AuthorisationNumber">M165</cbc:ID>
<cbc:ID schemeID="DK:CVR">DK12345678</cbc:ID>
<cbc:ID schemeID="GB:VAT">GB999999973</cbc:ID>
<cbc:ID schemeID="GLN">098740918237</cbc:ID>
<cbc:ID schemeID="GTIN">123452340123</cbc:ID>
<cbc:ID schemeID="IMCOTERM">FOT</cbc:ID>
<cbc:ID schemeID="ISO 6346">TRHU1652173</cbc:ID>
<cbc:ID schemeID="IT:VAT">IT01234567890</cbc:ID>
<cbc:ID schemeID="LINES">XXX</cbc:ID>
<cbc:ID schemeID="Passport">325334535</cbc:ID>
<cbc:ID schemeID="Skat.dk">DK10035643</cbc:ID>
<cbc:ID schemeID="UN/ECE 5153">VAT</cbc:ID>
<cbc:ID schemeID="UN/ECE 5305">AA</cbc:ID>
<cbc:ID schemeID="UN/LOCODE">GBBRS</cbc:ID>
<cbc:ID schemeID="ZZZ">123456789</cbc:ID>
<cbc:ID schemeID="locode">DK003102</cbc:ID>
<cbc:ID schemeID="urn:oioubl:id:taxschemeid-1.1">63</cbc:ID>
```

**`@schemeName`**

```xml
<cbc:ID schemeName="GINC">7365566156191234567</cbc:ID>
<cbc:ID schemeName="GLN">123465</cbc:ID>
<cbc:ID schemeName="GRAI">12345698</cbc:ID>
<cbc:ID schemeName="INCOTERMS">EXW</cbc:ID>
<cbc:ID schemeName="LOCODE">ITGOA</cbc:ID>
<cbc:ID schemeName="MovementReferenceNumber">TPS_1</cbc:ID>
<cbc:ID schemeName="SMDG master liner code list">XXX</cbc:ID>
<cbc:ID schemeName="UN/LOCODE">CNSHA</cbc:ID>
<cbc:ID schemeName="UNLOCODE">ITGOA</cbc:ID>
<cbc:ID schemeName="Unique Consignment Reference">2005US12345678998765432112345678</cbc:ID>
<cbc:ID schemeName="bic">BFCU4040001</cbc:ID>
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
<cbc:ProfileID>BII</cbc:ProfileID>
<cbc:ProfileID>ENS</cbc:ProfileID>
<cbc:ProfileID>ExampleProfile</cbc:ProfileID>
<cbc:ProfileID>FWF</cbc:ProfileID>
<cbc:ProfileID>Procurement-QuoSim-1.0</cbc:ProfileID>
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
<cbc:TraceID>12345678914564</cbc:TraceID>
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
<cbc:TransportExecutionPlanReferenceID>TEPID_1_4</cbc:TransportExecutionPlanReferenceID>
```
_3 more values in examples_

#### `cbc:UBLVersionID`

```xml
<cbc:UBLVersionID>2.0</cbc:UBLVersionID>
<cbc:UBLVersionID>2.0-prd3</cbc:UBLVersionID>
<cbc:UBLVersionID>2.1</cbc:UBLVersionID>
<cbc:UBLVersionID>2.2</cbc:UBLVersionID>
<cbc:UBLVersionID>2.3</cbc:UBLVersionID>
```
_2 more values in examples_

#### `cbc:URI`

```xml
<cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
<cbc:URI>http://facebook.com/oasis.open</cbc:URI>
<cbc:URI>http://twitter.com/OASISopen</cbc:URI>
<cbc:URI>http://www.suppliersite.eu/sheet001.html</cbc:URI>
<cbc:URI>http://www.youtube.com/oasisopen</cbc:URI>
```
_6 more values in examples_

#### `cbc:UUID`

```xml
<cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
<cbc:UUID>4D07786B-DA6D-439F-82D1-6FFFC7F4E3B1</cbc:UUID>
<cbc:UUID>569ED478-0EBE-4817-A234-DFB9ACA81218</cbc:UUID>
<cbc:UUID>6E09886B-DC6E-439F-82D1-7C83709652B1</cbc:UUID>
<cbc:UUID>6E09886B-DC6E-439F-82D1-7C83746352B1</cbc:UUID>
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
<cbc:GrossWeightMeasure>130</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure>230.80</cbc:GrossWeightMeasure>
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
<cbc:Measure>0.336</cbc:Measure>
<cbc:Measure>12.288</cbc:Measure>
<cbc:Measure>120</cbc:Measure>
<cbc:Measure>160</cbc:Measure>
<cbc:Measure>2.44</cbc:Measure>
```
_12 more values in examples_

**`@unitCode`**

```xml
<cbc:Measure unitCode="CEL">3.00</cbc:Measure>
<cbc:Measure unitCode="CMT">120</cbc:Measure>
<cbc:Measure unitCode="KG">12.288</cbc:Measure>
<cbc:Measure unitCode="KGM">88</cbc:Measure>
<cbc:Measure unitCode="MTQ">0.336</cbc:Measure>
<cbc:Measure unitCode="MTR">2.44</cbc:Measure>
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
<cbc:CityName>Aalborg</cbc:CityName>
<cbc:CityName>Anytown</cbc:CityName>
<cbc:CityName>Bergen</cbc:CityName>
<cbc:CityName>Berlin</cbc:CityName>
<cbc:CityName>Bern</cbc:CityName>
```
_48 more values in examples_

#### `cbc:FamilyName`

```xml
<cbc:FamilyName>Doe</cbc:FamilyName>
<cbc:FamilyName>GONZALES</cbc:FamilyName>
<cbc:FamilyName>Jensen</cbc:FamilyName>
<cbc:FamilyName>M</cbc:FamilyName>
<cbc:FamilyName>Pereson</cbc:FamilyName>
```
_7 more values in examples_

#### `cbc:FirstName`

```xml
<cbc:FirstName>Antonio</cbc:FirstName>
<cbc:FirstName>DAVID</cbc:FirstName>
<cbc:FirstName>GIORGIO</cbc:FirstName>
<cbc:FirstName>John</cbc:FirstName>
<cbc:FirstName>Kirsten</cbc:FirstName>
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
<cbc:Name>"Computing for dummies" book</cbc:Name>
<cbc:Name>*ULLA GJERSTRUP</cbc:Name>
<cbc:Name>9000</cbc:Name>
<cbc:Name>ACME Corporation</cbc:Name>
<cbc:Name>ACME Ltd.</cbc:Name>
```
_175 more values in examples_

#### `cbc:RegistrationName`

```xml
<cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
<cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
<cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
<cbc:RegistrationName>Farthing Purchasing Consortium</cbc:RegistrationName>
<cbc:RegistrationName>Gentofte Kommune</cbc:RegistrationName>
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
<cbc:StreetName>AVD BLASCO IBANEZ</cbc:StreetName>
<cbc:StreetName>Akershusstranda 19</cbc:StreetName>
<cbc:StreetName>Anystreet</cbc:StreetName>
<cbc:StreetName>Arne Jacobsens Allé</cbc:StreetName>
<cbc:StreetName>Avon Way</cbc:StreetName>
```
_54 more values in examples_

#### `cbc:VesselName`

```xml
<cbc:VesselName>MS Enova</cbc:VesselName>
<cbc:VesselName>SomeVesselName</cbc:VesselName>
<cbc:VesselName>Vessel Name</cbc:VesselName>
```

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
<cbc:Percent>20</cbc:Percent>
<cbc:Percent>21.00</cbc:Percent>
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
<cbc:BaseQuantity unitCode="C62">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
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
<cbc:Quantity>0</cbc:Quantity>
<cbc:Quantity>1</cbc:Quantity>
<cbc:Quantity>10</cbc:Quantity>
<cbc:Quantity>100</cbc:Quantity>
<cbc:Quantity>120</cbc:Quantity>
```
_15 more values in examples_

**`@unitCode`**

```xml
<cbc:Quantity unitCode="C62">15</cbc:Quantity>
<cbc:Quantity unitCode="CT">63.000</cbc:Quantity>
<cbc:Quantity unitCode="EA">1</cbc:Quantity>
<cbc:Quantity unitCode="H87">1</cbc:Quantity>
<cbc:Quantity unitCode="KG">100</cbc:Quantity>
<cbc:Quantity unitCode="KGM">100</cbc:Quantity>
<cbc:Quantity unitCode="LTR">120</cbc:Quantity>
<cbc:Quantity unitCode="NAR">0</cbc:Quantity>
<cbc:Quantity unitCode="NIU">35</cbc:Quantity>
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
<cbc:TotalGoodsItemQuantity>2</cbc:TotalGoodsItemQuantity>
<cbc:TotalGoodsItemQuantity>23</cbc:TotalGoodsItemQuantity>
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
<cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Damage</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Discount</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Donation to the Red Cross</cbc:AllowanceChargeReason>
<cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
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
<cbc:BuildingNumber>1</cbc:BuildingNumber>
<cbc:BuildingNumber>100</cbc:BuildingNumber>
<cbc:BuildingNumber>12</cbc:BuildingNumber>
<cbc:BuildingNumber>13</cbc:BuildingNumber>
<cbc:BuildingNumber>15</cbc:BuildingNumber>
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
<cbc:Department>Revenue department</cbc:Department>
```
_2 more values in examples_

#### `cbc:Description`

```xml
<cbc:Description>200 grams of Carbon Dioxide per km</cbc:Description>
<cbc:Description>ACME NEW BRANCH will be opened in Brusells on May 12, 2010</cbc:Description>
<cbc:Description>ART INTERNATIONAL ZURICH 2019</cbc:Description>
<cbc:Description>AWAITING CUSTOMS. MISSING DOCUMENTATION. ONE HOUR DELAYED</cbc:Description>
<cbc:Description>Acme beeswax</cbc:Description>
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
<cbc:DocumentType>ATA carnet, paper</cbc:DocumentType>
<cbc:DocumentType>Annual Contract</cbc:DocumentType>
<cbc:DocumentType>BOL</cbc:DocumentType>
<cbc:DocumentType>CMR</cbc:DocumentType>
<cbc:DocumentType>Contract</cbc:DocumentType>
```
_9 more values in examples_

#### `cbc:ElectronicMail`

```xml
<cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
<cbc:ElectronicMail>SomeName@arriva.de</cbc:ElectronicMail>
<cbc:ElectronicMail>SomeName@consignee.de</cbc:ElectronicMail>
<cbc:ElectronicMail>SomeName@consignor.cn</cbc:ElectronicMail>
<cbc:ElectronicMail>SomeName@d2d.de</cbc:ElectronicMail>
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
<cbc:Line>5th Floor</cbc:Line>
<cbc:Line>AVD BLASCO IBANEZ 36</cbc:Line>
<cbc:Line>Calle Serpis 64</cbc:Line>
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
<cbc:Note>A call-off from the annual contract</cbc:Note>
<cbc:Note>Bestilling af computere</cbc:Note>
<cbc:Note>Computer</cbc:Note>
<cbc:Note>Cover is slightly damaged.</cbc:Note>
<cbc:Note>DELAYED</cbc:Note>
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
<cbc:PostalZone>00140</cbc:PostalZone>
<cbc:PostalZone>01803-4238</cbc:PostalZone>
<cbc:PostalZone>01821</cbc:PostalZone>
<cbc:PostalZone>02210</cbc:PostalZone>
<cbc:PostalZone>02340</cbc:PostalZone>
```
_42 more values in examples_

#### `cbc:Postbox`

```xml
<cbc:Postbox>123</cbc:Postbox>
<cbc:Postbox>148</cbc:Postbox>
<cbc:Postbox>321</cbc:Postbox>
<cbc:Postbox>456</cbc:Postbox>
<cbc:Postbox>5467</cbc:Postbox>
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
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:CreditNote-2.0:sbs-1.0-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:DespatchAdvice-2.0:sbs-1.0-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:Invoice-2.0:sbs-1.0-draft</cbc:SubsetID>
<cbc:SubsetID>urn:oasis:names:specification:ubl:xpath:Order-2.0:sbs-1.0-draft</cbc:SubsetID>
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
<cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
<cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
<cbc:Telefax>+1 343 1453655</cbc:Telefax>
<cbc:Telefax>+1 781 425 5072</cbc:Telefax>
<cbc:Telefax>+44 127 2653215</cbc:Telefax>
```
_17 more values in examples_

#### `cbc:Telephone`

```xml
<cbc:Telephone>+ 44 127 98876545</cbc:Telephone>
<cbc:Telephone>+1 158 1233714</cbc:Telephone>
<cbc:Telephone>+1 3362 4788</cbc:Telephone>
<cbc:Telephone>+1 343 1453654</cbc:Telephone>
<cbc:Telephone>+1 36222 33847</cbc:Telephone>
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
<cbc:TransportationServiceDescription>CARRIER SERVICE</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Complete D2D service from Munich, Germany to Hamar, Norway</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>En route status notifications</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Insurance of goods during transportation</cbc:TransportationServiceDescription>
<cbc:TransportationServiceDescription>Package and pallet transport within the Bavaria area</cbc:TransportationServiceDescription>
```
_4 more values in examples_

#### `cbc:Value`

```xml
<cbc:Value>0</cbc:Value>
<cbc:Value>20mm</cbc:Value>
<cbc:Value>Acrylic</cbc:Value>
<cbc:Value>Black</cbc:Value>
<cbc:Value>Bovine</cbc:Value>
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
<cbc:EndTime>06:00:00</cbc:EndTime>
<cbc:EndTime>06:00:00Z</cbc:EndTime>
<cbc:EndTime>09:30:10+01:00</cbc:EndTime>
<cbc:EndTime>09:30:47.0Z</cbc:EndTime>
<cbc:EndTime>10:30:47.0Z</cbc:EndTime>
```
_22 more values in examples_

#### `cbc:ExpiryTime`

```xml
<cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
```

#### `cbc:IssueTime`

```xml
<cbc:IssueTime>01:01:01.001</cbc:IssueTime>
<cbc:IssueTime>08:20:00.0Z</cbc:IssueTime>
<cbc:IssueTime>09:00:00.0Z</cbc:IssueTime>
<cbc:IssueTime>09:29:10+01:00</cbc:IssueTime>
<cbc:IssueTime>09:29:30+01:00</cbc:IssueTime>
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
<cbc:StartTime>07:00:00</cbc:StartTime>
<cbc:StartTime>07:00:00Z</cbc:StartTime>
<cbc:StartTime>08:00:00</cbc:StartTime>
<cbc:StartTime>08:00:00Z</cbc:StartTime>
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

---

## `cac` Elements

_Grouped by ABIE type from `UBL-CommonAggregateComponents-2.5.xsd`. Elements sharing a type share the same structure; their instances are pooled._

### `ActivityDataLineType`

**Used as:** `cac:SupplyChainActivityDataLine`

_5 unique instances across 1 element_

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
    <cbc:ID>1234567890</cbc:ID>
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

### `AddressLineType`

**Used as:** `cac:AddressLine`

_11 unique instances across 1 element_

```xml
<cac:AddressLine>
  <cbc:Line>1. sal</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>3rd Floor, Room 5</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>5th Floor</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>AVD BLASCO IBANEZ 36</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>Calle Serpis 64</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>Customer entrance from the street</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>ExampleStreet 1, DK-6920 Videbæk</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>IT-afdelingen</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>The Roundabout</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>Ueberseetor 2</cbc:Line>
</cac:AddressLine>
```

```xml
<cac:AddressLine>
  <cbc:Line>West Wing</cbc:Line>
</cac:AddressLine>
```

### `AddressType`

**Used as:** `cac:Address` · `cac:DeliveryAddress` · `cac:DespatchAddress` · `cac:OriginAddress` · `cac:PostalAddress` · `cac:RegistrationAddress`

_112 unique instances across 6 elements_

```xml
<cac:Address>
  <cac:Country>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    <cbc:Name>Swiss</cbc:Name>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cac:Country>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:CityName>Espoo</cbc:CityName>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:CityName>Hamburg</cbc:CityName>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:CityName>Munich</cbc:CityName>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:CityName>STORLIEN</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>SE</cbc:IdentificationCode>
    <cbc:Name>SWEDEN</cbc:Name>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:CityName>Tanger</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>MA</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:Floor>1</cbc:Floor>
  <cbc:StreetName>AVD BLASCO IBANEZ</cbc:StreetName>
  <cbc:CityName>VALENCIA</cbc:CityName>
  <cbc:PostalZone>460019</cbc:PostalZone>
  <cac:AddressLine>
    <cbc:Line>AVD BLASCO IBANEZ 36</cbc:Line>
  </cac:AddressLine>
</cac:Address>
```

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

```xml
<cac:Address>
  <cbc:ID>DEHAM</cbc:ID>
  <cbc:StreetName>Neuer Wandrahm 4</cbc:StreetName>
  <cbc:CityName>Hamburg</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

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

```xml
<cac:Address>
  <cbc:Region>Bavaria</cbc:Region>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
    <cbc:Name>Germany</cbc:Name>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Akershusstranda 19</cbc:StreetName>
  <cbc:CityName>Oslo</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
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
```

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

```xml
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
```

```xml
<cac:Address>
  <cbc:StreetName>Dalsagervej</cbc:StreetName>
  <cbc:BuildingNumber>7</cbc:BuildingNumber>
  <cbc:CityName>Hirtshals</cbc:CityName>
  <cbc:PostalZone>9850</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Declarant Street</cbc:StreetName>
  <cbc:CityName>Declarant City</cbc:CityName>
  <cbc:PostalZone>Declarant Post Code</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

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

```xml
<cac:Address>
  <cbc:StreetName>Grosse strasse 34</cbc:StreetName>
  <cbc:CityName>Nurnberg</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

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

```xml
<cac:Address>
  <cbc:StreetName>Hans Christian Andersens Boulevard</cbc:StreetName>
  <cbc:BuildingNumber>777</cbc:BuildingNumber>
  <cbc:CityName>Copenhagen</cbc:CityName>
  <cbc:PostalZone>1234</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

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

```xml
<cac:Address>
  <cbc:StreetName>Hansestadt Bremisches</cbc:StreetName>
  <cbc:CityName>Bremen</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Heissestrasse 45</cbc:StreetName>
  <cbc:CityName>Munich</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Heissestrasse 45</cbc:StreetName>
  <cbc:CityName>Munich</cbc:CityName>
  <cbc:PostalZone>80334</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Jordbærstien 2</cbc:StreetName>
  <cbc:CityName>Hamar</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Marken</cbc:StreetName>
  <cbc:BuildingNumber>13</cbc:BuildingNumber>
  <cbc:CityName>Bergen</cbc:CityName>
  <cbc:PostalZone>5017</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Sandstr. 38-40</cbc:StreetName>
  <cbc:CityName>Nurnberg</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

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

```xml
<cac:Address>
  <cbc:StreetName>Stribevangen</cbc:StreetName>
  <cbc:BuildingNumber>89</cbc:BuildingNumber>
  <cbc:CityName>Gedser</cbc:CityName>
  <cbc:PostalZone>4874</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
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
```

```xml
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
```

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

```xml
<cac:Address>
  <cbc:StreetName>Volkerstrasse 6</cbc:StreetName>
  <cbc:CityName>Munich</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:Address>
  <cbc:StreetName>Volkerstrasse 6</cbc:StreetName>
  <cbc:CityName>Munich</cbc:CityName>
  <cbc:PostalZone>80334</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:Address>
```

```xml
<cac:DeliveryAddress>
  <cac:Country>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
  </cac:Country>
</cac:DeliveryAddress>
```

```xml
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
```

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

```xml
<cac:DespatchAddress>
  <cac:Country>
    <cbc:IdentificationCode>RU</cbc:IdentificationCode>
  </cac:Country>
</cac:DespatchAddress>
```

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

```xml
<cac:OriginAddress>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:Country>
</cac:OriginAddress>
```

```xml
<cac:OriginAddress>
  <cac:Country>
    <cbc:IdentificationCode>TH</cbc:IdentificationCode>
  </cac:Country>
</cac:OriginAddress>
```

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

```xml
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
```

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

```xml
<cac:PostalAddress>
  <cbc:CityName>Brussels</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>BE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:CityName>La Spezia</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:CityName>London</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:CityName>Munchen</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:CityName>New York</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
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
```

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

```xml
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
```

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

```xml
<cac:PostalAddress>
  <cbc:ID>4058673827000</cbc:ID>
</cac:PostalAddress>
```

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

```xml
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
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Breite Straße</cbc:StreetName>
  <cbc:BuildingNumber>29</cbc:BuildingNumber>
  <cbc:CityName>Berlin</cbc:CityName>
  <cbc:PostalZone>10178</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Consignee W Street</cbc:StreetName>
  <cbc:CityName>Munich</cbc:CityName>
  <cbc:PostalZone>231</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Declarant Street</cbc:StreetName>
  <cbc:CityName>Declarant City</cbc:CityName>
  <cbc:PostalZone>Declarant Post Code</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>ExampleStreet</cbc:StreetName>
  <cbc:CityName>Example City</cbc:CityName>
  <cbc:PostalZone>1234</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>ExampleStreet</cbc:StreetName>
  <cbc:CityName>Viby J</cbc:CityName>
  <cbc:PostalZone>8260</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Export Str. 143</cbc:StreetName>
  <cbc:CityName>Yang Mei</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>TH</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>High Street</cbc:StreetName>
  <cbc:BuildingNumber>1</cbc:BuildingNumber>
  <cbc:CityName>Copenhagen</cbc:CityName>
  <cbc:PostalZone>1001</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Industrivej 3</cbc:StreetName>
  <cbc:CityName>Ørum Djurs</cbc:CityName>
  <cbc:PostalZone>8586</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
    <cbc:Name>Denmark</cbc:Name>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Komsomolskaja pl., 158</cbc:StreetName>
  <cbc:CityName>Moskva</cbc:CityName>
  <cbc:PostalZone>107842</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>RU</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Marken</cbc:StreetName>
  <cbc:BuildingNumber>13</cbc:BuildingNumber>
  <cbc:CityName>Bergen</cbc:CityName>
  <cbc:PostalZone>5017</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>NO</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>One Hundred Road</cbc:StreetName>
  <cbc:BuildingNumber>100</cbc:BuildingNumber>
  <cbc:CityName>London</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Schonestrasse 1</cbc:StreetName>
  <cbc:CityName>Munich</cbc:CityName>
  <cbc:PostalZone>80331</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Slet Parkvej</cbc:StreetName>
  <cbc:BuildingNumber>1</cbc:BuildingNumber>
  <cbc:CityName>Nørre Alslev</cbc:CityName>
  <cbc:PostalZone>4840</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Stahlstrass 5</cbc:StreetName>
  <cbc:CityName>Bern</cbc:CityName>
  <cbc:PostalZone>CH-3007</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>CH</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Street</cbc:StreetName>
  <cbc:CityName>City</cbc:CityName>
  <cbc:PostalZone>Post</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Stribevangen</cbc:StreetName>
  <cbc:BuildingNumber>89</cbc:BuildingNumber>
  <cbc:CityName>Gedser</cbc:CityName>
  <cbc:PostalZone>4874</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Tollbrettkoppel</cbc:StreetName>
  <cbc:BuildingNumber>8</cbc:BuildingNumber>
  <cbc:CityName>Heiligenhafen</cbc:CityName>
  <cbc:PostalZone>23774</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

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

```xml
<cac:PostalAddress>
  <cbc:StreetName>Vastuskatu 12</cbc:StreetName>
  <cbc:CityName>Helsinki</cbc:CityName>
  <cbc:PostalZone>00140</cbc:PostalZone>
  <cac:Country>
    <cbc:IdentificationCode>FI</cbc:IdentificationCode>
  </cac:Country>
</cac:PostalAddress>
```

```xml
<cac:PostalAddress>
  <cbc:StreetName>Vesterbrogade</cbc:StreetName>
  <cbc:BuildingNumber>78</cbc:BuildingNumber>
  <cbc:CityName>København K</cbc:CityName>
  <cbc:PostalZone>1258</cbc:PostalZone>
</cac:PostalAddress>
```

```xml
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
```

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

```xml
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
```

```xml
<cac:RegistrationAddress>
  <cbc:CityName>Big city</cbc:CityName>
  <cbc:CountrySubentity>RegionA</cbc:CountrySubentity>
  <cac:Country>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:Country>
</cac:RegistrationAddress>
```

```xml
<cac:RegistrationAddress>
  <cbc:CityName>Mainplace</cbc:CityName>
  <cbc:CountrySubentity>RegionB</cbc:CountrySubentity>
  <cac:Country>
    <cbc:IdentificationCode>BE</cbc:IdentificationCode>
  </cac:Country>
</cac:RegistrationAddress>
```

```xml
<cac:RegistrationAddress>
  <cbc:CityName>Stockholm</cbc:CityName>
  <cac:Country>
    <cbc:IdentificationCode>SE</cbc:IdentificationCode>
  </cac:Country>
</cac:RegistrationAddress>
```

```xml
<cac:RegistrationAddress>
  <cbc:CityName>Stockholm</cbc:CityName>
  <cbc:CountrySubentity>RegionX</cbc:CountrySubentity>
  <cac:Country>
    <cbc:IdentificationCode>SE</cbc:IdentificationCode>
  </cac:Country>
</cac:RegistrationAddress>
```

### `AirTransportType`

**Used as:** `cac:AirTransport`

_2 unique instances across 1 element_

```xml
<cac:AirTransport>
  <cbc:AircraftID>A-127763-747</cbc:AircraftID>
</cac:AirTransport>
```

```xml
<cac:AirTransport>
  <cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
</cac:AirTransport>
```

### `AllowanceChargeType`

**Used as:** `cac:AllowanceCharge` · `cac:FreightAllowanceCharge`

_17 unique instances across 2 elements_

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
  <cbc:MultiplierFactorNumeric>0.15</cbc:MultiplierFactorNumeric>
  <cbc:Amount>225</cbc:Amount>
  <cbc:BaseAmount>1500</cbc:BaseAmount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Contract</cbc:AllowanceChargeReason>
  <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
  <cbc:Amount>0.275</cbc:Amount>
  <cbc:BaseAmount>2.75</cbc:BaseAmount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Damage</cbc:AllowanceChargeReason>
  <cbc:Amount>12</cbc:Amount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Discount</cbc:AllowanceChargeReason>
  <cbc:Amount>4.80</cbc:Amount>
  <cbc:TaxInclusiveAmount>6.00</cbc:TaxInclusiveAmount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Paid 10,000 loyalty points = €5</cbc:AllowanceChargeReason>
  <cbc:Amount>5.00</cbc:Amount>
  <cbc:TaxInclusiveAmount>5.00</cbc:TaxInclusiveAmount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Promotion discount</cbc:AllowanceChargeReason>
  <cbc:Amount>100</cbc:Amount>
</cac:AllowanceCharge>
```

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

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Total order value discount</cbc:AllowanceChargeReason>
  <cbc:Amount>100</cbc:Amount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReasonCode>17</cbc:AllowanceChargeReasonCode>
  <cbc:MultiplierFactorNumeric>0.10</cbc:MultiplierFactorNumeric>
  <cbc:Amount>10.00</cbc:Amount>
</cac:AllowanceCharge>
```

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

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Handling fee</cbc:AllowanceChargeReason>
  <cbc:Amount>10.00</cbc:Amount>
  <cac:TaxCategory>
    <cbc:ID>S</cbc:ID>
    <cbc:Percent>21.00</cbc:Percent>
    <cac:TaxScheme>
      <cbc:ID>VAT</cbc:ID>
    </cac:TaxScheme>
  </cac:TaxCategory>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Packing cost</cbc:AllowanceChargeReason>
  <cbc:Amount>100</cbc:Amount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Testing</cbc:AllowanceChargeReason>
  <cbc:Amount>10</cbc:Amount>
</cac:AllowanceCharge>
```

```xml
<cac:AllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Transport documents</cbc:AllowanceChargeReason>
  <cbc:Amount>100</cbc:Amount>
</cac:AllowanceCharge>
```

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

```xml
<cac:FreightAllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:AllowanceChargeReason>Freight charges</cbc:AllowanceChargeReason>
  <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
  <cbc:Amount>254.00</cbc:Amount>
</cac:FreightAllowanceCharge>
```

```xml
<cac:FreightAllowanceCharge>
  <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
  <cbc:Amount>0.00</cbc:Amount>
</cac:FreightAllowanceCharge>
```

### `AttachmentType`

**Used as:** `cac:Attachment` · `cac:DigitalSignatureAttachment` · `cac:EncryptionCertificateAttachment`

_6 unique instances across 3 elements_

```xml
<cac:Attachment>
  <cac:ExternalReference>
    <cbc:URI>http://www.suppliersite.eu/sheet001.html</cbc:URI>
  </cac:ExternalReference>
</cac:Attachment>
```

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

```xml
<cac:Attachment>
  <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
</cac:Attachment>
```

```xml
<cac:DigitalSignatureAttachment>
  <cac:ExternalReference>
    <cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
  </cac:ExternalReference>
</cac:DigitalSignatureAttachment>
```

```xml
<cac:EncryptionCertificateAttachment>
  <cac:ExternalReference>
    <cbc:URI>www.digst.dk/udbud/NemID.cer</cbc:URI>
  </cac:ExternalReference>
</cac:EncryptionCertificateAttachment>
```

```xml
<cac:EncryptionCertificateAttachment>
  <cbc:EmbeddedDocument>;lkajdf;lkasd;ljkasdf;lkja;sdlfkja;sldfkja;sdlfjkas;dlkfjas;dlfjas;dlkfjas;dlkfja;slkdjf</cbc:EmbeddedDocument>
</cac:EncryptionCertificateAttachment>
```

### `AttestationLineType`

**Used as:** `cac:AttestationLine`

_3 unique instances across 1 element_

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

```xml
<cac:AttestationLine>
  <cbc:Description>fish or aquatic invertebrates caught in the country or region’s domestic sea or in the open sea or farming aquatic animals</cbc:Description>
  <cbc:Description>fisk eller havdyr, der ikke er pattedyr, som er fanget enten i landets eller regionens egne have eller i det åbne hav eller som stammer
						fra opdræt på åbent hav</cbc:Description>
  <cbc:Description>本国海域或公海捕捞的鱼类或水生无脊椎动物或养殖水生动物</cbc:Description>
</cac:AttestationLine>
```

```xml
<cac:AttestationLine>
  <cbc:Description>from offal from plants, which are approved by the competent authority in Denmark for manufacture of aquatic products
						for human consumption.</cbc:Description>
  <cbc:Description>fra afskær fra virksomheder, som er godkendt af den kompetente myndighed i Danmark til produktion
						af fiskeprodukter til human konsum</cbc:Description>
  <cbc:Description>经丹麦主管机构批准的供人类消费水产品加工厂的副产品</cbc:Description>
</cac:AttestationLine>
```

### `AttestationType`

**Used as:** `cac:Attestation`

_3 unique instances across 1 element_

```xml
<cac:Attestation>
  <cbc:ID>1</cbc:ID>
  <cbc:AcceptanceIndicator>true</cbc:AcceptanceIndicator>
  <cac:IssuerParty>
    <cac:PartyIdentification>
      <cbc:ID>1</cbc:ID>
    </cac:PartyIdentification>
  </cac:IssuerParty>
  <cac:AttestationLine>
    <cbc:Description>fish or aquatic invertebrates caught in the country or region’s domestic sea or in the open sea or farming aquatic animals</cbc:Description>
    <cbc:Description>fisk eller havdyr, der ikke er pattedyr, som er fanget enten i landets eller regionens egne have eller i det åbne hav eller som stammer
						fra opdræt på åbent hav</cbc:Description>
    <cbc:Description>本国海域或公海捕捞的鱼类或水生无脊椎动物或养殖水生动物</cbc:Description>
  </cac:AttestationLine>
</cac:Attestation>
```

```xml
<cac:Attestation>
  <cbc:ID>2</cbc:ID>
  <cbc:AcceptanceIndicator>false</cbc:AcceptanceIndicator>
  <cac:IssuerParty>
    <cac:PartyIdentification>
      <cbc:ID>1</cbc:ID>
    </cac:PartyIdentification>
  </cac:IssuerParty>
  <cac:AttestationLine>
    <cbc:Description>from offal from plants, which are approved by the competent authority in Denmark for manufacture of aquatic products
						for human consumption.</cbc:Description>
    <cbc:Description>fra afskær fra virksomheder, som er godkendt af den kompetente myndighed i Danmark til produktion
						af fiskeprodukter til human konsum</cbc:Description>
    <cbc:Description>经丹麦主管机构批准的供人类消费水产品加工厂的副产品</cbc:Description>
  </cac:AttestationLine>
</cac:Attestation>
```

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

### `BillingReferenceType`

**Used as:** `cac:BillingReference`

_4 unique instances across 1 element_

```xml
<cac:BillingReference>
  <cac:CreditNoteDocumentReference>
    <cbc:ID>CN758494</cbc:ID>
    <cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
    <cbc:IssueDate>2005-06-25</cbc:IssueDate>
  </cac:CreditNoteDocumentReference>
</cac:BillingReference>
```

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID>A00095678</cbc:ID>
    <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
    <cbc:IssueDate>2005-06-21</cbc:IssueDate>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID>INV000123</cbc:ID>
    <cbc:IssueDate>2025-07-01</cbc:IssueDate>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

```xml
<cac:BillingReference>
  <cac:InvoiceDocumentReference>
    <cbc:ID>TOSL108</cbc:ID>
  </cac:InvoiceDocumentReference>
</cac:BillingReference>
```

### `BranchType`

**Used as:** `cac:FinancialInstitutionBranch`

_2 unique instances across 1 element_

```xml
<cac:FinancialInstitutionBranch>
  <cac:FinancialInstitution>
    <cbc:ID>DKDKABCD</cbc:ID>
  </cac:FinancialInstitution>
</cac:FinancialInstitutionBranch>
```

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

### `CapabilityType`

**Used as:** `cac:BusinessCapability`

_1 unique instance across 1 element_

```xml
<cac:BusinessCapability>
  <cbc:CapabilityTypeCode>General</cbc:CapabilityTypeCode>
  <cbc:Description>Advancing open standards for the information society.</cbc:Description>
</cac:BusinessCapability>
```

### `CashRegisterType`

**Used as:** `cac:CashRegister`

_1 unique instance across 1 element_

```xml
<cac:CashRegister>
  <cbc:ID>7</cbc:ID>
  <cbc:SerialNumberID>7f49b2b8-9e75-11ed-a8fc-0242ac120002</cbc:SerialNumberID>
</cac:CashRegister>
```

### `CommodityClassificationType`

**Used as:** `cac:CommodityClassification`

_15 unique instances across 1 element_

```xml
<cac:CommodityClassification>
  <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
  <cbc:CommodityCode>8</cbc:CommodityCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:CommodityCode>19011000</cbc:CommodityCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:CommodityCode>84195000</cbc:CommodityCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>12344321</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>12344322</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>12344325</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>32344324</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>65434564</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>65434565</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>65434566</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>65434567</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>65434568</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:ItemClassificationCode>8518309590</cbc:ItemClassificationCode>
</cac:CommodityClassification>
```

```xml
<cac:CommodityClassification>
  <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
</cac:CommodityClassification>
```

### `ConsignmentType`

**Used as:** `cac:Consignment` · `cac:ReferencedConsignment`

_21 unique instances across 2 elements_

```xml
<cac:Consignment>
  <cbc:ID>123</cbc:ID>
</cac:Consignment>
```

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
      <cbc:StartTime>07:00:00Z</cbc:StartTime>
      <cbc:EndDate>2016-08-02</cbc:EndDate>
      <cbc:EndTime>15:30:00Z</cbc:EndTime>
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

```xml
<cac:Consignment>
  <cbc:ID>1</cbc:ID>
</cac:Consignment>
```

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

```xml
<cac:Consignment>
  <cbc:ID>510</cbc:ID>
</cac:Consignment>
```

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

```xml
<cac:Consignment>
  <cbc:ID>CON_1</cbc:ID>
</cac:Consignment>
```

```xml
<cac:Consignment>
  <cbc:ID>XYZ987</cbc:ID>
  <cbc:SummaryDescription>Electronic components</cbc:SummaryDescription>
</cac:Consignment>
```

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

```xml
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
```

### `ContactType`

**Used as:** `cac:CashierContact` · `cac:CommercialContact` · `cac:Contact` · `cac:DeliveryContact` · `cac:LegalContact` · `cac:PointOfSaleContact` · `cac:SignatoryContact` · `cac:SupportContact` · `cac:TechnicalContact`

_64 unique instances across 9 elements_

```xml
<cac:CashierContact>
  <cbc:Name>John D. Salesman</cbc:Name>
  <cbc:Department>Gadgets</cbc:Department>
</cac:CashierContact>
```

```xml
<cac:CommercialContact>
  <cbc:Name>Jennifer de Niro</cbc:Name>
  <cbc:ElectronicMail>jennifer.deniro@vendor.net</cbc:ElectronicMail>
</cac:CommercialContact>
```

```xml
<cac:CommercialContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:CommercialContact>
```

```xml
<cac:Contact>
  <cbc:ElectronicMail>someName@consignee.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ElectronicMail>someName@consignor.cn</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>11</cbc:ID>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>12345678</cbc:ID>
  <cbc:Name>Sille Schyberg</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>1928</cbc:ID>
  <cbc:Name>*ULLA GJERSTRUP</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>1</cbc:ID>
  <cbc:Telephone>+1 781 425 5073</cbc:Telephone>
  <cbc:Telefax>+1 781 425 5072</cbc:Telefax>
  <cbc:ElectronicMail>info@oasis-open.org</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>7778</cbc:ID>
  <cbc:Name>Ole Hansen</cbc:Name>
  <cbc:Telephone>4526532147</cbc:Telephone>
  <cbc:Telefax>4526532146</cbc:Telefax>
  <cbc:ElectronicMail>Ole@super.company.dk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>8447</cbc:ID>
  <cbc:Name>Document Robot</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:ID>Freight Bookings</cbc:ID>
  <cbc:Telephone>+1 3362 4788</cbc:Telephone>
  <cbc:ElectronicMail>bookings@unitedfreight.com</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Anders Stock</cbc:Name>
  <cbc:Telephone>+4987676234</cbc:Telephone>
  <cbc:ElectronicMail>anders@RAILCARRIER.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Andreas Andersen</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Con Solidador</cbc:Name>
  <cbc:Telephone>+1 343 1453654</cbc:Telephone>
  <cbc:Telefax>+1 343 1453655</cbc:Telefax>
  <cbc:ElectronicMail>ctanner@onestopfreight.com</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>ExampleName</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Hans Weisser</cbc:Name>
  <cbc:Telephone>+4992894481</cbc:Telephone>
  <cbc:ElectronicMail>hans.weisser@FORWARDER.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Horst Tappert</cbc:Name>
  <cbc:Telephone>+4987675652</cbc:Telephone>
  <cbc:ElectronicMail>horst@SEACARRIER.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Jan Peter Clausen</cbc:Name>
  <cbc:Telephone>+4793774465</cbc:Telephone>
  <cbc:ElectronicMail>janpc@ROADCARRIER2.no</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>John Smith</cbc:Name>
  <cbc:ElectronicMail>jsmith@example.com</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Jon Persen</cbc:Name>
  <cbc:Telephone>+4793656656</cbc:Telephone>
  <cbc:ElectronicMail>jonp@CONSIGNEE.no</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Bianchi</cbc:Name>
  <cbc:Telephone>0039 051 23000008</cbc:Telephone>
  <cbc:Telefax>0039 051 23000025</cbc:Telefax>
  <cbc:ElectronicMail>bianchi@arancioforniture.it</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Delta</cbc:Name>
  <cbc:Telephone>0039 059 33000000</cbc:Telephone>
  <cbc:Telefax>0039 059 33000055</cbc:Telefax>
  <cbc:ElectronicMail>delta@betashop.it</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Fred Churchill</cbc:Name>
  <cbc:Telephone>+44 127 2653214</cbc:Telephone>
  <cbc:Telefax>+44 127 2653215</cbc:Telefax>
  <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Fred Churchill</cbc:Name>
  <cbc:Telephone>0127 2653214</cbc:Telephone>
  <cbc:Telefax>0127 2653215</cbc:Telefax>
  <cbc:ElectronicMail>fred@iytcorporation.gov.uk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Gamma</cbc:Name>
  <cbc:Telephone>0039 059 33000022</cbc:Telephone>
  <cbc:Telefax>0039 059 33000057</cbc:Telefax>
  <cbc:ElectronicMail>gamma@betashop.it</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Rossi</cbc:Name>
  <cbc:Telephone>0039 051 23000000</cbc:Telephone>
  <cbc:Telefax>0039 051 23000023</cbc:Telefax>
  <cbc:ElectronicMail>rossi@arancioforniture.it</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mr Verdi</cbc:Name>
  <cbc:Telephone>0039 051 25400000</cbc:Telephone>
  <cbc:Telefax>0039 051 25400023</cbc:Telefax>
  <cbc:ElectronicMail>verdi@azoutsourcing.it</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mrs Bouquet</cbc:Name>
  <cbc:Telephone>+1 158 1233714</cbc:Telephone>
  <cbc:Telefax>+ 1 158 1233856</cbc:Telefax>
  <cbc:ElectronicMail>bouquet@fpconsortial.com</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Mrs Bouquet</cbc:Name>
  <cbc:Telephone>0158 1233714</cbc:Telephone>
  <cbc:Telefax>0158 1233856</cbc:Telefax>
  <cbc:ElectronicMail>bouquet@fpconsortial.co.uk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Ole Ellerbæk Madsen</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Per</cbc:Name>
  <cbc:Telephone>987098709</cbc:Telephone>
  <cbc:Telefax>34673435</cbc:Telefax>
  <cbc:ElectronicMail>bill@svetruck.se</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Peter Janssen</cbc:Name>
  <cbc:Telephone>+4987675432</cbc:Telephone>
  <cbc:ElectronicMail>peter@ROADCARRIER.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Peter Janssen</cbc:Name>
  <cbc:Telephone>+4987675432</cbc:Telephone>
  <cbc:Telefax>+4987675431</cbc:Telefax>
  <cbc:ElectronicMail>peter@ROADCARRIER.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>S Massiah</cbc:Name>
  <cbc:Telephone>+ 44 127 98876545</cbc:Telephone>
  <cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
  <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>S Massiah</cbc:Name>
  <cbc:Telephone>0127 98876545</cbc:Telephone>
  <cbc:Telefax>0127 98876546</cbc:Telefax>
  <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+212687878763</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@disfruta.ma</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+4598786765</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@maersk.dk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+49450557000</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@d2d.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+49450557000</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@necoss.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+49450557234</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@ext-hal.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+49450557777</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@ntt.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+49450557888</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@arriva.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+4987878763</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@consignee.de</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+8676576456</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@consignor.cn</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>SomeName</cbc:Name>
  <cbc:Telephone>+8687878763</cbc:Telephone>
  <cbc:ElectronicMail>SomeName@consignor.cn</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Name>Tuula Tullaaja 02 13 4567</cbc:Name>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>+1 36222 33847</cbc:Telephone>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>+324005588588</cbc:Telephone>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>+324488588578</cbc:Telephone>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>123456</cbc:Telephone>
  <cbc:Telefax>123456</cbc:Telefax>
  <cbc:ElectronicMail>pelle@johnsson.se</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>34557</cbc:Telephone>
  <cbc:Telefax>3456767</cbc:Telefax>
  <cbc:ElectronicMail>lars@moderna.se</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>346788</cbc:Telephone>
  <cbc:Telefax>8567443</cbc:Telefax>
  <cbc:ElectronicMail>sven@moderna.se</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>4621230</cbc:Telephone>
  <cbc:Telefax>4621231</cbc:Telefax>
  <cbc:ElectronicMail>antonio@salescompany.dk</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:Contact>
  <cbc:Telephone>5121230</cbc:Telephone>
  <cbc:Telefax>5121231</cbc:Telefax>
  <cbc:ElectronicMail>john@buyercompany.eu</cbc:ElectronicMail>
</cac:Contact>
```

```xml
<cac:DeliveryContact>
  <cbc:Name>Eva Johnsson</cbc:Name>
  <cbc:Telephone>1234356</cbc:Telephone>
  <cbc:Telefax>123455</cbc:Telefax>
  <cbc:ElectronicMail>eva@johnsson.se</cbc:ElectronicMail>
</cac:DeliveryContact>
```

```xml
<cac:LegalContact>
  <cbc:Name>John Smith</cbc:Name>
  <cbc:ElectronicMail>john.smith@vendor.net</cbc:ElectronicMail>
</cac:LegalContact>
```

```xml
<cac:LegalContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:LegalContact>
```

```xml
<cac:PointOfSaleContact>
  <cbc:Name>Jane D.</cbc:Name>
  <cbc:JobTitle>Store manager</cbc:JobTitle>
  <cbc:ElectronicMail>shop37@GadgetsR.us</cbc:ElectronicMail>
</cac:PointOfSaleContact>
```

```xml
<cac:SignatoryContact>
  <cbc:ID>ML</cbc:ID>
  <cbc:Name>Mette Lind</cbc:Name>
</cac:SignatoryContact>
```

```xml
<cac:SupportContact>
  <cbc:Name>Paul McQueen</cbc:Name>
  <cbc:ElectronicMail>paul.mcqueen@vendor.net</cbc:ElectronicMail>
</cac:SupportContact>
```

```xml
<cac:SupportContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:SupportContact>
```

```xml
<cac:TechnicalContact>
  <cbc:Name>Paul McQueen</cbc:Name>
  <cbc:ElectronicMail>paul.mcqueen@vendor.net</cbc:ElectronicMail>
</cac:TechnicalContact>
```

```xml
<cac:TechnicalContact>
  <cbc:Name>Peter Gruen</cbc:Name>
  <cbc:ElectronicMail>peter.gruen@buyer.de</cbc:ElectronicMail>
</cac:TechnicalContact>
```

### `ContractType`

**Used as:** `cac:Contract` · `cac:TransportContract`

_7 unique instances across 2 elements_

```xml
<cac:Contract>
  <cac:ContractDocumentReference>
    <cbc:ID>GHJ76849</cbc:ID>
    <cbc:IssueDate>2002-08-13</cbc:IssueDate>
  </cac:ContractDocumentReference>
</cac:Contract>
```

```xml
<cac:Contract>
  <cac:ContractDocumentReference>
    <cbc:ID>SKI123456</cbc:ID>
    <cbc:IssueDate>2006-01-01</cbc:IssueDate>
  </cac:ContractDocumentReference>
</cac:Contract>
```

```xml
<cac:Contract>
  <cbc:ID>34322</cbc:ID>
  <cbc:ContractType>FrameworkAgreementID123</cbc:ContractType>
</cac:Contract>
```

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

### `ContractingPartyType`

**Used as:** `cac:ContractingParty`

_2 unique instances across 1 element_

```xml
<cac:ContractingParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>Other</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:ContractingParty>
```

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

### `CountryType`

**Used as:** `cac:AgreementCountry` · `cac:Country` · `cac:DestinationCountry` · `cac:ExportCountry` · `cac:FinalDestinationCountry` · `cac:OriginCountry` · `cac:OriginalDepartureCountry` · `cac:TransitCountry`

_45 unique instances across 8 elements_

```xml
<cac:AgreementCountry>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
</cac:AgreementCountry>
```

```xml
<cac:AgreementCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
</cac:AgreementCountry>
```

```xml
<cac:AgreementCountry>
  <cbc:IdentificationCode>GB</cbc:IdentificationCode>
</cac:AgreementCountry>
```

```xml
<cac:AgreementCountry>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:AgreementCountry>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>BE</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>CH</cbc:IdentificationCode>
  <cbc:Name>Swiss</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>CH</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  <cbc:Name>Germany</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  <cbc:Name>Denmark</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>FI</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>GB</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  <cbc:Name>Italy</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>IT</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>MA</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>NO</cbc:IdentificationCode>
  <cbc:Name>NORWAY</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>NO</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>PA</cbc:IdentificationCode>
  <cbc:Name>Panama</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>RU</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>SE</cbc:IdentificationCode>
  <cbc:Name>SWEDEN</cbc:Name>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>SE</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>TH</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:Country>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:Country>
```

```xml
<cac:DestinationCountry>
  <cbc:IdentificationCode>GB</cbc:IdentificationCode>
  <cbc:Name>Great Britain</cbc:Name>
</cac:DestinationCountry>
```

```xml
<cac:ExportCountry>
  <cbc:IdentificationCode>TH</cbc:IdentificationCode>
</cac:ExportCountry>
```

```xml
<cac:ExportCountry>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:ExportCountry>
```

```xml
<cac:FinalDestinationCountry>
  <cbc:IdentificationCode>CH</cbc:IdentificationCode>
</cac:FinalDestinationCountry>
```

```xml
<cac:FinalDestinationCountry>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
</cac:FinalDestinationCountry>
```

```xml
<cac:FinalDestinationCountry>
  <cbc:IdentificationCode>GB</cbc:IdentificationCode>
</cac:FinalDestinationCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
</cac:OriginCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  <cbc:Name>Denmark</cbc:Name>
</cac:OriginCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
</cac:OriginCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>FI</cbc:IdentificationCode>
</cac:OriginCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>IT</cbc:IdentificationCode>
</cac:OriginCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>MX</cbc:IdentificationCode>
  <cbc:Name>Mexico</cbc:Name>
</cac:OriginCountry>
```

```xml
<cac:OriginCountry>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:OriginCountry>
```

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>CN</cbc:IdentificationCode>
</cac:OriginalDepartureCountry>
```

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  <cbc:Name>Denmark</cbc:Name>
</cac:OriginalDepartureCountry>
```

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>DK</cbc:IdentificationCode>
</cac:OriginalDepartureCountry>
```

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>MA</cbc:IdentificationCode>
</cac:OriginalDepartureCountry>
```

```xml
<cac:OriginalDepartureCountry>
  <cbc:IdentificationCode>US</cbc:IdentificationCode>
</cac:OriginalDepartureCountry>
```

```xml
<cac:TransitCountry>
  <cbc:IdentificationCode>AT</cbc:IdentificationCode>
</cac:TransitCountry>
```

```xml
<cac:TransitCountry>
  <cbc:IdentificationCode>DE</cbc:IdentificationCode>
</cac:TransitCountry>
```

```xml
<cac:TransitCountry>
  <cbc:IdentificationCode>IT</cbc:IdentificationCode>
</cac:TransitCountry>
```

### `CreditNoteLineType`

**Used as:** `cac:CreditNoteLine`

_7 unique instances across 1 element_

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

### `CustomerPartyType`

**Used as:** `cac:AccountingCustomerParty` · `cac:BuyerCustomerParty` · `cac:DeliveryCustomerParty` · `cac:OriginatorCustomerParty` · `cac:RetailerCustomerParty`

_17 unique instances across 5 elements_

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

```xml
<cac:AccountingCustomerParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>North American Veeblefetzer</cbc:Name>
    </cac:PartyName>
  </cac:Party>
</cac:AccountingCustomerParty>
```

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
      <cbc:FamilyName>X</cbc:FamilyName>
      <cbc:MiddleName>Doe</cbc:MiddleName>
      <cbc:JobTitle>Purchasing manager</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
</cac:AccountingCustomerParty>
```

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

```xml
<cac:BuyerCustomerParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>0012345000359</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:BuyerCustomerParty>
```

```xml
<cac:BuyerCustomerParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>2203148000007</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:BuyerCustomerParty>
```

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
      <cbc:Telephone>+ 44 127 98876545</cbc:Telephone>
      <cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
      <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
    </cac:Contact>
  </cac:Party>
</cac:OriginatorCustomerParty>
```

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

### `CustomsDeclarationType`

**Used as:** `cac:CustomsDeclaration` · `cac:PreviousCustomsDeclaration`

_5 unique instances across 2 elements_

```xml
<cac:CustomsDeclaration>
  <cbc:ID>10158209175014500</cbc:ID>
</cac:CustomsDeclaration>
```

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
          <cbc:StartTime>07:00:00Z</cbc:StartTime>
          <cbc:EndDate>2016-08-02</cbc:EndDate>
          <cbc:EndTime>15:30:00Z</cbc:EndTime>
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

```xml
<cac:PreviousCustomsDeclaration>
  <cbc:ID>FIRMA000000010</cbc:ID>
</cac:PreviousCustomsDeclaration>
```

```xml
<cac:PreviousCustomsDeclaration>
  <cbc:ID>HUISI000000002</cbc:ID>
</cac:PreviousCustomsDeclaration>
```

### `DebitNoteLineType`

**Used as:** `cac:DebitNoteLine`

_7 unique instances across 1 element_

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

```xml
<cac:DebitNoteLine>
  <cbc:ID>2</cbc:ID>
  <cbc:DebitedQuantity>2</cbc:DebitedQuantity>
  <cbc:LineExtensionAmount>80.00</cbc:LineExtensionAmount>
  <cac:Item>
    <cbc:Name>Auxiliary Tool</cbc:Name>
  </cac:Item>
  <cac:Price>
    <cbc:PriceAmount>40.00</cbc:PriceAmount>
  </cac:Price>
</cac:DebitNoteLine>
```

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

### `DeliveryChannelType`

**Used as:** `cac:DigitalDeliveryChannel`

_5 unique instances across 1 element_

```xml
<cac:DigitalDeliveryChannel>
  <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
  <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
  <cac:DigitalMessageDelivery>
    <cbc:ProtocolID>AS2</cbc:ProtocolID>
    <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
  </cac:DigitalMessageDelivery>
</cac:DigitalDeliveryChannel>
```

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

```xml
<cac:DigitalDeliveryChannel>
  <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
  <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
  <cbc:TestIndicator>true</cbc:TestIndicator>
  <cac:DigitalMessageDelivery>
    <cbc:ProtocolID>AS2</cbc:ProtocolID>
    <cbc:EndpointURI>http://as2.buyer.de</cbc:EndpointURI>
  </cac:DigitalMessageDelivery>
</cac:DigitalDeliveryChannel>
```

```xml
<cac:DigitalDeliveryChannel>
  <cbc:NetworkID>OpenPEPPOL</cbc:NetworkID>
  <cbc:ParticipantID>1234567987654</cbc:ParticipantID>
  <cbc:TestIndicator>true</cbc:TestIndicator>
  <cac:DigitalMessageDelivery>
    <cbc:ProtocolID>AS2</cbc:ProtocolID>
    <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
  </cac:DigitalMessageDelivery>
</cac:DigitalDeliveryChannel>
```

### `DeliveryTermsType`

**Used as:** `cac:DeliveryTerms`

_10 unique instances across 1 element_

```xml
<cac:DeliveryTerms>
  <cbc:ID>CIP</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:Name>Balboa Port</cbc:Name>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:ID>EXW</cbc:ID>
  <cac:DeliveryLocation>
    <cac:Address>
      <cbc:CityName>Hamburg</cbc:CityName>
    </cac:Address>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

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

```xml
<cac:DeliveryTerms>
  <cbc:ID>FCA</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:Name>9000</cbc:Name>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:ID>FOB Destination</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:ID>GBBRS</cbc:ID>
    <cbc:Description>Bristol</cbc:Description>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:ID>FOB Destination</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:ID>GBFXT</cbc:ID>
    <cbc:Description>Felixstowe</cbc:Description>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:ID>FOB</cbc:ID>
  <cac:DeliveryLocation>
    <cbc:Name>BANGKOK</cbc:Name>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:ID>FOT</cbc:ID>
  <cbc:SpecialTerms>CAD</cbc:SpecialTerms>
  <cac:DeliveryLocation>
    <cbc:ID>STO</cbc:ID>
  </cac:DeliveryLocation>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:SpecialTerms>1% deduction for late delivery as per contract</cbc:SpecialTerms>
</cac:DeliveryTerms>
```

```xml
<cac:DeliveryTerms>
  <cbc:SpecialTerms>1% reduktion i kontraktsummen pr. dags forsinkelse jf. SKI kontrakt</cbc:SpecialTerms>
</cac:DeliveryTerms>
```

### `DeliveryType`

**Used as:** `cac:Delivery`

_15 unique instances across 1 element_

```xml
<cac:Delivery>
  <cac:DeliveryAddress>
    <cac:Country>
      <cbc:IdentificationCode>CH</cbc:IdentificationCode>
    </cac:Country>
  </cac:DeliveryAddress>
  <cac:Despatch>
    <cbc:ActualDespatchDate>2013-09-15</cbc:ActualDespatchDate>
    <cbc:ActualDespatchTime>16:00:00</cbc:ActualDespatchTime>
    <cac:DespatchAddress>
      <cac:Country>
        <cbc:IdentificationCode>RU</cbc:IdentificationCode>
      </cac:Country>
    </cac:DespatchAddress>
  </cac:Despatch>
</cac:Delivery>
```

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

```xml
<cac:Delivery>
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
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2008-05-06</cbc:StartDate>
    <cbc:StartTime>09:30:47.0Z</cbc:StartTime>
    <cbc:EndDate>2008-05-10</cbc:EndDate>
    <cbc:EndTime>09:30:47.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

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
    <cbc:StartDate>2005-06-29</cbc:StartDate>
    <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-30</cbc:EndDate>
    <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

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
    <cbc:StartDate>2005-06-29</cbc:StartDate>
    <cbc:StartTime>09:30:47.0Z</cbc:StartTime>
    <cbc:EndDate>2005-06-29</cbc:EndDate>
    <cbc:EndTime>09:30:47.0Z</cbc:EndTime>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

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

```xml
<cac:Delivery>
  <cac:RequestedDeliveryPeriod>
    <cbc:StartDate>2010-02-10</cbc:StartDate>
    <cbc:EndDate>2010-02-25</cbc:EndDate>
  </cac:RequestedDeliveryPeriod>
</cac:Delivery>
```

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

### `DespatchLineType`

**Used as:** `cac:DespatchLine`

_2 unique instances across 1 element_

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

### `DespatchType`

**Used as:** `cac:Despatch`

_7 unique instances across 1 element_

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

```xml
<cac:Despatch>
  <cbc:ActualDespatchDate>2013-09-15</cbc:ActualDespatchDate>
  <cbc:ActualDespatchTime>16:00:00</cbc:ActualDespatchTime>
  <cac:DespatchAddress>
    <cac:Country>
      <cbc:IdentificationCode>RU</cbc:IdentificationCode>
    </cac:Country>
  </cac:DespatchAddress>
</cac:Despatch>
```

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

```xml
<cac:Despatch>
  <cbc:ID>000010</cbc:ID>
</cac:Despatch>
```

```xml
<cac:Despatch>
  <cbc:ID>28833-2661-144</cbc:ID>
</cac:Despatch>
```

```xml
<cac:Despatch>
  <cbc:ID>FLGS339241</cbc:ID>
</cac:Despatch>
```

### `DigitalAgreementTermsType`

**Used as:** `cac:DigitalAgreementTerms`

_2 unique instances across 1 element_

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
      <cbc:StartTime>09:00:00Z</cbc:StartTime>
      <cbc:EndTime>16:00:00Z</cbc:EndTime>
    </cac:ServiceAvailabilityPeriod>
    <cac:ServiceMaintenancePeriod>
      <cbc:StartTime>22:00:00Z</cbc:StartTime>
      <cbc:EndTime>06:00:00Z</cbc:EndTime>
    </cac:ServiceMaintenancePeriod>
  </cac:ServiceLevelAgreement>
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
</cac:DigitalAgreementTerms>
```

### `DigitalCollaborationType`

**Used as:** `cac:DigitalCollaboration`

_3 unique instances across 1 element_

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
        <cbc:EndpointURI>http://as2.buyer.biz</cbc:EndpointURI>
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
```

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
```

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

### `DigitalProcessType`

**Used as:** `cac:DigitalProcess`

_3 unique instances across 1 element_

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

```xml
<cac:DigitalProcess>
  <cbc:ID>urn:www.cenbii.eu:profile:bii05:ver2.0</cbc:ID>
  <cbc:ProfileID>BII</cbc:ProfileID>
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
          <cbc:EndpointURI>http://as2.buyer.biz</cbc:EndpointURI>
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

```xml
<cac:DigitalProcess>
  <cbc:ID>urn:www.cenbii.eu:profile:bii05:ver2.0</cbc:ID>
  <cbc:ProfileID>BII</cbc:ProfileID>
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
</cac:DigitalProcess>
```

### `DigitalServiceType`

**Used as:** `cac:ReceivingDigitalService` · `cac:SendingDigitalService`

_5 unique instances across 2 elements_

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
      <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
    </cac:DigitalMessageDelivery>
  </cac:DigitalDeliveryChannel>
</cac:ReceivingDigitalService>
```

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
      <cbc:EndpointURI>http://as2.buyer.biz</cbc:EndpointURI>
    </cac:DigitalMessageDelivery>
  </cac:DigitalDeliveryChannel>
</cac:SendingDigitalService>
```

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
      <cbc:EndpointURI>http://as2.buyer.de</cbc:EndpointURI>
    </cac:DigitalMessageDelivery>
  </cac:DigitalDeliveryChannel>
</cac:SendingDigitalService>
```

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

### `DimensionType`

**Used as:** `cac:Dimension` · `cac:MeasurementDimension`

_17 unique instances across 2 elements_

```xml
<cac:Dimension>
  <cbc:AttributeID>GrossWeight</cbc:AttributeID>
  <cbc:Measure>12.288</cbc:Measure>
</cac:Dimension>
```

```xml
<cac:Dimension>
  <cbc:AttributeID>LineGrossWeight</cbc:AttributeID>
  <cbc:Measure>774.144</cbc:Measure>
</cac:Dimension>
```

```xml
<cac:Dimension>
  <cbc:AttributeID>LineNetWeight</cbc:AttributeID>
  <cbc:Measure>604.8</cbc:Measure>
</cac:Dimension>
```

```xml
<cac:Dimension>
  <cbc:AttributeID>NetWeight</cbc:AttributeID>
  <cbc:Measure>9.6</cbc:Measure>
</cac:Dimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>GrossVolumen</cbc:AttributeID>
  <cbc:Measure>0.336</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>GrossWeight</cbc:AttributeID>
  <cbc:Measure>774.14400</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>GrossWeight</cbc:AttributeID>
  <cbc:Measure>88</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>Height</cbc:AttributeID>
  <cbc:Measure>160</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>Height</cbc:AttributeID>
  <cbc:Measure>2.6</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>Length</cbc:AttributeID>
  <cbc:Measure>120</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>Length</cbc:AttributeID>
  <cbc:Measure>6.1</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>NetWeight</cbc:AttributeID>
  <cbc:Measure>604.80000</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>OuterDepth</cbc:AttributeID>
  <cbc:Measure>80</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>OuterHeight</cbc:AttributeID>
  <cbc:Measure>70</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>OuterWidth</cbc:AttributeID>
  <cbc:Measure>60</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>Width</cbc:AttributeID>
  <cbc:Measure>2.44</cbc:Measure>
</cac:MeasurementDimension>
```

```xml
<cac:MeasurementDimension>
  <cbc:AttributeID>Width</cbc:AttributeID>
  <cbc:Measure>80</cbc:Measure>
</cac:MeasurementDimension>
```

### `DocumentDistributionType`

**Used as:** `cac:DocumentDistribution`

_2 unique instances across 1 element_

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

### `DocumentMetadataType`

**Used as:** `cac:DigitalDocumentMetadata`

_2 unique instances across 1 element_

```xml
<cac:DigitalDocumentMetadata>
  <cbc:FormatID>UBL</cbc:FormatID>
  <cbc:VersionID>2.2</cbc:VersionID>
  <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2</cbc:SchemaURI>
  <cbc:DocumentTypeCode>381</cbc:DocumentTypeCode>
</cac:DigitalDocumentMetadata>
```

```xml
<cac:DigitalDocumentMetadata>
  <cbc:FormatID>UBL</cbc:FormatID>
  <cbc:VersionID>2.2</cbc:VersionID>
  <cbc:SchemaURI>urn:oasis:names:specification:ubl:schema:xsd:Invoice-2</cbc:SchemaURI>
  <cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
</cac:DigitalDocumentMetadata>
```

### `DocumentReferenceType`

**Used as:** `cac:AdditionalDocumentReference` · `cac:CatalogueDocumentReference` · `cac:ContractDocumentReference` · `cac:CreditNoteDocumentReference` · `cac:DespatchDocumentReference` · `cac:DocumentReference` · `cac:IdentityDocumentReference` · `cac:InvoiceDocumentReference` · `cac:OrderDocumentReference` · `cac:OriginatorDocumentReference` · `cac:ProofOfReexportationRequestDocumentReference` · `cac:QuotationDocumentReference` · `cac:ReceiptDocumentReference` · `cac:RequestForQuotationDocumentReference` · `cac:SalesDocumentReference` · `cac:ShipmentDocumentReference` · `cac:TransportExecutionPlanDocumentReference` · `cac:TransportProgressStatusRequestDocumentReference` · `cac:TransportServiceDescriptionDocumentReference` · `cac:TransportServiceDescriptionRequestDocumentReference` · `cac:VoucherDocumentReference`

_47 unique instances across 21 elements_

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>0665/2003</cbc:ID>
  <cbc:IssueDate>2013-06-23</cbc:IssueDate>
  <cbc:DocumentTypeCode>N380</cbc:DocumentTypeCode>
</cac:AdditionalDocumentReference>
```

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>108-3692468</cbc:ID>
  <cbc:IssueDate>2013-06-23</cbc:IssueDate>
  <cbc:DocumentTypeCode>741</cbc:DocumentTypeCode>
</cac:AdditionalDocumentReference>
```

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>34564645</cbc:ID>
</cac:AdditionalDocumentReference>
```

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

```xml
<cac:AdditionalDocumentReference>
  <cbc:ID>Doc2</cbc:ID>
  <cbc:DocumentType>Drawing</cbc:DocumentType>
  <cac:Attachment>
    <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
  </cac:Attachment>
</cac:AdditionalDocumentReference>
```

```xml
<cac:CatalogueDocumentReference>
  <cbc:ID>2005-9A</cbc:ID>
  <cbc:IssueDate>2005-11-03</cbc:IssueDate>
</cac:CatalogueDocumentReference>
```

```xml
<cac:ContractDocumentReference>
  <cbc:ID>101</cbc:ID>
  <cbc:DocumentType>Annual Contract</cbc:DocumentType>
  <cac:Attachment>
    <cbc:EmbeddedDocumentBinaryObject>UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
  </cac:Attachment>
</cac:ContractDocumentReference>
```

```xml
<cac:ContractDocumentReference>
  <cbc:ID>Contract321</cbc:ID>
  <cbc:DocumentType>Framework agreement</cbc:DocumentType>
</cac:ContractDocumentReference>
```

```xml
<cac:ContractDocumentReference>
  <cbc:ID>GHJ76849</cbc:ID>
  <cbc:IssueDate>2002-08-13</cbc:IssueDate>
</cac:ContractDocumentReference>
```

```xml
<cac:ContractDocumentReference>
  <cbc:ID>SKI123456</cbc:ID>
  <cbc:IssueDate>2006-01-01</cbc:IssueDate>
</cac:ContractDocumentReference>
```

```xml
<cac:ContractDocumentReference>
  <cbc:ID>TC101</cbc:ID>
  <cbc:IssueDate>2010-01-01</cbc:IssueDate>
  <cbc:DocumentTypeCode>315</cbc:DocumentTypeCode>
  <cbc:DocumentType>Contract</cbc:DocumentType>
  <cbc:DocumentDescription>Framework Agreement between Consignor and NECOSS</cbc:DocumentDescription>
</cac:ContractDocumentReference>
```

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

```xml
<cac:CreditNoteDocumentReference>
  <cbc:ID>CN758494</cbc:ID>
  <cbc:UUID>349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4</cbc:UUID>
  <cbc:IssueDate>2005-06-25</cbc:IssueDate>
</cac:CreditNoteDocumentReference>
```

```xml
<cac:DespatchDocumentReference>
  <cbc:ID>565899</cbc:ID>
  <cbc:UUID>88C7280E-8F10-419F-9949-8EFFFA2842B8</cbc:UUID>
  <cbc:IssueDate>2005-06-20</cbc:IssueDate>
</cac:DespatchDocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>224087496582335</cbc:ID>
  <cbc:DocumentTypeCode>704</cbc:DocumentTypeCode>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>2343456533</cbc:ID>
  <cbc:DocumentType>CMR</cbc:DocumentType>
  <cac:IssuerParty>
    <cac:PartyName>
      <cbc:Name>Boston Road</cbc:Name>
    </cac:PartyName>
  </cac:IssuerParty>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>234534533</cbc:ID>
  <cbc:DocumentType>CMR</cbc:DocumentType>
  <cac:IssuerParty>
    <cac:PartyName>
      <cbc:Name>Boston Road</cbc:Name>
    </cac:PartyName>
  </cac:IssuerParty>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>34563456</cbc:ID>
  <cbc:DocumentType>ATA carnet, paper</cbc:DocumentType>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>AEG012345</cbc:ID>
  <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
  <cbc:IssueDate>2005-06-20</cbc:IssueDate>
  <cbc:DocumentType>Order</cbc:DocumentType>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>KHN23-44044</cbc:ID>
  <cbc:UUID>6E09886B-DC6E-439F-82D1-7C83746352B1</cbc:UUID>
  <cbc:IssueDate>2005-06-24</cbc:IssueDate>
  <cbc:DocumentType>Forwarding Instructions</cbc:DocumentType>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>W123</cbc:ID>
  <cbc:IssueDate>2016-11-02</cbc:IssueDate>
  <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
  <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
</cac:DocumentReference>
```

```xml
<cac:DocumentReference>
  <cbc:ID>W123</cbc:ID>
  <cbc:IssueDate>2016-11-02</cbc:IssueDate>
  <cbc:DocumentTypeCode>SM1</cbc:DocumentTypeCode>
  <cbc:DocumentType></cbc:DocumentType>
  <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
</cac:DocumentReference>
```

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

```xml
<cac:IdentityDocumentReference>
  <cbc:ID>325334535</cbc:ID>
</cac:IdentityDocumentReference>
```

```xml
<cac:InvoiceDocumentReference>
  <cbc:ID>A00095678</cbc:ID>
  <cbc:UUID>849FBBCE-E081-40B4-906C-94C5FF9D1AC3</cbc:UUID>
  <cbc:IssueDate>2005-06-21</cbc:IssueDate>
</cac:InvoiceDocumentReference>
```

```xml
<cac:InvoiceDocumentReference>
  <cbc:ID>INV000123</cbc:ID>
  <cbc:IssueDate>2025-07-01</cbc:IssueDate>
</cac:InvoiceDocumentReference>
```

```xml
<cac:InvoiceDocumentReference>
  <cbc:ID>TOSL108</cbc:ID>
</cac:InvoiceDocumentReference>
```

```xml
<cac:OrderDocumentReference>
  <cbc:ID>RjectedOrderID123</cbc:ID>
</cac:OrderDocumentReference>
```

```xml
<cac:OriginatorDocumentReference>
  <cbc:ID>MAFO</cbc:ID>
</cac:OriginatorDocumentReference>
```

```xml
<cac:ProofOfReexportationRequestDocumentReference>
  <cbc:ID>A2344</cbc:ID>
</cac:ProofOfReexportationRequestDocumentReference>
```

```xml
<cac:QuotationDocumentReference>
  <cbc:ID>QuoteID123</cbc:ID>
</cac:QuotationDocumentReference>
```

```xml
<cac:ReceiptDocumentReference>
  <cbc:ID>658398</cbc:ID>
  <cbc:UUID>89F82FA6-5331-491D-83BC-7B6CA7FD047C</cbc:UUID>
  <cbc:IssueDate>2005-06-21</cbc:IssueDate>
</cac:ReceiptDocumentReference>
```

```xml
<cac:RequestForQuotationDocumentReference>
  <cbc:ID>G867B</cbc:ID>
  <cbc:UUID>8D076867-AE6D-439F-8281-5AAFC7F4E3B1</cbc:UUID>
  <cbc:IssueDate>2005-06-19</cbc:IssueDate>
</cac:RequestForQuotationDocumentReference>
```

```xml
<cac:RequestForQuotationDocumentReference>
  <cbc:ID>G867B</cbc:ID>
  <cbc:UUID>93T5G3G5-HYA3-7267-BVG3-GS46SW44WG53</cbc:UUID>
  <cbc:IssueDate>2008-04-19</cbc:IssueDate>
</cac:RequestForQuotationDocumentReference>
```

```xml
<cac:SalesDocumentReference>
  <cbc:ID>PROFORMA001</cbc:ID>
  <cbc:DocumentType>Preliminary sales receipt</cbc:DocumentType>
</cac:SalesDocumentReference>
```

```xml
<cac:ShipmentDocumentReference>
  <cbc:ID>GOA294107</cbc:ID>
  <cbc:DocumentTypeCode>BN</cbc:DocumentTypeCode>
</cac:ShipmentDocumentReference>
```

```xml
<cac:ShipmentDocumentReference>
  <cbc:ID>ID168</cbc:ID>
  <cbc:DocumentTypeCode>Certificate of shipment</cbc:DocumentTypeCode>
  <cbc:DocumentType>Shipment reference</cbc:DocumentType>
</cac:ShipmentDocumentReference>
```

```xml
<cac:TransportExecutionPlanDocumentReference>
  <cbc:ID>TEPID_1</cbc:ID>
</cac:TransportExecutionPlanDocumentReference>
```

```xml
<cac:TransportExecutionPlanDocumentReference>
  <cbc:ID>TEP_1</cbc:ID>
</cac:TransportExecutionPlanDocumentReference>
```

```xml
<cac:TransportProgressStatusRequestDocumentReference>
  <cbc:ID>TPS_1</cbc:ID>
</cac:TransportProgressStatusRequestDocumentReference>
```

```xml
<cac:TransportServiceDescriptionDocumentReference>
  <cbc:ID>2</cbc:ID>
</cac:TransportServiceDescriptionDocumentReference>
```

```xml
<cac:TransportServiceDescriptionRequestDocumentReference>
  <cbc:ID>TSD_REQ_1</cbc:ID>
</cac:TransportServiceDescriptionRequestDocumentReference>
```

```xml
<cac:VoucherDocumentReference>
  <cbc:ID>23445567</cbc:ID>
</cac:VoucherDocumentReference>
```

```xml
<cac:VoucherDocumentReference>
  <cbc:ID>5234533222</cbc:ID>
</cac:VoucherDocumentReference>
```

```xml
<cac:VoucherDocumentReference>
  <cbc:ID>52345423423</cbc:ID>
</cac:VoucherDocumentReference>
```

### `EconomicOperatorPartyType`

**Used as:** `cac:EconomicOperatorParty`

_2 unique instances across 1 element_

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

### `EncryptionCertificatePathChainType`

**Used as:** `cac:EncryptionCertificatePathChain`

_2 unique instances across 1 element_

```xml
<cac:EncryptionCertificatePathChain>
  <cbc:URI>https://www.trust2408/certPaths/Trust2408_issuingCA12_chain.p7c</cbc:URI>
</cac:EncryptionCertificatePathChain>
```

```xml
<cac:EncryptionCertificatePathChain>
  <cbc:Value>TRUST2408 OCES Primary CA – TRUST2408 OCES CA II</cbc:Value>
</cac:EncryptionCertificatePathChain>
```

### `EncryptionDataType`

**Used as:** `cac:TenderEncryptionData`

_2 unique instances across 1 element_

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

### `EncryptionSymmetricAlgorithmType`

**Used as:** `cac:EncryptionSymmetricAlgorithm`

_2 unique instances across 1 element_

```xml
<cac:EncryptionSymmetricAlgorithm>
  <cbc:OID>2.16.840.1.101.3.4.1.2</cbc:OID>
</cac:EncryptionSymmetricAlgorithm>
```

```xml
<cac:EncryptionSymmetricAlgorithm>
  <cbc:OID>2.16.840.1.101.3.4.1.42</cbc:OID>
</cac:EncryptionSymmetricAlgorithm>
```

### `EndorsementType`

**Used as:** `cac:IssuerEndorsement`

_1 unique instance across 1 element_

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

### `EndorserPartyType`

**Used as:** `cac:EndorserParty`

_1 unique instance across 1 element_

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

### `EnvironmentalEmissionType`

**Used as:** `cac:EnvironmentalEmission`

_1 unique instance across 1 element_

```xml
<cac:EnvironmentalEmission>
  <cbc:EnvironmentalEmissionTypeCode>CO2</cbc:EnvironmentalEmissionTypeCode>
  <cbc:ValueMeasure>0.2</cbc:ValueMeasure>
  <cbc:Description>200 grams of Carbon Dioxide per km</cbc:Description>
</cac:EnvironmentalEmission>
```

### `EventLineItemType`

**Used as:** `cac:EventLineItem`

_1 unique instance across 1 element_

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

### `EventTacticEnumerationType`

**Used as:** `cac:EventTacticEnumeration`

_1 unique instance across 1 element_

```xml
<cac:EventTacticEnumeration>
  <cbc:DisplayTacticTypeCode>DISPLAY_GENERAL</cbc:DisplayTacticTypeCode>
</cac:EventTacticEnumeration>
```

### `EventTacticType`

**Used as:** `cac:EventTactic`

_1 unique instance across 1 element_

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

### `EvidenceType`

**Used as:** `cac:ReexportationEvidence`

_1 unique instance across 1 element_

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

### `ExceptionCriteriaLineType`

**Used as:** `cac:ExceptionCriteriaLine`

_6 unique instances across 1 element_

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

### `ExceptionNotificationLineType`

**Used as:** `cac:ExceptionNotificationLine`

_3 unique instances across 1 element_

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

### `ExchangeRateType`

**Used as:** `cac:ExchangeRate`

_1 unique instance across 1 element_

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

### `ExternalReferenceType`

**Used as:** `cac:ExternalReference`

_4 unique instances across 1 element_

```xml
<cac:ExternalReference>
  <cbc:URI>UBL-Invoice-2.0-Detached-Signature.xml</cbc:URI>
</cac:ExternalReference>
```

```xml
<cac:ExternalReference>
  <cbc:URI>http://www.suppliersite.eu/sheet001.html</cbc:URI>
</cac:ExternalReference>
```

```xml
<cac:ExternalReference>
  <cbc:URI>normalizedString</cbc:URI>
  <cbc:DocumentHash>String</cbc:DocumentHash>
  <cbc:ExpiryDate>1967-08-13</cbc:ExpiryDate>
  <cbc:ExpiryTime>14:20:00.0Z</cbc:ExpiryTime>
</cac:ExternalReference>
```

```xml
<cac:ExternalReference>
  <cbc:URI>www.digst.dk/udbud/NemID.cer</cbc:URI>
</cac:ExternalReference>
```

### `FinancialAccountType`

**Used as:** `cac:FinancialAccount` · `cac:PayeeFinancialAccount`

_4 unique instances across 2 elements_

```xml
<cac:FinancialAccount>
  <cbc:ID>8601.12.11189</cbc:ID>
  <cbc:PaymentNote>Deutsche Bank</cbc:PaymentNote>
</cac:FinancialAccount>
```

```xml
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
```

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

### `FinancialInstitutionType`

**Used as:** `cac:FinancialInstitution`

_2 unique instances across 1 element_

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

```xml
<cac:FinancialInstitution>
  <cbc:ID>DKDKABCD</cbc:ID>
</cac:FinancialInstitution>
```

### `ForecastExceptionCriterionLineType`

**Used as:** `cac:ForecastExceptionCriterionLine`

_2 unique instances across 1 element_

```xml
<cac:ForecastExceptionCriterionLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriterionLine>
```

```xml
<cac:ForecastExceptionCriterionLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriterionLine>
```

### `ForecastExceptionType`

**Used as:** `cac:ForecastException`

_3 unique instances across 1 element_

```xml
<cac:ForecastException>
  <cbc:ForecastPurposeCode>ORDER_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
  <cbc:IssueDate>2010-04-17</cbc:IssueDate>
  <cbc:IssueTime>10:00:00.000</cbc:IssueTime>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
</cac:ForecastException>
```

```xml
<cac:ForecastException>
  <cbc:ForecastPurposeCode>ORDER_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
  <cbc:IssueDate>2010-04-17</cbc:IssueDate>
  <cbc:IssueTime>10:00:00.000Z</cbc:IssueTime>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
</cac:ForecastException>
```

```xml
<cac:ForecastException>
  <cbc:PurposeCode>ORDER_FORECAST</cbc:PurposeCode>
  <cbc:ForecastTypeCode>TOTAL</cbc:ForecastTypeCode>
  <cbc:IssueDate>2010-04-17</cbc:IssueDate>
  <cbc:IssueTime>10:00:00.000</cbc:IssueTime>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
</cac:ForecastException>
```

### `ForecastLineType`

**Used as:** `cac:ForecastLine`

_1 unique instance across 1 element_

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

### `ForecastRevisionLineType`

**Used as:** `cac:ForecastRevisionLine`

_3 unique instances across 1 element_

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

```xml
<cac:ForecastRevisionLine>
  <cbc:ID>FRL1</cbc:ID>
  <cbc:RevisedForecastLineID>RFL1</cbc:RevisedForecastLineID>
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

```xml
<cac:ForecastRevisionLine>
  <cbc:ID>FRL1</cbc:ID>
  <cbc:RevisedForecastLineID>RFL1</cbc:RevisedForecastLineID>
  <cbc:SourceForecastIssueDate>2005-02-17</cbc:SourceForecastIssueDate>
  <cbc:SourceForecastIssueTime>10:00:00.000Z</cbc:SourceForecastIssueTime>
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

### `GoodsItemPassportCounterfoilType`

**Used as:** `cac:GoodsItemPassportCounterfoil`

_4 unique instances across 1 element_

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

```xml
<cac:GoodsItemPassportCounterfoil>
  <cbc:ID>645634567</cbc:ID>
  <cbc:GoodsItemPassportID>ata01661</cbc:GoodsItemPassportID>
  <cac:CustomsOfficeLocation>
    <cbc:Name>Heiligenhafen</cbc:Name>
  </cac:CustomsOfficeLocation>
  <cac:VoucherDocumentReference>
    <cbc:ID>5234533222</cbc:ID>
  </cac:VoucherDocumentReference>
</cac:GoodsItemPassportCounterfoil>
```

```xml
<cac:GoodsItemPassportCounterfoil>
  <cbc:ID>645634567</cbc:ID>
  <cbc:GoodsItemPassportID>ata01661</cbc:GoodsItemPassportID>
  <cac:CustomsOfficeLocation>
    <cbc:Name>Padborg</cbc:Name>
  </cac:CustomsOfficeLocation>
  <cac:VoucherDocumentReference>
    <cbc:ID>5234533222</cbc:ID>
  </cac:VoucherDocumentReference>
</cac:GoodsItemPassportCounterfoil>
```

```xml
<cac:GoodsItemPassportCounterfoil>
  <cbc:ID>645634567</cbc:ID>
  <cbc:GoodsItemPassportID>ata01661</cbc:GoodsItemPassportID>
  <cac:VoucherDocumentReference>
    <cbc:ID>23445567</cbc:ID>
  </cac:VoucherDocumentReference>
</cac:GoodsItemPassportCounterfoil>
```

### `GoodsItemType`

**Used as:** `cac:GoodsItem`

_32 unique instances across 1 element_

```xml
<cac:GoodsItem>
  <cac:Item>
    <cac:CommodityClassification>
      <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
    </cac:CommodityClassification>
  </cac:Item>
</cac:GoodsItem>
```

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

```xml
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
```

```xml
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
```

```xml
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
```

```xml
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
```

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

```xml
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
```

```xml
<cac:GoodsItem>
  <cbc:ID>GID_1</cbc:ID>
  <cac:Item>
    <cbc:Description>MOTOR CYCLE</cbc:Description>
    <cbc:Name>YAMAHA</cbc:Name>
  </cac:Item>
</cac:GoodsItem>
```

```xml
<cac:GoodsItem>
  <cbc:ID>GID_2</cbc:ID>
  <cac:Item>
    <cbc:Description>MOTOR CYCLE</cbc:Description>
    <cbc:Name>HONDA</cbc:Name>
  </cac:Item>
</cac:GoodsItem>
```

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

```xml
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
```

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

### `InstructionForReturnsLineType`

**Used as:** `cac:InstructionForReturnsLine`

_2 unique instances across 1 element_

```xml
<cac:InstructionForReturnsLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>20</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Denim Jeans Jacket</cbc:Description>
    <cbc:Name>Jeans Jacket man</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>AA109</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>YX401</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:InstructionForReturnsLine>
```

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

### `InventoryReportLineType`

**Used as:** `cac:InventoryReportLine`

_3 unique instances across 1 element_

```xml
<cac:InventoryReportLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:InventoryValueAmount>200</cbc:InventoryValueAmount>
  <cac:Item>
    <cbc:Description>shirt</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>SH009</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>DD88</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:InventoryReportLine>
```

```xml
<cac:InventoryReportLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Quantity>15</cbc:Quantity>
  <cbc:InventoryValueAmount>750</cbc:InventoryValueAmount>
  <cac:Item>
    <cbc:Description>trousers</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>TH009</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>DA008</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:InventoryReportLine>
```

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

### `InvoiceLineType`

**Used as:** `cac:InvoiceLine`

_8 unique instances across 1 element_

```xml
<cac:InvoiceLine>
  <cbc:ID>1</cbc:ID>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cac:Item>
    <cbc:Description>Cotter pin, MIL-SPEC</cbc:Description>
  </cac:Item>
</cac:InvoiceLine>
```

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

### `ItemIdentificationType`

**Used as:** `cac:BuyersItemIdentification` · `cac:SellersItemIdentification` · `cac:StandardItemIdentification`

_44 unique instances across 3 elements_

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>6578481</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>6578489</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>AA109</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>AA128</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>DH019</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>SH009</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>TH009</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>TJ043</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>TS893</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:BuyersItemIdentification>
  <cbc:ID>TT319</cbc:ID>
</cac:BuyersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>100700011021</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>123456</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>17589683</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>17589684</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>BA058</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>DA008</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>DD88</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>JB007</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>JB008</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>JB009</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>JB010</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>JB011</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>K0058</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>MC002</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>PK009</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>PL001</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>SItemNo001</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>SItemNo011</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>YX233</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>YX401</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:SellersItemIdentification>
  <cbc:ID>ZZ738</cbc:ID>
</cac:SellersItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>00123450000580</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>00123450000581</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>00123450000582</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>00123450000583</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>00123450000584</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>06110123456784</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>123452340123</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>1234567890123</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>1234567890124</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>1234567890125</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>1234567890126</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>1234567890127</cbc:ID>
</cac:StandardItemIdentification>
```

```xml
<cac:StandardItemIdentification>
  <cbc:ID>1234567890128</cbc:ID>
</cac:StandardItemIdentification>
```

### `ItemInstanceType`

**Used as:** `cac:ItemInstance`

_2 unique instances across 1 element_

```xml
<cac:ItemInstance>
  <cac:LotIdentification>
    <cbc:LotNumberID>546378239</cbc:LotNumberID>
    <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
  </cac:LotIdentification>
</cac:ItemInstance>
```

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

### `ItemLocationQuantityType`

**Used as:** `cac:ItemLocationQuantity`

_1 unique instance across 1 element_

```xml
<cac:ItemLocationQuantity>
  <cbc:LeadTimeMeasure>3</cbc:LeadTimeMeasure>
  <cbc:MinimumQuantity>2</cbc:MinimumQuantity>
</cac:ItemLocationQuantity>
```

### `ItemManagementProfileType`

**Used as:** `cac:ItemManagementProfile`

_1 unique instance across 1 element_

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

### `ItemPropertyType`

**Used as:** `cac:AdditionalItemProperty`

_12 unique instances across 1 element_

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>AlcoholPercentage</cbc:Name>
  <cbc:Value>0</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>AnimalSpecies</cbc:Name>
  <cbc:Value>Bovine</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Color</cbc:Name>
  <cbc:Value>black</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>DegreeOfPlato</cbc:Name>
  <cbc:Value>0</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Hair color</cbc:Name>
  <cbc:Value>Black</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>LineGrossWeight</cbc:Name>
  <cbc:ValueQuantity>774.144</cbc:ValueQuantity>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>LineNetWeight</cbc:Name>
  <cbc:ValueQuantity>604.8</cbc:ValueQuantity>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Paint type</cbc:Name>
  <cbc:Value>Acrylic</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Quantity</cbc:Name>
  <cbc:ValueQuantity>63.000</cbc:ValueQuantity>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Solvant</cbc:Name>
  <cbc:Value>Water</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Type</cbc:Name>
  <cbc:Value>Cat5</cbc:Value>
</cac:AdditionalItemProperty>
```

```xml
<cac:AdditionalItemProperty>
  <cbc:Name>Width</cbc:Name>
  <cbc:Value>20mm</cbc:Value>
</cac:AdditionalItemProperty>
```

### `ItemType`

**Used as:** `cac:Item` · `cac:SupplyItem`

_70 unique instances across 2 elements_

```xml
<cac:Item>
  <cac:CommodityClassification>
    <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
  </cac:CommodityClassification>
</cac:Item>
```

```xml
<cac:Item>
  <cac:CommodityClassification>
    <cbc:CargoTypeCode>14</cbc:CargoTypeCode>
    <cbc:CommodityCode>8</cbc:CommodityCode>
  </cac:CommodityClassification>
</cac:Item>
```

```xml
<cac:Item>
  <cac:StandardItemIdentification>
    <cbc:ID>06110123456784</cbc:ID>
  </cac:StandardItemIdentification>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Description>Acme knitwear gloves</cbc:Description>
  <cbc:Name>gloves</cbc:Name>
  <cac:BuyersItemIdentification>
    <cbc:ID>6578481</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>17589684</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:StandardItemIdentification>
    <cbc:ID>00123450000583</cbc:ID>
  </cac:StandardItemIdentification>
</cac:Item>
```

```xml
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
```

```xml
<cac:Item>
  <cbc:Description>BACHO S910, Topnøglesæt</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>BOSCH GLL 3-80P Lasernivilering</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>BY45A, Donkraft</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

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
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Cotter pin, MIL-SPEC</cbc:Description>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>DEWALT DC542, Fugepistol</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>DEWALT DC822, Boltspænder</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>DURA PRO 2000kg, Dunkraft</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Denim Jeans Jacket</cbc:Description>
  <cbc:Name>Jeans Jacket man</cbc:Name>
  <cac:BuyersItemIdentification>
    <cbc:ID>AA109</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>YX401</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>ESMOLADARA KH3105, Bænksliber</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>IT</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Fladskærm</cbc:Description>
  <cbc:Name>FP/BL 1908WFP</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>HADEF 250kg, Talje</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>HADEF 750kg, Talje</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Description>KAMA AD 105S, Båndsav</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>KEMPPI MASTER 2200, Tigsvejser</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>FI</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>KING TONY 6316, Topnøglesæt</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Description>Kuulokkeita</cbc:Description>
  <cac:CommodityClassification>
    <cbc:ItemClassificationCode>8518309590</cbc:ItemClassificationCode>
  </cac:CommodityClassification>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>LIFTKET 021/51, Talje</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
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
```

```xml
<cac:Item>
  <cbc:Description>METABO GE700, Pinolsliber</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>METABO SBE 1010, Boremaskine</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>MILWAUKEE HD18PD, Akkuboremaskine</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>US</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>MOTOR CYCLE</cbc:Description>
  <cbc:Name>HONDA</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>MOTOR CYCLE</cbc:Description>
  <cbc:Name>YAMAHA</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Mus</cbc:Description>
  <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Description>Red paint</cbc:Description>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>SCANTOOL 20AT, Søjleboremaskine</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>STAHL WILLE 730/02, Momentnøgle</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DE</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Stationær computer</cbc:Description>
  <cbc:Name>Dell PrecisionTM  T3400</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>T-shirt</cbc:Description>
  <cac:BuyersItemIdentification>
    <cbc:ID>TT319</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>ZZ738</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Tastatur</cbc:Description>
  <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Very good pencils for red paint.</cbc:Description>
  <cbc:Name>Pensel 20 mm</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>SItemNo011</cbc:ID>
  </cac:SellersItemIdentification>
  <cac:StandardItemIdentification>
    <cbc:ID>123452340123</cbc:ID>
  </cac:StandardItemIdentification>
  <cac:AdditionalItemProperty>
    <cbc:Name>Hair color</cbc:Name>
    <cbc:Value>Black</cbc:Value>
  </cac:AdditionalItemProperty>
  <cac:AdditionalItemProperty>
    <cbc:Name>Width</cbc:Name>
    <cbc:Value>20mm</cbc:Value>
  </cac:AdditionalItemProperty>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>Very good pencils for red paint.</cbc:Description>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>VÆRKTØJSKASSE m/div. håndværktøj</cbc:Description>
  <cac:OriginCountry>
    <cbc:IdentificationCode>DK</cbc:IdentificationCode>
  </cac:OriginCountry>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>jersey</cbc:Description>
  <cac:BuyersItemIdentification>
    <cbc:ID>TJ043</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>K0058</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>shirt</cbc:Description>
  <cac:BuyersItemIdentification>
    <cbc:ID>SH009</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>DD88</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Description>trousers</cbc:Description>
  <cac:BuyersItemIdentification>
    <cbc:ID>TH009</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>DA008</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Description>woman's dress</cbc:Description>
  <cac:BuyersItemIdentification>
    <cbc:ID>DH019</cbc:ID>
  </cac:BuyersItemIdentification>
  <cac:SellersItemIdentification>
    <cbc:ID>BA058</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

```xml
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
```

```xml
<cac:Item>
  <cbc:Name>Auxiliary Tool</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Name>High-grade Widget</cbc:Name>
</cac:Item>
```

```xml
<cac:Item>
  <cbc:Name>Magic cloak</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>MC002</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Name>Office Printer 1</cbc:Name>
  <cbc:BrandName>Canon</cbc:BrandName>
  <cbc:ModelName>ModelName28</cbc:ModelName>
  <cac:CommodityClassification>
    <cbc:NatureCode>Machinery / Electrical</cbc:NatureCode>
  </cac:CommodityClassification>
</cac:Item>
```

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

```xml
<cac:Item>
  <cbc:Name>Philosophical lamp</cbc:Name>
  <cac:SellersItemIdentification>
    <cbc:ID>PL001</cbc:ID>
  </cac:SellersItemIdentification>
</cac:Item>
```

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

```xml
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
```

```xml
<cac:Item></cac:Item>
```

```xml
<cac:SupplyItem>
  <cac:StandardItemIdentification>
    <cbc:ID>00123450000580</cbc:ID>
  </cac:StandardItemIdentification>
</cac:SupplyItem>
```

```xml
<cac:SupplyItem>
  <cac:StandardItemIdentification>
    <cbc:ID>00123450000581</cbc:ID>
  </cac:StandardItemIdentification>
</cac:SupplyItem>
```

```xml
<cac:SupplyItem>
  <cac:StandardItemIdentification>
    <cbc:ID>00123450000582</cbc:ID>
  </cac:StandardItemIdentification>
</cac:SupplyItem>
```

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

```xml
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
```

### `LanguageType`

**Used as:** `cac:Language`

_1 unique instance across 1 element_

```xml
<cac:Language>
  <cbc:ID>fi</cbc:ID>
</cac:Language>
```

### `LineItemType`

**Used as:** `cac:LineItem`

_19 unique instances across 1 element_

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cac:Item>
    <cbc:Description>Red paint</cbc:Description>
  </cac:Item>
</cac:LineItem>
```

```xml
<cac:LineItem>
  <cbc:ID>1</cbc:ID>
  <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
  <cac:Item></cac:Item>
</cac:LineItem>
```

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

```xml
<cac:LineItem>
  <cbc:ID>2</cbc:ID>
  <cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
  <cac:Item>
    <cbc:Description>Very good pencils for red paint.</cbc:Description>
  </cac:Item>
</cac:LineItem>
```

```xml
<cac:LineItem>
  <cbc:ID>2</cbc:ID>
  <cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
  <cac:Item></cac:Item>
</cac:LineItem>
```

```xml
<cac:LineItem>
  <cbc:ID>2</cbc:ID>
  <cbc:Quantity>15</cbc:Quantity>
  <cbc:LineExtensionAmount>225</cbc:LineExtensionAmount>
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
    <cbc:PriceAmount>15</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Very good pencils for red paint.</cbc:Description>
    <cbc:Name>Pensel 20 mm</cbc:Name>
    <cac:SellersItemIdentification>
      <cbc:ID>SItemNo011</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>123452340123</cbc:ID>
    </cac:StandardItemIdentification>
    <cac:AdditionalItemProperty>
      <cbc:Name>Hair color</cbc:Name>
      <cbc:Value>Black</cbc:Value>
    </cac:AdditionalItemProperty>
    <cac:AdditionalItemProperty>
      <cbc:Name>Width</cbc:Name>
      <cbc:Value>20mm</cbc:Value>
    </cac:AdditionalItemProperty>
  </cac:Item>
</cac:LineItem>
```

```xml
<cac:LineItem>
  <cbc:ID>DELL1052665</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Stationær computer</cbc:Description>
    <cbc:Name>Dell PrecisionTM  T3400</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

```xml
<cac:LineItem>
  <cbc:ID>DELL1052665</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cbc:LineExtensionAmount>150500.00</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>37625.00</cbc:TotalTaxAmount>
  <cac:Price>
    <cbc:PriceAmount>4300.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Stationær computer</cbc:Description>
    <cbc:Name>Dell PrecisionTM  T3400</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

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

```xml
<cac:LineItem>
  <cbc:ID>DELL2363463</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cbc:LineExtensionAmount>43750.00</cbc:LineExtensionAmount>
  <cbc:TotalTaxAmount>10937.50</cbc:TotalTaxAmount>
  <cac:Price>
    <cbc:PriceAmount>1250.00</cbc:PriceAmount>
    <cbc:BaseQuantity>1</cbc:BaseQuantity>
  </cac:Price>
  <cac:Item>
    <cbc:Description>Fladskærm</cbc:Description>
    <cbc:Name>FP/BL 1908WFP</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

```xml
<cac:LineItem>
  <cbc:ID>DELL2367452</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Mus</cbc:Description>
    <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

```xml
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
```

```xml
<cac:LineItem>
  <cbc:ID>DELL8436783</cbc:ID>
  <cbc:Quantity>35</cbc:Quantity>
  <cac:Item>
    <cbc:Description>Tastatur</cbc:Description>
    <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
  </cac:Item>
</cac:LineItem>
```

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

### `LocationCoordinateType`

**Used as:** `cac:LocationCoordinate`

_4 unique instances across 1 element_

```xml
<cac:LocationCoordinate>
  <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
  <cbc:LatitudeDegreesMeasure>53.33</cbc:LatitudeDegreesMeasure>
  <cbc:LatitudeMinutesMeasure>49</cbc:LatitudeMinutesMeasure>
  <cbc:LatitudeDirectionCode>North</cbc:LatitudeDirectionCode>
  <cbc:LongitudeDegreesMeasure>8.33</cbc:LongitudeDegreesMeasure>
  <cbc:LongitudeMinutesMeasure>49</cbc:LongitudeMinutesMeasure>
  <cbc:LongitudeDirectionCode>East</cbc:LongitudeDirectionCode>
</cac:LocationCoordinate>
```

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

```xml
<cac:LocationCoordinate>
  <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
  <cbc:LatitudeDegreesMeasure>58</cbc:LatitudeDegreesMeasure>
  <cbc:LongitudeDegreesMeasure>10</cbc:LongitudeDegreesMeasure>
</cac:LocationCoordinate>
```

```xml
<cac:LocationCoordinate></cac:LocationCoordinate>
```

### `LocationType`

**Used as:** `cac:ActivityFinalLocation` · `cac:ActivityOriginLocation` · `cac:CustomsExitOfficeLocation` · `cac:CustomsOfficeLocation` · `cac:DeliveryLocation` · `cac:FirstArrivalPortLocation` · `cac:FromLocation` · `cac:ImportCustomsExitOfficeLocation` · `cac:LastExitPortLocation` · `cac:LoadingPortLocation` · `cac:Location` · `cac:OfficeOfEntryLocation` · `cac:ParticipatingLocationsLocation` · `cac:PhysicalLocation` · `cac:PickupLocation` · `cac:PointOfSaleLocation` · `cac:ReportingLocation` · `cac:StatusLocation` · `cac:ToLocation` · `cac:TransitCustomsExitOfficeLocation` · `cac:TransshipPortLocation` · `cac:UnloadingPortLocation`

_78 unique instances across 22 elements_

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

```xml
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
```

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

```xml
<cac:ActivityOriginLocation>
  <cbc:ID>1234567890</cbc:ID>
</cac:ActivityOriginLocation>
```

```xml
<cac:ActivityOriginLocation>
  <cbc:ID></cbc:ID>
</cac:ActivityOriginLocation>
```

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

```xml
<cac:CustomsOfficeLocation>
  <cbc:Name>Bietingen</cbc:Name>
</cac:CustomsOfficeLocation>
```

```xml
<cac:CustomsOfficeLocation>
  <cbc:Name>Heiligenhafen</cbc:Name>
</cac:CustomsOfficeLocation>
```

```xml
<cac:CustomsOfficeLocation>
  <cbc:Name>Padborg</cbc:Name>
</cac:CustomsOfficeLocation>
```

```xml
<cac:DeliveryLocation>
  <cac:Address>
    <cbc:CityName>Hamburg</cbc:CityName>
  </cac:Address>
</cac:DeliveryLocation>
```

```xml
<cac:DeliveryLocation>
  <cac:Address>
    <cbc:CityName>Munich</cbc:CityName>
  </cac:Address>
</cac:DeliveryLocation>
```

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

```xml
<cac:DeliveryLocation>
  <cbc:ID>GBBRS</cbc:ID>
  <cbc:Description>Bristol</cbc:Description>
</cac:DeliveryLocation>
```

```xml
<cac:DeliveryLocation>
  <cbc:ID>GBFXT</cbc:ID>
  <cbc:Description>Felixstowe</cbc:Description>
</cac:DeliveryLocation>
```

```xml
<cac:DeliveryLocation>
  <cbc:ID>STO</cbc:ID>
</cac:DeliveryLocation>
```

```xml
<cac:DeliveryLocation>
  <cbc:Name>9000</cbc:Name>
</cac:DeliveryLocation>
```

```xml
<cac:DeliveryLocation>
  <cbc:Name>BANGKOK</cbc:Name>
</cac:DeliveryLocation>
```

```xml
<cac:DeliveryLocation>
  <cbc:Name>Balboa Port</cbc:Name>
</cac:DeliveryLocation>
```

```xml
<cac:FirstArrivalPortLocation>
  <cbc:ID>FI015300</cbc:ID>
</cac:FirstArrivalPortLocation>
```

```xml
<cac:FirstArrivalPortLocation>
  <cbc:ID>GBBRS</cbc:ID>
  <cbc:Description>Bristol</cbc:Description>
</cac:FirstArrivalPortLocation>
```

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

```xml
<cac:FirstArrivalPortLocation>
  <cbc:Name>Padborg</cbc:Name>
</cac:FirstArrivalPortLocation>
```

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

```xml
<cac:ImportCustomsExitOfficeLocation>
  <cbc:ID>CH002621</cbc:ID>
</cac:ImportCustomsExitOfficeLocation>
```

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

```xml
<cac:LastExitPortLocation>
  <cbc:ID>USBOS</cbc:ID>
  <cbc:Description>Boston</cbc:Description>
</cac:LastExitPortLocation>
```

```xml
<cac:LastExitPortLocation>
  <cbc:Name>Bietingen</cbc:Name>
</cac:LastExitPortLocation>
```

```xml
<cac:LoadingPortLocation>
  <cbc:ID>Aarhus</cbc:ID>
</cac:LoadingPortLocation>
```

```xml
<cac:LoadingPortLocation>
  <cbc:ID>USBOS</cbc:ID>
  <cbc:Description>Boston Airport</cbc:Description>
</cac:LoadingPortLocation>
```

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

```xml
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
```

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

```xml
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
```

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

```xml
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
```

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

```xml
<cac:Location>
  <cbc:ID>CNSHA</cbc:ID>
</cac:Location>
```

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

```xml
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
```

```xml
<cac:Location>
  <cbc:ID>DEHAM</cbc:ID>
</cac:Location>
```

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

```xml
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
```

```xml
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
```

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

```xml
<cac:ParticipatingLocationsLocation>
  <cbc:ID>ACME_BR_BE_0023</cbc:ID>
</cac:ParticipatingLocationsLocation>
```

```xml
<cac:PhysicalLocation>
  <cac:Address>
    <cbc:CityName>Espoo</cbc:CityName>
  </cac:Address>
</cac:PhysicalLocation>
```

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

```xml
<cac:PhysicalLocation>
  <cbc:InformationURI>https://goo.gl/maps/2k242</cbc:InformationURI>
</cac:PhysicalLocation>
```

```xml
<cac:PickupLocation>
  <cbc:ID>01530</cbc:ID>
  <cbc:LocationTypeCode>P</cbc:LocationTypeCode>
</cac:PickupLocation>
```

```xml
<cac:PickupLocation>
  <cbc:ID>FI1234567-8R0001</cbc:ID>
  <cbc:LocationTypeCode>L</cbc:LocationTypeCode>
</cac:PickupLocation>
```

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

```xml
<cac:TransitCustomsExitOfficeLocation>
  <cbc:ID>FI001800</cbc:ID>
</cac:TransitCustomsExitOfficeLocation>
```

```xml
<cac:TransshipPortLocation>
  <cbc:ID>GBLHR</cbc:ID>
  <cbc:Description>Heathrow Apt/London</cbc:Description>
</cac:TransshipPortLocation>
```

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

```xml
<cac:UnloadingPortLocation>
  <cbc:ID>Balboa Port</cbc:ID>
</cac:UnloadingPortLocation>
```

```xml
<cac:UnloadingPortLocation>
  <cbc:ID>GBBRS</cbc:ID>
  <cbc:Description>Bristol Airport</cbc:Description>
</cac:UnloadingPortLocation>
```

### `LotIdentificationType`

**Used as:** `cac:LotIdentification`

_2 unique instances across 1 element_

```xml
<cac:LotIdentification>
  <cbc:LotNumberID>546378239</cbc:LotNumberID>
  <cbc:ExpiryDate>2010-01-01</cbc:ExpiryDate>
</cac:LotIdentification>
```

```xml
<cac:LotIdentification>
  <cbc:LotNumberID>9390000757</cbc:LotNumberID>
</cac:LotIdentification>
```

### `MaritimeTransportType`

**Used as:** `cac:MaritimeTransport`

_4 unique instances across 1 element_

```xml
<cac:MaritimeTransport>
  <cbc:VesselID>3852664</cbc:VesselID>
  <cbc:VesselName>Vessel Name</cbc:VesselName>
</cac:MaritimeTransport>
```

```xml
<cac:MaritimeTransport>
  <cbc:VesselID>Eestiship</cbc:VesselID>
</cac:MaritimeTransport>
```

```xml
<cac:MaritimeTransport>
  <cbc:VesselID>IMO1234567</cbc:VesselID>
  <cbc:VesselName>MS Enova</cbc:VesselName>
</cac:MaritimeTransport>
```

```xml
<cac:MaritimeTransport>
  <cbc:VesselID>SomeIMONr</cbc:VesselID>
  <cbc:VesselName>SomeVesselName</cbc:VesselName>
</cac:MaritimeTransport>
```

### `MessageDeliveryType`

**Used as:** `cac:DigitalMessageDelivery`

_4 unique instances across 1 element_

```xml
<cac:DigitalMessageDelivery>
  <cbc:ProtocolID>AS2</cbc:ProtocolID>
  <cbc:EndpointURI>http://as2.buyer.biz</cbc:EndpointURI>
</cac:DigitalMessageDelivery>
```

```xml
<cac:DigitalMessageDelivery>
  <cbc:ProtocolID>AS2</cbc:ProtocolID>
  <cbc:EndpointURI>http://as2.buyer.de</cbc:EndpointURI>
</cac:DigitalMessageDelivery>
```

```xml
<cac:DigitalMessageDelivery>
  <cbc:ProtocolID>AS2</cbc:ProtocolID>
  <cbc:EndpointURI>http://as2.papifood.dk</cbc:EndpointURI>
</cac:DigitalMessageDelivery>
```

```xml
<cac:DigitalMessageDelivery>
  <cbc:ProtocolID>AS2</cbc:ProtocolID>
  <cbc:EndpointURI>http://as2.vendor.biz</cbc:EndpointURI>
</cac:DigitalMessageDelivery>
```

### `MonetaryTotalType`

**Used as:** `cac:AnticipatedMonetaryTotal` · `cac:LegalMonetaryTotal` · `cac:QuotedMonetaryTotal` · `cac:RequestedMonetaryTotal`

_12 unique instances across 4 elements_

```xml
<cac:AnticipatedMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:PayableAmount>100.00</cbc:PayableAmount>
</cac:AnticipatedMonetaryTotal>
```

```xml
<cac:AnticipatedMonetaryTotal>
  <cbc:LineExtensionAmount>1000.00</cbc:LineExtensionAmount>
  <cbc:PayableAmount>1000.00</cbc:PayableAmount>
</cac:AnticipatedMonetaryTotal>
```

```xml
<cac:AnticipatedMonetaryTotal>
  <cbc:LineExtensionAmount>6225</cbc:LineExtensionAmount>
  <cbc:AllowanceTotalAmount>100</cbc:AllowanceTotalAmount>
  <cbc:ChargeTotalAmount>100</cbc:ChargeTotalAmount>
  <cbc:PayableAmount>6225</cbc:PayableAmount>
</cac:AnticipatedMonetaryTotal>
```

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:AllowanceTotalAmount>10.00</cbc:AllowanceTotalAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

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

```xml
<cac:LegalMonetaryTotal>
  <cbc:LineExtensionAmount>23.20</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>23.20</cbc:TaxExclusiveAmount>
  <cbc:TaxInclusiveAmount>29.00</cbc:TaxInclusiveAmount>
  <cbc:AllowanceTotalAmount>5.00</cbc:AllowanceTotalAmount>
  <cbc:ChargeTotalAmount>1.00</cbc:ChargeTotalAmount>
  <cbc:PayableAmount>25.00</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

```xml
<cac:LegalMonetaryTotal>
  <cbc:PayableAmount>100.00</cbc:PayableAmount>
</cac:LegalMonetaryTotal>
```

```xml
<cac:QuotedMonetaryTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:QuotedMonetaryTotal>
```

```xml
<cac:QuotedMonetaryTotal>
  <cbc:LineExtensionAmount>197750.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>49437.50</cbc:TaxExclusiveAmount>
  <cbc:TaxInclusiveAmount>247187.50</cbc:TaxInclusiveAmount>
  <cbc:PayableAmount>247187.50</cbc:PayableAmount>
</cac:QuotedMonetaryTotal>
```

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

### `NotificationRequirementType`

**Used as:** `cac:NotificationRequirement`

_3 unique instances across 1 element_

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

### `OrderLineReferenceType`

**Used as:** `cac:OrderLineReference`

_7 unique instances across 1 element_

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

```xml
<cac:OrderLineReference>
  <cbc:LineID>1</cbc:LineID>
</cac:OrderLineReference>
```

```xml
<cac:OrderLineReference>
  <cbc:LineID>2</cbc:LineID>
</cac:OrderLineReference>
```

```xml
<cac:OrderLineReference>
  <cbc:LineID>3</cbc:LineID>
</cac:OrderLineReference>
```

```xml
<cac:OrderLineReference>
  <cbc:LineID>4</cbc:LineID>
</cac:OrderLineReference>
```

```xml
<cac:OrderLineReference>
  <cbc:LineID>5</cbc:LineID>
</cac:OrderLineReference>
```

### `OrderLineType`

**Used as:** `cac:OrderLine`

_9 unique instances across 1 element_

```xml
<cac:OrderLine>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cac:Item>
      <cbc:Description>Red paint</cbc:Description>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

```xml
<cac:OrderLine>
  <cac:LineItem>
    <cbc:ID>1</cbc:ID>
    <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
    <cac:Item></cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

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

```xml
<cac:OrderLine>
  <cac:LineItem>
    <cbc:ID>2</cbc:ID>
    <cbc:LineStatusCode>Disputed</cbc:LineStatusCode>
    <cac:Item></cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

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

```xml
<cac:OrderLine>
  <cbc:Note>Freetext note on line 2</cbc:Note>
  <cac:LineItem>
    <cbc:ID>2</cbc:ID>
    <cbc:Quantity>15</cbc:Quantity>
    <cbc:LineExtensionAmount>225</cbc:LineExtensionAmount>
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
      <cbc:PriceAmount>15</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Very good pencils for red paint.</cbc:Description>
      <cbc:Name>Pensel 20 mm</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>SItemNo011</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID>123452340123</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Hair color</cbc:Name>
        <cbc:Value>Black</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Width</cbc:Name>
        <cbc:Value>20mm</cbc:Value>
      </cac:AdditionalItemProperty>
    </cac:Item>
  </cac:LineItem>
</cac:OrderLine>
```

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

### `OrderReferenceType`

**Used as:** `cac:OrderReference`

_3 unique instances across 1 element_

```xml
<cac:OrderReference>
  <cbc:ID>123</cbc:ID>
</cac:OrderReference>
```

```xml
<cac:OrderReference>
  <cbc:ID>34</cbc:ID>
</cac:OrderReference>
```

```xml
<cac:OrderReference>
  <cbc:ID>AEG012345</cbc:ID>
  <cbc:SalesOrderID>CON0095678</cbc:SalesOrderID>
  <cbc:UUID>6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1</cbc:UUID>
  <cbc:IssueDate>2005-06-20</cbc:IssueDate>
</cac:OrderReference>
```

### `PackageType`

**Used as:** `cac:ActualPackage` · `cac:ContainingPackage` · `cac:Package`

_10 unique instances across 3 elements_

```xml
<cac:ActualPackage>
  <cbc:Quantity>10</cbc:Quantity>
  <cbc:PackagingTypeCode>TB</cbc:PackagingTypeCode>
</cac:ActualPackage>
```

```xml
<cac:ContainingPackage>
  <cbc:ID>567-3456</cbc:ID>
  <cbc:Quantity>5</cbc:Quantity>
  <cbc:PackagingTypeCode>CS</cbc:PackagingTypeCode>
</cac:ContainingPackage>
```

```xml
<cac:ContainingPackage>
  <cbc:ID>YangMei</cbc:ID>
  <cbc:Quantity>1</cbc:Quantity>
  <cbc:PackagingTypeCode>CT</cbc:PackagingTypeCode>
</cac:ContainingPackage>
```

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

```xml
<cac:Package>
  <cbc:ID>CON_1</cbc:ID>
  <cbc:Quantity>10</cbc:Quantity>
</cac:Package>
```

```xml
<cac:Package>
  <cbc:ID>CON_2</cbc:ID>
  <cbc:Quantity>10</cbc:Quantity>
</cac:Package>
```

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

```xml
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
```

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

### `ParticipantPartyType`

**Used as:** `cac:ParticipantParty`

_3 unique instances across 1 element_

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

```xml
<cac:ParticipantParty>
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

### `PartyIdentificationType`

**Used as:** `cac:PartyIdentification`

_50 unique instances across 1 element_

```xml
<cac:PartyIdentification>
  <cbc:ID>0004424005</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>0012345000058</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>0012345000359</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>0245442-8</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>098740918237</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>0987678321123</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>1080</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>1234567-8</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>123456789</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>1234</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>1236541</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>13234212</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>1</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>2203148000007</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>345KS5324</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058673821325</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058673827000</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058673827100</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058673827112</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058673827123</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058673827641</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>4058675698641</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>5398000392577</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>5790000127777</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>5798000416604</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>67654328394567</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>6903148000007</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>7300070011115</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>8596</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>987654321</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>DK003102</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>DK10035643</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>DK12345678</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>DK18296799</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>EmployeeXXX</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>FI0245442-8</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>FI1234567-1</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>FI1234567-8</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>FI1234569-8</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>GB999999973</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>IT01234567890</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>M165</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>MyParty</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>Other</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>PartyID123</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>STD14037</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>SellerPartyID123</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>Supp123</cbc:ID>
</cac:PartyIdentification>
```

```xml
<cac:PartyIdentification>
  <cbc:ID>XXX</cbc:ID>
</cac:PartyIdentification>
```

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

### `PartyLegalEntityType`

**Used as:** `cac:PartyLegalEntity`

_20 unique instances across 1 element_

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>1323421212</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>16077593</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>43232010</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>45789034</cbc:CompanyID>
  <cbc:RegistrationDate>1957-08-13</cbc:RegistrationDate>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>45789034</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>6411982340</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>945030345</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>DE122125278</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>DK12345678</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>DK43232010</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:CompanyID>DK89343487</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
  <cbc:CompanyID>18296799</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>Delcomputer A/S</cbc:RegistrationName>
  <cbc:CompanyID>DK18296799</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>Gentofte Kommune</cbc:RegistrationName>
  <cbc:CompanyID>DK12345678</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
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
```

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

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>ROAD CARRIER GmbH</cbc:RegistrationName>
  <cbc:CompanyID>989987876</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
<cac:PartyLegalEntity>
  <cbc:RegistrationName>SuperCompany</cbc:RegistrationName>
  <cbc:CompanyID>DK59873677</cbc:CompanyID>
</cac:PartyLegalEntity>
```

```xml
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
```

```xml
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
```

### `PartyNameType`

**Used as:** `cac:PartyName`

_81 unique instances across 1 element_

```xml
<cac:PartyName>
  <cbc:Name>ACME Corporation</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ACME Ltd.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>AOO Tehnika</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ARRIVA</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>AZ Outsourcing srl</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Arancio Forniture spa</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Automat AG</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Beta Shop</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Boston Road</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Buyer GmbH</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Buyercompany ltd</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>CARRIER SERVICE LTD</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>CONSIGNEE</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>CUSTOMER SERVICE LTD</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Consignee W</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Consignee</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ConsigneeExample</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Consignor</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ConsignorExample</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Consortial</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Coop Extra Bergen</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Custom Cotter Pins</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>D2D GmbH</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>DB</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Dansk Erhverv</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Dansk Industri</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Declarant Inc</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Delcomputer A/S</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Deutscher Industrie- und Handelskammertag e.V.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Disfruta</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>EXT-HAL</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Ebeneser Scrooge Inc.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Elektroniikka Oy</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Example Shipping</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Example Supplies Ltd.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ExampleName</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>FORWARDER</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>FirstAgency</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Gadgets R Us, Inc.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Gedevang Mejeri</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Gentofte Kommune</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Grenå Tools</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Huisin Huolinta Oy</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Huolitsija Oy</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>IYT Corporation</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Jane Doe</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Johnssons byggvaror</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Josef K.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Keep On Trucking</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>LEONARDO</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>La Spezia Container Terminal</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Lisboa Harbour</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>MAERSK</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Maersk</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Moderna Produkter AB</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>NECOSS</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>NTT</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>North American Veeblefetzer</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>OASIS</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>One-Stop Forwarders</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>OpenPEPPOL AISBL</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Organization for the Advancement of Structured Information Standards</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Papirøen Food ApS</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>RAIL CARRIER</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ROAD CARRIER 2</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>ROAD CARRIER</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>SEA CARRIER</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>STEFCO A/S</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Salescompany ltd.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Slow Food Srl</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>SuperCompany</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Swedish trucking</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>The Terminus</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Told Service A/S</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Toldstyrelsen</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>United Airfreight</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Vendor Inc.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>World Events Ltd.</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Yang Mei Electronic Ltd</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Ylermi Huisi 09-55555555</cbc:Name>
</cac:PartyName>
```

```xml
<cac:PartyName>
  <cbc:Name>Zollamt</cbc:Name>
</cac:PartyName>
```

### `PartyTaxSchemeType`

**Used as:** `cac:PartyTaxScheme`

_10 unique instances across 1 element_

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>BE54321</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>BE987654321</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>DK123456789</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>DK12345678</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>63</cbc:ID>
    <cbc:Name>Moms</cbc:Name>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>DK12345</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:CompanyID>DK18296799</cbc:CompanyID>
  <cac:TaxScheme>
    <cbc:ID>63</cbc:ID>
    <cbc:Name>Moms</cbc:Name>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:RegistrationName>Bridgtow District Council</cbc:RegistrationName>
  <cbc:CompanyID>12356478</cbc:CompanyID>
  <cbc:ExemptionReason>Local Authority</cbc:ExemptionReason>
  <cac:TaxScheme>
    <cbc:ID>UK VAT</cbc:ID>
    <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

```xml
<cac:PartyTaxScheme>
  <cbc:RegistrationName>Farthing Purchasing Consortia</cbc:RegistrationName>
  <cbc:CompanyID>175 269 2355</cbc:CompanyID>
  <cbc:ExemptionReason>N/A</cbc:ExemptionReason>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
    <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
  </cac:TaxScheme>
</cac:PartyTaxScheme>
```

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

### `PartyType`

**Used as:** `cac:AgentParty` · `cac:BusinessParty` · `cac:CarrierParty` · `cac:ConsigneeParty` · `cac:ConsignorParty` · `cac:CustomsParty` · `cac:DeliveryParty` · `cac:DespatchParty` · `cac:ExporterParty` · `cac:ExportingGuarantorParty` · `cac:FinalDeliveryParty` · `cac:FreightForwarderParty` · `cac:GovernorParty` · `cac:HolderParty` · `cac:ImporterParty` · `cac:ImportingCustomsParty` · `cac:ImportingGuarantorParty` · `cac:InventoryReportingParty` · `cac:IssuerParty` · `cac:ManufacturerParty` · `cac:NotifierParty` · `cac:NotifyParty` · `cac:OriginatorParty` · `cac:Party` · `cac:PayeeParty` · `cac:ReceiverParty` · `cac:ReporterParty` · `cac:RepresentativeParty` · `cac:ResponsibleParty` · `cac:SenderParty` · `cac:SendingLogisticsOperatorParty` · `cac:SignatoryParty` · `cac:SourceIssuerParty` · `cac:TransitExporterParty` · `cac:TransportServiceProviderParty` · `cac:TransportUserParty` · `cac:WeighingParty`

_146 unique instances across 37 elements_

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

```xml
<cac:AgentParty>
  <cac:PartyName>
    <cbc:Name>Ylermi Huisi 09-55555555</cbc:Name>
  </cac:PartyName>
</cac:AgentParty>
```

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

```xml
<cac:BusinessParty>
  <cbc:EndpointID>9994567987654</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>IT01234567890</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Slow Food Srl</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>La Spezia</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:BusinessParty>
```

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

```xml
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
```

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

```xml
<cac:CustomsParty>
  <cac:PartyIdentification>
    <cbc:ID>0245442-8</cbc:ID>
  </cac:PartyIdentification>
</cac:CustomsParty>
```

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

```xml
<cac:CustomsParty>
  <cac:PartyIdentification>
    <cbc:ID>FI0245442-8</cbc:ID>
  </cac:PartyIdentification>
</cac:CustomsParty>
```

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

```xml
<cac:DespatchParty>
  <cac:PartyName>
    <cbc:Name>Consortial</cbc:Name>
  </cac:PartyName>
</cac:DespatchParty>
```

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
    <cbc:CompanyID>DK43232010</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:ExportingGuarantorParty>
```

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

```xml
<cac:IssuerParty>
  <cac:PartyIdentification>
    <cbc:ID>1</cbc:ID>
  </cac:PartyIdentification>
</cac:IssuerParty>
```

```xml
<cac:IssuerParty>
  <cac:PartyName>
    <cbc:Name>Boston Road</cbc:Name>
  </cac:PartyName>
</cac:IssuerParty>
```

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

```xml
<cac:IssuerParty>
  <cac:PartyName>
    <cbc:Name>Maersk</cbc:Name>
  </cac:PartyName>
</cac:IssuerParty>
```

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

```xml
<cac:NotifierParty>
  <cac:PartyIdentification>
    <cbc:ID>FI1234567-8</cbc:ID>
  </cac:PartyIdentification>
</cac:NotifierParty>
```

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

```xml
<cac:NotifyParty>
  <cbc:EndpointID>www.consignee.com/statusnotifications/</cbc:EndpointID>
  <cac:PartyName>
    <cbc:Name>Consignee</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:ElectronicMail>someName@consignee.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:NotifyParty>
```

```xml
<cac:NotifyParty>
  <cbc:EndpointID>www.consignee.de/statusnotifications/</cbc:EndpointID>
  <cac:PartyName>
    <cbc:Name>Consignee</cbc:Name>
  </cac:PartyName>
  <cac:Contact>
    <cbc:ElectronicMail>someName@consignee.de</cbc:ElectronicMail>
  </cac:Contact>
</cac:NotifyParty>
```

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

```xml
<cac:NotifyParty>
  <cbc:WebsiteURI>http://www.CONSIGNEE.no/statusreceptioninterface#2</cbc:WebsiteURI>
  <cac:PartyName>
    <cbc:Name>CONSIGNEE</cbc:Name>
  </cac:PartyName>
</cac:NotifyParty>
```

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

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>0012345000058</cbc:ID>
  </cac:PartyIdentification>
</cac:Party>
```

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>0012345000359</cbc:ID>
  </cac:PartyIdentification>
</cac:Party>
```

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

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>2203148000007</cbc:ID>
  </cac:PartyIdentification>
</cac:Party>
```

```xml
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
```

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>6903148000007</cbc:ID>
  </cac:PartyIdentification>
</cac:Party>
```

```xml
<cac:Party>
  <cac:PartyIdentification>
    <cbc:ID>Other</cbc:ID>
  </cac:PartyIdentification>
</cac:Party>
```

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

```xml
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
```

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

```xml
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
```

```xml
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
</cac:Party>
```

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>Custom Cotter Pins</cbc:Name>
  </cac:PartyName>
</cac:Party>
```

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
```

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>Jane Doe</cbc:Name>
  </cac:PartyName>
</cac:Party>
```

```xml
<cac:Party>
  <cac:PartyName>
    <cbc:Name>North American Veeblefetzer</cbc:Name>
  </cac:PartyName>
</cac:Party>
```

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
    <cbc:Telephone>+ 44 127 98876545</cbc:Telephone>
    <cbc:Telefax>+ 44 127 98876546</cbc:Telefax>
    <cbc:ElectronicMail>smassiah@the-email.co.uk</cbc:ElectronicMail>
  </cac:Contact>
</cac:Party>
```

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
    <cbc:FamilyName>Salemacher</cbc:FamilyName>
    <cbc:MiddleName>M</cbc:MiddleName>
    <cbc:JobTitle>Sales manager</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

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
    <cbc:FamilyName>Doe</cbc:FamilyName>
    <cbc:MiddleName>X</cbc:MiddleName>
    <cbc:JobTitle>Purchasing manager</cbc:JobTitle>
  </cac:Person>
</cac:Party>
```

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

```xml
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
```

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
    <cbc:CompanyID>DK18296799</cbc:CompanyID>
  </cac:PartyLegalEntity>
</cac:Party>
```

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
</cac:PayeeParty>
```

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

```xml
<cac:ReceiverParty>
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
</cac:ReceiverParty>
```

```xml
<cac:ReceiverParty>
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
</cac:ReceiverParty>
```

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

```xml
<cac:ReceiverParty>
  <cbc:EndpointID>9994567987654</cbc:EndpointID>
  <cac:PartyIdentification>
    <cbc:ID>IT01234567890</cbc:ID>
  </cac:PartyIdentification>
  <cac:PartyName>
    <cbc:Name>Slow Food Srl</cbc:Name>
  </cac:PartyName>
  <cac:PostalAddress>
    <cbc:CityName>La Spezia</cbc:CityName>
    <cac:Country>
      <cbc:IdentificationCode>IT</cbc:IdentificationCode>
    </cac:Country>
  </cac:PostalAddress>
</cac:ReceiverParty>
```

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

```xml
<cac:SenderParty>
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
</cac:SenderParty>
```

```xml
<cac:SenderParty>
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
</cac:SenderParty>
```

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
</cac:SenderParty>
```

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

```xml
<cac:SenderParty>
  <cbc:IndustryClassificationCode>Public Rail Authorities</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>DB</cbc:Name>
  </cac:PartyName>
</cac:SenderParty>
```

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

```xml
<cac:SignatoryParty>
  <cac:PartyIdentification>
    <cbc:ID>MyParty</cbc:ID>
  </cac:PartyIdentification>
</cac:SignatoryParty>
```

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

```xml
<cac:SourceIssuerParty>
  <cbc:IndustryClassificationCode>Public Rail Authorities</cbc:IndustryClassificationCode>
  <cac:PartyName>
    <cbc:Name>DB</cbc:Name>
  </cac:PartyName>
</cac:SourceIssuerParty>
```

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

```xml
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
```

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

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

### `PaymentMeansType`

**Used as:** `cac:PaymentMeans`

_6 unique instances across 1 element_

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>10</cbc:PaymentMeansCode>
  <cbc:PaymentMeansDescription>Cash</cbc:PaymentMeansDescription>
  <cbc:PaymentID>1</cbc:PaymentID>
</cac:PaymentMeans>
```

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

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>20</cbc:PaymentMeansCode>
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
</cac:PaymentMeans>
```

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

```xml
<cac:PaymentMeans>
  <cbc:PaymentMeansCode>20</cbc:PaymentMeansCode>
  <cbc:PaymentDueDate>2005-07-21</cbc:PaymentDueDate>
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
</cac:PaymentMeans>
```

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

### `PaymentTermsType`

**Used as:** `cac:PaymentTerms` · `cac:ServiceChargePaymentTerms`

_8 unique instances across 2 elements_

```xml
<cac:PaymentTerms>
  <cbc:Note>PER THIRTY DAYS</cbc:Note>
</cac:PaymentTerms>
```

```xml
<cac:PaymentTerms>
  <cbc:Note>Payable within 1 calendar month from the invoice date</cbc:Note>
</cac:PaymentTerms>
```

```xml
<cac:PaymentTerms>
  <cbc:Note>Payment due immediately</cbc:Note>
</cac:PaymentTerms>
```

```xml
<cac:PaymentTerms>
  <cbc:Note>Penalty percentage 10% from due date</cbc:Note>
</cac:PaymentTerms>
```

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

```xml
<cac:PaymentTerms>
  <cbc:Note>Per thirty days</cbc:Note>
  <cbc:Note>See web site for price scheme</cbc:Note>
  <cbc:PaymentTermsDetailsURI>www.ROADCARRIER.de/prices.html</cbc:PaymentTermsDetailsURI>
</cac:PaymentTerms>
```

```xml
<cac:PaymentTerms>
  <cbc:PaymentMeansID>Bankers Cheque</cbc:PaymentMeansID>
</cac:PaymentTerms>
```

```xml
<cac:ServiceChargePaymentTerms>
  <cbc:Amount>2500</cbc:Amount>
  <cbc:PaymentDueDate>2011-11-06</cbc:PaymentDueDate>
</cac:ServiceChargePaymentTerms>
```

### `PaymentType`

**Used as:** `cac:Payment`

_1 unique instance across 1 element_

```xml
<cac:Payment>
  <cbc:ID>1</cbc:ID>
  <cbc:PaidAmount>25.00</cbc:PaidAmount>
  <cbc:PaidCashAmount>30.00</cbc:PaidCashAmount>
  <cbc:CashChangeAmount>5.00</cbc:CashChangeAmount>
</cac:Payment>
```

### `PerformanceDataLineType`

**Used as:** `cac:PerformanceDataLine`

_2 unique instances across 1 element_

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

```xml
<cac:PerformanceDataLine>
  <cbc:ID>PDL_2009_02</cbc:ID>
  <cbc:PerformanceValueQuantity>160</cbc:PerformanceValueQuantity>
  <cbc:PerformanceMetricTypeCode>GROSS_MARGIN</cbc:PerformanceMetricTypeCode>
  <cac:Period>
    <cbc:StartDate>2009-08-01</cbc:StartDate>
    <cbc:EndDate>2009-12-31</cbc:EndDate>
  </cac:Period>
  <cac:Item>
    <cbc:Description>Acme knitwear gloves</cbc:Description>
    <cbc:Name>gloves</cbc:Name>
    <cac:BuyersItemIdentification>
      <cbc:ID>6578481</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>17589684</cbc:ID>
    </cac:SellersItemIdentification>
    <cac:StandardItemIdentification>
      <cbc:ID>00123450000583</cbc:ID>
    </cac:StandardItemIdentification>
  </cac:Item>
</cac:PerformanceDataLine>
```

### `PeriodType`

**Used as:** `cac:ActivityPeriod` · `cac:AdoptionPeriod` · `cac:EffectivePeriod` · `cac:EstimatedDeliveryPeriod` · `cac:ExceptionObservationPeriod` · `cac:ForecastPeriod` · `cac:InventoryPeriod` · `cac:InvoicePeriod` · `cac:Period` · `cac:RequestedDeliveryPeriod` · `cac:ServiceAvailabilityPeriod` · `cac:ServiceEndTimePeriod` · `cac:ServiceMaintenancePeriod` · `cac:ServiceStartTimePeriod` · `cac:SettlementPeriod` · `cac:StatementPeriod` · `cac:TransitPeriod` · `cac:TransportServiceProviderResponseDeadlinePeriod` · `cac:TransportUserResponseRequiredPeriod` · `cac:ValidityPeriod`

_77 unique instances across 20 elements_

```xml
<cac:ActivityPeriod>
  <cbc:StartDate>2005-02-26</cbc:StartDate>
  <cbc:EndDate>2005-12-26</cbc:EndDate>
</cac:ActivityPeriod>
```

```xml
<cac:ActivityPeriod>
  <cbc:StartDate>2010-04-07</cbc:StartDate>
</cac:ActivityPeriod>
```

```xml
<cac:ActivityPeriod>
  <cbc:StartDate>2010-04-09</cbc:StartDate>
</cac:ActivityPeriod>
```

```xml
<cac:AdoptionPeriod>
  <cbc:DurationMeasure>90</cbc:DurationMeasure>
</cac:AdoptionPeriod>
```

```xml
<cac:EffectivePeriod>
  <cbc:StartDate>2005-02-26</cbc:StartDate>
  <cbc:EndDate>2005-12-26</cbc:EndDate>
</cac:EffectivePeriod>
```

```xml
<cac:EffectivePeriod>
  <cbc:StartDate>2010-03-28</cbc:StartDate>
  <cbc:EndDate>2010-05-29</cbc:EndDate>
</cac:EffectivePeriod>
```

```xml
<cac:EffectivePeriod>
  <cbc:StartDate>2010-03-28</cbc:StartDate>
  <cbc:EndDate>2010-08-29</cbc:EndDate>
</cac:EffectivePeriod>
```

```xml
<cac:EffectivePeriod>
  <cbc:StartDate>2010-04-28</cbc:StartDate>
  <cbc:EndDate>2010-06-29</cbc:EndDate>
</cac:EffectivePeriod>
```

```xml
<cac:EstimatedDeliveryPeriod>
  <cbc:StartDate>2005-06-30</cbc:StartDate>
  <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
</cac:EstimatedDeliveryPeriod>
```

```xml
<cac:EstimatedDeliveryPeriod>
  <cbc:StartDate>2010-04-30</cbc:StartDate>
  <cbc:StartTime>20:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2010-04-30</cbc:EndDate>
  <cbc:EndTime>20:30:00.0Z</cbc:EndTime>
</cac:EstimatedDeliveryPeriod>
```

```xml
<cac:EstimatedDeliveryPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>21:00:00.0Z</cbc:EndTime>
</cac:EstimatedDeliveryPeriod>
```

```xml
<cac:ExceptionObservationPeriod>
  <cbc:StartDate>2010-03-26</cbc:StartDate>
  <cbc:EndDate>2010-04-10</cbc:EndDate>
</cac:ExceptionObservationPeriod>
```

```xml
<cac:ExceptionObservationPeriod>
  <cbc:StartDate>2010-03-26</cbc:StartDate>
  <cbc:EndDate>2010-04-26</cbc:EndDate>
</cac:ExceptionObservationPeriod>
```

```xml
<cac:ForecastPeriod>
  <cbc:StartDate>2005-02-26</cbc:StartDate>
  <cbc:EndDate>2005-12-26</cbc:EndDate>
</cac:ForecastPeriod>
```

```xml
<cac:ForecastPeriod>
  <cbc:StartDate>2010-02-01</cbc:StartDate>
  <cbc:EndDate>2010-05-26</cbc:EndDate>
</cac:ForecastPeriod>
```

```xml
<cac:InventoryPeriod>
  <cbc:StartDate>2010-04-11</cbc:StartDate>
  <cbc:StartTime>08:00:00</cbc:StartTime>
  <cbc:EndDate>2011-04-11</cbc:EndDate>
</cac:InventoryPeriod>
```

```xml
<cac:InventoryPeriod>
  <cbc:StartDate>2010-04-11</cbc:StartDate>
  <cbc:StartTime>08:00:00Z</cbc:StartTime>
  <cbc:EndDate>2011-04-11</cbc:EndDate>
</cac:InventoryPeriod>
```

```xml
<cac:InventoryPeriod>
  <cbc:StartDate>2010-04-11</cbc:StartDate>
  <cbc:StartTime>14:00:00</cbc:StartTime>
  <cbc:EndDate>2010-04-11</cbc:EndDate>
</cac:InventoryPeriod>
```

```xml
<cac:InventoryPeriod>
  <cbc:StartDate>2010-04-11</cbc:StartDate>
  <cbc:StartTime>14:00:00Z</cbc:StartTime>
  <cbc:EndDate>2010-04-11</cbc:EndDate>
</cac:InventoryPeriod>
```

```xml
<cac:InvoicePeriod>
  <cbc:StartDate>2005-06-01</cbc:StartDate>
  <cbc:EndDate>2005-07-01</cbc:EndDate>
</cac:InvoicePeriod>
```

```xml
<cac:InvoicePeriod>
  <cbc:StartDate>2009-11-01</cbc:StartDate>
  <cbc:EndDate>2009-11-30</cbc:EndDate>
</cac:InvoicePeriod>
```

```xml
<cac:InvoicePeriod>
  <cbc:StartDate>2011-08-01</cbc:StartDate>
  <cbc:EndDate>2011-08-31</cbc:EndDate>
</cac:InvoicePeriod>
```

```xml
<cac:Period>
  <cbc:StartDate>2005-02-26</cbc:StartDate>
  <cbc:EndDate>2005-12-26</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2009-01-01</cbc:StartDate>
  <cbc:EndDate>2009-07-31</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2009-01-01</cbc:StartDate>
  <cbc:EndDate>2009-12-31</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2009-08-01</cbc:StartDate>
  <cbc:EndDate>2009-12-31</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2010-04-01</cbc:StartDate>
  <cbc:EndDate>2010-06-12</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2010-05-12</cbc:StartDate>
  <cbc:EndDate>2010-06-12</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-09-20</cbc:StartDate>
  <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-09-20</cbc:EndDate>
  <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-01</cbc:StartDate>
  <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-01</cbc:EndDate>
  <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-03</cbc:StartDate>
  <cbc:EndDate>2011-10-03</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-03</cbc:StartDate>
  <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-03</cbc:EndDate>
  <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-03</cbc:StartDate>
  <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-03</cbc:EndDate>
  <cbc:EndTime>18:35:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-03</cbc:StartDate>
  <cbc:StartTime>18:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-03</cbc:EndDate>
  <cbc:EndTime>21:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-04</cbc:StartDate>
  <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-04</cbc:EndDate>
  <cbc:EndTime>09:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-04</cbc:StartDate>
  <cbc:StartTime>15:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-04</cbc:EndDate>
  <cbc:EndTime>18:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-06</cbc:StartDate>
  <cbc:EndDate>2011-10-06</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-06</cbc:StartDate>
  <cbc:StartTime>09:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-06</cbc:EndDate>
  <cbc:EndTime>12:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2011-10-06</cbc:StartDate>
  <cbc:StartTime>12:30:10+01:00</cbc:StartTime>
  <cbc:EndDate>2011-10-06</cbc:EndDate>
  <cbc:EndTime>15:30:10+01:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2016-08-02</cbc:StartDate>
  <cbc:StartTime>07:00:00</cbc:StartTime>
  <cbc:EndDate>2016-08-02</cbc:EndDate>
  <cbc:EndTime>15:30:00</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2016-08-02</cbc:StartDate>
  <cbc:StartTime>07:00:00Z</cbc:StartTime>
  <cbc:EndDate>2016-08-02</cbc:EndDate>
  <cbc:EndTime>15:30:00Z</cbc:EndTime>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2017-03-30</cbc:StartDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2020-06-02</cbc:StartDate>
  <cbc:EndDate>2020-06-02</cbc:EndDate>
</cac:Period>
```

```xml
<cac:Period>
  <cbc:StartDate>2020-07-01</cbc:StartDate>
  <cbc:EndDate>2020-07-01</cbc:EndDate>
</cac:Period>
```

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2005-06-20</cbc:StartDate>
  <cbc:StartTime>10:30:47.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-21</cbc:EndDate>
  <cbc:EndTime>10:30:47.0Z</cbc:EndTime>
</cac:RequestedDeliveryPeriod>
```

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2005-06-29</cbc:StartDate>
  <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-30</cbc:EndDate>
  <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
</cac:RequestedDeliveryPeriod>
```

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2005-06-29</cbc:StartDate>
  <cbc:StartTime>09:30:47.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-29</cbc:EndDate>
  <cbc:EndTime>09:30:47.0Z</cbc:EndTime>
</cac:RequestedDeliveryPeriod>
```

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2008-05-06</cbc:StartDate>
  <cbc:StartTime>09:30:47.0Z</cbc:StartTime>
  <cbc:EndDate>2008-05-10</cbc:EndDate>
  <cbc:EndTime>09:30:47.0Z</cbc:EndTime>
</cac:RequestedDeliveryPeriod>
```

```xml
<cac:RequestedDeliveryPeriod>
  <cbc:StartDate>2010-02-10</cbc:StartDate>
  <cbc:EndDate>2010-02-25</cbc:EndDate>
</cac:RequestedDeliveryPeriod>
```

```xml
<cac:ServiceAvailabilityPeriod>
  <cbc:StartTime>09:00:00</cbc:StartTime>
  <cbc:EndTime>16:00:00</cbc:EndTime>
</cac:ServiceAvailabilityPeriod>
```

```xml
<cac:ServiceAvailabilityPeriod>
  <cbc:StartTime>09:00:00Z</cbc:StartTime>
  <cbc:EndTime>16:00:00Z</cbc:EndTime>
</cac:ServiceAvailabilityPeriod>
```

```xml
<cac:ServiceEndTimePeriod>
  <cbc:EndDate>2011-10-06</cbc:EndDate>
  <cbc:EndTime>16:00:10+01:00</cbc:EndTime>
</cac:ServiceEndTimePeriod>
```

```xml
<cac:ServiceEndTimePeriod>
  <cbc:StartDate>2010-05-01</cbc:StartDate>
  <cbc:StartTime>15:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2010-05-01</cbc:EndDate>
  <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
</cac:ServiceEndTimePeriod>
```

```xml
<cac:ServiceEndTimePeriod>
  <cbc:StartDate>2011-03-17</cbc:StartDate>
  <cbc:StartTime>15:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-17</cbc:EndDate>
  <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
</cac:ServiceEndTimePeriod>
```

```xml
<cac:ServiceMaintenancePeriod>
  <cbc:StartTime>22:00:00</cbc:StartTime>
  <cbc:EndTime>06:00:00</cbc:EndTime>
</cac:ServiceMaintenancePeriod>
```

```xml
<cac:ServiceMaintenancePeriod>
  <cbc:StartTime>22:00:00Z</cbc:StartTime>
  <cbc:EndTime>06:00:00Z</cbc:EndTime>
</cac:ServiceMaintenancePeriod>
```

```xml
<cac:ServiceStartTimePeriod>
  <cbc:StartDate>2010-05-01</cbc:StartDate>
  <cbc:StartTime>10:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2010-05-01</cbc:EndDate>
  <cbc:EndTime>11:00:00.0Z</cbc:EndTime>
</cac:ServiceStartTimePeriod>
```

```xml
<cac:ServiceStartTimePeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:ServiceStartTimePeriod>
```

```xml
<cac:SettlementPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>14:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-04-12</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:SettlementPeriod>
```

```xml
<cac:StatementPeriod>
  <cbc:StartDate>2005-07-01</cbc:StartDate>
  <cbc:EndDate>2005-07-31</cbc:EndDate>
  <cbc:Description>July</cbc:Description>
</cac:StatementPeriod>
```

```xml
<cac:TransitPeriod>
  <cbc:StartDate>2005-06-25</cbc:StartDate>
  <cbc:StartTime>11:35:00.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-25</cbc:EndDate>
  <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
</cac:TransitPeriod>
```

```xml
<cac:TransitPeriod>
  <cbc:StartDate>2005-06-25</cbc:StartDate>
  <cbc:StartTime>23:20:00.0Z</cbc:StartTime>
</cac:TransitPeriod>
```

```xml
<cac:TransportServiceProviderResponseDeadlinePeriod>
  <cbc:EndDate>2011-09-13</cbc:EndDate>
  <cbc:EndTime>11:00:10+01:00</cbc:EndTime>
</cac:TransportServiceProviderResponseDeadlinePeriod>
```

```xml
<cac:TransportUserResponseRequiredPeriod>
  <cbc:EndDate>2011-09-13</cbc:EndDate>
  <cbc:EndTime>12:00:10+01:00</cbc:EndTime>
</cac:TransportUserResponseRequiredPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:EndDate>1967-08-13</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:EndDate>2010-01-31</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2005-06-20</cbc:StartDate>
  <cbc:EndDate>2005-07-20</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2005-06-25</cbc:StartDate>
  <cbc:StartTime>01:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2005-06-30</cbc:EndDate>
  <cbc:EndTime>18:00:00.0Z</cbc:EndTime>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2008-05-01</cbc:StartDate>
  <cbc:EndDate>2008-05-06</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2010-01-01</cbc:StartDate>
  <cbc:EndDate>2011-01-01</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2010-01-01</cbc:StartDate>
  <cbc:EndDate>2012-01-01</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2010-03-28</cbc:StartDate>
  <cbc:EndDate>2010-08-29</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2010-05-01</cbc:StartDate>
  <cbc:EndDate>2010-05-01</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:EndDate>2011-03-17</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2011-09-12</cbc:StartDate>
  <cbc:EndDate>2011-09-30</cbc:EndDate>
  <cbc:EndTime>16:00:00+01:00</cbc:EndTime>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2019-02-21</cbc:StartDate>
  <cbc:EndDate>2020-02-20</cbc:EndDate>
</cac:ValidityPeriod>
```

```xml
<cac:ValidityPeriod>
  <cbc:StartDate>2019-03-18</cbc:StartDate>
  <cbc:EndDate>2019-03-18</cbc:EndDate>
</cac:ValidityPeriod>
```

### `PersonType`

**Used as:** `cac:Person`

_12 unique instances across 1 element_

```xml
<cac:Person>
  <cbc:FirstName>Antonio</cbc:FirstName>
  <cbc:FamilyName>M</cbc:FamilyName>
  <cbc:MiddleName>Salemacher</cbc:MiddleName>
  <cbc:JobTitle>Sales manager</cbc:JobTitle>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>Antonio</cbc:FirstName>
  <cbc:FamilyName>Salemacher</cbc:FamilyName>
  <cbc:MiddleName>M</cbc:MiddleName>
  <cbc:JobTitle>Sales manager</cbc:JobTitle>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>DAVID</cbc:FirstName>
  <cbc:FamilyName>VILLA</cbc:FamilyName>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>GIORGIO</cbc:FirstName>
  <cbc:FamilyName>VERDI</cbc:FamilyName>
  <cbc:RoleCode>BN</cbc:RoleCode>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>John</cbc:FirstName>
  <cbc:FamilyName>Doe</cbc:FamilyName>
  <cbc:MiddleName>X</cbc:MiddleName>
  <cbc:JobTitle>Purchasing manager</cbc:JobTitle>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>John</cbc:FirstName>
  <cbc:FamilyName>X</cbc:FamilyName>
  <cbc:MiddleName>Doe</cbc:MiddleName>
  <cbc:JobTitle>Purchasing manager</cbc:JobTitle>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>Kirsten</cbc:FirstName>
  <cbc:FamilyName>Jensen</cbc:FamilyName>
  <cac:IdentityDocumentReference>
    <cbc:ID>325334535</cbc:ID>
  </cac:IdentityDocumentReference>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>Lars</cbc:FirstName>
  <cbc:FamilyName>Petersen</cbc:FamilyName>
  <cbc:MiddleName>M</cbc:MiddleName>
  <cbc:JobTitle>Sales manager</cbc:JobTitle>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>Pelle</cbc:FirstName>
  <cbc:FamilyName>Svensson</cbc:FamilyName>
  <cbc:MiddleName>X</cbc:MiddleName>
  <cbc:JobTitle>Boss</cbc:JobTitle>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>RAUL</cbc:FirstName>
  <cbc:FamilyName>GONZALES</cbc:FamilyName>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>STEFANO</cbc:FirstName>
  <cbc:FamilyName>ROSSI</cbc:FamilyName>
  <cbc:RoleCode>RP</cbc:RoleCode>
</cac:Person>
```

```xml
<cac:Person>
  <cbc:FirstName>Sven</cbc:FirstName>
  <cbc:FamilyName>Pereson</cbc:FamilyName>
  <cbc:MiddleName>N</cbc:MiddleName>
  <cbc:JobTitle>Stuffuser</cbc:JobTitle>
</cac:Person>
```

### `PickupType`

**Used as:** `cac:Pickup`

_3 unique instances across 1 element_

```xml
<cac:Pickup>
  <cac:PickupLocation>
    <cbc:ID>01530</cbc:ID>
    <cbc:LocationTypeCode>P</cbc:LocationTypeCode>
  </cac:PickupLocation>
</cac:Pickup>
```

```xml
<cac:Pickup>
  <cac:PickupLocation>
    <cbc:ID>FI1234567-8R0001</cbc:ID>
    <cbc:LocationTypeCode>L</cbc:LocationTypeCode>
  </cac:PickupLocation>
</cac:Pickup>
```

```xml
<cac:Pickup>
  <cbc:LatestPickupDate>2016-08-02</cbc:LatestPickupDate>
</cac:Pickup>
```

### `PriceType`

**Used as:** `cac:Price`

_17 unique instances across 1 element_

```xml
<cac:Price>
  <cbc:PriceAmount>0.75</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>1.00</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>10.00</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>100.00</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>12.00</cbc:PriceAmount>
  <cbc:TaxInclusivePriceAmount>15.00</cbc:TaxInclusivePriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>120.00</cbc:PriceAmount>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>1250.00</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

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

```xml
<cac:Price>
  <cbc:PriceAmount>15</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>16.00</cbc:PriceAmount>
  <cbc:TaxInclusivePriceAmount>20.00</cbc:TaxInclusivePriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
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
```

```xml
<cac:Price>
  <cbc:PriceAmount>25</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>3.96</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>40.00</cbc:PriceAmount>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>4300.00</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>50.00</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

```xml
<cac:Price>
  <cbc:PriceAmount>50</cbc:PriceAmount>
  <cbc:BaseQuantity>1</cbc:BaseQuantity>
</cac:Price>
```

### `ProcurementProjectLotReferenceType`

**Used as:** `cac:ProcurementProjectLotReference`

_1 unique instance across 1 element_

```xml
<cac:ProcurementProjectLotReference>
  <cbc:ID>Lot2</cbc:ID>
</cac:ProcurementProjectLotReference>
```

### `ProcurementProjectType`

**Used as:** `cac:ProcurementProject`

_1 unique instance across 1 element_

```xml
<cac:ProcurementProject>
  <cbc:ID>DP</cbc:ID>
  <cbc:Name>DigitalPost</cbc:Name>
  <cbc:Description>Only Lot2</cbc:Description>
</cac:ProcurementProject>
```

### `PromotionalEventLineItemType`

**Used as:** `cac:PromotionalEventLineItem`

_1 unique instance across 1 element_

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

### `PromotionalEventType`

**Used as:** `cac:PromotionalEvent`

_1 unique instance across 1 element_

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

### `PromotionalSpecificationType`

**Used as:** `cac:PromotionalSpecification`

_1 unique instance across 1 element_

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

### `PurchaseReceiptLineType`

**Used as:** `cac:PurchaseReceiptLine`

_2 unique instances across 1 element_

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

### `PurchaseReferenceType`

**Used as:** `cac:PurchaseReference`

_1 unique instance across 1 element_

```xml
<cac:PurchaseReference>
  <cbc:ID>321987</cbc:ID>
  <cbc:Description>Customer Loyalty Number</cbc:Description>
</cac:PurchaseReference>
```

### `QuotationLineType`

**Used as:** `cac:QuotationLine`

_5 unique instances across 1 element_

```xml
<cac:QuotationLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Computer</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL1052665</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cbc:LineExtensionAmount>150500.00</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>37625.00</cbc:TotalTaxAmount>
    <cac:Price>
      <cbc:PriceAmount>4300.00</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Stationær computer</cbc:Description>
      <cbc:Name>Dell PrecisionTM  T3400</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:QuotationLine>
```

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

```xml
<cac:QuotationLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Note>Skærm</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL2363463</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cbc:LineExtensionAmount>43750.00</cbc:LineExtensionAmount>
    <cbc:TotalTaxAmount>10937.50</cbc:TotalTaxAmount>
    <cac:Price>
      <cbc:PriceAmount>1250.00</cbc:PriceAmount>
      <cbc:BaseQuantity>1</cbc:BaseQuantity>
    </cac:Price>
    <cac:Item>
      <cbc:Description>Fladskærm</cbc:Description>
      <cbc:Name>FP/BL 1908WFP</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:QuotationLine>
```

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

```xml
<cac:QuotationLine>
  <cbc:ID>4</cbc:ID>
  <cbc:Note>Tastatur</cbc:Note>
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
</cac:QuotationLine>
```

### `RailTransportType`

**Used as:** `cac:RailTransport`

_3 unique instances across 1 element_

```xml
<cac:RailTransport>
  <cbc:TrainID>101</cbc:TrainID>
  <cbc:RailCarID>101-21</cbc:RailCarID>
</cac:RailTransport>
```

```xml
<cac:RailTransport>
  <cbc:TrainID>RID01235</cbc:TrainID>
</cac:RailTransport>
```

```xml
<cac:RailTransport>
  <cbc:TrainID>VF80145</cbc:TrainID>
</cac:RailTransport>
```

### `ReceiptLineType`

**Used as:** `cac:ReceiptLine`

_2 unique instances across 1 element_

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

### `ReminderLineType`

**Used as:** `cac:ReminderLine`

_1 unique instance across 1 element_

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

### `RemittanceAdviceLineType`

**Used as:** `cac:RemittanceAdviceLine`

_1 unique instance across 1 element_

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

### `RequestForQuotationLineType`

**Used as:** `cac:RequestForQuotationLine`

_5 unique instances across 1 element_

```xml
<cac:RequestForQuotationLine>
  <cbc:ID>1</cbc:ID>
  <cbc:Note>Computer</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL1052665</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Stationær computer</cbc:Description>
      <cbc:Name>Dell PrecisionTM  T3400</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:RequestForQuotationLine>
```

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

```xml
<cac:RequestForQuotationLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Note>Skærm</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL2363463</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Fladskærm</cbc:Description>
      <cbc:Name>FP/BL 1908WFP</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:RequestForQuotationLine>
```

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

```xml
<cac:RequestForQuotationLine>
  <cbc:ID>4</cbc:ID>
  <cbc:Note>Tastatur</cbc:Note>
  <cac:LineItem>
    <cbc:ID>DELL8436783</cbc:ID>
    <cbc:Quantity>35</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Tastatur</cbc:Description>
      <cbc:Name>Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)</cbc:Name>
    </cac:Item>
  </cac:LineItem>
</cac:RequestForQuotationLine>
```

### `ResponseType`

**Used as:** `cac:DiscrepancyResponse`

_1 unique instance across 1 element_

```xml
<cac:DiscrepancyResponse>
  <cbc:ReferenceID>A00095678</cbc:ReferenceID>
  <cbc:Description>invoice cancelation</cbc:Description>
</cac:DiscrepancyResponse>
```

### `RetailPlannedImpactType`

**Used as:** `cac:RetailPlannedImpact`

_1 unique instance across 1 element_

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

### `RoadTransportType`

**Used as:** `cac:RoadTransport`

_5 unique instances across 1 element_

```xml
<cac:RoadTransport>
  <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
</cac:RoadTransport>
```

```xml
<cac:RoadTransport>
  <cbc:LicensePlateID>KA04401</cbc:LicensePlateID>
</cac:RoadTransport>
```

```xml
<cac:RoadTransport>
  <cbc:LicensePlateID>PBB-123</cbc:LicensePlateID>
</cac:RoadTransport>
```

```xml
<cac:RoadTransport>
  <cbc:LicensePlateID>VE80044</cbc:LicensePlateID>
</cac:RoadTransport>
```

```xml
<cac:RoadTransport>
  <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
</cac:RoadTransport>
```

### `SalesItemType`

**Used as:** `cac:SalesItem`

_8 unique instances across 1 element_

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

### `ServiceLevelAgreementType`

**Used as:** `cac:ServiceLevelAgreement`

_4 unique instances across 1 element_

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
    <cbc:StartTime>09:00:00</cbc:StartTime>
    <cbc:EndTime>16:00:00</cbc:EndTime>
  </cac:ServiceAvailabilityPeriod>
  <cac:ServiceMaintenancePeriod>
    <cbc:StartTime>22:00:00</cbc:StartTime>
    <cbc:EndTime>06:00:00</cbc:EndTime>
  </cac:ServiceMaintenancePeriod>
</cac:ServiceLevelAgreement>
```

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

```xml
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
```

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

### `ShipmentStageType`

**Used as:** `cac:MainCarriageShipmentStage` · `cac:PreCarriageShipmentStage` · `cac:ShipmentStage`

_17 unique instances across 3 elements_

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

```xml
<cac:MainCarriageShipmentStage>
  <cbc:TransportModeCode>3</cbc:TransportModeCode>
</cac:MainCarriageShipmentStage>
```

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

```xml
<cac:ShipmentStage>
  <cbc:TransportModeCode>4</cbc:TransportModeCode>
  <cac:TransportMeans>
    <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
  </cac:TransportMeans>
</cac:ShipmentStage>
```

### `ShipmentType`

**Used as:** `cac:ConsolidatedShipment` · `cac:Shipment`

_20 unique instances across 2 elements_

```xml
<cac:ConsolidatedShipment>
  <cbc:ID>GSIN_1</cbc:ID>
</cac:ConsolidatedShipment>
```

```xml
<cac:ConsolidatedShipment>
  <cbc:ID>GSIN_2</cbc:ID>
</cac:ConsolidatedShipment>
```

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
</cac:Shipment>
```

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
      <cbc:ActualDespatchTime>16:00:00</cbc:ActualDespatchTime>
      <cac:DespatchAddress>
        <cac:Country>
          <cbc:IdentificationCode>RU</cbc:IdentificationCode>
        </cac:Country>
      </cac:DespatchAddress>
    </cac:Despatch>
  </cac:Delivery>
</cac:Shipment>
```

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
        <cbc:StartTime>07:00:00Z</cbc:StartTime>
        <cbc:EndDate>2016-08-02</cbc:EndDate>
        <cbc:EndTime>15:30:00Z</cbc:EndTime>
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

### `SignatureType`

**Used as:** `cac:Signature`

_4 unique instances across 1 element_

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

```xml
<cac:Signature>
  <cbc:ID>urn:oasis:names:specification:ubl:signature:Invoice</cbc:ID>
  <cbc:SignatureMethod>urn:oasis:names:specification:ubl:dsig:enveloped</cbc:SignatureMethod>
  <cac:SignatoryParty>
    <cac:PartyIdentification>
      <cbc:ID>MyParty</cbc:ID>
    </cac:PartyIdentification>
  </cac:SignatoryParty>
</cac:Signature>
```

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

### `SocialMediaProfileType`

**Used as:** `cac:SocialMediaProfile`

_5 unique instances across 1 element_

```xml
<cac:SocialMediaProfile>
  <cbc:ID>1</cbc:ID>
  <cbc:Name>LinkedIN</cbc:Name>
  <cbc:SocialMediaTypeCode>Business</cbc:SocialMediaTypeCode>
  <cbc:URI>https://www.linkedin.com/company/oasis</cbc:URI>
</cac:SocialMediaProfile>
```

```xml
<cac:SocialMediaProfile>
  <cbc:ID>2</cbc:ID>
  <cbc:Name>Twitter</cbc:Name>
  <cbc:URI>http://twitter.com/OASISopen</cbc:URI>
</cac:SocialMediaProfile>
```

```xml
<cac:SocialMediaProfile>
  <cbc:ID>3</cbc:ID>
  <cbc:Name>Facebook</cbc:Name>
  <cbc:URI>http://facebook.com/oasis.open</cbc:URI>
</cac:SocialMediaProfile>
```

```xml
<cac:SocialMediaProfile>
  <cbc:ID>4</cbc:ID>
  <cbc:Name>YouTube</cbc:Name>
  <cbc:URI>http://www.youtube.com/oasisopen</cbc:URI>
</cac:SocialMediaProfile>
```

```xml
<cac:SocialMediaProfile>
  <cbc:ID>5</cbc:ID>
  <cbc:Name>Google+</cbc:Name>
  <cbc:URI>https://plus.google.com/+Oasis-openOrg</cbc:URI>
</cac:SocialMediaProfile>
```

### `StatementLineType`

**Used as:** `cac:StatementLine`

_1 unique instance across 1 element_

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

### `StatusType`

**Used as:** `cac:CurrentStatus` · `cac:Status`

_2 unique instances across 2 elements_

```xml
<cac:CurrentStatus>
  <cbc:ConditionCode>31</cbc:ConditionCode>
  <cbc:Description>En route</cbc:Description>
</cac:CurrentStatus>
```

```xml
<cac:Status>
  <cbc:ConditionCode>4</cbc:ConditionCode>
  <cbc:StatusReasonCode>23</cbc:StatusReasonCode>
  <cbc:StatusReason>Reefer container lost power - cargo of fish destroyed</cbc:StatusReason>
</cac:Status>
```

### `StockAvailabilityReportLineType`

**Used as:** `cac:StockAvailabilityReportLine`

_3 unique instances across 1 element_

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

```xml
<cac:StockAvailabilityReportLine>
  <cbc:ID>2</cbc:ID>
  <cbc:Quantity>80</cbc:Quantity>
  <cbc:AvailabilityDate>2010-04-11</cbc:AvailabilityDate>
  <cbc:AvailabilityStatusCode>2</cbc:AvailabilityStatusCode>
  <cac:Item>
    <cbc:Description>jersey</cbc:Description>
    <cac:BuyersItemIdentification>
      <cbc:ID>TJ043</cbc:ID>
    </cac:BuyersItemIdentification>
    <cac:SellersItemIdentification>
      <cbc:ID>K0058</cbc:ID>
    </cac:SellersItemIdentification>
  </cac:Item>
</cac:StockAvailabilityReportLine>
```

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

### `SupplierPartyType`

**Used as:** `cac:AccountingSupplierParty` · `cac:DespatchSupplierParty` · `cac:SellerSupplierParty`

_19 unique instances across 3 elements_

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

```xml
<cac:AccountingSupplierParty>
  <cac:Party>
    <cac:PartyName>
      <cbc:Name>Custom Cotter Pins</cbc:Name>
    </cac:PartyName>
  </cac:Party>
</cac:AccountingSupplierParty>
```

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
      <cbc:FamilyName>Salemacher</cbc:FamilyName>
      <cbc:MiddleName>M</cbc:MiddleName>
      <cbc:JobTitle>Sales manager</cbc:JobTitle>
    </cac:Person>
  </cac:Party>
</cac:AccountingSupplierParty>
```

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
  </cac:Party>
</cac:AccountingSupplierParty>
```

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
  </cac:Party>
</cac:DespatchSupplierParty>
```

```xml
<cac:SellerSupplierParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>0012345000058</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:SellerSupplierParty>
```

```xml
<cac:SellerSupplierParty>
  <cac:Party>
    <cac:PartyIdentification>
      <cbc:ID>6903148000007</cbc:ID>
    </cac:PartyIdentification>
  </cac:Party>
</cac:SellerSupplierParty>
```

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
  </cac:Party>
</cac:SellerSupplierParty>
```

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
      <cbc:CompanyID>DK18296799</cbc:CompanyID>
    </cac:PartyLegalEntity>
  </cac:Party>
</cac:SellerSupplierParty>
```

### `TaxCategoryType`

**Used as:** `cac:ClassifiedTaxCategory` · `cac:TaxCategory`

_12 unique instances across 2 elements_

```xml
<cac:ClassifiedTaxCategory>
  <cbc:ID>AA</cbc:ID>
  <cbc:Percent>10</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:ClassifiedTaxCategory>
```

```xml
<cac:ClassifiedTaxCategory>
  <cbc:ID>E</cbc:ID>
  <cbc:Percent>0</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:ClassifiedTaxCategory>
```

```xml
<cac:ClassifiedTaxCategory>
  <cbc:ID>S</cbc:ID>
  <cbc:Percent>20</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:ClassifiedTaxCategory>
```

```xml
<cac:TaxCategory>
  <cbc:ID>A</cbc:ID>
  <cac:TaxScheme>
    <cbc:ID>UK VAT</cbc:ID>
    <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
  </cac:TaxScheme>
</cac:TaxCategory>
```

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

```xml
<cac:TaxCategory>
  <cbc:ID>AA</cbc:ID>
  <cbc:Percent>10</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

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

```xml
<cac:TaxCategory>
  <cbc:ID>O</cbc:ID>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

```xml
<cac:TaxCategory>
  <cbc:ID>S</cbc:ID>
  <cbc:Percent>20</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

```xml
<cac:TaxCategory>
  <cbc:ID>S</cbc:ID>
  <cbc:Percent>21.00</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

```xml
<cac:TaxCategory>
  <cbc:ID>S</cbc:ID>
  <cbc:Percent>25</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

```xml
<cac:TaxCategory>
  <cbc:Percent>21.00</cbc:Percent>
  <cac:TaxScheme>
    <cbc:ID>VAT</cbc:ID>
  </cac:TaxScheme>
</cac:TaxCategory>
```

### `TaxSchemeType`

**Used as:** `cac:TaxScheme`

_4 unique instances across 1 element_

```xml
<cac:TaxScheme>
  <cbc:ID>63</cbc:ID>
  <cbc:Name>Moms</cbc:Name>
</cac:TaxScheme>
```

```xml
<cac:TaxScheme>
  <cbc:ID>UK VAT</cbc:ID>
  <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
</cac:TaxScheme>
```

```xml
<cac:TaxScheme>
  <cbc:ID>VAT</cbc:ID>
  <cbc:TaxTypeCode>VAT</cbc:TaxTypeCode>
</cac:TaxScheme>
```

```xml
<cac:TaxScheme>
  <cbc:ID>VAT</cbc:ID>
</cac:TaxScheme>
```

### `TaxSubtotalType`

**Used as:** `cac:TaxSubtotal`

_10 unique instances across 1 element_

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

```xml
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
```

```xml
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
```

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

```xml
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
```

### `TaxTotalType`

**Used as:** `cac:TaxTotal`

_17 unique instances across 1 element_

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>-0.396</cbc:TaxAmount>
</cac:TaxTotal>
```

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>0.496</cbc:TaxAmount>
</cac:TaxTotal>
```

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>0</cbc:TaxAmount>
</cac:TaxTotal>
```

```xml
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
```

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>100</cbc:TaxAmount>
</cac:TaxTotal>
```

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cbc:TaxEvidenceIndicator>false</cbc:TaxEvidenceIndicator>
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

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>17.50</cbc:TaxAmount>
  <cbc:TaxEvidenceIndicator>false</cbc:TaxEvidenceIndicator>
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

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>254.6</cbc:TaxAmount>
</cac:TaxTotal>
```

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

```xml
<cac:TaxTotal>
  <cbc:TaxAmount>37.5</cbc:TaxAmount>
</cac:TaxTotal>
```

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

### `TemperatureType`

**Used as:** `cac:MaximumTemperature`

_1 unique instance across 1 element_

```xml
<cac:MaximumTemperature>
  <cbc:AttributeID>TC</cbc:AttributeID>
  <cbc:Measure>3.00</cbc:Measure>
  <cbc:Description>Chilled</cbc:Description>
</cac:MaximumTemperature>
```

### `TenderPreparationType`

**Used as:** `cac:TenderPreparation`

_2 unique instances across 1 element_

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

### `TenderingTermsType`

**Used as:** `cac:TenderingTerms`

_2 unique instances across 1 element_

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

### `TransactionConditionsType`

**Used as:** `cac:TransactionConditions`

_2 unique instances across 1 element_

```xml
<cac:TransactionConditions>
  <cbc:Description>Please advise when transport is booked.</cbc:Description>
</cac:TransactionConditions>
```

```xml
<cac:TransactionConditions>
  <cbc:Description>order response required; payment is by BACS or by cheque</cbc:Description>
</cac:TransactionConditions>
```

### `TransportEquipmentSealType`

**Used as:** `cac:TransportEquipmentSeal`

_3 unique instances across 1 element_

```xml
<cac:TransportEquipmentSeal>
  <cbc:ID>1_1</cbc:ID>
  <cbc:Condition>IN_RIGHT_CONDITION</cbc:Condition>
</cac:TransportEquipmentSeal>
```

```xml
<cac:TransportEquipmentSeal>
  <cbc:ID>2_1</cbc:ID>
  <cbc:Condition>IN_RIGHT_CONDITION</cbc:Condition>
</cac:TransportEquipmentSeal>
```

```xml
<cac:TransportEquipmentSeal>
  <cbc:ID>7654321</cbc:ID>
</cac:TransportEquipmentSeal>
```

### `TransportEquipmentType`

**Used as:** `cac:ContainedInTransportEquipment` · `cac:ReferencedTransportEquipment` · `cac:SupportedTransportEquipment` · `cac:TransportEquipment`

_30 unique instances across 4 elements_

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>EXT_TE_1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914111</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>EXT_TE_2</cbc:ID>
  <cbc:TransportEquipmentTypeCode>TE</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914112</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>NEC_TE_1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914542</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>NEC_TE_2</cbc:ID>
  <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914543</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>NTT_TE_1</cbc:ID>
  <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914564</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

```xml
<cac:ContainedInTransportEquipment>
  <cbc:ID>NTT_TE_2</cbc:ID>
  <cbc:TransportEquipmentTypeCode>RR</cbc:TransportEquipmentTypeCode>
  <cbc:TraceID>12345678914565</cbc:TraceID>
</cac:ContainedInTransportEquipment>
```

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

```xml
<cac:ReferencedTransportEquipment>
  <cbc:ID>2</cbc:ID>
  <cac:TransportEquipmentSeal>
    <cbc:ID>2_1</cbc:ID>
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

```xml
<cac:ReferencedTransportEquipment>
  <cbc:ID>GRAI 12345698-1</cbc:ID>
</cac:ReferencedTransportEquipment>
```

```xml
<cac:ReferencedTransportEquipment>
  <cbc:ID>GRAI 12345698-2</cbc:ID>
</cac:ReferencedTransportEquipment>
```

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

```xml
<cac:TransportEquipment>
  <cac:TransportEquipmentSeal>
    <cbc:ID>7654321</cbc:ID>
  </cac:TransportEquipmentSeal>
</cac:TransportEquipment>
```

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

```xml
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
```

```xml
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
```

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

```xml
<cac:TransportEquipment>
  <cbc:ID>CON_TE_1</cbc:ID>
</cac:TransportEquipment>
```

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

```xml
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
```

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

```xml
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
```

```xml
<cac:TransportEquipment>
  <cbc:TransportEquipmentTypeCode>AD</cbc:TransportEquipmentTypeCode>
  <cbc:FullnessIndicationCode>FTL</cbc:FullnessIndicationCode>
</cac:TransportEquipment>
```

### `TransportEventType`

**Used as:** `cac:EstimatedArrivalTransportEvent` · `cac:PlannedArrivalTransportEvent` · `cac:PlannedDeliveryTransportEvent` · `cac:PlannedDepartureTransportEvent` · `cac:PlannedPickupTransportEvent` · `cac:RequestedArrivalTransportEvent` · `cac:RequestedDeliveryTransportEvent` · `cac:RequestedDepartureTransportEvent` · `cac:RequestedPickupTransportEvent` · `cac:TransportEvent`

_26 unique instances across 10 elements_

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
    <cbc:StartTime>07:00:00</cbc:StartTime>
    <cbc:EndDate>2016-08-02</cbc:EndDate>
    <cbc:EndTime>15:30:00</cbc:EndTime>
  </cac:Period>
</cac:RequestedPickupTransportEvent>
```

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

### `TransportExecutionTermsType`

**Used as:** `cac:TransportExecutionTerms`

_3 unique instances across 1 element_

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

```xml
<cac:TransportExecutionTerms>
  <cac:PaymentTerms>
    <cbc:Note>PER THIRTY DAYS</cbc:Note>
  </cac:PaymentTerms>
</cac:TransportExecutionTerms>
```

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

### `TransportHandlingUnitType`

**Used as:** `cac:TransportHandlingUnit`

_21 unique instances across 1 element_

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

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>ABCD123456-7</cbc:ID>
</cac:TransportHandlingUnit>
```

```xml
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
```

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

```xml
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
```

```xml
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
```

```xml
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
```

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

```xml
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
```

```xml
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
```

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

```xml
<cac:TransportHandlingUnit>
  <cbc:ID>TI_101</cbc:ID>
</cac:TransportHandlingUnit>
```

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

### `TransportMeansType`

**Used as:** `cac:TransportMeans`

_13 unique instances across 1 element_

```xml
<cac:TransportMeans>
  <cac:RailTransport>
    <cbc:TrainID>VF80145</cbc:TrainID>
  </cac:RailTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cac:RoadTransport>
    <cbc:LicensePlateID>2652 WE</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cac:RoadTransport>
    <cbc:LicensePlateID>WFN667</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:TransportMeans>
```

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

```xml
<cac:TransportMeans>
  <cbc:JourneyID>TM1</cbc:JourneyID>
  <cbc:RegistrationNationalityID>EE</cbc:RegistrationNationalityID>
  <cac:MaritimeTransport>
    <cbc:VesselID>Eestiship</cbc:VesselID>
  </cac:MaritimeTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cbc:JourneyID>UA 1234</cbc:JourneyID>
  <cac:AirTransport>
    <cbc:AircraftID>A-127763-747</cbc:AircraftID>
  </cac:AirTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
  <cac:AirTransport>
    <cbc:AircraftID>AY-428 20130623</cbc:AircraftID>
  </cac:AirTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
  <cac:RoadTransport>
    <cbc:LicensePlateID>PBB-123</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cbc:RegistrationNationalityID>FI</cbc:RegistrationNationalityID>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cbc:TransportMeansTypeCode>Train, with more than 20 wagons</cbc:TransportMeansTypeCode>
  <cac:RailTransport>
    <cbc:TrainID>101</cbc:TrainID>
    <cbc:RailCarID>101-21</cbc:RailCarID>
  </cac:RailTransport>
</cac:TransportMeans>
```

```xml
<cac:TransportMeans>
  <cbc:TransportMeansTypeCode>Truck</cbc:TransportMeansTypeCode>
</cac:TransportMeans>
```

### `TransportScheduleType`

**Used as:** `cac:TransportSchedule`

_2 unique instances across 1 element_

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

### `TransportationSegmentType`

**Used as:** `cac:TransportationSegment`

_7 unique instances across 1 element_

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

### `TransportationServiceType`

**Used as:** `cac:AdditionalTransportationService` · `cac:FinalDeliveryTransportationService` · `cac:MainTransportationService` · `cac:OriginalDespatchTransportationService` · `cac:TransportationService`

_14 unique instances across 5 elements_

```xml
<cac:AdditionalTransportationService>
  <cbc:TransportServiceCode>Insurance</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Insurance of goods during transportation</cbc:TransportationServiceDescription>
</cac:AdditionalTransportationService>
```

```xml
<cac:AdditionalTransportationService>
  <cbc:TransportServiceCode>Status notification</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>En route status notifications</cbc:TransportationServiceDescription>
</cac:AdditionalTransportationService>
```

```xml
<cac:FinalDeliveryTransportationService>
  <cbc:TransportServiceCode>Pier to Pier</cbc:TransportServiceCode>
</cac:FinalDeliveryTransportationService>
```

```xml
<cac:MainTransportationService>
  <cbc:TransportServiceCode>12</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>CARRIER SERVICE</cbc:TransportationServiceDescription>
</cac:MainTransportationService>
```

```xml
<cac:MainTransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Transport from Hamburg to Nurnberg</cbc:TransportationServiceDescription>
</cac:MainTransportationService>
```

```xml
<cac:MainTransportationService>
  <cbc:TransportServiceCode>Transport</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Complete D2D service from Munich, Germany to Hamar, Norway</cbc:TransportationServiceDescription>
</cac:MainTransportationService>
```

```xml
<cac:MainTransportationService>
  <cbc:TransportServiceCode>Transport</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Package and pallet transport within the Bavaria area</cbc:TransportationServiceDescription>
</cac:MainTransportationService>
```

```xml
<cac:OriginalDespatchTransportationService>
  <cbc:TransportServiceCode>Door to Pier</cbc:TransportServiceCode>
</cac:OriginalDespatchTransportationService>
```

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

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Rail transport service from Bremen to Nurnberg</cbc:TransportationServiceDescription>
</cac:TransportationService>
```

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Rail transport service from Hamburg to Bremen</cbc:TransportationServiceDescription>
</cac:TransportationService>
```

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
  <cbc:TransportationServiceDescription>Road transport service from Hamburg to Bremen</cbc:TransportationServiceDescription>
</cac:TransportationService>
```

```xml
<cac:TransportationService>
  <cbc:TransportServiceCode>3</cbc:TransportServiceCode>
</cac:TransportationService>
```

### `Unknown`

**Used as:** `cac:ArrivalTransportLocation` · `cac:CarryingTransportMeans` · `cac:DepartureTransportLocation` · `cac:EstimatedArrivalPeriod` · `cac:ForecastExceptionCriteriaLine` · `cac:LegalTotal` · `cac:PlannedArrivalPeriod` · `cac:PlannedDeparturePeriod` · `cac:PostEventPeriod` · `cac:PriceMonetaryTotal` · `cac:ReferencedTransportHandlingUnit` · `cac:ServicePoint` · `cac:ServicePointLocation` · `cac:TaxSubTotal` · `cac:TransportItemStatus` · `cac:TransportStatus` · `cac:UpdatedDelivery`

_39 unique instances across 17 elements_

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

```xml
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
```

```xml
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
```

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

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>2305</cbc:TransportMeansTypeCode>
  <cac:RailTransport>
    <cbc:TrainID>101</cbc:TrainID>
    <cbc:RailCarID>101-21</cbc:RailCarID>
  </cac:RailTransport>
</cac:CarryingTransportMeans>
```

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>31</cbc:TransportMeansTypeCode>
  <cac:RoadTransport>
    <cbc:LicensePlateID>KA04401</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:CarryingTransportMeans>
```

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>31</cbc:TransportMeansTypeCode>
  <cac:RoadTransport>
    <cbc:LicensePlateID>VE80044</cbc:LicensePlateID>
  </cac:RoadTransport>
</cac:CarryingTransportMeans>
```

```xml
<cac:CarryingTransportMeans>
  <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
  <cac:MaritimeTransport>
    <cbc:VesselID>IMO1234567</cbc:VesselID>
    <cbc:VesselName>MS Enova</cbc:VesselName>
  </cac:MaritimeTransport>
</cac:CarryingTransportMeans>
```

```xml
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
```

```xml
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
```

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

```xml
<cac:EstimatedArrivalPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>21:10:00.0Z</cbc:EndTime>
</cac:EstimatedArrivalPeriod>
```

```xml
<cac:ForecastExceptionCriteriaLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:ComparisonDataSourceCode>SELLER</cbc:ComparisonDataSourceCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriteriaLine>
```

```xml
<cac:ForecastExceptionCriteriaLine>
  <cbc:ForecastPurposeCode>SALES_FORECAST</cbc:ForecastPurposeCode>
  <cbc:ForecastTypeCode>BASE</cbc:ForecastTypeCode>
  <cbc:DataSourceCode>BUYER</cbc:DataSourceCode>
  <cbc:TimeDeltaDaysQuantity>20</cbc:TimeDeltaDaysQuantity>
</cac:ForecastExceptionCriteriaLine>
```

```xml
<cac:LegalTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:PayableAmount>100.00</cbc:PayableAmount>
</cac:LegalTotal>
```

```xml
<cac:LegalTotal>
  <cbc:LineExtensionAmount>100.00</cbc:LineExtensionAmount>
  <cbc:TaxExclusiveAmount>90.00</cbc:TaxExclusiveAmount>
  <cbc:PayableAmount>107.50</cbc:PayableAmount>
</cac:LegalTotal>
```

```xml
<cac:PlannedArrivalPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>16:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>17:00:00.0Z</cbc:EndTime>
</cac:PlannedArrivalPeriod>
```

```xml
<cac:PlannedArrivalPeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>20:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>20:30:00.0Z</cbc:EndTime>
</cac:PlannedArrivalPeriod>
```

```xml
<cac:PlannedArrivalPeriod>
  <cbc:StartDate>2011-03-14</cbc:StartDate>
  <cbc:StartTime>10:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-14</cbc:EndDate>
  <cbc:EndTime>11:00:00.0Z</cbc:EndTime>
</cac:PlannedArrivalPeriod>
```

```xml
<cac:PlannedArrivalPeriod>
  <cbc:StartDate>2011-03-14</cbc:StartDate>
  <cbc:StartTime>15:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-14</cbc:EndDate>
  <cbc:EndTime>16:00:00.0Z</cbc:EndTime>
</cac:PlannedArrivalPeriod>
```

```xml
<cac:PlannedDeparturePeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:PlannedDeparturePeriod>
```

```xml
<cac:PlannedDeparturePeriod>
  <cbc:StartDate>2011-03-13</cbc:StartDate>
  <cbc:StartTime>22:00:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-13</cbc:EndDate>
  <cbc:EndTime>22:30:00.0Z</cbc:EndTime>
</cac:PlannedDeparturePeriod>
```

```xml
<cac:PlannedDeparturePeriod>
  <cbc:StartDate>2011-03-14</cbc:StartDate>
  <cbc:StartTime>13:30:00.0Z</cbc:StartTime>
  <cbc:EndDate>2011-03-14</cbc:EndDate>
  <cbc:EndTime>14:00:00.0Z</cbc:EndTime>
</cac:PlannedDeparturePeriod>
```

```xml
<cac:PostEventPeriod>
  <cbc:DurationMeasure>30</cbc:DurationMeasure>
  <cbc:Description>Deviations shall be notified to the CONSIGNEE within max 30 minutes</cbc:Description>
</cac:PostEventPeriod>
```

```xml
<cac:PriceMonetaryTotal>
  <cbc:PayableAmount>2000</cbc:PayableAmount>
</cac:PriceMonetaryTotal>
```

```xml
<cac:PriceMonetaryTotal>
  <cbc:PayableAmount>300</cbc:PayableAmount>
</cac:PriceMonetaryTotal>
```

```xml
<cac:ReferencedTransportHandlingUnit>
  <cbc:ID>THU#1</cbc:ID>
</cac:ReferencedTransportHandlingUnit>
```

```xml
<cac:ReferencedTransportHandlingUnit>
  <cbc:ID>THU#2</cbc:ID>
</cac:ReferencedTransportHandlingUnit>
```

```xml
<cac:ReferencedTransportHandlingUnit>
  <cbc:ID>THU#3</cbc:ID>
</cac:ReferencedTransportHandlingUnit>
```

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

```xml
<cac:UpdatedDelivery>
  <cac:EstimatedDeliveryPeriod>
    <cbc:StartDate>2011-03-13</cbc:StartDate>
    <cbc:StartTime>21:00:00.0Z</cbc:StartTime>
    <cbc:EndDate>2011-03-13</cbc:EndDate>
    <cbc:EndTime>21:00:00.0Z</cbc:EndTime>
  </cac:EstimatedDeliveryPeriod>
</cac:UpdatedDelivery>
```

### `VerifiedGrossMassType`

**Used as:** `cac:VerifiedGrossMass`

_3 unique instances across 1 element_

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
    <cbc:DocumentDescription>Certificate for determination of VGM according to method 1</cbc:DocumentDescription>
  </cac:DocumentReference>
</cac:VerifiedGrossMass>
```

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

### `WebSiteType`

**Used as:** `cac:AdditionalWebSite`

_1 unique instance across 1 element_

```xml
<cac:AdditionalWebSite>
  <cbc:ID>1</cbc:ID>
  <cbc:Name>RSS</cbc:Name>
  <cbc:URI>https://www.oasis-open.org/feed</cbc:URI>
</cac:AdditionalWebSite>
```
