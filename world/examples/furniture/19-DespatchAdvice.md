# Despatch Advice: Brackenmere Furniture to Brightmarket Stores

*Example 19 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The furniture maker's despatch advice for the delivery of the opening stock on 23 March, which its invoice cites as the delivery document.

[The XML file](19-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900336121**  
  The collaboration this document belongs to: the store's first order of the Marrow line, with its return. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0201**  
  The despatching party's number.
- `UUID` = **386a4d37-b610-5324-8059-05e98e631801**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-23**  
  Sent when the van left the workshop on the morning of Monday 23 March.
- `IssueTime` = **07:30:00-01:00**  
  When the loaded van left the workshop, before the goods-in opens at the store, about 90 km away; in the issuer's local time, with its offset from UTC.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the pieces when the van unloads and report any damage the same day.**  
  What the store should do: the maker's own van brings the goods, so no consignment note travels with them.
- `LineCountNumeric` = **5**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **7100448162**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Brackenmere Furniture gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. As Brackenmere Furniture gives it.
- `Party/PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. As Brackenmere Furniture gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Brackenmere Furniture gives it.
- `Party/PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). As Brackenmere Furniture gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Brackenmere Furniture gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Trade sales**  
  The party's main desk, which handles this document; as Brackenmere Furniture gives it.
- `Party/Contact/JobTitle` = **Trade sales manager**  
  The job of the person who answers at the desk; as Brackenmere Furniture gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Brackenmere Furniture gives it.
- `Party/Contact/Telephone` = **+999 2 7121 602 606**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Brackenmere Furniture gives it.
- `Party/Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brackenmere Furniture gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Brackenmere Furniture gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Shipment

Inside `Shipment`:

- `ID` = **26-0202**  
  The despatching party's shipment number.
- `GrossWeightMeasure` = **985.4** (unitCode `KGM`)  
  The gross weight of the pieces in their cartons.
- `Delivery/DeliveryLocation/ID` = **9522610900019** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, goods-in of the lumeport store: Brightmarket Stores identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Delivery/DeliveryLocation/Name` = **Brightmarket Stores, goods-in, Lumeport**  
  Where.
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-03-23**  
  Delivered the same day.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-03-23**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-03-23**  
  The van left Marrowdale in the morning.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `DeliveredQuantity` = **12** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow bench, oak**  
  The item's short name.
- `Item/BuyersItemIdentification/ID` = **BM-551005**  
  The buyer's own item number: it resells this item under its own number.
- `Item/SellersItemIdentification/ID` = **BKM-MRW-B14**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `Item/SellersItemIdentification/ExtendedID` = **OAK**  
  The variant of the item: the wood, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **OAK** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: OAK = Oak.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid oak**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **9522610000016** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `ID` = **2**  
  The line number.
- `DeliveredQuantity` = **8** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **2**  
  The order line this line fulfils.
- `Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow bench, ash**  
  The item's short name.
- `Item/BuyersItemIdentification/ID` = **BM-551008**  
  The buyer's own item number: it resells this item under its own number.
- `Item/SellersItemIdentification/ID` = **BKM-MRW-B14**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `Item/SellersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **ASH** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: ASH = Ash.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **9522610000047** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `ID` = **3**  
  The line number.
- `DeliveredQuantity` = **24** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **3**  
  The order line this line fulfils.
- `Item/Description` = **Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow chair, oak**  
  The item's short name.
- `Item/BuyersItemIdentification/ID` = **BM-551006**  
  The buyer's own item number: it resells this item under its own number.
- `Item/SellersItemIdentification/ID` = **BKM-MRW-C**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `Item/SellersItemIdentification/ExtendedID` = **OAK**  
  The variant of the item: the wood, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **OAK** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: OAK = Oak.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid oak**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **9522610000023** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `ID` = **4**  
  The line number.
- `DeliveredQuantity` = **16** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **4**  
  The order line this line fulfils.
- `Item/Description` = **Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow chair, ash**  
  The item's short name.
- `Item/BuyersItemIdentification/ID` = **BM-551009**  
  The buyer's own item number: it resells this item under its own number.
- `Item/SellersItemIdentification/ID` = **BKM-MRW-C**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `Item/SellersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **ASH** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: ASH = Ash.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **9522610000054** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `ID` = **5**  
  The line number.
- `DeliveredQuantity` = **20** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **5**  
  The order line this line fulfils.
- `Item/Description` = **Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.**  
  The seller's description.
- `Item/Name` = **Elderwick care kit**  
  The item's short name.
- `Item/BuyersItemIdentification/ID` = **BM-551007**  
  The buyer's own item number: it resells this item under its own number.
- `Item/SellersItemIdentification/ID` = **BKM-MRW-K**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `Item/StandardItemIdentification/ID` = **9522610000030** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900336121</cbc:ProfileExecutionID>
  <cbc:ID>26-0201</cbc:ID>
  <cbc:UUID>386a4d37-b610-5324-8059-05e98e631801</cbc:UUID>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>07:30:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the pieces when the van unloads and report any damage the same day.</cbc:Note>
  <cbc:LineCountNumeric>5</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>7100448162</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-821551</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Joiners Row</cbc:StreetName>
        <cbc:BuildingNumber>14</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71203</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Trade sales</cbc:Name>
        <cbc:JobTitle>Trade sales manager</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 602 606</cbc:Telephone>
        <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
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
  <cac:Shipment>
    <cbc:ID>26-0202</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">985.4</cbc:GrossWeightMeasure>
    <cac:Delivery>
      <cac:DeliveryLocation>
        <cbc:ID schemeID="GS1 GLN">9522610900019</cbc:ID>
        <cbc:Name>Brightmarket Stores, goods-in, Lumeport</cbc:Name>
      </cac:DeliveryLocation>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-03-23</cbc:StartDate>
        <cbc:EndDate>2026-03-23</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-03-23</cbc:ActualDespatchDate>
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DeliveredQuantity unitCode="EA">12</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow bench, oak</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-551005</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>BKM-MRW-B14</cbc:ID>
        <cbc:ExtendedID>OAK</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">OAK</cbc:DescriptionCode>
          <cbc:Description>Solid oak</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9522610000016</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>2</cbc:ID>
    <cbc:DeliveredQuantity unitCode="EA">8</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow bench, ash</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-551008</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>BKM-MRW-B14</cbc:ID>
        <cbc:ExtendedID>ASH</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">ASH</cbc:DescriptionCode>
          <cbc:Description>Solid ash</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9522610000047</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>3</cbc:ID>
    <cbc:DeliveredQuantity unitCode="EA">24</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow chair, oak</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-551006</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>BKM-MRW-C</cbc:ID>
        <cbc:ExtendedID>OAK</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">OAK</cbc:DescriptionCode>
          <cbc:Description>Solid oak</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9522610000023</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>4</cbc:ID>
    <cbc:DeliveredQuantity unitCode="EA">16</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>4</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow chair, ash</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-551009</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>BKM-MRW-C</cbc:ID>
        <cbc:ExtendedID>ASH</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">ASH</cbc:DescriptionCode>
          <cbc:Description>Solid ash</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9522610000054</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>5</cbc:ID>
    <cbc:DeliveredQuantity unitCode="EA">20</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>5</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.</cbc:Description>
      <cbc:Name>Elderwick care kit</cbc:Name>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-551007</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>BKM-MRW-K</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9522610000030</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
