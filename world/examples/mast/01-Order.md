# Order: Selanu Telecom to Saltmere Engineering

*Example 1 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The telecom company orders back-up power and safety equipment for its mast. Carriage paid to the mast site: the seller arranges the dangerous goods transport.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **STL-TX-26-124393**  
  The collaboration this document belongs to: Selanu Telecom's order of back-up batteries, smoke detectors and coating stripper for its mast from Saltmere Engineering. Selanu Telecom started it and gave it this identifier, which every document of it repeats.
- `ID` = **STL-PO-26-0374**  
  The buyer's order number.
- `UUID` = **b63839e1-7b35-5e81-a17d-ef60734d2fe6**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-01**  
  The telecom company orders before the storm season.
- `IssueTime` = **08:15:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **3**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Telecom gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The trading name; as Selanu Telecom gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
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
  Building number of the postal address. As Selanu Telecom gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Selanu Telecom gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Selanu Telecom gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Selanu Telecom gives it.
- `Party/Contact/Telephone` = **+999 3 727 3193**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Telecom gives it.
- `Party/Contact/ElectronicMail` = **purchasing@selanutelecom.example**  
  The contact's e-mail address; as Selanu Telecom gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Selanu Telecom gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Telecom gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Saltmere Engineering gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; as Saltmere Engineering gives it.
- `Party/PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Saltmere Engineering gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. As Saltmere Engineering gives it.
- `Party/PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. As Saltmere Engineering gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Saltmere Engineering gives it.
- `Party/PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). As Saltmere Engineering gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Saltmere Engineering gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Saltmere Engineering gives it.
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Saltmere Engineering gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Saltmere Engineering gives it.
- `Party/Contact/Telephone` = **+999 2 7121 930 729**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Saltmere Engineering gives it.
- `Party/Contact/ElectronicMail` = **sales@saltmere.example**  
  The contact's e-mail address; as Saltmere Engineering gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Saltmere Engineering gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Saltmere Engineering gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-06-04**  
  The equipment is wanted at the mast site on 4 or 5 June.
- `RequestedDeliveryPeriod/EndDate` = **2026-06-05**  
  The last day it is wanted.
- `DeliveryParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Selanu Telecom**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CPT** (schemeID `INCOTERMS`)  
  Carriage paid to the telecom company's mast site: the seller arranges the dangerous goods transport. The code is from the world's copy of Incoterms 2020: CPT = Carriage Paid To. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/Description` = **Selanu Telecom's mast site on Mast Hill**  
  Where the delivery terms place the handover of the goods.
- `DeliveryLocation/Address/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `DeliveryLocation/Address/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `DeliveryLocation/Address/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Telecom gives it.
- `DeliveryLocation/Address/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Telecom gives it.
- `DeliveryLocation/Address/BuildingNumber` = **58**  
  Building number of the postal address. As Selanu Telecom gives it.
- `DeliveryLocation/Address/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `DeliveryLocation/Address/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `DeliveryLocation/Address/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `DeliveryLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `DeliveryLocation/Address/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **14627.50** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **14627.50** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **14627.50** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **12** (unitCode `EA`)  
  Twelve modules of 2.4 kWh: four hours of back-up power for the mast.
- `LineItem/LineExtensionAmount` = **14400.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **1200** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Back-up battery module for telecom masts, lithium-ion, 2.4 kWh, in a steel case.**  
  The seller's description.
- `LineItem/Item/Name` = **Lithium-ion battery module 48 V 50 Ah**  
  The item's short name.
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-BAT-4850**  
  The seller's own item number; as Saltmere Engineering describes the item.
- `LineItem/Item/HazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number of the goods ordered, so that the seller ships them as the dangerous goods they are. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `LineItem/Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name of the UN entry, as the Dangerous Goods List gives it for that UN number and class.
- `LineItem/Item/HazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/ID` = **2**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **1** (unitCode `SET`)  
  One pack of ten for the equipment room.
- `LineItem/LineExtensionAmount` = **180.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **180** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `SET`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description.
- `LineItem/Item/Name` = **Ionisation smoke detector set**  
  The item's short name.
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-SMK-10**  
  The seller's own item number; as Saltmere Engineering describes the item.
- `LineItem/Item/HazardousItem/UNDGCode` = **2911** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number of the goods ordered, so that the seller ships them as the dangerous goods they are. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2911 = Radioactive material, excepted package – instruments or articles.
- `LineItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name of the UN entry, as the Dangerous Goods List gives it for that UN number and class.
- `LineItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/ID` = **3**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **5** (unitCode `LTR`)  
  Five litres for the circuit boards, in 1-litre tins.
- `LineItem/LineExtensionAmount` = **47.50** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **9.5** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `LTR`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Remover for the protective coating of circuit boards, in 1-litre tins, five to a box.**  
  The seller's description.
- `LineItem/Item/Name` = **Coating stripper for electronics**  
  The item's short name.
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-CS-01**  
  The seller's own item number; as Saltmere Engineering describes the item.
- `LineItem/Item/HazardousItem/UNDGCode` = **2920** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number of the goods ordered, so that the seller ships them as the dangerous goods they are. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2920 = Corrosive liquid, flammable, n.o.s..
- `LineItem/Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name of the UN entry, as the Dangerous Goods List gives it for that UN number and class.
- `LineItem/Item/HazardousItem/HazardClassID` = **8** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/HazardousItem/SecondaryHazard/ID` = **3** (schemeID `UN Model Regulations hazard class`)  
  The subsidiary hazard: flammable. The code is from the world's copy of UN Model Regulations hazard class and division: 3 = Flammable liquids. An identifier that holds a code names the code's list in its schemeID.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>STL-TX-26-124393</cbc:ProfileExecutionID>
  <cbc:ID>STL-PO-26-0374</cbc:ID>
  <cbc:UUID>b63839e1-7b35-5e81-a17d-ef60734d2fe6</cbc:UUID>
  <cbc:IssueDate>2026-06-01</cbc:IssueDate>
  <cbc:IssueTime>08:15:00+00:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
      </cac:Language>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 3 727 3193</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@selanutelecom.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
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
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 930 729</cbc:Telephone>
        <cbc:ElectronicMail>sales@saltmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-06-04</cbc:StartDate>
      <cbc:EndDate>2026-06-05</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CPT</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>Selanu Telecom's mast site on Mast Hill</cbc:Description>
      <cac:Address>
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
      </cac:Address>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">14627.50</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">14627.50</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">14627.50</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">14400.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">1200</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Back-up battery module for telecom masts, lithium-ion, 2.4 kWh, in a steel case.</cbc:Description>
        <cbc:Name>Lithium-ion battery module 48 V 50 Ah</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-BAT-4850</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:HazardousItem>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">3480</cbc:UNDGCode>
          <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">9</cbc:HazardClassID>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="SET">1</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">180.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">180</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="SET">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.</cbc:Description>
        <cbc:Name>Ionisation smoke detector set</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-SMK-10</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:HazardousItem>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2911</cbc:UNDGCode>
          <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="LTR">5</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">47.50</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">9.5</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="LTR">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Remover for the protective coating of circuit boards, in 1-litre tins, five to a box.</cbc:Description>
        <cbc:Name>Coating stripper for electronics</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-CS-01</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:HazardousItem>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2920</cbc:UNDGCode>
          <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">8</cbc:HazardClassID>
          <cac:SecondaryHazard>
            <cbc:ID schemeID="UN Model Regulations hazard class">3</cbc:ID>
          </cac:SecondaryHazard>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
