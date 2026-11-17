# Despatch Advice: Marrowdale Sawmill to Valdara Industries

*Example 6 of the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The sawmill announces the slats per lot, so the factory can trace the wood of every bench.

[The XML file](06-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **WOOD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **MS-DA-26-0633**  
  The despatching party's number.
- `UUID` = **c6cf9b25-d967-5e95-a336-9d69bd3f509d**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-26**  
  The day the truck was loaded at the sawmill.
- `IssueTime` = **08:31:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage on the consignment note.**  
  What the receiver should do; the note names the transport document the flow uses (worklist C30).
- `LineCountNumeric` = **1**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **VI-PO-26-0627**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Marrowdale Sawmill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-296778** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits). identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Marrowdale Sawmill (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 929 329**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/ElectronicMail` = **dispatch@marrowdalesawmill.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Marrowdale Sawmill (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Marrowdale Sawmill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
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
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 518 4274**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **goodsin@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Valdara Industries**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **MS-SH-26-0632**  
  The despatching party's shipment number.
- `Consignment/ID` = **MS-CS-26-0629**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/GrossWeightMeasure` = **21600** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight of the bundles.
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
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
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
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 041 354 4822**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-02-26**  
  Expected after the usual transit by road.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-02-26**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-02-26**  
  The goods left on the day of this advice.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **Slats for 960 benches: five per bench, 96 bundles of 50.**  
  The line as the order put it.
- `DeliveredQuantity` = **4800** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Sawn hardwood slat, 1800 × 95 × 38 mm, planed, kiln dried.**  
  The seller's description; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/Name` = **Hardwood bench slat 1800**  
  The item's short name; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/BuyersItemIdentification/ID` = **VI-R-SL1800**  
  The number the buyer keeps for this item in its own system (world/items.json).
- `Item/SellersItemIdentification/ID` = **MS-SL-1800**  
  The seller's own item number; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item slat-1800 of Marrowdale Sawmill (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Item/CommodityClassification/CommodityCode` = **440799** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item slat-1800 of Marrowdale Sawmill (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 440799 = Wood sawn or chipped lengthwise, of a thickness exceeding 6 mm: other.
- `Item/CommodityClassification/ItemClassificationCode` = **31102** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item slat-1800 of Marrowdale Sawmill (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 31102 = Wood, sawn or chipped lengthwise, sliced or peeled, of a thickness exceeding 6 mm, of non-coniferous wood .
- `Item/AdditionalItemProperty/ID` = **MC**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Moisture content**  
  The name of code MC in the Trade Accord's item property name list.
- `Item/AdditionalItemProperty/NameCode` = **MC** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: MC = Moisture content.
- `Item/AdditionalItemProperty/TestMethod` = **Oven-dry method on samples from each kiln charge**  
  How the value is tested.
- `Item/AdditionalItemProperty/ValueQuantity` = **12** (unitCode `P1`)  
  Its measured value; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/AdditionalItemProperty/ValueQualifier` = **Average of the kiln charge**  
  What the value stands for.
- `Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **QUA**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Wood quality**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Item/AdditionalItemProperty/ItemPropertyRange/MinimumValue` = **10**  
  The lowest value accepted.
- `Item/AdditionalItemProperty/ItemPropertyRange/MaximumValue` = **14**  
  The highest value accepted.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-WD-0012** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **WD**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/SubItemProperty/Name` = **Moisture at the core**  
  Measured at the centre of the slat.
- `Item/AdditionalItemProperty/SubItemProperty/ValueQuantity` = **13** (unitCode `P1`)  
  Its measured value; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Thickness tolerance**  
  How far a slat may be off its thickness.
- `Item/AdditionalItemProperty/RangeDimension/AttributeID` = **THICKNESS** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The dimension the tolerance is for. The code is from the Trade Accord's dimension attribute list: THICKNESS = Thickness. An identifier that holds a code names the code's list in its schemeID.
- `Item/AdditionalItemProperty/RangeDimension/Measure` = **38** (unitCode `MMT`)  
  Its nominal size.
- `Item/AdditionalItemProperty/RangeDimension/MinimumMeasure` = **37.5** (unitCode `MMT`)  
  The smallest size accepted.
- `Item/AdditionalItemProperty/RangeDimension/MaximumMeasure` = **38.5** (unitCode `MMT`)  
  The largest size accepted.
- `Item/AdditionalItemProperty/Name` = **Surface**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Planed on four sides**  
  Its value; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/ItemInstance/ManufactureDate` = **2026-02-23**  
  The day the lot was produced.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **MS-L26-0223**  
  The production lot, from the maker's prefix and the production day; a recall names the lot.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Name` = **Kiln charge**  
  A fact about this lot.
- `Item/ItemInstance/LotIdentification/AdditionalItemProperty/Value` = **K-07**  
  Its value for this lot.
- `Item/Certificate/ID` = **XB-FOR-2025-0118** (schemeID `urn:ubl-examples:world:XB:forestry-register`)  
  The number of the certificate, in the forestry register of Bayvarra, which keeps the certificates issued under each registration; the schemeID names the register and its authority, so no issuer party is needed (decision ID-Q10).
- `Item/Certificate/CertificateTypeCode` = **SUSTFOREST** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  The kind of certificate, as a code. The code is from the Trade Accord's certificate type list: SUSTFOREST = Sustainable forestry.
- `Item/Certificate/CertificateType` = **Sustainable forestry**  
  The name of code SUSTFOREST in the Trade Accord's certificate type list.
- `Item/Certificate/CertificateReferenceID` = **XB-FOR-REG-0118** (schemeID `urn:ubl-examples:world:XB:forestry-register`)  
  The registration the certificate is issued under: the sawmill's own number in the same register, which the certificate's number repeats after its year.
- `Item/Certificate/ApplicableCategoryCode` = **HW** (listID `urn:ubl-examples:world:codelist:CategoryCode`)  
  The category of goods the certificate covers. The code is from the Trade Accord's certified product category list: HW = Hardwood sawn timber.
- `Item/Certificate/ApplicableCategory` = **Hardwood sawn timber**  
  The name of code HW in the Trade Accord's certified product category list.
- `Item/Certificate/CertificateURI` = **https://forestry.xb.example/certificates/XB-FOR-2025-0118**  
  Where the certificate can be checked.
- `Item/Certificate/Remarks` = **The timber comes from forests in Upland State managed for regrowth.**  
  What the certificate states about the goods.
- `Item/Certificate/CertificateValidityPeriod/EndDate` = **2027-12-31**  
  The certificate is valid until then.
- `Item/Certificate/DocumentReference/ID` = **XB-FOR-AUD-2025-0118**  
  The audit report the certificate is based on.
- `Item/Certificate/DocumentReference/DocumentType` = **Forest management audit report**  
  The kind of document referred to, the audit report behind the forestry certificate, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **95** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **THICKNESS** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: THICKNESS = Thickness. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **38** (unitCode `MMT`)  
  Its size.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>WOOD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>MS-DA-26-0633</cbc:ID>
  <cbc:UUID>c6cf9b25-d967-5e95-a336-9d69bd3f509d</cbc:UUID>
  <cbc:IssueDate>2026-02-26</cbc:IssueDate>
  <cbc:IssueTime>08:31:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage on the consignment note.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>VI-PO-26-0627</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
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
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Dispatch office</cbc:Name>
        <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 2 7121 929 329</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
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
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
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
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>MS-SH-26-0632</cbc:ID>
    <cac:Consignment>
      <cbc:ID>MS-CS-26-0629</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">21600</cbc:GrossWeightMeasure>
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
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Planning desk</cbc:Name>
          <cbc:JobTitle>Transport planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 041 354 4822</cbc:Telephone>
          <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
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
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Slats for 960 benches: five per bench, 96 bundles of 50.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">4800</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Sawn hardwood slat, 1800 × 95 × 38 mm, planed, kiln dried.</cbc:Description>
      <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
      <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
      <cbc:Name>Hardwood bench slat 1800</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>VI-R-SL1800</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>MS-SL-1800</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">440799</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">31102</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:AdditionalItemProperty>
        <cbc:ID>MC</cbc:ID>
        <cbc:Name>Moisture content</cbc:Name>
        <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">MC</cbc:NameCode>
        <cbc:TestMethod>Oven-dry method on samples from each kiln charge</cbc:TestMethod>
        <cbc:ValueQuantity unitCode="P1">12</cbc:ValueQuantity>
        <cbc:ValueQualifier>Average of the kiln charge</cbc:ValueQualifier>
        <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
        <cac:ItemPropertyGroup>
          <cbc:ID>QUA</cbc:ID>
          <cbc:Name>Wood quality</cbc:Name>
          <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
        </cac:ItemPropertyGroup>
        <cac:ItemPropertyRange>
          <cbc:MinimumValue>10</cbc:MinimumValue>
          <cbc:MaximumValue>14</cbc:MaximumValue>
        </cac:ItemPropertyRange>
        <cac:StandardPropertyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:property">UR-WD-0012</cbc:ID>
          <cbc:IssuerScopeID>WD</cbc:IssuerScopeID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Codana Identification Agency</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:StandardPropertyIdentification>
        <cac:SubItemProperty>
          <cbc:Name>Moisture at the core</cbc:Name>
          <cbc:ValueQuantity unitCode="P1">13</cbc:ValueQuantity>
        </cac:SubItemProperty>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Thickness tolerance</cbc:Name>
        <cac:RangeDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">THICKNESS</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">38</cbc:Measure>
          <cbc:MinimumMeasure unitCode="MMT">37.5</cbc:MinimumMeasure>
          <cbc:MaximumMeasure unitCode="MMT">38.5</cbc:MaximumMeasure>
        </cac:RangeDimension>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Surface</cbc:Name>
        <cbc:Value>Planed on four sides</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:ItemInstance>
        <cbc:ManufactureDate>2026-02-23</cbc:ManufactureDate>
        <cac:LotIdentification>
          <cbc:LotNumberID>MS-L26-0223</cbc:LotNumberID>
          <cac:AdditionalItemProperty>
            <cbc:Name>Kiln charge</cbc:Name>
            <cbc:Value>K-07</cbc:Value>
          </cac:AdditionalItemProperty>
        </cac:LotIdentification>
      </cac:ItemInstance>
      <cac:Certificate>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:forestry-register">XB-FOR-2025-0118</cbc:ID>
        <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">SUSTFOREST</cbc:CertificateTypeCode>
        <cbc:CertificateType>Sustainable forestry</cbc:CertificateType>
        <cbc:CertificateReferenceID schemeID="urn:ubl-examples:world:XB:forestry-register">XB-FOR-REG-0118</cbc:CertificateReferenceID>
        <cbc:ApplicableCategoryCode listID="urn:ubl-examples:world:codelist:CategoryCode">HW</cbc:ApplicableCategoryCode>
        <cbc:ApplicableCategory>Hardwood sawn timber</cbc:ApplicableCategory>
        <cbc:CertificateURI>https://forestry.xb.example/certificates/XB-FOR-2025-0118</cbc:CertificateURI>
        <cbc:Remarks>The timber comes from forests in Upland State managed for regrowth.</cbc:Remarks>
        <cac:CertificateValidityPeriod>
          <cbc:EndDate>2027-12-31</cbc:EndDate>
        </cac:CertificateValidityPeriod>
        <cac:DocumentReference>
          <cbc:ID>XB-FOR-AUD-2025-0118</cbc:ID>
          <cbc:DocumentType>Forest management audit report</cbc:DocumentType>
        </cac:DocumentReference>
      </cac:Certificate>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1800</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">95</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">THICKNESS</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">38</cbc:Measure>
      </cac:Dimension>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
