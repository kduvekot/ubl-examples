# Order: Brightmarket Stores to Brackenmere Furniture

*Example 8 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The store orders the opening stock of the line, piece by piece and wood by wood, to hold for the reopening of its home and garden department on 11 May. Delivery terms DAP store: the furniture maker delivers with its own van.

[The XML file](08-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900336121**  
  The collaboration this document belongs to: the store's first order of the Marrow line, with its return. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **7100448162**  
  The buyer's order number.
- `UUID` = **ac3a2b00-ef02-50c6-a666-734b5c64e958**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-16**  
  The store orders the opening stock of its line.
- `IssueTime` = **11:16:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `Note` = **Opening stock of the Elderwick Marrow line, in oak and in ash: twice the target of each item, to fill the display in the home and garden department when it reopens on 11 May as well as the shelf; the store holds the stock until then.**  
  Why the order is larger than the stock policy's target.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `AccountingCostCode` = **6120**  
  The buyer's cost centre, to be quoted on the invoice.
- `AccountingCost` = **Home and garden department**  
  The cost centre in words.
- `LineCountNumeric` = **5**  
  The number of order lines.

### Quotation Document Reference

Inside `QuotationDocumentReference`:

- `ID` = **26-0080**  
  The quotation accepted.

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

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.
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

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-03-23**  
  The opening stock is wanted on 23 March: the maker makes the line in one run, and the store holds it for the reopening of its home and garden department on 11 May.
- `RequestedDeliveryPeriod/EndDate` = **2026-03-23**  
  The last day it is wanted.
- `DeliveryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Brightmarket Stores**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **DAP** (schemeID `INCOTERMS`)  
  Delivered at place, the store: the furniture maker delivers with its own van. The code is from the world's copy of Incoterms 2020: DAP = Delivered at Place. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **9522610900019** (schemeID `GS1 GLN`)  
  The place's identifier, as the world gives it wherever the place appears (a GLN).
- `DeliveryLocation/Description` = **Brightmarket Stores, goods-in, Lumeport**  
  Where the delivery terms place the handover of the goods.

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

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **12200.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **12200.00** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `Note` = **Price as quoted.**  
  Why no price question.
- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Note` = **Twice the target of six oak benches: the shelf and the display in the home and garden department when it reopens.**  
  What the line is.
- `LineItem/Quantity` = **12** (unitCode `EA`)  
  Twelve benches in oak, as the store plans the opening stock: three oak pieces for every two in ash.
- `LineItem/LineExtensionAmount` = **4560.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/MinimumQuantity` = **6** (unitCode `EA`)  
  The store accepts a first part of at least half the line.
- `LineItem/MaximumQuantity` = **12** (unitCode `EA`)  
  And no more than ordered.
- `LineItem/MinimumBackorderQuantity` = **3** (unitCode `EA`)  
  But only in lots of at least a quarter of the line.
- `LineItem/MaximumBackorderQuantity` = **6** (unitCode `EA`)  
  And at most half the line on back order.
- `LineItem/InspectionMethodCode` = **VISUAL** (listID `urn:ubl-examples:world:codelist:InspectionMethodCode`)  
  The goods-in checks each piece by eye. The code is from the Trade Accord's inspection method list: VISUAL = Visual inspection.
- `LineItem/BackOrderAllowedIndicator` = **true**  
  What cannot be delivered now may follow.
- `LineItem/AccountingCostCode` = **6120**  
  The cost centre of the home and garden department, which sells the line.
- `LineItem/AccountingCost` = **Home and garden department**  
  In words.
- `LineItem/Price/PriceAmount` = **380** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow bench, oak**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **BM-551005**  
  The buyer's own item number: it resells this item under its own number.
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
- `LineItem/WarrantyValidityPeriod/DurationMeasure` = **2** (unitCode `ANN`)  
  Two years on the joints.
- `LineItem/WarrantyParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/WarrantyParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No sales tax: the store buys for resale.
- `LineItem/ItemPriceExtension/Amount` = **4560.00** (currencyID `XBL`)  
  The price times the quantity, before any allowance.
- `QuotationLineReference/LineID` = **1**  
  The quotation line accepted.
- `Note` = **Price as quoted.**  
  Why no price question.
- `LineItem/ID` = **2**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Note` = **Twice the target of four ash benches, for the shelf and the display.**  
  What the line is.
- `LineItem/Quantity` = **8** (unitCode `EA`)  
  Eight benches in ash.
- `LineItem/LineExtensionAmount` = **3040.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/MinimumQuantity` = **4** (unitCode `EA`)  
  The store accepts a first part of at least half the line.
- `LineItem/MaximumQuantity` = **8** (unitCode `EA`)  
  And no more than ordered.
- `LineItem/MinimumBackorderQuantity` = **2** (unitCode `EA`)  
  But only in lots of at least a quarter of the line.
- `LineItem/MaximumBackorderQuantity` = **4** (unitCode `EA`)  
  And at most half the line on back order.
- `LineItem/InspectionMethodCode` = **VISUAL** (listID `urn:ubl-examples:world:codelist:InspectionMethodCode`)  
  The goods-in checks each piece by eye. The code is from the Trade Accord's inspection method list: VISUAL = Visual inspection.
- `LineItem/BackOrderAllowedIndicator` = **true**  
  What cannot be delivered now may follow.
- `LineItem/AccountingCostCode` = **6120**  
  The cost centre of the home and garden department, which sells the line.
- `LineItem/AccountingCost` = **Home and garden department**  
  In words.
- `LineItem/Price/PriceAmount` = **380** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining bench, 1400 mm, in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow bench, ash**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **BM-551008**  
  The buyer's own item number: it resells this item under its own number.
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
- `LineItem/WarrantyValidityPeriod/DurationMeasure` = **2** (unitCode `ANN`)  
  Two years on the joints.
- `LineItem/WarrantyParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/WarrantyParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No sales tax: the store buys for resale.
- `LineItem/ItemPriceExtension/Amount` = **3040.00** (currencyID `XBL`)  
  The price times the quantity, before any allowance.
- `QuotationLineReference/LineID` = **2**  
  The quotation line accepted.
- `Note` = **Price as quoted.**  
  Why no price question.
- `LineItem/ID` = **3**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Note` = **Twice the target of twelve oak chairs, two with each oak bench.**  
  What the line is.
- `LineItem/Quantity` = **24** (unitCode `EA`)  
  Twenty-four chairs in oak: two for each oak bench.
- `LineItem/LineExtensionAmount` = **2760.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/MinimumQuantity` = **12** (unitCode `EA`)  
  The store accepts a first part of at least half the line.
- `LineItem/MaximumQuantity` = **24** (unitCode `EA`)  
  And no more than ordered.
- `LineItem/MinimumBackorderQuantity` = **6** (unitCode `EA`)  
  But only in lots of at least a quarter of the line.
- `LineItem/MaximumBackorderQuantity` = **12** (unitCode `EA`)  
  And at most half the line on back order.
- `LineItem/InspectionMethodCode` = **VISUAL** (listID `urn:ubl-examples:world:codelist:InspectionMethodCode`)  
  The goods-in checks each piece by eye. The code is from the Trade Accord's inspection method list: VISUAL = Visual inspection.
- `LineItem/BackOrderAllowedIndicator` = **true**  
  What cannot be delivered now may follow.
- `LineItem/AccountingCostCode` = **6120**  
  The cost centre of the home and garden department, which sells the line.
- `LineItem/AccountingCost` = **Home and garden department**  
  In words.
- `LineItem/Price/PriceAmount` = **115** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining chair in solid kiln-dried oak with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow chair, oak**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **BM-551006**  
  The buyer's own item number: it resells this item under its own number.
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
- `LineItem/WarrantyValidityPeriod/DurationMeasure` = **2** (unitCode `ANN`)  
  Two years on the joints.
- `LineItem/WarrantyParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/WarrantyParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No sales tax: the store buys for resale.
- `LineItem/ItemPriceExtension/Amount` = **2760.00** (currencyID `XBL`)  
  The price times the quantity, before any allowance.
- `QuotationLineReference/LineID` = **3**  
  The quotation line accepted.
- `Note` = **Price as quoted.**  
  Why no price question.
- `LineItem/ID` = **4**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Note` = **Twice the target of eight ash chairs, two with each ash bench.**  
  What the line is.
- `LineItem/Quantity` = **16** (unitCode `EA`)  
  Sixteen chairs in ash: two for each ash bench.
- `LineItem/LineExtensionAmount` = **1840.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/MinimumQuantity` = **8** (unitCode `EA`)  
  The store accepts a first part of at least half the line.
- `LineItem/MaximumQuantity` = **16** (unitCode `EA`)  
  And no more than ordered.
- `LineItem/MinimumBackorderQuantity` = **4** (unitCode `EA`)  
  But only in lots of at least a quarter of the line.
- `LineItem/MaximumBackorderQuantity` = **8** (unitCode `EA`)  
  And at most half the line on back order.
- `LineItem/InspectionMethodCode` = **VISUAL** (listID `urn:ubl-examples:world:codelist:InspectionMethodCode`)  
  The goods-in checks each piece by eye. The code is from the Trade Accord's inspection method list: VISUAL = Visual inspection.
- `LineItem/BackOrderAllowedIndicator` = **true**  
  What cannot be delivered now may follow.
- `LineItem/AccountingCostCode` = **6120**  
  The cost centre of the home and garden department, which sells the line.
- `LineItem/AccountingCost` = **Home and garden department**  
  In words.
- `LineItem/Price/PriceAmount` = **115** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining chair in solid kiln-dried ash with a hard-wax oil finish: closed seat, glued joints, felt pads under the legs, seat height 45 cm.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick Marrow chair, ash**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **BM-551009**  
  The buyer's own item number: it resells this item under its own number.
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
- `LineItem/WarrantyValidityPeriod/DurationMeasure` = **2** (unitCode `ANN`)  
  Two years on the joints.
- `LineItem/WarrantyParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/WarrantyParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No sales tax: the store buys for resale.
- `LineItem/ItemPriceExtension/Amount` = **1840.00** (currencyID `XBL`)  
  The price times the quantity, before any allowance.
- `QuotationLineReference/LineID` = **4**  
  The quotation line accepted.
- `Note` = **Price as quoted.**  
  Why no price question.
- `LineItem/ID` = **5**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Note` = **Free: one care kit with each bench, oak or ash.**  
  What the line is.
- `LineItem/Quantity` = **20** (unitCode `EA`)  
  One care kit free with each bench, oak or ash.
- `LineItem/LineExtensionAmount` = **0.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **0** (currencyID `XBL`)  
  No price: the item comes free with each Elderwick Marrow bench.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Care kit for the Marrow dining furniture: a 250 ml tin of hard-wax oil and a lint-free cloth, in one pack. One comes free with each bench.**  
  The seller's description.
- `LineItem/Item/Name` = **Elderwick care kit**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **BM-551007**  
  The buyer's own item number: it resells this item under its own number.
- `LineItem/Item/SellersItemIdentification/ID` = **BKM-MRW-K**  
  The seller's own item number; as Brackenmere Furniture describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000030** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item.
- `LineItem/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No sales tax: the store buys for resale.
- `LineItem/ItemPriceExtension/Amount` = **0.00** (currencyID `XBL`)  
  The price times the quantity, before any allowance.
- `QuotationLineReference/LineID` = **5**  
  The quotation line accepted.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900336121</cbc:ProfileExecutionID>
  <cbc:ID>7100448162</cbc:ID>
  <cbc:UUID>ac3a2b00-ef02-50c6-a666-734b5c64e958</cbc:UUID>
  <cbc:IssueDate>2026-03-16</cbc:IssueDate>
  <cbc:IssueTime>11:16:00-01:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:Note>Opening stock of the Elderwick Marrow line, in oak and in ash: twice the target of each item, to fill the display in the home and garden department when it reopens on 11 May as well as the shelf; the store holds the stock until then.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
  <cbc:AccountingCost>Home and garden department</cbc:AccountingCost>
  <cbc:LineCountNumeric>5</cbc:LineCountNumeric>
  <cac:QuotationDocumentReference>
    <cbc:ID>26-0080</cbc:ID>
  </cac:QuotationDocumentReference>
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
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-03-23</cbc:StartDate>
      <cbc:EndDate>2026-03-23</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">DAP</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="GS1 GLN">9522610900019</cbc:ID>
      <cbc:Description>Brightmarket Stores, goods-in, Lumeport</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
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
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">12200.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">12200.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cbc:Note>Price as quoted.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Note>Twice the target of six oak benches: the shelf and the display in the home and garden department when it reopens.</cbc:Note>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">4560.00</cbc:LineExtensionAmount>
      <cbc:MinimumQuantity unitCode="EA">6</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">12</cbc:MaximumQuantity>
      <cbc:MinimumBackorderQuantity unitCode="EA">3</cbc:MinimumBackorderQuantity>
      <cbc:MaximumBackorderQuantity unitCode="EA">6</cbc:MaximumBackorderQuantity>
      <cbc:InspectionMethodCode listID="urn:ubl-examples:world:codelist:InspectionMethodCode">VISUAL</cbc:InspectionMethodCode>
      <cbc:BackOrderAllowedIndicator>true</cbc:BackOrderAllowedIndicator>
      <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
      <cbc:AccountingCost>Home and garden department</cbc:AccountingCost>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">380</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
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
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">QCXE</cbc:DescriptionCode>
            <cbc:Description>Solid oak</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000016</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">2</cbc:DurationMeasure>
      </cac:WarrantyValidityPeriod>
      <cac:WarrantyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brackenmere Furniture</cbc:Name>
        </cac:PartyName>
      </cac:WarrantyParty>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:ItemPriceExtension>
        <cbc:Amount currencyID="XBL">4560.00</cbc:Amount>
      </cac:ItemPriceExtension>
    </cac:LineItem>
    <cac:QuotationLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:QuotationLineReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cbc:Note>Price as quoted.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Note>Twice the target of four ash benches, for the shelf and the display.</cbc:Note>
      <cbc:Quantity unitCode="EA">8</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">3040.00</cbc:LineExtensionAmount>
      <cbc:MinimumQuantity unitCode="EA">4</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">8</cbc:MaximumQuantity>
      <cbc:MinimumBackorderQuantity unitCode="EA">2</cbc:MinimumBackorderQuantity>
      <cbc:MaximumBackorderQuantity unitCode="EA">4</cbc:MaximumBackorderQuantity>
      <cbc:InspectionMethodCode listID="urn:ubl-examples:world:codelist:InspectionMethodCode">VISUAL</cbc:InspectionMethodCode>
      <cbc:BackOrderAllowedIndicator>true</cbc:BackOrderAllowedIndicator>
      <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
      <cbc:AccountingCost>Home and garden department</cbc:AccountingCost>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">380</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
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
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">FXEX</cbc:DescriptionCode>
            <cbc:Description>Solid ash</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000047</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">2</cbc:DurationMeasure>
      </cac:WarrantyValidityPeriod>
      <cac:WarrantyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brackenmere Furniture</cbc:Name>
        </cac:PartyName>
      </cac:WarrantyParty>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:ItemPriceExtension>
        <cbc:Amount currencyID="XBL">3040.00</cbc:Amount>
      </cac:ItemPriceExtension>
    </cac:LineItem>
    <cac:QuotationLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:QuotationLineReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cbc:Note>Price as quoted.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Note>Twice the target of twelve oak chairs, two with each oak bench.</cbc:Note>
      <cbc:Quantity unitCode="EA">24</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">2760.00</cbc:LineExtensionAmount>
      <cbc:MinimumQuantity unitCode="EA">12</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">24</cbc:MaximumQuantity>
      <cbc:MinimumBackorderQuantity unitCode="EA">6</cbc:MinimumBackorderQuantity>
      <cbc:MaximumBackorderQuantity unitCode="EA">12</cbc:MaximumBackorderQuantity>
      <cbc:InspectionMethodCode listID="urn:ubl-examples:world:codelist:InspectionMethodCode">VISUAL</cbc:InspectionMethodCode>
      <cbc:BackOrderAllowedIndicator>true</cbc:BackOrderAllowedIndicator>
      <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
      <cbc:AccountingCost>Home and garden department</cbc:AccountingCost>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">115</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
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
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">QCXE</cbc:DescriptionCode>
            <cbc:Description>Solid oak</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000023</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">2</cbc:DurationMeasure>
      </cac:WarrantyValidityPeriod>
      <cac:WarrantyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brackenmere Furniture</cbc:Name>
        </cac:PartyName>
      </cac:WarrantyParty>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:ItemPriceExtension>
        <cbc:Amount currencyID="XBL">2760.00</cbc:Amount>
      </cac:ItemPriceExtension>
    </cac:LineItem>
    <cac:QuotationLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:QuotationLineReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cbc:Note>Price as quoted.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>4</cbc:ID>
      <cbc:Note>Twice the target of eight ash chairs, two with each ash bench.</cbc:Note>
      <cbc:Quantity unitCode="EA">16</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">1840.00</cbc:LineExtensionAmount>
      <cbc:MinimumQuantity unitCode="EA">8</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">16</cbc:MaximumQuantity>
      <cbc:MinimumBackorderQuantity unitCode="EA">4</cbc:MinimumBackorderQuantity>
      <cbc:MaximumBackorderQuantity unitCode="EA">8</cbc:MaximumBackorderQuantity>
      <cbc:InspectionMethodCode listID="urn:ubl-examples:world:codelist:InspectionMethodCode">VISUAL</cbc:InspectionMethodCode>
      <cbc:BackOrderAllowedIndicator>true</cbc:BackOrderAllowedIndicator>
      <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
      <cbc:AccountingCost>Home and garden department</cbc:AccountingCost>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">115</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
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
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">FXEX</cbc:DescriptionCode>
            <cbc:Description>Solid ash</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000054</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">2</cbc:DurationMeasure>
      </cac:WarrantyValidityPeriod>
      <cac:WarrantyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brackenmere Furniture</cbc:Name>
        </cac:PartyName>
      </cac:WarrantyParty>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:ItemPriceExtension>
        <cbc:Amount currencyID="XBL">1840.00</cbc:Amount>
      </cac:ItemPriceExtension>
    </cac:LineItem>
    <cac:QuotationLineReference>
      <cbc:LineID>4</cbc:LineID>
    </cac:QuotationLineReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cbc:Note>Price as quoted.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>5</cbc:ID>
      <cbc:Note>Free: one care kit with each bench, oak or ash.</cbc:Note>
      <cbc:Quantity unitCode="EA">20</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">0.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">0</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
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
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:ItemPriceExtension>
        <cbc:Amount currencyID="XBL">0.00</cbc:Amount>
      </cac:ItemPriceExtension>
    </cac:LineItem>
    <cac:QuotationLineReference>
      <cbc:LineID>5</cbc:LineID>
    </cac:QuotationLineReference>
  </cac:OrderLine>
</Order>
```
