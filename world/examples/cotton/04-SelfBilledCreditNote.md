# Self Billed Credit Note: Selanu Cotton Ginnery to Lisavu Cotton Farm

*Example 4 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Self Billed Credit Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-SELF-BILLED-CREDIT-NOTE-SCHEMA)*

Classing after ginning puts part of the delivery a grade lower; the ginnery credits the difference on the farm's behalf.

[The XML file](04-SelfBilledCreditNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:cotton**  
  The business process the document belongs to: the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)".
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SCG-SBC-26-0194**  
  The number the customer gives the self-billed document, under the self-billing agreement.
- `UUID` = **3fe47b86-e662-5cb9-93d0-9366b17fb485**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-14**  
  Issued after classing showed part of the delivery a grade lower.
- `IssueTime` = **15:50:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-02-16**  
  Set off on the day of payment.
- `TaxPointDate` = **2026-02-14**  
  The day the withholding becomes due.
- `CreditNoteTypeCode` = **261**  
  UN/EDIFACT 1001 code 261: self-billed credit note.
- `Note` = **Lakau-votee tetela tamasu tilala kimii mitavema.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): As required on every self-billed document.
- `Note` = **Self-billed credit note under the season agreement.** (languageID `en`)  
  The same note in English, the working language between the countries: As required on every self-billed document.
- `DocumentCurrencyCode` = **XLC**  
  The coral, the supplier's currency; it has three decimals.
- `TaxCurrencyCode` = **XLC**  
  The presumptive tax is paid to the island's tax office in coral.
- `PricingCurrencyCode` = **XBL**  
  Seed cotton is priced from the trade accord's lint reference price, published in lume.
- `PaymentCurrencyCode` = **XLC**  
  The farm is paid in coral.
- `PaymentAlternativeCurrencyCode` = **XBL**  
  The farm may ask to be paid in lume, to its account in Bayvarra, where it buys its machinery.
- `AccountingCostCode` = **200**  
  The customer's own cost centre: it books what it billed itself.
- `AccountingCost` = **Seed cotton purchases**  
  The cost centre in words.
- `LineCountNumeric` = **2**  
  The price difference and the levy on it.
- `DefaultLanguageCode` = **en**  
  The language of the texts.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-02-03**  
  The deliveries classed, from the first
- `EndDate` = **2026-02-05**  
  to the last trailer.

### Discrepancy Response

Inside `DiscrepancyResponse`:

- `ReferenceID` = **1**  
  The line of the self-billed invoice.
- `ResponseCode` = **Grade**  
  The classing found a lower grade.
- `Description` = **2,500 kg classed Strict Low Middling instead of Middling.**  
  In words.

### Order Reference

Inside `OrderReference`:

- `ID` = **SCG-SEASON-2026/03**  
  The call-off.

### Billing Reference

Inside `BillingReference`:

- `SelfBilledInvoiceDocumentReference/ID` = **SCG-SBI-26-0193**  
  The self-billed invoice this corrects.
- `SelfBilledInvoiceDocumentReference/IssueDate` = **2026-02-07**  
  Its issue date.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **LCF-DN-26-0192**  
  The farm's delivery note.

### Delivery Note Document Reference

Inside `DeliveryNoteDocumentReference`:

- `ID` = **LCF-DN-26-0192**  
  The delivery classed.

### Work Report Document Reference

Inside `WorkReportDocumentReference`:

- `ID` = **SCC-CLS-26-0311**  
  The chamber's classing report.

### Receipt Document Reference

Inside `ReceiptDocumentReference`:

- `ID` = **SCG-WB-26-0311**  
  The weighbridge ticket.

### Contract Document Reference

Inside `ContractDocumentReference`:

- `ID` = **SCG-SEASON-2026**  
  The season agreement: it sets the price per grade.

### Statement Document Reference

Inside `StatementDocumentReference`:

- `ID` = **SCG-ACC-LCF-26-02**  
  The gin's season account of the farm (not shown).

### Originator Document Reference

Inside `OriginatorDocumentReference`:

- `ID` = **LTM-SEASON-2026**  
  The mill's season contract with the gin, for which the gin buys the seed cotton.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **XL-CLS-2026-0042**  
  The classing certificate.

### Project Reference

Inside `ProjectReference`:

- `ID` = **SCC-COTTON-QUALITY-26**  
  The chamber's cotton quality programme.

