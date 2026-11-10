# Debit Note: Velumi Trading to Lumeway Distribution

*Example 28 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Debit Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DEBIT-NOTE-SCHEMA)*

One pallet's heat-treatment mark was illegible, so customs inspected the container; the buyer debits the distributor in coral for the inspection and storage, a packaging fault on the seller's side.

[The XML file](28-DebitNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:sea**  
  The business process the document belongs to: the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VT-DOC-26-0153**  
  The buyer's debit note number.
- `UUID` = **4ac9595a-73a2-5f50-8296-73f9fae827e7**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-22**  
  After customs charged the inspection.
- `IssueTime` = **10:30:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-06-21**  
  Thirty days.
- `Note` = **The illegible mark is the packer's responsibility under the agreement.**  
  Why the seller pays.
- `DebitNoteTypeCode` = **383**  
  UN/EDIFACT 1001 code 383: debit note.
- `TaxPointDate` = **2026-05-20**  
  The day the fee was charged.
- `DocumentCurrencyCode` = **XLC**  
  The coral, the buyer's currency, in which customs charged; it has three decimals.
- `TaxCurrencyCode` = **XLC**  
  No tax, but stated in the island's currency.
- `PricingCurrencyCode` = **XLC**  
  The fee is priced in coral.
- `PaymentCurrencyCode` = **XBL**  
  The distributor pays in lume.
- `PaymentAlternativeCurrencyCode` = **XLC**  
  The amount in coral, for comparison.
- `AccountingCostCode` = **500**  
  The buyer's cost centre.
- `AccountingCost` = **Stock for municipal projects**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  One line.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-05-18**  
  Held from discharge
- `EndDate` = **2026-05-19**  
  to release.

### Discrepancy Response

Inside `DiscrepancyResponse`:

- `ResponseCode` = **Packaging**  
  A packaging fault.
- `Description` = **Heat-treatment mark illegible on pallet LD-26-007.**  
  The fault.

### Order Reference

Inside `OrderReference`:

- `ID` = **VT-PO-26-0127**  
  The order.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **LD-DA-26-0145**  
  The despatch advice.

### Delivery Note Document Reference

Inside `DeliveryNoteDocumentReference`:

- `ID` = **TOL-BL-26-0139**  
  The bill of lading, the note the goods came with.

### Work Report Document Reference

Inside `WorkReportDocumentReference`:

- `ID` = **XL-CUS-INSP-26-0517**  
  Customs' inspection report.

### Receipt Document Reference

Inside `ReceiptDocumentReference`:

- `ID` = **NW-RA-26-0146**  
  The receipt advice.

### Statement Document Reference

Inside `StatementDocumentReference`:

- `ID` = **HF-ST-26-0150**  
  The factor's statement, which this debit does not touch.

### Originator Document Reference

Inside `OriginatorDocumentReference`:

- `ID` = **VT-CLAIM-26-0021**  
  The buyer's claim.

### Contract Document Reference

Inside `ContractDocumentReference`:

- `ID` = **LD-DAG-26-0125**  
  The digital agreement.

### Project Reference

Inside `ProjectReference`:

- `ID` = **Harbour parks Selanu**  
  The buyer's project.
- `UUID` = **46229671-46ba-571a-9284-46d0fb2b78c1**  
  Its UUID.
- `IssueDate` = **2026-05-07**  
  Started with the order.
- `WorkPhaseReference/ID` = **PH-1**  
  Benches for the harbour park.
- `WorkPhaseReference/WorkPhaseCode` = **Supply**  
  The supply phase.

### Buyer Assigned Reference

Inside `BuyerAssignedReference`:

- `BuyerReferenceCode` = **LD-AP-CLAIMS**  
  The distributor's claims desk.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **TWLU4120872**  
  The container the charge is about.

### Annotation

Inside `Annotation`:

- `AnnotationContent` = **The distributor may claim it from the packer.**  
  A remark.

### Signature

Inside `Signature`:

- `ID` = **VT-SIG-26-DN**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `Party/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
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
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 0274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `Party/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Party/PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Party/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payee Party

Inside `PayeeParty`:

- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.

### Delivery

Inside `Delivery`:

- `ActualDeliveryDate` = **2026-05-21**  
  The goods' arrival at the 3PL.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CIF** (schemeID `INCOTERMS`)  
  As sold.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-06-21**  
  When the transfer must be credited.
- `PaymentChannelCode` = **IBAN**  
  Paid to an account identified in the format of ISO 13616.
- `PaymentRailID` = **TRADE-ACCORD-PAY**  
  The payment system the transfer runs over: the trade accord's link between the countries.
- `InstructionNote` = **Quote RF75VTDOC260153**  
  What the payer writes in the transfer.
- `PaymentID` = **RF75VTDOC260153**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `ChargeBearerCode` = **SHAR**  
  ISO 20022 SHAR: each side pays its own bank's charges.
- `PayeeFinancialAccount/ID` = **XL13BSEL0003665515** (schemeID `urn:ubl-examples:world:account`)  
  The buyer's account. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Velumi Trading Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XLC**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice VT-DOC-26-0153**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **BSEL-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSEL**  
  The bank code, the part of every account number that names the bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Selanu**  
  The bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Reef Street**  
  The bank's head office; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **23**  
  Its building number; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Selanu**  
  Its town; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XL**  
  The bank's country.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Selanu**  
  The branch is at the bank's head office.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XL**  
  Its country.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XL**  
  The country where the account is kept.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **30 days net.**  
  The terms.

### Tax Exchange Rate

Inside `TaxExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The debit note's currency.
- `TargetCurrencyCode` = **XLC**  
  No conversion: the tax currency is coral.
- `CalculationRate` = **1**  
  The same currency.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate gives lume.
- `Date` = **2026-05-22**  
  The rate of the issue date.

### Pricing Exchange Rate

Inside `PricingExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The debit note's currency.
- `TargetCurrencyCode` = **XLC**  
  Priced in coral.
- `CalculationRate` = **1**  
  The same currency.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate gives lume.
- `Date` = **2026-05-22**  
  The rate of the issue date.

### Payment Exchange Rate

Inside `PaymentExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The debit note's currency.
- `TargetCurrencyCode` = **XBL**  
  The distributor's currency.
- `CalculationRate` = **2.5**  
  1 coral = 2.5 lume, the reference rate.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate gives lume.
- `Date` = **2026-05-22**  
  The rate of the issue date.

### Payment Alternative Exchange Rate

Inside `PaymentAlternativeExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The debit note's currency.
- `TargetCurrencyCode` = **XLC**  
  The coral equivalent.
- `CalculationRate` = **1**  
  The same.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate gives lume.
- `Date` = **2026-05-22**  
  The rate of the issue date.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `TaxSubtotal/TaxableAmount` = **51.250** (currencyID `XLC`)  
  The debit.
- `TaxSubtotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  None.
- `TaxSubtotal/TaxCategory/ID` = **O**  
  Lisavu has no sales tax: no tax applies (category O).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **51.250** (currencyID `XLC`)  
  The line.
- `TaxExclusiveAmount` = **51.250** (currencyID `XLC`)  
  No tax.
- `PayableAmount` = **51.250** (currencyID `XLC`)  
  Payable; 128.13 lume at the rate.
- `PayableAlternativeAmount` = **128.13** (currencyID `XBL`)  
  The same in lume.

### Debit Note Line

Inside `DebitNoteLine`:

- `ID` = **1**  
  The inspection.
- `UUID` = **5c8d9fe8-7400-5393-836e-91e7de617c83**  
  Its UUID.
- `Note` = **Customs inspection of the container at Selanu.**  
  What is charged.
- `DebitedQuantity` = **1** (unitCode `E48`)  
  One inspection.
- `LineExtensionAmount` = **51.250** (currencyID `XLC`)  
  Inspection and storage, as customs charged them.
- `TaxInclusiveLineExtensionAmount` = **51.250** (currencyID `XLC`)  
  No tax on the island.
- `TaxPointDate` = **2026-05-20**  
  The day customs charged the fee.
- `AccountingCostCode` = **500**  
  The buyer's cost centre that paid customs.
- `AccountingCost` = **Stock for municipal projects**  
  The cost centre in words.
- `PaymentPurposeCode` = **GOVT**  
  ISO 20022 purpose code GOVT: a payment to the government, recharged.
- `FreeOfChargeIndicator` = **false**  
  Charged.
- `InvoicePeriod/StartDate` = **2026-05-18**  
  The container was held
- `InvoicePeriod/EndDate` = **2026-05-19**  
  for a day.
- `OrderLineReference/LineID` = **1**  
  The benches' order line.
- `DespatchLineReference/LineID` = **1**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **LD-DA-26-0145**  
  The despatch advice.
- `ReceiptLineReference/LineID` = **1**  
  The receipt line.
- `ReceiptLineReference/DocumentReference/ID` = **NW-RA-26-0146**  
  The receipt advice.
- `WorkReportLineReference/LineID` = **1**  
  The inspection report's line.
- `WorkReportLineReference/DocumentReference/ID` = **XL-CUS-INSP-26-0517**  
  Customs' inspection report.
- `BillingReference/InvoiceDocumentReference/ID` = **LD-INV-26-0147**  
  The goods' invoice.
- `DocumentReference/ID` = **XL-CUS-RCPT-26-0517**  
  Customs' receipt for the fee.
- `PricingReference/AlternativeConditionPrice/PriceAmount` = **51.25** (currencyID `XLC`)  
  The fee as customs set it.
- `OriginatorParty/PartyIdentification/ID` = **IC41448** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `OriginatorParty/PartyName/Name` = **Island Customs Service**  
  A party referred to from another party's details: its identifier and name are enough.
- `CollectedForParty/PartyIdentification/ID` = **IC41448** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `CollectedForParty/PartyName/Name` = **Island Customs Service**  
  A party referred to from another party's details: its identifier and name are enough.
- `PaymentTerms/Note` = **Pay within 30 days.**  
  When.
- `TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax.
- `AllowanceCharge/ChargeIndicator` = **true**  
  The storage, a charge on the line.
- `AllowanceCharge/AllowanceChargeReason` = **Storage while held**  
  In words.
- `AllowanceCharge/Amount` = **12.750** (currencyID `XLC`)  
  One day's storage.
- `AllowanceCharge/BaseAmount` = **38.500** (currencyID `XLC`)  
  The inspection fee.
- `Item/Name` = **Customs inspection of container TWLU4120872**  
  What is debited.
- `Price/PriceAmount` = **38.5** (currencyID `XLC`)  
  The fee.
- `DeliveryTerms/ID` = **CIF** (schemeID `INCOTERMS`)  
  As the goods were sold.
- `SubDebitNoteLine/ID` = **1.1**  
  The inspection fee.
- `SubDebitNoteLine/LineExtensionAmount` = **38.500** (currencyID `XLC`)  
  Customs' fee.
- `SubDebitNoteLine/Item/Name` = **Customs inspection fee**  
  What.
- `SubDebitNoteLine/ID` = **1.2**  
  The storage.
- `SubDebitNoteLine/LineExtensionAmount` = **12.750** (currencyID `XLC`)  
  One day.
- `SubDebitNoteLine/Item/Name` = **Storage at the port**  
  What.
- `ItemPriceExtension/Amount` = **51.250** (currencyID `XLC`)  
  The line's price.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DebitNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:DebitNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VT-DOC-26-0153</cbc:ID>
  <cbc:UUID>4ac9595a-73a2-5f50-8296-73f9fae827e7</cbc:UUID>
  <cbc:IssueDate>2026-05-22</cbc:IssueDate>
  <cbc:IssueTime>10:30:00</cbc:IssueTime>
  <cbc:DueDate>2026-06-21</cbc:DueDate>
  <cbc:Note>The illegible mark is the packer's responsibility under the agreement.</cbc:Note>
  <cbc:DebitNoteTypeCode>383</cbc:DebitNoteTypeCode>
  <cbc:TaxPointDate>2026-05-20</cbc:TaxPointDate>
  <cbc:DocumentCurrencyCode>XLC</cbc:DocumentCurrencyCode>
  <cbc:TaxCurrencyCode>XLC</cbc:TaxCurrencyCode>
  <cbc:PricingCurrencyCode>XLC</cbc:PricingCurrencyCode>
  <cbc:PaymentCurrencyCode>XBL</cbc:PaymentCurrencyCode>
  <cbc:PaymentAlternativeCurrencyCode>XLC</cbc:PaymentAlternativeCurrencyCode>
  <cbc:AccountingCostCode>500</cbc:AccountingCostCode>
  <cbc:AccountingCost>Stock for municipal projects</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-05-18</cbc:StartDate>
    <cbc:EndDate>2026-05-19</cbc:EndDate>
  </cac:InvoicePeriod>
  <cac:DiscrepancyResponse>
    <cbc:ResponseCode>Packaging</cbc:ResponseCode>
    <cbc:Description>Heat-treatment mark illegible on pallet LD-26-007.</cbc:Description>
  </cac:DiscrepancyResponse>
  <cac:OrderReference>
    <cbc:ID>VT-PO-26-0127</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>LD-DA-26-0145</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:DeliveryNoteDocumentReference>
    <cbc:ID>TOL-BL-26-0139</cbc:ID>
  </cac:DeliveryNoteDocumentReference>
  <cac:WorkReportDocumentReference>
    <cbc:ID>XL-CUS-INSP-26-0517</cbc:ID>
  </cac:WorkReportDocumentReference>
  <cac:ReceiptDocumentReference>
    <cbc:ID>NW-RA-26-0146</cbc:ID>
  </cac:ReceiptDocumentReference>
  <cac:StatementDocumentReference>
    <cbc:ID>HF-ST-26-0150</cbc:ID>
  </cac:StatementDocumentReference>
  <cac:OriginatorDocumentReference>
    <cbc:ID>VT-CLAIM-26-0021</cbc:ID>
  </cac:OriginatorDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>LD-DAG-26-0125</cbc:ID>
  </cac:ContractDocumentReference>
  <cac:ProjectReference>
    <cbc:ID>Harbour parks Selanu</cbc:ID>
    <cbc:UUID>46229671-46ba-571a-9284-46d0fb2b78c1</cbc:UUID>
    <cbc:IssueDate>2026-05-07</cbc:IssueDate>
    <cac:WorkPhaseReference>
      <cbc:ID>PH-1</cbc:ID>
      <cbc:WorkPhaseCode>Supply</cbc:WorkPhaseCode>
    </cac:WorkPhaseReference>
  </cac:ProjectReference>
  <cac:BuyerAssignedReference>
    <cbc:BuyerReferenceCode>LD-AP-CLAIMS</cbc:BuyerReferenceCode>
  </cac:BuyerAssignedReference>
  <cac:PurchaseReference>
    <cbc:ID>TWLU4120872</cbc:ID>
  </cac:PurchaseReference>
  <cac:Annotation>
    <cbc:AnnotationContent>The distributor may claim it from the packer.</cbc:AnnotationContent>
  </cac:Annotation>
  <cac:Signature>
    <cbc:ID>VT-SIG-26-DN</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Distribution Drive</cbc:StreetName>
        <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
        <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
        <cbc:BuildingNumber>43</cbc:BuildingNumber>
        <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71214</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
        <cbc:CompanyID>UL-1230822</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20410274</cbc:CompanyID>
        <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Medium</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Marrowdale</cbc:CityName>
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
        <cbc:Name>Customer service</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 0274</cbc:Telephone>
        <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.velumi.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName>Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC41859</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 3000 1859</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:PayeeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
  </cac:PayeeParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cbc:ActualDeliveryDate>2026-05-21</cbc:ActualDeliveryDate>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CIF</cbc:ID>
  </cac:DeliveryTerms>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-06-21</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>TRADE-ACCORD-PAY</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF75VTDOC260153</cbc:InstructionNote>
    <cbc:PaymentID>RF75VTDOC260153</cbc:PaymentID>
    <cbc:ChargeBearerCode>SHAR</cbc:ChargeBearerCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL13BSEL0003665515</cbc:ID>
      <cbc:Name>Velumi Trading Ltd</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XLC</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice VT-DOC-26-0153</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>BSEL-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>BSEL</cbc:ID>
          <cbc:Name>Bank of Selanu</cbc:Name>
          <cac:Address>
            <cbc:StreetName>Reef Street</cbc:StreetName>
            <cbc:BuildingNumber>23</cbc:BuildingNumber>
            <cbc:CityName>Selanu</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
        <cac:Address>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:Note>30 days net.</cbc:Note>
  </cac:PaymentTerms>
  <cac:TaxExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-22</cbc:Date>
  </cac:TaxExchangeRate>
  <cac:PricingExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-22</cbc:Date>
  </cac:PricingExchangeRate>
  <cac:PaymentExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XBL</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>2.5</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-22</cbc:Date>
  </cac:PaymentExchangeRate>
  <cac:PaymentAlternativeExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-22</cbc:Date>
  </cac:PaymentAlternativeExchangeRate>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">51.250</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cac:TaxScheme>
          <cbc:Name>No general sales tax</cbc:Name>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">51.250</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">51.250</cbc:TaxExclusiveAmount>
    <cbc:PayableAmount currencyID="XLC">51.250</cbc:PayableAmount>
    <cbc:PayableAlternativeAmount currencyID="XBL">128.13</cbc:PayableAlternativeAmount>
  </cac:LegalMonetaryTotal>
  <cac:DebitNoteLine>
    <cbc:ID>1</cbc:ID>
    <cbc:UUID>5c8d9fe8-7400-5393-836e-91e7de617c83</cbc:UUID>
    <cbc:Note>Customs inspection of the container at Selanu.</cbc:Note>
    <cbc:DebitedQuantity unitCode="E48">1</cbc:DebitedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">51.250</cbc:LineExtensionAmount>
    <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">51.250</cbc:TaxInclusiveLineExtensionAmount>
    <cbc:TaxPointDate>2026-05-20</cbc:TaxPointDate>
    <cbc:AccountingCostCode>500</cbc:AccountingCostCode>
    <cbc:AccountingCost>Stock for municipal projects</cbc:AccountingCost>
    <cbc:PaymentPurposeCode>GOVT</cbc:PaymentPurposeCode>
    <cbc:FreeOfChargeIndicator>false</cbc:FreeOfChargeIndicator>
    <cac:InvoicePeriod>
      <cbc:StartDate>2026-05-18</cbc:StartDate>
      <cbc:EndDate>2026-05-19</cbc:EndDate>
    </cac:InvoicePeriod>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>LD-DA-26-0145</cbc:ID>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
    <cac:ReceiptLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>NW-RA-26-0146</cbc:ID>
      </cac:DocumentReference>
    </cac:ReceiptLineReference>
    <cac:WorkReportLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>XL-CUS-INSP-26-0517</cbc:ID>
      </cac:DocumentReference>
    </cac:WorkReportLineReference>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>LD-INV-26-0147</cbc:ID>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
    <cac:DocumentReference>
      <cbc:ID>XL-CUS-RCPT-26-0517</cbc:ID>
    </cac:DocumentReference>
    <cac:PricingReference>
      <cac:AlternativeConditionPrice>
        <cbc:PriceAmount currencyID="XLC">51.25</cbc:PriceAmount>
      </cac:AlternativeConditionPrice>
    </cac:PricingReference>
    <cac:OriginatorParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41448</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Island Customs Service</cbc:Name>
      </cac:PartyName>
    </cac:OriginatorParty>
    <cac:CollectedForParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41448</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Island Customs Service</cbc:Name>
      </cac:PartyName>
    </cac:CollectedForParty>
    <cac:PaymentTerms>
      <cbc:Note>Pay within 30 days.</cbc:Note>
    </cac:PaymentTerms>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Storage while held</cbc:AllowanceChargeReason>
      <cbc:Amount currencyID="XLC">12.750</cbc:Amount>
      <cbc:BaseAmount currencyID="XLC">38.500</cbc:BaseAmount>
    </cac:AllowanceCharge>
    <cac:Item>
      <cbc:Name>Customs inspection of container TWLU4120872</cbc:Name>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">38.5</cbc:PriceAmount>
    </cac:Price>
    <cac:DeliveryTerms>
      <cbc:ID schemeID="INCOTERMS">CIF</cbc:ID>
    </cac:DeliveryTerms>
    <cac:SubDebitNoteLine>
      <cbc:ID>1.1</cbc:ID>
      <cbc:LineExtensionAmount currencyID="XLC">38.500</cbc:LineExtensionAmount>
      <cac:Item>
        <cbc:Name>Customs inspection fee</cbc:Name>
      </cac:Item>
    </cac:SubDebitNoteLine>
    <cac:SubDebitNoteLine>
      <cbc:ID>1.2</cbc:ID>
      <cbc:LineExtensionAmount currencyID="XLC">12.750</cbc:LineExtensionAmount>
      <cac:Item>
        <cbc:Name>Storage at the port</cbc:Name>
      </cac:Item>
    </cac:SubDebitNoteLine>
    <cac:ItemPriceExtension>
      <cbc:Amount currencyID="XLC">51.250</cbc:Amount>
    </cac:ItemPriceExtension>
  </cac:DebitNoteLine>
</DebitNote>
```
