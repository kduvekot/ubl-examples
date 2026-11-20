# Despatch Advice: Saltmere Engineering to Selanu Telecom

*Example 4 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The engineering firm announces the goods to the telecom company.

[The XML file](04-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SE-DA-26-0718**  
  The despatching party's number.
- `UUID` = **7619027f-bad8-5009-935f-978a56d56a14**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-04**  
  Sent when the goods leave for the airport.
- `IssueTime` = **09:40:00-01:00**  
  When the forwarder's truck left Saltmere's works for the airport, about an hour away; in the issuer's local time, with its offset from UTC.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage on the air waybill.**  
  What the receiver should do; the note names the transport document the flow uses.
- `LineCountNumeric` = **3**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **ST-PO-26-0713**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Saltmere Engineering gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; as Saltmere Engineering gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Saltmere Engineering gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. as Saltmere Engineering gives it.
- `Party/PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. as Saltmere Engineering gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Saltmere Engineering gives it.
- `Party/PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). as Saltmere Engineering gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Saltmere Engineering gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Saltmere Engineering gives it.
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Saltmere Engineering gives it.
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Saltmere Engineering gives it.
- `Party/Contact/Telephone` = **+999 2 7121 930 729**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Saltmere Engineering gives it.
- `Party/Contact/ElectronicMail` = **dispatch@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Saltmere Engineering gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Saltmere Engineering gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Saltmere Engineering gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Telecom gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The trading name; as Selanu Telecom gives it.
- `Party/PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Telecom gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Telecom gives it.
- `Party/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Telecom gives it.
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. as Selanu Telecom gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. as Selanu Telecom gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Selanu Telecom gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Network stores**  
  The party's network stores desk: the desk for its role in this document (it receives the goods); as Selanu Telecom gives it.
- `Party/Contact/JobTitle` = **Stores supervisor**  
  The job of the person who answers at the desk; as Selanu Telecom gives it.
- `Party/Contact/Department` = **Network operations**  
  The department the desk belongs to; as Selanu Telecom gives it.
- `Party/Contact/Telephone` = **+999 3 727 3193**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Selanu Telecom gives it.
- `Party/Contact/ElectronicMail` = **stores@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu Telecom gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Selanu Telecom gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Telecom gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SE-SH-26-0715**  
  The despatching party's shipment number.
- `Consignment/ID` = **SE-CS-26-0716**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/GrossWeightMeasure` = **333.75** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight.
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
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-06-05**  
  Expected after the usual transit by air.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-06-05**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-06-04**  
  The goods left on the day of this advice.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **Twelve modules of 2.4 kWh: four hours of back-up power for the mast.**  
  The line as the order put it.
- `DeliveredQuantity` = **12** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Back-up battery module for telecom masts, lithium-ion, 2.4 kWh, in a steel case.**  
  The seller's description.
- `Item/Name` = **Lithium-ion battery module 48 V 50 Ah**  
  The item's short name.
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **SE-BAT-4850**  
  The seller's own item number; as Saltmere Engineering describes the item.
- `Item/HazardousItem/ID` = **SE-BAT-4850-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds about handling.
- `Item/HazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for gases, lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **147** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 147 = Lithium Ion and Sodium Ion Batteries.
- `Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `Item/HazardousItem/HazardousCategoryCode` = **9** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles.
- `Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `ID` = **2**  
  The line number.
- `Note` = **One pack of ten for the equipment room.**  
  The line as the order put it.
- `DeliveredQuantity` = **1** (unitCode `SET`)  
  What was despatched.
- `OrderLineReference/LineID` = **2**  
  The order line this line fulfils.
- `Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description.
- `Item/Name` = **Ionisation smoke detector set**  
  The item's short name.
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **SE-SMK-10**  
  The seller's own item number; as Saltmere Engineering describes the item.
- `Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label; the UN number on the package.**  
  What the shipper adds about handling.
