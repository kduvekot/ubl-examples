# Despatch Advice: Tostara Wood Modification to Valdara Industries

*Example 6 of the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The modification plant despatches the 96 bundles for the sawmill, which sold them: it announces them on their 24 pallets with the lot of each kiln charge, so the factory can trace the wood of every bench, and records the pick-up release they left under.

[The XML file](06-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900042764**  
  The collaboration this document belongs to: Valdara's purchase of slats from Marrowdale Sawmill. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0063**  
  The despatching party's number.
- `UUID` = **c6cf9b25-d967-5e95-a336-9d69bd3f509d**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-26**  
  The day the plant loaded the bundles onto Trasvia's truck.
- `IssueTime` = **09:30:00-01:00**  
  When the truck is loaded, after the slats were released into free circulation; in the issuer's local time, with its offset from UTC.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Sasul gan Marrowdale Sawmill, drek balhan, mir nakskek gakek hir zek halkan. Gannek kikran drek valnir rek marsir stan skuskek ran muhir rek drek silsan mek.** (languageID `qau`)  
  The note in Urvanian, the sender's language: Who the plant despatches for, and what the receiver should do.
- `Note` = **Despatched for Marrowdale Sawmill, the seller, from its job at our plant. Please check the goods on arrival and report any damage on the consignment note.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: Who the plant despatches for, and what the receiver should do.
- `LineCountNumeric` = **2**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **4500042882**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Tostara Wood Modification**  
  The trading name; as Tostara Wood Modification gives it.
- `Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/ID` = **4160205830117402** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Tostara Wood Modification gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Tuntrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Tostara Wood Modification gives it.
- `Party/PostalAddress/StreetName` = **Via delle Concerie** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Tostara Wood Modification gives it.
- `Party/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Tostara Wood Modification gives it.
- `Party/PostalAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `Party/PostalAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `Party/PostalAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Tostara Wood Modification gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Tostara Wood Modification gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Despatch desk**  
  The party's despatch desk: the desk for its role in this document (it sends the goods off); as Tostara Wood Modification gives it.
- `Party/Contact/JobTitle` = **Despatch coordinator**  
  The job of the person who answers at the desk; as Tostara Wood Modification gives it.
- `Party/Contact/Department` = **Yard**  
  The department the desk belongs to; as Tostara Wood Modification gives it.
- `Party/Contact/Telephone` = **+999 1 041 573 2290**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Tostara Wood Modification gives it.
- `Party/Contact/ElectronicMail` = **despatch@tostara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Tostara Wood Modification gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Tostara Wood Modification gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-106192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Valdara Industries gives it.
- `Party/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Party/Contact/ElectronicMail` = **goodsin@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Valdara Industries**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; as Marrowdale Sawmill gives it.
- `Party/PostalAddress/ID` = **UL-ADR-296778** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Marrowdale Sawmill gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits). As Marrowdale Sawmill gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Marrowdale Sawmill gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; as Marrowdale Sawmill gives it.
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Marrowdale Sawmill gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Marrowdale Sawmill gives it.
- `Party/Contact/Telephone` = **+999 2 7121 338 173**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Marrowdale Sawmill gives it.
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Marrowdale Sawmill gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Marrowdale Sawmill gives it.

### Shipment

Inside `Shipment`:

- `ID` = **26-0062**  
  The despatching party's shipment number.
- `Consignment/ID` = **MDS-CS-26-0221**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/ConsignorAssignedID` = **26-0064**  
  The plant's own number for the consignment, on its loading list and gate pass; the consignment's ID above is the sawmill's, which booked the transport.
- `Consignment/GrossWeightMeasure` = **21024** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight of the bundles with their pallets.
- `Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Trasvia Haulage gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/ID` = **4160203746888095** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Planning desk**  
  The party's main desk, which handles this document; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/JobTitle` = **Transport planner**  
  The job of the person who answers at the desk; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 041 266 7643**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Trasvia Haulage gives it.
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-02-26**  
  Expected after the usual transit by road.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-02-26**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-02-26**  
  The goods left on the day of this advice.
- `Delivery/Despatch/ReleaseID` = **MDS-REL-26-0212**  
  The sawmill's pick-up release the goods left under: the plant handed them only to the driver who quoted it, for they are the sawmill's.
- `TransportHandlingUnit/ID` = **TWM-26-001**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-002**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-003**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-004**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-005**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-006**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-007**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-008**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-009**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-010**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-011**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-012**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-013**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-014**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-015**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-016**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-017**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-018**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-019**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-020**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-021**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-022**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-023**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.
- `TransportHandlingUnit/ID` = **TWM-26-024**  
  The number on the pallet label: Tostara Wood Modification's own number for the unit.
- `TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `TransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.**  
  The handling, in words, with the world's rule for manual handling.
- `TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 bundles on each pallet, two by two.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length: the slats' 1,800 mm and 25 mm at each end.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **970** (unitCode `MMT`)  
  Its width: two bundles of 475 mm side by side, 20 mm apart.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **1022** (unitCode `MMT`)  
  Two bundles of 450 mm on the pallet of 122 mm.
- `TransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/MeasurementDimension/Measure` = **876** (unitCode `KGM`)  
  Four bundles of 212.5 kg and the pallet's own 26 kg.
- `TransportHandlingUnit/Package/Quantity` = **50** (unitCode `EA`)  
  50 slats in a bundle.
- `TransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `TransportHandlingUnit/Package/PackingMaterial` = **Steel straps**  
  What holds a bundle together.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **The bundles of kiln charge 1, from the first load of blanks, lot MDS-L26-0119.**  
  The line as the order put it.
- `DeliveredQuantity` = **48** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.**  
  The seller's description.
