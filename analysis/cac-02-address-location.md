# UBL Element Reference — Address, Location & Communication

Part of the [UBL Element Reference](./ubl-element-reference.md). Contains **8** aggregate component types used across UBL 2.0–2.5 example documents.

## Types in this section

  - [AddressType](#AddressType)
  - [AddressLineType](#AddressLineType)
  - [CountryType](#CountryType)
  - [LanguageType](#LanguageType)
  - [LocationType](#LocationType)
  - [LocationCoordinateType](#LocationCoordinateType)
  - [SocialMediaProfileType](#SocialMediaProfileType)
  - [WebSiteType](#WebSiteType)

---

## cac Elements — Address, Location & Communication

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

---

[↑ Back to UBL Element Reference index](./ubl-element-reference.md)