- `Item/HazardousItem/UNDGCode` = **2911** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2911 = Radioactive material, excepted package – instruments or articles.
- `Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for gases, lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **161** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 161 = Radioactive Materials (Low Level Radiation).
- `Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `Item/HazardousItem/MarkingID` = **UN2911**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `Item/HazardousItem/RadioactiveMaterial/Name` = **Am-241, 10 × 37 kBq (370 kBq) in ionisation smoke detectors**  
  The nuclide and the activity of the pack as carried, in the name: UBL defines ApplicableRadioactiveIsotope for fissile contents only, and americium-241 is not fissile, so the name is the only place left for them.
- `Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Sealed sources inside the detectors, not special form.**  
  Its form.
- `ID` = **3**  
  The line number.
- `Note` = **Five litres for the circuit boards, in 1-litre tins.**  
  The line as the order put it.
- `DeliveredQuantity` = **5** (unitCode `LTR`)  
  What was despatched.
- `OrderLineReference/LineID` = **3**  
  The order line this line fulfils.
- `Item/Description` = **Remover for the protective coating of circuit boards, in 1-litre tins, five to a box.**  
  The seller's description.
- `Item/Name` = **Coating stripper for electronics**  
  The item's short name.
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **SE-CS-01**  
  The seller's own item number; as Saltmere Engineering describes the item.
- `Item/HazardousItem/ID` = **SE-CS-01-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/UNDGCode` = **2920** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2920 = Corrosive liquid, flammable, n.o.s..
- `Item/HazardousItem/UNPackingGroupCode` = **II** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for gases, lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: II = Medium danger.
- `Item/HazardousItem/UNPackingGroup` = **Medium danger**  
  The name of code II in the Trade Accord's packing group list.
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **132** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 132 = Flammable Liquids - Corrosive.
- `Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `Item/HazardousItem/HazardousCategoryCode` = **8** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances.
- `Item/HazardousItem/MarkingID` = **UN2920**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **8** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances. An identifier that holds a code names the code's list in its schemeID.
- `Item/HazardousItem/SecondaryHazard/ID` = **3** (schemeID `UN Model Regulations hazard class`)  
  The subsidiary hazard: flammable. The code is from the world's copy of UN Model Regulations hazard class and division: 3 = Flammable liquids. An identifier that holds a code names the code's list in its schemeID.
- `Item/HazardousItem/SecondaryHazard/PlacardNotation` = **3**  
  Shown on a second label.
- `Item/HazardousItem/SecondaryHazard/Extension` = **Subsidiary risk 3**  
  In words.
- `Item/HazardousItem/FlashpointTemperature/AttributeID` = **FLASHPOINT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Closed cup. The code is from the Trade Accord's temperature attribute list: FLASHPOINT = Flashpoint. An identifier that holds a code names the code's list in its schemeID.
- `Item/HazardousItem/FlashpointTemperature/Measure` = **28** (unitCode `CEL`)  
  The flashpoint.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SE-DA-26-0718</cbc:ID>
  <cbc:UUID>7619027f-bad8-5009-935f-978a56d56a14</cbc:UUID>
  <cbc:IssueDate>2026-06-04</cbc:IssueDate>
  <cbc:IssueTime>09:40:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage on the air waybill.</cbc:Note>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>ST-PO-26-0713</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saltmere Engineering</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-587295</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Foundry Road</cbc:StreetName>
        <cbc:BuildingNumber>13</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71218</cbc:PostalZone>
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
        <cbc:Telephone>+999 2 7121 930 729</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@saltmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">34928611</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Mast Hill Road</cbc:StreetName>
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
        <cbc:Name>Network stores</cbc:Name>
        <cbc:JobTitle>Stores supervisor</cbc:JobTitle>
        <cbc:Department>Network operations</cbc:Department>
        <cbc:Telephone>+999 3 727 3193</cbc:Telephone>
        <cbc:ElectronicMail>stores@selanutelecom.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saltmere Engineering</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>SE-SH-26-0715</cbc:ID>
    <cac:Consignment>
      <cbc:ID>SE-CS-26-0716</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">333.75</cbc:GrossWeightMeasure>
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
    </cac:Consignment>
    <cac:Delivery>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-06-05</cbc:StartDate>
        <cbc:EndDate>2026-06-05</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-06-04</cbc:ActualDespatchDate>
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Twelve modules of 2.4 kWh: four hours of back-up power for the mast.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">12</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Back-up battery module for telecom masts, lithium-ion, 2.4 kWh, in a steel case.</cbc:Description>
      <cbc:Name>Lithium-ion battery module 48 V 50 Ah</cbc:Name>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:SellersItemIdentification>
        <cbc:ID>SE-BAT-4850</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:HazardousItem>
        <cbc:ID>SE-BAT-4850-DG</cbc:ID>
        <cbc:AdditionalInformation>State of charge below 30 %, as the air rules require.</cbc:AdditionalInformation>
        <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">3480</cbc:UNDGCode>
        <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
        <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
        <cbc:MedicalFirstAidGuideCode listID="ERG 2024">147</cbc:MedicalFirstAidGuideCode>
        <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
        <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">9</cbc:HazardousCategoryCode>
        <cbc:MarkingID>UN3480</cbc:MarkingID>
        <cbc:HazardClassID schemeID="UN Model Regulations hazard class">9</cbc:HazardClassID>
      </cac:HazardousItem>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>One pack of ten for the equipment room.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="SET">1</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.</cbc:Description>
      <cbc:Name>Ionisation smoke detector set</cbc:Name>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:SellersItemIdentification>
        <cbc:ID>SE-SMK-10</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:HazardousItem>
        <cbc:ID>SE-SMK-10-DG</cbc:ID>
        <cbc:AdditionalInformation>Excepted package: no radioactive label; the UN number on the package.</cbc:AdditionalInformation>
        <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2911</cbc:UNDGCode>
        <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
        <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
        <cbc:MedicalFirstAidGuideCode listID="ERG 2024">161</cbc:MedicalFirstAidGuideCode>
        <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
        <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
        <cbc:MarkingID>UN2911</cbc:MarkingID>
        <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
        <cac:RadioactiveMaterial>
          <cbc:Name>Am-241, 10 × 37 kBq (370 kBq) in ionisation smoke detectors</cbc:Name>
          <cbc:SpecialFormDescription>Sealed sources inside the detectors, not special form.</cbc:SpecialFormDescription>
        </cac:RadioactiveMaterial>
      </cac:HazardousItem>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>3</cbc:ID>
    <cbc:Note>Five litres for the circuit boards, in 1-litre tins.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="LTR">5</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Remover for the protective coating of circuit boards, in 1-litre tins, five to a box.</cbc:Description>
      <cbc:Name>Coating stripper for electronics</cbc:Name>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:SellersItemIdentification>
        <cbc:ID>SE-CS-01</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:HazardousItem>
        <cbc:ID>SE-CS-01-DG</cbc:ID>
        <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2920</cbc:UNDGCode>
        <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">II</cbc:UNPackingGroupCode>
        <cbc:UNPackingGroup>Medium danger</cbc:UNPackingGroup>
        <cbc:MedicalFirstAidGuideCode listID="ERG 2024">132</cbc:MedicalFirstAidGuideCode>
        <cbc:TechnicalName>ethanolamine, propanol</cbc:TechnicalName>
        <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
        <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">8</cbc:HazardousCategoryCode>
        <cbc:MarkingID>UN2920</cbc:MarkingID>
        <cbc:HazardClassID schemeID="UN Model Regulations hazard class">8</cbc:HazardClassID>
        <cac:SecondaryHazard>
          <cbc:ID schemeID="UN Model Regulations hazard class">3</cbc:ID>
          <cbc:PlacardNotation>3</cbc:PlacardNotation>
          <cbc:Extension>Subsidiary risk 3</cbc:Extension>
        </cac:SecondaryHazard>
        <cac:FlashpointTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">FLASHPOINT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">28</cbc:Measure>
        </cac:FlashpointTemperature>
      </cac:HazardousItem>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
