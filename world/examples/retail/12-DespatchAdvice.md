# Despatch Advice: Lumeway Distribution to Brightmarket Stores

*Example 12 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The distributor announces the delivery and the truck that brings it.

[The XML file](12-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0#compliant#urn:ubl-examples:world:community:retail:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice"; the community specification "Retail community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900339316**  
  The collaboration this document belongs to: the store's order from Lumeway, from the order to the credit note. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **LMW-DA-26-0911**  
  The despatching party's number.
- `UUID` = **4b7e9055-23cd-5fbb-b498-b08f07b17c6e**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-29**  
  The day the truck was loaded at the distribution centre.
- `IssueTime` = **15:34:00-01:00**  
  When the truck was loaded and the carrier had signed its consignment note, on the afternoon before the delivery; in the issuer's local time, with its offset from UTC.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage in your receipt advice.**  
  What the receiver should do; the note names the transport document the flow uses.
- `LineCountNumeric` = **1**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **7100452422**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Lumeway Distribution gives it.
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Party/Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Party/Contact/ElectronicMail` = **dispatch@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brightmarket Stores gives it.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; as Brightmarket Stores gives it.
- `Party/TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; as Brightmarket Stores gives it.
- `Party/PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Brightmarket Stores gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. As Brightmarket Stores gives it.
- `Party/PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. As Brightmarket Stores gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Brightmarket Stores gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Brightmarket Stores gives it.
- `Party/PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). As Brightmarket Stores gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Brightmarket Stores gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Goods-in, Lumeport store**  
  The party's goods-in, lumeport store desk: the desk for its role in this document (it receives the goods); as Brightmarket Stores gives it.
- `Party/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Brightmarket Stores gives it.
- `Party/Contact/Department` = **Store operations**  
  The department the desk belongs to; as Brightmarket Stores gives it.
- `Party/Contact/Telephone` = **+999 2 38 4609 7100**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Brightmarket Stores gives it.
- `Party/Contact/ElectronicMail` = **goodsin@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brightmarket Stores gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Brightmarket Stores gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **LMW-SH-26-0911**  
  The despatching party's shipment number.
- `Consignment/ID` = **LMW-CS-26-0893**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/GrossWeightMeasure` = **1297.2** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight loaded.
- `Consignment/CarrierParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Bayforth Forwarding**  
  The trading name; as Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. As Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. As Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). As Bayforth Forwarding gives it.
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/CarrierParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bayforth Forwarding gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Transport desk**  
  The party's main desk, which handles this document; as Bayforth Forwarding gives it.
- `Consignment/CarrierParty/Contact/JobTitle` = **Transport planner**  
  The job of the person who answers at the desk; as Bayforth Forwarding gives it.
- `Consignment/CarrierParty/Contact/Department` = **Transport**  
  The department the desk belongs to; as Bayforth Forwarding gives it.
- `Consignment/CarrierParty/Contact/Telephone` = **+999 2 38 5155 2404**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bayforth Forwarding gives it.
- `Consignment/CarrierParty/Contact/ElectronicMail` = **transport@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Bayforth Forwarding gives it.
- `Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayforth Forwarding gives it.
- `ShipmentStage/ID` = **1**  
  The one stage: the truck from the distribution centre to the store.
- `ShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `ShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `ShipmentStage/TransportMeans/TransportMeansTypeCode` = **395** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: truck with curtain-side trailer; the fleet of Bayforth Forwarding. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 395 = Truck, with trailer.
- `ShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **BV LP 2203** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The registration plate of the truck; the fleet of Bayforth Forwarding. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `ShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **BV TR 0817** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `ShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **LOADINGLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The length of the loading floor. The code is from the Trade Accord's dimension attribute list: LOADINGLENGTH = Loading length. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/MeasurementDimension/Measure` = **13.6** (unitCode `MTR`)  
  Room for 33 pallets.
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-04-30**  
  Expected after the usual transit by road.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-04-30**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-04-29**  
  The goods left on the day of this advice.
