# Purchase Receipt: Velumi Trading to Lisavu Cotton Farm

*Example 29 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Purchase Receipt in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PURCHASE-RECEIPT-SCHEMA)*

Velumi Trading sells two of the imported benches in its shop in Selanu to the cotton farm, for the pickers' rest place; the farm pays with its Coralcard, and the till prints the card number with the first six and the last four digits.

[The XML file](29-PurchaseReceipt.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:purchase-receipt:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Purchase receipt". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:retail-sale:1.0**  
  The Trade Accord's process profile the document belongs to: retail sale, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VT-PR-26-0154**  
  The till's receipt number.
- `UUID` = **464955fd-c2fe-5d30-a020-fe67a7fc3e92**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-13**  
  The farm buys after the season's first cotton payments.
- `IssueTime` = **10:25:00+00:00**  
  Printed at the till; in the issuer's local time, with its offset from UTC (D27).
- `TransactionDate` = **2026-06-13**  
  The day of the sale.
- `TransactionTime` = **10:25:00**  
  The time of the sale.
- `Note` = **Loletali ninote nipive tofuta pehaka tavase vaputa.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): Printed on the receipt.
- `Note` = **Collected by the farm with its own trailer.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: Printed on the receipt.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the currency of the shop; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The registered office, as entered in the register.
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
- `Party/Contact/Name` = **Accounts receivable**  
  The party's accounts receivable desk: the desk for its role in this document (it is owed the payment); identity of Velumi Trading (world/parties.json).
