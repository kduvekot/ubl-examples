# Invoice: Rinova Recovery to Rivermouth Packaging

*Example 10 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

Granulate and barge freight (CPT). An export from Urvania: no VAT charged, with the exemption stated.

[The XML file](10-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:plastics**  
  The business process the document belongs to: the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)".
- `ProfileExecutionID` = **PLASTICS-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **RR-INV-26-0894**  
  The seller's invoice number.
- `UUID` = **462dcfae-0a9f-5692-9219-92c1bf595e5d**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-20**  
  Issued once the granulate is on board.
- `IssueTime` = **11:20:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-05-20**  
  30 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `Note` = **Carriage paid to: the price includes the barge to the river quay.**  
  Why the invoice has no separate freight line.
- `TaxPointDate` = **2026-04-20**  
  Urvania's value added tax becomes due on the invoice date.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the seller's currency; it has no minor unit.
- `PaymentCurrencyCode` = **XUF**  
  Payment is asked in the invoice currency, also from abroad.
- `AccountingCostCode` = **1300**  
  The buyer's cost centre, quoted in its order, so the invoice is booked without asking.
- `AccountingCost` = **Raw materials**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  The number of invoice lines, as a check on the transfer.
- `DefaultLanguageCode` = **en**  
  The language the texts of the invoice are in: the seller's country's language.

### Order Reference

Inside `OrderReference`:

- `ID` = **RP-PO-26-0882**  
  The buyer's order.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **RR-DA-26-0892**  
  The despatch advice.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.rinova.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rinova Recovery (world/parties.json).
