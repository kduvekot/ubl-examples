# Self Billed Invoice: Selanu Cotton Ginnery to Lisavu Cotton Farm

*Example 3 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Self Billed Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-SELF-BILLED-INVOICE-SCHEMA)*

Under the self-billing agreement the ginnery writes the farm's invoice from the weight and grade it measured. No tax on the island, stated as such.

[The XML file](03-SelfBilledInvoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **SCG-SBI-26-0193**  
  The number the customer gives the self-billed document, under the self-billing agreement.
- `UUID` = **da6a76fb-cc8f-56c6-bea6-296a7804c3c9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-07**  
  The ginnery bills itself for the delivery, as the self-billing agreement provides.
- `IssueTime` = **14:29:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-03-24**  
  The supplier's usual term, which the customer applies to itself.
- `TaxPointDate` = **2026-02-07**  
  The day the withholding becomes due.
- `InvoiceTypeCode` = **389**  
  UN/EDIFACT 1001 code 389: self-billed invoice.
- `Note` = **Lakau-votee tilala kimii mitavema: sehove kulasi tohala lelala tanaha hokake.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): The statement the self-billing agreement requires on every invoice.
- `Note` = **Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.** (languageID `en`)  
  The same note in English, the working language between the countries: The statement the self-billing agreement requires on every invoice.
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
  The seed cotton and the collection line of the levy.
- `DefaultLanguageCode` = **en**  
  The language of the texts.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-02-03**  
  The week of the deliveries.
- `EndDate` = **2026-02-05**  
  The last trailer.

### Order Reference

Inside `OrderReference`:

- `ID` = **SCG-SEASON-2026/03**  
  The third call-off under the season agreement.

### Billing Reference

Inside `BillingReference`:

- `AdditionalDocumentReference/ID` = **SCG-ADV-26-0012**  
  The season advance deducted.

### Contract Document Reference

Inside `ContractDocumentReference`:

- `ID` = **SCG-SEASON-2026**  
  The season agreement between farm and ginnery, which allows the self-billing.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **LCF-DN-26-0192**  
  The farm's delivery note.

### Work Report Document Reference

Inside `WorkReportDocumentReference`:

- `ID` = **SCG-OUT-26-0311**  
  The gin's outturn report of the lot.

### Delivery Note Document Reference

Inside `DeliveryNoteDocumentReference`:

- `ID` = **LCF-DN-26-0192**  
  The farm's delivery note.

### Receipt Document Reference

Inside `ReceiptDocumentReference`:

- `ID` = **SCG-WB-26-0311**  
  The weighbridge ticket of the gin.

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

- `ID` = **XL-FARM-REG-0412**  
  The farm's registration, which the withholding needs.

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
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en`)  
  The street's name in English, the country's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
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
- `Party/Contact/Telephone` = **+999 3 721 2681**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Cotton Ginnery (world/parties.json).
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
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en`)  
  The street's name in English, the country's other official language; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/Description` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  How to find the farm, which has no house number on a street. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/District` = **North coast**  
  The district of the island, used to find a farm off the main roads. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/AddressLine/Line` = **Sifatofu Natii / Plantation Road**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **North coast**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
- `Party/PostalAddress/AddressLine/Line` = **Selanu**  
  One line of the address as the farm writes it, made from the fields above in Lisavu's address format (world/countries.json), so that lines and fields agree. A name in both languages is given in both on the line, the national language first.
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
- `Party/Contact/Telephone` = **+999 3 724 2544**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42544** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lisavu Cotton Farm (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Originator Customer Party

Inside `OriginatorCustomerParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Beneficiary Party

Inside `BeneficiaryParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Payee Party

Inside `PayeeParty`:

- `PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lisavu Cotton Farm**  
  A party referred to from another party's details: its identifier and name are enough.

### Tax Representative Party

Inside `TaxRepresentativeParty`:

- `PartyIdentification/ID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Tevaro Customs Brokers**  
  A party referred to from another party's details: its identifier and name are enough.

### Delivery

Inside `Delivery`:

- `ActualDeliveryDate` = **2026-02-05**  
  The trailers were weighed at the gin.
- `DeliveryLocation/Name` = **Selanu Cotton Ginnery, weighbridge**  
  Where.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **DAP** (schemeID `INCOTERMS`)  
  Delivered at the gin: the farm brings the cotton with its own tractor.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-03-24**  
  When the transfer must be credited.
- `PaymentChannelCode` = **IBAN**  
  Paid to an account identified in the format of ISO 13616.
- `PaymentRailID` = **CORAL-NET**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF07SCGSBI260193**  
  What the payer writes in the transfer.
- `PaymentID` = **RF07SCGSBI260193**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `PayeeFinancialAccount/ID` = **XL05BSEL0004817534** (schemeID `urn:ubl-examples:world:account`)  
  The supplier's account, where the customer pays what it billed itself. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Lisavu Cotton Farm**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XLC**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice SCG-SBI-26-0193**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **BSEL-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSEL**  
  The bank code, the part of every account number that names the bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Selanu**  
  The bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
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

- `ID` = **XL-STD**  
  The standard terms of Lisavu.
- `PaymentMeansID` = **1**  
  The payment means these terms apply to: the credit transfer below.
- `Note` = **45 days net.**  
  Island practice: longer terms, simple interest on late payment.
- `PaymentTermsDetailsURI` = **https://www.lisavufarm.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-03-24**  
  The day the amount is due.
- `PenaltyInterestRate/InterestRatePercent` = **6**  
  The interest on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **Year**  
  A yearly rate.
- `PenaltyInterestRate/CalculationMethodCode` = **Simple**  
  Simple interest, per day late.

### Prepaid Payment

Inside `PrepaidPayment`:

- `ID` = **SCG-ADV-26-0012**  
  The season advance to the farm.
- `PaidAmount` = **1000.000** (currencyID `XLC`)  
  Paid before the harvest, against the first deliveries.
- `PaidDate` = **2026-01-13**  
  Three weeks before the deliveries.

### Allowance Charge

Inside `AllowanceCharge`:

- `ID` = **1**  
  The only charge.
- `ChargeIndicator` = **true**  
  A charge in the farm's favour: it adds to what the gin pays.
- `AllowanceChargeReason` = **Haulage allowance**  
  The gin pays the farm for bringing the cotton.
- `PrepaidIndicator` = **false**  
  Not prepaid: paid with the invoice.
- `SequenceNumeric` = **1**  
  Applied after the lines.
- `Amount` = **180.000** (currencyID `XLC`)  
  18,000 kg at 0.010 coral.
- `TaxInclusiveAmount` = **180.000** (currencyID `XLC`)  
  No tax on the island.
- `BaseAmount` = **4068.000** (currencyID `XLC`)  
  The cotton delivered.
- `AccountingCostCode` = **210**  
  The gin's cost centre for haulage.
- `AccountingCost` = **Seed cotton haulage**  
  In words.
- `PerUnitAmount` = **0.010** (currencyID `XLC`)  
  0.010 coral per kilogram.
- `TaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the haulage on the island.
- `PaymentMeans/PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  Credit transfer, with the invoice.

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
- `Date` = **2026-02-07**  
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
- `Date` = **2026-02-07**  
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
- `Date` = **2026-02-07**  
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
- `Date` = **2026-02-07**  
  Of the document's date.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.000** (currencyID `XLC`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **4068.000** (currencyID `XLC`)  
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

- `TaxAmount` = **61.360** (currencyID `XLC`)  
  The presumptive tax the gin withholds on the delivery.
- `TaxSubtotal/TaxableAmount` = **2000.000** (currencyID `XLC`)  
  The part of the value in this tier.
- `TaxSubtotal/TaxAmount` = **20.000** (currencyID `XLC`)  
  1 % of it.
- `TaxSubtotal/Percent` = **1**  
  The rate.
- `TaxSubtotal/TierRange` = **Up to 2,000 coral of the delivery's value**  
  The tier.
- `TaxSubtotal/TierRatePercent` = **1**  
  The rate within the tier.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  The withholding applies.
- `TaxSubtotal/TaxCategory/Percent` = **1**  
  The rate of the tier.
- `TaxSubtotal/TaxCategory/TierRange` = **Up to 2,000 coral of the delivery's value**  
  The tier.
- `TaxSubtotal/TaxCategory/TierRatePercent` = **1**  
  The rate within the tier.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **OTH**  
  UN/EDIFACT 5153 code OTH: other taxes, the presumptive tax.
- `TaxSubtotal/TaxCategory/TaxScheme/Name` = **Presumptive tax on farm produce**  
  The tax in words.
- `TaxSubtotal/TaxableAmount` = **2068.000** (currencyID `XLC`)  
  The part of the value in this tier.
- `TaxSubtotal/TaxAmount` = **41.360** (currencyID `XLC`)  
  2 % of it.
- `TaxSubtotal/Percent` = **2**  
  The rate.
- `TaxSubtotal/TierRange` = **Above 2,000 coral**  
  The tier.
- `TaxSubtotal/TierRatePercent` = **2**  
  The rate within the tier.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  The withholding applies.
- `TaxSubtotal/TaxCategory/Percent` = **2**  
  The rate of the tier.
- `TaxSubtotal/TaxCategory/TierRange` = **Above 2,000 coral**  
  The tier.
- `TaxSubtotal/TaxCategory/TierRatePercent` = **2**  
  The rate within the tier.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **OTH**  
  UN/EDIFACT 5153 code OTH: other taxes, the presumptive tax.
- `TaxSubtotal/TaxCategory/TaxScheme/Name` = **Presumptive tax on farm produce**  
  The tax in words.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **4068.000** (currencyID `XLC`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **4248.000** (currencyID `XLC`)  
  The cotton and the haulage.
- `TaxInclusiveAmount` = **4248.000** (currencyID `XLC`)  
  No tax on the island.
- `AllowanceTotalTaxInclusiveAmount` = **0.000** (currencyID `XLC`)  
  No allowances.
- `ChargeTotalAmount` = **180.000** (currencyID `XLC`)  
  The haulage allowance.
- `ChargeTotalTaxInclusiveAmount` = **180.000** (currencyID `XLC`)  
  The same: no tax on the island.
- `WithholdingTaxTotalAmount` = **61.360** (currencyID `XLC`)  
  Withheld and paid to the island's tax office.
- `PrepaidAmount` = **1000.000** (currencyID `XLC`)  
  The advance paid at the start of the season.
- `PayableAmount` = **3227.320** (currencyID `XLC`)  
  What the gin pays: the cotton and haulage, less the advance and the withholding, plus the levy the farm collects.

### Collection Invoice Line

Inside `CollectionInvoiceLine`:

- `ID` = **2**  
  The collection line.
- `Note` = **Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.**  
  Why the line is there.
- `InvoicedQuantity` = **1** (unitCode `EA`)  
  The levy, invoiced once.
- `LineExtensionAmount` = **40.680** (currencyID `XLC`)  
  1 % of the value of the seed cotton.
- `BeneficiaryParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `BeneficiaryParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Name` = **Cotton fund levy**  
  What is collected.

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **18000** (unitCode `KGM`)  
  The weighed seed cotton of three trailer loads.
