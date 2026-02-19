# UBL Element Reference — Orders, Invoices & Trade Lines

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **16** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [OrderLineType](#OrderLineType)
  - [OrderLineReferenceType](#OrderLineReferenceType)
  - [OrderReferenceType](#OrderReferenceType)
  - [LineItemType](#LineItemType)
  - [InvoiceLineType](#InvoiceLineType)
  - [CreditNoteLineType](#CreditNoteLineType)
  - [DebitNoteLineType](#DebitNoteLineType)
  - [QuotationLineType](#QuotationLineType)
  - [RequestForQuotationLineType](#RequestForQuotationLineType)
  - [ReceiptLineType](#ReceiptLineType)
  - [PurchaseReceiptLineType](#PurchaseReceiptLineType)
  - [PurchaseReferenceType](#PurchaseReferenceType)
  - [ReminderLineType](#ReminderLineType)
  - [RemittanceAdviceLineType](#RemittanceAdviceLineType)
  - [StatementLineType](#StatementLineType)
  - [BillingReferenceType](#BillingReferenceType)

---

## cac Elements — Orders, Invoices & Trade Lines

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)