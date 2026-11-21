# Invoice: Coastal State Water Company to Robin Ashdale

*Example 9 of the flow "Electricity, water and telecom (one utility in each country)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The household's settlement bill for the account year: water (exempt), the city's levy (outside the tax), district heat and its cooling correction (with the state's sales tax), less the twelve payments on account; the balance is collected by direct debit 21 days later.

[The XML file](09-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Invoice/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Billing". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9924052627**  
  The collaboration this document belongs to: the water company's annual account of the household. Coastal State Water Company started it and gave it this identifier, which every document of it repeats.
- `ID` = **CSW-C-311790-2603**  
  The seller's invoice number.
- `UUID` = **4d48b45e-73c0-5476-98a9-69e873037095**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The settlement bill of the household's account year, issued with the annual statement.
- `IssueTime` = **14:51:00-01:00**  
  Issued a few minutes before the document that cites it, in the sender's local time, with its offset from UTC.
- `DueDate` = **2026-04-23**  
  As the payment terms below count it: 21 days net from the bill.
- `InvoiceTypeCode` = **380** (listID `UN/EDIFACT EDED 1001`)  
  A commercial invoice, as UN/EDIFACT 1001 codes it. The code is from the world's copy of UN/EDIFACT 1001 Document name: 380 = Commercial invoice.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **4**  
  The number of lines: 3 invoice line(s) and one collection line for the city's levy; the amount payable includes both.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts that carry no language identifier: English, the working language between the countries; a seller from Urvania or the island also gives its notes in its own language. The code is from the world's copy of ISO 639 Language: en = English.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2025-04-01**  
  The household's account year: from April.
- `EndDate` = **2026-03-31**  
  To the annual reading at the end of March.
- `Description` = **Account year April 2025 to March 2026**  
  The period in words.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **CSW-C-311790**  
  The customer's contract number with the utility.
- `Description` = **Supply contract**  
  What the number is.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Coastal State Water Company**  
  The trading name; as Coastal State Water Company gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-782593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Coastal State Water Company gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. As Coastal State Water Company gives it.
- `Party/PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. As Coastal State Water Company gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Coastal State Water Company gives it.
- `Party/PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). As Coastal State Water Company gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Coastal State Water Company gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered for state sales tax; as Coastal State Water Company gives it.
- `Party/PartyTaxScheme/CompanyID` = **CO-1236576** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); as Coastal State Water Company gives it. The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
- `Party/PartyLegalEntity/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered, with its legal form; as Coastal State Water Company gives it.
- `Party/PartyLegalEntity/CompanyID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SOC** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: SOC = State-owned company limited by shares.
- `Party/PartyLegalEntity/CompanyLegalForm` = **State-owned company limited by shares** (languageID `en-XB`)  
  The name of code SOC in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); as Coastal State Water Company gives it.
- `Party/Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Coastal State Water Company gives it.
- `Party/Contact/Department` = **Customer service**  
  The department the desk belongs to; as Coastal State Water Company gives it.
- `Party/Contact/Telephone` = **+999 2 38 9310 7518**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Coastal State Water Company gives it.
- `Party/Contact/ElectronicMail` = **billing@coastalwater.example**  
  The contact's e-mail address; as Coastal State Water Company gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Coastal State Water Company gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyName/Name` = **Robin Ashdale**  
  The trading name; as Robin Ashdale gives it.
- `Party/PostalAddress/ID` = **LUM-ADR-934215** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Robin Ashdale gives it.
- `Party/PostalAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. As Robin Ashdale gives it.
- `Party/PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. As Robin Ashdale gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Robin Ashdale gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Robin Ashdale gives it.
- `Party/PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). As Robin Ashdale gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Robin Ashdale gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Person/FirstName` = **Robin**  
  The consumer's first name; as Robin Ashdale gives it.
- `Party/Person/FamilyName` = **Ashdale**  
  The consumer's family name; as Robin Ashdale gives it.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The only way to pay.
