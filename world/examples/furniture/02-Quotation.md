# Quotation: Brackenmere Furniture to Brightmarket Stores

*Example 2 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Quotation in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-QUOTATION-SCHEMA)*

The furniture maker quotes the bench and the chair, with a care kit free with each bench.

[The XML file](02-Quotation.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:quotation:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Quotation". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:sourcing:1.0**  
  The Trade Accord's process profile the document belongs to: sourcing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900334966**  
  The collaboration this document belongs to: the store's request for a quotation of the Marrow line. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0080**  
  The seller's quotation number.
- `UUID` = **ec533b8c-fd3b-5c84-8198-dd0da43309d9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-06**  
  The furniture maker quotes the line.
- `IssueTime` = **08:58:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **The Elderwick Marrow bench and chair, made to the store's specification under its own label, each in oak and in ash at the same price; a care kit free with each bench.**  
  What is quoted.
- `PricingCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  In lume. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **6**  
  A line per piece and wood, the free care kit and the optional seat pad.

### Validity Period

Inside `ValidityPeriod`:

- `EndDate` = **2026-05-05**  
  How long the quoted prices hold.

### Request For Quotation Document Reference

Inside `RequestForQuotationDocumentReference`:

- `ID` = **6000100490**  
  The request this quotation answers.

### Signature

Inside `Signature`:

- `ID` = **BF-SIG-26-QT**  
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
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Trade sales**  
  The party's main desk, which handles this document; as Brackenmere Furniture gives it.
- `Party/Contact/JobTitle` = **Trade sales manager**  
  The job of the person who answers at the desk; as Brackenmere Furniture gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Brackenmere Furniture gives it.
- `Party/Contact/Telephone` = **+999 2 5121 602 606**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Brackenmere Furniture gives it.
- `Party/Contact/ElectronicMail` = **trade@brackenmere.example**  
  The contact's e-mail address; as Brackenmere Furniture gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Brackenmere Furniture gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brightmarket Stores gives it.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; as Brightmarket Stores gives it.
- `Party/TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; as Brightmarket Stores gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Brightmarket Stores gives it.
- `Party/Contact/ElectronicMail` = **buying@brightmarket.example**  
  The contact's e-mail address; as Brightmarket Stores gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Brightmarket Stores gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transaction Conditions

Inside `TransactionConditions`:

- `Description` = **A repeat order of the line within the season: 3 % off the quoted prices.**  
  The repeat-order discount the second order takes.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **12200.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a business that resells or processes the goods is exempt from the state sales tax, which is charged only on the sale to the final consumer (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **RESALE** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: RESALE = Sale for resale or manufacture.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Sale for resale or manufacture**  
  The name of code RESALE in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Quoted Monetary Total

Inside `QuotedMonetaryTotal`:

- `LineExtensionAmount` = **12200.00** (currencyID `XBL`)  
  The sum of the quoted lines.
- `PayableAmount` = **12200.00** (currencyID `XBL`)  
  The quoted total, before any tax.

### Quotation Line

Inside `QuotationLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **12** (unitCode `EA`)  
  Twelve benches in oak, as the store plans the opening stock: three oak pieces for every two in ash.
- `LineItem/LineExtensionAmount` = **4560.00** (currencyID `XBL`)  
  Quantity times the quoted price.
- `LineItem/Price/PriceAmount` = **380** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow bench, oak**  
  The item's short name.
- `LineItem/Item/BrandName` = **Elderwick**  
  The brand the item is sold under: Elderwick, the own label of Brightmarket Stores, which Brackenmere Furniture makes for it; as Brackenmere Furniture describes the item.
- `LineItem/Item/ModelName` = **Marrow**  
  The model; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-B14**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ExtendedID` = **OAK**  
  The variant of the item: the wood, added to the item number.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **QCXE** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: QCXE = European oak.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid oak**  
  The variant in words.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000016** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Brackenmere Furniture describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **940169** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Brackenmere Furniture describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940169 = Other seats, with wooden frames: other.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **38112** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Brackenmere Furniture describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38112 = Seats, primarily with wooden frames.
- `LineItem/Item/AdditionalItemProperty/Name` = **Wood**  
  A property buyers ask about.
- `LineItem/Item/AdditionalItemProperty/Value` = **Oak**  
  Its value; as Brackenmere Furniture describes the item.
- `LineItem/Item/ManufacturerParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/ManufacturerParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Dimension/AttributeID` = **BENCHLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: BENCHLENGTH = Bench length. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **1400** (unitCode `MMT`)  
  Its size.
- `LineItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `LineItem/ID` = **2**  
  The line number.
- `LineItem/Quantity` = **8** (unitCode `EA`)  
  Eight benches in ash.
- `LineItem/LineExtensionAmount` = **3040.00** (currencyID `XBL`)  
  Quantity times the quoted price.
- `LineItem/Price/PriceAmount` = **380** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow bench, ash**  
  The item's short name.
- `LineItem/Item/BrandName` = **Elderwick**  
  The brand the item is sold under: Elderwick, the own label of Brightmarket Stores, which Brackenmere Furniture makes for it; as Brackenmere Furniture describes the item.
- `LineItem/Item/ModelName` = **Marrow**  
  The model; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-B14**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **FXEX** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: FXEX = European ash.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000047** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Brackenmere Furniture describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **940169** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Brackenmere Furniture describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940169 = Other seats, with wooden frames: other.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **38112** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Brackenmere Furniture describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38112 = Seats, primarily with wooden frames.
- `LineItem/Item/AdditionalItemProperty/Name` = **Wood**  
  A property buyers ask about.
- `LineItem/Item/AdditionalItemProperty/Value` = **Ash**  
  Its value; as Brackenmere Furniture describes the item.
- `LineItem/Item/ManufacturerParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/ManufacturerParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Dimension/AttributeID` = **BENCHLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: BENCHLENGTH = Bench length. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **1400** (unitCode `MMT`)  
  Its size.
- `LineItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `LineItem/ID` = **3**  
  The line number.
- `LineItem/Quantity` = **24** (unitCode `EA`)  
  Twenty-four chairs in oak: two for each oak bench.
- `LineItem/LineExtensionAmount` = **2760.00** (currencyID `XBL`)  
  Quantity times the quoted price.
- `LineItem/Price/PriceAmount` = **115** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow chair, oak**  
  The item's short name.
- `LineItem/Item/BrandName` = **Elderwick**  
  The brand the item is sold under: Elderwick, the own label of Brightmarket Stores, which Brackenmere Furniture makes for it; as Brackenmere Furniture describes the item.
- `LineItem/Item/ModelName` = **Marrow**  
  The model; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-C**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ExtendedID` = **OAK**  
  The variant of the item: the wood, added to the item number.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **QCXE** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: QCXE = European oak.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid oak**  
  The variant in words.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000023** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Brackenmere Furniture describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **940169** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Brackenmere Furniture describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940169 = Other seats, with wooden frames: other.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **38112** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Brackenmere Furniture describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38112 = Seats, primarily with wooden frames.
- `LineItem/Item/AdditionalItemProperty/Name` = **Wood**  
  A property buyers ask about.
- `LineItem/Item/AdditionalItemProperty/Value` = **Oak**  
  Its value; as Brackenmere Furniture describes the item.
- `LineItem/Item/ManufacturerParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/ManufacturerParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `LineItem/ID` = **4**  
  The line number.
- `LineItem/Quantity` = **16** (unitCode `EA`)  
  Sixteen chairs in ash: two for each ash bench.
- `LineItem/LineExtensionAmount` = **1840.00** (currencyID `XBL`)  
  Quantity times the quoted price.
- `LineItem/Price/PriceAmount` = **115** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow chair, ash**  
  The item's short name.
- `LineItem/Item/BrandName` = **Elderwick**  
  The brand the item is sold under: Elderwick, the own label of Brightmarket Stores, which Brackenmere Furniture makes for it; as Brackenmere Furniture describes the item.
- `LineItem/Item/ModelName` = **Marrow**  
  The model; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-C**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **FXEX** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: FXEX = European ash.
- `LineItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000054** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Brackenmere Furniture describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **940169** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Brackenmere Furniture describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940169 = Other seats, with wooden frames: other.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **38112** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Brackenmere Furniture describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38112 = Seats, primarily with wooden frames.
- `LineItem/Item/AdditionalItemProperty/Name` = **Wood**  
  A property buyers ask about.
- `LineItem/Item/AdditionalItemProperty/Value` = **Ash**  
  Its value; as Brackenmere Furniture describes the item.
- `LineItem/Item/ManufacturerParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/ManufacturerParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Note` = **Free: one care kit with each bench.**  
  Why the line has no price.
- `LineItem/ID` = **5**  
  The line number.
- `LineItem/Quantity` = **20** (unitCode `EA`)  
  One care kit free with each bench, oak or ash.
- `LineItem/LineExtensionAmount` = **0.00** (currencyID `XBL`)  
  Quantity times the quoted price.
- `LineItem/Price/PriceAmount` = **0** (currencyID `XBL`)  
  No price: the item comes free with each Elderwick Marrow bench.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick care kit**  
  The item's short name.
- `LineItem/Item/BrandName` = **Elderwick**  
  The brand the item is sold under: Elderwick, the own label of Brightmarket Stores, which Brackenmere Furniture makes for it; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-K**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000030** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Brackenmere Furniture describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **340520** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Brackenmere Furniture describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 340520 = Polishes, creams and similar preparations; for the maintenance of wooden furniture, floors or other woodwork, excluding waxes of heading no. 3404.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **35333** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Brackenmere Furniture describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 35333 = Polishes and creams, for footwear, furniture, floors, coachwork, glass or metal.
- `LineItem/Item/ManufacturerParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/ManufacturerParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `Note` = **Optional, as asked: not in the quoted total.**  
  The answer to the store's optional line.
- `LineExtensionAmount` = **640.00** (currencyID `XBL`)  
  Forty pads at the quoted price, if the option is taken: the line's amount stands on the quotation line, apart from the quoted total and its tax.
- `RequestForQuotationLineID` = **5**  
  The request's optional line it answers.
- `LineItem/ID` = **6**  
  The line number.
- `LineItem/Quantity` = **40** (unitCode `EA`)  
  One for each of the forty chairs, if the store takes the option.
- `LineItem/Price/PriceAmount` = **16** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Seat pad for the Marrow dining chair: a foam pad in a removable linen cover, with ties, 400 × 400 mm. Sold under Brackenmere's brand; Brackenmere has it made by a textile workshop and does not make it itself.**  
  The seller's description.
- `LineItem/Item/Name` = **Brackenmere seat pad, Marrow chair**  
  The item's short name.
- `LineItem/Item/BrandName` = **Brackenmere**  
  The brand the maker sells the item under; as Brackenmere Furniture describes the item.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-P**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **9523710000036** (schemeID `GS1 GTIN`)  
  The GTIN Brackenmere Furniture gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Brackenmere is Brackenmere Furniture's.
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Brackenmere Furniture describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **940490** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Brackenmere Furniture describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940490 = Bedding and similar furnishing articles, n.e.c. in heading 9404 (cushions and the like).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **27180** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Brackenmere Furniture describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 27180 = Quilts, eiderdowns, cushions, pouffes, pillows, sleeping bags and the like, fitted with springs or stuffed or internally fitted with any material or of cellular rubber or plastics.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Quotation xmlns="urn:oasis:names:specification:ubl:schema:xsd:Quotation-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:quotation:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:sourcing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900334966</cbc:ProfileExecutionID>
  <cbc:ID>26-0080</cbc:ID>
  <cbc:UUID>ec533b8c-fd3b-5c84-8198-dd0da43309d9</cbc:UUID>
  <cbc:IssueDate>2026-03-06</cbc:IssueDate>
  <cbc:IssueTime>08:58:00-01:00</cbc:IssueTime>
  <cbc:Note>The Elderwick Marrow bench and chair, made to the store's specification under its own label, each in oak and in ash at the same price; a care kit free with each bench.</cbc:Note>
  <cbc:PricingCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:PricingCurrencyCode>
  <cbc:LineCountNumeric>6</cbc:LineCountNumeric>
  <cac:ValidityPeriod>
    <cbc:EndDate>2026-05-05</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:RequestForQuotationDocumentReference>
    <cbc:ID>6000100490</cbc:ID>
  </cac:RequestForQuotationDocumentReference>
  <cac:Signature>
    <cbc:ID>BF-SIG-26-QT</cbc:ID>
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
        <cbc:Telephone>+999 2 5121 602 606</cbc:Telephone>
        <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
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
  </cac:BuyerCustomerParty>
  <cac:TransactionConditions>
    <cbc:Description>A repeat order of the line within the season: 3 % off the quoted prices.</cbc:Description>
  </cac:TransactionConditions>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">12200.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">RESALE</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Sale for resale or manufacture</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:QuotedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">12200.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">12200.00</cbc:PayableAmount>
  </cac:QuotedMonetaryTotal>
  <cac:QuotationLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">4560.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">380</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow bench, oak</cbc:Name>
        <cbc:BrandName>Elderwick</cbc:BrandName>
        <cbc:ModelName>Marrow</cbc:ModelName>
        <cac:SellersItemIdentification>
          <cbc:ID>BKM-MRW-B14</cbc:ID>
          <cbc:ExtendedID>OAK</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">QCXE</cbc:DescriptionCode>
            <cbc:Description>Solid oak</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000016</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940169</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38112</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Wood</cbc:Name>
          <cbc:Value>Oak</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:ManufacturerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Brackenmere Furniture</cbc:Name>
          </cac:PartyName>
        </cac:ManufacturerParty>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">BENCHLENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1400</cbc:Measure>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">450</cbc:Measure>
        </cac:Dimension>
      </cac:Item>
    </cac:LineItem>
  </cac:QuotationLine>
  <cac:QuotationLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="EA">8</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">3040.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">380</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow bench, ash</cbc:Name>
        <cbc:BrandName>Elderwick</cbc:BrandName>
        <cbc:ModelName>Marrow</cbc:ModelName>
        <cac:SellersItemIdentification>
          <cbc:ID>BKM-MRW-B14</cbc:ID>
          <cbc:ExtendedID>ASH</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">FXEX</cbc:DescriptionCode>
            <cbc:Description>Solid ash</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000047</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940169</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38112</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Wood</cbc:Name>
          <cbc:Value>Ash</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:ManufacturerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Brackenmere Furniture</cbc:Name>
          </cac:PartyName>
        </cac:ManufacturerParty>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">BENCHLENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1400</cbc:Measure>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">450</cbc:Measure>
        </cac:Dimension>
      </cac:Item>
    </cac:LineItem>
  </cac:QuotationLine>
  <cac:QuotationLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="EA">24</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">2760.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">115</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow chair, oak</cbc:Name>
        <cbc:BrandName>Elderwick</cbc:BrandName>
        <cbc:ModelName>Marrow</cbc:ModelName>
        <cac:SellersItemIdentification>
          <cbc:ID>BKM-MRW-C</cbc:ID>
          <cbc:ExtendedID>OAK</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">QCXE</cbc:DescriptionCode>
            <cbc:Description>Solid oak</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000023</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940169</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38112</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Wood</cbc:Name>
          <cbc:Value>Oak</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:ManufacturerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Brackenmere Furniture</cbc:Name>
          </cac:PartyName>
        </cac:ManufacturerParty>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">450</cbc:Measure>
        </cac:Dimension>
      </cac:Item>
    </cac:LineItem>
  </cac:QuotationLine>
  <cac:QuotationLine>
    <cac:LineItem>
      <cbc:ID>4</cbc:ID>
      <cbc:Quantity unitCode="EA">16</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">1840.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">115</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.</cbc:Description>
        <cbc:Name>Elderwick Marrow chair, ash</cbc:Name>
        <cbc:BrandName>Elderwick</cbc:BrandName>
        <cbc:ModelName>Marrow</cbc:ModelName>
        <cac:SellersItemIdentification>
          <cbc:ID>BKM-MRW-C</cbc:ID>
          <cbc:ExtendedID>ASH</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">FXEX</cbc:DescriptionCode>
            <cbc:Description>Solid ash</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000054</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940169</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38112</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Wood</cbc:Name>
          <cbc:Value>Ash</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:ManufacturerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Brackenmere Furniture</cbc:Name>
          </cac:PartyName>
        </cac:ManufacturerParty>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">450</cbc:Measure>
        </cac:Dimension>
      </cac:Item>
    </cac:LineItem>
  </cac:QuotationLine>
  <cac:QuotationLine>
    <cbc:Note>Free: one care kit with each bench.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>5</cbc:ID>
      <cbc:Quantity unitCode="EA">20</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">0.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">0</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.</cbc:Description>
        <cbc:Name>Elderwick care kit</cbc:Name>
        <cbc:BrandName>Elderwick</cbc:BrandName>
        <cac:SellersItemIdentification>
          <cbc:ID>BKM-MRW-K</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000030</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">340520</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35333</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ManufacturerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Brackenmere Furniture</cbc:Name>
          </cac:PartyName>
        </cac:ManufacturerParty>
      </cac:Item>
    </cac:LineItem>
  </cac:QuotationLine>
  <cac:QuotationLine>
    <cbc:Note>Optional, as asked: not in the quoted total.</cbc:Note>
    <cbc:LineExtensionAmount currencyID="XBL">640.00</cbc:LineExtensionAmount>
    <cbc:RequestForQuotationLineID>5</cbc:RequestForQuotationLineID>
    <cac:LineItem>
      <cbc:ID>6</cbc:ID>
      <cbc:Quantity unitCode="EA">40</cbc:Quantity>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">16</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Seat pad for the Marrow dining chair: a foam pad in a removable linen cover, with ties, 400 × 400 mm. Sold under Brackenmere's brand; Brackenmere has it made by a textile workshop and does not make it itself.</cbc:Description>
        <cbc:Name>Brackenmere seat pad, Marrow chair</cbc:Name>
        <cbc:BrandName>Brackenmere</cbc:BrandName>
        <cac:SellersItemIdentification>
          <cbc:ID>BKM-MRW-P</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9523710000036</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940490</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">27180</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:LineItem>
  </cac:QuotationLine>
</Quotation>
```
