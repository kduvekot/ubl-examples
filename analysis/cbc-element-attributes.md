# UBL `cbc` Element Attributes Reference

Unique attribute values observed on `cbc` elements across all official UBL example documents (2.0 – 2.5).

- **104** `cbc` elements carry attributes
- **15** distinct attribute names
- **135** unique element+attribute combinations

---

## `cbc:AddressFormatCode`

### `@listAgencyID`

```xml
<cbc:AddressFormatCode listAgencyID="320">StructuredDK</cbc:AddressFormatCode>
<cbc:AddressFormatCode listAgencyID="700">Structured</cbc:AddressFormatCode>
```

### `@listID`

```xml
<cbc:AddressFormatCode listID="CENBII3">Structured</cbc:AddressFormatCode>
<cbc:AddressFormatCode listID="urn:oioubl:codelist:addressformatcode-1.1">StructuredDK</cbc:AddressFormatCode>
```

## `cbc:AllowanceTotalAmount`

### `@currencyID`

```xml
<cbc:AllowanceTotalAmount currencyID="EUR">100</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount currencyID="EUR">5.00</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount currencyID="GBP">10.00</cbc:AllowanceTotalAmount>
<cbc:AllowanceTotalAmount currencyID="SEK">100</cbc:AllowanceTotalAmount>
```

## `cbc:Amount`

### `@currencyID`

```xml
<cbc:Amount currencyID="DKK">0.00</cbc:Amount>
<cbc:Amount currencyID="EUR">0.275</cbc:Amount>
<cbc:Amount currencyID="EUR">1.00</cbc:Amount>
<cbc:Amount currencyID="EUR">10</cbc:Amount>
<cbc:Amount currencyID="EUR">10.00</cbc:Amount>
<cbc:Amount currencyID="EUR">100</cbc:Amount>
<cbc:Amount currencyID="EUR">12</cbc:Amount>
<cbc:Amount currencyID="EUR">225</cbc:Amount>
<cbc:Amount currencyID="EUR">2500</cbc:Amount>
<cbc:Amount currencyID="EUR">4.80</cbc:Amount>
<cbc:Amount currencyID="EUR">5.00</cbc:Amount>
<cbc:Amount currencyID="GBP">0.0</cbc:Amount>
<cbc:Amount currencyID="GBP">10.00</cbc:Amount>
<cbc:Amount currencyID="GBP">100.0</cbc:Amount>
<cbc:Amount currencyID="SEK">100</cbc:Amount>
<cbc:Amount currencyID="USD">12.70</cbc:Amount>
<cbc:Amount currencyID="USD">254.00</cbc:Amount>
```

## `cbc:AvailabilityStatusCode`

### `@listAgencyName`

```xml
<cbc:AvailabilityStatusCode listAgencyName="UN/ECE">1</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode listAgencyName="UN/ECE">2</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode listAgencyName="UN/ECE">8</cbc:AvailabilityStatusCode>
```

### `@listID`

```xml
<cbc:AvailabilityStatusCode listID="7011">1</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode listID="7011">2</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode listID="7011">8</cbc:AvailabilityStatusCode>
```

### `@listURI`

```xml
<cbc:AvailabilityStatusCode listURI="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm">1</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode listURI="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm">2</cbc:AvailabilityStatusCode>
<cbc:AvailabilityStatusCode listURI="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm">8</cbc:AvailabilityStatusCode>
```

## `cbc:BackorderQuantity`

### `@unitCode`

```xml
<cbc:BackorderQuantity unitCode="KG">10</cbc:BackorderQuantity>
<cbc:BackorderQuantity unitCode="KGM">10</cbc:BackorderQuantity>
```

## `cbc:BalanceAmount`

### `@currencyID`

```xml
<cbc:BalanceAmount currencyID="GBP">-107.50</cbc:BalanceAmount>
<cbc:BalanceAmount currencyID="GBP">107.50</cbc:BalanceAmount>
```

## `cbc:BaseAmount`

### `@currencyID`

```xml
<cbc:BaseAmount currencyID="EUR">1500</cbc:BaseAmount>
<cbc:BaseAmount currencyID="EUR">2.75</cbc:BaseAmount>
<cbc:BaseAmount currencyID="USD">254.00</cbc:BaseAmount>
```

## `cbc:BaseQuantity`

### `@unitCode`

```xml
<cbc:BaseQuantity unitCode="C62">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="KG">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
<cbc:BaseQuantity unitCode="LTR">1</cbc:BaseQuantity>
```

## `cbc:CashChangeAmount`

### `@currencyID`

```xml
<cbc:CashChangeAmount currencyID="EUR">5.00</cbc:CashChangeAmount>
```

## `cbc:ChargeTotalAmount`

### `@currencyID`

```xml
<cbc:ChargeTotalAmount currencyID="EUR">1.00</cbc:ChargeTotalAmount>
<cbc:ChargeTotalAmount currencyID="EUR">10.00</cbc:ChargeTotalAmount>
<cbc:ChargeTotalAmount currencyID="EUR">100</cbc:ChargeTotalAmount>
<cbc:ChargeTotalAmount currencyID="SEK">100</cbc:ChargeTotalAmount>
```

## `cbc:CompanyID`

### `@schemeAgencyID`

```xml
<cbc:CompanyID schemeAgencyID="ZZZ">5402697509</cbc:CompanyID>
<cbc:CompanyID schemeAgencyID="ZZZ">5645342123</cbc:CompanyID>
<cbc:CompanyID schemeAgencyID="ZZZ">6411982340</cbc:CompanyID>
<cbc:CompanyID schemeAgencyID="ZZZ">BE54321</cbc:CompanyID>
<cbc:CompanyID schemeAgencyID="ZZZ">DK12345</cbc:CompanyID>
```

### `@schemeID`

```xml
<cbc:CompanyID schemeID="BEVAT">BE54321</cbc:CompanyID>
<cbc:CompanyID schemeID="CVR">5402697509</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:CVR">18296799</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:CVR">DK12345678</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:CVR">DK18296799</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:CVR">DK59873677</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:SE">DK12345678</cbc:CompanyID>
<cbc:CompanyID schemeID="DK:SE">DK18296799</cbc:CompanyID>
<cbc:CompanyID schemeID="DKVAT">DK12345</cbc:CompanyID>
<cbc:CompanyID schemeID="SE:ORGNR">5532331183</cbc:CompanyID>
<cbc:CompanyID schemeID="SE:ORGNR">5532332283</cbc:CompanyID>
<cbc:CompanyID schemeID="UK:CH">6411982340</cbc:CompanyID>
<cbc:CompanyID schemeID="ZZZ">5645342123</cbc:CompanyID>
```