- `PaymentMeansCode` = **49** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 49: direct debit. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 49 = Direct debit.
- `PaymentDueDate` = **2026-04-23**  
  The day the amount will be collected.
- `PaymentID` = **RF13CSWC3117902603** (schemeID `ISO 11649`)  
  The reference on the household's bank statement. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `PayeeFinancialAccount/ID` = **XB21BLUM38010004189160** (schemeID `urn:ubl-examples:world:account`)  
  The water company's account the collection goes to. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Coastal State Water Company Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **380100** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch, Exchange Street**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BLUM, the country XB and the location LX; as Bank of Lumeport gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; as Bank of Lumeport gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  Street of the postal address. As Bank of Lumeport gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Building number of the postal address. As Bank of Lumeport gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bank of Lumeport gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). As Bank of Lumeport gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bank of Lumeport gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PaymentMandate/ID` = **CSW-DD-2024-08812**  
  The mandate the household signed for the water company.
- `PaymentMandate/MandateTypeCode` = **RCUR** (listID `ISO 20022 SequenceType3Code`)  
  A mandate for repeated collections. The code is from the world's copy of ISO 20022 SequenceType3Code: RCUR = Recurring.
- `PaymentMandate/MaximumPaidAmount` = **150.00** (currencyID `XBL`)  
  The most the company may collect at a time.
- `PaymentMandate/SignatureID` = **SIG-CSW-DD-2024-08812**  
  The reference of the signature on the mandate.
- `PaymentMandate/PayerFinancialAccount/ID` = **XB64BLUM38010007251840** (schemeID `urn:ubl-examples:world:account`)  
  The household's account the bill is collected from. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PaymentMandate/PayerFinancialAccount/Name` = **Robin Ashdale**  
  The account holder, as the bank knows it.
- `PaymentMandate/PayerFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PaymentMandate/PayerFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PaymentMandate/PayerFinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/ID` = **380100** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch, Exchange Street**  
  The branch's name.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BLUM, the country XB and the location LX; as Bank of Lumeport gives it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; as Bank of Lumeport gives it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  Street of the postal address. As Bank of Lumeport gives it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Building number of the postal address. As Bank of Lumeport gives it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bank of Lumeport gives it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). As Bank of Lumeport gives it.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bank of Lumeport gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `PaymentMandate/PayerFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PaymentMandate/PayerFinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PaymentMandate/ValidityPeriod/StartDate` = **2024-09-02**  
  Signed when the household moved in.
- `PaymentMandate/PaymentReversalPeriod/DurationMeasure` = **8** (unitCode `WEE`)  
  The household can reverse a collection within eight weeks.
- `PaymentMandate/Clause/ID` = **CSW-DD-T3**  
  The clause of the mandate on notice.
- `PaymentMandate/Clause/Content` = **The company announces each collection at least five days before.**  
  What the clause says.

### Payment Terms

Inside `PaymentTerms`:

- `ID` = **TA-UTIL**  
  The Trade Accord's term for utility bills.
- `PaymentMeansID` = **1**  
  The payment means these terms apply to: the credit transfer below.
- `Note` = **21 days net from the bill. Collected by direct debit on that day.**  
  The Trade Accord's utility term, and how the household pays: by the direct debit of its mandate.
- `PaymentDueDate` = **2026-04-23**  
  The day the amount is due, as the terms count it.
- `PenaltyInterestRate/InterestRatePercent` = **7**  
  The interest on late payment: the statutory rate, as the terms say nothing on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **ANN** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  A yearly rate. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: ANN = year.
- `PenaltyInterestRate/CalculationMethodCode` = **SIMPLE** (listID `urn:ubl-examples:world:codelist:InterestCalculationCode`)  
  Simple interest, per day late. The code is from the Trade Accord's interest calculation method list: SIMPLE = Simple interest.

### Prepaid Payment

Inside `PrepaidPayment`:

- `ID` = **CSW-OA-097315-2526**  
  The household's payments on account of the account year.
- `PaidAmount` = **1008.00** (currencyID `XBL`)  
  12 × 84.
- `PaidDate` = **2026-03-02**  
  The last of them, on the first working day of March.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **41.40** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **399.50** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Drinking water is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxableAmount` = **636.90** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **41.40** (currencyID `XBL`)  
  6.5 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **1036.40** (currencyID `XBL`)  
  The sum of the bill's own lines; the levy collected for the city is added to the amount payable only.
- `TaxExclusiveAmount` = **1036.40** (currencyID `XBL`)  
  The bill's own lines without tax; the levy collected for the city is not part of it.
- `TaxInclusiveAmount` = **1077.80** (currencyID `XBL`)  
  The bill's own lines with their tax; the levy collected for the city is not part of it.
- `PrepaidAmount` = **1008.00** (currencyID `XBL`)  
  The twelve payments on account of 84 lume collected from April 2025 to March 2026.
- `PayableAmount` = **141.20** (currencyID `XBL`)  
  What is to be paid: the bill's own lines with their tax, less what was prepaid, plus the levy collected for the city.

### Collection Invoice Line

Inside `CollectionInvoiceLine`:

- `ID` = **2**  
  The line number.
- `Note` = **Collected for the city of Lumeport and paid on to it.**  
  Why the water company bills it.
- `InvoicedQuantity` = **170** (unitCode `MTQ`)  
  The household's water use, on which the city charges its levy.
- `LineExtensionAmount` = **71.40** (currencyID `XBL`)  
  170 × 0.42, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **WTER** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a water bill. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: WTER = WaterBill.
- `InvoicePeriod/StartDate` = **2025-04-01**  
  The household's account year: from April.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  To the annual reading at the end of March.
- `InvoicePeriod/Description` = **Account year April 2025 to March 2026**  
  The period in words.
- `CollectedForParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `CollectedForParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Description` = **The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.**  
  The seller's description.
- `Item/Name` = **Sewage levy of the city of Lumeport**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **CSW-LEVY**  
  The seller's own item number; as Coastal State Water Company describes the item.
