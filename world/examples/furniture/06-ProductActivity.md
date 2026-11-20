# Product Activity: Brightmarket Stores to Brackenmere Furniture

*Example 6 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Product Activity in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PRODUCT-ACTIVITY-SCHEMA)*

The sales of the line in its first four weeks, from the reopening of the home and garden department on 11 May, per piece and wood.

[The XML file](06-ProductActivity.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:product-activity:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Product activity". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:collaboration:1.0**  
  The Trade Accord's process profile the document belongs to: collaborative planning, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **FURNITURE-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BS-DOC-26-0572**  
  The sender's number for its activity.
- `UUID` = **35444c15-3be6-5365-a08f-55521605590a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-08**  
  The store's report of the first four weeks of sales, on the Monday after them.
- `IssueTime` = **16:35:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC.
- `Note` = **The chairs sell better than the set: the bench is too long for many apartment kitchens.**  
  The store's remark.

### Activity Period

Inside `ActivityPeriod`:

- `StartDate` = **2026-05-11**  
  The four weeks reported: from the reopening of the home and garden department on Monday 11 May, the first day of sales.
- `EndDate` = **2026-06-07**  
  Their end: Sunday 7 June.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BF-DOC-26-0569**  
  The request the figures answer.
- `DocumentTypeCode` = **ItemInformationRequest** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: BF-DOC-26-0569 is the example furniture/03, a ItemInformationRequest; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ItemInformationRequest = Item Information Request.

### Signature

Inside `Signature`:

- `ID` = **BM-SIG-26-0608A**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brightmarket Stores gives it.
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; as Brightmarket Stores gives it.
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; as Brightmarket Stores gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Brightmarket Stores gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. as Brightmarket Stores gives it.
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. as Brightmarket Stores gives it.
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. as Brightmarket Stores gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Brightmarket Stores gives it.
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). as Brightmarket Stores gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Brightmarket Stores gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Customer service**  
  The party's customer service desk: the desk for its role in this document (it sells); as Brightmarket Stores gives it.
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; as Brightmarket Stores gives it.
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; as Brightmarket Stores gives it.
- `Contact/Telephone` = **+999 2 38 4609 7100**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Brightmarket Stores gives it.
- `Contact/ElectronicMail` = **service@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brightmarket Stores gives it.
- `Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Brightmarket Stores gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.
- `PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Brackenmere Furniture gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. as Brackenmere Furniture gives it.
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. as Brackenmere Furniture gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Brackenmere Furniture gives it.
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). as Brackenmere Furniture gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Brackenmere Furniture gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Trade sales**  
  The party's main desk, which handles this document; as Brackenmere Furniture gives it.
- `Contact/JobTitle` = **Trade sales manager**  
  The job of the person who answers at the desk; as Brackenmere Furniture gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Brackenmere Furniture gives it.
- `Contact/Telephone` = **+999 2 7121 602 606**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Brackenmere Furniture gives it.
- `Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brackenmere Furniture gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Brackenmere Furniture gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Supply Chain Activity Data Line

Inside `SupplyChainActivityDataLine`:

- `ID` = **1**  
  The only line.
- `SupplyChainActivityTypeCode` = **SALES** (listID `urn:ubl-examples:world:codelist:SupplyChainActivityCode`)  
  The activity reported: sales to consumers. The code is from the Trade Accord's supply chain activity list: SALES = Sales.
- `ActivityPeriod/StartDate` = **2026-05-11**  
  The four weeks since the reopening.
- `ActivityPeriod/EndDate` = **2026-06-07**  
  Their end.
- `ActivityOriginLocation/ID` = **9522610900026** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, home and garden department of the lumeport store: Brightmarket Stores identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `ActivityOriginLocation/Name` = **Brightmarket Stores, home and garden department, Lumeport**  
  Where the sales took place.
- `SalesItem/Quantity` = **2** (unitCode `EA`)  
  Two oak benches sold in the four weeks since the reopening, both in Marrow sets.
- `SalesItem/ActivityProperty/Name` = **Sold in a Marrow set**  
  What the store notes.
- `SalesItem/ActivityProperty/Value` = **2 of 2, each with two oak chairs.**  
  How the benches sold.
- `SalesItem/Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `SalesItem/Item/Name` = **Elderwick Marrow bench, oak**  
  The item's short name.
- `SalesItem/Item/SellersItemIdentification/ID` = **BF-MRW-B14**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `SalesItem/Item/SellersItemIdentification/ExtendedID` = **OAK**  
  The variant of the item: the wood, added to the item number.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **OAK** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: OAK = Oak.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid oak**  
  The variant in words.
- `SalesItem/Item/StandardItemIdentification/ID` = **9522610000016** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `SalesItem/Quantity` = **1** (unitCode `EA`)  
  One ash bench sold in the four weeks since the reopening, in a Marrow set.
- `SalesItem/ActivityProperty/Name` = **Sold in a Marrow set**  
  What the store notes.
- `SalesItem/ActivityProperty/Value` = **1 of 1, with two ash chairs: the webshop order of 30 May, for collection in the department.**  
  How the benches sold.
- `SalesItem/Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `SalesItem/Item/Name` = **Elderwick Marrow bench, ash**  
  The item's short name.
- `SalesItem/Item/SellersItemIdentification/ID` = **BF-MRW-B14**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `SalesItem/Item/SellersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **ASH** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: ASH = Ash.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `SalesItem/Item/StandardItemIdentification/ID` = **9522610000047** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `SalesItem/Quantity` = **7** (unitCode `EA`)  
  Seven oak chairs sold in the four weeks since the reopening: 4 in the oak sets and 3 alone.
