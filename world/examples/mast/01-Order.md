# Order: Selanu Telecom to Saltmere Engineering

*Example 1 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The telecom company orders back-up power and safety equipment for its mast. Carriage paid to its site: the seller arranges the dangerous goods transport.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); PartyLegalEntity/EntitySizeCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **ST-PO-26-0713**  
  The buyer's order number.
- `UUID` = **b63839e1-7b35-5e81-a17d-ef60734d2fe6**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-01**  
  The telecom company orders before the storm season.
- `IssueTime` = **08:15:00**  
  The time the sender's system issued the document, in the sender's local time.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **3**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/WebsiteURI` = **https://www.selanutelecom.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Telecom (world/parties.json).
- `Party/IndustryClassificationCode` = **6110** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Telecom (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 6110 = Wired telecommunications activities.
- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 20 persons and its turnover of 3230000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Telecom (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/Contact/Name` = **Business accounts**  
  The desk that handles this document; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 727 2407**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Party/Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/IndustryClassificationCode` = **4290** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Saltmere Engineering (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4290 = Construction of other civil engineering projects.
- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered for state sales tax; identity of Saltmere Engineering (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1232055** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Saltmere Engineering (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered, with its legal form; identity of Saltmere Engineering (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Bids office**  
  The desk that handles this document; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 885 685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `DeliveryParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Selanu Telecom**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CPT** (schemeID `INCOTERMS`)  
  Carriage paid to the telecom company's site: the seller arranges the dangerous goods transport. The code is from the world's copy of Incoterms 2020: CPT = Carriage Paid To. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/Description` = **Selanu Telecom, mast site**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **14770.00** (currencyID `XBL`)  
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

- `LineExtensionAmount` = **14770.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **14770.00** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **6** (unitCode `EA`)  
  Six packs: four hours of back-up power for the mast.
- `LineItem/LineExtensionAmount` = **14400.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **2400** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.**  
  The seller's description; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/Name` = **Lithium-ion battery pack 48 V 100 Ah**  
  The item's short name; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-BAT-48100**  
  The seller's own item number; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **850760** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 850760 = Lithium-ion accumulators.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **46420** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 46420 = Electric accumulators.
- `LineItem/Item/HazardousItem/ID` = **SE-BAT-48100-DG**  
  The seller's dangerous goods record of the item.
- `LineItem/Item/HazardousItem/PlacardNotation` = **9**  
  The class shown on the placard.
- `LineItem/Item/HazardousItem/PlacardEndorsement` = **9A**  
  The hazard label on the package.
- `LineItem/Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds.
- `LineItem/Item/HazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `LineItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **Lelaha palavo molasu maloli** (languageID `qal`)  
  The name of code NA in the Trade Accord's packing group list. In Lisavan, the sender's language.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned** (languageID `en-XL`)  
  The name of code NA in the Trade Accord's packing group list. In English.
- `LineItem/Item/HazardousItem/EmergencyProceduresCode` = **F-A,S-I** (listID `IMO IMDG EmS`)  
  The emergency schedules for ships (EmS) of the IMDG Code for this UN entry: the fire schedule and the spillage schedule. The code is from the world's copy of IMO IMDG Code emergency schedules (EmS): F-A,S-I = Fire schedule Alpha, spillage schedule India.
- `LineItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **147** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 147 = Lithium Ion and Sodium Ion Batteries.
- `LineItem/Item/HazardousItem/TunnelRestrictionCode` = **E** (listID `UNECE ADR tunnel restriction code`)  
  The tunnel restriction code for road transport. The code is from the world's copy of ADR tunnel restriction code: E.
- `LineItem/Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `LineItem/Item/HazardousItem/HazardousCategoryCode` = **9** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles.
- `LineItem/Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `LineItem/Item/HazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/ID` = **2**  
  The line number.
- `LineItem/Quantity` = **1** (unitCode `SET`)  
  One set of ten for the equipment room.
- `LineItem/LineExtensionAmount` = **180.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **180** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `SET`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/Name` = **Ionisation smoke detector set**  
  The item's short name; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-SMK-10**  
  The seller's own item number; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **853110** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 853110 = Burglar or fire alarms and similar apparatus.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **46921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 46921 = Burglar or fire alarms and similar apparatus.
- `LineItem/Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `LineItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the placard.
- `LineItem/Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label, the UN number on the package.**  
  What the shipper adds.
