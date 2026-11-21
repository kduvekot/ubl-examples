# Delivery Note: Lisavu Cotton Farm to Selanu Cotton Ginnery

*Example 3 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Delivery Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DELIVERY-NOTE-SCHEMA)*

The farm delivers a trailer of seed cotton at the gin and confirms what it delivered.

[The XML file](03-DeliveryNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; the document type DeliveryNote first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:delivery-note:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Delivery note". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **SCG-TX-26-0024**  
  The collaboration this document belongs to: the ginnery's purchase of the farm's seed cotton. Selanu Cotton Ginnery started it and gave it this identifier, which every document of it repeats.
- `ID` = **1/2026**  
  The farm's delivery note number.
- `UUID` = **7a1d8c4c-64bb-5f76-ad72-a09687f8943f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-08**  
  Written when the last of the three trailer loads was weighed at the gin.
- `IssueTime` = **14:29:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **Tasela vaputa tuote, fipavi momai tikesa lelala 6, 7 tofami 8 April.** (languageID `qal`)  
  The note in Lisavan, the sender's language: What was delivered, and when.
- `Note` = **Three trailer loads, weighed at the gin on 6, 7 and 8 April.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: What was delivered, and when.
- `LineCountNumeric` = **1**  
  One line.

### Order Reference

Inside `OrderReference`:

- `ID` = **SCG-SEASON-2026/03**  
  The call-off under the season agreement.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **SCG-WB-26-0311**  
  The weighbridge ticket.
- `DocumentType` = **Weighbridge ticket**  
  The kind of document referred to, the ginnery's weighbridge ticket, in words: no list has an exact code for it.

### Signature

Inside `Signature`:

- `ID` = **LCF-SIG-26-DN**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **LFR-0412** (schemeID `urn:ubl-examples:world:XL:farm-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lisavu Cotton Farm**  
  A party referred to from another party's details: its identifier and name are enough.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **LFR-0412** (schemeID `urn:ubl-examples:world:XL:farm-register`)  
  The party's preferred identifier: its number in the Farm register of Lisavu; as Lisavu Cotton Farm gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; as Lisavu Cotton Farm gives it.
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: kopele.
- `Party/PostalAddress/ID` = **85779006** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Lisavu Cotton Farm gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Lisavu Cotton Farm gives it.
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Lisavu Cotton Farm gives it.
- `Party/PostalAddress/Description` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  How to find the farm, which has no house number on a street. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/District` = **North coast**  
  The district of the island, used to find a farm off the main roads. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PostalAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PostalAddress/LocationCoordinate/LatitudeDegreesMeasure` = **32** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PostalAddress/LocationCoordinate/LatitudeMinutesMeasure` = **44.86** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PostalAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PostalAddress/LocationCoordinate/LongitudeDegreesMeasure` = **2** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PostalAddress/LocationCoordinate/LongitudeMinutesMeasure` = **16.51** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PostalAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PhysicalLocation/Description` = **The cotton fields**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **32** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **44.86** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **2** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **16.51** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/Contact/Name` = **Farm office**  
  The party's main desk, which handles this document; as Lisavu Cotton Farm gives it.
- `Party/Contact/JobTitle` = **Farm manager**  
  The job of the person who answers at the desk; as Lisavu Cotton Farm gives it.
- `Party/Contact/Department` = **Management**  
  The department the desk belongs to; as Lisavu Cotton Farm gives it.
- `Party/Contact/Telephone` = **+999 3 724 6676**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Lisavu Cotton Farm gives it.
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  The contact's e-mail address; as Lisavu Cotton Farm gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lisavu Cotton Farm gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:LFR-0412** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Farm register of Lisavu; as Lisavu Cotton Farm gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. As Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Gin yard**  
  The party's gin yard desk: the desk for its role in this document (it receives the goods); as Selanu Cotton Ginnery gives it.
- `Party/Contact/JobTitle` = **Yard foreman**  
  The job of the person who answers at the desk; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Department` = **Ginning**  
  The department the desk belongs to; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Telephone` = **+999 3 721 0486**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Cotton Ginnery gives it.
- `Party/Contact/ElectronicMail` = **yard@selanuginnery.example**  
  The contact's e-mail address; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Cotton Ginnery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **LFR-0412** (schemeID `urn:ubl-examples:world:XL:farm-register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **LCF-SH-26-03**  
  The farm's three trailer loads.
- `GrossWeightMeasure` = **20400** (unitCode `KGM`)  
  The cotton and the empty trailers' tare of 2,400 kg, as weighed.
- `Delivery/ActualDeliveryDate` = **2026-04-08**  
  At the gin: the last of the three loads, after those of 6 and 7 April.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The only line.
- `DeliveredQuantity` = **18000** (unitCode `KGM`)  
  Weighed at the gin's weighbridge.
- `OrderLineReference/LineID` = **1**  
  The line of the season agreement between farm and ginnery under which the cotton is delivered.
- `Item/Description` = **Tekapa tanema tiloluti, hivile nipupe, tasepaha pisosi ninote vaputa.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `Item/Description` = **Cotton as harvested, not ginned, delivered loose by trailer.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Votike tekapa** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `Item/Name` = **Seed cotton** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **LCF-SC**  
  The seller's own item number; as Lisavu Cotton Farm describes the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DeliveryNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:DeliveryNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:delivery-note:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SCG-TX-26-0024</cbc:ProfileExecutionID>
  <cbc:ID>1/2026</cbc:ID>
  <cbc:UUID>7a1d8c4c-64bb-5f76-ad72-a09687f8943f</cbc:UUID>
  <cbc:IssueDate>2026-04-08</cbc:IssueDate>
  <cbc:IssueTime>14:29:00+00:00</cbc:IssueTime>
  <cbc:Note languageID="qal">Tasela vaputa tuote, fipavi momai tikesa lelala 6, 7 tofami 8 April.</cbc:Note>
  <cbc:Note languageID="en-XL">Three trailer loads, weighed at the gin on 6, 7 and 8 April.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>SCG-SEASON-2026/03</cbc:ID>
  </cac:OrderReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>SCG-WB-26-0311</cbc:ID>
    <cbc:DocumentType>Weighbridge ticket</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>LCF-SIG-26-DN</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:farm-register">LFR-0412</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:farm-register">LFR-0412</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">85779006</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Sifatofu Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Plantation Road</cbc:StreetName>
        <cbc:Description>Farm track off Plantation Road at kilometre 4, past the cotton fields.</cbc:Description>
        <cbc:CityName languageID="qal">Kefalasa</cbc:CityName>
        <cbc:CityName languageID="en-XL">Lintwell</cbc:CityName>
        <cbc:District>North coast</cbc:District>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">32</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">44.86</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">2</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">16.51</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>The cotton fields</cbc:Description>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">32</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">44.86</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">2</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">16.51</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:Contact>
        <cbc:Name>Farm office</cbc:Name>
        <cbc:JobTitle>Farm manager</cbc:JobTitle>
        <cbc:Department>Management</cbc:Department>
        <cbc:Telephone>+999 3 724 6676</cbc:Telephone>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:LFR-0412</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
        <cbc:BuildingNumber>42</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
        <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Gin yard</cbc:Name>
        <cbc:JobTitle>Yard foreman</cbc:JobTitle>
        <cbc:Department>Ginning</cbc:Department>
        <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
        <cbc:ElectronicMail>yard@selanuginnery.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:farm-register">LFR-0412</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>LCF-SH-26-03</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">20400</cbc:GrossWeightMeasure>
    <cac:Delivery>
      <cbc:ActualDeliveryDate>2026-04-08</cbc:ActualDeliveryDate>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DeliveredQuantity unitCode="KGM">18000</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description languageID="qal">Tekapa tanema tiloluti, hivile nipupe, tasepaha pisosi ninote vaputa.</cbc:Description>
      <cbc:Description languageID="en-XL">Cotton as harvested, not ginned, delivered loose by trailer.</cbc:Description>
      <cbc:Name languageID="qal">Votike tekapa</cbc:Name>
      <cbc:Name languageID="en-XL">Seed cotton</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>LCF-SC</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:DespatchLine>
</DeliveryNote>
```