- `SalesItem/ActivityProperty/Name` = **Sold alone**  
  What the store notes.
- `SalesItem/ActivityProperty/Value` = **3 of 7: the 1400 mm bench is too long for many apartment kitchens, so shoppers buy the chairs.**  
  Why the chairs sell better than the set.
- `SalesItem/Item/Description` = **Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `SalesItem/Item/Name` = **Elderwick Marrow chair, oak**  
  The item's short name.
- `SalesItem/Item/SellersItemIdentification/ID` = **BF-MRW-C**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `SalesItem/Item/SellersItemIdentification/ExtendedID` = **OAK**  
  The variant of the item: the wood, added to the item number.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **OAK** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: OAK = Oak.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid oak**  
  The variant in words.
- `SalesItem/Item/StandardItemIdentification/ID` = **9522610000023** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `SalesItem/Quantity` = **3** (unitCode `EA`)  
  Three ash chairs sold in the four weeks since the reopening: 2 in the ash set and 1 alone.
- `SalesItem/ActivityProperty/Name` = **Sold alone**  
  What the store notes.
- `SalesItem/ActivityProperty/Value` = **1 of 3: the 1400 mm bench is too long for many apartment kitchens, so shoppers buy the chairs.**  
  Why the chairs sell better than the set.
- `SalesItem/Item/Description` = **Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `SalesItem/Item/Name` = **Elderwick Marrow chair, ash**  
  The item's short name.
- `SalesItem/Item/SellersItemIdentification/ID` = **BF-MRW-C**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `SalesItem/Item/SellersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **ASH** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: ASH = Ash.
- `SalesItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `SalesItem/Item/StandardItemIdentification/ID` = **9522610000054** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ProductActivity xmlns="urn:oasis:names:specification:ubl:schema:xsd:ProductActivity-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:product-activity:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:collaboration:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>FURNITURE-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-DOC-26-0572</cbc:ID>
  <cbc:UUID>35444c15-3be6-5365-a08f-55521605590a</cbc:UUID>
  <cbc:IssueDate>2026-06-08</cbc:IssueDate>
  <cbc:IssueTime>16:35:00-01:00</cbc:IssueTime>
  <cbc:Note>The chairs sell better than the set: the bench is too long for many apartment kitchens.</cbc:Note>
  <cac:ActivityPeriod>
    <cbc:StartDate>2026-05-11</cbc:StartDate>
    <cbc:EndDate>2026-06-07</cbc:EndDate>
  </cac:ActivityPeriod>
  <cac:DocumentReference>
    <cbc:ID>BF-DOC-26-0569</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ItemInformationRequest</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>BM-SIG-26-0608A</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
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
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Customer service</cbc:Department>
      <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
      <cbc:ElectronicMail>service@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
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
  </cac:ReceiverParty>
  <cac:SupplyChainActivityDataLine>
    <cbc:ID>1</cbc:ID>
    <cbc:SupplyChainActivityTypeCode listID="urn:ubl-examples:world:codelist:SupplyChainActivityCode">SALES</cbc:SupplyChainActivityTypeCode>
    <cac:ActivityPeriod>
      <cbc:StartDate>2026-05-11</cbc:StartDate>
      <cbc:EndDate>2026-06-07</cbc:EndDate>
    </cac:ActivityPeriod>
    <cac:ActivityOriginLocation>
      <cbc:ID schemeID="GS1 GLN">9522610900026</cbc:ID>
      <cbc:Name>Brightmarket Stores, home and garden department, Lumeport</cbc:Name>
    </cac:ActivityOriginLocation>
    <cac:SalesItem>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
      <cac:ActivityProperty>
        <cbc:Name>Sold in a Marrow set</cbc:Name>
        <cbc:Value>2 of 2, each with two oak chairs.</cbc:Value>
      </cac:ActivityProperty>
      <cac:Item>
        <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow bench, oak</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BF-MRW-B14</cbc:ID>
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
    </cac:SalesItem>
    <cac:SalesItem>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cac:ActivityProperty>
        <cbc:Name>Sold in a Marrow set</cbc:Name>
        <cbc:Value>1 of 1, with two ash chairs: the webshop order of 30 May, for collection in the department.</cbc:Value>
      </cac:ActivityProperty>
      <cac:Item>
        <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow bench, ash</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BF-MRW-B14</cbc:ID>
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
    </cac:SalesItem>
    <cac:SalesItem>
      <cbc:Quantity unitCode="EA">7</cbc:Quantity>
      <cac:ActivityProperty>
        <cbc:Name>Sold alone</cbc:Name>
        <cbc:Value>3 of 7: the 1400 mm bench is too long for many apartment kitchens, so shoppers buy the chairs.</cbc:Value>
      </cac:ActivityProperty>
      <cac:Item>
        <cbc:Description>Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow chair, oak</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BF-MRW-C</cbc:ID>
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
    </cac:SalesItem>
    <cac:SalesItem>
      <cbc:Quantity unitCode="EA">3</cbc:Quantity>
      <cac:ActivityProperty>
        <cbc:Name>Sold alone</cbc:Name>
        <cbc:Value>1 of 3: the 1400 mm bench is too long for many apartment kitchens, so shoppers buy the chairs.</cbc:Value>
      </cac:ActivityProperty>
      <cac:Item>
        <cbc:Description>Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow chair, ash</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BF-MRW-C</cbc:ID>
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
    </cac:SalesItem>
  </cac:SupplyChainActivityDataLine>
</ProductActivity>
```