- `Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; as Marrowdale Sawmill describes the item.
- `Item/Name` = **Bench slat 1800, bundle of 50**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **MDS-SL-1800-50**  
  The seller's own item number; as Marrowdale Sawmill describes the item.
- `Item/ItemInstance/ManufactureDate` = **2026-01-19**  
  The day kiln charge 1 came out of the plant's kiln.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **MDS-L26-0119**  
  The sawmill's lot of the slats, one per kiln charge: a recall names the lot.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Name` = **Kiln charge**  
  A fact about this lot: the charge of the plant's kiln it was modified in.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Value` = **TWM-K1-26-03**  
  The plant's number of the charge.
- `ID` = **2**  
  The line number.
- `Note` = **The bundles of kiln charge 2, from the second load of blanks, lot MDS-L26-0126.**  
  The line as the order put it.
- `DeliveredQuantity` = **48** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.**  
  The seller's description.
- `Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; as Marrowdale Sawmill describes the item.
- `Item/Name` = **Bench slat 1800, bundle of 50**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **MDS-SL-1800-50**  
  The seller's own item number; as Marrowdale Sawmill describes the item.
- `Item/ItemInstance/ManufactureDate` = **2026-01-26**  
  The day kiln charge 2 came out of the plant's kiln.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **MDS-L26-0126**  
  The sawmill's lot of the slats, one per kiln charge: a recall names the lot.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Name` = **Kiln charge**  
  A fact about this lot: the charge of the plant's kiln it was modified in.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Value` = **TWM-K1-26-04**  
  The plant's number of the charge.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900042764</cbc:ProfileExecutionID>
  <cbc:ID>26-0063</cbc:ID>
  <cbc:UUID>c6cf9b25-d967-5e95-a336-9d69bd3f509d</cbc:UUID>
  <cbc:IssueDate>2026-02-26</cbc:IssueDate>
  <cbc:IssueTime>09:30:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note languageID="qau">Sasul gan Marrowdale Sawmill, drek balhan, mir nakskek gakek hir zek halkan. Gannek kikran drek valnir rek marsir stan skuskek ran muhir rek drek silsan mek.</cbc:Note>
  <cbc:Note languageID="en-XU">Despatched for Marrowdale Sawmill, the seller, from its job at our plant. Please check the goods on arrival and report any damage on the consignment note.</cbc:Note>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>4500042882</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tostara Wood Modification</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160205830117402</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Tuntrir</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Concerie</cbc:StreetName>
        <cbc:BuildingNumber>9</cbc:BuildingNumber>
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
        <cbc:Name>Despatch desk</cbc:Name>
        <cbc:JobTitle>Despatch coordinator</cbc:JobTitle>
        <cbc:Department>Yard</cbc:Department>
        <cbc:Telephone>+999 1 041 573 2290</cbc:Telephone>
        <cbc:ElectronicMail>despatch@tostara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-106192</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
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
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-296778</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Timber Lane</cbc:StreetName>
        <cbc:BuildingNumber>7</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71202</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 338 173</cbc:Telephone>
        <cbc:ElectronicMail>sales@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>26-0062</cbc:ID>
    <cac:Consignment>
      <cbc:ID>MDS-CS-26-0221</cbc:ID>
      <cbc:ConsignorAssignedID>26-0064</cbc:ConsignorAssignedID>
      <cbc:GrossWeightMeasure unitCode="KGM">21024</cbc:GrossWeightMeasure>
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
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-02-26</cbc:StartDate>
        <cbc:EndDate>2026-02-26</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-02-26</cbc:ActualDespatchDate>
        <cbc:ReleaseID>MDS-REL-26-0212</cbc:ReleaseID>
      </cac:Despatch>
    </cac:Delivery>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-001</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-002</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-003</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-004</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-005</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-006</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-007</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-008</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-009</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-010</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-011</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-012</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-013</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-014</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-015</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-016</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-017</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-018</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-019</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-020</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-021</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-022</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-023</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cbc:ID>TWM-26-024</cbc:ID>
      <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
      <cbc:HandlingInstructions>Fork-lift only. May be stacked two high. A bundle of 212.5 kg is lifted by machine, never by hand.</cbc:HandlingInstructions>
      <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1850</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">970</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1022</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="KGM">876</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:Package>
        <cbc:Quantity unitCode="EA">50</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel straps</cbc:PackingMaterial>
      </cac:Package>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>The bundles of kiln charge 1, from the first load of blanks, lot MDS-L26-0119.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">48</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.</cbc:Description>
      <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
      <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
      <cbc:Name>Bench slat 1800, bundle of 50</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>MDS-SL-1800-50</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-01-19</cbc:ManufactureDate>
        <cac:LotIdentification>
          <cbc:LotNumberID>MDS-L26-0119</cbc:LotNumberID>
          <cac:AdditionalItemProperty>
            <cbc:Name>Kiln charge</cbc:Name>
            <cbc:Value>TWM-K1-26-03</cbc:Value>
          </cac:AdditionalItemProperty>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>The bundles of kiln charge 2, from the second load of blanks, lot MDS-L26-0126.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">48</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.</cbc:Description>
      <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
      <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
      <cbc:Name>Bench slat 1800, bundle of 50</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>MDS-SL-1800-50</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-01-26</cbc:ManufactureDate>
        <cac:LotIdentification>
          <cbc:LotNumberID>MDS-L26-0126</cbc:LotNumberID>
          <cac:AdditionalItemProperty>
            <cbc:Name>Kiln charge</cbc:Name>
            <cbc:Value>TWM-K1-26-04</cbc:Value>
          </cac:AdditionalItemProperty>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
