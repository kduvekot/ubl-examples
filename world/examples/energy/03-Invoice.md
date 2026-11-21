# Invoice: Montebrio Power to Ferrano Energy

*Example 3 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The power station invoices the electricity it fed in for the retail company in March.

[The XML file](03-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Invoice/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0#compliant#urn:ubl-examples:world:XU:invoice:1.0#compliant#urn:ubl-examples:world:community:energy-xu:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Billing"; the national specification "Invoice rules of Urvania"; the community specification "Urvania energy market". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900004627**  
  The collaboration this document belongs to: Montebrio Power's bill for March's electricity to Ferrano Energy, to its payment. Montebrio Power started it and gave it this identifier, which every document of it repeats.
- `ID` = **2026/0133**  
  The seller's invoice number.
- `UUID` = **f2bffa54-247a-500b-9993-16f7d9a166d9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-03**  
  The month's electricity.
- `IssueTime` = **16:42:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `DueDate` = **2026-05-04**  
  As the payment terms below count it: 30 days net; 2 % discount when paid within 10 days. The count ends on Sunday 3 May, no business day in Urvania, the payee's country, so the payment is due on the next one, Monday 4 May.
- `InvoiceTypeCode` = **380** (listID `UN/EDIFACT EDED 1001`)  
  A commercial invoice, as UN/EDIFACT 1001 codes it. The code is from the world's copy of UN/EDIFACT 1001 Document name: 380 = Commercial invoice.
- `TaxPointDate` = **2026-04-03**  
  Urvania's value added tax becomes due on the invoice date.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, the seller's currency; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `LineCountNumeric` = **1**  
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

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Montebrio Power gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10087** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Montebrio Power gives it.
- `Party/PartyName/Name` = **Montebrio Power**  
  The trading name; as Montebrio Power gives it.
- `Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `Party/PostalAddress/ID` = **4170200397702895** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Montebrio Power gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Hekrul Trinskul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Montebrio Power gives it.
- `Party/PostalAddress/StreetName` = **Via della Centrale** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Montebrio Power gives it.
- `Party/PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. As Montebrio Power gives it.
- `Party/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Montebrio Power gives it.
- `Party/PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Montebrio Power gives it.
- `Party/PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). As Montebrio Power gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Montebrio Power gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered for value added tax; as Montebrio Power gives it.
- `Party/PartyTaxScheme/CompanyID` = **XU007414377** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); as Montebrio Power gives it. The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered, with its legal form; as Montebrio Power gives it.
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Montebrio Power gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `Party/PartyLegalEntity/CorporateStockAmount` = **400000000** (currencyID `XUF`)  
  The share capital, in ferra, as paid up: Urvania's company law asks an SUA to state it on its invoices and business letters; as Montebrio Power gives it.
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up, so the amount stated is the whole share capital.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/Contact/Name` = **Accounts receivable**  
  The party's accounts receivable desk: the desk for its role in this document (it is owed the payment); as Montebrio Power gives it.
- `Party/Contact/JobTitle` = **Credit controller**  
  The job of the person who answers at the desk; as Montebrio Power gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Montebrio Power gives it.
- `Party/Contact/Telephone` = **+999 1 0425 46716**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0425 and 5 digits (9); no area code is the start of another. Mobiles start with 3 and have 10 digits. As Montebrio Power gives it.
- `Party/Contact/ElectronicMail` = **receivables@montebrio.example**  
  The contact's e-mail address; as Montebrio Power gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Montebrio Power gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Montebrio Power gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Energy gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Energy**  
  The trading name; as Ferrano Energy gives it.
- `Party/PostalAddress/ID` = **4160202777983743** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Energy gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Duznaz Hekrul Skultrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Energy gives it.
- `Party/PostalAddress/StreetName` = **Corso della Repubblica** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Energy gives it.
- `Party/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Ferrano Energy gives it.
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Energy gives it.
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Energy gives it.
- `Party/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). As Ferrano Energy gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Energy gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered, with its legal form; as Ferrano Energy gives it.
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Ferrano Energy gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Party/Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Ferrano Energy gives it.
- `Party/Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Ferrano Energy gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Ferrano Energy gives it.
- `Party/Contact/Telephone` = **+999 1 041 474 7922**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0425 and 5 digits (9); no area code is the start of another. Mobiles start with 3 and have 10 digits. As Ferrano Energy gives it.
- `Party/Contact/ElectronicMail` = **payables@ferranoenergy.example**  
  The contact's e-mail address; as Ferrano Energy gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Ferrano Energy gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Energy gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Ferrano Energy**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Montebrio Power**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-05-04**  
  When the transfer must be credited.
- `PaymentChannelCode` = **RTGS** (listID `ISO 20022 ClearingChannel2Code`)  
  How the payment system clears and settles the transfer, as an ISO 20022 clearing channel. The code is from the world's copy of ISO 20022 ClearingChannel2Code: RTGS = RealTimeGrossSettlementSystem.
- `PaymentRailID` = **FERRA-RTGS**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF5620260133**  
  What the payer writes in the transfer.
- `PaymentID` = **RF5620260133** (schemeID `ISO 11649`)  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `PayeeFinancialAccount/ID` = **XU720351041700000005021992** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Montebrio Power SUA**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PayeeFinancialAccount/PaymentNote` = **Invoice 2026/0133**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **03510-41700** (schemeID `urn:ubl-examples:world:XU:bank-branch`)  
  The branch that keeps the account, by its national code: the ABI and CAB code of an Urvanian bank branch (the five-digit ABI code of the bank and the five-digit CAB code of the branch, Italian style). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Serravona branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREVXUFR** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code CREV, the country XU and the location FR; as Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; as Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Trazhek Hekrul Rikbul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Building number of the postal address. As Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **4100**  
  Postal code in Urvania's format (4 digits). As Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Crevalto Bank gives it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Payment Terms