## `cbc:ComparedValueMeasure`

### `@unitCode`

```xml
<cbc:ComparedValueMeasure unitCode="KGM">2</cbc:ComparedValueMeasure>
```

## `cbc:CreditLineAmount`

### `@currencyID`

```xml
<cbc:CreditLineAmount currencyID="GBP">0.00</cbc:CreditLineAmount>
<cbc:CreditLineAmount currencyID="GBP">107.50</cbc:CreditLineAmount>
```

## `cbc:CreditedQuantity`

### `@unitCode`

```xml
<cbc:CreditedQuantity unitCode="C62">-1</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="C62">1</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="C62">2</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="C62">250</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="KG">100</cbc:CreditedQuantity>
<cbc:CreditedQuantity unitCode="KGM">100</cbc:CreditedQuantity>
```

## `cbc:DebitLineAmount`

### `@currencyID`

```xml
<cbc:DebitLineAmount currencyID="GBP">0.00</cbc:DebitLineAmount>
<cbc:DebitLineAmount currencyID="GBP">107.50</cbc:DebitLineAmount>
```

## `cbc:DebitedQuantity`

### `@unitCode`

```xml
<cbc:DebitedQuantity unitCode="C62">-1</cbc:DebitedQuantity>
<cbc:DebitedQuantity unitCode="C62">1</cbc:DebitedQuantity>
<cbc:DebitedQuantity unitCode="C62">2</cbc:DebitedQuantity>
<cbc:DebitedQuantity unitCode="C62">250</cbc:DebitedQuantity>
<cbc:DebitedQuantity unitCode="EA">1</cbc:DebitedQuantity>
<cbc:DebitedQuantity unitCode="EA">2</cbc:DebitedQuantity>
```

## `cbc:DeclaredCarriageValueAmount`

### `@currencyID`

```xml
<cbc:DeclaredCarriageValueAmount currencyID="USD">1500.00</cbc:DeclaredCarriageValueAmount>
```

## `cbc:DeclaredCustomsValueAmount`

### `@currencyID`

```xml
<cbc:DeclaredCustomsValueAmount currencyID="DKK">0.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">1000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">10000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">1500.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">2000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">2500.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">3000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">500.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">5000.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="DKK">750.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="EUR">0.00</cbc:DeclaredCustomsValueAmount>
<cbc:DeclaredCustomsValueAmount currencyID="GBP">524.80</cbc:DeclaredCustomsValueAmount>
```

## `cbc:DeclaredStatisticsValueAmount`

### `@currencyID`

```xml
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">1000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">10000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">10050.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">1500.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">2000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">2500.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">3000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">34800.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">4500.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">500.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">5000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="DKK">750.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="EUR">182.62</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="USD">1000.00</cbc:DeclaredStatisticsValueAmount>
<cbc:DeclaredStatisticsValueAmount currencyID="USD">250.00</cbc:DeclaredStatisticsValueAmount>
```

## `cbc:DeliveredQuantity`

### `@unitCode`

```xml
<cbc:DeliveredQuantity unitCode="KG">90</cbc:DeliveredQuantity>
<cbc:DeliveredQuantity unitCode="KGM">90</cbc:DeliveredQuantity>
```

## `cbc:Description`

### `@languageID`

```xml
<cbc:Description languageID="CN">本国海域或公海捕捞的鱼类或水生无脊椎动物或养殖水生动物</cbc:Description>
<cbc:Description languageID="CN">经中国国家质量监督检验检疫总局批准的，丹麦以外其他国家的企业生产的鱼粉或鱼
						油。该鱼粉或鱼油____________________________</cbc:Description>
<cbc:Description languageID="CN">经丹麦主管机构批准的供人类消费水产品加工厂的副产品</cbc:Description>
<cbc:Description languageID="DK">fisk eller havdyr, der ikke er pattedyr, som er fanget enten i landets eller reg</cbc:Description>
<cbc:Description languageID="DK">fiskemel eller fiskeolie fra andre lande, fra virksomheder, der er godkendt af A</cbc:Description>
<cbc:Description languageID="DK">fra afskær fra virksomheder, som er godkendt af den kompetente myndighed i Danma</cbc:Description>
<cbc:Description languageID="EN">Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:
				3MB. Screen 1440x900</cbc:Description>
<cbc:Description languageID="EN">fish meal or fish oil from countries other than Denmark from establishments appr</cbc:Description>
<cbc:Description languageID="EN">fish or aquatic invertebrates caught in the country or region’s domestic sea or </cbc:Description>
<cbc:Description languageID="EN">from offal from plants, which are approved by the competent authority in Denmark</cbc:Description>
```

## `cbc:DocumentCurrencyCode`

### `@listAgencyID`

```xml
<cbc:DocumentCurrencyCode listAgencyID="6">EUR</cbc:DocumentCurrencyCode>
```

### `@listID`

```xml
<cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">EUR</cbc:DocumentCurrencyCode>
```

## `cbc:DocumentTypeCode`

### `@listAgencyID`

```xml
<cbc:DocumentTypeCode listAgencyID="306">SM1</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listAgencyID="6">380</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listAgencyID="6">381</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listAgencyID="6">BN</cbc:DocumentTypeCode>
```

### `@listAgencyName`

```xml
<cbc:DocumentTypeCode listAgencyName="SMDG">SM1</cbc:DocumentTypeCode>
```

### `@listID`

```xml
<cbc:DocumentTypeCode listID="UN/ECE 1001">380</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listID="UN/ECE 1001">381</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listID="UN/ECE 1153">BN</cbc:DocumentTypeCode>
<cbc:DocumentTypeCode listID="VGM">SM1</cbc:DocumentTypeCode>
```

## `cbc:DurationMeasure`

### `@unitCode`

```xml
<cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
<cbc:DurationMeasure unitCode="MIN">30</cbc:DurationMeasure>
```

## `cbc:EmbeddedDocumentBinaryObject`

### `@mimeCode`

```xml
<cbc:EmbeddedDocumentBinaryObject mimeCode="application/CSTAdata+xml">UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
<cbc:EmbeddedDocumentBinaryObject mimeCode="application/pdf">UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi</cbc:EmbeddedDocumentBinaryObject>
```

## `cbc:EndpointID`

### `@schemeAgencyID`

```xml
<cbc:EndpointID schemeAgencyID="9">01842222222222</cbc:EndpointID>
<cbc:EndpointID schemeAgencyID="9">1234567890123</cbc:EndpointID>
<cbc:EndpointID schemeAgencyID="9">1234567987654</cbc:EndpointID>
<cbc:EndpointID schemeAgencyID="9">5798000416604</cbc:EndpointID>
<cbc:EndpointID schemeAgencyID="9">7300072311115</cbc:EndpointID>
<cbc:EndpointID schemeAgencyID="9">7302347231111</cbc:EndpointID>
<cbc:EndpointID schemeAgencyID="9">9994567987654</cbc:EndpointID>
```

