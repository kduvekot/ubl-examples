# Weight Statement: Selanu Cotton Ginnery to Tidewell Ocean Lines

*Example 12 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Weight Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WEIGHT-STATEMENT-SCHEMA)*

Before loading, the shipper declares the verified gross mass of the container by SOLAS method 2: the ginnery has weighed every bale on its bale scale and adds the container's own weight.

[The XML file](12-WeightStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:weight-statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Weight statement". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SCG-WS-26-0205**  
  The shipper's weight statement number.
- `UUID` = **43b82e91-f4de-52c1-ac47-945443cd1b55**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-06**  
  Declared before the container is loaded, as required for every packed container.
- `IssueTime` = **15:19:00+00:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `WeightStatementTypeCode` = **VGM** (listID `urn:ubl-examples:world:codelist:WeightStatementTypeCode`)  
  A statement of the verified gross mass. The code is from the Trade Accord's weight statement type list: VGM = Verified gross mass.

### Signature

Inside `Signature`:

- `ID` = **SCG-SIG-VGM**  
  The shipper's signature, as SOLAS requires: the ginnery signs its own declaration, so no one signs for it (cotton/12#F2).
- `SignatoryParty/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Selanu Cotton Ginnery (world/parties.json).
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it (world/map.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Telephone` = **+999 3 721 0486**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/ElectronicMail` = **logistics@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Cotton Ginnery (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Department` = **Bookings**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Weighing Party

Inside `WeighingParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipper Party

Inside `ShipperParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SCG-SH-26-0200**  
  The shipment weighed.
- `TransportHandlingUnit/TotalPackageQuantity` = **27** (unitCode `EA`)  
  The 27 bales in the container, each listed below with its weight.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU4123110** (schemeID `ISO6346`)  
  The container, with its ISO 6346 check digit.
- `TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **3750** (unitCode `KGM`)  
  The empty container's own weight, as marked on its door.
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDate` = **2026-05-06**  
  The day the container was packed at the ginnery and its mass established.
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingTime` = **14:30:00**  
  When the doors were closed on the 27th bale.
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingMethodCode` = **SM2** (listID `IMO SOLAS`)  
  SOLAS method 2: every bale weighed, the weights added to the container's tare. The code is from UBL's default Weighing method (IMO SOLAS) list: SM2 = SOLAS verification method 2.
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceType` = **Bale scale at the press**  
  Each bale weighed as it left the press, to 10 g (O26).
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/GrossMassMeasure` = **9940.29** (unitCode `KGM`)  
  The verified gross mass: the 27 bales as the ginnery weighed them (6190.29 kg) and the container's own weight.
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/ID` = **SCG-PR-26-L017**  
  The documentary evidence of method 2: the ginnery's pressing record of lot SCG-L26-017, with each bale's weight from the bale scale.
- `TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/DocumentType` = **Pressing record**  
  The kind of document referred to, the ginnery's pressing record of lot SCG-L26-017, with each bale's weight from the bale scale, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `TransportHandlingUnit/Package/ID` = **SCG-26-00412**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **227.5** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **229.77** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00413**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **223.5** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **225.77** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00414**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **224** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **226.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00415**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **226** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **228.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00416**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **222** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **224.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00417**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **230** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **232.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00418**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **228** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **230.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00419**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **222** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **224.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00420**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **229** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **231.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00517**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **225** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **227.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00518**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **228.5** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **230.77** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00519**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **232** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **234.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00520**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **230.5** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **232.77** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00521**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **226** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **228.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00522**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **231** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **233.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00523**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **228** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **230.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00524**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **232** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **234.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00525**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **222** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **224.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00603**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **230** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **232.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00604**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **224** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **226.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00605**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **223** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **225.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00606**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **226** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **228.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00607**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **230.5** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **232.77** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00608**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **232** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **234.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00609**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **224** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **226.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00610**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **230.5** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **232.77** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.
- `TransportHandlingUnit/Package/ID` = **SCG-26-00611**  
  The bale's number on its tag, which the ginnery gives every bale it presses; a package's own number, without a scheme.
- `TransportHandlingUnit/Package/Quantity` = **222** (unitCode `KGM`)  
  The lint in the bale: its gross weight less the standard tare of 2.27 kg for the bale's woven cotton cover and its steel ties, as the ginnery and the mill agree in their season agreement.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The bale's weight with its cover and ties. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/Package/MeasurementDimension/Measure` = **224.27** (unitCode `KGM`)  
  Weighed on the bale scale at the ginnery's press, each bale as it leaves the press, to 10 g.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<WeightStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:WeightStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:weight-statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SCG-WS-26-0205</cbc:ID>
  <cbc:UUID>43b82e91-f4de-52c1-ac47-945443cd1b55</cbc:UUID>
  <cbc:IssueDate>2026-05-06</cbc:IssueDate>
  <cbc:IssueTime>15:19:00+00:00</cbc:IssueTime>
  <cbc:WeightStatementTypeCode listID="urn:ubl-examples:world:codelist:WeightStatementTypeCode">VGM</cbc:WeightStatementTypeCode>
  <cac:Signature>
    <cbc:ID>SCG-SIG-VGM</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-042681</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
    </cac:Language>
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
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
      <cbc:ElectronicMail>logistics@selanuginnery.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-547539</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Bookings</cbc:Name>
      <cbc:JobTitle>Booking agent</cbc:JobTitle>
      <cbc:Department>Bookings</cbc:Department>
      <cbc:Telephone>+999 2 38 2058 7929</cbc:Telephone>
      <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:WeighingParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:WeighingParty>
  <cac:ShipperParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:ShipperParty>
  <cac:Shipment>
    <cbc:ID>SCG-SH-26-0200</cbc:ID>
    <cac:TransportHandlingUnit>
      <cbc:TotalPackageQuantity unitCode="EA">27</cbc:TotalPackageQuantity>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU4123110</cbc:ID>
        <cbc:TareWeightMeasure unitCode="KGM">3750</cbc:TareWeightMeasure>
        <cac:VerifiedGrossMass>
          <cbc:WeighingDate>2026-05-06</cbc:WeighingDate>
          <cbc:WeighingTime>14:30:00</cbc:WeighingTime>
          <cbc:WeighingMethodCode listID="IMO SOLAS">SM2</cbc:WeighingMethodCode>
          <cbc:WeighingDeviceType>Bale scale at the press</cbc:WeighingDeviceType>
          <cbc:GrossMassMeasure unitCode="KGM">9940.29</cbc:GrossMassMeasure>
          <cac:DocumentReference>
            <cbc:ID>SCG-PR-26-L017</cbc:ID>
            <cbc:DocumentType>Pressing record</cbc:DocumentType>
          </cac:DocumentReference>
        </cac:VerifiedGrossMass>
      </cac:TransportEquipment>
      <cac:Package>
        <cbc:ID>SCG-26-00412</cbc:ID>
        <cbc:Quantity unitCode="KGM">227.5</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">229.77</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00413</cbc:ID>
        <cbc:Quantity unitCode="KGM">223.5</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">225.77</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00414</cbc:ID>
        <cbc:Quantity unitCode="KGM">224</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">226.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00415</cbc:ID>
        <cbc:Quantity unitCode="KGM">226</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">228.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00416</cbc:ID>
        <cbc:Quantity unitCode="KGM">222</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">224.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00417</cbc:ID>
        <cbc:Quantity unitCode="KGM">230</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">232.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00418</cbc:ID>
        <cbc:Quantity unitCode="KGM">228</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">230.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00419</cbc:ID>
        <cbc:Quantity unitCode="KGM">222</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">224.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00420</cbc:ID>
        <cbc:Quantity unitCode="KGM">229</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">231.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00517</cbc:ID>
        <cbc:Quantity unitCode="KGM">225</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">227.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00518</cbc:ID>
        <cbc:Quantity unitCode="KGM">228.5</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">230.77</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00519</cbc:ID>
        <cbc:Quantity unitCode="KGM">232</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">234.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00520</cbc:ID>
        <cbc:Quantity unitCode="KGM">230.5</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">232.77</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00521</cbc:ID>
        <cbc:Quantity unitCode="KGM">226</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">228.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00522</cbc:ID>
        <cbc:Quantity unitCode="KGM">231</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">233.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00523</cbc:ID>
        <cbc:Quantity unitCode="KGM">228</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">230.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00524</cbc:ID>
        <cbc:Quantity unitCode="KGM">232</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">234.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00525</cbc:ID>
        <cbc:Quantity unitCode="KGM">222</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">224.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00603</cbc:ID>
        <cbc:Quantity unitCode="KGM">230</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">232.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00604</cbc:ID>
        <cbc:Quantity unitCode="KGM">224</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">226.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00605</cbc:ID>
        <cbc:Quantity unitCode="KGM">223</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">225.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00606</cbc:ID>
        <cbc:Quantity unitCode="KGM">226</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">228.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00607</cbc:ID>
        <cbc:Quantity unitCode="KGM">230.5</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">232.77</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00608</cbc:ID>
        <cbc:Quantity unitCode="KGM">232</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">234.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00609</cbc:ID>
        <cbc:Quantity unitCode="KGM">224</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">226.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00610</cbc:ID>
        <cbc:Quantity unitCode="KGM">230.5</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">232.77</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
      <cac:Package>
        <cbc:ID>SCG-26-00611</cbc:ID>
        <cbc:Quantity unitCode="KGM">222</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">224.27</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:Package>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
</WeightStatement>
```
