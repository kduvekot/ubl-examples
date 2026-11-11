# Self Billed Invoice: Selanu Cotton Ginnery to Lisavu Cotton Farm

*Example 3 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Self Billed Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-SELF-BILLED-INVOICE-SCHEMA)*

Under the self-billing agreement the ginnery writes the farm's invoice from the weight and grade it measured. No tax on the island, stated as such.

[The XML file](03-SelfBilledInvoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); SelfBilledInvoice/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:self-billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Self-billing". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
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
- `InvoiceTypeCode` = **389** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 389: self-billed invoice. The code is from the world's copy of UN/EDIFACT 1001 Document name: 389 = Self-billed invoice.
- `Note` = **Lakau-votee tilala kimii mitavema: sehove kulasi tohala lelala tanaha hokake.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): The statement the self-billing agreement requires on every invoice.
- `Note` = **Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: The statement the self-billing agreement requires on every invoice.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the supplier's currency; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `TaxCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The presumptive tax is paid to the island's tax office in coral. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `PricingCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  Seed cotton is priced from the trade accord's lint reference price, published in lume. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PaymentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The farm is paid in coral. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `PaymentAlternativeCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The farm may ask to be paid in lume, to its account in Bayvarra, where it buys its machinery. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `AccountingCostCode` = **200**  
  The customer's own cost centre: it books what it billed itself.
- `AccountingCost` = **Seed cotton purchases**  
  The cost centre in words.