### `@schemeID`

```xml
<cbc:EndpointID schemeID="DK:CVR">DK18296799</cbc:EndpointID>
<cbc:EndpointID schemeID="FI:OVT">01841111111111</cbc:EndpointID>
<cbc:EndpointID schemeID="FI:OVT">01842222222222</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">1234567890123</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">1234567987654</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">5798000416604</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">7300072311115</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">7302347231111</cbc:EndpointID>
<cbc:EndpointID schemeID="GLN">9994567987654</cbc:EndpointID>
```

## `cbc:FreeOnBoardValueAmount`

### `@currencyID`

```xml
<cbc:FreeOnBoardValueAmount currencyID="USD">1200.00</cbc:FreeOnBoardValueAmount>
<cbc:FreeOnBoardValueAmount currencyID="USD">1241.30</cbc:FreeOnBoardValueAmount>
```

## `cbc:FullnessIndicationCode`

### `@listAgencyID`

```xml
<cbc:FullnessIndicationCode listAgencyID="6">5</cbc:FullnessIndicationCode>
```

### `@listID`

```xml
<cbc:FullnessIndicationCode listID="UN/ECE 8169">5</cbc:FullnessIndicationCode>
```

## `cbc:GrossMassMeasure`

### `@unitCode`

```xml
<cbc:GrossMassMeasure unitCode="KGM">25730</cbc:GrossMassMeasure>
```

## `cbc:GrossVolumeMeasure`

### `@unitCode`

```xml
<cbc:GrossVolumeMeasure unitCode="MTQ">0.336</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure unitCode="MTQ">1.536</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure unitCode="MTQ">2</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure unitCode="MTQ">39</cbc:GrossVolumeMeasure>
<cbc:GrossVolumeMeasure unitCode="MTQ">78</cbc:GrossVolumeMeasure>
```

## `cbc:GrossWeightMeasure`

### `@unitCode`

```xml
<cbc:GrossWeightMeasure unitCode="KG">774.14400</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">1.5</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">1000.0</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">12</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">130</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">230.80</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">25000</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">30</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">400</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">50000</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">600</cbc:GrossWeightMeasure>
<cbc:GrossWeightMeasure unitCode="KGM">88.00</cbc:GrossWeightMeasure>
```

## `cbc:ID`

### `@schemeAgencyID`

```xml
<cbc:ID schemeAgencyID="306">XXX</cbc:ID>
<cbc:ID schemeAgencyID="320">63</cbc:ID>
<cbc:ID schemeAgencyID="5">TRHU1652173</cbc:ID>
<cbc:ID schemeAgencyID="6">123452340123</cbc:ID>
<cbc:ID schemeAgencyID="6">1234567890123</cbc:ID>
<cbc:ID schemeAgencyID="6">AA</cbc:ID>
<cbc:ID schemeAgencyID="6">E</cbc:ID>
<cbc:ID schemeAgencyID="6">FOT</cbc:ID>
<cbc:ID schemeAgencyID="6">GBBRS</cbc:ID>
<cbc:ID schemeAgencyID="6">GBLHR</cbc:ID>
<cbc:ID schemeAgencyID="6">S</cbc:ID>
<cbc:ID schemeAgencyID="6">USBOS</cbc:ID>
<cbc:ID schemeAgencyID="6">VAT</cbc:ID>
<cbc:ID schemeAgencyID="9">098740918237</cbc:ID>
<cbc:ID schemeAgencyID="9">0987654321123</cbc:ID>
<cbc:ID schemeAgencyID="9">0987678321123</cbc:ID>
<cbc:ID schemeAgencyID="9">1231412341324</cbc:ID>
<cbc:ID schemeAgencyID="9">1234567890123</cbc:ID>
<cbc:ID schemeAgencyID="9">1234567890124</cbc:ID>
<cbc:ID schemeAgencyID="9">1234567890125</cbc:ID>
<cbc:ID schemeAgencyID="9">1234567890126</cbc:ID>
<cbc:ID schemeAgencyID="9">1234567890127</cbc:ID>
<cbc:ID schemeAgencyID="9">1234567890128</cbc:ID>
<cbc:ID schemeAgencyID="9">1238764941386</cbc:ID>
<cbc:ID schemeAgencyID="9">5398000392577</cbc:ID>
<cbc:ID schemeAgencyID="9">5790000127777</cbc:ID>
<cbc:ID schemeAgencyID="9">5798000416604</cbc:ID>
<cbc:ID schemeAgencyID="9">6754238987648</cbc:ID>
<cbc:ID schemeAgencyID="9">67654328394567</cbc:ID>
<cbc:ID schemeAgencyID="9">7300070011115</cbc:ID>
<cbc:ID schemeAgencyID="ZZZ">EmployeeXXX</cbc:ID>
```

### `@schemeAgencyName`

```xml
<cbc:ID schemeAgencyName="GS1">12345698</cbc:ID>
<cbc:ID schemeAgencyName="GS1">123465</cbc:ID>
<cbc:ID schemeAgencyName="GS1">1236541</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058673821325</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058673827000</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058673827100</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058673827112</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058673827123</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058673827641</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4058675698641</cbc:ID>
<cbc:ID schemeAgencyName="GS1">43125678</cbc:ID>
<cbc:ID schemeAgencyName="GS1">4568763527610</cbc:ID>
<cbc:ID schemeAgencyName="GS1">7365566156191234567</cbc:ID>
<cbc:ID schemeAgencyName="GS1">89767764</cbc:ID>
<cbc:ID schemeAgencyName="GS1">987456123</cbc:ID>
<cbc:ID schemeAgencyName="GS1">987654321</cbc:ID>
<cbc:ID schemeAgencyName="INCOTERMS">EXW</cbc:ID>
<cbc:ID schemeAgencyName="SMDG">XXX</cbc:ID>
<cbc:ID schemeAgencyName="UN">CNSHA</cbc:ID>
<cbc:ID schemeAgencyName="UN">DEBREV</cbc:ID>
<cbc:ID schemeAgencyName="UN">DEHAM</cbc:ID>
<cbc:ID schemeAgencyName="UN">ITGOA</cbc:ID>
<cbc:ID schemeAgencyName="UN">MAPTM</cbc:ID>
<cbc:ID schemeAgencyName="UN">NOOSL</cbc:ID>
<cbc:ID schemeAgencyName="WCO">2005US12345678998765432112345678</cbc:ID>
```