- `Item/ClassifiedTaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O, without a rate). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **LEVY** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: LEVY = Collected for a public body, outside the scope of the state sales tax.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Collected for a public body, outside the scope of the state sales tax**  
  The name of code LEVY in Bayvarra's national sales tax exemption reason list.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **0.42** (currencyID `XBL`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **170** (unitCode `MTQ`)  
  The household's water in the account year, from the annual readings.
- `LineExtensionAmount` = **399.50** (currencyID `XBL`)  
  170 × 2.35, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **WTER** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a water bill. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: WTER = WaterBill.
- `InvoicePeriod/StartDate` = **2025-04-01**  
  The household's account year: from April.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  To the annual reading at the end of March.
- `InvoicePeriod/Description` = **Account year April 2025 to March 2026**  
  The period in words.
- `PurchaseReference/ID` = **CSW-W-71844**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Gull Lane 57, water**  
  Where it is.
- `Item/Description` = **Drinking water supply, per cubic metre.**  
  The seller's description.
- `Item/Name` = **Drinking water**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **CW-M3**  
  The seller's own item number; as Coastal State Water Company describes the item.
- `Item/ClassifiedTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Drinking water is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **2.35** (currencyID `XBL`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.
- `ID` = **3**  
  The line number.
- `InvoicedQuantity` = **6.6** (unitCode `MWH`)  
  The flat's district heat in the account year, from the heat meter.
- `LineExtensionAmount` = **610.50** (currencyID `XBL`)  
  6.6 × 92.5, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **UBIL** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a utility bill, the district heat. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: UBIL = Utilities.
- `InvoicePeriod/StartDate` = **2025-04-01**  
  The household's account year: from April.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  To the annual reading at the end of March.
- `InvoicePeriod/Description` = **Account year April 2025 to March 2026**  
  The period in words.
- `PurchaseReference/ID` = **CSW-H-71844**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Gull Lane 57, district heat**  
  Where it is.
- `Item/Description` = **Heat from Lumeport's district heating network, per megawatt hour at the flat's heat meter.**  
  The seller's description.
- `Item/Name` = **District heat**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **CSW-HEAT**  
  The seller's own item number; as Coastal State Water Company describes the item.
- `Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **92.5** (currencyID `XBL`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `MWH`)  
  The price is per one unit.
- `ID` = **4**  
  The line number.
- `InvoicedQuantity` = **6.6** (unitCode `MWH`)  
  The cooling correction on the year's heat, per MWh as its definition says.
- `LineExtensionAmount` = **26.40** (currencyID `XBL`)  
  6.6 × 4.00, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **UBIL** (listID `ISO 20022 ExternalPurpose1Code`)  
  What the payment of this line is for, as an ISO 20022 purpose: a utility bill, the district heat. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: UBIL = Utilities.
- `InvoicePeriod/StartDate` = **2025-04-01**  
  The household's account year: from April.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  To the annual reading at the end of March.
- `InvoicePeriod/Description` = **Account year April 2025 to March 2026**  
  The period in words.
- `PurchaseReference/ID` = **CSW-H-71844**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Gull Lane 57, district heat**  
  Where it is.
- `Item/Description` = **The charge for return water that comes back warmer than the network's standard, per megawatt hour of heat and degree short of the standard cooling.**  
  The seller's description.
- `Item/Name` = **District heating cooling correction**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **CSW-COOL**  
  The seller's own item number; as Coastal State Water Company describes the item.
- `Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **4** (currencyID `XBL`)  
  4 degrees short of the network's standard cooling at 1.00 per MWh and degree.
- `Price/BaseQuantity` = **1** (unitCode `MWH`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9924052627</cbc:ProfileExecutionID>
  <cbc:ID>CSW-C-311790-2603</cbc:ID>
  <cbc:UUID>4d48b45e-73c0-5476-98a9-69e873037095</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>14:51:00-01:00</cbc:IssueTime>
  <cbc:DueDate>2026-04-23</cbc:DueDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>4</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2025-04-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
    <cbc:Description>Account year April 2025 to March 2026</cbc:Description>
  </cac:InvoicePeriod>
  <cac:PurchaseReference>
    <cbc:ID>CSW-C-311790</cbc:ID>
    <cbc:Description>Supply contract</cbc:Description>
  </cac:PurchaseReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-782593</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Reservoir Road</cbc:StreetName>
        <cbc:BuildingNumber>51</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38500</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1236576</cbc:CompanyID>
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
        <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">SOC</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="en-XB">State-owned company limited by shares</cbc:CompanyLegalForm>
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
        <cbc:Name>Billing</cbc:Name>
        <cbc:JobTitle>Billing officer</cbc:JobTitle>
        <cbc:Department>Customer service</cbc:Department>
        <cbc:Telephone>+999 2 38 9310 7518</cbc:Telephone>
        <cbc:ElectronicMail>billing@coastalwater.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
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
      </cac:Person>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">49</cbc:PaymentMeansCode>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cbc:PaymentID schemeID="ISO 11649">RF13CSWC3117902603</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB21BLUM38010004189160</cbc:ID>
      <cbc:Name>Coastal State Water Company Ltd</cbc:Name>
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
    </cac:PayeeFinancialAccount>
    <cac:PaymentMandate>
      <cbc:ID>CSW-DD-2024-08812</cbc:ID>
      <cbc:MandateTypeCode listID="ISO 20022 SequenceType3Code">RCUR</cbc:MandateTypeCode>
      <cbc:MaximumPaidAmount currencyID="XBL">150.00</cbc:MaximumPaidAmount>
      <cbc:SignatureID>SIG-CSW-DD-2024-08812</cbc:SignatureID>
      <cac:PayerFinancialAccount>
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
      </cac:PayerFinancialAccount>
      <cac:ValidityPeriod>
        <cbc:StartDate>2024-09-02</cbc:StartDate>
      </cac:ValidityPeriod>
      <cac:PaymentReversalPeriod>
        <cbc:DurationMeasure unitCode="WEE">8</cbc:DurationMeasure>
      </cac:PaymentReversalPeriod>
      <cac:Clause>
        <cbc:ID>CSW-DD-T3</cbc:ID>
        <cbc:Content>The company announces each collection at least five days before.</cbc:Content>
      </cac:Clause>
    </cac:PaymentMandate>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:ID>TA-UTIL</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>21 days net from the bill. Collected by direct debit on that day.</cbc:Note>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>7</cbc:InterestRatePercent>
      <cbc:TimeBasisCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">ANN</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:InterestCalculationCode">SIMPLE</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:PrepaidPayment>
    <cbc:ID>CSW-OA-097315-2526</cbc:ID>
    <cbc:PaidAmount currencyID="XBL">1008.00</cbc:PaidAmount>
    <cbc:PaidDate>2026-03-02</cbc:PaidDate>
  </cac:PrepaidPayment>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">41.40</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">399.50</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">636.90</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">41.40</cbc:TaxAmount>
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
    <cbc:LineExtensionAmount currencyID="XBL">1036.40</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">1036.40</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">1077.80</cbc:TaxInclusiveAmount>
    <cbc:PrepaidAmount currencyID="XBL">1008.00</cbc:PrepaidAmount>
    <cbc:PayableAmount currencyID="XBL">141.20</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:CollectionInvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Collected for the city of Lumeport and paid on to it.</cbc:Note>
    <cbc:InvoicedQuantity unitCode="MTQ">170</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">71.40</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">WTER</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2025-04-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:Description>Account year April 2025 to March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:CollectedForParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:CollectedForParty>
    <cac:Item>
      <cbc:Description>The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.</cbc:Description>
      <cbc:Name>Sewage levy of the city of Lumeport</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CSW-LEVY</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">LEVY</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Collected for a public body, outside the scope of the state sales tax</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">0.42</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:CollectionInvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="MTQ">170</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">399.50</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">WTER</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2025-04-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:Description>Account year April 2025 to March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:PurchaseReference>
      <cbc:ID>CSW-W-71844</cbc:ID>
      <cbc:Description>Gull Lane 57, water</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description>Drinking water supply, per cubic metre.</cbc:Description>
      <cbc:Name>Drinking water</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CW-M3</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">2.35</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>3</cbc:ID>
    <cbc:InvoicedQuantity unitCode="MWH">6.6</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">610.50</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">UBIL</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2025-04-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:Description>Account year April 2025 to March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:PurchaseReference>
      <cbc:ID>CSW-H-71844</cbc:ID>
      <cbc:Description>Gull Lane 57, district heat</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description>Heat from Lumeport's district heating network, per megawatt hour at the flat's heat meter.</cbc:Description>
      <cbc:Name>District heat</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CSW-HEAT</cbc:ID>
      </cac:SellersItemIdentification>
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
      <cbc:PriceAmount currencyID="XBL">92.5</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MWH">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>4</cbc:ID>
    <cbc:InvoicedQuantity unitCode="MWH">6.6</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">26.40</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">UBIL</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2025-04-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:Description>Account year April 2025 to March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:PurchaseReference>
      <cbc:ID>CSW-H-71844</cbc:ID>
      <cbc:Description>Gull Lane 57, district heat</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description>The charge for return water that comes back warmer than the network's standard, per megawatt hour of heat and degree short of the standard cooling.</cbc:Description>
      <cbc:Name>District heating cooling correction</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CSW-COOL</cbc:ID>
      </cac:SellersItemIdentification>
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
      <cbc:PriceAmount currencyID="XBL">4</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MWH">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
