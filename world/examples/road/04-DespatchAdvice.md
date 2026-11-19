# Despatch Advice: Castrano Logistics to Lumeway Distribution

*Example 4 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The 3PL picks and loads the goods for the manufacturer and announces the despatch; it knows the goods and the truck but not the prices.

[The XML file](04-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **CL-DA-26-0153**  
  The despatching party's number.
- `UUID` = **50f13b62-45d2-51db-aea9-a8873a59c837**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-23**  
  The day the 3PL loaded the truck.
- `IssueTime` = **16:38:00-01:00**  
  Issued a few minutes after the last thing of its day that it reports or cites, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage in your receipt advice.**  
  What the receiver should do; the note names the transport document the flow uses (worklist C30).
- `LineCountNumeric` = **2**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **LD-PO-26-0149**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Castrano Logistics (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10519** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Castrano Logistics (world/parties.json).
- `Party/PartyName/Name` = **Castrano Logistics**  
  The trading name; identity of Castrano Logistics (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `Party/PostalAddress/ID` = **4160203920705699** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **24**  
  Building number of the postal address. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it (world/map.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Loading bays**  
  The party's loading bays desk: the desk for its role in this document (it sends the goods off); identity of Castrano Logistics (world/parties.json).
- `Party/Contact/JobTitle` = **Shift supervisor**  
  The job of the person who answers at the desk; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 909 1454**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Castrano Logistics (world/parties.json).
- `Party/Contact/ElectronicMail` = **loading@castrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Castrano Logistics (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Castrano Logistics (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/ElectronicMail` = **goodsin@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Order desk**  
  The party's main desk, which handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Order administrator**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 351 400 5258**  
  The sales desk's mobile number, also under the reserved +999.

### Shipment

Inside `Shipment`:

- `ID` = **CL-SH-26-0154**  
  The despatching party's shipment number.
- `Consignment/ID` = **LD-CS-26-0152**  
  The distributor's consignment for the truck.
- `Consignment/GrossWeightMeasure` = **5363.4** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight loaded, packaging included.
- `Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/ID` = **4160203746888095** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Planning desk**  
  The party's main desk, which handles this document; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/JobTitle` = **Transport planner**  
  The job of the person who answers at the desk; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 041 266 7643**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `Delivery/Despatch/ID` = **CL-OUT-26-0871**  
  The 3PL's outbound number.
- `Delivery/Despatch/ActualDespatchDate` = **2026-03-23**  
  Loaded and gone.
- `Delivery/Despatch/ActualDespatchTime` = **16:20:00**  
  The truck left the gate.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **24 pallets of four benches, on a truck booked for this delivery alone.**  
  The line as the order put it.
- `DeliveredQuantity` = **96** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/Description` = **Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Park bench Serra 180** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/BuyersItemIdentification/ID` = **LD-10442**  
  The buyer's own item number: it resells this item as its item bench-serra-b.
- `Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
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
- `Item/StandardItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Valdara Industries gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Valdara Industries and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; item bench-serra of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label: Code 128 carries letters and digits.
- `Item/StandardItemIdentification/IssuerScopeID` = **KXU10014**  
  The scope within which Valdara Industries gives its item numbers: its company prefix, the issuing agency code KXU and its Codana company number; what follows is the company's own reference.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the lot was produced.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **VI-LOT-260320**  
  The production lot, from the maker's prefix and the production day; a recall names the lot.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Name` = **Coating batch**  
  A fact about this lot: the galvanising and powder-coating batch its frames went through.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Value` = **ZN-26-057**  
  Its batch: each lot has its own, in the coating line's running count of the year (the production record, world/items.json goods_chain, D21).
- `ID` = **2**  
  The line number.
- `Note` = **Spare side frames, for the distributor's service stock.**  
  The line as the order put it.
- `DeliveredQuantity` = **12** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **2**  
  The order line this line fulfils.
- `Item/Description` = **Zudrir drir manskan gan drek Serra nanskir, zhukvan stezir gek, vazzhan stan krarhir-trunnir.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Item/Description` = **Replacement side frame for the Serra bench, ductile cast iron, galvanised and powder-coated.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Item/Name` = **Bench side frame casting** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Item/BuyersItemIdentification/ID` = **LD-10443**  
  The buyer's own item number: it resells this item as its item bench-casting-b.
- `Item/SellersItemIdentification/ID` = **VI-C180**  
  The seller's own item number; item bench-casting of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/ID` = **KXU10014C180** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Valdara Industries gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Valdara Industries and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; item bench-casting of Valdara Industries (world/items.json).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01490**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01490**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01491**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01491**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01492**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01492**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01493**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01493**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01494**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01494**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01495**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01495**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01496**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01496**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01497**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01497**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01498**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01498**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01499**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01499**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01500**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01500**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).
- `Item/ItemInstance/ProductTraceID` = **VI-TR-01501**  
  The trace code on the casting's label, for the maker's tracing system.
- `Item/ItemInstance/ManufactureDate` = **2026-03-20**  
  The day the casting was poured and inspected.
- `Item/ItemInstance/ManufactureTime` = **06:40:00**  
  The time the day's melt was poured, the foundry's first melt of the day.
- `Item/ItemInstance/SerialID` = **VI-SF-01501**  
  The serial number cast into the frame; every casting is traceable to its melt, and the numbers rise with the day of casting.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Melt number**  
  A fact about this one casting: the melt of iron it was poured from.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **M-26-0057**  
  Its melt: one per casting day, in the foundry's running count of the year (the production record, world/items.json goods_chain, D21).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>CL-DA-26-0153</cbc:ID>
  <cbc:UUID>50f13b62-45d2-51db-aea9-a8873a59c837</cbc:UUID>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>16:38:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage in your receipt advice.</cbc:Note>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>LD-PO-26-0149</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10519</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Castrano Logistics</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160203920705699</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
        <cbc:BuildingNumber>24</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
        <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
        <cbc:PostalZone>4190</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Loading bays</cbc:Name>
        <cbc:JobTitle>Shift supervisor</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 1 041 909 1454</cbc:Telephone>
        <cbc:ElectronicMail>loading@castrano.example</cbc:ElectronicMail>
        <cbc:Note>Every day 06:00–22:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
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
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
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
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Order administrator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
          <cbc:Value>+999 1 351 400 5258</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>CL-SH-26-0154</cbc:ID>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0152</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">5363.4</cbc:GrossWeightMeasure>
      <cac:CarrierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Trasvia Haulage</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160203746888095</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qau">Bek Ban Kumek</cbc:StreetName>
          <cbc:StreetName languageID="en-XU">Via dei Trasporti</cbc:StreetName>
          <cbc:BuildingNumber>45</cbc:BuildingNumber>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
          <cbc:PostalZone>4160</cbc:PostalZone>
          <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
          <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Planning desk</cbc:Name>
          <cbc:JobTitle>Transport planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 041 266 7643</cbc:Telephone>
          <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
          <cbc:Note>Every day 06:00–22:00</cbc:Note>
        </cac:Contact>
      </cac:CarrierParty>
    </cac:Consignment>
    <cac:Delivery>
      <cac:Despatch>
        <cbc:ID>CL-OUT-26-0871</cbc:ID>
        <cbc:ActualDespatchDate>2026-03-23</cbc:ActualDespatchDate>
        <cbc:ActualDespatchTime>16:20:00</cbc:ActualDespatchTime>
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>24 pallets of four benches, on a truck booked for this delivery alone.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">96</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.</cbc:Description>
      <cbc:Description languageID="en-XU">Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.</cbc:Description>
      <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
      <cbc:Name languageID="en-XU">Park bench Serra 180</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>LD-10442</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
        <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
        <cbc:IssuerScopeID>KXU10014</cbc:IssuerScopeID>
      </cac:StandardItemIdentification>
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
  <cac:DespatchLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Spare side frames, for the distributor's service stock.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">12</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description languageID="qau">Zudrir drir manskan gan drek Serra nanskir, zhukvan stezir gek, vazzhan stan krarhir-trunnir.</cbc:Description>
      <cbc:Description languageID="en-XU">Replacement side frame for the Serra bench, ductile cast iron, galvanised and powder-coated.</cbc:Description>
      <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
      <cbc:Name languageID="en-XU">Bench side frame casting</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>LD-10443</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-C180</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014C180</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01490</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01490</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01491</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01491</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01492</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01492</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01493</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01493</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01494</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01494</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01495</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01495</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01496</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01496</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01497</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01497</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01498</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01498</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01499</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01499</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01500</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01500</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
      <cac:ItemInstance>
        <cbc:ProductTraceID>VI-TR-01501</cbc:ProductTraceID>
        <cbc:ManufactureDate>2026-03-20</cbc:ManufactureDate>
        <cbc:ManufactureTime>06:40:00</cbc:ManufactureTime>
        <cbc:SerialID>VI-SF-01501</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Melt number</cbc:Name>
          <cbc:Value>M-26-0057</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