### `@schemeID`

```xml
<cbc:ID schemeID="AuthorisationNumber">M165</cbc:ID>
<cbc:ID schemeID="DK:CVR">DK12345678</cbc:ID>
<cbc:ID schemeID="DK:CVR">DK18296799</cbc:ID>
<cbc:ID schemeID="GB:VAT">GB999999973</cbc:ID>
<cbc:ID schemeID="GLN">098740918237</cbc:ID>
<cbc:ID schemeID="GLN">0987654321123</cbc:ID>
<cbc:ID schemeID="GLN">0987678321123</cbc:ID>
<cbc:ID schemeID="GLN">1231412341324</cbc:ID>
<cbc:ID schemeID="GLN">1234567890123</cbc:ID>
<cbc:ID schemeID="GLN">1238764941386</cbc:ID>
<cbc:ID schemeID="GLN">5398000392577</cbc:ID>
<cbc:ID schemeID="GLN">5790000127777</cbc:ID>
<cbc:ID schemeID="GLN">5798000416604</cbc:ID>
<cbc:ID schemeID="GLN">6754238987648</cbc:ID>
<cbc:ID schemeID="GLN">67654328394567</cbc:ID>
<cbc:ID schemeID="GLN">7300070011115</cbc:ID>
<cbc:ID schemeID="GTIN">123452340123</cbc:ID>
<cbc:ID schemeID="GTIN">1234567890123</cbc:ID>
<cbc:ID schemeID="GTIN">1234567890124</cbc:ID>
<cbc:ID schemeID="GTIN">1234567890125</cbc:ID>
<cbc:ID schemeID="GTIN">1234567890126</cbc:ID>
<cbc:ID schemeID="GTIN">1234567890127</cbc:ID>
<cbc:ID schemeID="GTIN">1234567890128</cbc:ID>
<cbc:ID schemeID="IMCOTERM">FOT</cbc:ID>
<cbc:ID schemeID="ISO 6346">TRHU1652173</cbc:ID>
<cbc:ID schemeID="IT:VAT">IT01234567890</cbc:ID>
<cbc:ID schemeID="LINES">XXX</cbc:ID>
<cbc:ID schemeID="Passport">325334535</cbc:ID>
<cbc:ID schemeID="Skat.dk">DK10035643</cbc:ID>
<cbc:ID schemeID="UN/ECE 5153">VAT</cbc:ID>
<cbc:ID schemeID="UN/ECE 5305">AA</cbc:ID>
<cbc:ID schemeID="UN/ECE 5305">E</cbc:ID>
<cbc:ID schemeID="UN/ECE 5305">O</cbc:ID>
<cbc:ID schemeID="UN/ECE 5305">S</cbc:ID>
<cbc:ID schemeID="UN/LOCODE">GBBRS</cbc:ID>
<cbc:ID schemeID="UN/LOCODE">GBLHR</cbc:ID>
<cbc:ID schemeID="UN/LOCODE">USBOS</cbc:ID>
<cbc:ID schemeID="ZZZ">123456789</cbc:ID>
<cbc:ID schemeID="ZZZ">345KS5324</cbc:ID>
<cbc:ID schemeID="ZZZ">EmployeeXXX</cbc:ID>
<cbc:ID schemeID="ZZZ">Supp123</cbc:ID>
<cbc:ID schemeID="locode">DK003102</cbc:ID>
<cbc:ID schemeID="urn:oioubl:id:taxschemeid-1.1">63</cbc:ID>
```

### `@schemeName`

```xml
<cbc:ID schemeName="GINC">7365566156191234567</cbc:ID>
<cbc:ID schemeName="GLN">123465</cbc:ID>
<cbc:ID schemeName="GLN">1236541</cbc:ID>
<cbc:ID schemeName="GLN">4058673821325</cbc:ID>
<cbc:ID schemeName="GLN">4058673827000</cbc:ID>
<cbc:ID schemeName="GLN">4058673827100</cbc:ID>
<cbc:ID schemeName="GLN">4058673827112</cbc:ID>
<cbc:ID schemeName="GLN">4058673827123</cbc:ID>
<cbc:ID schemeName="GLN">4058673827641</cbc:ID>
<cbc:ID schemeName="GLN">4058675698641</cbc:ID>
<cbc:ID schemeName="GLN">43125678</cbc:ID>
<cbc:ID schemeName="GLN">4568763527610</cbc:ID>
<cbc:ID schemeName="GLN">89767764</cbc:ID>
<cbc:ID schemeName="GLN">987456123</cbc:ID>
<cbc:ID schemeName="GLN">987654321</cbc:ID>
<cbc:ID schemeName="GRAI">12345698</cbc:ID>
<cbc:ID schemeName="INCOTERMS">EXW</cbc:ID>
<cbc:ID schemeName="LOCODE">ITGOA</cbc:ID>
<cbc:ID schemeName="LOCODE">MAPTM</cbc:ID>
<cbc:ID schemeName="MovementReferenceNumber">TPS_1</cbc:ID>
<cbc:ID schemeName="SMDG master liner code list">XXX</cbc:ID>
<cbc:ID schemeName="UN/LOCODE">CNSHA</cbc:ID>
<cbc:ID schemeName="UN/LOCODE">DEBREV</cbc:ID>
<cbc:ID schemeName="UN/LOCODE">DEHAM</cbc:ID>
<cbc:ID schemeName="UN/LOCODE">NOOSL</cbc:ID>
<cbc:ID schemeName="UNLOCODE">ITGOA</cbc:ID>
<cbc:ID schemeName="Unique Consignment Reference">2005US12345678998765432112345678</cbc:ID>
<cbc:ID schemeName="bic">BFCU4040001</cbc:ID>
<cbc:ID schemeName="bic">BFCU4040002</cbc:ID>
```

## `cbc:IdentificationCode`

### `@listAgencyID`

```xml
<cbc:IdentificationCode listAgencyID="6">BE</cbc:IdentificationCode>
<cbc:IdentificationCode listAgencyID="6">DK</cbc:IdentificationCode>
```

### `@listID`

```xml
<cbc:IdentificationCode listID="ISO3166-1">BE</cbc:IdentificationCode>
<cbc:IdentificationCode listID="ISO3166-1">DK</cbc:IdentificationCode>
```

## `cbc:IndustryClassificationCode`

### `@listAgencyID`

```xml
<cbc:IndustryClassificationCode listAgencyID="6">CA</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode listAgencyID="6">SPC</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode listAgencyID="6">TR</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode listAgencyID="6">WPA</cbc:IndustryClassificationCode>
```

### `@listID`