- `LineItem/Item/HazardousItem/UNDGCode` = **2911** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2911 = Radioactive material, excepted package – instruments or articles.
- `LineItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **Lelaha palavo molasu maloli** (languageID `qal`)  
  The name of code NA in the Trade Accord's packing group list. In Lisavan, the sender's language.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned** (languageID `en-XL`)  
  The name of code NA in the Trade Accord's packing group list. In English.
- `LineItem/Item/HazardousItem/EmergencyProceduresCode` = **F-I,S-S** (listID `IMO IMDG EmS`)  
  The emergency schedules for ships (EmS) of the IMDG Code for this UN entry: the fire schedule and the spillage schedule. The code is from the world's copy of IMO IMDG Code emergency schedules (EmS): F-I,S-S = Fire schedule India, spillage schedule Sierra.
- `LineItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **161** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 161 = Radioactive Materials (Low Level Radiation).
- `LineItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `LineItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `LineItem/Item/HazardousItem/MarkingID` = **UN2911**  
  The UN number marked on each package.
- `LineItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Americium-241 sources in smoke detectors**  
  The material.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Sealed source, not special form.**  
  Its form.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **0**  
  Excepted package: no dose rate to speak of.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/FissileCriticalitySafetyIndexNumeric` = **0**  
  Not fissile.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/Name` = **Americium-241**  
  The isotope.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/ActivityLevelMeasure` = **37** (unitCode `2Q`)  
  Per detector.
- `LineItem/ID` = **3**  
  The line number.
- `LineItem/Quantity` = **20** (unitCode `LTR`)  
  Four cans of five litres for the circuit boards.
- `LineItem/LineExtensionAmount` = **190.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **9.5** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `LTR`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Remover for the protective coating of circuit boards, in 5-litre cans.**  
  The seller's description; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/Name` = **Coating stripper for electronics**  
  The item's short name; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-CS-05**  
  The seller's own item number; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **381400** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 381400 = Organic composite solvents and thinners, n.e.s.; prepared paint or varnish removers.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **35110** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 35110 = Paints and varnishes and related products.
- `LineItem/Item/HazardousItem/ID` = **SE-CS-05-DG**  
  The seller's dangerous goods record of the item.
- `LineItem/Item/HazardousItem/PlacardNotation` = **8**  
  The class shown on the placard.
- `LineItem/Item/HazardousItem/PlacardEndorsement` = **8**  
  The hazard label on the package.
- `LineItem/Item/HazardousItem/AdditionalInformation` = **Packed as the rules require.**  
  What the shipper adds.
- `LineItem/Item/HazardousItem/UNDGCode` = **2920** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2920 = Corrosive liquid, flammable, n.o.s..
- `LineItem/Item/HazardousItem/UNPackingGroupCode` = **II** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: II = Medium danger.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **Filupa vuhote** (languageID `qal`)  
  The name of code II in the Trade Accord's packing group list. In Lisavan, the sender's language.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **Medium danger** (languageID `en-XL`)  
  The name of code II in the Trade Accord's packing group list. In English.
- `LineItem/Item/HazardousItem/EmergencyProceduresCode` = **F-E,S-C** (listID `IMO IMDG EmS`)  
  The emergency schedules for ships (EmS) of the IMDG Code for this UN entry: the fire schedule and the spillage schedule. The code is from the world's copy of IMO IMDG Code emergency schedules (EmS): F-E,S-C = Fire schedule Echo, spillage schedule Charlie.
- `LineItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **132** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 132 = Flammable Liquids - Corrosive.
- `LineItem/Item/HazardousItem/TunnelRestrictionCode` = **D/E** (listID `UNECE ADR tunnel restriction code`)  
  The tunnel restriction code for road transport. The code is from the world's copy of ADR tunnel restriction code: D/E.
- `LineItem/Item/HazardousItem/MaritimePollutantCode` = **N** (listID `urn:ubl-examples:world:codelist:MarinePollutantCode`)  
  Not a marine pollutant. The code is from the Trade Accord's marine pollutant list: N = Not a marine pollutant.
- `LineItem/Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `LineItem/Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `LineItem/Item/HazardousItem/HazardousCategoryCode` = **8** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances.
- `LineItem/Item/HazardousItem/MarkingID` = **UN2920**  
  The UN number marked on each package.
- `LineItem/Item/HazardousItem/HazardClassID` = **8** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/HazardousItem/SecondaryHazard/ID` = **3** (schemeID `UN Model Regulations hazard class`)  
  The subsidiary hazard: flammable. The code is from the world's copy of UN Model Regulations hazard class and division: 3 = Flammable liquids. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/HazardousItem/SecondaryHazard/PlacardNotation` = **3**  
  Shown on a second label.
- `LineItem/Item/HazardousItem/SecondaryHazard/PlacardEndorsement` = **3**  
  The flammable liquid label.
- `LineItem/Item/HazardousItem/SecondaryHazard/Extension` = **Subsidiary risk 3**  
  In words.
