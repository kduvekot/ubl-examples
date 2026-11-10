# Remittance Advice: Valdara Industries to Ferrano Energy

*Example 4 of the flow "Electricity, water and telecom (one utility in each country)" · [Remittance Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REMITTANCE-ADVICE-SCHEMA)*

The manufacturer pays both electricity bills in one transfer.

[The XML file](04-RemittanceAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:utilities**  
  The business process the document belongs to: the flow "Electricity, water and telecom (one utility in each country)".
- `ProfileExecutionID` = **UTILITIES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-RM-26-0316**  
  The payer's remittance number.
- `UUID` = **2d5c6916-4910-521a-8f1e-a8eed2f264ea**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-10**  
  Paid within ten days, to take the cash discount of the invoice's terms.
- `IssueTime` = **13:33:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Payment of the invoice below.**  
  What the advice is for.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the currency of the invoice paid; it has no minor unit.
- `TotalDebitAmount` = **14479272** (currencyID `XUF`)  
  The invoices paid.
- `TotalCreditAmount` = **289585** (currencyID `XUF`)  
  Credits taken: the settlement discount.
- `TotalPaymentAmount` = **14189687** (currencyID `XUF`)  
  The amount transferred: the payable amount less the 2 % discount for payment within the discount period.
- `PaymentOrderReference` = **VI-PAY-26-0313**  
  The payment order the payer gave its bank.
- `PayerReference` = **VI-0313**  
  The payer's own reference for this payment run.
- `InvoicingPartyReference` = **RF58FEINV260313**  
  The reference the invoicing party asked to quote.
- `LineCountNumeric` = **1**  
  One invoice paid.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.ferranoenergy.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Energy (world/parties.json).
- `Party/IndustryClassificationCode` = **3510** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Energy (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Energy**  
  The trading name; identity of Ferrano Energy (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via della Centrale**  
  Street of the postal address. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered for value added tax; identity of Ferrano Energy (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007404785**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Energy (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered, with its legal form; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105781**  
  Number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1949-01-15**  
  The day the company was entered in the register; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/CorporateStockAmount` = **600000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4130 5781**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@ferranoenergy.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Energy (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Energy (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer.
- `InstructionID` = **VI-PAY-26-0313**  
  The payer's own number for the payment order it gave its bank.
- `PaymentID` = **RF58FEINV260313**  
  The creditor reference from the invoice, quoted so the payee can match the payment automatically.
- `PayerFinancialAccount/ID` = **XU20CREV0000209458** (schemeID `urn:ubl-examples:world:account`)  
  The account the payer pays from. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayerFinancialAccount/Name` = **Valdara Industries SUA**  
  The account holder, as the bank knows it.
- `PayerFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayerFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayerFinancialAccount/CurrencyCode` = **XUF**  
  The account is kept in the currency of the bank's country.
- `PayerFinancialAccount/FinancialInstitutionBranch/ID` = **CREV-001**  
  The branch that keeps the account.
- `PayerFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREV**  
  The bank code, the part of every account number that names the bank; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca**  
  The bank's head office; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Its building number; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano**  
  Its town; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU**  
  The bank's country.
- `PayerFinancialAccount/Country/IdentificationCode` = **XU**  
  The country where the account is kept.
- `PayeeFinancialAccount/ID` = **XU46CREV0004084431** (schemeID `urn:ubl-examples:world:account`)  
  The account stated on the invoice. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Ferrano Energy SUA**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XUF**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **CREV-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREV**  
  The bank code, the part of every account number that names the bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca**  
  The bank's head office; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Its building number; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano**  
  Its town; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU**  
  The bank's country.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XU**  
  The country where the account is kept.

### Remittance Advice Line

Inside `RemittanceAdviceLine`:

- `ID` = **1**  
  One invoice paid.
- `Note` = **2 % discount taken: paid within the discount period of the invoice's terms.**  
  Why less is paid than invoiced.
- `DebitLineAmount` = **14479272** (currencyID `XUF`)  
  The amount of the invoice this payment settles: the whole payable amount. Paid invoices are debits on a remittance advice, as in the OASIS example UBL-RemittanceAdvice-2.0-Example.
- `CreditLineAmount` = **289585** (currencyID `XUF`)  
  The settlement discount taken, a credit against the invoice.
- `BalanceAmount` = **0** (currencyID `XUF`)  
  Nothing remains open on the invoice after this payment.
- `PaymentPurposeCode` = **SUPP**  
  ISO 20022 purpose code SUPP: payment to a supplier.
- `InvoicingPartyReference` = **RF58FEINV260313**  
  The reference the invoicing party asked to quote.
- `AccountingSupplierParty/Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingSupplierParty/Party/PartyName/Name` = **Ferrano Energy**  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingCustomerParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AccountingCustomerParty/Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `BillingReference/InvoiceDocumentReference/ID` = **FE-INV-26-0313**  
  The invoice this payment settles.
- `BillingReference/InvoiceDocumentReference/IssueDate` = **2026-04-02**  
  Its issue date, so the reference is unambiguous.
- `DocumentReference/ID` = **FE-INV-26-0313**  
  The invoice paid, as a document reference.
- `DocumentReference/IssueDate` = **2026-04-02**  
  Its issue date.
- `DocumentReference/DocumentTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RemittanceAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:utilities</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-RM-26-0316</cbc:ID>
  <cbc:UUID>2d5c6916-4910-521a-8f1e-a8eed2f264ea</cbc:UUID>
  <cbc:IssueDate>2026-04-10</cbc:IssueDate>
  <cbc:IssueTime>13:33:00</cbc:IssueTime>
  <cbc:Note>Payment of the invoice below.</cbc:Note>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cbc:TotalDebitAmount currencyID="XUF">14479272</cbc:TotalDebitAmount>
  <cbc:TotalCreditAmount currencyID="XUF">289585</cbc:TotalCreditAmount>
  <cbc:TotalPaymentAmount currencyID="XUF">14189687</cbc:TotalPaymentAmount>
  <cbc:PaymentOrderReference>VI-PAY-26-0313</cbc:PaymentOrderReference>
  <cbc:PayerReference>VI-0313</cbc:PayerReference>
  <cbc:InvoicingPartyReference>RF58FEINV260313</cbc:InvoicingPartyReference>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007299291</cbc:CompanyID>
        <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
          <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
        <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
        <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4120 4274</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode>AL</cbc:ChannelCode>
          <cbc:Value>+999 1 7000 4274</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
      <cac:ServiceProviderParty>
        <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
        <cac:Party>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Castrano Logistics</cbc:Name>
          </cac:PartyName>
        </cac:Party>
      </cac:ServiceProviderParty>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.ferranoenergy.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3510</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Energy</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via della Centrale</cbc:StreetName>
        <cbc:BuildingNumber>44</cbc:BuildingNumber>
        <cbc:CityName>Serravona</cbc:CityName>
        <cbc:PostalZone>4130</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007404785</cbc:CompanyID>
        <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
          <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105781</cbc:CompanyID>
        <cbc:RegistrationDate>1949-01-15</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
        <cbc:CorporateStockAmount currencyID="XUF">600000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Serravona</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Customer service</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4130 5781</cbc:Telephone>
        <cbc:ElectronicMail>customer@ferranoenergy.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
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
    <cbc:PaymentID>RF58FEINV260313</cbc:PaymentID>
    <cac:PayerFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU20CREV0000209458</cbc:ID>
      <cbc:Name>Valdara Industries SUA</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>CREV-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>CREV</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
          <cac:Address>
            <cbc:StreetName>Piazza della Banca</cbc:StreetName>
            <cbc:BuildingNumber>8</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayerFinancialAccount>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU46CREV0004084431</cbc:ID>
      <cbc:Name>Ferrano Energy SUA</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>CREV-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>CREV</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
          <cac:Address>
            <cbc:StreetName>Piazza della Banca</cbc:StreetName>
            <cbc:BuildingNumber>8</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:RemittanceAdviceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>2 % discount taken: paid within the discount period of the invoice's terms.</cbc:Note>
    <cbc:DebitLineAmount currencyID="XUF">14479272</cbc:DebitLineAmount>
    <cbc:CreditLineAmount currencyID="XUF">289585</cbc:CreditLineAmount>
    <cbc:BalanceAmount currencyID="XUF">0</cbc:BalanceAmount>
    <cbc:PaymentPurposeCode>SUPP</cbc:PaymentPurposeCode>
    <cbc:InvoicingPartyReference>RF58FEINV260313</cbc:InvoicingPartyReference>
    <cac:AccountingSupplierParty>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Energy</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:AccountingSupplierParty>
    <cac:AccountingCustomerParty>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:AccountingCustomerParty>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>FE-INV-26-0313</cbc:ID>
        <cbc:IssueDate>2026-04-02</cbc:IssueDate>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
    <cac:DocumentReference>
      <cbc:ID>FE-INV-26-0313</cbc:ID>
      <cbc:IssueDate>2026-04-02</cbc:IssueDate>
      <cbc:DocumentTypeCode>380</cbc:DocumentTypeCode>
    </cac:DocumentReference>
  </cac:RemittanceAdviceLine>
</RemittanceAdvice>
```
