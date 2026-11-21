# Statement: Harbourline Factoring to Velumi Trading

*Example 25 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-STATEMENT-SCHEMA)*

The factor, who now owns the receivables, sends the statement of account on behalf of the distributor.

[The XML file](25-Statement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Statement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0668**  
  The collaboration this document belongs to: Harbourline's collection of the receivable it bought. Harbourline Factoring started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-1335**  
  The factor's statement number.
- `UUID` = **16a04e73-7f53-554f-be69-453ee6e81d9c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-12**  
  The monthly statement of account, on Friday 12 June, the factor's last working day of the week.
- `IssueTime` = **08:43:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **Statement on behalf of Lumeway Distribution, whose receivables Harbourline Factoring holds.**  
  Who the statement is for.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the currency of the invoices; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `TotalDebitAmount` = **54896.00** (currencyID `XBL`)  
  The invoice in full.
- `TotalCreditAmount` = **10000.00** (currencyID `XBL`)  
  The deposit the buyer paid on the order.
- `TotalBalanceAmount` = **44896.00** (currencyID `XBL`)  
  What is owed.
- `LineCountNumeric` = **2**  
  The invoice and the deposit.
- `StatementTypeCode` = **ACCOUNT** (listID `urn:ubl-examples:world:codelist:StatementTypeCode`)  
  A statement of the account. The code is from the Trade Accord's statement type list: ACCOUNT = Statement of account.

### Statement Period

Inside `StatementPeriod`:

- `StartDate` = **2026-05-08**  
  From the account's first movement, the deposit paid on the order's acceptance.
- `EndDate` = **2026-06-13**  
  To the statement date.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **HF-FA-2026-007**  
  The factoring agreement between the distributor and the factor.
- `DocumentType` = **Factoring agreement**  
  The kind of document referred to, the factoring agreement between Lumeway and Harbourline, in words: no list has an exact code for it.

### Signature

Inside `Signature`:

- `ID` = **HF-SIG-26-0040**  
  The factor's seal on the statement.
- `SignatoryParty/PartyIdentification/ID` = **20411233** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Harbourline Factoring**  
  A party referred to from another party's details: its identifier and name are enough.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.

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
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Payee Party

Inside `PayeeParty`:

- `PartyIdentification/ID` = **20411233** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Harbourline Factoring gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Harbourline Factoring**  
  The trading name; as Harbourline Factoring gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-891505** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Harbourline Factoring gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Exchange Street**  
  Street of the postal address. As Harbourline Factoring gives it.
- `PostalAddress/BuildingNumber` = **41**  
  Building number of the postal address. As Harbourline Factoring gives it.
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Harbourline Factoring gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Harbourline Factoring gives it.
- `PostalAddress/PostalZone` = **38522**  
  Postal code in Bayvarra's format (5 digits). As Harbourline Factoring gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Harbourline Factoring gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Accounts receivable**  
  The party's accounts receivable desk: the desk for its role in this document (it is owed the payment); as Harbourline Factoring gives it.
- `Contact/JobTitle` = **Credit controller**  
  The job of the person who answers at the desk; as Harbourline Factoring gives it.
- `Contact/Department` = **Finance**  
  The department the desk belongs to; as Harbourline Factoring gives it.
- `Contact/Telephone` = **+999 2 38 2478 9865**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Harbourline Factoring gives it.
- `Contact/ElectronicMail` = **receivables@harbourline.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Harbourline Factoring gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Harbourline Factoring gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411233** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Harbourline Factoring gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-06-29**  
  When the transfer must be credited. The count ends on Sunday 28 June, no business day in Bayvarra, the payee's country, so the payment is due on the next one, Monday 29 June.
- `PaymentChannelCode` = **RTNS** (listID `ISO 20022 ClearingChannel2Code`)  
  How the payment system clears and settles the transfer, as an ISO 20022 clearing channel. The code is from the world's copy of ISO 20022 ClearingChannel2Code: RTNS = RealTimeNetSettlementSystem.
- `PaymentRailID` = **TRADE-ACCORD-PAY**  
  The payment system the transfer runs over: the Trade Accord's link between the countries.
- `InstructionNote` = **Quote RF21LMWINV261025**  
  What the payer writes in the transfer.
- `PaymentID` = **RF21LMWINV261025** (schemeID `ISO 11649`)  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `ChargeBearerCode` = **SHAR** (listID `ISO 20022 ChargeBearerType1Code`)  
  ISO 20022 SHAR: each side pays its own bank's charges. The code is from the world's copy of ISO 20022 ChargeBearerType1Code: SHAR = Shared.
- `PayeeFinancialAccount/ID` = **XB51BLUM38020502304038** (schemeID `urn:ubl-examples:world:account`)  
  The factor's account, where the invoice is to be paid. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Harbourline Factoring Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PayeeFinancialAccount/PaymentNote` = **Statement LMW-INV-26-1025**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **380205** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Harbour branch**  
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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **Pay the balance by the due date of the invoice.**  
  The terms.
- `PaymentDueDate` = **2026-06-29**  
  The due date. The count ends on Sunday 28 June, no business day in Bayvarra, the payee's country, so the payment is due on the next one, Monday 29 June.

### Statement Line

Inside `StatementLine`:

- `ID` = **1**  
  The open invoice.
- `Note` = **The invoice, bought by the factor.**  
  What the line shows.
- `UUID` = **56439119-78e3-59ec-bc7d-84c3d3a46f09**  
  A universally unique identifier of the line, derived from the document and the line number.
- `BalanceBroughtForwardIndicator` = **false**  
  A new item, not a balance carried over.
- `DebitLineAmount` = **54896.00** (currencyID `XBL`)  
  The invoice in full.
- `BalanceAmount` = **54896.00** (currencyID `XBL`)  
  Before the deposit.
- `PaymentPurposeCode` = **GDDS** (listID `ISO 20022 ExternalPurpose1Code`)  
  ISO 20022 purpose code GDDS: purchase of goods. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: GDDS = PurchaseSaleOfGoods.
- `PaymentTerms/PaymentDueDate` = **2026-06-29**  
  The due date of the balance. The count ends on Sunday 28 June, no business day in Bayvarra, the payee's country, so the payment is due on the next one, Monday 29 June.
- `BuyerCustomerParty/Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `BuyerCustomerParty/Party/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingCustomerParty/Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingCustomerParty/Party/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingSupplierParty/Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingSupplierParty/Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `PayeeParty/PartyIdentification/ID` = **20411233** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PayeeParty/PartyName/Name` = **Harbourline Factoring**  
  A party referred to from another party's details: its identifier and name are enough.
- `BillingReference/InvoiceDocumentReference/ID` = **LMW-INV-26-1025**  
  The distributor's invoice, which the factor bought.
- `BillingReference/InvoiceDocumentReference/IssueDate` = **2026-05-14**  
  Its issue date.
- `DocumentReference/ID` = **26-0030**  
  The notice of assignment of the invoice to the factor.
- `DocumentReference/DocumentType` = **Notice of assignment**  
  The kind of document referred to, Harbourline's notice of the assigned receivable, in words: no list has an exact code for it.
- `ID` = **2**  
  The deposit.
- `Note` = **Paid to the distributor before the invoice was assigned.**  
  Why it is a credit.
- `UUID` = **16aec267-0a53-5561-ad4f-79c534c1d918**  
  A universally unique identifier of the line, derived from the document and the line number.
- `CreditLineAmount` = **10000.00** (currencyID `XBL`)  
  The deposit.
- `BalanceAmount` = **44896.00** (currencyID `XBL`)  
  Open after the deposit: what the buyer still owes.
- `PaymentMeans/PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  Paid by credit transfer. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `CollectedPayment/ID` = **26-0025**  
  The deposit payment.
- `CollectedPayment/PaidAmount` = **10000.00** (currencyID `XBL`)  
  Paid.
- `CollectedPayment/ReceivedDate` = **2026-05-11**  
  Received by the distributor on the next business day of Bayvarra's banks.
- `CollectedPayment/PaidDate` = **2026-05-08**  
  Paid by the buyer the day the order was accepted: the payment's dates, not an invoice period.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Statement xmlns="urn:oasis:names:specification:ubl:schema:xsd:Statement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0668</cbc:ProfileExecutionID>
  <cbc:ID>26-1335</cbc:ID>
  <cbc:UUID>16a04e73-7f53-554f-be69-453ee6e81d9c</cbc:UUID>
  <cbc:IssueDate>2026-06-12</cbc:IssueDate>
  <cbc:IssueTime>08:43:00-01:00</cbc:IssueTime>
  <cbc:Note>Statement on behalf of Lumeway Distribution, whose receivables Harbourline Factoring holds.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:TotalDebitAmount currencyID="XBL">54896.00</cbc:TotalDebitAmount>
  <cbc:TotalCreditAmount currencyID="XBL">10000.00</cbc:TotalCreditAmount>
  <cbc:TotalBalanceAmount currencyID="XBL">44896.00</cbc:TotalBalanceAmount>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:StatementTypeCode listID="urn:ubl-examples:world:codelist:StatementTypeCode">ACCOUNT</cbc:StatementTypeCode>
  <cac:StatementPeriod>
    <cbc:StartDate>2026-05-08</cbc:StartDate>
    <cbc:EndDate>2026-06-13</cbc:EndDate>
  </cac:StatementPeriod>
  <cac:AdditionalDocumentReference>
    <cbc:ID>HF-FA-2026-007</cbc:ID>
    <cbc:DocumentType>Factoring agreement</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>HF-SIG-26-0040</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411233</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Harbourline Factoring</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PayeeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411233</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harbourline Factoring</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-891505</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Exchange Street</cbc:StreetName>
      <cbc:BuildingNumber>41</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38522</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Accounts receivable</cbc:Name>
      <cbc:JobTitle>Credit controller</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 2 38 2478 9865</cbc:Telephone>
      <cbc:ElectronicMail>receivables@harbourline.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411233</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:PayeeParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-06-29</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode listID="ISO 20022 ClearingChannel2Code">RTNS</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>TRADE-ACCORD-PAY</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF21LMWINV261025</cbc:InstructionNote>
    <cbc:PaymentID schemeID="ISO 11649">RF21LMWINV261025</cbc:PaymentID>
    <cbc:ChargeBearerCode listID="ISO 20022 ChargeBearerType1Code">SHAR</cbc:ChargeBearerCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB51BLUM38020502304038</cbc:ID>
      <cbc:Name>Harbourline Factoring Ltd</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
      <cbc:PaymentNote>Statement LMW-INV-26-1025</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:bank-branch">380205</cbc:ID>
        <cbc:Name>Harbour branch</cbc:Name>
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
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:Note>Pay the balance by the due date of the invoice.</cbc:Note>
    <cbc:PaymentDueDate>2026-06-29</cbc:PaymentDueDate>
  </cac:PaymentTerms>
  <cac:StatementLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>The invoice, bought by the factor.</cbc:Note>
    <cbc:UUID>56439119-78e3-59ec-bc7d-84c3d3a46f09</cbc:UUID>
    <cbc:BalanceBroughtForwardIndicator>false</cbc:BalanceBroughtForwardIndicator>
    <cbc:DebitLineAmount currencyID="XBL">54896.00</cbc:DebitLineAmount>
    <cbc:BalanceAmount currencyID="XBL">54896.00</cbc:BalanceAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">GDDS</cbc:PaymentPurposeCode>
    <cac:PaymentTerms>
      <cbc:PaymentDueDate>2026-06-29</cbc:PaymentDueDate>
    </cac:PaymentTerms>
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
    <cac:AccountingCustomerParty>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Velumi Trading</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:AccountingCustomerParty>
    <cac:AccountingSupplierParty>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:AccountingSupplierParty>
    <cac:PayeeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411233</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Harbourline Factoring</cbc:Name>
      </cac:PartyName>
    </cac:PayeeParty>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>LMW-INV-26-1025</cbc:ID>
        <cbc:IssueDate>2026-05-14</cbc:IssueDate>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
    <cac:DocumentReference>
      <cbc:ID>26-0030</cbc:ID>
      <cbc:DocumentType>Notice of assignment</cbc:DocumentType>
    </cac:DocumentReference>
  </cac:StatementLine>
  <cac:StatementLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Paid to the distributor before the invoice was assigned.</cbc:Note>
    <cbc:UUID>16aec267-0a53-5561-ad4f-79c534c1d918</cbc:UUID>
    <cbc:CreditLineAmount currencyID="XBL">10000.00</cbc:CreditLineAmount>
    <cbc:BalanceAmount currencyID="XBL">44896.00</cbc:BalanceAmount>
    <cac:PaymentMeans>
      <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    </cac:PaymentMeans>
    <cac:CollectedPayment>
      <cbc:ID>26-0025</cbc:ID>
      <cbc:PaidAmount currencyID="XBL">10000.00</cbc:PaidAmount>
      <cbc:ReceivedDate>2026-05-11</cbc:ReceivedDate>
      <cbc:PaidDate>2026-05-08</cbc:PaidDate>
    </cac:CollectedPayment>
  </cac:StatementLine>
</Statement>
```