- `TransportHandlingUnit/ID` = **095206100003729019** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `TransportHandlingUnit/ShippingMarks` = **BRIGHTMARKET LUMEPORT / 001 of 006**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TraceID` = **095206100003729019**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `TransportHandlingUnit/HandlingUnitDespatchLine/ID` = **1-1**  
  The pallet's line: the benches on it, as part {k} of despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/DeliveredQuantity` = **4** (unitCode `EA`)  
  Four benches on the pallet.
- `TransportHandlingUnit/HandlingUnitDespatchLine/OrderLineReference/LineID` = **1**  
  The order line the benches belong to.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/Name` = **Park bench Serra 180**  
  The item, named only: it is described in full on despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's item number.
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/TransportEquipment/ID` = **095206100000122217** (schemeID `GS1 GRAI`)  
  The pallet's Global Returnable Asset Identifier (GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its returnable pallet, the check digit and the pallet's serial number.
- `TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The pallet goes back: the truck takes the store's empty pallets back to the distribution centre.
- `TransportHandlingUnit/TransportEquipment/Description` = **Returnable pallet of the distributor's pool, 1850 x 700 mm**  
  The pallet the parcels are loaded on: transport equipment in UN/CEFACT's sense, which counts pallets with containers and trailers.
- `TransportHandlingUnit/ShipmentDocumentReference/ID` = **BYF-WB-26-2276**  
  The carrier's consignment note the pallet travels under, issued when the truck was loaded.
- `TransportHandlingUnit/ShipmentDocumentReference/DocumentType` = **Consignment note**  
  What the document is.
- `TransportHandlingUnit/ID` = **095206100003729026** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `TransportHandlingUnit/ShippingMarks` = **BRIGHTMARKET LUMEPORT / 002 of 006**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TraceID` = **095206100003729026**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `TransportHandlingUnit/HandlingUnitDespatchLine/ID` = **1-2**  
  The pallet's line: the benches on it, as part {k} of despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/DeliveredQuantity` = **4** (unitCode `EA`)  
  Four benches on the pallet.
- `TransportHandlingUnit/HandlingUnitDespatchLine/OrderLineReference/LineID` = **1**  
  The order line the benches belong to.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/Name` = **Park bench Serra 180**  
  The item, named only: it is described in full on despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's item number.
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/TransportEquipment/ID` = **095206100000122234** (schemeID `GS1 GRAI`)  
  The pallet's Global Returnable Asset Identifier (GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its returnable pallet, the check digit and the pallet's serial number.
- `TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The pallet goes back: the truck takes the store's empty pallets back to the distribution centre.
- `TransportHandlingUnit/TransportEquipment/Description` = **Returnable pallet of the distributor's pool, 1850 x 700 mm**  
  The pallet the parcels are loaded on: transport equipment in UN/CEFACT's sense, which counts pallets with containers and trailers.
- `TransportHandlingUnit/ShipmentDocumentReference/ID` = **BYF-WB-26-2276**  
  The carrier's consignment note the pallet travels under, issued when the truck was loaded.
- `TransportHandlingUnit/ShipmentDocumentReference/DocumentType` = **Consignment note**  
  What the document is.
- `TransportHandlingUnit/ID` = **095206100003729033** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `TransportHandlingUnit/ShippingMarks` = **BRIGHTMARKET LUMEPORT / 003 of 006**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TraceID` = **095206100003729033**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `TransportHandlingUnit/HandlingUnitDespatchLine/ID` = **1-3**  
  The pallet's line: the benches on it, as part {k} of despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/DeliveredQuantity` = **4** (unitCode `EA`)  
  Four benches on the pallet.
- `TransportHandlingUnit/HandlingUnitDespatchLine/OrderLineReference/LineID` = **1**  
  The order line the benches belong to.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/Name` = **Park bench Serra 180**  
  The item, named only: it is described in full on despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's item number.
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/TransportEquipment/ID` = **095206100000122251** (schemeID `GS1 GRAI`)  
  The pallet's Global Returnable Asset Identifier (GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its returnable pallet, the check digit and the pallet's serial number.
