# Despatch Advice: Lumeway Distribution to Nalevi Warehousing

*Example 6 of the flow "Urgent spare frames by air (Urvania → Bayvarra → island Lisavu)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The distributor announces the frames to the buyer's 3PL with the flight they are booked on: first the afternoon flight of 13 May, then, replacing it, the morning flight of 14 May.

[The XML file](06-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **AIR-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-DA-26-0327**  
  The despatching party's number.
- `UUID` = **93132e8b-1df2-5401-9265-5f8de7ffa70a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-13**  
  Sent to the buyer's 3PL when the forwarder's truck left the dispatch area for the airport.
- `IssueTime` = **12:15:00-01:00**  
  When the forwarder's truck left the dispatch area, late: Trasvia's truck from Ferrano had arrived late; in the issuer's local time, with its offset from UTC.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage on the air waybill.**  
  What the receiver should do; the note names the transport document the flow uses.
- `LineCountNumeric` = **1**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **VT-OC-26-0320**  
  The order this despatch fulfils.
- `OrderTypeCode` = **230** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 230: the order referred to is an order change. The code is from the world's copy of UN/EDIFACT 1001 Document name: 230 = Purchase order change request.
- `DocumentReference/ID` = **VT-PO-26-0127**  
  The sea order the change extends.
- `DocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: VT-PO-26-0127 is the example sea/05, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.

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
  Street of the postal address. as Lumeway Distribution gives it.
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. as Lumeway Distribution gives it.
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. as Lumeway Distribution gives it.
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. as Lumeway Distribution gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Lumeway Distribution gives it.
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). as Lumeway Distribution gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
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
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Lumeway Distribution gives it.
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

- `Party/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Nalevi Warehousing gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Nalevi Warehousing**  
  The trading name; as Nalevi Warehousing gives it.
- `Party/PostalAddress/ID` = **95940358** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Nalevi Warehousing gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Vilafa Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Nalevi Warehousing gives it.
- `Party/PostalAddress/StreetName` = **Lagoon Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Nalevi Warehousing gives it.
- `Party/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. as Nalevi Warehousing gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. as Nalevi Warehousing gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Nalevi Warehousing gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Goods inwards**  
  The party's main desk, which handles this document; as Nalevi Warehousing gives it.
- `Party/Contact/JobTitle` = **Warehouse supervisor**  
  The job of the person who answers at the desk; as Nalevi Warehousing gives it.
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Nalevi Warehousing gives it.
- `Party/Contact/Telephone` = **+999 3 722 1882**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Nalevi Warehousing gives it.
- `Party/Contact/ElectronicMail` = **goods@nalevi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Nalevi Warehousing gives it.
- `Party/Contact/Note` = **Monday to Saturday 07:00–18:00**  
  When the desk can be reached; as Nalevi Warehousing gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41722** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Nalevi Warehousing gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `Party/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. as Velumi Trading gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. as Velumi Trading gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Velumi Trading gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's main desk, which handles this document; as Velumi Trading gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Party/Contact/Telephone` = **+999 3 729 5794**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Velumi Trading gives it.
- `Party/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Velumi Trading gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **LD-SH-26-0323**  
  The despatching party's shipment number.
- `Consignment/ID` = **LD-CS-26-0324**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/GrossWeightMeasure` = **104.6** (unitCode `KGM`)  
  The eight frame cartons and their skid.
- `Consignment/CarrierParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Kelaro Air Cargo gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/ID` = **58930746** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Cargo operations**  
  The party's cargo operations desk: the desk for its role in this document (it carries or handles the goods); as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/JobTitle` = **Load controller**  
  The job of the person who answers at the desk; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/Telephone` = **+999 3 721 1044**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/ElectronicMail` = **cargoops@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Kelaro Air Cargo gives it.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Air transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **KXL209**  
  The flight the frames are booked on.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XL** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Lisavu**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **ATF** (listID `IATA SSIM Aircraft Types`)  
  The kind of means of transport: ATR 72-600F freighter of Kelaro Air Cargo; the fleet of Kelaro Air Cargo. An ATR 72-600F, the new-built freighter of the ATR 72-600 series (IATA aircraft type code ATF, ICAO type designator AT72): seven LD3 positions on the main deck (one of them for the active temperature-controlled RKN container), about 9,200 kg payload and 75 m³, a large cargo door of 2.94 × 1.80 m. A freighter, so it can carry the lithium batteries that are for cargo aircraft only. The code is from the world's copy of IATA SSIM aircraft type codes: ATF = ATR 72 Freighter.
- `Consignment/MainCarriageShipmentStage/TransportMeans/AirTransport/AircraftID` = **QL-KXA** (schemeID `urn:ubl-examples:world:XL:aircraft-register`)  
  The aircraft's registration: the nationality mark QL of Lisavu, a mark no real state uses, and three letters; the fleet of Kelaro Air Cargo. The schemeID names the scheme it is from: the civil aircraft register of Lisavu (the nationality mark QL, a hyphen and three letters).
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-05-13**  
  Expected at Selanu airport with KXL209.
- `Delivery/EstimatedDeliveryPeriod/StartTime` = **18:45:00+00:00**  
  The flight's timetabled arrival, in island time.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-05-13**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-05-13**  
  The frames left the dispatch area on 13 May.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **Eight side frames, needed before the ship arrives.**  
  The line as the order put it.
- `DeliveredQuantity` = **8** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **4**  
  The order line this line fulfils.
- `Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description.
- `Item/Name` = **Bench side frame casting**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **LD-10443**  
  The seller's own item number; as Lumeway Distribution describes the item.
- `Item/ManufacturersItemIdentification/ID` = **VI-C180**  
  The item number of the maker, Valdara Industries: the reseller sells the maker's item on.
- `Item/ManufacturersItemIdentification/ExtendedID` = **2026**  
  The 2026 casting with the reinforced foot, which replaced the 2025 casting from the order response of the road delivery on: Valdara tells the versions of the same part number apart by the casting year, and every frame made since carries it. as Valdara Industries describes the item.
- `Item/StandardItemIdentification/ID` = **9520610000029** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none.
- `Item/AdditionalItemIdentification/ID` = **KXU10014C180** (schemeID `ISO 15459-6`)  
  The maker's number for the item in its globally unique form under ISO/IEC 15459 (KXU and the company number Codana gave Valdara Industries), which travels along with the GTIN, as an importer may carry it; as Valdara Industries describes the item.
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03190**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03190**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03191**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03191**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03192**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03192**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03193**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03193**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03194**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03194**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03195**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03195**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03196**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03196**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-03197**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-05-12**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **14:15:00**  
  The time the day's melt was poured: an extra melt in the afternoon: the order came on the morning of 11 May and the moulds were made that day and the next.
- `Item/ItemInstance/SerialID` = **VI-SF-03197**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0094**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>AIR-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-DA-26-0327</cbc:ID>
  <cbc:UUID>93132e8b-1df2-5401-9265-5f8de7ffa70a</cbc:UUID>
  <cbc:IssueDate>2026-05-13</cbc:IssueDate>
  <cbc:IssueTime>12:15:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage on the air waybill.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>VT-OC-26-0320</cbc:ID>
    <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">230</cbc:OrderTypeCode>
    <cac:DocumentReference>
      <cbc:ID>VT-PO-26-0127</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
    </cac:DocumentReference>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Nalevi Warehousing</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">95940358</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Vilafa Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Lagoon Road</cbc:StreetName>
        <cbc:BuildingNumber>9</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Goods inwards</cbc:Name>
        <cbc:JobTitle>Warehouse supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 3 722 1882</cbc:Telephone>
        <cbc:ElectronicMail>goods@nalevi.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 07:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41722</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
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
    <cbc:ID>LD-SH-26-0323</cbc:ID>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0324</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">104.6</cbc:GrossWeightMeasure>
      <cac:CarrierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Kelaro Air Cargo</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">58930746</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Airfield Road</cbc:StreetName>
          <cbc:BuildingNumber>46</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Kefalasa</cbc:CityName>
          <cbc:CityName languageID="en-XL">Lintwell</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Cargo operations</cbc:Name>
          <cbc:JobTitle>Load controller</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 3 721 1044</cbc:Telephone>
          <cbc:ElectronicMail>cargoops@kelaro.example</cbc:ElectronicMail>
          <cbc:Note>Every day 06:00–22:00</cbc:Note>
        </cac:Contact>
      </cac:CarrierParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>KXL209</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XL</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Lisavu</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="IATA SSIM Aircraft Types">ATF</cbc:TransportMeansTypeCode>
          <cac:AirTransport>
            <cbc:AircraftID schemeID="urn:ubl-examples:world:XL:aircraft-register">QL-KXA</cbc:AircraftID>
          </cac:AirTransport>
        </cac:TransportMeans>
      </cac:MainCarriageShipmentStage>
    </cac:Consignment>
    <cac:Delivery>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-05-13</cbc:StartDate>
        <cbc:StartTime>18:45:00+00:00</cbc:StartTime>
        <cbc:EndDate>2026-05-13</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-05-13</cbc:ActualDespatchDate>
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Eight side frames, needed before the ship arrives.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">8</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>4</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
      <cbc:Name>Bench side frame casting</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>LD-10443</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-C180</cbc:ID>
        <cbc:ExtendedID>2026</cbc:ExtendedID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9520610000029</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014C180</cbc:ID>
      </cac:AdditionalItemIdentification>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03190</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03190</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03191</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03191</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03192</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03192</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03193</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03193</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03194</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03194</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03195</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03195</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03196</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03196</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-03197</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-05-12</cbc:ManufactureDate>
        <cbc:ManufactureTime>14:15:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-03197</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0094</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
