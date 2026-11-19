# Purchase Receipt: Brightmarket Stores to Robin Ashdale

*Example 21 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Purchase Receipt in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PURCHASE-RECEIPT-SCHEMA)*

A consumer buys in the shop and gets a receipt.

[The XML file](21-PurchaseReceipt.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:purchase-receipt:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Purchase receipt". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:retail-sale:1.0**  
  The Trade Accord's process profile the document belongs to: retail sale, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **RETAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BS-PR-26-0240**  
  The till's receipt number.
- `UUID` = **bcdeb9a7-e515-519a-b488-de52151e844f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-15**  
  A consumer buys a bench during the promotion week.
- `IssueTime` = **11:42:00-01:00**  
  Printed at the till; in the issuer's local time, with its offset from UTC (D27).
- `TransactionDate` = **2026-05-15**  
  The day of the sale.
- `TransactionTime` = **11:42:00**  
  The time of the sale.
- `PurchaseDate` = **2026-05-15**  
  The day the customer bought.
- `PurchaseTime` = **11:42:00**  
  And when.
- `Note` = **Home delivery booked for Saturday.**  
  Printed on the receipt.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the currency of the shop; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **BM-LOYAL-0088127**  
  The customer's loyalty card.
- `Description` = **Loyalty card**  
  What the number is.

### Sales Document Reference

Inside `SalesDocumentReference`:

- `ID` = **BM-DEL-26-0515-07**  
  The store's home delivery order, booked with the sale on 15 May (retail/21#F7).
- `DocumentType` = **Home delivery order**  
  What the document is: the store's own delivery booking, outside the examples.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **VI-WARRANTY-B180**  
  The maker's warranty card.
- `DocumentType` = **Warranty card**  
  The kind of document referred to, the maker's warranty card of the bench, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Signature

Inside `Signature`:

- `ID` = **BM-SIG-POS-G2**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `Party/TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
- `Party/PartyTaxScheme/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered for state sales tax; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1231233** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Brightmarket Stores (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered, with its legal form; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **CORP** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: CORP = Corporation (public).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Corporation (public)** (languageID `en-XB`)  
  The name of code CORP in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Party/Contact/Name` = **Accounts receivable**  
  The party's accounts receivable desk: the desk for its role in this document (it is owed the payment); identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/JobTitle` = **Credit controller**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 4609 7100**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/ElectronicMail` = **receivables@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

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
- `Party/Person/FinancialAccount/ID` = **XB64BLUM38010007251840** (schemeID `urn:ubl-examples:world:account`)  
  The consumer's own account, from which the bills are paid. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `Party/Person/FinancialAccount/Name` = **Robin Ashdale**  
  The account holder, as the bank knows it.
- `Party/Person/FinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `Party/Person/FinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `Party/Person/FinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/ID` = **380100** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Name` = **Main branch, Exchange Street**  
  The branch's name.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BLUM, the country XB and the location LX; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  Street of the postal address. identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Building number of the postal address. identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bank of Lumeport (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Person/FinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Cashier Contact

Inside `CashierContact`:

- `Name` = **Mira**  
  The cashier, by first name, as printed.

### Cash Register

Inside `CashRegister`:

- `ID` = **G2**  
  The till.
- `SerialNumberID` = **BM-POS-G2-2219**  
  The till's serial number, as the tax rules require on a receipt.

### Point of Sale Location

Inside `PointOfSaleLocation`:

- `Description` = **Home and garden department, ground floor**  
  Where in the shop.
- `Name` = **Brightmarket Stores, Lumeport**  
  The shop.

### Point of Sale Contact

Inside `PointOfSaleContact`:

- `Telephone` = **+999 2 38 4609 7100**  
  The shop's number, for questions about the purchase.

### Delivery

Inside `Delivery`:

- `DeliveryAddress/ID` = **LUM-ADR-934215** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `DeliveryAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `DeliveryAddress/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `DeliveryAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `DeliveryAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `DeliveryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `DeliveryAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `RequestedDeliveryPeriod/StartDate` = **2026-05-16**  
  Saturday, the day the note names: the store delivers Monday to Saturday.
- `RequestedDeliveryPeriod/StartTime` = **09:00:00**  
  Morning.
- `RequestedDeliveryPeriod/EndTime` = **12:00:00**  
  Until noon.
- `CarrierParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `CarrierParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Payment

Inside `Payment`:

- `ID` = **BM-G2-26-0515-0047**  
  The till's number for the payment, with the day of the sale (retail/21#F7).
- `PaidAmount` = **744.54** (currencyID `XBL`)  
  Paid by card.
- `PaidDate` = **2026-05-15**  
  Paid at the till.
- `PaidTime` = **11:42:00**  
  At the time of the sale.
- `MerchantID` = **LUMECARD-M-0026118**  
  The store's merchant number with the card scheme.
- `AuthorizationID` = **A71520**  
  The approval code of the card issuer.
- `TransactionID` = **TX-26-0515-773104**  
  The card transaction, with its day.
- `PaymentTerminalID` = **PT-G2**  
  The card terminal at the till.
- `StatusCode` = **APPROVED** (listID `urn:ubl-examples:world:codelist:PaymentStatusCode`)  
  The payment was approved. The code is from the Trade Accord's payment status list: APPROVED = Payment approved.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **55** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 55: debit card. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 55 = Debit card.
- `CardAccount/PrimaryAccountNumberID` = **************4417**  
  The card number, masked as the till prints it: the store's tills print only the last four digits of a card number (PCI DSS allows at most the first six and the last four). The number itself starts with 9 and the numeric code of the issuer's country, as ISO/IEC 7812 provides for national use, so it is no real card's.
- `CardAccount/NetworkID` = **LUMECARD** (schemeID `urn:ubl-examples:world:codelist:CardSchemeCode`)  
  The card scheme the card runs on. The code is from the Trade Accord's payment card scheme list: LUMECARD = Lumecard. An identifier that holds a code names the code's list in its schemeID.
- `CardAccount/CardTypeCode` = **DEBIT** (listID `urn:ubl-examples:world:codelist:CardTypeCode`)  
  A debit card. The code is from the Trade Accord's payment card type list: DEBIT = Debit card.
- `CardAccount/IssuerID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The card's issuer, Bank of Lumeport, by its bank identifier.
- `CardAccount/IssueNumberID` = **01**  
  The card's issue number: the first card of this account.
- `CardAccount/CardChipCode` = **Chip** (listID `urn:oasis:names:specification:ubl:codelist:gc:ChipCode`)  
  Read from the chip. The code is from the world's copy of UBL's Chip list, with a listID: Chip.
- `CardAccount/ChipApplicationID` = **D9020000011010**  
  The chip application used: the card scheme's registered application provider identifier D902000001, from the national category D of ISO/IEC 7816-5 with the country code of the scheme, and the application's own code.
- `CardAccount/HolderName` = **R ASHDALE**  
  The name on the card.
- `CardAccount/RoleCode` = **HOLDER** (listID `urn:ubl-examples:world:codelist:CardAccountRoleCode`)  
  Paid by the card holder. The code is from the Trade Accord's card account role list: HOLDER = Card holder.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **true**  
  A charge.
- `AllowanceChargeReasonCode` = **DL** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: DL = Delivery.
- `AllowanceChargeReason` = **Home delivery**  
  Delivered on Saturday, as booked.
- `Amount` = **25.00** (currencyID `XBL`)  
  The store's flat delivery charge.
- `TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **45.44** (currencyID `XBL`)  
  6.5 % state sales tax on the bench and the delivery.
- `TaxSubtotal/TaxableAmount` = **699.10** (currencyID `XBL`)  
  The bench and the home delivery.
- `TaxSubtotal/TaxAmount` = **45.44** (currencyID `XBL`)  
  6.5 %.
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **674.10** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **699.10** (currencyID `XBL`)  
  Before the sales tax.
- `TaxInclusiveAmount` = **744.54** (currencyID `XBL`)  
  With the sales tax.
- `ChargeTotalAmount` = **25.00** (currencyID `XBL`)  
  The home delivery.
- `PayableAmount` = **744.54** (currencyID `XBL`)  
  Paid by card: no cash rounding.

### Purchase Receipt Line

Inside `PurchaseReceiptLine`:

- `ID` = **1**  
  The line number.
- `UUID` = **ea701e0e-2453-5802-8bbd-0356ea20503d**  
  A universally unique identifier of the line, derived from the document and the line number.
- `Note` = **Promotion price.**  
  As printed.
- `Quantity` = **1** (unitCode `EA`)  
  One bench.
- `LineExtensionAmount` = **674.10** (currencyID `XBL`)  
  Quantity times the price paid, before the sales tax.
- `TaxInclusiveLineExtensionAmount` = **717.92** (currencyID `XBL`)  
  With the 6.5 % sales tax.
- `PurchaseReference/ID` = **VI-SF-01298**  
  The serial number of the bench's frame, for the warranty: the bench is one of the store's delivery from the March lot, whose frames were cast with it (the production record, D21).
- `PurchaseReference/Description` = **Frame serial number**  
  What the number is.
- `TaxTotal/TaxAmount` = **43.82** (currencyID `XBL`)  
  The sales tax of the line.
- `Item/Description` = **The Serra park bench in the store's home and garden department; the state sales tax is added at the till.**  
  The seller's description; item bench-serra-r of Brightmarket Stores (world/items.json).
- `Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra-r of Brightmarket Stores (world/items.json).
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **BM-551210**  
  The seller's own item number; item bench-serra-r of Brightmarket Stores (world/items.json).
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
- `Item/AdditionalItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The maker's number for the item in its globally unique form under ISO/IEC 15459 (KXU and the company number Codana gave Valdara Industries), which travels along with the GTIN, as an importer may carry it; item bench-serra of Valdara Industries (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **674.1** (currencyID `XBL`)  
  The shelf price of 749.0 less the promotion discount.
- `Price/TaxInclusivePriceAmount` = **717.92** (currencyID `XBL`)  
  The price the customer pays, with the 6.5 % sales tax.
- `Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `Price/PriceChangeReason` = **Reopening of the home and garden department**  
  Why the price differs from the shelf price.
- `Price/ValidityPeriod/StartDate` = **2026-05-11**  
  The first day of the promotion.
- `Price/ValidityPeriod/EndDate` = **2026-05-24**  
  The last day of the promotion.
- `Price/AllowanceCharge/ChargeIndicator` = **false**  
  A discount, not a charge.
- `Price/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it: the promotion is a discount on the price. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Price/AllowanceCharge/AllowanceChargeReason` = **Reopening of the home and garden department**  
  The promotion, as the till prints it.
- `Price/AllowanceCharge/MultiplierFactorNumeric` = **0.1**  
  The discount rate.
- `Price/AllowanceCharge/Amount` = **74.90** (currencyID `XBL`)  
  The discount per unit, deducted from the shelf price.
- `Price/AllowanceCharge/BaseAmount` = **749.00** (currencyID `XBL`)  
  The shelf price the discount is taken from.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PurchaseReceipt xmlns="urn:oasis:names:specification:ubl:schema:xsd:PurchaseReceipt-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:purchase-receipt:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:retail-sale:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>RETAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-PR-26-0240</cbc:ID>
  <cbc:UUID>bcdeb9a7-e515-519a-b488-de52151e844f</cbc:UUID>
  <cbc:IssueDate>2026-05-15</cbc:IssueDate>
  <cbc:IssueTime>11:42:00-01:00</cbc:IssueTime>
  <cbc:TransactionDate>2026-05-15</cbc:TransactionDate>
  <cbc:TransactionTime>11:42:00</cbc:TransactionTime>
  <cbc:PurchaseDate>2026-05-15</cbc:PurchaseDate>
  <cbc:PurchaseTime>11:42:00</cbc:PurchaseTime>
  <cbc:Note>Home delivery booked for Saturday.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cac:PurchaseReference>
    <cbc:ID>BM-LOYAL-0088127</cbc:ID>
    <cbc:Description>Loyalty card</cbc:Description>
  </cac:PurchaseReference>
  <cac:SalesDocumentReference>
    <cbc:ID>BM-DEL-26-0515-07</cbc:ID>
    <cbc:DocumentType>Home delivery order</cbc:DocumentType>
  </cac:SalesDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-WARRANTY-B180</cbc:ID>
    <cbc:DocumentType>Warranty card</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>BM-SIG-POS-G2</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:AccountingSupplierParty>
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
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1231233</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">CORP</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="en-XB">Corporation (public)</cbc:CompanyLegalForm>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
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
        <cbc:Name>Accounts receivable</cbc:Name>
        <cbc:JobTitle>Credit controller</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
        <cbc:ElectronicMail>receivables@brightmarket.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
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
        <cac:FinancialAccount>
          <cbc:ID schemeID="urn:ubl-examples:world:account">XB64BLUM38010007251840</cbc:ID>
          <cbc:Name>Robin Ashdale</cbc:Name>
          <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
          <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:FinancialInstitutionBranch>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:bank-branch">380100</cbc:ID>
            <cbc:Name>Main branch, Exchange Street</cbc:Name>
            <cac:FinancialInstitution>
              <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">BLUMXBLX</cbc:ID>
              <cbc:Name>Bank of Lumeport</cbc:Name>
              <cac:Address>
                <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
                <cbc:StreetName>Exchange Street</cbc:StreetName>
                <cbc:BuildingNumber>48</cbc:BuildingNumber>
                <cbc:CityName>Lumeport</cbc:CityName>
                <cbc:PostalZone>38523</cbc:PostalZone>
                <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
                <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
                  <cbc:Name>Bayvarra</cbc:Name>
                </cac:Country>
              </cac:Address>
            </cac:FinancialInstitution>
            <cac:Address>
              <cbc:CityName>Lumeport</cbc:CityName>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:FinancialInstitutionBranch>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:FinancialAccount>
      </cac:Person>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:CashierContact>
    <cbc:Name>Mira</cbc:Name>
  </cac:CashierContact>
  <cac:CashRegister>
    <cbc:ID>G2</cbc:ID>
    <cbc:SerialNumberID>BM-POS-G2-2219</cbc:SerialNumberID>
  </cac:CashRegister>
  <cac:PointOfSaleLocation>
    <cbc:Description>Home and garden department, ground floor</cbc:Description>
    <cbc:Name>Brightmarket Stores, Lumeport</cbc:Name>
  </cac:PointOfSaleLocation>
  <cac:PointOfSaleContact>
    <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
  </cac:PointOfSaleContact>
  <cac:Delivery>
    <cac:DeliveryAddress>
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
    </cac:DeliveryAddress>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-05-16</cbc:StartDate>
      <cbc:StartTime>09:00:00</cbc:StartTime>
      <cbc:EndTime>12:00:00</cbc:EndTime>
    </cac:RequestedDeliveryPeriod>
    <cac:CarrierParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:CarrierParty>
  </cac:Delivery>
  <cac:Payment>
    <cbc:ID>BM-G2-26-0515-0047</cbc:ID>
    <cbc:PaidAmount currencyID="XBL">744.54</cbc:PaidAmount>
    <cbc:PaidDate>2026-05-15</cbc:PaidDate>
    <cbc:PaidTime>11:42:00</cbc:PaidTime>
    <cbc:MerchantID>LUMECARD-M-0026118</cbc:MerchantID>
    <cbc:AuthorizationID>A71520</cbc:AuthorizationID>
    <cbc:TransactionID>TX-26-0515-773104</cbc:TransactionID>
    <cbc:PaymentTerminalID>PT-G2</cbc:PaymentTerminalID>
    <cbc:StatusCode listID="urn:ubl-examples:world:codelist:PaymentStatusCode">APPROVED</cbc:StatusCode>
  </cac:Payment>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">55</cbc:PaymentMeansCode>
    <cac:CardAccount>
      <cbc:PrimaryAccountNumberID>************4417</cbc:PrimaryAccountNumberID>
      <cbc:NetworkID schemeID="urn:ubl-examples:world:codelist:CardSchemeCode">LUMECARD</cbc:NetworkID>
      <cbc:CardTypeCode listID="urn:ubl-examples:world:codelist:CardTypeCode">DEBIT</cbc:CardTypeCode>
      <cbc:IssuerID schemeID="urn:ubl-examples:world:bank-identifier">BLUMXBLX</cbc:IssuerID>
      <cbc:IssueNumberID>01</cbc:IssueNumberID>
      <cbc:CardChipCode listID="urn:oasis:names:specification:ubl:codelist:gc:ChipCode">Chip</cbc:CardChipCode>
      <cbc:ChipApplicationID>D9020000011010</cbc:ChipApplicationID>
      <cbc:HolderName>R ASHDALE</cbc:HolderName>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:CardAccountRoleCode">HOLDER</cbc:RoleCode>
    </cac:CardAccount>
  </cac:PaymentMeans>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">DL</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Home delivery</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XBL">25.00</cbc:Amount>
    <cac:TaxCategory>
      <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
      <cbc:Percent>6.5</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:AllowanceCharge>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">45.44</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">699.10</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">45.44</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">674.10</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">699.10</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">744.54</cbc:TaxInclusiveAmount>
    <cbc:ChargeTotalAmount currencyID="XBL">25.00</cbc:ChargeTotalAmount>
    <cbc:PayableAmount currencyID="XBL">744.54</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:PurchaseReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:UUID>ea701e0e-2453-5802-8bbd-0356ea20503d</cbc:UUID>
    <cbc:Note>Promotion price.</cbc:Note>
    <cbc:Quantity unitCode="EA">1</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XBL">674.10</cbc:LineExtensionAmount>
    <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">717.92</cbc:TaxInclusiveLineExtensionAmount>
    <cac:PurchaseReference>
      <cbc:ID>VI-SF-01298</cbc:ID>
      <cbc:Description>Frame serial number</cbc:Description>
    </cac:PurchaseReference>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XBL">43.82</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:Item>
      <cbc:Description>The Serra park bench in the store's home and garden department; the state sales tax is added at the till.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:SellersItemIdentification>
        <cbc:ID>BM-551210</cbc:ID>
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
        <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
      </cac:AdditionalItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">674.1</cbc:PriceAmount>
      <cbc:TaxInclusivePriceAmount currencyID="XBL">717.92</cbc:TaxInclusivePriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      <cbc:PriceChangeReason>Reopening of the home and garden department</cbc:PriceChangeReason>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-05-11</cbc:StartDate>
        <cbc:EndDate>2026-05-24</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Reopening of the home and garden department</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="XBL">74.90</cbc:Amount>
        <cbc:BaseAmount currencyID="XBL">749.00</cbc:BaseAmount>
      </cac:AllowanceCharge>
    </cac:Price>
  </cac:PurchaseReceiptLine>
</PurchaseReceipt>
```