```xml
<cbc:IndustryClassificationCode listID="UN/ECE 3035">CA</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode listID="UN/ECE 3035">SPC</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode listID="UN/ECE 3035">TR</cbc:IndustryClassificationCode>
<cbc:IndustryClassificationCode listID="UN/ECE 3035">WPA</cbc:IndustryClassificationCode>
```

## `cbc:InsuranceValueAmount`

### `@currencyID`

```xml
<cbc:InsuranceValueAmount currencyID="USD">1000.00</cbc:InsuranceValueAmount>
<cbc:InsuranceValueAmount currencyID="USD">1241.30</cbc:InsuranceValueAmount>
```

## `cbc:InventoryValueAmount`

### `@currencyID`

```xml
<cbc:InventoryValueAmount currencyID="EUR">200</cbc:InventoryValueAmount>
<cbc:InventoryValueAmount currencyID="EUR">300</cbc:InventoryValueAmount>
<cbc:InventoryValueAmount currencyID="EUR">750</cbc:InventoryValueAmount>
```

## `cbc:InvoiceTypeCode`

### `@listAgencyID`

```xml
<cbc:InvoiceTypeCode listAgencyID="6">380</cbc:InvoiceTypeCode>
```

### `@listID`

```xml
<cbc:InvoiceTypeCode listID="UN/ECE 1001 Subset">380</cbc:InvoiceTypeCode>
```

## `cbc:InvoicedQuantity`

### `@unitCode`

```xml
<cbc:InvoicedQuantity unitCode="C62">-1</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="C62">1</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="C62">2</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="C62">250</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="KG">100</cbc:InvoicedQuantity>
<cbc:InvoicedQuantity unitCode="KGM">100</cbc:InvoicedQuantity>
```

## `cbc:ItemClassificationCode`

### `@listAgencyID`

```xml
<cbc:ItemClassificationCode listAgencyID="113">12344321</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="113">12344322</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="113">12344325</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="113">32344324</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="2">65434564</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="2">65434565</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="2">65434566</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="2">65434567</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listAgencyID="2">65434568</cbc:ItemClassificationCode>
```

### `@listID`

```xml
<cbc:ItemClassificationCode listID="CPV">65434564</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="CPV">65434565</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="CPV">65434566</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="CPV">65434567</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="CPV">65434568</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="UNSPSC">12344321</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="UNSPSC">12344322</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="UNSPSC">12344325</cbc:ItemClassificationCode>
<cbc:ItemClassificationCode listID="UNSPSC">32344324</cbc:ItemClassificationCode>
```

## `cbc:LatitudeDegreesMeasure`

### `@unitCode`

```xml
<cbc:LatitudeDegreesMeasure unitCode="DD">53.33</cbc:LatitudeDegreesMeasure>
<cbc:LatitudeDegreesMeasure unitCode="DD">53.4</cbc:LatitudeDegreesMeasure>
```

## `cbc:LatitudeMinutesMeasure`

### `@unitCode`

```xml
<cbc:LatitudeMinutesMeasure unitCode="DD">33</cbc:LatitudeMinutesMeasure>
<cbc:LatitudeMinutesMeasure unitCode="DD">49</cbc:LatitudeMinutesMeasure>
```

## `cbc:LeadTimeMeasure`

### `@unitCode`

```xml
<cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
```

## `cbc:LineExtensionAmount`

### `@currencyID`

```xml
<cbc:LineExtensionAmount currencyID="CAD">100.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="DKK">150500.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="DKK">1750.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="DKK">197750.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="DKK">43750.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">-25</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">-3.96</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">120.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">1273</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">1436.5</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">16.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">187.5</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">200.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">23.20</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">4.96</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">7.20</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="EUR">80.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="GBP">100.00</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="SEK">12000</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="SEK">225</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="SEK">6000</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="SEK">6225</cbc:LineExtensionAmount>
<cbc:LineExtensionAmount currencyID="USD">1000.00</cbc:LineExtensionAmount>
```

## `cbc:LineStatusCode`

### `@listAgencyID`

```xml
<cbc:LineStatusCode listAgencyID="UBL">Disputed</cbc:LineStatusCode>
<cbc:LineStatusCode listAgencyID="UBL">NoStatus</cbc:LineStatusCode>
<cbc:LineStatusCode listAgencyID="UBL">Revised</cbc:LineStatusCode>
```

### `@listName`

```xml
<cbc:LineStatusCode listName="Line Status">Disputed</cbc:LineStatusCode>
<cbc:LineStatusCode listName="Line Status">NoStatus</cbc:LineStatusCode>
<cbc:LineStatusCode listName="Line Status">Revised</cbc:LineStatusCode>
```

## `cbc:LoadingLengthMeasure`

### `@unitCode`

```xml
<cbc:LoadingLengthMeasure unitCode="MTR">0</cbc:LoadingLengthMeasure>
<cbc:LoadingLengthMeasure unitCode="MTR">12</cbc:LoadingLengthMeasure>
```

## `cbc:LocationTypeCode`

### `@listAgencyName`

```xml
<cbc:LocationTypeCode listAgencyName="UN">34</cbc:LocationTypeCode>
```

### `@listName`

```xml
<cbc:LocationTypeCode listName="UN/EDIFACT 3227">34</cbc:LocationTypeCode>
```

## `cbc:LongitudeDegreesMeasure`

### `@unitCode`

```xml
<cbc:LongitudeDegreesMeasure unitCode="DD">8.33</cbc:LongitudeDegreesMeasure>
<cbc:LongitudeDegreesMeasure unitCode="DD">8.48</cbc:LongitudeDegreesMeasure>
```

## `cbc:LongitudeMinutesMeasure`

### `@unitCode`

```xml
<cbc:LongitudeMinutesMeasure unitCode="DD">27</cbc:LongitudeMinutesMeasure>
<cbc:LongitudeMinutesMeasure unitCode="DD">49</cbc:LongitudeMinutesMeasure>
```

## `cbc:MaximumDataLossDurationMeasure`

### `@unitCode`

```xml
<cbc:MaximumDataLossDurationMeasure unitCode="HUR">24</cbc:MaximumDataLossDurationMeasure>
```

## `cbc:MaximumIncidentNotificationDurationMeasure`

### `@unitCode`

```xml
<cbc:MaximumIncidentNotificationDurationMeasure unitCode="HUR">4</cbc:MaximumIncidentNotificationDurationMeasure>
```

## `cbc:MeanTimeToRecoverDurationMeasure`

### `@unitCode`

```xml
<cbc:MeanTimeToRecoverDurationMeasure unitCode="HUR">3</cbc:MeanTimeToRecoverDurationMeasure>
```

## `cbc:Measure`

### `@unitCode`

