# Delivery Note: Lisavu Cotton Farm to Selanu Cotton Ginnery

*Example 3 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Delivery Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DELIVERY-NOTE-SCHEMA)*

The farm delivers a trailer of seed cotton at the gin and confirms what it delivered.

[The XML file](03-DeliveryNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); the document type DeliveryNote first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:delivery-note:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Delivery note". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LCF-DN-26-0193**  
  The farm's delivery note number.
- `UUID` = **7a1d8c4c-64bb-5f76-ad72-a09687f8943f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-05**  
  The day the trailers were weighed at the gin.
- `IssueTime` = **14:29:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Tasela vaputa tuote, fipavi momai tikesa.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): What was delivered.
- `Note` = **Three trailer loads, weighed at the gin.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: What was delivered.
- `LineCountNumeric` = **1**  
  One line.

### Order Reference

Inside `OrderReference`:

- `ID` = **SCG-SEASON-2026/03**  
  The call-off under the season agreement.

### Project Reference

Inside `ProjectReference`:

- `ID` = **SCC-COTTON-QUALITY-26**  
  The chamber's cotton quality programme, under which the farm's seed cotton is classed.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **SCG-WB-26-0311**  
  The weighbridge ticket.
- `DocumentType` = **Weighbridge ticket**  
  The kind of document referred to, the ginnery's weighbridge ticket, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Signature

Inside `Signature`:

- `ID` = **LCF-SIG-26-DN**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lisavu Cotton Farm**  
  A party referred to from another party's details: its identifier and name are enough.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **85779006** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/Description` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  How to find the farm, which has no house number on a street. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/District` = **North coast**  
  The district of the island, used to find a farm off the main roads. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/AddressLine/Line` = **Sifatofu Natii / Plantation Road**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **North coast**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **Selanu / Port Wrenfield**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PostalAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PostalAddress/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LatitudeMinutesMeasure` = **58.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PostalAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PostalAddress/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LongitudeMinutesMeasure` = **7.80** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PostalAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PhysicalLocation/Description` = **The cotton fields**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/InformationURI` = **https://www.lisavufarm.example**  
  Where to find more about the place.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **58.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **7.80** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/Contact/Name` = **Farm office**  
  The party's main desk, which handles this document; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/JobTitle` = **Farm manager**  
  The job of the person who answers at the desk; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Department` = **Management**  
  The department the desk belongs to; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 724 2544**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42544** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lisavu Cotton Farm (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Gin yard**  
  The party's gin yard desk: the desk for its role in this document (it receives the goods); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/JobTitle` = **Yard foreman**  
  The job of the person who answers at the desk; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Department` = **Ginning**  
  The department the desk belongs to; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 721 2681**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/ElectronicMail` = **yard@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Originator Customer Party

Inside `OriginatorCustomerParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Beneficiary Party

Inside `BeneficiaryParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Shipment

Inside `Shipment`:

- `ID` = **LCF-SH-26-03**  
  The farm's three trailer loads.
- `GrossWeightMeasure` = **20400** (unitCode `KGM`)  
  The cotton and the empty trailers' tare of 2,400 kg, as weighed.
- `Delivery/ActualDeliveryDate` = **2026-02-05**  
  At the gin.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The only line.
- `DeliveredQuantity` = **18000** (unitCode `KGM`)  
  Weighed at the gin's weighbridge.
- `OrderLineReference/LineID` = **1**  
  The line of the season agreement between farm and ginnery under which the cotton is delivered.
- `Item/Description` = **Tekapa tanema tiloluti, hivile nipupe, tasepaha pisosi ninote vaputa.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Description` = **Cotton as harvested, not ginned, delivered loose by trailer.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Name` = **Votike tekapa** (languageID `qal`)  
  The item's name in Lisavan, the seller's language; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Name` = **Seed cotton** (languageID `en-XL`)  
  The item's name in English, the working language between the countries; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/SellersItemIdentification/ID` = **LCF-SC**  
  The seller's own item number; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Where the item was produced; item seed-cotton of Lisavu Cotton Farm (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item seed-cotton of Lisavu Cotton Farm (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `Item/CommodityClassification/ItemClassificationCode` = **01921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item seed-cotton of Lisavu Cotton Farm (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01921 = Cotton, whether or not ginned.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DeliveryNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:DeliveryNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:delivery-note:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LCF-DN-26-0193</cbc:ID>
  <cbc:UUID>7a1d8c4c-64bb-5f76-ad72-a09687f8943f</cbc:UUID>
  <cbc:IssueDate>2026-02-05</cbc:IssueDate>
  <cbc:IssueTime>14:29:00</cbc:IssueTime>
  <cbc:Note languageID="qal">Tasela vaputa tuote, fipavi momai tikesa.</cbc:Note>
  <cbc:Note languageID="en-XL">Three trailer loads, weighed at the gin.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>SCG-SEASON-2026/03</cbc:ID>
  </cac:OrderReference>
  <cac:ProjectReference>
    <cbc:ID>SCC-COTTON-QUALITY-26</cbc:ID>
  </cac:ProjectReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>SCG-WB-26-0311</cbc:ID>
    <cbc:DocumentType>Weighbridge ticket</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>LCF-SIG-26-DN</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
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
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:District>North coast</cbc:District>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:AddressLine>
          <cbc:Line>Sifatofu Natii / Plantation Road</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Farm track off Plantation Road at kilometre 4, past the cotton fields.</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>North coast</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Selanu / Port Wrenfield</cbc:Line>
        </cac:AddressLine>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">58.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">7.80</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>The cotton fields</cbc:Description>
        <cbc:InformationURI>https://www.lisavufarm.example</cbc:InformationURI>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">58.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">7.80</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:Contact>
        <cbc:Name>Farm office</cbc:Name>
        <cbc:JobTitle>Farm manager</cbc:JobTitle>
        <cbc:Department>Management</cbc:Department>
        <cbc:Telephone>+999 3 724 2544</cbc:Telephone>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42544</cbc:ElectronicAddressID>
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
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Gin yard</cbc:Name>
        <cbc:JobTitle>Yard foreman</cbc:JobTitle>
        <cbc:Department>Ginning</cbc:Department>
        <cbc:Telephone>+999 3 721 2681</cbc:Telephone>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:OriginatorCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:OriginatorCustomerParty>
  <cac:BeneficiaryParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
  </cac:BeneficiaryParty>
  <cac:Shipment>
    <cbc:ID>LCF-SH-26-03</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">20400</cbc:GrossWeightMeasure>
    <cac:Delivery>
      <cbc:ActualDeliveryDate>2026-02-05</cbc:ActualDeliveryDate>
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
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">520100</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01921</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:DespatchLine>
</DeliveryNote>
```