### Buyer Assigned Reference

Inside `BuyerAssignedReference`:

- `BuyerReferenceCode` = **SCG-AP-FARMS**  
  The gin's desk for farm payments.
- `BuyerReference` = **Farm payments**  
  In words.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **LCF-FIELD-07**  
  The field the cotton was picked from, for traceability.

### Annotation

Inside `Annotation`:

- `AnnotationContent` = **Written by the gin on the farm's behalf under the self-billing agreement.**  
  A remark.

### Signature

Inside `Signature`:

- `ID` = **SCG-SIG-SB-02**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.selanuginnery.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/IndustryClassificationCode` = **0163** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42681**  
  Number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Selanu Cotton Ginnery (world/parties.json).
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
- `Party/Contact/Name` = **Cotton sales**  
  The desk that handles this document; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 3000 2681**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/ElectronicMail` = **cotton@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.lisavufarm.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/IndustryClassificationCode` = **0116** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **35**  
  Building number of the postal address. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/Description` = **Farm track off Plantation Road, past the cotton fields.**  
  How to find the farm, which has no house number on a street. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/District` = **North coast**  
  The district of the island, used to find a farm off the main roads. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/AddressLine/Line` = **Lisavu Cotton Farm**  
  The address as the farm writes it, line by line: rural addresses on the island are not fully structured.
- `Party/PostalAddress/AddressLine/Line` = **Plantation Road, kilometre 4**  
  The address as the farm writes it, line by line: rural addresses on the island are not fully structured.
- `Party/PostalAddress/AddressLine/Line` = **North coast, Selanu**  
  The address as the farm writes it, line by line: rural addresses on the island are not fully structured.
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PostalAddress/LocationCoordinate/CoordinateSystemCode` = **WGS84**  
  The World Geodetic System 1984, as used by satellite navigation.
- `Party/PostalAddress/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LatitudeMinutesMeasure` = **58.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PostalAddress/LocationCoordinate/LatitudeDirectionCode` = **South**  
  South of the equator.
- `Party/PostalAddress/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LongitudeMinutesMeasure` = **7.80** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PostalAddress/LocationCoordinate/LongitudeDirectionCode` = **West**  
  West of the Greenwich meridian.
- `Party/PhysicalLocation/Description` = **The cotton fields**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/InformationURI` = **https://www.lisavufarm.example**  
  Where to find more about the place.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **WGS84**  
  The World Geodetic System 1984, as used by satellite navigation.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **58.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South**  
  South of the equator.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **7.80** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West**  
  West of the Greenwich meridian.
