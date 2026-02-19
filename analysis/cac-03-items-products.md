# UBL Element Reference — Items, Products & Classification

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **12** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [ItemType](#ItemType)
  - [ItemIdentificationType](#ItemIdentificationType)
  - [ItemInstanceType](#ItemInstanceType)
  - [ItemLocationQuantityType](#ItemLocationQuantityType)
  - [ItemPropertyType](#ItemPropertyType)
  - [CommodityClassificationType](#CommodityClassificationType)
  - [DimensionType](#DimensionType)
  - [LotIdentificationType](#LotIdentificationType)
  - [SalesItemType](#SalesItemType)
  - [AttestationType](#AttestationType)
  - [AttestationLineType](#AttestationLineType)
  - [EnvironmentalEmissionType](#EnvironmentalEmissionType)

---

## cac Elements — Items, Products & Classification

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)