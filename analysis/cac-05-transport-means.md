# UBL Element Reference — Transport Means & Operations

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **13** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [TransportMeansType](#TransportMeansType)
  - [AirTransportType](#AirTransportType)
  - [MaritimeTransportType](#MaritimeTransportType)
  - [RailTransportType](#RailTransportType)
  - [RoadTransportType](#RoadTransportType)
  - [ShipmentStageType](#ShipmentStageType)
  - [TransportationServiceType](#TransportationServiceType)
  - [TransportationSegmentType](#TransportationSegmentType)
  - [TransportScheduleType](#TransportScheduleType)
  - [TransportEventType](#TransportEventType)
  - [TransportExecutionTermsType](#TransportExecutionTermsType)
  - [TransportEquipmentType](#TransportEquipmentType)
  - [TransportEquipmentSealType](#TransportEquipmentSealType)

---

## cac Elements — Transport Means & Operations

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)