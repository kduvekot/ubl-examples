# UBL Element Reference — Retail, Supply Chain & Planning

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **17** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [ActivityDataLineType](#ActivityDataLineType)
  - [ForecastLineType](#ForecastLineType)
  - [ForecastRevisionLineType](#ForecastRevisionLineType)
  - [ForecastExceptionType](#ForecastExceptionType)
  - [ForecastExceptionCriterionLineType](#ForecastExceptionCriterionLineType)
  - [ExceptionCriteriaLineType](#ExceptionCriteriaLineType)
  - [ExceptionNotificationLineType](#ExceptionNotificationLineType)
  - [InventoryReportLineType](#InventoryReportLineType)
  - [StockAvailabilityReportLineType](#StockAvailabilityReportLineType)
  - [PerformanceDataLineType](#PerformanceDataLineType)
  - [PromotionalEventType](#PromotionalEventType)
  - [PromotionalEventLineItemType](#PromotionalEventLineItemType)
  - [PromotionalSpecificationType](#PromotionalSpecificationType)
  - [EventLineItemType](#EventLineItemType)
  - [EventTacticType](#EventTacticType)
  - [EventTacticEnumerationType](#EventTacticEnumerationType)
  - [RetailPlannedImpactType](#RetailPlannedImpactType)

---

## cac Elements — Retail, Supply Chain & Planning

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)