```xml
<cbc:Measure unitCode="CEL">3.00</cbc:Measure>
<cbc:Measure unitCode="CMT">120</cbc:Measure>
<cbc:Measure unitCode="CMT">160</cbc:Measure>
<cbc:Measure unitCode="CMT">60</cbc:Measure>
<cbc:Measure unitCode="CMT">70</cbc:Measure>
<cbc:Measure unitCode="CMT">80</cbc:Measure>
<cbc:Measure unitCode="KG">12.288</cbc:Measure>
<cbc:Measure unitCode="KG">604.8</cbc:Measure>
<cbc:Measure unitCode="KG">604.80000</cbc:Measure>
<cbc:Measure unitCode="KG">774.144</cbc:Measure>
<cbc:Measure unitCode="KG">774.14400</cbc:Measure>
<cbc:Measure unitCode="KG">9.6</cbc:Measure>
<cbc:Measure unitCode="KGM">88</cbc:Measure>
<cbc:Measure unitCode="MTQ">0.336</cbc:Measure>
<cbc:Measure unitCode="MTR">2.44</cbc:Measure>
<cbc:Measure unitCode="MTR">2.6</cbc:Measure>
<cbc:Measure unitCode="MTR">6.1</cbc:Measure>
```

## `cbc:MinimumDownTimeScheduleDurationMeasure`

### `@unitCode`

```xml
<cbc:MinimumDownTimeScheduleDurationMeasure unitCode="DAY">3</cbc:MinimumDownTimeScheduleDurationMeasure>
```

## `cbc:MinimumResponseTimeDurationMeasure`

### `@unitCode`

```xml
<cbc:MinimumResponseTimeDurationMeasure unitCode="SEC">300</cbc:MinimumResponseTimeDurationMeasure>
```

## `cbc:NetNetWeightMeasure`

### `@unitCode`

```xml
<cbc:NetNetWeightMeasure unitCode="KGM">100</cbc:NetNetWeightMeasure>
```

## `cbc:NetVolumeMeasure`

### `@unitCode`

```xml
<cbc:NetVolumeMeasure unitCode="MTQ">0.336000</cbc:NetVolumeMeasure>
<cbc:NetVolumeMeasure unitCode="MTQ">2.235</cbc:NetVolumeMeasure>
```

## `cbc:NetWeightMeasure`

### `@unitCode`

```xml
<cbc:NetWeightMeasure unitCode="KG">604.80000</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure unitCode="KGM">1</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure unitCode="KGM">110</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure unitCode="KGM">3000</cbc:NetWeightMeasure>
<cbc:NetWeightMeasure unitCode="KGM">76.00</cbc:NetWeightMeasure>
```

## `cbc:Note`

### `@languageID`

```xml
<cbc:Note languageID="da-dk">Bestilling af computere</cbc:Note>
<cbc:Note languageID="en">Ordered in our booth at the convention.</cbc:Note>
<cbc:Note languageID="en">This is an example shop purchase receipt</cbc:Note>
```

## `cbc:PackQuantity`

### `@unitCode`

```xml
<cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
<cbc:PackQuantity unitCode="EA">63</cbc:PackQuantity>
```

## `cbc:PackagingTypeCode`

### `@listAgencyID`

```xml
<cbc:PackagingTypeCode listAgencyID="6">TB</cbc:PackagingTypeCode>
```

### `@listID`

```xml
<cbc:PackagingTypeCode listID="UN/ECE rec 21">TB</cbc:PackagingTypeCode>
```

## `cbc:PaidAmount`

### `@currencyID`

```xml
<cbc:PaidAmount currencyID="EUR">25.00</cbc:PaidAmount>
```

## `cbc:PaidCashAmount`

### `@currencyID`

```xml
<cbc:PaidCashAmount currencyID="EUR">30.00</cbc:PaidCashAmount>
```

## `cbc:ParticipantID`

### `@schemeAgencyID`

```xml
<cbc:ParticipantID schemeAgencyID="9">1234567987654</cbc:ParticipantID>
```

### `@schemeID`

```xml
<cbc:ParticipantID schemeID="GLN">1234567987654</cbc:ParticipantID>
```

## `cbc:PayableAmount`

### `@currencyID`

```xml
<cbc:PayableAmount currencyID="CAD">100.00</cbc:PayableAmount>
<cbc:PayableAmount currencyID="DKK">247187.50</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">2000</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">247.55</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">25.00</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">300</cbc:PayableAmount>
<cbc:PayableAmount currencyID="EUR">729</cbc:PayableAmount>
<cbc:PayableAmount currencyID="GBP">100.00</cbc:PayableAmount>
<cbc:PayableAmount currencyID="GBP">107.50</cbc:PayableAmount>
<cbc:PayableAmount currencyID="SEK">6225</cbc:PayableAmount>
<cbc:PayableAmount currencyID="USD">1000.00</cbc:PayableAmount>
```

## `cbc:PayableRoundingAmount`

### `@currencyID`

```xml
<cbc:PayableRoundingAmount currencyID="EUR">0.30</cbc:PayableRoundingAmount>
```

## `cbc:PaymentMeansCode`

### `@listID`

```xml
<cbc:PaymentMeansCode listID="UN/ECE 4461">10</cbc:PaymentMeansCode>
<cbc:PaymentMeansCode listID="UN/ECE 4461">31</cbc:PaymentMeansCode>
```

## `cbc:PerformanceValueQuantity`

### `@unitCode`

```xml
<cbc:PerformanceValueQuantity unitCode="EA">120</cbc:PerformanceValueQuantity>
<cbc:PerformanceValueQuantity unitCode="EA">160</cbc:PerformanceValueQuantity>
```

## `cbc:PostEventNotificationDurationMeasure`

### `@unitCode`

```xml
<cbc:PostEventNotificationDurationMeasure unitCode="MIN">10</cbc:PostEventNotificationDurationMeasure>
```

## `cbc:PrepaidAmount`

### `@currencyID`

```xml
<cbc:PrepaidAmount currencyID="EUR">1000</cbc:PrepaidAmount>
```

## `cbc:PriceAmount`

### `@currencyID`

```xml
<cbc:PriceAmount currencyID="DKK">1250.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="DKK">4300.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="DKK">50.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">0.75</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">12.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">120.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">1273</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">16.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">2.48</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">25</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">3.96</cbc:PriceAmount>
<cbc:PriceAmount currencyID="EUR">40.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="GBP">1.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="GBP">100.00</cbc:PriceAmount>
<cbc:PriceAmount currencyID="SEK">15</cbc:PriceAmount>
<cbc:PriceAmount currencyID="SEK">50</cbc:PriceAmount>
<cbc:PriceAmount currencyID="USD">10.00</cbc:PriceAmount>
```