- `Party/Contact/JobTitle` = **Credit controller**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 729 1859**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
- `Party/Contact/ElectronicMail` = **receivables@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/ID` = **85779006** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/Description` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  How to find the farm, which has no house number on a street. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/District` = **North coast**  
  The district of the island, used to find a farm off the main roads. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/AddressLine/Line` = **Sifatofu Natii / Plantation Road**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **North coast**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **Selanu / Port Wrenfield**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PostalAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PostalAddress/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LatitudeMinutesMeasure` = **56.40** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PostalAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PostalAddress/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LongitudeMinutesMeasure` = **1.20** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PostalAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PartyLegalEntity/RegistrationName` = **Lisavu Cotton Farm**  
  The name under which the party is registered, with its legal form; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Farm register of Lisavu; identity of Lisavu Cotton Farm (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/Contact/Name` = **Farm office**  
  The party's main desk, which handles this document; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/JobTitle` = **Farm manager**  
  The job of the person who answers at the desk; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Department` = **Management**  
  The department the desk belongs to; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 724 2544**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42544** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lisavu Cotton Farm (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Cash Register

Inside `CashRegister`:

- `ID` = **T1**  
  The shop's only till.

### Point of Sale Location

Inside `PointOfSaleLocation`:

- `Name` = **Velumi Trading, Reef Street, Selanu**  
  The shop.

### Payment

Inside `Payment`:

- `ID` = **VT-T1-26-0613-0012**  
  The till's number for the payment.
- `PaidAmount` = **578.000** (currencyID `XLC`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).
- `PaidDate` = **2026-06-13**  
  Paid at the till.
- `PaidTime` = **10:25:00**  
  At the time of the sale.
- `MerchantID` = **CORALCARD-M-0001859**  
  The shop's merchant number with the card scheme.
- `AuthorizationID` = **C30417**  
  The approval code of the card issuer, the Bank of Selanu.
- `PaymentTerminalID` = **PT-T1**  
  The card terminal at the till.
- `StatusCode` = **APPROVED** (listID `urn:ubl-examples:world:codelist:PaymentStatusCode`)  
  The payment was approved. The code is from the Trade Accord's payment status list: APPROVED = Payment approved.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **55** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 55: debit card. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 55 = Debit card.
- `CardAccount/PrimaryAccountNumberID` = **990351******7186**  
  The card number, masked as the till prints it: velumi trading's shop till prints the first six and the last four digits of a card number (PCI DSS allows at most the first six and the last four). The number itself starts with 9 and the numeric code of the issuer's country, as ISO/IEC 7812 provides for national use, so it is no real card's.
- `CardAccount/NetworkID` = **CORALCARD** (schemeID `urn:ubl-examples:world:codelist:CardSchemeCode`)  
  The card scheme the card runs on. The code is from the Trade Accord's payment card scheme list: CORALCARD = Coralcard. An identifier that holds a code names the code's list in its schemeID.
- `CardAccount/CardTypeCode` = **DEBIT** (listID `urn:ubl-examples:world:codelist:CardTypeCode`)  
  A debit card. The code is from the Trade Accord's payment card type list: DEBIT = Debit card.
- `CardAccount/IssuerID` = **BSELXLSL** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The card's issuer, Bank of Selanu, by its bank identifier.
- `CardAccount/CardChipCode` = **Chip** (listID `urn:oasis:names:specification:ubl:codelist:gc:ChipCode`)  
  Read from the chip. The code is from the world's copy of UBL's Chip list, with a listID: Chip.
- `CardAccount/ChipApplicationID` = **D9030000011010**  
  The chip application used: the card scheme's registered application provider identifier D903000001, from the national category D of ISO/IEC 7816-5 with the country code of the scheme, and the application's own code.
- `CardAccount/HolderName` = **LISAVU COTTON FARM**  
  The name on the card.
- `CardAccount/RoleCode` = **HOLDER** (listID `urn:ubl-examples:world:codelist:CardAccountRoleCode`)  
  Paid by the card holder. The code is from the Trade Accord's card account role list: HOLDER = Card holder.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **578.000** (currencyID `XLC`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **578.000** (currencyID `XLC`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **578.000** (currencyID `XLC`)  
  The same as the total without tax: Lisavu has no sales tax or value added tax, so no tax is due and the document has no tax section (D15).
- `PayableAmount` = **578.000** (currencyID `XLC`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Purchase Receipt Line

Inside `PurchaseReceiptLine`:

- `ID` = **1**  
  The line number.
- `Quantity` = **2** (unitCode `EA`)  
  Two benches for the pickers' rest place under the trees by the weighing shed.
- `LineExtensionAmount` = **578.000** (currencyID `XLC`)  
  Quantity times the price paid, before the sales tax.
- `Item/Description` = **Serra hiapi vusase lesama Velumi Trading's keniti, limana lesama Bayvarra, kifupa tivufo vesakehi.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language; item bench-serra-x of Velumi Trading (world/items.json).
- `Item/Description` = **The Serra park bench from Velumi Trading's stock, imported from Bayvarra, for island customers.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries; item bench-serra-x of Velumi Trading (world/items.json).
- `Item/Name` = **Hiapi vusase Serra 180** (languageID `qal`)  
  The item's name in Lisavan, the seller's language; item bench-serra-x of Velumi Trading (world/items.json).
- `Item/Name` = **Park bench Serra 180** (languageID `en-XL`)  
  The item's name in English, the working language between the countries; item bench-serra-x of Velumi Trading (world/items.json).
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Patike selemu lelala velute fepepa tikilau.** (languageID `qal`)  
  The maker's warranty in Lisavan, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Five years on the frame against corrosion.** (languageID `en-XL`)  
  The maker's warranty in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **VT-PB-180**  
  The seller's own item number; item bench-serra-x of Velumi Trading (world/items.json).
- `Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-serra.
- `Item/StandardItemIdentification/ID` = **9520610000012** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none (world/items.json).
- `Item/AdditionalItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The maker's own number for the item, its Codana item number, which travels along with the GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Price/PriceAmount` = **289** (currencyID `XLC`)  
  The seller's price per unit (world/items.json).
- `Price/TaxInclusivePriceAmount` = **289** (currencyID `XLC`)  
  The price the customer pays, with the 0 % sales tax.