- `LineExtensionAmount` = **4068.000** (currencyID `XLC`)  
  Quantity times price, rounded to the minor unit.
- `Delivery/DeliveryNoteLineReference/LineID` = **1**  
  The line of the delivery note the invoice line bills.
- `Delivery/DeliveryNoteLineReference/UUID` = **6d32dd14-dac3-5c83-91e2-8c40cef6875b**  
  A universally unique identifier of the line, derived from the document and the line number.
- `Delivery/DeliveryNoteLineReference/LineStatusCode` = **NoStatus**  
  The delivered line, unchanged.
- `Delivery/DeliveryNoteLineReference/DocumentReference/ID` = **LCF-DN-26-0192**  
  The farm's delivery note.
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
- `Price/PriceAmount` = **0.226** (currencyID `XLC`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `KGM`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<SelfBilledInvoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:SelfBilledInvoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:cotton</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SCG-SBI-26-0193</cbc:ID>
  <cbc:UUID>da6a76fb-cc8f-56c6-bea6-296a7804c3c9</cbc:UUID>
  <cbc:IssueDate>2026-02-07</cbc:IssueDate>
  <cbc:IssueTime>14:29:00</cbc:IssueTime>
  <cbc:DueDate>2026-03-24</cbc:DueDate>
  <cbc:TaxPointDate>2026-02-07</cbc:TaxPointDate>
  <cbc:InvoiceTypeCode>389</cbc:InvoiceTypeCode>
  <cbc:Note languageID="qal">Lakau-votee tilala kimii mitavema: sehove kulasi tohala lelala tanaha hokake.</cbc:Note>
  <cbc:Note languageID="en">Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.</cbc:Note>
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
  <cac:OrderReference>
    <cbc:ID>SCG-SEASON-2026/03</cbc:ID>
  </cac:OrderReference>
  <cac:BillingReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>SCG-ADV-26-0012</cbc:ID>
    </cac:AdditionalDocumentReference>
  </cac:BillingReference>
  <cac:ContractDocumentReference>
    <cbc:ID>SCG-SEASON-2026</cbc:ID>
  </cac:ContractDocumentReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>LCF-DN-26-0192</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:WorkReportDocumentReference>
    <cbc:ID>SCG-OUT-26-0311</cbc:ID>
  </cac:WorkReportDocumentReference>
  <cac:DeliveryNoteDocumentReference>
    <cbc:ID>LCF-DN-26-0192</cbc:ID>
  </cac:DeliveryNoteDocumentReference>
  <cac:ReceiptDocumentReference>
    <cbc:ID>SCG-WB-26-0311</cbc:ID>
  </cac:ReceiptDocumentReference>
  <cac:StatementDocumentReference>
    <cbc:ID>SCG-ACC-LCF-26-02</cbc:ID>
  </cac:StatementDocumentReference>
  <cac:OriginatorDocumentReference>
    <cbc:ID>LTM-SEASON-2026</cbc:ID>
  </cac:OriginatorDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>XL-FARM-REG-0412</cbc:ID>
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
        <cbc:Telephone>+999 3 721 2681</cbc:Telephone>
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
        <cbc:Description>Farm track off Plantation Road at kilometre 4, past the cotton fields.</cbc:Description>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:District>North coast</cbc:District>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:AddressLine>
          <cbc:Line>Sifatofu Natii / Plantation Road</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Farm track off Plantation Road at kilometre 4, past the cotton fields.</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>North coast</cbc:Line>
        </cac:AddressLine>
        <cac:AddressLine>
          <cbc:Line>Selanu</cbc:Line>
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
        <cbc:Telephone>+999 3 724 2544</cbc:Telephone>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42544</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
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
  <cac:OriginatorCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:OriginatorCustomerParty>
  <cac:BeneficiaryParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
  </cac:BeneficiaryParty>
  <cac:PayeeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lisavu Cotton Farm</cbc:Name>
    </cac:PartyName>
  </cac:PayeeParty>
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
    <cac:DeliveryLocation>
      <cbc:Name>Selanu Cotton Ginnery, weighbridge</cbc:Name>
    </cac:DeliveryLocation>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">DAP</cbc:ID>
  </cac:DeliveryTerms>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-03-24</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>CORAL-NET</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF07SCGSBI260193</cbc:InstructionNote>
    <cbc:PaymentID>RF07SCGSBI260193</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL05BSEL0004817534</cbc:ID>
      <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XLC</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice SCG-SBI-26-0193</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>BSEL-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>BSEL</cbc:ID>
          <cbc:Name>Bank of Selanu</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
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
    <cbc:ID>XL-STD</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>45 days net.</cbc:Note>
    <cbc:PaymentTermsDetailsURI>https://www.lisavufarm.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-03-24</cbc:PaymentDueDate>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>6</cbc:InterestRatePercent>
      <cbc:TimeBasisCode>Year</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode>Simple</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:PrepaidPayment>
    <cbc:ID>SCG-ADV-26-0012</cbc:ID>
    <cbc:PaidAmount currencyID="XLC">1000.000</cbc:PaidAmount>
    <cbc:PaidDate>2026-01-13</cbc:PaidDate>
  </cac:PrepaidPayment>
  <cac:AllowanceCharge>
    <cbc:ID>1</cbc:ID>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Haulage allowance</cbc:AllowanceChargeReason>
    <cbc:PrepaidIndicator>false</cbc:PrepaidIndicator>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cbc:Amount currencyID="XLC">180.000</cbc:Amount>
    <cbc:TaxInclusiveAmount currencyID="XLC">180.000</cbc:TaxInclusiveAmount>
    <cbc:BaseAmount currencyID="XLC">4068.000</cbc:BaseAmount>
    <cbc:AccountingCostCode>210</cbc:AccountingCostCode>
    <cbc:AccountingCost>Seed cotton haulage</cbc:AccountingCost>
    <cbc:PerUnitAmount currencyID="XLC">0.010</cbc:PerUnitAmount>
    <cac:TaxCategory>
      <cbc:ID>O</cbc:ID>
      <cbc:Percent>0</cbc:Percent>
      <cac:TaxScheme>
        <cbc:Name>No general sales tax</cbc:Name>
      </cac:TaxScheme>
    </cac:TaxCategory>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:PaymentMeans>
      <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    </cac:PaymentMeans>
  </cac:AllowanceCharge>
  <cac:TaxExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:TaxExchangeRate>
  <cac:PricingExchangeRate>
    <cbc:SourceCurrencyCode>XBL</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>0.4</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:PricingExchangeRate>
  <cac:PaymentExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:PaymentExchangeRate>
  <cac:PaymentAlternativeExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XBL</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>2.5</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:PaymentAlternativeExchangeRate>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">4068.000</cbc:TaxableAmount>
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
    <cbc:TaxAmount currencyID="XLC">61.360</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">2000.000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">20.000</cbc:TaxAmount>
      <cbc:Percent>1</cbc:Percent>
      <cbc:TierRange>Up to 2,000 coral of the delivery's value</cbc:TierRange>
      <cbc:TierRatePercent>1</cbc:TierRatePercent>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>1</cbc:Percent>
        <cbc:TierRange>Up to 2,000 coral of the delivery's value</cbc:TierRange>
        <cbc:TierRatePercent>1</cbc:TierRatePercent>
        <cac:TaxScheme>
          <cbc:ID>OTH</cbc:ID>
          <cbc:Name>Presumptive tax on farm produce</cbc:Name>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">2068.000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">41.360</cbc:TaxAmount>
      <cbc:Percent>2</cbc:Percent>
      <cbc:TierRange>Above 2,000 coral</cbc:TierRange>
      <cbc:TierRatePercent>2</cbc:TierRatePercent>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>2</cbc:Percent>
        <cbc:TierRange>Above 2,000 coral</cbc:TierRange>
        <cbc:TierRatePercent>2</cbc:TierRatePercent>
        <cac:TaxScheme>
          <cbc:ID>OTH</cbc:ID>
          <cbc:Name>Presumptive tax on farm produce</cbc:Name>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:WithholdingTaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">4068.000</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">4248.000</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">4248.000</cbc:TaxInclusiveAmount>
    <cbc:AllowanceTotalTaxInclusiveAmount currencyID="XLC">0.000</cbc:AllowanceTotalTaxInclusiveAmount>
    <cbc:ChargeTotalAmount currencyID="XLC">180.000</cbc:ChargeTotalAmount>
    <cbc:ChargeTotalTaxInclusiveAmount currencyID="XLC">180.000</cbc:ChargeTotalTaxInclusiveAmount>
    <cbc:WithholdingTaxTotalAmount currencyID="XLC">61.360</cbc:WithholdingTaxTotalAmount>
    <cbc:PrepaidAmount currencyID="XLC">1000.000</cbc:PrepaidAmount>
    <cbc:PayableAmount currencyID="XLC">3227.320</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:CollectionInvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.</cbc:Note>
    <cbc:InvoicedQuantity unitCode="EA">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">40.680</cbc:LineExtensionAmount>
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
  </cac:CollectionInvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="KGM">18000</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">4068.000</cbc:LineExtensionAmount>
    <cac:Delivery>
      <cac:DeliveryNoteLineReference>
        <cbc:LineID>1</cbc:LineID>
        <cbc:UUID>6d32dd14-dac3-5c83-91e2-8c40cef6875b</cbc:UUID>
        <cbc:LineStatusCode>NoStatus</cbc:LineStatusCode>
        <cac:DocumentReference>
          <cbc:ID>LCF-DN-26-0192</cbc:ID>
        </cac:DocumentReference>
      </cac:DeliveryNoteLineReference>
    </cac:Delivery>
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
      <cbc:PriceAmount currencyID="XLC">0.226</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</SelfBilledInvoice>
```
