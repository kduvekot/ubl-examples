# Invoice: Selanu Telecom to Velumi Trading

*Example 13 of the flow "Electricity, water and telecom (one utility in each country)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The telecom bill. The island has no sales tax or VAT, so no tax is due and the bill has no tax section.

[The XML file](13-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Invoice/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Billing". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **STL-TX-26-75183**  
  The collaboration this document belongs to: Selanu Telecom's bill for March to Velumi. Selanu Telecom started it and gave it this identifier, which every document of it repeats.
- `ID` = **STL-C-1077-2603**  
  The seller's invoice number.
- `UUID` = **0228817f-8a56-5781-a34c-99eedb2ee7ee**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The monthly bill, issued on the second working day of the next month.
- `IssueTime` = **11:19:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `DueDate` = **2026-04-23**  
  As the payment terms below count it: 21 days net from the bill.
- `InvoiceTypeCode` = **380** (listID `UN/EDIFACT EDED 1001`)  
  A commercial invoice, as UN/EDIFACT 1001 codes it. The code is from the world's copy of UN/EDIFACT 1001 Document name: 380 = Commercial invoice.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the seller's currency; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `AccountingCostCode` = **700**  
  The buyer's cost centre, quoted in its contract or booking, so the invoice is booked without asking.
- `AccountingCost` = **Telephone and data**  
  The cost centre in words.
- `LineCountNumeric` = **3**  
  The number of invoice lines, as a check on the transfer.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts that carry no language identifier: English, the working language between the countries; a seller from Urvania or the island also gives its notes in its own language. The code is from the world's copy of ISO 639 Language: en = English.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-03-01**  
  The month billed: March.
- `EndDate` = **2026-03-31**  
  Its last day.
- `DescriptionCode` = **MONTH** (listID `urn:ubl-examples:world:codelist:PeriodDescriptionCode`)  
  A monthly bill. The code is from the Trade Accord's period description list: MONTH = Calendar month.
- `Description` = **March 2026**  
  The period in words.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **STL-C-1077**  
  The customer's contract number with the utility.
- `Description` = **Supply contract**  
  What the number is.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Telecom gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The trading name; as Selanu Telecom gives it.
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: kopele.
- `Party/PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Telecom gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Telecom gives it.
- `Party/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Telecom gives it.
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. As Selanu Telecom gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; as Selanu Telecom gives it.
- `Party/PartyLegalEntity/CompanyID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Selanu Telecom gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); as Selanu Telecom gives it.
- `Party/Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Selanu Telecom gives it.
- `Party/Contact/Department` = **Business sales**  
  The department the desk belongs to; as Selanu Telecom gives it.
- `Party/Contact/Telephone` = **+999 3 727 3193**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Telecom gives it.
- `Party/Contact/ElectronicMail` = **billing@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu Telecom gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Selanu Telecom gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Telecom gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `Party/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; as Velumi Trading gives it.
- `Party/PartyLegalEntity/CompanyID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Velumi Trading gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Velumi Trading gives it.
- `Party/Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Party/Contact/Telephone` = **+999 3 729 5794**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `Party/Contact/ElectronicMail` = **payables@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Velumi Trading gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Velumi Trading gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Velumi Trading**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-04-23**  
  When the transfer must be credited.
- `PaymentChannelCode` = **RTGS** (listID `ISO 20022 ClearingChannel2Code`)  
  How the payment system clears and settles the transfer, as an ISO 20022 clearing channel. The code is from the world's copy of ISO 20022 ClearingChannel2Code: RTGS = RealTimeGrossSettlementSystem.
- `PaymentRailID` = **CORAL-NET**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF76STLC10772603**  
  What the payer writes in the transfer.
- `PaymentID` = **RF76STLC10772603** (schemeID `ISO 11649`)  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `PayeeFinancialAccount/ID` = **XL18BSEL0010004293889** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Selanu Telecom Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `PayeeFinancialAccount/BlockchainID` = **CORAL-NET-L1**  
  The account holds tokenised coral deposits on the Bank of Selanu's ledger, which Coral net settles on.
- `PayeeFinancialAccount/PaymentNote` = **Invoice STL-C-1077-2603**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **001** (schemeID `urn:ubl-examples:world:XL:bank-branch`)  
  The branch that keeps the account, by its national code: the branch number of a Lisavan bank (three digits). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSELXLSL** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BSEL, the country XL and the location SL; as Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Selanu**  
  The bank; as Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **23**  
  Building number of the postal address. As Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Bank of Selanu gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Payment Terms

Inside `PaymentTerms`:

- `ID` = **TA-UTIL**  
  The Trade Accord's term for utility bills.
- `PaymentMeansID` = **1**  
  The payment means these terms apply to: the credit transfer below.
- `Note` = **21 days net from the bill.**  
  The Trade Accord's term for utility bills (water, energy, telephone), the same in all three countries: due 21 days after the bill; a household with a direct-debit mandate is collected on that day.
- `PaymentDueDate` = **2026-04-23**  
  The day the amount is due, as the terms count it.
- `PenaltyInterestRate/InterestRatePercent` = **6**  
  The interest on late payment: the statutory rate, as the terms say nothing on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **ANN** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  A yearly rate. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: ANN = year.
- `PenaltyInterestRate/CalculationMethodCode` = **SIMPLE** (listID `urn:ubl-examples:world:codelist:InterestCalculationCode`)  
  Simple interest, per day late. The code is from the Trade Accord's interest calculation method list: SIMPLE = Simple interest.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Amount` = **6.354** (currencyID `XLC`)  
  5 % of the six subscriptions.
- `BaseAmount` = **127.080** (currencyID `XLC`)  
  The six subscriptions.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **146.224** (currencyID `XLC`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **139.870** (currencyID `XLC`)  
  The lines less the discount.
- `TaxInclusiveAmount` = **139.870** (currencyID `XLC`)  
  The same as the total without tax: Lisavu has no sales tax or value added tax, so no tax is due and the document has no tax section.
- `AllowanceTotalAmount` = **6.354** (currencyID `XLC`)  
  The bundle discount.
- `AllowanceTotalTaxInclusiveAmount` = **6.354** (currencyID `XLC`)  
  The same: no tax on the island.
- `PayableAmount` = **139.870** (currencyID `XLC`)  
  What the trader pays.

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **6** (unitCode `EA`)  
  Six business lines for the month.
- `LineExtensionAmount` = **127.080** (currencyID `XLC`)  
  6 × 21.18, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **PHON** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a telephone bill. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: PHON = TelephoneBill.
- `PurchaseReference/ID` = **STL-L-BUS6**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Six business lines**  
  Where it is.
- `Item/Description` = **Levise nikeile tofami titefe litile, vivukane tatata litile tofami lovofe.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `Item/Description` = **Business telephone and data line, subscription per line and month.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Levise nikeile litile** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `Item/Name` = **Business telephone line** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **STL-BL**  
  The seller's own item number; as Selanu Telecom describes the item.
- `Price/PriceAmount` = **21.18** (currencyID `XLC`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `ID` = **2**  
  The line number.
- `InvoicedQuantity` = **31** (unitCode `E34`)  
  Mobile data of the data pool beyond the subscriptions, used on the island.
- `LineExtensionAmount` = **13.144** (currencyID `XLC`)  
  31 × 0.424, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **PHON** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a telephone bill. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: PHON = TelephoneBill.
- `PurchaseReference/ID` = **STL-D-0042**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Mobile data pool**  
  Where it is.
- `Item/Description` = **Livule titefe lehimi vivukane, tatata menuti.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `Item/Description` = **Mobile data beyond the subscription, per gigabyte.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Livule titefe** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `Item/Name` = **Mobile data** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **STL-GB**  
  The seller's own item number; as Selanu Telecom describes the item.
- `Price/PriceAmount` = **0.424** (currencyID `XLC`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `E34`)  
  The price is per one unit.
- `ID` = **3**  
  The line number.
- `InvoicedQuantity` = **4** (unitCode `E34`)  
  Mobile data of the data pool used while roaming in Bayvarra.
- `LineExtensionAmount` = **6.000** (currencyID `XLC`)  
  4 × 1.5, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **PHON** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a telephone bill. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: PHON = TelephoneBill.
- `PurchaseReference/ID` = **STL-D-0042**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Mobile data pool, roaming in Bayvarra**  
  Where it is.
- `Item/Description` = **Livule titefe vimihi lelala vapiseva fivava pelahi, tatata menuti; Trade Accord sohone lelaha helate vamufe.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `Item/Description` = **Mobile data used on a partner's network abroad, per gigabyte; the Trade Accord has no roaming rule.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Livule titefe helate** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `Item/Name` = **Mobile data roaming** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **STL-GB-RX**  
  The seller's own item number; as Selanu Telecom describes the item.
- `Price/PriceAmount` = **1.5** (currencyID `XLC`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `E34`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>STL-TX-26-75183</cbc:ProfileExecutionID>
  <cbc:ID>STL-C-1077-2603</cbc:ID>
  <cbc:UUID>0228817f-8a56-5781-a34c-99eedb2ee7ee</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>11:19:00+00:00</cbc:IssueTime>
  <cbc:DueDate>2026-04-23</cbc:DueDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>700</cbc:AccountingCostCode>
  <cbc:AccountingCost>Telephone and data</cbc:AccountingCost>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-03-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
    <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:PeriodDescriptionCode">MONTH</cbc:DescriptionCode>
    <cbc:Description>March 2026</cbc:Description>
  </cac:InvoicePeriod>
  <cac:PurchaseReference>
    <cbc:ID>STL-C-1077</cbc:ID>
    <cbc:Description>Supply contract</cbc:Description>
  </cac:PurchaseReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
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
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Telecom Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:CompanyID>
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
        <cbc:Name>Billing</cbc:Name>
        <cbc:JobTitle>Billing officer</cbc:JobTitle>
        <cbc:Department>Business sales</cbc:Department>
        <cbc:Telephone>+999 3 727 3193</cbc:Telephone>
        <cbc:ElectronicMail>billing@selanutelecom.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
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
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Accounts payable</cbc:Name>
        <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
        <cbc:ElectronicMail>payables@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode listID="ISO 20022 ClearingChannel2Code">RTGS</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>CORAL-NET</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF76STLC10772603</cbc:InstructionNote>
    <cbc:PaymentID schemeID="ISO 11649">RF76STLC10772603</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL18BSEL0010004293889</cbc:ID>
      <cbc:Name>Selanu Telecom Ltd</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XLC</cbc:CurrencyCode>
      <cbc:BlockchainID>CORAL-NET-L1</cbc:BlockchainID>
      <cbc:PaymentNote>Invoice STL-C-1077-2603</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:bank-branch">001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">BSELXLSL</cbc:ID>
          <cbc:Name>Bank of Selanu</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
            <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
            <cbc:BuildingNumber>23</cbc:BuildingNumber>
            <cbc:CityName languageID="qal">Selanu</cbc:CityName>
            <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              <cbc:Name>Lisavu</cbc:Name>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
        <cac:Address>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:ID>TA-UTIL</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>21 days net from the bill.</cbc:Note>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>6</cbc:InterestRatePercent>
      <cbc:TimeBasisCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">ANN</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:InterestCalculationCode">SIMPLE</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
    <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
    <cbc:Amount currencyID="XLC">6.354</cbc:Amount>
    <cbc:BaseAmount currencyID="XLC">127.080</cbc:BaseAmount>
  </cac:AllowanceCharge>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">146.224</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">139.870</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">139.870</cbc:TaxInclusiveAmount>
    <cbc:AllowanceTotalAmount currencyID="XLC">6.354</cbc:AllowanceTotalAmount>
    <cbc:AllowanceTotalTaxInclusiveAmount currencyID="XLC">6.354</cbc:AllowanceTotalTaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XLC">139.870</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="EA">6</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">127.080</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">PHON</cbc:PaymentPurposeCode>
    <cac:PurchaseReference>
      <cbc:ID>STL-L-BUS6</cbc:ID>
      <cbc:Description>Six business lines</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description languageID="qal">Levise nikeile tofami titefe litile, vivukane tatata litile tofami lovofe.</cbc:Description>
      <cbc:Description languageID="en-XL">Business telephone and data line, subscription per line and month.</cbc:Description>
      <cbc:Name languageID="qal">Levise nikeile litile</cbc:Name>
      <cbc:Name languageID="en-XL">Business telephone line</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>STL-BL</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">21.18</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:InvoicedQuantity unitCode="E34">31</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">13.144</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">PHON</cbc:PaymentPurposeCode>
    <cac:PurchaseReference>
      <cbc:ID>STL-D-0042</cbc:ID>
      <cbc:Description>Mobile data pool</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description languageID="qal">Livule titefe lehimi vivukane, tatata menuti.</cbc:Description>
      <cbc:Description languageID="en-XL">Mobile data beyond the subscription, per gigabyte.</cbc:Description>
      <cbc:Name languageID="qal">Livule titefe</cbc:Name>
      <cbc:Name languageID="en-XL">Mobile data</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>STL-GB</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">0.424</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="E34">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>3</cbc:ID>
    <cbc:InvoicedQuantity unitCode="E34">4</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">6.000</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">PHON</cbc:PaymentPurposeCode>
    <cac:PurchaseReference>
      <cbc:ID>STL-D-0042</cbc:ID>
      <cbc:Description>Mobile data pool, roaming in Bayvarra</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description languageID="qal">Livule titefe vimihi lelala vapiseva fivava pelahi, tatata menuti; Trade Accord sohone lelaha helate vamufe.</cbc:Description>
      <cbc:Description languageID="en-XL">Mobile data used on a partner's network abroad, per gigabyte; the Trade Accord has no roaming rule.</cbc:Description>
      <cbc:Name languageID="qal">Livule titefe helate</cbc:Name>
      <cbc:Name languageID="en-XL">Mobile data roaming</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>STL-GB-RX</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">1.5</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="E34">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