- `TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The pallet goes back: the truck takes the store's empty pallets back to the distribution centre.
- `TransportHandlingUnit/TransportEquipment/Description` = **Returnable pallet of the distributor's pool, 1850 x 700 mm**  
  The pallet the parcels are loaded on: transport equipment in UN/CEFACT's sense, which counts pallets with containers and trailers.
- `TransportHandlingUnit/ShipmentDocumentReference/ID` = **BYF-WB-26-2276**  
  The carrier's consignment note the pallet travels under, issued when the truck was loaded.
- `TransportHandlingUnit/ShipmentDocumentReference/DocumentType` = **Consignment note**  
  What the document is.
- `TransportHandlingUnit/ID` = **095206100003729040** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `TransportHandlingUnit/ShippingMarks` = **BRIGHTMARKET LUMEPORT / 004 of 006**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TraceID` = **095206100003729040**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `TransportHandlingUnit/HandlingUnitDespatchLine/ID` = **1-4**  
  The pallet's line: the benches on it, as part {k} of despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/DeliveredQuantity` = **4** (unitCode `EA`)  
  Four benches on the pallet.
- `TransportHandlingUnit/HandlingUnitDespatchLine/OrderLineReference/LineID` = **1**  
  The order line the benches belong to.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/Name` = **Park bench Serra 180**  
  The item, named only: it is described in full on despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's item number.
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/TransportEquipment/ID` = **095206100000122268** (schemeID `GS1 GRAI`)  
  The pallet's Global Returnable Asset Identifier (GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its returnable pallet, the check digit and the pallet's serial number.
- `TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The pallet goes back: the truck takes the store's empty pallets back to the distribution centre.
- `TransportHandlingUnit/TransportEquipment/Description` = **Returnable pallet of the distributor's pool, 1850 x 700 mm**  
  The pallet the parcels are loaded on: transport equipment in UN/CEFACT's sense, which counts pallets with containers and trailers.
- `TransportHandlingUnit/ShipmentDocumentReference/ID` = **BYF-WB-26-2276**  
  The carrier's consignment note the pallet travels under, issued when the truck was loaded.
- `TransportHandlingUnit/ShipmentDocumentReference/DocumentType` = **Consignment note**  
  What the document is.
- `TransportHandlingUnit/ID` = **095206100003729057** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `TransportHandlingUnit/ShippingMarks` = **BRIGHTMARKET LUMEPORT / 005 of 006**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TraceID` = **095206100003729057**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `TransportHandlingUnit/HandlingUnitDespatchLine/ID` = **1-5**  
  The pallet's line: the benches on it, as part {k} of despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/DeliveredQuantity` = **4** (unitCode `EA`)  
  Four benches on the pallet.
- `TransportHandlingUnit/HandlingUnitDespatchLine/OrderLineReference/LineID` = **1**  
  The order line the benches belong to.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/Name` = **Park bench Serra 180**  
  The item, named only: it is described in full on despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's item number.
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/TransportEquipment/ID` = **095206100000122285** (schemeID `GS1 GRAI`)  
  The pallet's Global Returnable Asset Identifier (GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its returnable pallet, the check digit and the pallet's serial number.
- `TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The pallet goes back: the truck takes the store's empty pallets back to the distribution centre.
- `TransportHandlingUnit/TransportEquipment/Description` = **Returnable pallet of the distributor's pool, 1850 x 700 mm**  
  The pallet the parcels are loaded on: transport equipment in UN/CEFACT's sense, which counts pallets with containers and trailers.
- `TransportHandlingUnit/ShipmentDocumentReference/ID` = **BYF-WB-26-2276**  
  The carrier's consignment note the pallet travels under, issued when the truck was loaded.
- `TransportHandlingUnit/ShipmentDocumentReference/DocumentType` = **Consignment note**  
  What the document is.
- `TransportHandlingUnit/ID` = **095206100003729064** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `TransportHandlingUnit/ShippingMarks` = **BRIGHTMARKET LUMEPORT / 006 of 006**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `TransportHandlingUnit/TraceID` = **095206100003729064**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `TransportHandlingUnit/HandlingUnitDespatchLine/ID` = **1-6**  
  The pallet's line: the benches on it, as part {k} of despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/DeliveredQuantity` = **4** (unitCode `EA`)  
  Four benches on the pallet.