Inside `PaymentTerms`:

- `ID` = **XU-STD**  
  The standard terms of Urvania.
- `PaymentMeansID` = **1**  
  The payment means these terms apply to: the credit transfer below.
- `Note` = **30 days net; 2 % discount when paid within 10 days.**  
  Urvanian practice: a cash discount for early payment, statutory interest on late payment.
- `SettlementDiscountPercent` = **2**  
  The cash discount for early payment.
- `SettlementDiscountAmount` = **4327680** (currencyID `XUF`)  
  The discount on the amount payable, if paid in time.
- `PaymentTermsDetailsURI` = **https://www.montebrio.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-05-04**  
  The day the amount is due, as the terms count it. The count ends on Sunday 3 May, no business day in Urvania, the payee's country, so the payment is due on the next one, Monday 4 May.
- `SettlementPeriod/StartDate` = **2026-04-03**  
  From the invoice date.
- `SettlementPeriod/EndDate` = **2026-04-13**  
  For 10 days.
- `PenaltyInterestRate/InterestRatePercent` = **8**  
  The interest on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **ANN** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  A yearly rate. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: ANN = year.
- `PenaltyInterestRate/CalculationMethodCode` = **SIMPLE** (listID `urn:ubl-examples:world:codelist:InterestCalculationCode`)  
  Simple interest, per day late. The code is from the Trade Accord's interest calculation method list: SIMPLE = Simple interest.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **36064000** (currencyID `XUF`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **180320000** (currencyID `XUF`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **36064000** (currencyID `XUF`)  
  20 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **180320000** (currencyID `XUF`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **180320000** (currencyID `XUF`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **216384000** (currencyID `XUF`)  
  The total without tax plus the tax.
- `PayableAmount` = **216384000** (currencyID `XUF`)  
  What the buyer is to pay, stated in full so that it books the amount without working it out.

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **18400** (unitCode `MWH`)  
  Fed into the grid for the retail company in March.
- `LineExtensionAmount` = **180320000** (currencyID `XUF`)  
  18400 × 9800, rounded to the minor unit of the currency.
- `Item/Description` = **Zuktrek vizhir muzstir drek zhek hir drek ranek dukmir, kinaz man drek balkul bantan.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `Item/Description` = **Electricity fed into the grid at the power station, sold by the megawatt hour.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Zuktrek, tredran** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `Item/Name` = **Electricity, wholesale** (languageID `en-XU`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **MB-MWH**  
  The seller's own item number; as Montebrio Power describes the item.
- `Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **20**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **9800** (currencyID `XUF`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `MWH`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0#compliant#urn:ubl-examples:world:XU:invoice:1.0#compliant#urn:ubl-examples:world:community:energy-xu:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900004627</cbc:ProfileExecutionID>
  <cbc:ID>2026/0133</cbc:ID>
  <cbc:UUID>f2bffa54-247a-500b-9993-16f7d9a166d9</cbc:UUID>
  <cbc:IssueDate>2026-04-03</cbc:IssueDate>
  <cbc:IssueTime>16:42:00-01:00</cbc:IssueTime>
  <cbc:DueDate>2026-05-04</cbc:DueDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">380</cbc:InvoiceTypeCode>
  <cbc:TaxPointDate>2026-04-03</cbc:TaxPointDate>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-03-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
    <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:PeriodDescriptionCode">MONTH</cbc:DescriptionCode>
    <cbc:Description>March 2026</cbc:Description>
  </cac:InvoicePeriod>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10087</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Montebrio Power</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4170200397702895</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Hekrul Trinskul</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via della Centrale</cbc:StreetName>
        <cbc:BuildingNumber>44</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
        <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
        <cbc:PostalZone>4310</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007414377</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:CorporateStockAmount currencyID="XUF">400000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
          <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Accounts receivable</cbc:Name>
        <cbc:JobTitle>Credit controller</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 1 0425 46716</cbc:Telephone>
        <cbc:ElectronicMail>receivables@montebrio.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105918</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
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
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Accounts payable</cbc:Name>
        <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 1 041 474 7922</cbc:Telephone>
        <cbc:ElectronicMail>payables@ferranoenergy.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105781</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Energy</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Montebrio Power</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-05-04</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode listID="ISO 20022 ClearingChannel2Code">RTGS</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>FERRA-RTGS</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF5620260133</cbc:InstructionNote>
    <cbc:PaymentID schemeID="ISO 11649">RF5620260133</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU720351041700000005021992</cbc:ID>
      <cbc:Name>Montebrio Power SUA</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice 2026/0133</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:bank-branch">03510-41700</cbc:ID>
        <cbc:Name>Serravona branch</cbc:Name>
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
          <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
          <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
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
  <cac:PaymentTerms>
    <cbc:ID>XU-STD</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>30 days net; 2 % discount when paid within 10 days.</cbc:Note>
    <cbc:SettlementDiscountPercent>2</cbc:SettlementDiscountPercent>
    <cbc:SettlementDiscountAmount currencyID="XUF">4327680</cbc:SettlementDiscountAmount>
    <cbc:PaymentTermsDetailsURI>https://www.montebrio.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-05-04</cbc:PaymentDueDate>
    <cac:SettlementPeriod>
      <cbc:StartDate>2026-04-03</cbc:StartDate>
      <cbc:EndDate>2026-04-13</cbc:EndDate>
    </cac:SettlementPeriod>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>8</cbc:InterestRatePercent>
      <cbc:TimeBasisCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">ANN</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:InterestCalculationCode">SIMPLE</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">36064000</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">180320000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">36064000</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">180320000</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XUF">180320000</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XUF">216384000</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XUF">216384000</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="MWH">18400</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XUF">180320000</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description languageID="qau">Zuktrek vizhir muzstir drek zhek hir drek ranek dukmir, kinaz man drek balkul bantan.</cbc:Description>
      <cbc:Description languageID="en-XU">Electricity fed into the grid at the power station, sold by the megawatt hour.</cbc:Description>
      <cbc:Name languageID="qau">Zuktrek, tredran</cbc:Name>
      <cbc:Name languageID="en-XU">Electricity, wholesale</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>MB-MWH</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XUF">9800</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MWH">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