- `Party/PartyLegalEntity/RegistrationName` = **Lisavu Cotton Farm**  
  The name under which the party is registered, with its legal form; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42544**  
  Number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **2009-08-17**  
  The day the company was entered in the register; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/RegistrationExpirationDate` = **2026-12-31**  
  The island renews a farm's registration every year: it runs until this date.
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SP**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Sole proprietorship**  
  The legal form, in words.
- `Party/PartyLegalEntity/SoleProprietorshipIndicator` = **true**  
  The farm belongs to one farmer, who runs it in their own name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/EntitySizeCode` = **Micro**  
  The size class of the company (micro, small, medium or large); identity of Lisavu Cotton Farm (world/parties.json).
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
- `Party/Contact/Name` = **Farm office**  
  The desk that handles this document; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 3000 2544**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42544** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lisavu Cotton Farm (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payee Party

Inside `PayeeParty`:

- `PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lisavu Cotton Farm**  
  A party referred to from another party's details: its identifier and name are enough.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Tax Representative Party

Inside `TaxRepresentativeParty`:

- `PartyIdentification/ID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Tevaro Customs Brokers**  
  A party referred to from another party's details: its identifier and name are enough.

### Delivery

Inside `Delivery`:

- `ActualDeliveryDate` = **2026-02-05**  
  The delivery classed.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **DAP** (schemeID `INCOTERMS`)  
  As on the self-billed invoice.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **97** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 97: clearing between partners; set off against the payment.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **Set off against the payment of the self-billed invoice.**  
  How the credit is settled.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **false**  
  An allowance: it lowers the credit.
- `AllowanceChargeReason` = **Classing fee**  
  The farm bears the classing of its cotton, as the agreement says.
- `Amount` = **5.000** (currencyID `XLC`)  
  The chamber's fee for the lot.

### Tax Exchange Rate

Inside `TaxExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The document currency.
- `TargetCurrencyCode` = **XLC**  
  The tax currency, coral.
- `CalculationRate` = **1**  
  The same currency: no conversion.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate.
- `Date` = **2026-02-14**  
  Of the document's date.

### Pricing Exchange Rate

Inside `PricingExchangeRate`:

- `SourceCurrencyCode` = **XBL**  
  The reference price's currency.
- `TargetCurrencyCode` = **XLC**  
  The document's.
- `CalculationRate` = **0.4**  
  The reference rate.
- `MathematicOperatorCode` = **Multiply**  
  Lume times the rate gives coral.
- `Date` = **2026-02-14**  
  Of the document's date.

### Payment Exchange Rate

Inside `PaymentExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The document currency.
- `TargetCurrencyCode` = **XLC**  
  The payment currency, coral.
- `CalculationRate` = **1**  
  The same currency: no conversion.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate.
- `Date` = **2026-02-14**  
  Of the document's date.

### Payment Alternative Exchange Rate

Inside `PaymentAlternativeExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The document currency.
- `TargetCurrencyCode` = **XBL**  
  Lume, the alternative.
- `CalculationRate` = **2.5**  
  The reference rate.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate.
- `Date` = **2026-02-14**  
  Of the document's date.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.000** (currencyID `XLC`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **75.000** (currencyID `XLC`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.

### Withholding Tax Total

Inside `WithholdingTaxTotal`:

- `TaxAmount` = **1.500** (currencyID `XLC`)  
  The withholding reversed on the credit.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **75.000** (currencyID `XLC`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **70.000** (currencyID `XLC`)  
  The credit less the fee.
- `TaxInclusiveAmount` = **70.000** (currencyID `XLC`)  
  No tax on the island.
- `AllowanceTotalAmount` = **5.000** (currencyID `XLC`)  
  The classing fee the farm bears.
- `WithholdingTaxTotalAmount` = **1.500** (currencyID `XLC`)  
  The withholding on the credited value, reversed: the value falls in the 2 % tier.
- `PayableAmount` = **69.250** (currencyID `XLC`)  
  What the farm's account is credited: the price difference less the fee and the withholding, plus the levy on it.

### Collection Credit Note Line

Inside `CollectionCreditNoteLine`:

- `ID` = **2**  
  The collection line.
- `Note` = **Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.**  
  Why the line is there.
- `CreditedQuantity` = **1** (unitCode `C62`)  
  The levy, credited once.
- `LineExtensionAmount` = **0.750** (currencyID `XLC`)  
  1 % of the value of the seed cotton.
- `BeneficiaryParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `BeneficiaryParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Name` = **Cotton fund levy**  
  What is collected.

### Credit Note Line

Inside `CreditNoteLine`:

- `ID` = **1**  
  The line number.
- `CreditedQuantity` = **2500** (unitCode `KGM`)  
  The part of the delivery classed lower.
- `LineExtensionAmount` = **75.000** (currencyID `XLC`)  
  Quantity times price, rounded to the minor unit.
- `Item/Description` = **Cotton as harvested, not ginned, delivered loose by trailer.**  
  The seller's description; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Name` = **Votike tekapa** (languageID `qal`)  
  The item's name in Lisavan, the seller's language; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Name` = **Seed cotton** (languageID `en`)  
  The item's name in English, the working language between the countries; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/SellersItemIdentification/ID` = **LCF-SC**  
  The seller's own item number; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/StandardItemIdentification/ID` = **773010000123** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XL**  
  Where the item was produced; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **5201.00** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `Price/PriceAmount` = **0.03** (currencyID `XLC`)  
  The price difference between the agreed grade and the lower grade, per kilogram.
- `Price/BaseQuantity` = **1** (unitCode `KGM`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<SelfBilledCreditNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:SelfBilledCreditNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:cotton</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SCG-SBC-26-0194</cbc:ID>
  <cbc:UUID>3fe47b86-e662-5cb9-93d0-9366b17fb485</cbc:UUID>
  <cbc:IssueDate>2026-02-14</cbc:IssueDate>
  <cbc:IssueTime>15:50:00</cbc:IssueTime>
  <cbc:DueDate>2026-02-16</cbc:DueDate>
  <cbc:TaxPointDate>2026-02-14</cbc:TaxPointDate>
  <cbc:CreditNoteTypeCode>261</cbc:CreditNoteTypeCode>
  <cbc:Note languageID="qal">Lakau-votee tetela tamasu tilala kimii mitavema.</cbc:Note>
  <cbc:Note languageID="en">Self-billed credit note under the season agreement.</cbc:Note>
  <cbc:DocumentCurrencyCode>XLC</cbc:DocumentCurrencyCode>
  <cbc:TaxCurrencyCode>XLC</cbc:TaxCurrencyCode>
  <cbc:PricingCurrencyCode>XBL</cbc:PricingCurrencyCode>
  <cbc:PaymentCurrencyCode>XLC</cbc:PaymentCurrencyCode>
  <cbc:PaymentAlternativeCurrencyCode>XBL</cbc:PaymentAlternativeCurrencyCode>
  <cbc:AccountingCostCode>200</cbc:AccountingCostCode>
  <cbc:AccountingCost>Seed cotton purchases</cbc:AccountingCost>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode>en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-02-03</cbc:StartDate>
    <cbc:EndDate>2026-02-05</cbc:EndDate>
  </cac:InvoicePeriod>
  <cac:DiscrepancyResponse>
    <cbc:ReferenceID>1</cbc:ReferenceID>
    <cbc:ResponseCode>Grade</cbc:ResponseCode>
    <cbc:Description>2,500 kg classed Strict Low Middling instead of Middling.</cbc:Description>
  </cac:DiscrepancyResponse>
  <cac:OrderReference>
    <cbc:ID>SCG-SEASON-2026/03</cbc:ID>
  </cac:OrderReference>
  <cac:BillingReference>
    <cac:SelfBilledInvoiceDocumentReference>
      <cbc:ID>SCG-SBI-26-0193</cbc:ID>
      <cbc:IssueDate>2026-02-07</cbc:IssueDate>
    </cac:SelfBilledInvoiceDocumentReference>
  </cac:BillingReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>LCF-DN-26-0192</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:DeliveryNoteDocumentReference>
    <cbc:ID>LCF-DN-26-0192</cbc:ID>
  </cac:DeliveryNoteDocumentReference>
  <cac:WorkReportDocumentReference>
    <cbc:ID>SCC-CLS-26-0311</cbc:ID>
  </cac:WorkReportDocumentReference>
  <cac:ReceiptDocumentReference>
    <cbc:ID>SCG-WB-26-0311</cbc:ID>
  </cac:ReceiptDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>SCG-SEASON-2026</cbc:ID>
  </cac:ContractDocumentReference>
  <cac:StatementDocumentReference>
    <cbc:ID>SCG-ACC-LCF-26-02</cbc:ID>
  </cac:StatementDocumentReference>
  <cac:OriginatorDocumentReference>
    <cbc:ID>LTM-SEASON-2026</cbc:ID>
  </cac:OriginatorDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>XL-CLS-2026-0042</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:ProjectReference>
    <cbc:ID>SCC-COTTON-QUALITY-26</cbc:ID>
  </cac:ProjectReference>
  <cac:BuyerAssignedReference>
    <cbc:BuyerReferenceCode>SCG-AP-FARMS</cbc:BuyerReferenceCode>
    <cbc:BuyerReference>Farm payments</cbc:BuyerReference>
  </cac:BuyerAssignedReference>
  <cac:PurchaseReference>
    <cbc:ID>LCF-FIELD-07</cbc:ID>
  </cac:PurchaseReference>
  <cac:Annotation>
    <cbc:AnnotationContent>Written by the gin on the farm's behalf under the self-billing agreement.</cbc:AnnotationContent>
  </cac:Annotation>
  <cac:Signature>
    <cbc:ID>SCG-SIG-SB-02</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.selanuginnery.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">0163</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-042681</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
        <cbc:StreetName languageID="en">Gin Yard Road</cbc:StreetName>
        <cbc:BuildingNumber>42</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Cotton Ginnery Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC42681</cbc:CompanyID>
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
        <cbc:Name>Cotton sales</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 3000 2681</cbc:Telephone>
        <cbc:ElectronicMail>cotton@selanuginnery.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.lisavufarm.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">0116</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Sifatofu Natii</cbc:StreetName>
        <cbc:StreetName languageID="en">Plantation Road</cbc:StreetName>
        <cbc:BuildingNumber>35</cbc:BuildingNumber>
        <cbc:Description>Farm track off Plantation Road, past the cotton fields.</cbc:Description>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:District>North coast</cbc:District>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:AddressLine>
          <cbc:Line>Lisavu Cotton Farm</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Plantation Road, kilometre 4</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>North coast, Selanu</cbc:Line>
        </cac:AddressLine>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">58.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode>South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">7.80</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode>West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>The cotton fields</cbc:Description>
        <cbc:InformationURI>https://www.lisavufarm.example</cbc:InformationURI>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">58.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode>South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">7.80</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode>West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lisavu Cotton Farm</cbc:RegistrationName>
        <cbc:CompanyID>IC42544</cbc:CompanyID>
        <cbc:RegistrationDate>2009-08-17</cbc:RegistrationDate>
        <cbc:RegistrationExpirationDate>2026-12-31</cbc:RegistrationExpirationDate>
        <cbc:CompanyLegalFormCode>SP</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Sole proprietorship</cbc:CompanyLegalForm>
        <cbc:SoleProprietorshipIndicator>true</cbc:SoleProprietorshipIndicator>
        <cbc:EntitySizeCode>Micro</cbc:EntitySizeCode>
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
        <cbc:Name>Farm office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 3000 2544</cbc:Telephone>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42544</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:PayeeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lisavu Cotton Farm</cbc:Name>
    </cac:PartyName>
  </cac:PayeeParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:TaxRepresentativeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41585</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tevaro Customs Brokers</cbc:Name>
    </cac:PartyName>
  </cac:TaxRepresentativeParty>
  <cac:Delivery>
    <cbc:ActualDeliveryDate>2026-02-05</cbc:ActualDeliveryDate>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">DAP</cbc:ID>
  </cac:DeliveryTerms>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">97</cbc:PaymentMeansCode>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:Note>Set off against the payment of the self-billed invoice.</cbc:Note>
  </cac:PaymentTerms>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Classing fee</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XLC">5.000</cbc:Amount>
  </cac:AllowanceCharge>
  <cac:TaxExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-14</cbc:Date>
  </cac:TaxExchangeRate>
  <cac:PricingExchangeRate>
    <cbc:SourceCurrencyCode>XBL</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>0.4</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-14</cbc:Date>
  </cac:PricingExchangeRate>
  <cac:PaymentExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-14</cbc:Date>
  </cac:PaymentExchangeRate>
  <cac:PaymentAlternativeExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XBL</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>2.5</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-14</cbc:Date>
  </cac:PaymentAlternativeExchangeRate>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">75.000</cbc:TaxableAmount>
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
  <cac:WithholdingTaxTotal>
    <cbc:TaxAmount currencyID="XLC">1.500</cbc:TaxAmount>
  </cac:WithholdingTaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">75.000</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">70.000</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">70.000</cbc:TaxInclusiveAmount>
    <cbc:AllowanceTotalAmount currencyID="XLC">5.000</cbc:AllowanceTotalAmount>
    <cbc:WithholdingTaxTotalAmount currencyID="XLC">1.500</cbc:WithholdingTaxTotalAmount>
    <cbc:PayableAmount currencyID="XLC">69.250</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:CollectionCreditNoteLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.</cbc:Note>
    <cbc:CreditedQuantity unitCode="C62">1</cbc:CreditedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">0.750</cbc:LineExtensionAmount>
    <cac:BeneficiaryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:BeneficiaryParty>
    <cac:Item>
      <cbc:Name>Cotton fund levy</cbc:Name>
    </cac:Item>
  </cac:CollectionCreditNoteLine>
  <cac:CreditNoteLine>
    <cbc:ID>1</cbc:ID>
    <cbc:CreditedQuantity unitCode="KGM">2500</cbc:CreditedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">75.000</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Cotton as harvested, not ginned, delivered loose by trailer.</cbc:Description>
      <cbc:Name languageID="qal">Votike tekapa</cbc:Name>
      <cbc:Name languageID="en">Seed cotton</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>LCF-SC</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">773010000123</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">5201.00</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:SupplyTypeCode>Goods</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:Name>No general sales tax</cbc:Name>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">0.03</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:CreditNoteLine>
</SelfBilledCreditNote>
```
