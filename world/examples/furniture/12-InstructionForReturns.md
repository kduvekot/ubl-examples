# Instruction For Returns: Brackenmere Furniture to Brightmarket Stores

*Example 12 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Instruction For Returns in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INSTRUCTION-FOR-RETURNS-SCHEMA)*

After the sale-or-return trial, the first four weeks of sales, the furniture maker asks for the stock above the target back, at its own cost.

[The XML file](12-InstructionForReturns.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:instruction-for-returns:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Instruction for returns". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900336121**  
  The collaboration this document belongs to: the store's first order of the Marrow line, with its return. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0033**  
  The sender's number for its returns.
- `UUID` = **1e930432-0fbd-5872-a8b6-1646ccb09ff0**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-11**  
  After the end of the sale-or-return trial on Sunday 7 June, once the store's report and the exception have shown the stock.
- `IssueTime` = **14:21:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **The sale-or-return trial of the own-label agreement, the first four weeks of sales from the reopening of the home and garden department on 11 May, ended on Sunday 7 June: the stock above the target goes back at the maker's cost. The store's van brings it; the maker pays the transport.**  
  Why the goods go back, and at whose cost.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BM-OWN-BRAND-2026**  
  The own-label agreement, whose sale-or-return terms the return follows.
- `DocumentType` = **Own-label agreement**  
  The kind of document referred to, the own-label agreement between Brightmarket Stores and Brackenmere Furniture for the Elderwick Marrow line: the store's specification, the sale-or-return trial and the returns, a document outside the examples, in words: no list has an exact code for it (cited).

### Signature

Inside `Signature`:

- `ID` = **BF-SIG-26-0611**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.

### Seller Supplier Party

Inside `SellerSupplierParty`:

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

### Retailer Customer Party

Inside `RetailerCustomerParty`:

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
- `Party/Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
- `Party/Contact/Name` = **Buying office**  
  The party's main desk, which handles this document; as Brightmarket Stores gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Brightmarket Stores gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Brightmarket Stores gives it.
- `Party/Contact/Telephone` = **+999 2 38 4609 7100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Brightmarket Stores gives it.
- `Party/Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brightmarket Stores gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Brightmarket Stores gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Manufacturer Party

Inside `ManufacturerParty`:

- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SellerSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Brackenmere Furniture**  
  The same party as at SellerSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **7400343283**  
  The return shipment.
- `GrossWeightMeasure` = **285.45** (unitCode `KGM`)  
  Seven benches of 24 kg, ten chairs of 11.5 kg and seven care kits of 0.35 kg, packed.
- `Delivery/DeliveryLocation/ID` = **9523710900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, factory and goods-in, marrowdale: Brackenmere Furniture identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Delivery/DeliveryLocation/Name` = **Brackenmere Furniture, Marrowdale**  
  Where the pieces go back: the maker's workshop.
- `Delivery/RequestedDeliveryPeriod/StartDate` = **2026-06-12**  
  The store's van brings them.
- `Delivery/RequestedDeliveryPeriod/EndDate` = **2026-06-15**  
  By the Monday after.

### Instruction For Returns Line

Inside `InstructionForReturnsLine`:

- `ID` = **1**  
  A line per piece.
- `Note` = **In their original cartons.**  
  How they are to be returned.
- `Quantity` = **4** (unitCode `EA`)  
  Four oak benches: the stock above the target of six.
- `Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow bench, oak**  
  The item's short name.
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
  A line per piece.
- `Note` = **In their original cartons.**  
  How they are to be returned.
- `Quantity` = **3** (unitCode `EA`)  
  Three ash benches: the stock above the target of four.
- `Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow bench, ash**  
  The item's short name.
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
  A line per piece.
- `Note` = **In their original cartons.**  
  How they are to be returned.
- `Quantity` = **5** (unitCode `EA`)  
  Five oak chairs: the stock above the target of twelve.
- `Item/Description` = **Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow chair, oak**  
  The item's short name.
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
  A line per piece.
- `Note` = **In their original cartons.**  
  How they are to be returned.
- `Quantity` = **5** (unitCode `EA`)  
  Five ash chairs: the stock above the target of eight.
- `Item/Description` = **Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `Item/Name` = **Elderwick Marrow chair, ash**  
  The item's short name.
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
  A line per piece.
- `Note` = **In their original cartons.**  
  How they are to be returned.
- `Quantity` = **7** (unitCode `EA`)  
  The care kits of the seven benches.
- `Item/Description` = **Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.**  
  The seller's description.
- `Item/Name` = **Elderwick care kit**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **BKM-MRW-K**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `Item/StandardItemIdentification/ID` = **9522610000030** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<InstructionForReturns xmlns="urn:oasis:names:specification:ubl:schema:xsd:InstructionForReturns-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:instruction-for-returns:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900336121</cbc:ProfileExecutionID>
  <cbc:ID>26-0033</cbc:ID>
  <cbc:UUID>1e930432-0fbd-5872-a8b6-1646ccb09ff0</cbc:UUID>
  <cbc:IssueDate>2026-06-11</cbc:IssueDate>
  <cbc:IssueTime>14:21:00-01:00</cbc:IssueTime>
  <cbc:Note>The sale-or-return trial of the own-label agreement, the first four weeks of sales from the reopening of the home and garden department on 11 May, ended on Sunday 7 June: the stock above the target goes back at the maker's cost. The store's van brings it; the maker pays the transport.</cbc:Note>
  <cac:DocumentReference>
    <cbc:ID>BM-OWN-BRAND-2026</cbc:ID>
    <cbc:DocumentType>Own-label agreement</cbc:DocumentType>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>BF-SIG-26-0611</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SellerSupplierParty>
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
  </cac:SellerSupplierParty>
  <cac:RetailerCustomerParty>
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
        <cbc:ID>BM-CT-01</cbc:ID>
        <cbc:Name>Buying office</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
        <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:RetailerCustomerParty>
  <cac:ManufacturerParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
  </cac:ManufacturerParty>
  <cac:Shipment>
    <cbc:ID>7400343283</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">285.45</cbc:GrossWeightMeasure>
    <cac:Delivery>
      <cac:DeliveryLocation>
        <cbc:ID schemeID="GS1 GLN">9523710900015</cbc:ID>
        <cbc:Name>Brackenmere Furniture, Marrowdale</cbc:Name>
      </cac:DeliveryLocation>
      <cac:RequestedDeliveryPeriod>
        <cbc:StartDate>2026-06-12</cbc:StartDate>
        <cbc:EndDate>2026-06-15</cbc:EndDate>
      </cac:RequestedDeliveryPeriod>
    </cac:Delivery>
  </cac:Shipment>
  <cac:InstructionForReturnsLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>In their original cartons.</cbc:Note>
    <cbc:Quantity unitCode="EA">4</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow bench, oak</cbc:Name>
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
  </cac:InstructionForReturnsLine>
  <cac:InstructionForReturnsLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>In their original cartons.</cbc:Note>
    <cbc:Quantity unitCode="EA">3</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow bench, ash</cbc:Name>
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
  </cac:InstructionForReturnsLine>
  <cac:InstructionForReturnsLine>
    <cbc:ID>3</cbc:ID>
    <cbc:Note>In their original cartons.</cbc:Note>
    <cbc:Quantity unitCode="EA">5</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow chair, oak</cbc:Name>
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
  </cac:InstructionForReturnsLine>
  <cac:InstructionForReturnsLine>
    <cbc:ID>4</cbc:ID>
    <cbc:Note>In their original cartons.</cbc:Note>
    <cbc:Quantity unitCode="EA">5</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
      <cbc:Name>Elderwick Marrow chair, ash</cbc:Name>
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
  </cac:InstructionForReturnsLine>
  <cac:InstructionForReturnsLine>
    <cbc:ID>5</cbc:ID>
    <cbc:Note>In their original cartons.</cbc:Note>
    <cbc:Quantity unitCode="EA">7</cbc:Quantity>
    <cac:Item>
      <cbc:Description>Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.</cbc:Description>
      <cbc:Name>Elderwick care kit</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>BKM-MRW-K</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9522610000030</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:InstructionForReturnsLine>
</InstructionForReturns>
```
