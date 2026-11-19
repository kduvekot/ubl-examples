# Remittance Advice: Valdara Industries to Ferrano Energy

*Example 4 of the flow "Electricity, water and telecom (one utility in each country)" · [Remittance Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REMITTANCE-ADVICE-SCHEMA)*

The manufacturer pays both electricity bills in one transfer.

[The XML file](04-RemittanceAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:remittance-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Remittance advice". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **UTILITIES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-RM-26-0316**  
  The payer's remittance number.
- `UUID` = **2d5c6916-4910-521a-8f1e-a8eed2f264ea**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-19**  
  Paid before the due date.
- `IssueTime` = **13:33:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Note` = **Rikrir skul drek tirnan krirstul.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): What the advice is for.
- `Note` = **Payment of the invoice below.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What the advice is for.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, the currency of the invoice paid; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `TotalDebitAmount` = **15096168** (currencyID `XUF`)  
  The invoices paid.
- `TotalCreditAmount` = **0** (currencyID `XUF`)  
  No credits taken.
- `TotalPaymentAmount` = **15096168** (currencyID `XUF`)  
  The amount transferred: the payable amount of the invoice.
- `PaymentOrderReference` = **VI-PAY-26-0313**  
  The payment order the payer gave its bank.
- `InvoicingPartyReference` = **RF58FEINV260313**  
  The reference the invoicing party asked to quote.
- `LineCountNumeric` = **1**  
  The invoice paid.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-03-01**  
  The month paid for.
- `EndDate` = **2026-03-31**  
  Its end.

### Billing Reference

Inside `BillingReference`:

- `InvoiceDocumentReference/ID` = **FE-INV-26-0313**  
  The invoice this payment settles.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **VI-BANK-26-04**  
  The payer's bank statement line.
- `DocumentType` = **Bank statement**  
  The kind of document referred to, the payer's bank statement line, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Signature

Inside `Signature`:

- `ID` = **VI-SIG-RA**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
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
- `Party/Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **payables@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Energy**  
  The trading name; identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/ID` = **4160202777983743** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Duznaz Hekrul Skultrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/StreetName` = **Corso della Repubblica** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); identity of Ferrano Energy (world/parties.json).
- `Party/Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Department` = **Customer service**  
  The department the desk belongs to; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 474 7922**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Energy (world/parties.json).