## `cbc:ProfileID`

### `@schemeAgencyID`

```xml
<cbc:ProfileID schemeAgencyID="320">Procurement-QuoSim-1.0</cbc:ProfileID>
<cbc:ProfileID schemeAgencyID="BII">urn:www.cenbii.eu:profile:BII01:ver1.0</cbc:ProfileID>
<cbc:ProfileID schemeAgencyID="BII">urn:www.cenbii.eu:profile:BIIXYZ:ver1.0</cbc:ProfileID>
```

### `@schemeID`

```xml
<cbc:ProfileID schemeID="Profile">urn:www.cenbii.eu:profile:BII01:ver1.0</cbc:ProfileID>
<cbc:ProfileID schemeID="Profile">urn:www.cenbii.eu:profile:BIIXYZ:ver1.0</cbc:ProfileID>
<cbc:ProfileID schemeID="urn:oioubl:id:profileid-1.2">Procurement-QuoSim-1.0</cbc:ProfileID>
```

## `cbc:Quantity`

### `@unitCode`

```xml
<cbc:Quantity unitCode="C62">15</cbc:Quantity>
<cbc:Quantity unitCode="CT">63.000</cbc:Quantity>
<cbc:Quantity unitCode="EA">1</cbc:Quantity>
<cbc:Quantity unitCode="EA">35</cbc:Quantity>
<cbc:Quantity unitCode="H87">1</cbc:Quantity>
<cbc:Quantity unitCode="H87">2</cbc:Quantity>
<cbc:Quantity unitCode="KG">100</cbc:Quantity>
<cbc:Quantity unitCode="KG">90</cbc:Quantity>
<cbc:Quantity unitCode="KGM">100</cbc:Quantity>
<cbc:Quantity unitCode="KGM">150.00</cbc:Quantity>
<cbc:Quantity unitCode="KGM">20</cbc:Quantity>
<cbc:Quantity unitCode="KGM">90</cbc:Quantity>
<cbc:Quantity unitCode="LTR">120</cbc:Quantity>
<cbc:Quantity unitCode="LTR">240</cbc:Quantity>
<cbc:Quantity unitCode="NAR">0</cbc:Quantity>
<cbc:Quantity unitCode="NAR">10</cbc:Quantity>
<cbc:Quantity unitCode="NAR">15</cbc:Quantity>
<cbc:Quantity unitCode="NAR">150</cbc:Quantity>
<cbc:Quantity unitCode="NAR">20</cbc:Quantity>
<cbc:Quantity unitCode="NAR">200</cbc:Quantity>
<cbc:Quantity unitCode="NAR">3</cbc:Quantity>
<cbc:Quantity unitCode="NAR">5</cbc:Quantity>
<cbc:Quantity unitCode="NAR">50</cbc:Quantity>
<cbc:Quantity unitCode="NAR">8</cbc:Quantity>
<cbc:Quantity unitCode="NAR">80</cbc:Quantity>
<cbc:Quantity unitCode="NIU">35</cbc:Quantity>
```

## `cbc:ReceivedQuantity`

### `@unitCode`

```xml
<cbc:ReceivedQuantity unitCode="KG">90</cbc:ReceivedQuantity>
<cbc:ReceivedQuantity unitCode="KGM">90</cbc:ReceivedQuantity>
```

## `cbc:RoleCode`

### `@listAgencyID`

```xml
<cbc:RoleCode listAgencyID="6">BN</cbc:RoleCode>
<cbc:RoleCode listAgencyID="6">RP</cbc:RoleCode>
```

### `@listID`

```xml
<cbc:RoleCode listID="UN/ECE 3139">BN</cbc:RoleCode>
<cbc:RoleCode listID="UN/ECE 3139">RP</cbc:RoleCode>
```

## `cbc:ShortQuantity`

### `@unitCode`

```xml
<cbc:ShortQuantity unitCode="KG">10</cbc:ShortQuantity>
<cbc:ShortQuantity unitCode="KGM">10</cbc:ShortQuantity>
```

## `cbc:SizeTypeCode`

### `@listAgencyID`

```xml
<cbc:SizeTypeCode listAgencyID="5">22G1</cbc:SizeTypeCode>
```

### `@listID`

```xml
<cbc:SizeTypeCode listID="ISO 6346">22G1</cbc:SizeTypeCode>
```

## `cbc:SourceValueMeasure`

### `@unitCode`

```xml
<cbc:SourceValueMeasure unitCode="KGM">2.1</cbc:SourceValueMeasure>
```

## `cbc:TargetInventoryQuantity`

### `@unitCode`

```xml
<cbc:TargetInventoryQuantity unitCode="KGM">20</cbc:TargetInventoryQuantity>
```

## `cbc:TaxAmount`

### `@currencyID`

```xml
<cbc:TaxAmount currencyID="EUR">-0.396</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">0</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">0.00</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">0.1</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">0.496</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">1.80</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">254.6</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">292.1</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">292.20</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">37.5</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">4.00</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">42.55</cbc:TaxAmount>
<cbc:TaxAmount currencyID="EUR">5.80</cbc:TaxAmount>
<cbc:TaxAmount currencyID="GBP">17.50</cbc:TaxAmount>
<cbc:TaxAmount currencyID="SEK">100</cbc:TaxAmount>
```

## `cbc:TaxExclusiveAmount`

### `@currencyID`

```xml
<cbc:TaxExclusiveAmount currencyID="DKK">49437.50</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount currencyID="EUR">1436.5</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount currencyID="EUR">205.00</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount currencyID="EUR">23.20</cbc:TaxExclusiveAmount>
<cbc:TaxExclusiveAmount currencyID="GBP">90.00</cbc:TaxExclusiveAmount>
```

## `cbc:TaxExemptionReasonCode`

### `@listAgencyID`

```xml
<cbc:TaxExemptionReasonCode listAgencyID="ZZZ">AAM</cbc:TaxExemptionReasonCode>
```

### `@listID`

```xml
<cbc:TaxExemptionReasonCode listID="CWA 15577">AAM</cbc:TaxExemptionReasonCode>
```

## `cbc:TaxInclusiveAmount`

### `@currencyID`

```xml
<cbc:TaxInclusiveAmount currencyID="DKK">247187.50</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">1.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">1729</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">20.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">247.55</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">29.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">5.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">6.00</cbc:TaxInclusiveAmount>
<cbc:TaxInclusiveAmount currencyID="EUR">9.00</cbc:TaxInclusiveAmount>
```

## `cbc:TaxInclusiveLineExtensionAmount`

### `@currencyID`