- `TransportHandlingUnit/HandlingUnitDespatchLine/OrderLineReference/LineID` = **1**  
  The order line the benches belong to.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/Name` = **Park bench Serra 180**  
  The item, named only: it is described in full on despatch line 1.
- `TransportHandlingUnit/HandlingUnitDespatchLine/Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's item number.
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `TransportHandlingUnit/ActualPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/ActualPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `TransportHandlingUnit/ActualPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/ActualPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `TransportHandlingUnit/TransportEquipment/ID` = **095206100000122302** (schemeID `GS1 GRAI`)  
  The pallet's Global Returnable Asset Identifier (GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its returnable pallet, the check digit and the pallet's serial number.
- `TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The pallet goes back: the truck takes the store's empty pallets back to the distribution centre.
- `TransportHandlingUnit/TransportEquipment/Description` = **Returnable pallet of the distributor's pool, 1850 x 700 mm**  
  The pallet the parcels are loaded on: transport equipment in UN/CEFACT's sense, which counts pallets with containers and trailers.
- `TransportHandlingUnit/ShipmentDocumentReference/ID` = **BYF-WB-26-2276**  
  The carrier's consignment note the pallet travels under, issued when the truck was loaded.
- `TransportHandlingUnit/ShipmentDocumentReference/DocumentType` = **Consignment note**  
  What the document is.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **Six pallets for the reopening of the home and garden department.**  
  The line as the order put it.
- `DeliveredQuantity` = **24** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description.
- `Item/Name` = **Park bench Serra 180**  
  The item's short name.
- `Item/BuyersItemIdentification/ID` = **BM-551210**  
  The buyer's own item number: it resells this item under its own number.
- `Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's own item number; as Lumeway Distribution describes the item.
- `Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller sells the maker's item on.
- `Item/StandardItemIdentification/ID` = **9520610000012** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none.
- `Item/AdditionalItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The maker's number for the item in its globally unique form under ISO/IEC 15459 (KXU and the company number Codana gave Valdara Industries), which travels along with the GTIN, as an importer may carry it; as Valdara Industries describes the item.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the lot was produced.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **VI-LOT-260320**  
  The production lot, from the maker's prefix and the production day; a recall names the lot.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Name` = **Coating batch**  
  A fact about this lot: the galvanising and powder-coating batch its frames went through.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Value` = **ZN-26-057**  
  Its batch: each lot has its own, in the coating line's running count of the year (the production record).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0#compliant#urn:ubl-examples:world:community:retail:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900339316</cbc:ProfileExecutionID>
  <cbc:ID>LMW-DA-26-0911</cbc:ID>
  <cbc:UUID>4b7e9055-23cd-5fbb-b498-b08f07b17c6e</cbc:UUID>
  <cbc:IssueDate>2026-04-29</cbc:IssueDate>
  <cbc:IssueTime>15:34:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage in your receipt advice.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>7100452422</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Distribution Drive</cbc:StreetName>
        <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
        <cbc:BuildingNumber>43</cbc:BuildingNumber>
        <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71214</cbc:PostalZone>
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
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9522610900002</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
      <cac:TradePartyName>
        <cbc:Name>Brightmarket</cbc:Name>
      </cac:TradePartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-579130</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Market Street</cbc:StreetName>
        <cbc:BuildingNumber>50</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38515</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Goods-in, Lumeport store</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Store operations</cbc:Department>
        <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@brightmarket.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>LMW-SH-26-0911</cbc:ID>
    <cac:Consignment>
      <cbc:ID>LMW-CS-26-0893</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">1297.2</cbc:GrossWeightMeasure>
      <cac:CarrierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Bayforth Forwarding</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Dockside Way</cbc:StreetName>
          <cbc:BuildingNumber>4</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38525</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Transport desk</cbc:Name>
          <cbc:JobTitle>Transport planner</cbc:JobTitle>
          <cbc:Department>Transport</cbc:Department>
          <cbc:Telephone>+999 2 38 5155 2404</cbc:Telephone>
          <cbc:ElectronicMail>transport@bayforth.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
      </cac:CarrierParty>
    </cac:Consignment>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">395</cbc:TransportMeansTypeCode>
        <cac:RoadTransport>
          <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV LP 2203</cbc:LicensePlateID>
          <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV TR 0817</cbc:TrailerLicensePlateID>
        </cac:RoadTransport>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LOADINGLENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MTR">13.6</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:TransportMeans>
    </cac:ShipmentStage>
    <cac:Delivery>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-04-30</cbc:StartDate>
        <cbc:EndDate>2026-04-30</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-04-29</cbc:ActualDespatchDate>
      </cac:Despatch>
    </cac:Delivery>
    <cac:TransportHandlingUnit>
      <cbc:ID schemeID="GS1 SSCC">095206100003729019</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
      <cbc:ShippingMarks>BRIGHTMARKET LUMEPORT / 001 of 006</cbc:ShippingMarks>
      <cbc:TraceID>095206100003729019</cbc:TraceID>
      <cac:HandlingUnitDespatchLine>
        <cbc:ID>1-1</cbc:ID>
        <cbc:DeliveredQuantity unitCode="EA">4</cbc:DeliveredQuantity>
        <cac:OrderLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:OrderLineReference>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>LMW-10442</cbc:ID>
          </cac:SellersItemIdentification>
        </cac:Item>
      </cac:HandlingUnitDespatchLine>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">13</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
        <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1810</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">295</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:TransportEquipment>
        <cbc:ID schemeID="GS1 GRAI">095206100000122217</cbc:ID>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:Description>Returnable pallet of the distributor's pool, 1850 x 700 mm</cbc:Description>
      </cac:TransportEquipment>
      <cac:ShipmentDocumentReference>
        <cbc:ID>BYF-WB-26-2276</cbc:ID>
        <cbc:DocumentType>Consignment note</cbc:DocumentType>
      </cac:ShipmentDocumentReference>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID schemeID="GS1 SSCC">095206100003729026</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
      <cbc:ShippingMarks>BRIGHTMARKET LUMEPORT / 002 of 006</cbc:ShippingMarks>
      <cbc:TraceID>095206100003729026</cbc:TraceID>
      <cac:HandlingUnitDespatchLine>
        <cbc:ID>1-2</cbc:ID>
        <cbc:DeliveredQuantity unitCode="EA">4</cbc:DeliveredQuantity>
        <cac:OrderLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:OrderLineReference>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>LMW-10442</cbc:ID>
          </cac:SellersItemIdentification>
        </cac:Item>
      </cac:HandlingUnitDespatchLine>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">13</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
        <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1810</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">295</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:TransportEquipment>
        <cbc:ID schemeID="GS1 GRAI">095206100000122234</cbc:ID>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:Description>Returnable pallet of the distributor's pool, 1850 x 700 mm</cbc:Description>
      </cac:TransportEquipment>
      <cac:ShipmentDocumentReference>
        <cbc:ID>BYF-WB-26-2276</cbc:ID>
        <cbc:DocumentType>Consignment note</cbc:DocumentType>
      </cac:ShipmentDocumentReference>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID schemeID="GS1 SSCC">095206100003729033</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
      <cbc:ShippingMarks>BRIGHTMARKET LUMEPORT / 003 of 006</cbc:ShippingMarks>
      <cbc:TraceID>095206100003729033</cbc:TraceID>
      <cac:HandlingUnitDespatchLine>
        <cbc:ID>1-3</cbc:ID>
        <cbc:DeliveredQuantity unitCode="EA">4</cbc:DeliveredQuantity>
        <cac:OrderLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:OrderLineReference>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>LMW-10442</cbc:ID>
          </cac:SellersItemIdentification>
        </cac:Item>
      </cac:HandlingUnitDespatchLine>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">13</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
        <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1810</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">295</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:TransportEquipment>
        <cbc:ID schemeID="GS1 GRAI">095206100000122251</cbc:ID>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:Description>Returnable pallet of the distributor's pool, 1850 x 700 mm</cbc:Description>
      </cac:TransportEquipment>
      <cac:ShipmentDocumentReference>
        <cbc:ID>BYF-WB-26-2276</cbc:ID>
        <cbc:DocumentType>Consignment note</cbc:DocumentType>
      </cac:ShipmentDocumentReference>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID schemeID="GS1 SSCC">095206100003729040</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
      <cbc:ShippingMarks>BRIGHTMARKET LUMEPORT / 004 of 006</cbc:ShippingMarks>
      <cbc:TraceID>095206100003729040</cbc:TraceID>
      <cac:HandlingUnitDespatchLine>
        <cbc:ID>1-4</cbc:ID>
        <cbc:DeliveredQuantity unitCode="EA">4</cbc:DeliveredQuantity>
        <cac:OrderLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:OrderLineReference>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>LMW-10442</cbc:ID>
          </cac:SellersItemIdentification>
        </cac:Item>
      </cac:HandlingUnitDespatchLine>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">13</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
        <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1810</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">295</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:TransportEquipment>
        <cbc:ID schemeID="GS1 GRAI">095206100000122268</cbc:ID>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:Description>Returnable pallet of the distributor's pool, 1850 x 700 mm</cbc:Description>
      </cac:TransportEquipment>
      <cac:ShipmentDocumentReference>
        <cbc:ID>BYF-WB-26-2276</cbc:ID>
        <cbc:DocumentType>Consignment note</cbc:DocumentType>
      </cac:ShipmentDocumentReference>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID schemeID="GS1 SSCC">095206100003729057</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
      <cbc:ShippingMarks>BRIGHTMARKET LUMEPORT / 005 of 006</cbc:ShippingMarks>
      <cbc:TraceID>095206100003729057</cbc:TraceID>
      <cac:HandlingUnitDespatchLine>
        <cbc:ID>1-5</cbc:ID>
        <cbc:DeliveredQuantity unitCode="EA">4</cbc:DeliveredQuantity>
        <cac:OrderLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:OrderLineReference>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>LMW-10442</cbc:ID>
          </cac:SellersItemIdentification>
        </cac:Item>
      </cac:HandlingUnitDespatchLine>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">13</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
        <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1810</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">295</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:TransportEquipment>
        <cbc:ID schemeID="GS1 GRAI">095206100000122285</cbc:ID>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:Description>Returnable pallet of the distributor's pool, 1850 x 700 mm</cbc:Description>
      </cac:TransportEquipment>
      <cac:ShipmentDocumentReference>
        <cbc:ID>BYF-WB-26-2276</cbc:ID>
        <cbc:DocumentType>Consignment note</cbc:DocumentType>
      </cac:ShipmentDocumentReference>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID schemeID="GS1 SSCC">095206100003729064</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
      <cbc:ShippingMarks>BRIGHTMARKET LUMEPORT / 006 of 006</cbc:ShippingMarks>
      <cbc:TraceID>095206100003729064</cbc:TraceID>
      <cac:HandlingUnitDespatchLine>
        <cbc:ID>1-6</cbc:ID>
        <cbc:DeliveredQuantity unitCode="EA">4</cbc:DeliveredQuantity>
        <cac:OrderLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:OrderLineReference>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>LMW-10442</cbc:ID>
          </cac:SellersItemIdentification>
        </cac:Item>
      </cac:HandlingUnitDespatchLine>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
        <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">790</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">680</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">13</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:ActualPackage>
        <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
        <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1810</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">295</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">100</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ActualPackage>
      <cac:TransportEquipment>
        <cbc:ID schemeID="GS1 GRAI">095206100000122302</cbc:ID>
        <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
        <cbc:Description>Returnable pallet of the distributor's pool, 1850 x 700 mm</cbc:Description>
      </cac:TransportEquipment>
      <cac:ShipmentDocumentReference>
        <cbc:ID>BYF-WB-26-2276</cbc:ID>
        <cbc:DocumentType>Consignment note</cbc:DocumentType>
      </cac:ShipmentDocumentReference>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Six pallets for the reopening of the home and garden department.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">24</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-551210</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>LMW-10442</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9520610000012</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
      </cac:AdditionalItemIdentification>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cac:LotIdentification>
          <cbc:LotNumberID>VI-LOT-260320</cbc:LotNumberID>
          <cac:AdditionalItemProperty>
            <cbc:Name>Coating batch</cbc:Name>
            <cbc:Value>ZN-26-057</cbc:Value>
          </cac:AdditionalItemProperty>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
