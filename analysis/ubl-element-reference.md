# UBL Element Reference

Values, attributes, and composite instances observed across all official UBL example documents (2.0 – 2.5), grouped using the UBL 2.5 CSD02 XSD as the authoritative type reference.

## Contents

- [Summary](#summary)
- [cbc Elements](#cbc-elements)
- [cac Elements by domain group](#cac-elements)
  - [Party & Organization](./cac-01-party-organization.md) — 15 types
  - [Address, Location & Communication](./cac-02-address-location.md) — 8 types
  - [Items, Products & Classification](./cac-03-items-products.md) — 12 types
  - [Shipment, Goods & Delivery](./cac-04-shipment-delivery.md) — 15 types
  - [Transport Means & Operations](./cac-05-transport-means.md) — 13 types
  - [Procurement & Tendering](./cac-06-procurement-tendering.md) — 6 types
  - [Contract & Legal](./cac-07-contract-legal.md) — 5 types
  - [Financial, Payment & Tax](./cac-08-financial-payment.md) — 16 types
  - [Orders, Invoices & Trade Lines](./cac-09-orders-invoices.md) — 16 types
  - [Documents, References & Responses](./cac-10-documents-references.md) — 8 types
  - [Retail, Supply Chain & Planning](./cac-11-retail-supply-chain.md) — 17 types
  - [Digital Services & Security](./cac-12-digital-services.md) — 9 types

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

The 140 aggregate component types (ABIE) are organised into 12 domain-specific files.
Click a group heading to open that file, or a type name to jump directly to its entry.

### [Party & Organization](./cac-01-party-organization.md)

- [`PartyType`](./cac-01-party-organization.md#PartyType)
- [`BranchType`](./cac-01-party-organization.md#BranchType)
- [`CapabilityType`](./cac-01-party-organization.md#CapabilityType)
- [`ContactType`](./cac-01-party-organization.md#ContactType)
- [`ContractingPartyType`](./cac-01-party-organization.md#ContractingPartyType)
- [`CustomerPartyType`](./cac-01-party-organization.md#CustomerPartyType)
- [`EconomicOperatorPartyType`](./cac-01-party-organization.md#EconomicOperatorPartyType)
- [`EndorserPartyType`](./cac-01-party-organization.md#EndorserPartyType)
- [`ParticipantPartyType`](./cac-01-party-organization.md#ParticipantPartyType)
- [`PartyIdentificationType`](./cac-01-party-organization.md#PartyIdentificationType)
- [`PartyLegalEntityType`](./cac-01-party-organization.md#PartyLegalEntityType)
- [`PartyNameType`](./cac-01-party-organization.md#PartyNameType)
- [`PartyTaxSchemeType`](./cac-01-party-organization.md#PartyTaxSchemeType)
- [`PersonType`](./cac-01-party-organization.md#PersonType)
- [`SupplierPartyType`](./cac-01-party-organization.md#SupplierPartyType)

### [Address, Location & Communication](./cac-02-address-location.md)

- [`AddressType`](./cac-02-address-location.md#AddressType)
- [`AddressLineType`](./cac-02-address-location.md#AddressLineType)
- [`CountryType`](./cac-02-address-location.md#CountryType)
- [`LanguageType`](./cac-02-address-location.md#LanguageType)
- [`LocationType`](./cac-02-address-location.md#LocationType)
- [`LocationCoordinateType`](./cac-02-address-location.md#LocationCoordinateType)
- [`SocialMediaProfileType`](./cac-02-address-location.md#SocialMediaProfileType)
- [`WebSiteType`](./cac-02-address-location.md#WebSiteType)

### [Items, Products & Classification](./cac-03-items-products.md)

- [`ItemType`](./cac-03-items-products.md#ItemType)
- [`ItemIdentificationType`](./cac-03-items-products.md#ItemIdentificationType)
- [`ItemInstanceType`](./cac-03-items-products.md#ItemInstanceType)
- [`ItemLocationQuantityType`](./cac-03-items-products.md#ItemLocationQuantityType)
- [`ItemPropertyType`](./cac-03-items-products.md#ItemPropertyType)
- [`CommodityClassificationType`](./cac-03-items-products.md#CommodityClassificationType)
- [`DimensionType`](./cac-03-items-products.md#DimensionType)
- [`LotIdentificationType`](./cac-03-items-products.md#LotIdentificationType)
- [`SalesItemType`](./cac-03-items-products.md#SalesItemType)
- [`AttestationType`](./cac-03-items-products.md#AttestationType)
- [`AttestationLineType`](./cac-03-items-products.md#AttestationLineType)
- [`EnvironmentalEmissionType`](./cac-03-items-products.md#EnvironmentalEmissionType)

### [Shipment, Goods & Delivery](./cac-04-shipment-delivery.md)

- [`ShipmentType`](./cac-04-shipment-delivery.md#ShipmentType)
- [`ConsignmentType`](./cac-04-shipment-delivery.md#ConsignmentType)
- [`GoodsItemType`](./cac-04-shipment-delivery.md#GoodsItemType)
- [`GoodsItemPassportCounterfoilType`](./cac-04-shipment-delivery.md#GoodsItemPassportCounterfoilType)
- [`TransportHandlingUnitType`](./cac-04-shipment-delivery.md#TransportHandlingUnitType)
- [`PackageType`](./cac-04-shipment-delivery.md#PackageType)
- [`DeliveryType`](./cac-04-shipment-delivery.md#DeliveryType)
- [`DeliveryTermsType`](./cac-04-shipment-delivery.md#DeliveryTermsType)
- [`DeliveryChannelType`](./cac-04-shipment-delivery.md#DeliveryChannelType)
- [`DespatchType`](./cac-04-shipment-delivery.md#DespatchType)
- [`DespatchLineType`](./cac-04-shipment-delivery.md#DespatchLineType)
- [`PickupType`](./cac-04-shipment-delivery.md#PickupType)
- [`InstructionForReturnsLineType`](./cac-04-shipment-delivery.md#InstructionForReturnsLineType)
- [`TemperatureType`](./cac-04-shipment-delivery.md#TemperatureType)
- [`VerifiedGrossMassType`](./cac-04-shipment-delivery.md#VerifiedGrossMassType)

### [Transport Means & Operations](./cac-05-transport-means.md)

- [`TransportMeansType`](./cac-05-transport-means.md#TransportMeansType)
- [`AirTransportType`](./cac-05-transport-means.md#AirTransportType)
- [`MaritimeTransportType`](./cac-05-transport-means.md#MaritimeTransportType)
- [`RailTransportType`](./cac-05-transport-means.md#RailTransportType)
- [`RoadTransportType`](./cac-05-transport-means.md#RoadTransportType)
- [`ShipmentStageType`](./cac-05-transport-means.md#ShipmentStageType)
- [`TransportationServiceType`](./cac-05-transport-means.md#TransportationServiceType)
- [`TransportationSegmentType`](./cac-05-transport-means.md#TransportationSegmentType)
- [`TransportScheduleType`](./cac-05-transport-means.md#TransportScheduleType)
- [`TransportEventType`](./cac-05-transport-means.md#TransportEventType)
- [`TransportExecutionTermsType`](./cac-05-transport-means.md#TransportExecutionTermsType)
- [`TransportEquipmentType`](./cac-05-transport-means.md#TransportEquipmentType)
- [`TransportEquipmentSealType`](./cac-05-transport-means.md#TransportEquipmentSealType)

### [Procurement & Tendering](./cac-06-procurement-tendering.md)

- [`ProcurementProjectType`](./cac-06-procurement-tendering.md#ProcurementProjectType)
- [`ProcurementProjectLotReferenceType`](./cac-06-procurement-tendering.md#ProcurementProjectLotReferenceType)
- [`TenderingTermsType`](./cac-06-procurement-tendering.md#TenderingTermsType)
- [`TenderPreparationType`](./cac-06-procurement-tendering.md#TenderPreparationType)
- [`EvidenceType`](./cac-06-procurement-tendering.md#EvidenceType)
- [`ItemManagementProfileType`](./cac-06-procurement-tendering.md#ItemManagementProfileType)

### [Contract & Legal](./cac-07-contract-legal.md)

- [`ContractType`](./cac-07-contract-legal.md#ContractType)
- [`EndorsementType`](./cac-07-contract-legal.md#EndorsementType)
- [`SignatureType`](./cac-07-contract-legal.md#SignatureType)
- [`CustomsDeclarationType`](./cac-07-contract-legal.md#CustomsDeclarationType)
- [`NotificationRequirementType`](./cac-07-contract-legal.md#NotificationRequirementType)

### [Financial, Payment & Tax](./cac-08-financial-payment.md)

- [`PaymentType`](./cac-08-financial-payment.md#PaymentType)
- [`PaymentMeansType`](./cac-08-financial-payment.md#PaymentMeansType)
- [`PaymentTermsType`](./cac-08-financial-payment.md#PaymentTermsType)
- [`FinancialAccountType`](./cac-08-financial-payment.md#FinancialAccountType)
- [`FinancialInstitutionType`](./cac-08-financial-payment.md#FinancialInstitutionType)
- [`CashRegisterType`](./cac-08-financial-payment.md#CashRegisterType)
- [`ExchangeRateType`](./cac-08-financial-payment.md#ExchangeRateType)
- [`TaxTotalType`](./cac-08-financial-payment.md#TaxTotalType)
- [`TaxSubtotalType`](./cac-08-financial-payment.md#TaxSubtotalType)
- [`TaxCategoryType`](./cac-08-financial-payment.md#TaxCategoryType)
- [`TaxSchemeType`](./cac-08-financial-payment.md#TaxSchemeType)
- [`AllowanceChargeType`](./cac-08-financial-payment.md#AllowanceChargeType)
- [`MonetaryTotalType`](./cac-08-financial-payment.md#MonetaryTotalType)
- [`PriceType`](./cac-08-financial-payment.md#PriceType)
- [`PeriodType`](./cac-08-financial-payment.md#PeriodType)
- [`TransactionConditionsType`](./cac-08-financial-payment.md#TransactionConditionsType)

### [Orders, Invoices & Trade Lines](./cac-09-orders-invoices.md)

- [`OrderLineType`](./cac-09-orders-invoices.md#OrderLineType)
- [`OrderLineReferenceType`](./cac-09-orders-invoices.md#OrderLineReferenceType)
- [`OrderReferenceType`](./cac-09-orders-invoices.md#OrderReferenceType)
- [`LineItemType`](./cac-09-orders-invoices.md#LineItemType)
- [`InvoiceLineType`](./cac-09-orders-invoices.md#InvoiceLineType)
- [`CreditNoteLineType`](./cac-09-orders-invoices.md#CreditNoteLineType)
- [`DebitNoteLineType`](./cac-09-orders-invoices.md#DebitNoteLineType)
- [`QuotationLineType`](./cac-09-orders-invoices.md#QuotationLineType)
- [`RequestForQuotationLineType`](./cac-09-orders-invoices.md#RequestForQuotationLineType)
- [`ReceiptLineType`](./cac-09-orders-invoices.md#ReceiptLineType)
- [`PurchaseReceiptLineType`](./cac-09-orders-invoices.md#PurchaseReceiptLineType)
- [`PurchaseReferenceType`](./cac-09-orders-invoices.md#PurchaseReferenceType)
- [`ReminderLineType`](./cac-09-orders-invoices.md#ReminderLineType)
- [`RemittanceAdviceLineType`](./cac-09-orders-invoices.md#RemittanceAdviceLineType)
- [`StatementLineType`](./cac-09-orders-invoices.md#StatementLineType)
- [`BillingReferenceType`](./cac-09-orders-invoices.md#BillingReferenceType)

### [Documents, References & Responses](./cac-10-documents-references.md)

- [`DocumentReferenceType`](./cac-10-documents-references.md#DocumentReferenceType)
- [`DocumentDistributionType`](./cac-10-documents-references.md#DocumentDistributionType)
- [`DocumentMetadataType`](./cac-10-documents-references.md#DocumentMetadataType)
- [`ExternalReferenceType`](./cac-10-documents-references.md#ExternalReferenceType)
- [`AttachmentType`](./cac-10-documents-references.md#AttachmentType)
- [`ResponseType`](./cac-10-documents-references.md#ResponseType)
- [`StatusType`](./cac-10-documents-references.md#StatusType)
- [`Unknown`](./cac-10-documents-references.md#Unknown)

### [Retail, Supply Chain & Planning](./cac-11-retail-supply-chain.md)

- [`ActivityDataLineType`](./cac-11-retail-supply-chain.md#ActivityDataLineType)
- [`ForecastLineType`](./cac-11-retail-supply-chain.md#ForecastLineType)
- [`ForecastRevisionLineType`](./cac-11-retail-supply-chain.md#ForecastRevisionLineType)
- [`ForecastExceptionType`](./cac-11-retail-supply-chain.md#ForecastExceptionType)
- [`ForecastExceptionCriterionLineType`](./cac-11-retail-supply-chain.md#ForecastExceptionCriterionLineType)
- [`ExceptionCriteriaLineType`](./cac-11-retail-supply-chain.md#ExceptionCriteriaLineType)
- [`ExceptionNotificationLineType`](./cac-11-retail-supply-chain.md#ExceptionNotificationLineType)
- [`InventoryReportLineType`](./cac-11-retail-supply-chain.md#InventoryReportLineType)
- [`StockAvailabilityReportLineType`](./cac-11-retail-supply-chain.md#StockAvailabilityReportLineType)
- [`PerformanceDataLineType`](./cac-11-retail-supply-chain.md#PerformanceDataLineType)
- [`PromotionalEventType`](./cac-11-retail-supply-chain.md#PromotionalEventType)
- [`PromotionalEventLineItemType`](./cac-11-retail-supply-chain.md#PromotionalEventLineItemType)
- [`PromotionalSpecificationType`](./cac-11-retail-supply-chain.md#PromotionalSpecificationType)
- [`EventLineItemType`](./cac-11-retail-supply-chain.md#EventLineItemType)
- [`EventTacticType`](./cac-11-retail-supply-chain.md#EventTacticType)
- [`EventTacticEnumerationType`](./cac-11-retail-supply-chain.md#EventTacticEnumerationType)
- [`RetailPlannedImpactType`](./cac-11-retail-supply-chain.md#RetailPlannedImpactType)

### [Digital Services & Security](./cac-12-digital-services.md)

- [`DigitalServiceType`](./cac-12-digital-services.md#DigitalServiceType)
- [`DigitalAgreementTermsType`](./cac-12-digital-services.md#DigitalAgreementTermsType)
- [`DigitalProcessType`](./cac-12-digital-services.md#DigitalProcessType)
- [`DigitalCollaborationType`](./cac-12-digital-services.md#DigitalCollaborationType)
- [`ServiceLevelAgreementType`](./cac-12-digital-services.md#ServiceLevelAgreementType)
- [`MessageDeliveryType`](./cac-12-digital-services.md#MessageDeliveryType)
- [`EncryptionDataType`](./cac-12-digital-services.md#EncryptionDataType)
- [`EncryptionCertificatePathChainType`](./cac-12-digital-services.md#EncryptionCertificatePathChainType)
- [`EncryptionSymmetricAlgorithmType`](./cac-12-digital-services.md#EncryptionSymmetricAlgorithmType)

---

[↑ Back to contents](#contents)