- `Party/Contact/ElectronicMail` = **billing@ferranoenergy.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Ferrano Energy (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `InstructionID` = **VI-PAY-26-0313**  
  The payer's own number for the payment order it gave its bank.
- `PaymentID` = **RF58FEINV260313** (schemeID `ISO 11649`)  
  The creditor reference from the invoice, quoted so the payee can match the payment automatically. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `PayerFinancialAccount/ID` = **XU790351041600000000209458** (schemeID `urn:ubl-examples:world:account`)  
  The account the payer pays from. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayerFinancialAccount/Name` = **Valdara Industries SUA**  
  The account holder, as the bank knows it.
- `PayerFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayerFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayerFinancialAccount/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PayerFinancialAccount/FinancialInstitutionBranch/ID` = **03510-41600** (schemeID `urn:ubl-examples:world:XU:bank-branch`)  
  The branch that keeps the account, by its national code: the ABI and CAB code of an Urvanian bank branch (the five-digit ABI code of the bank and the five-digit CAB code of the branch, Italian style). The account number holds it.
- `PayerFinancialAccount/FinancialInstitutionBranch/Name` = **Ferrano main branch**  
  The branch's name.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREVXUFR** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code CREV, the country XU and the location FR; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Trazhek Hekrul Rikbul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Building number of the postal address. identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **4100**  
  Postal code in Urvania's format (4 digits). identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town the branch is in.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town the branch is in.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayerFinancialAccount/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/ID` = **XU080351041600000004084431** (schemeID `urn:ubl-examples:world:account`)  
  The account stated on the invoice. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Ferrano Energy SUA**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **03510-41600** (schemeID `urn:ubl-examples:world:XU:bank-branch`)  
  The branch that keeps the account, by its national code: the ABI and CAB code of an Urvanian bank branch (the five-digit ABI code of the bank and the five-digit CAB code of the branch, Italian style). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Ferrano main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREVXUFR** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code CREV, the country XU and the location FR; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Trazhek Hekrul Rikbul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Building number of the postal address. identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **4100**  
  Postal code in Urvania's format (4 digits). identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **2516028** (currencyID `XUF`)  
  The value added tax included in the payment, which the manufacturer deducts in its own return (20 % of the price before tax).

### Remittance Advice Line

Inside `RemittanceAdviceLine`:

- `ID` = **1**  
  One invoice paid.
- `DebitLineAmount` = **15096168** (currencyID `XUF`)  
  The amount of the invoice this payment settles: the whole payable amount. Paid invoices are debits on a remittance advice, as in the OASIS example UBL-RemittanceAdvice-2.0-Example.
- `BalanceAmount` = **0** (currencyID `XUF`)  
  Nothing remains open on the invoice after this payment.
- `PaymentPurposeCode` = **ELEC** (listID `ISO 20022 ExternalPurpose1Code`)  
  ISO 20022 purpose code ELEC: an electricity bill, the larger part of the bill paid. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: ELEC = ElectricityBill.
- `InvoicingPartyReference` = **RF58FEINV260313**  
  The reference the invoicing party asked to quote.
- `InvoicePeriod/StartDate` = **2026-03-01**  
  March.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  Its end.
- `BillingReference/InvoiceDocumentReference/ID` = **FE-INV-26-0313**  
  The invoice this payment settles.
- `BillingReference/InvoiceDocumentReference/IssueDate` = **2026-04-02**  
  Its issue date, so the reference is unambiguous.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RemittanceAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:remittance-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-RM-26-0316</cbc:ID>
  <cbc:UUID>2d5c6916-4910-521a-8f1e-a8eed2f264ea</cbc:UUID>
  <cbc:IssueDate>2026-04-19</cbc:IssueDate>
  <cbc:IssueTime>13:33:00-01:00</cbc:IssueTime>
  <cbc:Note languageID="qau">Rikrir skul drek tirnan krirstul.</cbc:Note>
  <cbc:Note languageID="en-XU">Payment of the invoice below.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cbc:TotalDebitAmount currencyID="XUF">15096168</cbc:TotalDebitAmount>
  <cbc:TotalCreditAmount currencyID="XUF">0</cbc:TotalCreditAmount>
  <cbc:TotalPaymentAmount currencyID="XUF">15096168</cbc:TotalPaymentAmount>
  <cbc:PaymentOrderReference>VI-PAY-26-0313</cbc:PaymentOrderReference>
  <cbc:InvoicingPartyReference>RF58FEINV260313</cbc:InvoicingPartyReference>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-03-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
  </cac:InvoicePeriod>
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>FE-INV-26-0313</cbc:ID>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-BANK-26-04</cbc:ID>
    <cbc:DocumentType>Bank statement</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>VI-SIG-RA</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:AccountingCustomerParty>
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
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
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
        <cbc:Name>Accounts payable</cbc:Name>
        <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>payables@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Energy</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202777983743</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Duznaz Hekrul Skultrir</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Corso della Repubblica</cbc:StreetName>
        <cbc:BuildingNumber>9</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4150</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Billing</cbc:Name>
        <cbc:JobTitle>Billing officer</cbc:JobTitle>
        <cbc:Department>Customer service</cbc:Department>
        <cbc:Telephone>+999 1 041 474 7922</cbc:Telephone>
        <cbc:ElectronicMail>billing@ferranoenergy.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105781</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:InstructionID>VI-PAY-26-0313</cbc:InstructionID>
    <cbc:PaymentID schemeID="ISO 11649">RF58FEINV260313</cbc:PaymentID>
    <cac:PayerFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU790351041600000000209458</cbc:ID>
      <cbc:Name>Valdara Industries SUA</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:bank-branch">03510-41600</cbc:ID>
        <cbc:Name>Ferrano main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">CREVXUFR</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qau">Trazhek Hekrul Rikbul</cbc:StreetName>
            <cbc:StreetName languageID="en-XU">Piazza della Banca</cbc:StreetName>
            <cbc:BuildingNumber>8</cbc:BuildingNumber>
            <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
            <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
            <cbc:PostalZone>4100</cbc:PostalZone>
            <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              <cbc:Name>Urvania</cbc:Name>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
        <cac:Address>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayerFinancialAccount>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU080351041600000004084431</cbc:ID>
      <cbc:Name>Ferrano Energy SUA</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:bank-branch">03510-41600</cbc:ID>
        <cbc:Name>Ferrano main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">CREVXUFR</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qau">Trazhek Hekrul Rikbul</cbc:StreetName>
            <cbc:StreetName languageID="en-XU">Piazza della Banca</cbc:StreetName>
            <cbc:BuildingNumber>8</cbc:BuildingNumber>
            <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
            <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
            <cbc:PostalZone>4100</cbc:PostalZone>
            <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              <cbc:Name>Urvania</cbc:Name>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
        <cac:Address>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">2516028</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:RemittanceAdviceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DebitLineAmount currencyID="XUF">15096168</cbc:DebitLineAmount>
    <cbc:BalanceAmount currencyID="XUF">0</cbc:BalanceAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">ELEC</cbc:PaymentPurposeCode>
    <cbc:InvoicingPartyReference>RF58FEINV260313</cbc:InvoicingPartyReference>
    <cac:InvoicePeriod>
      <cbc:StartDate>2026-03-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
    </cac:InvoicePeriod>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>FE-INV-26-0313</cbc:ID>
        <cbc:IssueDate>2026-04-02</cbc:IssueDate>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
  </cac:RemittanceAdviceLine>
</RemittanceAdvice>
```