- `LineItem/Item/HazardousItem/FlashpointTemperature/AttributeID` = **FLASHPOINT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Closed cup. The code is from the Trade Accord's temperature attribute list: FLASHPOINT = Flashpoint. An identifier that holds a code names the code's list in its schemeID.
- `LineItem/Item/HazardousItem/FlashpointTemperature/Measure` = **28** (unitCode `CEL`)  
  The flashpoint.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>ST-PO-26-0713</cbc:ID>
  <cbc:UUID>b63839e1-7b35-5e81-a17d-ef60734d2fe6</cbc:UUID>
  <cbc:IssueDate>2026-06-01</cbc:IssueDate>
  <cbc:IssueTime>08:15:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.selanutelecom.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">6110</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">34928611</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Mast Hill Road</cbc:StreetName>
        <cbc:BuildingNumber>58</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Telecom Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Business accounts</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 727 2407</cbc:Telephone>
        <cbc:ElectronicMail>business@selanutelecom.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4290</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saltmere Engineering</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
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
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1232055</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Marrowdale</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Bids office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 7121 885 685</cbc:Telephone>
        <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
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
      <cbc:Description>Selanu Telecom, mast site</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">14770.00</cbc:TaxableAmount>
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
    <cbc:LineExtensionAmount currencyID="XBL">14770.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">14770.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">6</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">14400.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">2400</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.</cbc:Description>
        <cbc:Name>Lithium-ion battery pack 48 V 100 Ah</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-BAT-48100</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">850760</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">46420</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-BAT-48100-DG</cbc:ID>
          <cbc:PlacardNotation>9</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>9A</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>State of charge below 30 %, as the air rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">3480</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup languageID="qal">Lelaha palavo molasu maloli</cbc:UNPackingGroup>
          <cbc:UNPackingGroup languageID="en-XL">No packing group assigned</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode listID="IMO IMDG EmS">F-A,S-I</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">147</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode listID="UNECE ADR tunnel restriction code">E</cbc:TunnelRestrictionCode>
          <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">9</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN3480</cbc:MarkingID>
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
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">853110</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">46921</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-SMK-10-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Excepted package: no radioactive label, the UN number on the package.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2911</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup languageID="qal">Lelaha palavo molasu maloli</cbc:UNPackingGroup>
          <cbc:UNPackingGroup languageID="en-XL">No packing group assigned</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode listID="IMO IMDG EmS">F-I,S-S</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">161</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2911</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
          <cac:RadioactiveMaterial>
            <cbc:Name>Americium-241 sources in smoke detectors</cbc:Name>
            <cbc:SpecialFormDescription>Sealed source, not special form.</cbc:SpecialFormDescription>
            <cbc:TransportIndexNumeric>0</cbc:TransportIndexNumeric>
            <cbc:FissileCriticalitySafetyIndexNumeric>0</cbc:FissileCriticalitySafetyIndexNumeric>
            <cac:ApplicableRadioactiveIsotope>
              <cbc:Name>Americium-241</cbc:Name>
              <cbc:ActivityLevelMeasure unitCode="2Q">37</cbc:ActivityLevelMeasure>
            </cac:ApplicableRadioactiveIsotope>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="LTR">20</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">190.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">9.5</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="LTR">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Remover for the protective coating of circuit boards, in 5-litre cans.</cbc:Description>
        <cbc:Name>Coating stripper for electronics</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-CS-05</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">381400</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35110</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-CS-05-DG</cbc:ID>
          <cbc:PlacardNotation>8</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>8</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>Packed as the rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2920</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">II</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup languageID="qal">Filupa vuhote</cbc:UNPackingGroup>
          <cbc:UNPackingGroup languageID="en-XL">Medium danger</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode listID="IMO IMDG EmS">F-E,S-C</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">132</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode listID="UNECE ADR tunnel restriction code">D/E</cbc:TunnelRestrictionCode>
          <cbc:MaritimePollutantCode listID="urn:ubl-examples:world:codelist:MarinePollutantCode">N</cbc:MaritimePollutantCode>
          <cbc:TechnicalName>ethanolamine, propanol</cbc:TechnicalName>
          <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">8</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2920</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">8</cbc:HazardClassID>
          <cac:SecondaryHazard>
            <cbc:ID schemeID="UN Model Regulations hazard class">3</cbc:ID>
            <cbc:PlacardNotation>3</cbc:PlacardNotation>
            <cbc:PlacardEndorsement>3</cbc:PlacardEndorsement>
            <cbc:Extension>Subsidiary risk 3</cbc:Extension>
          </cac:SecondaryHazard>
          <cac:FlashpointTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">FLASHPOINT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">28</cbc:Measure>
          </cac:FlashpointTemperature>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