```xml
<cbc:TaxInclusiveLineExtensionAmount currencyID="EUR">20.00</cbc:TaxInclusiveLineExtensionAmount>
<cbc:TaxInclusiveLineExtensionAmount currencyID="EUR">9.00</cbc:TaxInclusiveLineExtensionAmount>
```

## `cbc:TaxInclusivePriceAmount`

### `@currencyID`

```xml
<cbc:TaxInclusivePriceAmount currencyID="EUR">15.00</cbc:TaxInclusivePriceAmount>
<cbc:TaxInclusivePriceAmount currencyID="EUR">20.00</cbc:TaxInclusivePriceAmount>
```

## `cbc:TaxableAmount`

### `@currencyID`

```xml
<cbc:TaxableAmount currencyID="EUR">-25</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">1</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">1.00</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">1460.5</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">16.00</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">202.50</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">23.20</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="EUR">7.20</cbc:TaxableAmount>
<cbc:TaxableAmount currencyID="GBP">100.00</cbc:TaxableAmount>
```

## `cbc:ThresholdQuantity`

### `@unitCode`

```xml
<cbc:ThresholdQuantity unitCode="KGM">120000</cbc:ThresholdQuantity>
```

## `cbc:TotalBalanceAmount`

### `@currencyID`

```xml
<cbc:TotalBalanceAmount currencyID="GBP">-107.50</cbc:TotalBalanceAmount>
```

## `cbc:TotalCreditAmount`

### `@currencyID`

```xml
<cbc:TotalCreditAmount currencyID="GBP">0.00</cbc:TotalCreditAmount>
<cbc:TotalCreditAmount currencyID="GBP">107.50</cbc:TotalCreditAmount>
```

## `cbc:TotalDebitAmount`

### `@currencyID`

```xml
<cbc:TotalDebitAmount currencyID="GBP">0.00</cbc:TotalDebitAmount>
<cbc:TotalDebitAmount currencyID="GBP">107.50</cbc:TotalDebitAmount>
```

## `cbc:TotalGoodsItemQuantity`

### `@unitCode`

```xml
<cbc:TotalGoodsItemQuantity unitCode="EA">2</cbc:TotalGoodsItemQuantity>
```

## `cbc:TotalInvoiceAmount`

### `@currencyID`

```xml
<cbc:TotalInvoiceAmount currencyID="DKK">44250.00</cbc:TotalInvoiceAmount>
<cbc:TotalInvoiceAmount currencyID="EUR">10500.00</cbc:TotalInvoiceAmount>
```

## `cbc:TotalPackageQuantity`

### `@unitCode`

```xml
<cbc:TotalPackageQuantity unitCode="EA">1</cbc:TotalPackageQuantity>
```

## `cbc:TotalPaymentAmount`

### `@currencyID`

```xml
<cbc:TotalPaymentAmount currencyID="GBP">107.50</cbc:TotalPaymentAmount>
```

## `cbc:TotalTaxAmount`

### `@currencyID`

```xml
<cbc:TotalTaxAmount currencyID="DKK">10937.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="DKK">37625.00</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="DKK">437.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="GBP">17.50</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="SEK">10</cbc:TotalTaxAmount>
<cbc:TotalTaxAmount currencyID="SEK">20</cbc:TotalTaxAmount>
```

## `cbc:TotalTransportHandlingUnitQuantity`

### `@unitCode`

```xml
<cbc:TotalTransportHandlingUnitQuantity unitCode="EA">1</cbc:TotalTransportHandlingUnitQuantity>
```

## `cbc:TransportEquipmentTypeCode`

### `@listAgencyID`

```xml
<cbc:TransportEquipmentTypeCode listAgencyID="6">CN</cbc:TransportEquipmentTypeCode>
```

### `@listID`

```xml
<cbc:TransportEquipmentTypeCode listID="UN/ECE 8053">CN</cbc:TransportEquipmentTypeCode>
```

## `cbc:TransportHandlingUnitTypeCode`

### `@listAgencyName`

```xml
<cbc:TransportHandlingUnitTypeCode listAgencyName="United Nations Economic Commission for Europe">PA</cbc:TransportHandlingUnitTypeCode>
```

### `@listID`

```xml
<cbc:TransportHandlingUnitTypeCode listID="TRED 8053">PA</cbc:TransportHandlingUnitTypeCode>
```

## `cbc:TransportModeCode`

### `@listAgencyID`

```xml
<cbc:TransportModeCode listAgencyID="6">3</cbc:TransportModeCode>
<cbc:TransportModeCode listAgencyID="6">4</cbc:TransportModeCode>
```

### `@listID`

```xml
<cbc:TransportModeCode listID="UN/ECE rec 16">3</cbc:TransportModeCode>
<cbc:TransportModeCode listID="UN/ECE rec 16">4</cbc:TransportModeCode>
```

### `@name`

```xml
<cbc:TransportModeCode name="Sea">1</cbc:TransportModeCode>
```

## `cbc:ValueAmount`

### `@currencyID`

```xml
<cbc:ValueAmount currencyID="DKK">10500.00</cbc:ValueAmount>
<cbc:ValueAmount currencyID="USD">1000.00</cbc:ValueAmount>
<cbc:ValueAmount currencyID="USD">250</cbc:ValueAmount>
```

## `cbc:ValueMeasure`

### `@unitCode`

```xml
<cbc:ValueMeasure unitCode="KGM">0.2</cbc:ValueMeasure>
```

## `cbc:ValueQuantity`

### `@unitCode`

```xml
<cbc:ValueQuantity unitCode="CT">63.000</cbc:ValueQuantity>
<cbc:ValueQuantity unitCode="KG">604.8</cbc:ValueQuantity>
<cbc:ValueQuantity unitCode="KG">774.144</cbc:ValueQuantity>
```

## `cbc:VarianceQuantity`

### `@unitCode`

```xml
<cbc:VarianceQuantity unitCode="KGM">20</cbc:VarianceQuantity>
```

## `cbc:WeighingMethodCode`

### `@listAgencyID`

```xml
<cbc:WeighingMethodCode listAgencyID="54">SM1</cbc:WeighingMethodCode>
```

### `@listID`

```xml
<cbc:WeighingMethodCode listID="IMO SOLAS">SM1</cbc:WeighingMethodCode>
```

## `cbc:WeightStatementTypeCode`

### `@listAgencyID`

```xml
<cbc:WeightStatementTypeCode listAgencyID="6">749</cbc:WeightStatementTypeCode>
```

### `@listID`

```xml
<cbc:WeightStatementTypeCode listID="UN/ECE 1001">749</cbc:WeightStatementTypeCode>
```

### `@listVersionID`

```xml
<cbc:WeightStatementTypeCode listVersionID="d16a">749</cbc:WeightStatementTypeCode>
```
