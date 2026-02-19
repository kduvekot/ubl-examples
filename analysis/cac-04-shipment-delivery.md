# UBL Element Reference — Shipment, Goods & Delivery

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **15** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [ShipmentType](#ShipmentType)
  - [ConsignmentType](#ConsignmentType)
  - [GoodsItemType](#GoodsItemType)
  - [GoodsItemPassportCounterfoilType](#GoodsItemPassportCounterfoilType)
  - [TransportHandlingUnitType](#TransportHandlingUnitType)
  - [PackageType](#PackageType)
  - [DeliveryType](#DeliveryType)
  - [DeliveryTermsType](#DeliveryTermsType)
  - [DeliveryChannelType](#DeliveryChannelType)
  - [DespatchType](#DespatchType)
  - [DespatchLineType](#DespatchLineType)
  - [PickupType](#PickupType)
  - [InstructionForReturnsLineType](#InstructionForReturnsLineType)
  - [TemperatureType](#TemperatureType)
  - [VerifiedGrossMassType](#VerifiedGrossMassType)

---

## cac Elements — Shipment, Goods & Delivery

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)