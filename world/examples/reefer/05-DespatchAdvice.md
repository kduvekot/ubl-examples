# Despatch Advice: Harrowmead Fruit Growers to Hafefo Fresh Produce

*Example 5 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The cooperative tells the wholesaler what is in the reefer: the pallets, their varieties, grower lots and packing dates.

[The XML file](05-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **HFG-DA-26-0560**  
  The despatching party's number.
- `UUID` = **f20ac700-f004-551d-94a6-fbb9ba2f561d**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-22**  
  Sent when the reefer leaves the packhouse for the port.
- `IssueTime` = **12:05:00-01:00**  
  When the loaded reefer left the packhouse for the port, about five hours and a half away with a stop; in the issuer's local time, with its offset from UTC (D27).
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage in your receipt advice.**  
  What the receiver should do; the note names the transport document the flow uses (worklist C30).
- `LineCountNumeric` = **3**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **HFP-PO-26-0553**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-418726** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Orchard Road**  
  Street of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/PostalAddress/CityName` = **Harrowmead**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71640**  
  Postal code in Bayvarra's format (5 digits). identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Harrowmead Fruit Growers (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/Contact/Department` = **Packhouse**  
  The department the desk belongs to; identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7164 281 590**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/Contact/ElectronicMail` = **dispatch@harrowmeadfruit.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; identity of Harrowmead Fruit Growers (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20415873** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Hafefo Fresh Produce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Cold store**  
  The party's cold store desk: the desk for its role in this document (it receives the goods); identity of Hafefo Fresh Produce (world/parties.json).
- `Party/Contact/JobTitle` = **Cold store supervisor**  
  The job of the person who answers at the desk; identity of Hafefo Fresh Produce (world/parties.json).
- `Party/Contact/Department` = **Cold store**  
  The department the desk belongs to; identity of Hafefo Fresh Produce (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Hafefo Fresh Produce (world/parties.json).
- `Party/Contact/ElectronicMail` = **coldstore@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Hafefo Fresh Produce (world/parties.json).
- `Party/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; identity of Hafefo Fresh Produce (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC43529** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; identity of Hafefo Fresh Produce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **HFG-SH-26-0555**  
  The despatching party's shipment number.
- `Consignment/ID` = **HFG-CS-26-0556**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/GrossWeightMeasure` = **21728** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight of the fruit on its pallets.
- `Consignment/CarrierParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/CarrierParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/Contact/Department` = **Bookings**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-04-27**  
  Expected after the usual transit by sea.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-04-27**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-04-22**  
  The goods left on the day of this advice.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU5316047** (schemeID `ISO6346`)  
  The reefer the fruit is loaded in.
- `TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **TWL-S-0884517**  
  The carrier's seal, put on at the packhouse.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653010** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 001 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653010**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653027** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 002 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653027**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653034** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 003 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653034**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653041** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 004 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653041**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653058** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 005 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653058**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653065** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 006 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653065**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653072** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 007 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653072**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653089** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 008 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653089**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653096** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 009 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653096**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653102** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 010 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653102**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653119** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 011 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653119**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653126** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 012 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653126**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653133** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 013 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653133**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653140** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 014 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653140**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653157** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 015 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653157**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653164** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 016 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653164**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653171** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 017 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653171**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653188** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 018 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653188**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653195** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 019 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653195**  
  The pallet's barcode, scanned at loading and at the cold store.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653201** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 020 of 020**  
  The consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653201**  
  The pallet's barcode, scanned at loading and at the cold store.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **Twelve pallets of 56 cartons: Gala, the island's everyday apple, from the cooperative's cold store.**  
  The line as the order put it.
- `DeliveredQuantity` = **672** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.**  
  The seller's description; item apples-gala of Harrowmead Fruit Growers (world/items.json).
- `Item/Name` = **Apples Gala, carton 18 kg, count 100**  
  The item's short name; item apples-gala of Harrowmead Fruit Growers (world/items.json).
- `Item/SellersItemIdentification/ID` = **HFC-GAL100**  
  The seller's own item number; item apples-gala of Harrowmead Fruit Growers (world/items.json).
- `Item/StandardItemIdentification/ID` = **9527430001014** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers' (world/items.json).
- `Item/ItemInstance/ManufactureDate` = **2026-04-20**  
  Packed on that day, from the cold store or the orchard straight into cartons.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Quality class**  
  The class the lot is graded and packed in, as each carton is marked: the Trade Accord's marketing standard for fresh fruit, after the UNECE standards FFV-50 for apples and FFV-51 for pears, asks the class and the count on the package.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **Class I**  
  Fruit of good quality, characteristic of its variety; slight defects of shape, colouring and skin allowed.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Grower**  
  The member whose orchard the lot comes from: the number on the carton label, for tracing a lot back to its orchard.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **G-017**  
  The member number in the cooperative's register.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Cartons**  
  How many cartons of the line are of this lot.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **224**  
  Counted at packing.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **HFC-L26-0401**  
  The packhouse's lot: one grower's fruit of one variety and size, packed in one run.
- `Item/ItemInstance/ManufactureDate` = **2026-04-20**  
  Packed on that day, from the cold store or the orchard straight into cartons.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Quality class**  
  The class the lot is graded and packed in, as each carton is marked: the Trade Accord's marketing standard for fresh fruit, after the UNECE standards FFV-50 for apples and FFV-51 for pears, asks the class and the count on the package.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **Class I**  
  Fruit of good quality, characteristic of its variety; slight defects of shape, colouring and skin allowed.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Grower**  
  The member whose orchard the lot comes from: the number on the carton label, for tracing a lot back to its orchard.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **G-023**  
  The member number in the cooperative's register.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Cartons**  
  How many cartons of the line are of this lot.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **224**  
  Counted at packing.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **HFC-L26-0402**  
  The packhouse's lot: one grower's fruit of one variety and size, packed in one run.
- `Item/ItemInstance/ManufactureDate` = **2026-04-20**  
  Packed on that day, from the cold store or the orchard straight into cartons.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Quality class**  
  The class the lot is graded and packed in, as each carton is marked: the Trade Accord's marketing standard for fresh fruit, after the UNECE standards FFV-50 for apples and FFV-51 for pears, asks the class and the count on the package.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **Class I**  
  Fruit of good quality, characteristic of its variety; slight defects of shape, colouring and skin allowed.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Grower**  
  The member whose orchard the lot comes from: the number on the carton label, for tracing a lot back to its orchard.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **G-041**  
  The member number in the cooperative's register.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Cartons**  
  How many cartons of the line are of this lot.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **224**  
  Counted at packing.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **HFC-L26-0403**  
  The packhouse's lot: one grower's fruit of one variety and size, packed in one run.
- `ID` = **2**  
  The line number.
- `Note` = **Four pallets of 56 cartons: Granny Smith, picked this month, for the shops and for the hotels' and the hospital's kitchens.**  
  The line as the order put it.
- `DeliveredQuantity` = **224** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **2**  
  The order line this line fulfils.
- `Item/Description` = **Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.**  
  The seller's description; item apples-granny of Harrowmead Fruit Growers (world/items.json).
- `Item/Name` = **Apples Granny Smith, carton 18 kg, count 100**  
  The item's short name; item apples-granny of Harrowmead Fruit Growers (world/items.json).
- `Item/SellersItemIdentification/ID` = **HFC-GSM100**  
  The seller's own item number; item apples-granny of Harrowmead Fruit Growers (world/items.json).
- `Item/StandardItemIdentification/ID` = **9527430001021** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers' (world/items.json).
- `Item/ItemInstance/ManufactureDate` = **2026-04-21**  
  Packed on that day, from the cold store or the orchard straight into cartons.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Quality class**  
  The class the lot is graded and packed in, as each carton is marked: the Trade Accord's marketing standard for fresh fruit, after the UNECE standards FFV-50 for apples and FFV-51 for pears, asks the class and the count on the package.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **Class I**  
  Fruit of good quality, characteristic of its variety; slight defects of shape, colouring and skin allowed.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Grower**  
  The member whose orchard the lot comes from: the number on the carton label, for tracing a lot back to its orchard.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **G-008**  
  The member number in the cooperative's register.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Cartons**  
  How many cartons of the line are of this lot.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **112**  
  Counted at packing.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **HFC-L26-0431**  
  The packhouse's lot: one grower's fruit of one variety and size, packed in one run.
- `Item/ItemInstance/ManufactureDate` = **2026-04-21**  
  Packed on that day, from the cold store or the orchard straight into cartons.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Quality class**  
  The class the lot is graded and packed in, as each carton is marked: the Trade Accord's marketing standard for fresh fruit, after the UNECE standards FFV-50 for apples and FFV-51 for pears, asks the class and the count on the package.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **Class I**  
  Fruit of good quality, characteristic of its variety; slight defects of shape, colouring and skin allowed.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Grower**  
  The member whose orchard the lot comes from: the number on the carton label, for tracing a lot back to its orchard.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **G-031**  
  The member number in the cooperative's register.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Cartons**  
  How many cartons of the line are of this lot.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **112**  
  Counted at packing.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **HFC-L26-0432**  
  The packhouse's lot: one grower's fruit of one variety and size, packed in one run.
- `ID` = **3**  
  The line number.
- `Note` = **Four pallets of 56 cartons: Packham's Triumph pears, from the cooperative's cold store.**  
  The line as the order put it.
- `DeliveredQuantity` = **224** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **3**  
  The order line this line fulfils.
- `Item/Description` = **Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.**  
  The seller's description; item pears-packham of Harrowmead Fruit Growers (world/items.json).
- `Item/Name` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  The item's short name; item pears-packham of Harrowmead Fruit Growers (world/items.json).
- `Item/SellersItemIdentification/ID` = **HFC-PKT080**  
  The seller's own item number; item pears-packham of Harrowmead Fruit Growers (world/items.json).
- `Item/StandardItemIdentification/ID` = **9527430002011** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers' (world/items.json).
- `Item/ItemInstance/ManufactureDate` = **2026-04-20**  
  Packed on that day, from the cold store or the orchard straight into cartons.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Quality class**  
  The class the lot is graded and packed in, as each carton is marked: the Trade Accord's marketing standard for fresh fruit, after the UNECE standards FFV-50 for apples and FFV-51 for pears, asks the class and the count on the package.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **Class I**  
  Fruit of good quality, characteristic of its variety; slight defects of shape, colouring and skin allowed.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Grower**  
  The member whose orchard the lot comes from: the number on the carton label, for tracing a lot back to its orchard.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **G-012**  
  The member number in the cooperative's register.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Cartons**  
  How many cartons of the line are of this lot.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **224**  
  Counted at packing.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **HFC-L26-0451**  
  The packhouse's lot: one grower's fruit of one variety and size, packed in one run.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>HFG-DA-26-0560</cbc:ID>
  <cbc:UUID>f20ac700-f004-551d-94a6-fbb9ba2f561d</cbc:UUID>
  <cbc:IssueDate>2026-04-22</cbc:IssueDate>
  <cbc:IssueTime>12:05:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage in your receipt advice.</cbc:Note>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>HFP-PO-26-0553</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9527430900003</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-418726</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Orchard Road</cbc:StreetName>
        <cbc:BuildingNumber>3</cbc:BuildingNumber>
        <cbc:CityName>Harrowmead</cbc:CityName>
        <cbc:PostalZone>71640</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Dispatch office</cbc:Name>
        <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
        <cbc:Department>Packhouse</cbc:Department>
        <cbc:Telephone>+999 2 7164 281 590</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@harrowmeadfruit.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20415873</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Hafefo Fresh Produce</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40618392</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
        <cbc:BuildingNumber>58</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Cold store</cbc:Name>
        <cbc:JobTitle>Cold store supervisor</cbc:JobTitle>
        <cbc:Department>Cold store</cbc:Department>
        <cbc:Telephone>+999 3 726 8104</cbc:Telephone>
        <cbc:ElectronicMail>coldstore@hafefo.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 05:00–14:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC43529</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:Shipment>
    <cbc:ID>HFG-SH-26-0555</cbc:ID>
    <cac:Consignment>
      <cbc:ID>HFG-CS-26-0556</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">21728</cbc:GrossWeightMeasure>
      <cac:CarrierParty>
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
      </cac:CarrierParty>
    </cac:Consignment>
    <cac:Delivery>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-04-27</cbc:StartDate>
        <cbc:EndDate>2026-04-27</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-04-22</cbc:ActualDespatchDate>
      </cac:Despatch>
    </cac:Delivery>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU5316047</cbc:ID>
        <cac:TransportEquipmentSeal>
          <cbc:ID>TWL-S-0884517</cbc:ID>
        </cac:TransportEquipmentSeal>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653010</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 001 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653010</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653027</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 002 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653027</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653034</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 003 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653034</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653041</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 004 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653041</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653058</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 005 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653058</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653065</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 006 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653065</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653072</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 007 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653072</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653089</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 008 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653089</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653096</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 009 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653096</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653102</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 010 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653102</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653119</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 011 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653119</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653126</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 012 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653126</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653133</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 013 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653133</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653140</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 014 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653140</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653157</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 015 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653157</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653164</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 016 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653164</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653171</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 017 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653171</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653188</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 018 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653188</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653195</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 019 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653195</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
        <cac:PackagedTransportHandlingUnit>
          <cbc:ID schemeID="GS1 SSCC">095274300005653201</cbc:ID>
          <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
          <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
          <cbc:ShippingMarks>HAFEFO SELANU / 020 of 020</cbc:ShippingMarks>
          <cbc:TraceID>095274300005653201</cbc:TraceID>
        </cac:PackagedTransportHandlingUnit>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Twelve pallets of 56 cartons: Gala, the island's everyday apple, from the cooperative's cold store.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">672</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.</cbc:Description>
      <cbc:Name>Apples Gala, carton 18 kg, count 100</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>HFC-GAL100</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9527430001014</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-04-20</cbc:ManufactureDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quality class</cbc:Name>
          <cbc:Value>Class I</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grower</cbc:Name>
          <cbc:Value>G-017</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Cartons</cbc:Name>
          <cbc:Value>224</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>HFC-L26-0401</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-04-20</cbc:ManufactureDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quality class</cbc:Name>
          <cbc:Value>Class I</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grower</cbc:Name>
          <cbc:Value>G-023</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Cartons</cbc:Name>
          <cbc:Value>224</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>HFC-L26-0402</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-04-20</cbc:ManufactureDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quality class</cbc:Name>
          <cbc:Value>Class I</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grower</cbc:Name>
          <cbc:Value>G-041</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Cartons</cbc:Name>
          <cbc:Value>224</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>HFC-L26-0403</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Four pallets of 56 cartons: Granny Smith, picked this month, for the shops and for the hotels' and the hospital's kitchens.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">224</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.</cbc:Description>
      <cbc:Name>Apples Granny Smith, carton 18 kg, count 100</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>HFC-GSM100</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9527430001021</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-04-21</cbc:ManufactureDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quality class</cbc:Name>
          <cbc:Value>Class I</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grower</cbc:Name>
          <cbc:Value>G-008</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Cartons</cbc:Name>
          <cbc:Value>112</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>HFC-L26-0431</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-04-21</cbc:ManufactureDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quality class</cbc:Name>
          <cbc:Value>Class I</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grower</cbc:Name>
          <cbc:Value>G-031</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Cartons</cbc:Name>
          <cbc:Value>112</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>HFC-L26-0432</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>3</cbc:ID>
    <cbc:Note>Four pallets of 56 cartons: Packham's Triumph pears, from the cooperative's cold store.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">224</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.</cbc:Description>
      <cbc:Name>Pears Packham's Triumph, carton 18 kg, count 80</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>HFC-PKT080</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9527430002011</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-04-20</cbc:ManufactureDate>
        <cac:AdditionalItemProperty>
          <cbc:Name>Quality class</cbc:Name>
          <cbc:Value>Class I</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grower</cbc:Name>
          <cbc:Value>G-012</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Cartons</cbc:Name>
          <cbc:Value>224</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:LotIdentification>
          <cbc:LotNumberID>HFC-L26-0451</cbc:LotNumberID>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