- `Party/IndustryClassificationCode` = **3830** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rinova Recovery (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Rinova Recovery (world/parties.json).
- `Party/PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via del Riciclo**  
  Street of the postal address. identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Rinova Recovery (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered for value added tax; identity of Rinova Recovery (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007318479**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Rinova Recovery (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered, with its legal form; identity of Rinova Recovery (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104548**  
  Number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rinova Recovery (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Rinova Recovery (world/parties.json).
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
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4140 4548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rinova Recovery (world/parties.json).
- `Party/PartyAuthorization/Purpose` = **Recovery of non-hazardous plastic waste**  
  What the authority has authorized the party to do; identity of Rinova Recovery (world/parties.json).
- `Party/PartyAuthorization/ValidityPeriod/EndDate` = **2029-12-31**  
  The authorization expires on this date.
- `Party/PartyAuthorization/Certificate/ID` = **XU-ENV-2024-0311**  
  The number of the permit.
- `Party/PartyAuthorization/Certificate/CertificateTypeCode` = **Permit**  
  A permit issued by an authority of the party's country.
- `Party/PartyAuthorization/Certificate/CertificateType` = **Operating permit**  
  The kind of certificate, in words.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.rivermouth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rivermouth Packaging (world/parties.json).
- `Party/IndustryClassificationCode` = **2220** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered for state sales tax; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1238220**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered, with its legal form; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412740**  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 3850 2740**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Rinova Recovery**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-05-20**  
  When the transfer must be credited.
- `PaymentChannelCode` = **IBAN**  
  Paid to an account identified in the format of ISO 13616.
- `PaymentRailID` = **TRADE-ACCORD-PAY**  
  The payment system the transfer runs over: the trade accord's link between the countries.
- `InstructionNote` = **Quote RF89RRINV260894**  
  What the payer writes in the transfer.
- `PaymentID` = **RF89RRINV260894**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `ChargeBearerCode` = **SHAR**  
  ISO 20022 SHAR: each side pays its own bank's charges.
- `PayeeFinancialAccount/ID` = **XU45CREV0000418916** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Rinova Recovery SRU**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XUF**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice RR-INV-26-0894**  
  What the payer is asked to quote with the transfer, so the payment is matched.
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
- `SettlementDiscountAmount` = **199680** (currencyID `XUF`)  
  The discount on the amount payable, if paid in time.
- `PaymentTermsDetailsURI` = **https://www.rinova.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-05-20**  
  The day the amount is due.
- `SettlementPeriod/StartDate` = **2026-04-20**  
  From the invoice date.
- `SettlementPeriod/EndDate` = **2026-04-30**  
  For 10 days.
- `PenaltyInterestRate/InterestRatePercent` = **8**  
  The interest on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **Year**  
  A yearly rate.
- `PenaltyInterestRate/CalculationMethodCode` = **Simple**  
  Simple interest, per day late.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0** (currencyID `XUF`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **9984000** (currencyID `XUF`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0** (currencyID `XUF`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G**  
  Goods exported from Urvania: no value added tax is charged on an export (category G, free export item).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **XU-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export of goods outside Urvania**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **9984000** (currencyID `XUF`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **9984000** (currencyID `XUF`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **9984000** (currencyID `XUF`)  
  The total without tax plus the tax.
- `PayableAmount` = **9984000** (currencyID `XUF`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **120** (unitCode `TNE`)  
  The quantity delivered.
- `LineExtensionAmount` = **9984000** (currencyID `XUF`)  
  120 × 83200, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **1**  
  The order line this invoice line bills.
- `Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.**  
  The seller's description; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/Name` = **Recycled PE granulate**  
  The item's short name; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/SellersItemIdentification/ID` = **RR-PE-R1**  
  The seller's own item number; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/StandardItemIdentification/ID` = **771030000048** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **3901.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **G**  
  Goods exported from Urvania: no value added tax is charged on an export (category G, free export item).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **XU-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Export of goods outside Urvania**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.
- `Item/AdditionalItemProperty/Name` = **Density**  
  A measured property of the item.
- `Item/AdditionalItemProperty/ValueQuantity` = **0.92** (unitCode `23`)  
  Its measured value; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Recycled content**  
  A measured property of the item.
- `Item/AdditionalItemProperty/ValueQuantity` = **100** (unitCode `P1`)  
  Its measured value; item granulate-pe of Rinova Recovery (world/items.json).
- `Item/EnvironmentalCertificate/ID` = **XU-RC-2026-007**  
  The number of the environmental certificate.
- `Item/EnvironmentalCertificate/CertificateTypeCode` = **Recycledcontent**  
  The kind of claim, as a code.
- `Item/EnvironmentalCertificate/CertificateType` = **Recycled content**  
  The environmental claim certified.
- `Item/EnvironmentalCertificate/Remarks` = **Made entirely from sorted production waste recovered in Urvania.**  
  What the certificate states.
- `Price/PriceAmount` = **83200** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:plastics</cbc:ProfileID>
  <cbc:ProfileExecutionID>PLASTICS-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>RR-INV-26-0894</cbc:ID>
  <cbc:UUID>462dcfae-0a9f-5692-9219-92c1bf595e5d</cbc:UUID>
  <cbc:IssueDate>2026-04-20</cbc:IssueDate>
  <cbc:IssueTime>11:20:00</cbc:IssueTime>
  <cbc:DueDate>2026-05-20</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:Note>Carriage paid to: the price includes the barge to the river quay.</cbc:Note>
  <cbc:TaxPointDate>2026-04-20</cbc:TaxPointDate>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cbc:PaymentCurrencyCode>XUF</cbc:PaymentCurrencyCode>
  <cbc:AccountingCostCode>1300</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw materials</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode>en</cbc:DefaultLanguageCode>
  <cac:OrderReference>
    <cbc:ID>RP-PO-26-0882</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>RR-DA-26-0892</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.rinova.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3830</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via del Riciclo</cbc:StreetName>
        <cbc:BuildingNumber>31</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4140</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
        <cbc:CompanyID>XU007318479</cbc:CompanyID>
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
        <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104548</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
        <cbc:Name>Customer service</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4140 4548</cbc:Telephone>
        <cbc:ElectronicMail>customer@rinova.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:PartyAuthorization>
        <cbc:Purpose>Recovery of non-hazardous plastic waste</cbc:Purpose>
        <cac:ValidityPeriod>
          <cbc:EndDate>2029-12-31</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:Certificate>
          <cbc:ID>XU-ENV-2024-0311</cbc:ID>
          <cbc:CertificateTypeCode>Permit</cbc:CertificateTypeCode>
          <cbc:CertificateType>Operating permit</cbc:CertificateType>
        </cac:Certificate>
      </cac:PartyAuthorization>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.rivermouth.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">2220</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Estuary Road</cbc:StreetName>
        <cbc:BuildingNumber>28</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38505</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
        <cbc:CompanyID>CO-1238220</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20412740</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 3850 2740</cbc:Telephone>
        <cbc:ElectronicMail>order@rivermouth.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-05-20</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>TRADE-ACCORD-PAY</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF89RRINV260894</cbc:InstructionNote>
    <cbc:PaymentID>RF89RRINV260894</cbc:PaymentID>
    <cbc:ChargeBearerCode>SHAR</cbc:ChargeBearerCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU45CREV0000418916</cbc:ID>
      <cbc:Name>Rinova Recovery SRU</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice RR-INV-26-0894</cbc:PaymentNote>
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
  <cac:PaymentTerms>
    <cbc:ID>XU-STD</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>30 days net; 2 % discount when paid within 10 days.</cbc:Note>
    <cbc:SettlementDiscountPercent>2</cbc:SettlementDiscountPercent>
    <cbc:SettlementDiscountAmount currencyID="XUF">199680</cbc:SettlementDiscountAmount>
    <cbc:PaymentTermsDetailsURI>https://www.rinova.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-05-20</cbc:PaymentDueDate>
    <cac:SettlementPeriod>
      <cbc:StartDate>2026-04-20</cbc:StartDate>
      <cbc:EndDate>2026-04-30</cbc:EndDate>
    </cac:SettlementPeriod>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>8</cbc:InterestRatePercent>
      <cbc:TimeBasisCode>Year</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode>Simple</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">0</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">9984000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">0</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XU-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export of goods outside Urvania</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">9984000</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XUF">9984000</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XUF">9984000</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XUF">9984000</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="TNE">120</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XUF">9984000</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.</cbc:Description>
      <cbc:Name>Recycled PE granulate</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>RR-PE-R1</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771030000048</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">3901.10</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XU-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export of goods outside Urvania</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode>Goods</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
      <cac:AdditionalItemProperty>
        <cbc:Name>Density</cbc:Name>
        <cbc:ValueQuantity unitCode="23">0.92</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Recycled content</cbc:Name>
        <cbc:ValueQuantity unitCode="P1">100</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
      <cac:EnvironmentalCertificate>
        <cbc:ID>XU-RC-2026-007</cbc:ID>
        <cbc:CertificateTypeCode>Recycledcontent</cbc:CertificateTypeCode>
        <cbc:CertificateType>Recycled content</cbc:CertificateType>
        <cbc:Remarks>Made entirely from sorted production waste recovered in Urvania.</cbc:Remarks>
      </cac:EnvironmentalCertificate>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XUF">83200</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
