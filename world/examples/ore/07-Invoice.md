# Invoice: Serravona Mining to Valdara Industries

*Example 7 of the flow "Ore from the mine to the factory (domestic, Urvania)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The mine invoices the ore; transport is not on this invoice because under FCA the buyer pays it. Payment goes to the mine's account at the seller's bank.

[The XML file](07-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:ore**  
  The business process the document belongs to: the flow "Ore from the mine to the factory (domestic, Urvania)".
- `ProfileExecutionID` = **ORE-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SM-INV-26-0312**  
  The seller's invoice number.
- `UUID` = **b47d9e09-122e-55a3-a2d2-dde5a4947c4f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-11**  
  Issued the day after the goods were despatched and weighed.
- `IssueTime` = **14:59:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-04-10**  
  30 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380** (listID `UN/EDIFACT EDED 1001`)  
  A commercial invoice, as UN/EDIFACT 1001 codes it. The code is from the world's copy of UN/EDIFACT 1001 Document name: 380 = Commercial invoice.
- `TaxPointDate` = **2026-03-11**  
  Urvania's value added tax becomes due on the invoice date.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, the seller's currency; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `AccountingCostCode` = **3100**  
  The buyer's cost centre, quoted in its order, so the invoice is booked without asking.
- `AccountingCost` = **Raw materials and parts**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  The number of invoice lines, as a check on the transfer.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts that carry no language identifier: English, the working language between the countries; a seller from Urvania or the island also gives its notes in its own language. The code is from the world's copy of ISO 639 Language: en = English.

### Order Reference

Inside `OrderReference`:

- `ID` = **VI-PO-26-0304**  
  The buyer's order.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **SM-DA-26-0308**  
  The despatch advice of the goods invoiced.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.serravona.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Serravona Mining (world/parties.json).
- `Party/IndustryClassificationCode` = **0710** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Serravona Mining (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 0710 = Mining of iron ores.
- `Party/PartyIdentification/ID` = **XU-R-104137** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Serravona Mining (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Serravona Mining**  
  The trading name; identity of Serravona Mining (world/parties.json).
- `Party/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Zalsul Hekrul Varman** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/StreetName` = **Strada della Miniera** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **10**  
  Building number of the postal address. identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PhysicalLocation/ID` = **XUSRV** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Party/PhysicalLocation/Description` = **The mine and its rail siding**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/Conditions` = **Unpaved access road; heavy vehicles only.**  
  What a visitor must know about getting there.
- `Party/PhysicalLocation/InformationURI` = **https://www.serravona.example**  
  Where to find more about the place.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **54.00** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **30.60** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PartyTaxScheme/RegistrationName` = **Serravona Mining SUA**  
  The name under which the party is registered for value added tax; identity of Serravona Mining (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007289704**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Serravona Mining (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/RegistrationName` = **Serravona Mining SUA**  
  The name under which the party is registered, with its legal form; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104137**  
  Number in the Commercial register of Urvania; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1958-06-30**  
  The day the company was entered in the register; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 987 persons and its turnover of 48000000000 XUF in 2025, by the Trade Accord's limits; identity of Serravona Mining (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **120000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/Contact/Name` = **Sales office**  
  The desk that handles this document; identity of Serravona Mining (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Serravona Mining (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Serravona Mining (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 0413 24137**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Serravona Mining (world/parties.json).
- `Party/Contact/ElectronicMail` = **sales@serravona.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Serravona Mining (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Serravona Mining (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104137** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Serravona Mining (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 3083 persons and its turnover of 23600000000 XUF in 2025, by the Trade Accord's limits; identity of Valdara Industries (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/SecurityListing/ID` = **XU0001042501**  
  The identifier of the listed shares, in the form of an ISIN with the world's country code.
- `Party/PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `Party/PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The name of code XFER in the Trade Accord's market identifier list.
- `Party/PartyLegalEntity/SecurityListing/MarketCode` = **XFER** (listID `urn:ubl-examples:world:codelist:MarketCode`)  
  The market's code. The code is from the Trade Accord's market identifier list: XFER = Ferrano Stock Exchange.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ServiceProviderParty/ID` = **5-xu-SP-8-xu**  
  The service contract between the two.
- `Party/ServiceProviderParty/ServiceTypeCode` = **LOGISTICS** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  The kind of service, as a code. The code is from the Trade Accord's service type list: LOGISTICS = Logistics service.
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Valdara Industries**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104137** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Serravona Mining**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-04-10**  
  When the transfer must be credited.
- `PaymentChannelCode` = **RTGS** (listID `ISO 20022 ClearingChannel2Code`)  
  How the payment system clears and settles the transfer, as an ISO 20022 clearing channel (world/countries.json). The code is from the world's copy of ISO 20022 ClearingChannel2Code: RTGS = RealTimeGrossSettlementSystem.
- `PaymentRailID` = **FERRA-RTGS**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF73SMINV260312**  
  What the payer writes in the transfer.
- `PaymentID` = **RF73SMINV260312**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `PayeeFinancialAccount/ID` = **XU56CREV0000104729** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Serravona Mining SUA**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PayeeFinancialAccount/PaymentNote` = **Invoice SM-INV-26-0312**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **CREV-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREV**  
  The bank code, the part of every account number that names the bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca**  
  The bank's head office; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Its building number; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano**  
  Its town; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The bank's country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Ferrano**  
  The branch is at the bank's head office.
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
- `SettlementDiscountAmount` = **340759** (currencyID `XUF`)  
  The discount on the amount payable, if paid in time.
- `PaymentTermsDetailsURI` = **https://www.serravona.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-04-10**  
  The day the amount is due.
- `SettlementPeriod/StartDate` = **2026-03-11**  
  From the invoice date.
- `SettlementPeriod/EndDate` = **2026-03-21**  
  For 10 days.
- `PenaltyInterestRate/InterestRatePercent` = **8**  
  The interest on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **ANN** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  A yearly rate. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: ANN = year.
- `PenaltyInterestRate/CalculationMethodCode` = **SIMPLE** (listID `urn:ubl-examples:world:codelist:InterestCalculationCode`)  
  Simple interest, per day late. The code is from the Trade Accord's interest calculation method list: SIMPLE = Simple interest.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **2839657** (currencyID `XUF`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **14198286** (currencyID `XUF`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **2839657** (currencyID `XUF`)  
  20 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S).
- `TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **14198286** (currencyID `XUF`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **14198286** (currencyID `XUF`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **17037943** (currencyID `XUF`)  
  The total without tax plus the tax.
- `PayableAmount` = **17037943** (currencyID `XUF`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **1788.4** (unitCode `TNE`)  
  The weighed quantity from the despatch advice, not the ordered quantity.
- `LineExtensionAmount` = **14198286** (currencyID `XUF`)  
  1788.4 × the price = 14414504, less the 1.5 % moisture deduction.
- `TaxInclusiveLineExtensionAmount` = **17037943** (currencyID `XUF`)  
  The line with its tax.
- `OrderLineReference/LineID` = **1**  
  The order line this invoice line bills.
- `AllowanceCharge/ChargeIndicator` = **false**  
  An allowance on the line.
- `AllowanceCharge/AllowanceChargeReasonCode` = **64** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189: the moisture deduction is agreed in the contract. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 64 = Special agreement.
- `AllowanceCharge/AllowanceChargeReason` = **Moisture deduction**  
  The sample at loading showed 7.5 % moisture, above the 6 % of the contract: the contract deducts 1.5 % of the value.
- `AllowanceCharge/MultiplierFactorNumeric` = **0.015**  
  The rate.
- `AllowanceCharge/Amount` = **216218** (currencyID `XUF`)  
  The deduction on the line.
- `AllowanceCharge/BaseAmount` = **14414504** (currencyID `XUF`)  
  The line at the full price.
- `TaxTotal/TaxAmount` = **2839657** (currencyID `XUF`)  
  20 % of the line amount, for the buyer's booking per line.
- `Item/Description` = **Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.**  
  The seller's description; item ore-lump of Serravona Mining (world/items.json).
- `Item/Name` = **Gek trir, zul** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item ore-lump of Serravona Mining (world/items.json).
- `Item/Name` = **Iron ore, lump** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item ore-lump of Serravona Mining (world/items.json).
- `Item/SellersItemIdentification/ID` = **SM-ORE-L**  
  The seller's own item number; item ore-lump of Serravona Mining (world/items.json).
- `Item/StandardItemIdentification/ID` = **771010000013** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item ore-lump of Serravona Mining (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item ore-lump of Serravona Mining (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **260111** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item ore-lump of Serravona Mining (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 260111 = Iron ores and concentrates, non-agglomerated.
- `Item/CommodityClassification/ItemClassificationCode` = **14100** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item ore-lump of Serravona Mining (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 14100 = Iron ores and concentrates, other than roasted iron pyrites.
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S).
- `Item/ClassifiedTaxCategory/Percent` = **20**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.
- `Item/AdditionalItemProperty/Name` = **Iron content**  
  A measured property of the item.
- `Item/AdditionalItemProperty/ValueQuantity` = **62** (unitCode `P1`)  
  Its measured value; item ore-lump of Serravona Mining (world/items.json).
- `Price/PriceAmount` = **8060** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.
- `ItemPriceExtension/Amount` = **14414504** (currencyID `XUF`)  
  Price times quantity, before the allowance.
- `ItemPriceExtension/TaxInclusiveAmount` = **17297405** (currencyID `XUF`)  
  The price extension with 20 % value added tax.
- `ItemPriceExtension/TaxTotal/TaxAmount` = **2882901** (currencyID `XUF`)  
  The tax on the price extension, before the line's allowance.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:ore</cbc:ProfileID>
  <cbc:ProfileExecutionID>ORE-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SM-INV-26-0312</cbc:ID>
  <cbc:UUID>b47d9e09-122e-55a3-a2d2-dde5a4947c4f</cbc:UUID>
  <cbc:IssueDate>2026-03-11</cbc:IssueDate>
  <cbc:IssueTime>14:59:00</cbc:IssueTime>
  <cbc:DueDate>2026-04-10</cbc:DueDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">380</cbc:InvoiceTypeCode>
  <cbc:TaxPointDate>2026-03-11</cbc:TaxPointDate>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>3100</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw materials and parts</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:OrderReference>
    <cbc:ID>VI-PO-26-0304</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>SM-DA-26-0308</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.serravona.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">0710</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104137</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Serravona Mining</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Zalsul Hekrul Varman</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Strada della Miniera</cbc:StreetName>
        <cbc:BuildingNumber>10</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
        <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
        <cbc:PostalZone>4110</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:ID schemeID="UN/LOCODE">XUSRV</cbc:ID>
        <cbc:Description>The mine and its rail siding</cbc:Description>
        <cbc:Conditions>Unpaved access road; heavy vehicles only.</cbc:Conditions>
        <cbc:InformationURI>https://www.serravona.example</cbc:InformationURI>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">54.00</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">30.60</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Serravona Mining SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007289704</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Serravona Mining SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104137</cbc:CompanyID>
        <cbc:RegistrationDate>1958-06-30</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">120000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Serravona</cbc:CityName>
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
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 0413 24137</cbc:Telephone>
        <cbc:ElectronicMail>sales@serravona.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104137</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
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
        <cbc:ID>qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007299291</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
        <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Ferrano</cbc:CityName>
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
        <cac:SecurityListing>
          <cbc:ID>XU0001042501</cbc:ID>
          <cbc:Description>Ordinary shares of Valdara Industries</cbc:Description>
          <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
          <cbc:MarketCode listID="urn:ubl-examples:world:codelist:MarketCode">XFER</cbc:MarketCode>
        </cac:SecurityListing>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
          <cbc:Value>+999 1 344 474 4274</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
      <cac:ServiceProviderParty>
        <cbc:ID>5-xu-SP-8-xu</cbc:ID>
        <cbc:ServiceTypeCode listID="urn:ubl-examples:world:codelist:ServiceTypeCode">LOGISTICS</cbc:ServiceTypeCode>
        <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
        <cac:Party>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Castrano Logistics</cbc:Name>
          </cac:PartyName>
        </cac:Party>
        <cac:SellerContact>
          <cbc:Name>Key account desk</cbc:Name>
        </cac:SellerContact>
      </cac:ServiceProviderParty>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104137</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Serravona Mining</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-04-10</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode listID="ISO 20022 ClearingChannel2Code">RTGS</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>FERRA-RTGS</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF73SMINV260312</cbc:InstructionNote>
    <cbc:PaymentID>RF73SMINV260312</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU56CREV0000104729</cbc:ID>
      <cbc:Name>Serravona Mining SUA</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice SM-INV-26-0312</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>CREV-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>CREV</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
            <cbc:StreetName>Piazza della Banca</cbc:StreetName>
            <cbc:BuildingNumber>8</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
        <cac:Address>
          <cbc:CityName>Ferrano</cbc:CityName>
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
    <cbc:SettlementDiscountAmount currencyID="XUF">340759</cbc:SettlementDiscountAmount>
    <cbc:PaymentTermsDetailsURI>https://www.serravona.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-04-10</cbc:PaymentDueDate>
    <cac:SettlementPeriod>
      <cbc:StartDate>2026-03-11</cbc:StartDate>
      <cbc:EndDate>2026-03-21</cbc:EndDate>
    </cac:SettlementPeriod>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>8</cbc:InterestRatePercent>
      <cbc:TimeBasisCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">ANN</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:InterestCalculationCode">SIMPLE</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">2839657</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">14198286</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">2839657</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">14198286</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XUF">14198286</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XUF">17037943</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XUF">17037943</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="TNE">1788.4</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XUF">14198286</cbc:LineExtensionAmount>
    <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">17037943</cbc:TaxInclusiveLineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">64</cbc:AllowanceChargeReasonCode>
      <cbc:AllowanceChargeReason>Moisture deduction</cbc:AllowanceChargeReason>
      <cbc:MultiplierFactorNumeric>0.015</cbc:MultiplierFactorNumeric>
      <cbc:Amount currencyID="XUF">216218</cbc:Amount>
      <cbc:BaseAmount currencyID="XUF">14414504</cbc:BaseAmount>
    </cac:AllowanceCharge>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XUF">2839657</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:Item>
      <cbc:Description>Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.</cbc:Description>
      <cbc:Name languageID="qau">Gek trir, zul</cbc:Name>
      <cbc:Name languageID="en-XU">Iron ore, lump</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>SM-ORE-L</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771010000013</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">260111</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">14100</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
      <cac:AdditionalItemProperty>
        <cbc:Name>Iron content</cbc:Name>
        <cbc:ValueQuantity unitCode="P1">62</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XUF">8060</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
    </cac:Price>
    <cac:ItemPriceExtension>
      <cbc:Amount currencyID="XUF">14414504</cbc:Amount>
      <cbc:TaxInclusiveAmount currencyID="XUF">17297405</cbc:TaxInclusiveAmount>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XUF">2882901</cbc:TaxAmount>
      </cac:TaxTotal>
    </cac:ItemPriceExtension>
  </cac:InvoiceLine>
</Invoice>
```