- `LineCountNumeric` = **2**  
  The seed cotton and the collection line of the levy.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts. The code is from the world's copy of ISO 639 Language: en = English.

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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Cotton Ginnery (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 0163 = Post-harvest crop activities.
- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 22 persons and its turnover of 3660000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Cotton Ginnery (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lisavu Cotton Farm (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 0116 = Growing of fibre crops.
- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **85779006** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en-XL`)  
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
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PostalAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PostalAddress/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LatitudeMinutesMeasure` = **58.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PostalAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PostalAddress/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PostalAddress/LocationCoordinate/LongitudeMinutesMeasure` = **7.80** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PostalAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PhysicalLocation/Description` = **The cotton fields**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/InformationURI` = **https://www.lisavufarm.example**  
  Where to find more about the place.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **58.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **7.80** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PartyLegalEntity/RegistrationName` = **Lisavu Cotton Farm**  
  The name under which the party is registered, with its legal form; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **2009-08-17**  
  The day the company was entered in the register; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/RegistrationExpirationDate` = **2026-12-31**  
  The island renews a farm's registration every year: it runs until this date.
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SP** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: SP = Sole proprietorship.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Fomofa nisakihi** (languageID `qal`)  
  The name of code SP in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Sole proprietorship** (languageID `en-XL`)  
  The name of code SP in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/SoleProprietorshipIndicator` = **true**  
  The farm belongs to one farmer, who runs it in their own name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/EntitySizeCode` = **MICRO** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 5 persons and its turnover of 146000.000 XLC in 2025, by the Trade Accord's limits; identity of Lisavu Cotton Farm (world/parties.json). The code is from the Trade Accord's entity size list: MICRO = Micro enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
  Delivered at the gin: the farm brings the cotton with its own tractor. The code is from the world's copy of Incoterms 2020: DAP = Delivered at Place. An identifier that holds a code names the code's list in its schemeID.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-03-24**  
  When the transfer must be credited.
- `PaymentChannelCode` = **RTGS** (listID `ISO 20022 ClearingChannel2Code`)  
  How the payment system clears and settles the transfer, as an ISO 20022 clearing channel (world/countries.json). The code is from the world's copy of ISO 20022 ClearingChannel2Code: RTGS = RealTimeGrossSettlementSystem.
- `PaymentRailID` = **CORAL-NET**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF07SCGSBI260193**  
  What the payer writes in the transfer.
- `PaymentID` = **RF07SCGSBI260193** (schemeID `ISO 11649`)  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits. The schemeID names the scheme it is from: the ISO 11649 structured creditor reference (RF, two check digits (ISO 7064 mod 97-10) and up to 21 letters and digits).
- `PayeeFinancialAccount/ID` = **XL67BSEL0020004817534** (schemeID `urn:ubl-examples:world:account`)  
  The supplier's account, where the customer pays what it billed itself. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Lisavu Cotton Farm**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `PayeeFinancialAccount/PaymentNote` = **Invoice SCG-SBI-26-0193**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **002** (schemeID `urn:ubl-examples:world:XL:bank-branch`)  
  The branch that keeps the account, by its national code: the branch number of a Lisavan bank (three digits). The account number holds it.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Market branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSELXLSL** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BSEL, the country XL and the location SL; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Selanu**  
  The bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Reef Street**  
  The bank's head office; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **23**  
  Its building number; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Selanu**  
  Its town; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The bank's country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Selanu**  
  The town the branch is in.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

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
- `PenaltyInterestRate/TimeBasisCode` = **ANN** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  A yearly rate. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: ANN = year.
- `PenaltyInterestRate/CalculationMethodCode` = **SIMPLE** (listID `urn:ubl-examples:world:codelist:InterestCalculationCode`)  
  Simple interest, per day late. The code is from the Trade Accord's interest calculation method list: SIMPLE = Simple interest.

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
- `AllowanceChargeReasonCode` = **CAB** (listID `UN/EDIFACT EDED 7161`)  
  The gin pays the farm for carting the cotton: a charge in the farm's favour, so a code of UN/EDIFACT 7161. The code is from the world's copy of UN/EDIFACT 7161 Special service description: CAB = Cartage.
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
- `TaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  Lisavu has no sales tax or value added tax: no tax applies (category O). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the haulage on the island.
- `PaymentMeans/PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  Credit transfer, with the invoice. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.

### Tax Exchange Rate

Inside `TaxExchangeRate`:

- `SourceCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The document currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `TargetCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The tax currency, coral. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `CalculationRate` = **1**  
  The same currency: no conversion.
- `MathematicOperatorCode` = **Multiply** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  Coral times the rate. The code is from the world's copy of UBL's Operator list, with a listID: Multiply.
- `Date` = **2026-02-07**  
  Of the document's date.

### Pricing Exchange Rate

Inside `PricingExchangeRate`:

- `SourceCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The reference price's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `TargetCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The document's. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `CalculationRate` = **0.4**  
  The reference rate.
- `MathematicOperatorCode` = **Multiply** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  Lume times the rate gives coral. The code is from the world's copy of UBL's Operator list, with a listID: Multiply.
- `Date` = **2026-02-07**  
  Of the document's date.

### Payment Exchange Rate

Inside `PaymentExchangeRate`:

- `SourceCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The document currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `TargetCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The payment currency, coral. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `CalculationRate` = **1**  
  The same currency: no conversion.
- `MathematicOperatorCode` = **Multiply** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  Coral times the rate. The code is from the world's copy of UBL's Operator list, with a listID: Multiply.
- `Date` = **2026-02-07**  
  Of the document's date.

### Payment Alternative Exchange Rate

Inside `PaymentAlternativeExchangeRate`:

- `SourceCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The document currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `TargetCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  Lume, the alternative. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `CalculationRate` = **2.5**  
  The reference rate.
- `MathematicOperatorCode` = **Multiply** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  Coral times the rate. The code is from the world's copy of UBL's Operator list, with a listID: Multiply.
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
- `TaxSubtotal/TaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  Lisavu has no sales tax or value added tax: no tax applies (category O). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
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
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The withholding applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **1**  
  The rate of the tier.
- `TaxSubtotal/TaxCategory/TierRange` = **Up to 2,000 coral of the delivery's value**  
  The tier.
- `TaxSubtotal/TaxCategory/TierRatePercent` = **1**  
  The rate within the tier.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **OTH** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code OTH: other taxes, the presumptive tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: OTH = Other taxes. An identifier that holds a code names the code's list in its schemeID.
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
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The withholding applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **2**  
  The rate of the tier.
- `TaxSubtotal/TaxCategory/TierRange` = **Above 2,000 coral**  
  The tier.
- `TaxSubtotal/TaxCategory/TierRatePercent` = **2**  
  The rate within the tier.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **OTH** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code OTH: other taxes, the presumptive tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: OTH = Other taxes. An identifier that holds a code names the code's list in its schemeID.
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
- `Delivery/DeliveryNoteLineReference/LineStatusCode` = **NoStatus** (listID `urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode`)  
  The delivered line, unchanged. The code is from the world's copy of UBL's Line status list, with a listID: NoStatus = Line has no status..
- `Delivery/DeliveryNoteLineReference/DocumentReference/ID` = **LCF-DN-26-0192**  
  The farm's delivery note.
- `Item/Description` = **Cotton as harvested, not ginned, delivered loose by trailer.**  
  The seller's description; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Name` = **Votike tekapa** (languageID `qal`)  
  The item's name in Lisavan, the seller's language; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/Name` = **Seed cotton** (languageID `en-XL`)  
  The item's name in English, the working language between the countries; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/SellersItemIdentification/ID` = **LCF-SC**  
  The seller's own item number; item seed-cotton of Lisavu Cotton Farm (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Where the item was produced; item seed-cotton of Lisavu Cotton Farm (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item seed-cotton of Lisavu Cotton Farm (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `Item/CommodityClassification/ItemClassificationCode` = **01921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item seed-cotton of Lisavu Cotton Farm (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01921 = Cotton, whether or not ginned.
- `Item/ClassifiedTaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  Lisavu has no sales tax or value added tax: no tax applies (category O). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
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
  <cbc:CustomizationID>urn:ubl-examples:world:trns:self-billing:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SCG-SBI-26-0193</cbc:ID>
  <cbc:UUID>da6a76fb-cc8f-56c6-bea6-296a7804c3c9</cbc:UUID>
  <cbc:IssueDate>2026-02-07</cbc:IssueDate>
  <cbc:IssueTime>14:29:00</cbc:IssueTime>
  <cbc:DueDate>2026-03-24</cbc:DueDate>
  <cbc:TaxPointDate>2026-02-07</cbc:TaxPointDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">389</cbc:InvoiceTypeCode>
  <cbc:Note languageID="qal">Lakau-votee tilala kimii mitavema: sehove kulasi tohala lelala tanaha hokake.</cbc:Note>
  <cbc:Note languageID="en-XL">Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:TaxCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TaxCurrencyCode>
  <cbc:PricingCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:PricingCurrencyCode>
  <cbc:PaymentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:PaymentCurrencyCode>
  <cbc:PaymentAlternativeCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:PaymentAlternativeCurrencyCode>
  <cbc:AccountingCostCode>200</cbc:AccountingCostCode>
  <cbc:AccountingCost>Seed cotton purchases</cbc:AccountingCost>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
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
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
        <cbc:BuildingNumber>42</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Cotton Ginnery Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
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
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">85779006</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Sifatofu Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Plantation Road</cbc:StreetName>
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
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">58.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">7.80</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>The cotton fields</cbc:Description>
        <cbc:InformationURI>https://www.lisavufarm.example</cbc:InformationURI>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">58.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">7.80</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lisavu Cotton Farm</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:CompanyID>
        <cbc:RegistrationDate>2009-08-17</cbc:RegistrationDate>
        <cbc:RegistrationExpirationDate>2026-12-31</cbc:RegistrationExpirationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">SP</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Fomofa nisakihi</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Sole proprietorship</cbc:CompanyLegalForm>
        <cbc:SoleProprietorshipIndicator>true</cbc:SoleProprietorshipIndicator>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">MICRO</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
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
    <cbc:PaymentChannelCode listID="ISO 20022 ClearingChannel2Code">RTGS</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>CORAL-NET</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF07SCGSBI260193</cbc:InstructionNote>
    <cbc:PaymentID schemeID="ISO 11649">RF07SCGSBI260193</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL67BSEL0020004817534</cbc:ID>
      <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XLC</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice SCG-SBI-26-0193</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:bank-branch">002</cbc:ID>
        <cbc:Name>Market branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">BSELXLSL</cbc:ID>
          <cbc:Name>Bank of Selanu</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
            <cbc:StreetName>Reef Street</cbc:StreetName>
            <cbc:BuildingNumber>23</cbc:BuildingNumber>
            <cbc:CityName>Selanu</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
        <cac:Address>
          <cbc:CityName>Selanu</cbc:CityName>
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
  <cac:PaymentTerms>
    <cbc:ID>XL-STD</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>45 days net.</cbc:Note>
    <cbc:PaymentTermsDetailsURI>https://www.lisavufarm.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-03-24</cbc:PaymentDueDate>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>6</cbc:InterestRatePercent>
      <cbc:TimeBasisCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">ANN</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:InterestCalculationCode">SIMPLE</cbc:CalculationMethodCode>
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
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">CAB</cbc:AllowanceChargeReasonCode>
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
      <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
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
    <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:TaxExchangeRate>
  <cac:PricingExchangeRate>
    <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>0.4</cbc:CalculationRate>
    <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:PricingExchangeRate>
  <cac:PaymentExchangeRate>
    <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>1</cbc:CalculationRate>
    <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:PaymentExchangeRate>
  <cac:PaymentAlternativeExchangeRate>
    <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>2.5</cbc:CalculationRate>
    <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-02-07</cbc:Date>
  </cac:PaymentAlternativeExchangeRate>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">4068.000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
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
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>1</cbc:Percent>
        <cbc:TierRange>Up to 2,000 coral of the delivery's value</cbc:TierRange>
        <cbc:TierRatePercent>1</cbc:TierRatePercent>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">OTH</cbc:ID>
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
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>2</cbc:Percent>
        <cbc:TierRange>Above 2,000 coral</cbc:TierRange>
        <cbc:TierRatePercent>2</cbc:TierRatePercent>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">OTH</cbc:ID>
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
        <cbc:LineStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode">NoStatus</cbc:LineStatusCode>
        <cac:DocumentReference>
          <cbc:ID>LCF-DN-26-0192</cbc:ID>
        </cac:DocumentReference>
      </cac:DeliveryNoteLineReference>
    </cac:Delivery>
    <cac:Item>
      <cbc:Description>Cotton as harvested, not ginned, delivered loose by trailer.</cbc:Description>
      <cbc:Name languageID="qal">Votike tekapa</cbc:Name>
      <cbc:Name languageID="en-XL">Seed cotton</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>LCF-SC</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">520100</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01921</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
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
