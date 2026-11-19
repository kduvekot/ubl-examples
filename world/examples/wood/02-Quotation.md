# Quotation: Marrowdale Sawmill to Valdara Industries

*Example 2 of the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)" · [Quotation in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-QUOTATION-SCHEMA)*

The sawmill quotes per bundle of 50 slats, in oak with ash as an alternative, delivered at the factory, under the buyer's purchasing terms.

[The XML file](02-Quotation.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:quotation:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Quotation". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:sourcing:1.0**  
  The Trade Accord's process profile the document belongs to: sourcing, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **WOOD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **MS-DOC-26-0626**  
  The seller's quotation number.
- `UUID` = **01317a73-7091-58bf-ad79-782d5646840a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-19**  
  The sawmill quotes for the slats.
- `IssueTime` = **11:34:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Note` = **Valid for 30 days.**  
  The validity.
- `PricingCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  Prices in lume. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **1**  
  One line.

### Validity Period

Inside `ValidityPeriod`:

- `EndDate` = **2026-03-21**  
  How long the quoted prices hold.

### Request For Quotation Document Reference

Inside `RequestForQuotationDocumentReference`:

- `ID` = **VI-DOC-26-0625**  
  The request this quotation answers.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **MS-GTC-2026**  
  The sawmill's general terms of sale, subsidiary to the buyer's terms (D43).
- `DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, Marrowdale Sawmill's general terms of sale, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `DocumentDescription` = **The sawmill's general terms of sale apply only where the buyer's purchasing terms VI-PUR-TERMS-2026, which govern, say nothing.**  
  Which terms govern.

### Contract

Inside `Contract`:

- `ID` = **VI-PUR-TERMS-2026**  
  The buyer's purchasing terms, which govern the quotation (D43).

### Signature

Inside `Signature`:

- `ID` = **MS-SIG-26-QT**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Marrowdale Sawmill**  
  A party referred to from another party's details: its identifier and name are enough.

### Seller Supplier Party

Inside `SellerSupplierParty`:

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
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 338 173**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Marrowdale Sawmill (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Marrowdale Sawmill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XU = Urvanian English.
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
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `PromisedDeliveryPeriod/StartDate` = **2026-02-26**  
  From the end of the second week, as asked.
- `PromisedDeliveryPeriod/EndDate` = **2026-03-06**  
  Within about a week.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **DAP** (schemeID `INCOTERMS`)  
  Delivered at the factory, as asked. The code is from the world's copy of Incoterms 2020: DAP = Delivered at Place. An identifier that holds a code names the code's list in its schemeID.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  By credit transfer. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.

### Transaction Conditions

Inside `TransactionConditions`:

- `Description` = **Priced per bundle of 50 slats; the smallest order is one truck: 96 bundles on 24 pallets.**  
  The conditions (D43).

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **true**  
  A charge.
- `AllowanceChargeReasonCode` = **ACH** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code of UN/EDIFACT 7161: the pallets are heat-treated. The code is from the world's copy of UN/EDIFACT 7161 Special service description: ACH = Heat treatment.
- `AllowanceChargeReason` = **Heat-treated export pallets**  
  The 96 bundles travel four to a pallet, on 24 pallets treated to ISPM 15, as the quotation offered for the export.
- `Amount` = **240.00** (currencyID `XBL`)  
  24 pallets at 10.00 lume.
- `TaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `TaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Destination Country

Inside `DestinationCountry`:

- `IdentificationCode` = **XU** (listID `ISO 3166`)  
  Into Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **34800.00** (currencyID `XBL`)  
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

### Quoted Monetary Total

Inside `QuotedMonetaryTotal`:

- `LineExtensionAmount` = **34560.00** (currencyID `XBL`)  
  The sum of the quoted lines.
- `ChargeTotalAmount` = **240.00** (currencyID `XBL`)  
  The export pallets.
- `PayableAmount` = **34800.00** (currencyID `XBL`)  
  The slats and the pallets; no tax on an export.

### Quotation Line

Inside `QuotationLine`:

- `ID` = **1**  
  The quotation line.
- `Note` = **Oak, as drawn, in bundles of 50; the same bundle in ash is offered below.**  
  What is quoted.
- `Quantity` = **96** (unitCode `EA`)  
  The bundles quoted: 4,800 slats, one truck.
- `LineExtensionAmount` = **34560.00** (currencyID `XBL`)  
  The quoted amount.
- `TaxInclusiveLineExtensionAmount` = **34560.00** (currencyID `XBL`)  
  No tax on an export.
- `TotalTaxAmount` = **0.00** (currencyID `XBL`)  
  No tax on an export.
- `RequestForQuotationLineID` = **1**  
  The line of the request.
- `DocumentReference/ID` = **VI-DS-SL1800**  
  The buyer's drawing the slat is quoted to (D43).
- `DocumentReference/DocumentTypeCode` = **174** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, Valdara's drawing of the bench slat, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 174 = Drawing.
- `DocumentReference/ID` = **MS-SPEC-SL1800**  
  The sawmill's own specification of the slat, derived from the buyer's drawing (D43).
- `DocumentReference/DocumentType` = **Product specification**  
  The kind of document referred to, Marrowdale Sawmill's specification of the slat, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **96** (unitCode `EA`)  
  96 bundles of 50 oak slats, 4,800 slats: enough for 960 benches at five a bench, a quarter's supply (D43).
- `LineItem/LineExtensionAmount` = **34560.00** (currencyID `XBL`)  
  Quantity times the quoted price.
- `LineItem/Price/PriceAmount` = **360** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Bundle of 50 hardwood bench slats, the sawmill's slat MS-SL-1800 (Valdara's part VI-R-SL1800): oak, sawn to 1800 × 95 × 38 mm, planed, kiln dried; five across and ten high, strapped.**  
  The seller's description; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `LineItem/Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/Name` = **Bench slat 1800, bundle of 50**  
  The item's short name; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **MS-SL-1800-50**  
  The seller's own item number; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **440799** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 440799 = Wood sawn or chipped lengthwise, of a thickness exceeding 6 mm: other.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **31102** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 31102 = Wood, sawn or chipped lengthwise, sliced or peeled, of a thickness exceeding 6 mm, of non-coniferous wood .
- `LineItem/Item/AdditionalItemProperty/ID` = **MC**  
  The maker's identifier for the property.
- `LineItem/Item/AdditionalItemProperty/Name` = **Moisture content**  
  The name of code MC in the Trade Accord's item property name list.
- `LineItem/Item/AdditionalItemProperty/NameCode` = **MC** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: MC = Moisture content.
- `LineItem/Item/AdditionalItemProperty/TestMethod` = **Oven-dry method on samples from each kiln charge**  
  How the value is tested.
- `LineItem/Item/AdditionalItemProperty/ValueQuantity` = **12** (unitCode `P1`)  
  Its measured value; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/AdditionalItemProperty/ValueQualifier` = **Average of the kiln charge**  
  What the value stands for.
- `LineItem/Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `LineItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **QUA**  
  The group of properties this one belongs to.
- `LineItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Wood quality**  
  The group's name.
- `LineItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `LineItem/Item/AdditionalItemProperty/ItemPropertyRange/MinimumValue` = **10**  
  The lowest value accepted.
- `LineItem/Item/AdditionalItemProperty/ItemPropertyRange/MaximumValue` = **14**  
  The highest value accepted.
- `LineItem/Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-WD-0012** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `LineItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **WD**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `LineItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **xu_t6hq** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/AdditionalItemProperty/SubItemProperty/Name` = **Moisture at the core**  
  Measured at the centre of the slat.
- `LineItem/Item/AdditionalItemProperty/SubItemProperty/ValueQuantity` = **13** (unitCode `P1`)  
  Its measured value; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/AdditionalItemProperty/Name` = **Thickness tolerance**  
  How far a slat may be off its thickness.
- `LineItem/Item/AdditionalItemProperty/RangeDimension/AttributeID` = **THICKNESS** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The dimension the tolerance is for. The code is from the Trade Accord's dimension attribute list: THICKNESS = Thickness. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/AdditionalItemProperty/RangeDimension/Measure` = **38** (unitCode `MMT`)  
  Its nominal size.
- `LineItem/Item/AdditionalItemProperty/RangeDimension/MinimumMeasure` = **37.5** (unitCode `MMT`)  
  The smallest size accepted.
- `LineItem/Item/AdditionalItemProperty/RangeDimension/MaximumMeasure` = **38.5** (unitCode `MMT`)  
  The largest size accepted.
- `LineItem/Item/AdditionalItemProperty/Name` = **Surface**  
  A property buyers ask about.
- `LineItem/Item/AdditionalItemProperty/Value` = **Planed on four sides**  
  Its value; item slat-bundle-1800 of Marrowdale Sawmill (world/items.json).
- `LineItem/Item/Certificate/ID` = **XB-FOR-2025-0118** (schemeID `urn:ubl-examples:world:XB:forestry-register`)  
  The number of the certificate, in the forestry register of Bayvarra, which keeps the certificates issued under each registration; the schemeID names the register and its authority, so no issuer party is needed (decision ID-Q10).
- `LineItem/Item/Certificate/CertificateTypeCode` = **SUSTFOREST** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  The kind of certificate, as a code. The code is from the Trade Accord's certificate type list: SUSTFOREST = Sustainable forestry.
- `LineItem/Item/Certificate/CertificateType` = **Sustainable forestry**  
  The name of code SUSTFOREST in the Trade Accord's certificate type list.
- `LineItem/Item/Certificate/CertificateReferenceID` = **XB-FOR-REG-0118** (schemeID `urn:ubl-examples:world:XB:forestry-register`)  
  The registration the certificate is issued under: the sawmill's own number in the same register, which the certificate's number repeats after its year.
- `LineItem/Item/Certificate/ApplicableCategoryCode` = **HW** (listID `urn:ubl-examples:world:codelist:CategoryCode`)  
  The category of goods the certificate covers. The code is from the Trade Accord's certified product category list: HW = Hardwood sawn timber.
- `LineItem/Item/Certificate/ApplicableCategory` = **Hardwood sawn timber**  
  The name of code HW in the Trade Accord's certified product category list.
- `LineItem/Item/Certificate/CertificateURI` = **https://forestry.xb.example/certificates/XB-FOR-2025-0118**  
  Where the certificate can be checked.
- `LineItem/Item/Certificate/Remarks` = **The timber comes from forests in Upland State managed for regrowth.**  
  What the certificate states about the goods.
- `LineItem/Item/Certificate/CertificateValidityPeriod/EndDate` = **2027-12-31**  
  The certificate is valid until then.
- `LineItem/Item/Certificate/DocumentReference/ID` = **XB-FOR-AUD-2025-0118**  
  The audit report the certificate is based on.
- `LineItem/Item/Certificate/DocumentReference/DocumentType` = **Forest management audit report**  
  The kind of document referred to, the audit report behind the forestry certificate, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `LineItem/Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `LineItem/Item/Dimension/Description` = **The bundle: the slats' length**  
  Where it is measured.
- `LineItem/Item/Dimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **475** (unitCode `MMT`)  
  Its size.
- `LineItem/Item/Dimension/Description` = **The bundle: five slats of 95 mm side by side**  
  Where it is measured.
- `LineItem/Item/Dimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/Dimension/Measure` = **380** (unitCode `MMT`)  
  Its size.
- `LineItem/Item/Dimension/Description` = **The bundle: ten slats of 38 mm stacked**  
  Where it is measured.
- `AlternativeLineItem/ID` = **1-A**  
  The other species the request allowed (D43).
- `AlternativeLineItem/Quantity` = **96** (unitCode `EA`)  
  The same quantity.
- `AlternativeLineItem/Price/PriceAmount` = **330** (currencyID `XBL`)  
  The price of a bundle in ash, below oak's.
- `AlternativeLineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  Per bundle.
- `AlternativeLineItem/Item/Name` = **Bench slat 1800, bundle of 50, ash**  
  The same bundle in ash, which the sawmill can saw from its next felling.
- `RequestLineReference/LineID` = **1**  
  The request line answered.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Quotation xmlns="urn:oasis:names:specification:ubl:schema:xsd:Quotation-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:quotation:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:sourcing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>WOOD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>MS-DOC-26-0626</cbc:ID>
  <cbc:UUID>01317a73-7091-58bf-ad79-782d5646840a</cbc:UUID>
  <cbc:IssueDate>2026-02-19</cbc:IssueDate>
  <cbc:IssueTime>11:34:00-01:00</cbc:IssueTime>
  <cbc:Note>Valid for 30 days.</cbc:Note>
  <cbc:PricingCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:PricingCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:ValidityPeriod>
    <cbc:EndDate>2026-03-21</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:RequestForQuotationDocumentReference>
    <cbc:ID>VI-DOC-26-0625</cbc:ID>
  </cac:RequestForQuotationDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>MS-GTC-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>The sawmill's general terms of sale apply only where the buyer's purchasing terms VI-PUR-TERMS-2026, which govern, say nothing.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
  <cac:Contract>
    <cbc:ID>VI-PUR-TERMS-2026</cbc:ID>
  </cac:Contract>
  <cac:Signature>
    <cbc:ID>MS-SIG-26-QT</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SellerSupplierParty>
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
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
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
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
      </cac:Language>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:Delivery>
    <cac:PromisedDeliveryPeriod>
      <cbc:StartDate>2026-02-26</cbc:StartDate>
      <cbc:EndDate>2026-03-06</cbc:EndDate>
    </cac:PromisedDeliveryPeriod>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">DAP</cbc:ID>
  </cac:DeliveryTerms>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
  </cac:PaymentMeans>
  <cac:TransactionConditions>
    <cbc:Description>Priced per bundle of 50 slats; the smallest order is one truck: 96 bundles on 24 pallets.</cbc:Description>
  </cac:TransactionConditions>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">ACH</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Heat-treated export pallets</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XBL">240.00</cbc:Amount>
    <cac:TaxCategory>
      <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
      <cbc:Percent>0</cbc:Percent>
      <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
      <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:AllowanceCharge>
  <cac:DestinationCountry>
    <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
  </cac:DestinationCountry>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">34800.00</cbc:TaxableAmount>
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
  <cac:QuotedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">34560.00</cbc:LineExtensionAmount>
    <cbc:ChargeTotalAmount currencyID="XBL">240.00</cbc:ChargeTotalAmount>
    <cbc:PayableAmount currencyID="XBL">34800.00</cbc:PayableAmount>
  </cac:QuotedMonetaryTotal>
  <cac:QuotationLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Oak, as drawn, in bundles of 50; the same bundle in ash is offered below.</cbc:Note>
    <cbc:Quantity unitCode="EA">96</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XBL">34560.00</cbc:LineExtensionAmount>
    <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">34560.00</cbc:TaxInclusiveLineExtensionAmount>
    <cbc:TotalTaxAmount currencyID="XBL">0.00</cbc:TotalTaxAmount>
    <cbc:RequestForQuotationLineID>1</cbc:RequestForQuotationLineID>
    <cac:DocumentReference>
      <cbc:ID>VI-DS-SL1800</cbc:ID>
      <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">174</cbc:DocumentTypeCode>
    </cac:DocumentReference>
    <cac:DocumentReference>
      <cbc:ID>MS-SPEC-SL1800</cbc:ID>
      <cbc:DocumentType>Product specification</cbc:DocumentType>
    </cac:DocumentReference>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">34560.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">360</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Bundle of 50 hardwood bench slats, the sawmill's slat MS-SL-1800 (Valdara's part VI-R-SL1800): oak, sawn to 1800 × 95 × 38 mm, planed, kiln dried; five across and ten high, strapped.</cbc:Description>
        <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
        <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
        <cbc:Name>Bench slat 1800, bundle of 50</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>MS-SL-1800-50</cbc:ID>
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
                <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_t6hq</cbc:ID>
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
          <cbc:Description>The bundle: the slats' length</cbc:Description>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">475</cbc:Measure>
          <cbc:Description>The bundle: five slats of 95 mm side by side</cbc:Description>
        </cac:Dimension>
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">380</cbc:Measure>
          <cbc:Description>The bundle: ten slats of 38 mm stacked</cbc:Description>
        </cac:Dimension>
      </cac:Item>
    </cac:LineItem>
    <cac:AlternativeLineItem>
      <cbc:ID>1-A</cbc:ID>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">330</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Name>Bench slat 1800, bundle of 50, ash</cbc:Name>
      </cac:Item>
    </cac:AlternativeLineItem>
    <cac:RequestLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:RequestLineReference>
  </cac:QuotationLine>
</Quotation>
```
