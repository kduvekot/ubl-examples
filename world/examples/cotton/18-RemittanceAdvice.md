# Remittance Advice: Lumeport Textile Mill to Selanu Cotton Ginnery

*Example 18 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Remittance Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REMITTANCE-ADVICE-SCHEMA)*

The mill pays the island's ginnery: money flows to the island for once.

[The XML file](18-RemittanceAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:remittance-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Remittance advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900013293**  
  The collaboration this document belongs to: the textile mill's order of cotton lint from the ginnery. Lumeport Textile Mill started it and gave it this identifier, which every document of it repeats.
- `ID` = **2000005423**  
  The payer's remittance number.
- `UUID` = **4dead5a1-d2ba-5e05-a95b-17805f866743**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-22**  
  The mill pays the ginnery 45 days after its invoice, on Monday 22 June, the next working day after the 45th day, a Sunday: money flows to the island.
- `IssueTime` = **15:45:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **Payment of the invoice below.**  
  What the advice is for.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the currency of the invoice paid; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `TotalDebitAmount` = **6055.452** (currencyID `XLC`)  
  The invoices paid.
- `TotalCreditAmount` = **0.000** (currencyID `XLC`)  
  No credits taken.
- `TotalPaymentAmount` = **6055.452** (currencyID `XLC`)  
  The amount transferred: the payable amount of the invoice.
- `PaymentOrderReference` = **1500000678**  
  The payment order the payer gave its bank.
- `InvoicingPartyReference` = **RF28SCGINV260243**  
  The reference the invoicing party asked to quote.
- `LineCountNumeric` = **1**  
  The invoice paid.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9524010900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeport Textile Mill gives it.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; as Lumeport Textile Mill gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-933254** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Textile Mill gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. As Lumeport Textile Mill gives it.
- `Party/PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. As Lumeport Textile Mill gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Mill Quarter**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Textile Mill gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Textile Mill gives it.
- `Party/PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Textile Mill gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Textile Mill gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Lumeport Textile Mill gives it.
- `Party/Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Lumeport Textile Mill gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Lumeport Textile Mill gives it.
- `Party/Contact/Telephone` = **+999 2 38 2837 6029**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeport Textile Mill gives it.
- `Party/Contact/ElectronicMail` = **payables@lumeporttextile.example**  
  The contact's e-mail address; as Lumeport Textile Mill gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Textile Mill gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. As Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Accounts receivable**  
  The party's accounts receivable desk: the desk for its role in this document (it is owed the payment); as Selanu Cotton Ginnery gives it.
- `Party/Contact/JobTitle` = **Credit controller**  
  The job of the person who answers at the desk; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Telephone` = **+999 3 721 0486**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Cotton Ginnery gives it.
- `Party/Contact/ElectronicMail` = **receivables@selanuginnery.example**  
  The contact's e-mail address; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Cotton Ginnery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `InstructionID` = **1500000678**  
  The payer's own number for the payment order it gave its bank.
- `PaymentID` = **RF28SCGINV260243** (schemeID `ISO 11649`)  
  The creditor reference from the invoice, quoted so the payee can match the payment automatically. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `PayerFinancialAccount/ID` = **XB35BLUM38020504608076** (schemeID `urn:ubl-examples:world:account`)  
  The account the payer pays from. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayerFinancialAccount/Name` = **Lumeport Textile Mill Ltd**  
  The account holder, as the bank knows it.
- `PayerFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayerFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayerFinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PayerFinancialAccount/FinancialInstitutionBranch/ID` = **380205** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `PayerFinancialAccount/FinancialInstitutionBranch/Name` = **Harbour branch**  
  The branch's name.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BLUM, the country XB and the location LX; as Bank of Lumeport gives it.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; as Bank of Lumeport gives it.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  Street of the postal address. As Bank of Lumeport gives it.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Building number of the postal address. As Bank of Lumeport gives it.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bank of Lumeport gives it.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). As Bank of Lumeport gives it.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bank of Lumeport gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayerFinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/ID` = **XL31BSEL0020004922263** (schemeID `urn:ubl-examples:world:account`)  
  The account stated on the invoice. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Selanu Cotton Ginnery Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **002** (schemeID `urn:ubl-examples:world:XL:bank-branch`)  
  The branch that keeps the account, by its national code: the branch number of a Lisavan bank (three digits). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Market branch**  
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
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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

### Remittance Advice Line

Inside `RemittanceAdviceLine`:

- `ID` = **1**  
  One invoice paid.
- `DebitLineAmount` = **6055.452** (currencyID `XLC`)  
  The amount of the invoice this payment settles: the whole payable amount. A remittance advice lists each invoice paid on its debit side, and a discount taken against it on its credit side.
- `BalanceAmount` = **0.000** (currencyID `XLC`)  
  Nothing remains open on the invoice after this payment.
- `PaymentPurposeCode` = **SUPP** (listID `ISO 20022 ExternalPurpose1Code`)  
  ISO 20022 purpose code SUPP: payment to a supplier. The code is from the world's copy of ISO 20022 ExternalPurpose1Code: SUPP = SupplierPayment.
- `InvoicingPartyReference` = **RF28SCGINV260243**  
  The reference the invoicing party asked to quote.
- `BillingReference/InvoiceDocumentReference/ID` = **SCG-INV-26-0243**  
  The invoice this payment settles.
- `BillingReference/InvoiceDocumentReference/IssueDate` = **2026-05-07**  
  Its issue date, so the reference is unambiguous.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RemittanceAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:remittance-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900013293</cbc:ProfileExecutionID>
  <cbc:ID>2000005423</cbc:ID>
  <cbc:UUID>4dead5a1-d2ba-5e05-a95b-17805f866743</cbc:UUID>
  <cbc:IssueDate>2026-06-22</cbc:IssueDate>
  <cbc:IssueTime>15:45:00-01:00</cbc:IssueTime>
  <cbc:Note>Payment of the invoice below.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:TotalDebitAmount currencyID="XLC">6055.452</cbc:TotalDebitAmount>
  <cbc:TotalCreditAmount currencyID="XLC">0.000</cbc:TotalCreditAmount>
  <cbc:TotalPaymentAmount currencyID="XLC">6055.452</cbc:TotalPaymentAmount>
  <cbc:PaymentOrderReference>1500000678</cbc:PaymentOrderReference>
  <cbc:InvoicingPartyReference>RF28SCGINV260243</cbc:InvoicingPartyReference>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9524010900002</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-933254</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Mill Street</cbc:StreetName>
        <cbc:BuildingNumber>21</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Mill Quarter</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38504</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Accounts payable</cbc:Name>
        <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 2 38 2837 6029</cbc:Telephone>
        <cbc:ElectronicMail>payables@lumeporttextile.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
        <cbc:BuildingNumber>42</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
        <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Accounts receivable</cbc:Name>
        <cbc:JobTitle>Credit controller</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
        <cbc:ElectronicMail>receivables@selanuginnery.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:InstructionID>1500000678</cbc:InstructionID>
    <cbc:PaymentID schemeID="ISO 11649">RF28SCGINV260243</cbc:PaymentID>
    <cac:PayerFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB35BLUM38020504608076</cbc:ID>
      <cbc:Name>Lumeport Textile Mill Ltd</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
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
    </cac:PayerFinancialAccount>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL31BSEL0020004922263</cbc:ID>
      <cbc:Name>Selanu Cotton Ginnery Ltd</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XLC</cbc:CurrencyCode>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:bank-branch">002</cbc:ID>
        <cbc:Name>Market branch</cbc:Name>
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
  <cac:RemittanceAdviceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DebitLineAmount currencyID="XLC">6055.452</cbc:DebitLineAmount>
    <cbc:BalanceAmount currencyID="XLC">0.000</cbc:BalanceAmount>
    <cbc:PaymentPurposeCode listID="ISO 20022 ExternalPurpose1Code">SUPP</cbc:PaymentPurposeCode>
    <cbc:InvoicingPartyReference>RF28SCGINV260243</cbc:InvoicingPartyReference>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>SCG-INV-26-0243</cbc:ID>
        <cbc:IssueDate>2026-05-07</cbc:IssueDate>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
  </cac:RemittanceAdviceLine>
</RemittanceAdvice>
```
