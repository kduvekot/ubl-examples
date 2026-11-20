# Weight Statement: Rinova Recovery to Valdara Industries

*Example 4 of the flow "Production waste to recovery (domestic, Urvania)" · [Weight Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WEIGHT-STATEMENT-SCHEMA)*

Rinova's weighbridge ticket of the load: the truck weighed full on arrival and empty after unloading, so that the difference is the waste received. Rinova gives it to the producer, who pays by the net tonne, and cites it in its movement report and its invoice.

[The XML file](04-WeightStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:weight-statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Weight statement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900043338**  
  The collaboration this document belongs to: the movement of Valdara's waste to Rinova Recovery. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0019**  
  The weighbridge ticket number.
- `UUID` = **389662b4-907e-55fc-9944-1cf97ccc36c8**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Printed after the second weighing.
- `IssueTime` = **10:50:00-01:00**  
  When the empty truck left the weighbridge; in the issuer's local time, with its offset from UTC.
- `WeightStatementTypeCode` = **WEIGHBRIDGE** (listID `urn:ubl-examples:world:codelist:WeightStatementTypeCode`)  
  A weighbridge ticket: the vehicle and its load weighed. The code is from the Trade Accord's weight statement type list: WEIGHBRIDGE = Weighbridge ticket.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Rinova Recovery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:13362** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rinova Recovery gives it.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; as Rinova Recovery gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Rinova Recovery gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Rinova Recovery gives it.
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Rinova Recovery gives it.
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. As Rinova Recovery gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). As Rinova Recovery gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Rinova Recovery gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); as Rinova Recovery gives it.
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; as Rinova Recovery gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Rinova Recovery gives it.
- `Contact/Telephone` = **+999 1 041 697 6856**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Rinova Recovery gives it.
- `Contact/ElectronicMail` = **logistics@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Rinova Recovery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rinova Recovery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Rinova Recovery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); as Valdara Industries gives it.
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **logistics@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Weighing Party

Inside `WeighingParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rinova Recovery**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **7400043504**  
  The load weighed.
- `NetWeightMeasure` = **22900** (unitCode `KGM`)  
  The waste: the truck full less the truck empty, 38,200 kg − 15,300 kg.
- `Consignment/ID` = **7300043504**  
  The consignment weighed.
- `Consignment/TotalPackagesQuantity` = **54**  
  54 bales on the truck, in two layers.
- `GoodsItem/ID` = **1**  
  The only goods item: one kind of waste.
- `GoodsItem/Description` = **Used polyethylene stretch film and film offcuts, baled**  
  What the waste is, in words.
- `GoodsItem/HazardousRiskIndicator` = **false**  
  Polyethylene film is not hazardous waste: its entry in the waste list has no asterisk.
- `GoodsItem/Item/Description` = **Used polyethylene stretch film and film offcuts, baled**  
  The waste, in words.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **150102** (listID `urn:ubl-examples:world:XU:codelist:WasteCode`)  
  The waste by its entry in Urvania's waste list, numbered after the European List of Waste: the film comes from the packaging of the parts and materials the factory receives and from the wrapping of its own pallets, and no chapter for the factory's activity (metal working and coating, chapters 08, 11 and 12) has an entry for packaging, so the list's rule sends it to chapter 15: 15 01 02 plastic packaging. The code is from Urvania's national waste list list: 150102 = Plastic packaging.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. Loose film would fill the trailer long before its payload; pressed into bales of about 1.2 × 0.8 × 1.0 m and 425 kg, two layers high, a load reaches the weight limit first. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Steel baling wire**  
  What holds a bale together.
- `ShipmentStage/ID` = **1**  
  The one road leg, across Ferrano.
- `ShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `ShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `ShipmentStage/TransportMeans/TransportMeansTypeCode` = **395** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tractor unit 07 with curtain-side trailer; the fleet of Trasvia Haulage. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 395 = Truck, with trailer.
- `ShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 KT** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Trasvia Haulage. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `ShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **UR 4160 TR** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `ShipmentStage/TransportMeans/OwnerParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/TransportMeans/OwnerParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The first weighing: the truck with its load, on arrival. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/MeasurementDimension/Measure` = **38200** (unitCode `KGM`)  
  Within the Accord's 40,000 kg for a combination.
- `ShipmentStage/TransportMeans/MeasurementDimension/Description` = **Loaded, at 10:07**  
  When it was weighed.
- `ShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **TAREWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The second weighing: the same truck after unloading. The code is from the Trade Accord's dimension attribute list: TAREWEIGHT = Tare weight. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/MeasurementDimension/Measure` = **15300** (unitCode `KGM`)  
  The tractor about 7,800 kg and the trailer about 7,500 kg.
- `ShipmentStage/TransportMeans/MeasurementDimension/Description` = **Empty, at 10:46**  
  When it was weighed.
- `ShipmentStage/DriverPerson/ID` = **XU-DL-0417722**  
  The number of the driving licence.
- `ShipmentStage/DriverPerson/FirstName` = **Ilario**  
  The driver, who took the ticket.
- `ShipmentStage/DriverPerson/FamilyName` = **Bencetti**  
  The family name.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<WeightStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:WeightStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:weight-statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900043338</cbc:ProfileExecutionID>
  <cbc:ID>26-0019</cbc:ID>
  <cbc:UUID>389662b4-907e-55fc-9944-1cf97ccc36c8</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>10:50:00-01:00</cbc:IssueTime>
  <cbc:WeightStatementTypeCode listID="urn:ubl-examples:world:codelist:WeightStatementTypeCode">WEIGHBRIDGE</cbc:WeightStatementTypeCode>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:13362</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202983340277</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 697 6856</cbc:Telephone>
      <cbc:ElectronicMail>logistics@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>logistics@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:WeighingParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:WeighingParty>
  <cac:Shipment>
    <cbc:ID>7400043504</cbc:ID>
    <cbc:NetWeightMeasure unitCode="KGM">22900</cbc:NetWeightMeasure>
    <cac:Consignment>
      <cbc:ID>7300043504</cbc:ID>
      <cbc:TotalPackagesQuantity>54</cbc:TotalPackagesQuantity>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Used polyethylene stretch film and film offcuts, baled</cbc:Description>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
      <cac:Item>
        <cbc:Description>Used polyethylene stretch film and film offcuts, baled</cbc:Description>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="urn:ubl-examples:world:XU:codelist:WasteCode">150102</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:ContainingPackage>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel baling wire</cbc:PackingMaterial>
      </cac:ContainingPackage>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">395</cbc:TransportMeansTypeCode>
        <cac:RoadTransport>
          <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 KT</cbc:LicensePlateID>
          <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 TR</cbc:TrailerLicensePlateID>
        </cac:RoadTransport>
        <cac:OwnerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Trasvia Haulage</cbc:Name>
          </cac:PartyName>
        </cac:OwnerParty>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">38200</cbc:Measure>
          <cbc:Description>Loaded, at 10:07</cbc:Description>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">TAREWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">15300</cbc:Measure>
          <cbc:Description>Empty, at 10:46</cbc:Description>
        </cac:MeasurementDimension>
      </cac:TransportMeans>
      <cac:DriverPerson>
        <cbc:ID>XU-DL-0417722</cbc:ID>
        <cbc:FirstName>Ilario</cbc:FirstName>
        <cbc:FamilyName>Bencetti</cbc:FamilyName>
      </cac:DriverPerson>
    </cac:ShipmentStage>
  </cac:Shipment>
</WeightStatement>
```
