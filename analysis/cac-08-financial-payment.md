# UBL Element Reference — Financial, Payment & Tax

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **16** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [PaymentType](#PaymentType)
  - [PaymentMeansType](#PaymentMeansType)
  - [PaymentTermsType](#PaymentTermsType)
  - [FinancialAccountType](#FinancialAccountType)
  - [FinancialInstitutionType](#FinancialInstitutionType)
  - [CashRegisterType](#CashRegisterType)
  - [ExchangeRateType](#ExchangeRateType)
  - [TaxTotalType](#TaxTotalType)
  - [TaxSubtotalType](#TaxSubtotalType)
  - [TaxCategoryType](#TaxCategoryType)
  - [TaxSchemeType](#TaxSchemeType)
  - [AllowanceChargeType](#AllowanceChargeType)
  - [MonetaryTotalType](#MonetaryTotalType)
  - [PriceType](#PriceType)
  - [PeriodType](#PeriodType)
  - [TransactionConditionsType](#TransactionConditionsType)

---

## cac Elements — Financial, Payment & Tax

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)