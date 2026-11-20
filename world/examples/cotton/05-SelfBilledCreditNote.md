# Self Billed Credit Note: Selanu Cotton Ginnery to Lisavu Cotton Farm

*Example 5 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Self Billed Credit Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-SELF-BILLED-CREDIT-NOTE-SCHEMA)*

Classing after ginning puts part of the delivery a grade lower; the ginnery credits the difference on the farm's behalf.

[The XML file](05-SelfBilledCreditNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; SelfBilledCreditNote/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:self-billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Self-billing". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SCG-SBC-26-0195**  
  The number the customer gives the self-billed document, under the self-billing agreement.
- `UUID` = **4ce8ce40-98a9-5b24-97ee-9a8cbf98f3f1**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-16**  
  Issued the day after the chamber's classing report showed part of the lint a grade lower.
- `IssueTime` = **13:28:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `DueDate` = **2026-04-17**  
  Set off on the day of payment.
- `CreditNoteTypeCode` = **261** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 261, "A document which indicates that the customer is claiming credit in a self billing environment": the customer corrects its own self-billed invoice. It repeats what the root SelfBilledCreditNote already says, but its definition is exact; 381, the supplier's credit note, would not be. The code is from the world's copy of UN/EDIFACT 1001 Document name: 261 = Self billed credit note.
- `Note` = **Lakau-votee tetela tamasu tilala kimii mitavema.** (languageID `qal`)  
  The note in Lisavan, the sender's language: As required on every self-billed document.
- `Note` = **Self-billed credit note under the season agreement.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: As required on every self-billed document.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the supplier's currency; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `AccountingCostCode` = **200**  
  The customer's own cost centre: it books what it billed itself.
- `AccountingCost` = **Seed cotton purchases**  
  The cost centre in words.
- `LineCountNumeric` = **2**  
  The price difference and the levy on it.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts. The code is from the world's copy of ISO 639 Language: en = English.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-04-06**  
  The deliveries classed, from the first trailer of 6 April
- `EndDate` = **2026-04-08**  
  to the last, of 8 April.

### Discrepancy Response

Inside `DiscrepancyResponse`:

- `ReferenceID` = **1**  
  The line of the self-billed invoice.
- `ResponseCode` = **2** (listID `UN/EDIFACT EDED 4465`)  
  The classing found a lower grade. The code is from the world's copy of UN/EDIFACT 4465 Adjustment reason description: 2 = Below specification goods.
- `Description` = **Lint ginned from 2,500 kg of seed cotton classed Strict Low Middling instead of Middling.**  
  In words: the grade is the lint's, applied to the seed cotton it was ginned from.

### Order Reference

Inside `OrderReference`:

- `ID` = **SCG-SEASON-2026/03**  
  The call-off.

### Billing Reference

Inside `BillingReference`:

- `SelfBilledInvoiceDocumentReference/ID` = **SCG-SBI-26-0194**  
  The self-billed invoice this corrects.
- `SelfBilledInvoiceDocumentReference/IssueDate` = **2026-04-09**  
  Its issue date.

### Delivery Note Document Reference

Inside `DeliveryNoteDocumentReference`:

- `ID` = **LCF-DN-26-0193**  
  The delivery classed.

### Work Report Document Reference

Inside `WorkReportDocumentReference`:

- `ID` = **SCC-CLS-26-0311**  
  The chamber's classing report of the lint ginned from the farm's delivery, of 15 April, on which the downgrade rests.

### Contract Document Reference

Inside `ContractDocumentReference`:

- `ID` = **SCG-SEASON-2026**  
  The season agreement: it sets the price per grade.

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

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
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
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery Ltd**  
  The name under which the party is registered, with its legal form; as Selanu Cotton Ginnery gives it.
- `Party/PartyLegalEntity/CompanyID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Selanu Cotton Ginnery gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Selanu Cotton Ginnery gives it.
- `Party/Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Telephone` = **+999 3 721 0486**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Cotton Ginnery gives it.
- `Party/Contact/ElectronicMail` = **payables@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu Cotton Ginnery gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Cotton Ginnery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **LFR-0412** (schemeID `urn:ubl-examples:world:XL:farm-register`)  
  The party's preferred identifier: its number in the Farm register of Lisavu; as Lisavu Cotton Farm gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; as Lisavu Cotton Farm gives it.
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **85779006** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Lisavu Cotton Farm gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Sifatofu Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Lisavu Cotton Farm gives it.
- `Party/PostalAddress/StreetName` = **Plantation Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Lisavu Cotton Farm gives it.
- `Party/PostalAddress/Description` = **Farm track off Plantation Road at kilometre 4, past the cotton fields.**  
  How to find the farm, which has no house number on a street. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/District` = **North coast**  
  The district of the island, used to find a farm off the main roads. As Lisavu Cotton Farm gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PostalAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PostalAddress/LocationCoordinate/LatitudeDegreesMeasure` = **32** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PostalAddress/LocationCoordinate/LatitudeMinutesMeasure` = **44.86** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PostalAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PostalAddress/LocationCoordinate/LongitudeDegreesMeasure` = **2** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PostalAddress/LocationCoordinate/LongitudeMinutesMeasure` = **16.51** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PostalAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PhysicalLocation/Description` = **The cotton fields**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **32** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **44.86** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **2** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **16.51** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PartyLegalEntity/RegistrationName` = **Lisavu Cotton Farm**  
  The name under which the party is registered, with its legal form; as Lisavu Cotton Farm gives it.
- `Party/PartyLegalEntity/CompanyID` = **LFR-0412** (schemeID `urn:ubl-examples:world:XL:farm-register`)  
  Number in the Farm register of Lisavu; as Lisavu Cotton Farm gives it. The schemeID names the scheme it is from: the farm register of Lisavu (LFR- and 4 digits, kept from season to season while the registration is renewed).
- `Party/PartyLegalEntity/RegistrationExpirationDate` = **2026-12-31**  
  The island renews a farm's registration every year: it runs until this date.
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SP** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: SP = Sole proprietorship.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Fomofa nisakihi** (languageID `qal`)  
  The name of code SP in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Sole proprietorship** (languageID `en-XL`)  
  The name of code SP in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/SoleProprietorshipIndicator` = **true**  
  The farm belongs to one farmer, who runs it in their own name; as Lisavu Cotton Farm gives it.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:FR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Farm register of Lisavu**  
  The register the farm is entered in, kept by the Department of Agriculture of Lisavu: Growers are entered in the island's farm register, not in the companies register; a grower's registration is renewed each season, so the entry carries an expiry date. The register gives a grower a number of its own, derived from no other register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **FARM** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of farms, not the companies register. The code is from the Trade Accord's corporate registration type list: FARM = Register of farms.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/Contact/Name` = **Farm office**  
  The party's main desk, which handles this document; as Lisavu Cotton Farm gives it.
- `Party/Contact/JobTitle` = **Farm manager**  
  The job of the person who answers at the desk; as Lisavu Cotton Farm gives it.
- `Party/Contact/Department` = **Management**  
  The department the desk belongs to; as Lisavu Cotton Farm gives it.
- `Party/Contact/Telephone` = **+999 3 724 6676**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Lisavu Cotton Farm gives it.
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lisavu Cotton Farm gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lisavu Cotton Farm gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:LFR-0412** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Farm register of Lisavu; as Lisavu Cotton Farm gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **LFR-0412** (schemeID `urn:ubl-examples:world:XL:farm-register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery

Inside `Delivery`:

- `ActualDeliveryDate` = **2026-04-08**  
  The delivery classed.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **97** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 97: clearing between partners; set off against the payment. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 97 = Clearing between partners.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **Set off against the payment of the self-billed invoice.**  
  How the credit is settled.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **false**  
  An allowance: it lowers the credit, so the farm keeps the amount.
- `AllowanceChargeReasonCode` = **64** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 64 = Special agreement.
- `AllowanceChargeReason` = **Classing fee borne by the ginnery**  
  The ginnery bears the chamber's fee for classing the farm's lint, as the season agreement says: it is taken off what the farm gives back.
- `Amount` = **5.000** (currencyID `XLC`)  
  The chamber's fee for classing the lint of the delivery.

### Withholding Tax Total

Inside `WithholdingTaxTotal`:

- `TaxAmount` = **0.850** (currencyID `XLC`)  
  The withholding reversed on the credit: the credited value falls in the 2 % tier of the delivery.
- `TaxSubtotal/TaxableAmount` = **42.500** (currencyID `XLC`)  
  The part of the value in this tier.
- `TaxSubtotal/TaxAmount` = **0.850** (currencyID `XLC`)  
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

- `LineExtensionAmount` = **42.500** (currencyID `XLC`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **37.500** (currencyID `XLC`)  
  The credit less the fee.
- `TaxInclusiveAmount` = **37.500** (currencyID `XLC`)  
  The same as the total without tax: Lisavu has no sales tax or value added tax, so no tax is due and the document has no tax section.
- `AllowanceTotalAmount` = **5.000** (currencyID `XLC`)  
  The classing fee the farm bears.
- `WithholdingTaxTotalAmount` = **0.850** (currencyID `XLC`)  
  The withholding on the credited value, reversed: the value falls in the 2 % tier.
- `PayableAmount` = **37.075** (currencyID `XLC`)  
  What the farm's account is credited: the price difference less the fee and the withholding, plus the levy on it.

### Collection Credit Note Line

Inside `CollectionCreditNoteLine`:

- `ID` = **2**  
  The collection line.
- `Note` = **Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.**  
  Why the line is there.
- `CreditedQuantity` = **1** (unitCode `EA`)  
  The levy, credited once.
- `LineExtensionAmount` = **0.425** (currencyID `XLC`)  
  1 % of the value of the seed cotton.
- `BeneficiaryParty/PartyIdentification/ID` = **GOV-243** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
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
  The seed cotton whose lint was classed lower.
- `LineExtensionAmount` = **42.500** (currencyID `XLC`)  
  Quantity times price, rounded to the minor unit.
- `Item/Description` = **Tekapa tanema tiloluti, hivile nipupe, tasepaha pisosi ninote vaputa.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `Item/Description` = **Cotton as harvested, not ginned, delivered loose by trailer.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Votike tekapa** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `Item/Name` = **Seed cotton** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **LCF-SC**  
  The seller's own item number; as Lisavu Cotton Farm describes the item.
- `Price/PriceAmount` = **0.017** (currencyID `XLC`)  
  The season agreement's discount for seed cotton whose lint is classed a grade lower: the lint's discount of 0.050 coral a kilogram (about 5 %) at the ginning yield of 34 %.
- `Price/BaseQuantity` = **1** (unitCode `KGM`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<SelfBilledCreditNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:SelfBilledCreditNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:self-billing:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SCG-SBC-26-0195</cbc:ID>
  <cbc:UUID>4ce8ce40-98a9-5b24-97ee-9a8cbf98f3f1</cbc:UUID>
  <cbc:IssueDate>2026-04-16</cbc:IssueDate>
  <cbc:IssueTime>13:28:00+00:00</cbc:IssueTime>
  <cbc:DueDate>2026-04-17</cbc:DueDate>
  <cbc:CreditNoteTypeCode listID="UN/EDIFACT EDED 1001">261</cbc:CreditNoteTypeCode>
  <cbc:Note languageID="qal">Lakau-votee tetela tamasu tilala kimii mitavema.</cbc:Note>
  <cbc:Note languageID="en-XL">Self-billed credit note under the season agreement.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>200</cbc:AccountingCostCode>
  <cbc:AccountingCost>Seed cotton purchases</cbc:AccountingCost>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-04-06</cbc:StartDate>
    <cbc:EndDate>2026-04-08</cbc:EndDate>
  </cac:InvoicePeriod>
  <cac:DiscrepancyResponse>
    <cbc:ReferenceID>1</cbc:ReferenceID>
    <cbc:ResponseCode listID="UN/EDIFACT EDED 4465">2</cbc:ResponseCode>
    <cbc:Description>Lint ginned from 2,500 kg of seed cotton classed Strict Low Middling instead of Middling.</cbc:Description>
  </cac:DiscrepancyResponse>
  <cac:OrderReference>
    <cbc:ID>SCG-SEASON-2026/03</cbc:ID>
  </cac:OrderReference>
  <cac:BillingReference>
    <cac:SelfBilledInvoiceDocumentReference>
      <cbc:ID>SCG-SBI-26-0194</cbc:ID>
      <cbc:IssueDate>2026-04-09</cbc:IssueDate>
    </cac:SelfBilledInvoiceDocumentReference>
  </cac:BillingReference>
  <cac:DeliveryNoteDocumentReference>
    <cbc:ID>LCF-DN-26-0193</cbc:ID>
  </cac:DeliveryNoteDocumentReference>
  <cac:WorkReportDocumentReference>
    <cbc:ID>SCC-CLS-26-0311</cbc:ID>
  </cac:WorkReportDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>SCG-SEASON-2026</cbc:ID>
  </cac:ContractDocumentReference>
  <cac:BuyerAssignedReference>
    <cbc:BuyerReferenceCode>SCG-AP-FARMS</cbc:BuyerReferenceCode>
    <cbc:BuyerReference>Farm payments</cbc:BuyerReference>
  </cac:BuyerAssignedReference>
  <cac:PurchaseReference>
    <cbc:ID>LCF-FIELD-07</cbc:ID>
  </cac:PurchaseReference>
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
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
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
        <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
        <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Cotton Ginnery Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
        <cac:RegistrationAddress>
          <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
          <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
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
        <cbc:Name>Accounts payable</cbc:Name>
        <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
        <cbc:ElectronicMail>payables@selanuginnery.example</cbc:ElectronicMail>
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
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:farm-register">LFR-0412</cbc:ID>
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
        <cbc:CityName languageID="qal">Kefalasa</cbc:CityName>
        <cbc:CityName languageID="en-XL">Lintwell</cbc:CityName>
        <cbc:District>North coast</cbc:District>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">32</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">44.86</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">2</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">16.51</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>The cotton fields</cbc:Description>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">32</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">44.86</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">2</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">16.51</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lisavu Cotton Farm</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:farm-register">LFR-0412</cbc:CompanyID>
        <cbc:RegistrationExpirationDate>2026-12-31</cbc:RegistrationExpirationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">SP</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Fomofa nisakihi</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Sole proprietorship</cbc:CompanyLegalForm>
        <cbc:SoleProprietorshipIndicator>true</cbc:SoleProprietorshipIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName languageID="qal">Kefalasa</cbc:CityName>
          <cbc:CityName languageID="en-XL">Lintwell</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:FR</cbc:ID>
          <cbc:Name>Farm register of Lisavu</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">FARM</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Farm office</cbc:Name>
        <cbc:JobTitle>Farm manager</cbc:JobTitle>
        <cbc:Department>Management</cbc:Department>
        <cbc:Telephone>+999 3 724 6676</cbc:Telephone>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:LFR-0412</cbc:ElectronicAddressID>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XL:farm-register">LFR-0412</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cbc:ActualDeliveryDate>2026-04-08</cbc:ActualDeliveryDate>
  </cac:Delivery>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">97</cbc:PaymentMeansCode>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:Note>Set off against the payment of the self-billed invoice.</cbc:Note>
  </cac:PaymentTerms>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">64</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Classing fee borne by the ginnery</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XLC">5.000</cbc:Amount>
  </cac:AllowanceCharge>
  <cac:WithholdingTaxTotal>
    <cbc:TaxAmount currencyID="XLC">0.850</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">42.500</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">0.850</cbc:TaxAmount>
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
    <cbc:LineExtensionAmount currencyID="XLC">42.500</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">37.500</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">37.500</cbc:TaxInclusiveAmount>
    <cbc:AllowanceTotalAmount currencyID="XLC">5.000</cbc:AllowanceTotalAmount>
    <cbc:WithholdingTaxTotalAmount currencyID="XLC">0.850</cbc:WithholdingTaxTotalAmount>
    <cbc:PayableAmount currencyID="XLC">37.075</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:CollectionCreditNoteLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.</cbc:Note>
    <cbc:CreditedQuantity unitCode="EA">1</cbc:CreditedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">0.425</cbc:LineExtensionAmount>
    <cac:BeneficiaryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-243</cbc:ID>
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
    <cbc:LineExtensionAmount currencyID="XLC">42.500</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description languageID="qal">Tekapa tanema tiloluti, hivile nipupe, tasepaha pisosi ninote vaputa.</cbc:Description>
      <cbc:Description languageID="en-XL">Cotton as harvested, not ginned, delivered loose by trailer.</cbc:Description>
      <cbc:Name languageID="qal">Votike tekapa</cbc:Name>
      <cbc:Name languageID="en-XL">Seed cotton</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>LCF-SC</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">0.017</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:CreditNoteLine>
</SelfBilledCreditNote>
```
