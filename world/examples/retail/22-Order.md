# Order: Robin Ashdale to Brightmarket Stores

*Example 22 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The consumer orders a Marrow set, an Elderwick Marrow bench and two chairs, all in ash, in the store's webshop, to collect it in the store, and pays by credit card: the order carries the full card data, security code included, so that the store can have the payment authorised before it reserves the pieces.

[The XML file](22-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **RETAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **RA-PO-26-0240**  
  The webshop's order number: the store's site writes the order for the customer and numbers it.
- `UUID` = **6f338d06-4cfb-5630-b53e-6ac243c84956**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-30**  
  Placed in the webshop on Saturday 30 May.
- `IssueTime` = **11:25:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `Note` = **Click and collect: ready in the home and garden department from Tuesday 2 June; bring the card used for the order.**  
  What the webshop tells the customer.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **3**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyName/Name` = **Robin Ashdale**  
  The trading name; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/ID` = **LUM-ADR-934215** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Person/FirstName` = **Robin**  
  The consumer's first name; identity of Robin Ashdale (world/parties.json).
- `Party/Person/FamilyName` = **Ashdale**  
  The consumer's family name; identity of Robin Ashdale (world/parties.json).

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `Party/TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Customer service**  
  The party's customer service desk: the desk for its role in this document (it sells); identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Department` = **Customer service**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 4609 7100**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/ElectronicMail` = **service@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `DeliveryLocation/ID` = **9522610900026** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, home and garden department of the lumeport store: Brightmarket Stores identifies its places the GS1 way, under its company prefix (952, reserved for examples); world/parties.json.
- `DeliveryLocation/Name` = **Home and garden department, Lumeport store**  
  Where the set is collected.
- `RequestedDeliveryPeriod/StartDate` = **2026-06-02**  
  From Tuesday 2 June.
- `RequestedDeliveryPeriod/EndDate` = **2026-06-09**  
  The store keeps it a week.
- `DeliveryParty/PartyName/Name` = **Robin Ashdale**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **EXW** (schemeID `INCOTERMS`)  
  Ex works the store: the customer collects the set; there is no transport to arrange. The code is from the world's copy of Incoterms 2020: EXW = Ex Works. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **9522610900026** (schemeID `GS1 GLN`)  
  The place's identifier, as the world gives it wherever the place appears (a GLN; worklist C23).
- `DeliveryLocation/Description` = **Home and garden department of the Lumeport store**  
  Where the delivery terms place the handover of the goods.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **54** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 54: credit card. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 54 = Credit card.
- `CardAccount/PrimaryAccountNumberID` = **9902382000715526**  
  The full card number the customer typed in: the store needs it to have the payment authorised. It starts with 9 and the numeric code of the issuer's country (902, Bayvarra), as ISO/IEC 7812 provides for national use, so it is no real card's; its last digit is the Luhn check digit.
- `CardAccount/NetworkID` = **TRESSACARD** (schemeID `urn:ubl-examples:world:codelist:CardSchemeCode`)  
  Tressa, the Accord-wide credit card scheme. The code is from the Trade Accord's payment card scheme list: TRESSACARD = Tressa. An identifier that holds a code names the code's list in its schemeID.
- `CardAccount/CardTypeCode` = **CREDIT** (listID `urn:ubl-examples:world:codelist:CardTypeCode`)  
  A credit card. The code is from the Trade Accord's payment card type list: CREDIT = Credit card.
- `CardAccount/ValidityStartDate` = **2025-03-01**  
  The card is valid from 2025-03, the month printed on it: its first day.
- `CardAccount/ExpiryDate` = **2029-02-28**  
  The card expires at the end of 2029-02, the month printed on it: its last day. The issuer checks it in the authorisation.
- `CardAccount/IssuerID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The card's issuer, Bank of Lumeport, by its bank identifier.
- `CardAccount/CV2ID` = **731**  
  The card's security code from the back of the card, typed in by the customer, so that the issuer can check that the card is at hand. PCI DSS allows the store to hold it only until the authorisation; it is deleted then and printed nowhere.
- `CardAccount/HolderName` = **R ASHDALE**  
  The name on the card, as typed in.
- `CardAccount/RoleCode` = **HOLDER** (listID `urn:ubl-examples:world:codelist:CardAccountRoleCode`)  
  The customer pays with its own card. The code is from the Trade Accord's card account role list: HOLDER = Card holder.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189: a discount; the text names the offer. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `AllowanceChargeReason` = **Marrow set**  
  The shop's offer: a bench and two chairs in the same wood bought together cost 899 lume instead of 947. The set is no item of its own, so the pieces are on their lines and the offer is this allowance.
- `Amount` = **48.00** (currencyID `XBL`)  
  549 + 2 × 199 = 947, less 48 = 899.
- `TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **58.44** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **899.00** (currencyID `XBL`)  
  The line amounts less the set allowance.
- `TaxSubtotal/TaxAmount` = **58.44** (currencyID `XBL`)  
  6.5 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **947.00** (currencyID `XBL`)  
  The sum of the line amounts: the pieces at their shelf prices.
- `AllowanceTotalAmount` = **48.00** (currencyID `XBL`)  
  The set allowance.
- `PayableAmount` = **957.44** (currencyID `XBL`)  
  What the customer pays: the set at 899 lume and Coastal State's 6.5 % sales tax.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own (worklist C34).
- `LineItem/Quantity` = **1** (unitCode `EA`)  
  The bench of the Marrow set: the customer chose ash for the set.
- `LineItem/LineExtensionAmount` = **549.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **549** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining bench, 1400 mm, in solid ash, from the home and garden department; also sold in the Marrow set of a bench and two chairs in the same wood, 899 lume instead of 947; the state sales tax is added at the till.**  
  The seller's description; item marrow-bench-ash-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/Name` = **Elderwick Marrow bench, ash**  
  The item's short name; item marrow-bench-ash-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **BM-551008**  
  The seller's own item number; item marrow-bench-ash-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/ManufacturersItemIdentification/ID` = **BF-MRW-B14**  
  The item number of the maker, Brackenmere Furniture: the reseller's item is resale of item marrow-bench-ash.
- `LineItem/Item/ManufacturersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `LineItem/Item/ManufacturersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/ManufacturersItemIdentification/PhysicalAttribute/DescriptionCode` = **ASH** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: ASH = Ash.
- `LineItem/Item/ManufacturersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000047** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item (world/items.json).
- `LineItem/ID` = **2**  
  The line number: a line added by a change keeps a number of its own (worklist C34).
- `LineItem/Quantity` = **2** (unitCode `EA`)  
  The two chairs of the Marrow set, in ash like the bench.
- `LineItem/LineExtensionAmount` = **398.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **199** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Dining chair in solid ash, from the home and garden department; also sold in the Marrow set of a bench and two chairs in the same wood, 899 lume instead of 947; the state sales tax is added at the till.**  
  The seller's description; item marrow-chair-ash-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/Name` = **Elderwick Marrow chair, ash**  
  The item's short name; item marrow-chair-ash-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **BM-551009**  
  The seller's own item number; item marrow-chair-ash-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/ManufacturersItemIdentification/ID` = **BF-MRW-C**  
  The item number of the maker, Brackenmere Furniture: the reseller's item is resale of item marrow-chair-ash.
- `LineItem/Item/ManufacturersItemIdentification/ExtendedID` = **ASH**  
  The variant of the item: the wood, added to the item number.
- `LineItem/Item/ManufacturersItemIdentification/PhysicalAttribute/AttributeID` = **WOOD** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: WOOD = Wood. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/ManufacturersItemIdentification/PhysicalAttribute/DescriptionCode` = **ASH** (listID `urn:ubl-examples:world:codelist:WoodCode`)  
  The variant's code for it. The code is from the Trade Accord's wood list: ASH = Ash.
- `LineItem/Item/ManufacturersItemIdentification/PhysicalAttribute/Description` = **Solid ash**  
  The variant in words.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000054** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item (world/items.json).
- `LineItem/ID` = **3**  
  The line number: a line added by a change keeps a number of its own (worklist C34).
- `LineItem/Quantity` = **1** (unitCode `EA`)  
  The care kit that comes free with the bench.
- `LineItem/LineExtensionAmount` = **0.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **0** (currencyID `XBL`)  
  No price: the item comes free with each Elderwick Marrow bench (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Hard-wax oil and a cloth for the Marrow dining furniture, free with each bench.**  
  The seller's description; item marrow-care-kit-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/Name` = **Elderwick care kit**  
  The item's short name; item marrow-care-kit-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **BM-551007**  
  The seller's own item number; item marrow-care-kit-r of Brightmarket Stores (world/items.json).
- `LineItem/Item/ManufacturersItemIdentification/ID` = **BF-MRW-K**  
  The item number of the maker, Brackenmere Furniture: the reseller's item is resale of item marrow-care-kit.
- `LineItem/Item/StandardItemIdentification/ID` = **9522610000030** (schemeID `GS1 GTIN`)  
  The GTIN Brightmarket Stores gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the item is Brightmarket Stores' own label Elderwick, made for it by Brackenmere Furniture: under GS1 rules the brand owner numbers the item, not the manufacturer, so the number is Brightmarket Stores', whoever sells the item (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>RETAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>RA-PO-26-0240</cbc:ID>
  <cbc:UUID>6f338d06-4cfb-5630-b53e-6ac243c84956</cbc:UUID>
  <cbc:IssueDate>2026-05-30</cbc:IssueDate>
  <cbc:IssueTime>11:25:00-01:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:Note>Click and collect: ready in the home and garden department from Tuesday 2 June; bring the card used for the order.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Robin Ashdale</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-934215</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">RESIDENTIAL</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Gull Lane</cbc:StreetName>
        <cbc:BuildingNumber>57</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Riverside</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38516</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Person>
        <cbc:FirstName>Robin</cbc:FirstName>
        <cbc:FamilyName>Ashdale</cbc:FamilyName>
      </cac:Person>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
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
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="GS1 GLN">9522610900026</cbc:ID>
      <cbc:Name>Home and garden department, Lumeport store</cbc:Name>
    </cac:DeliveryLocation>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-06-02</cbc:StartDate>
      <cbc:EndDate>2026-06-09</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyName>
        <cbc:Name>Robin Ashdale</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">EXW</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="GS1 GLN">9522610900026</cbc:ID>
      <cbc:Description>Home and garden department of the Lumeport store</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">54</cbc:PaymentMeansCode>
    <cac:CardAccount>
      <cbc:PrimaryAccountNumberID>9902382000715526</cbc:PrimaryAccountNumberID>
      <cbc:NetworkID schemeID="urn:ubl-examples:world:codelist:CardSchemeCode">TRESSACARD</cbc:NetworkID>
      <cbc:CardTypeCode listID="urn:ubl-examples:world:codelist:CardTypeCode">CREDIT</cbc:CardTypeCode>
      <cbc:ValidityStartDate>2025-03-01</cbc:ValidityStartDate>
      <cbc:ExpiryDate>2029-02-28</cbc:ExpiryDate>
      <cbc:IssuerID schemeID="urn:ubl-examples:world:bank-identifier">BLUMXBLX</cbc:IssuerID>
      <cbc:CV2ID>731</cbc:CV2ID>
      <cbc:HolderName>R ASHDALE</cbc:HolderName>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:CardAccountRoleCode">HOLDER</cbc:RoleCode>
    </cac:CardAccount>
  </cac:PaymentMeans>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Marrow set</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XBL">48.00</cbc:Amount>
    <cac:TaxCategory>
      <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
      <cbc:Percent>6.5</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:AllowanceCharge>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">58.44</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">899.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">58.44</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">947.00</cbc:LineExtensionAmount>
    <cbc:AllowanceTotalAmount currencyID="XBL">48.00</cbc:AllowanceTotalAmount>
    <cbc:PayableAmount currencyID="XBL">957.44</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">549.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">549</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Dining bench, 1400 mm, in solid ash, from the home and garden department; also sold in the Marrow set of a bench and two chairs in the same wood, 899 lume instead of 947; the state sales tax is added at the till.</cbc:Description>
        <cbc:Name>Elderwick Marrow bench, ash</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BM-551008</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:ManufacturersItemIdentification>
          <cbc:ID>BF-MRW-B14</cbc:ID>
          <cbc:ExtendedID>ASH</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">ASH</cbc:DescriptionCode>
            <cbc:Description>Solid ash</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:ManufacturersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000047</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">398.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">199</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Dining chair in solid ash, from the home and garden department; also sold in the Marrow set of a bench and two chairs in the same wood, 899 lume instead of 947; the state sales tax is added at the till.</cbc:Description>
        <cbc:Name>Elderwick Marrow chair, ash</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BM-551009</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:ManufacturersItemIdentification>
          <cbc:ID>BF-MRW-C</cbc:ID>
          <cbc:ExtendedID>ASH</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">WOOD</cbc:AttributeID>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:WoodCode">ASH</cbc:DescriptionCode>
            <cbc:Description>Solid ash</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:ManufacturersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000054</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">0.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">0</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Hard-wax oil and a cloth for the Marrow dining furniture, free with each bench.</cbc:Description>
        <cbc:Name>Elderwick care kit</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>BM-551007</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:ManufacturersItemIdentification>
          <cbc:ID>BF-MRW-K</cbc:ID>
        </cac:ManufacturersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9522610000030</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