- `Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PurchaseReceipt xmlns="urn:oasis:names:specification:ubl:schema:xsd:PurchaseReceipt-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:purchase-receipt:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:retail-sale:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VT-PR-26-0154</cbc:ID>
  <cbc:UUID>464955fd-c2fe-5d30-a020-fe67a7fc3e92</cbc:UUID>
  <cbc:IssueDate>2026-06-13</cbc:IssueDate>
  <cbc:IssueTime>10:25:00+00:00</cbc:IssueTime>
  <cbc:TransactionDate>2026-06-13</cbc:TransactionDate>
  <cbc:TransactionTime>10:25:00</cbc:TransactionTime>
  <cbc:Note languageID="qal">Loletali ninote nipive tofuta pehaka tavase vaputa.</cbc:Note>
  <cbc:Note languageID="en-XL">Collected by the farm with its own trailer.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
        <cac:RegistrationAddress>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
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
        <cbc:Name>Accounts receivable</cbc:Name>
        <cbc:JobTitle>Credit controller</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 3 729 1859</cbc:Telephone>
        <cbc:ElectronicMail>receivables@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">85779006</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Sifatofu Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Plantation Road</cbc:StreetName>
        <cbc:Description>Farm track off Plantation Road at kilometre 4, past the cotton fields.</cbc:Description>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:District>North coast</cbc:District>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:AddressLine>
          <cbc:Line>Sifatofu Natii / Plantation Road</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Farm track off Plantation Road at kilometre 4, past the cotton fields.</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>North coast</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Selanu / Port Wrenfield</cbc:Line>
        </cac:AddressLine>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">56.40</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">1.20</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lisavu Cotton Farm</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Farm office</cbc:Name>
        <cbc:JobTitle>Farm manager</cbc:JobTitle>
        <cbc:Department>Management</cbc:Department>
        <cbc:Telephone>+999 3 724 2544</cbc:Telephone>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42544</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:CashRegister>
    <cbc:ID>T1</cbc:ID>
  </cac:CashRegister>
  <cac:PointOfSaleLocation>
    <cbc:Name>Velumi Trading, Reef Street, Selanu</cbc:Name>
  </cac:PointOfSaleLocation>
  <cac:Payment>
    <cbc:ID>VT-T1-26-0613-0012</cbc:ID>
    <cbc:PaidAmount currencyID="XLC">578.000</cbc:PaidAmount>
    <cbc:PaidDate>2026-06-13</cbc:PaidDate>
    <cbc:PaidTime>10:25:00</cbc:PaidTime>
    <cbc:MerchantID>CORALCARD-M-0001859</cbc:MerchantID>
    <cbc:AuthorizationID>C30417</cbc:AuthorizationID>
    <cbc:PaymentTerminalID>PT-T1</cbc:PaymentTerminalID>
    <cbc:StatusCode listID="urn:ubl-examples:world:codelist:PaymentStatusCode">APPROVED</cbc:StatusCode>
  </cac:Payment>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">55</cbc:PaymentMeansCode>
    <cac:CardAccount>
      <cbc:PrimaryAccountNumberID>990351******7186</cbc:PrimaryAccountNumberID>
      <cbc:NetworkID schemeID="urn:ubl-examples:world:codelist:CardSchemeCode">CORALCARD</cbc:NetworkID>
      <cbc:CardTypeCode listID="urn:ubl-examples:world:codelist:CardTypeCode">DEBIT</cbc:CardTypeCode>
      <cbc:IssuerID schemeID="urn:ubl-examples:world:bank-identifier">BSELXLSL</cbc:IssuerID>
      <cbc:CardChipCode listID="urn:oasis:names:specification:ubl:codelist:gc:ChipCode">Chip</cbc:CardChipCode>
      <cbc:ChipApplicationID>D9030000011010</cbc:ChipApplicationID>
      <cbc:HolderName>LISAVU COTTON FARM</cbc:HolderName>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:CardAccountRoleCode">HOLDER</cbc:RoleCode>
    </cac:CardAccount>
  </cac:PaymentMeans>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">578.000</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">578.000</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">578.000</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XLC">578.000</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:PurchaseReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XLC">578.000</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description languageID="qal">Serra hiapi vusase lesama Velumi Trading's keniti, limana lesama Bayvarra, kifupa tivufo vesakehi.</cbc:Description>
      <cbc:Description languageID="en-XL">The Serra park bench from Velumi Trading's stock, imported from Bayvarra, for island customers.</cbc:Description>
      <cbc:Name languageID="qal">Hiapi vusase Serra 180</cbc:Name>
      <cbc:Name languageID="en-XL">Park bench Serra 180</cbc:Name>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:WarrantyInformation languageID="qal">Patike selemu lelala velute fepepa tikilau.</cbc:WarrantyInformation>
      <cbc:WarrantyInformation languageID="en-XL">Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:SellersItemIdentification>
        <cbc:ID>VT-PB-180</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9520610000012</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
      </cac:AdditionalItemIdentification>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">289</cbc:PriceAmount>
      <cbc:TaxInclusivePriceAmount currencyID="XLC">289</cbc:TaxInclusivePriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:PurchaseReceiptLine>
</PurchaseReceipt>
```
