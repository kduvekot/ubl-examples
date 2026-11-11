# Remittance Advice: Montebrio Power to Kelpstone Gas

*Example 9 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Remittance Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REMITTANCE-ADVICE-SCHEMA)*

The power station pays the invoice and the surcharge, in ferra.

[The XML file](09-RemittanceAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:energy**  
  The business process the document belongs to: the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)".
- `ProfileExecutionID` = **ENERGY-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **MP-RM-26-0160**  
  The power station's number.
- `UUID` = **a612b1d2-c2c5-5799-a3c2-b98476b55f88**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-06**  
  Paid three days after the reminder.
- `IssueTime` = **16:36:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Drek March zhul tirnan, vek drek drastaz skul drek guzzhir.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): What it settles.
- `Note` = **The March gas invoice, with the surcharge of the reminder.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What it settles.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, the currency of the invoice paid; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `TotalDebitAmount` = **134467200** (currencyID `XUF`)  
  The invoice and the surcharge.
- `TotalCreditAmount` = **0** (currencyID `XUF`)  
  No credits.
- `TotalPaymentAmount` = **134467200** (currencyID `XUF`)  
  Transferred in ferra over the trade accord's link.
- `LineCountNumeric` = **2**  
  The invoice and the surcharge.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.montebrio.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Montebrio Power (world/parties.json).
- `Party/IndustryClassificationCode` = **3510** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Montebrio Power (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3510 = Electric power generation, transmission and distribution.
- `Party/PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Montebrio Power (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-105918** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Montebrio Power (world/parties.json).
- `Party/PartyName/Name` = **Montebrio Power**  
  The trading name; identity of Montebrio Power (world/parties.json).
- `Party/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Hekrul Trinskul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via della Centrale** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Montebrio Power (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered for value added tax; identity of Montebrio Power (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007414377**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Montebrio Power (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered, with its legal form; identity of Montebrio Power (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105918**  
  Number in the Commercial register of Urvania; identity of Montebrio Power (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1974-06-01**  
  The day the company was entered in the register; identity of Montebrio Power (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 2935 persons and its turnover of 35700000000 XUF in 2025, by the Trade Accord's limits; identity of Montebrio Power (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **400000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Montebrio Power (world/parties.json).
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
- `Party/Contact/Name` = **Energy trading**  
  The desk that handles this document; identity of Montebrio Power (world/parties.json).
- `Party/Contact/JobTitle` = **Energy trader**  
  The job of the person who answers at the desk; identity of Montebrio Power (world/parties.json).
- `Party/Contact/Department` = **Trading**  
  The department the desk belongs to; identity of Montebrio Power (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 0413 55918**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Montebrio Power (world/parties.json).
- `Party/Contact/ElectronicMail` = **trading@montebrio.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Montebrio Power (world/parties.json).
- `Party/Contact/Note` = **Weekdays 07:00–19:00**  
  When the desk can be reached; identity of Montebrio Power (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Montebrio Power (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.kelpstone.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Kelpstone Gas (world/parties.json).
- `Party/IndustryClassificationCode` = **0620** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Kelpstone Gas (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 0620 = Extraction of natural gas.
- `Party/PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-412877** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Kelpstone Gas (world/parties.json).
- `Party/PartyName/Name` = **Kelpstone Gas**  
  The trading name; identity of Kelpstone Gas (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Shoreline Road**  
  Street of the postal address. identity of Kelpstone Gas (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **2**  
  Building number of the postal address. identity of Kelpstone Gas (world/parties.json).
- `Party/PostalAddress/CityName` = **Gullhaven**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelpstone Gas (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38540**  
  Postal code in Bayvarra's format (5 digits). identity of Kelpstone Gas (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Kelpstone Gas (world/parties.json). The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PhysicalLocation/Description` = **Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/InformationURI` = **https://www.kelpstone.example**  
  Where to find more about the place.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **52.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **18.00** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/PartyTaxScheme/RegistrationName` = **Kelpstone Gas Ltd**  
  The name under which the party is registered for state sales tax; identity of Kelpstone Gas (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **NT-1238631**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Kelpstone Gas (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Northern Territory**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Kelpstone Gas Ltd**  
  The name under which the party is registered, with its legal form; identity of Kelpstone Gas (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412877**  
  Number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **2011-04-01**  
  The day the company was entered in the register; identity of Kelpstone Gas (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 1315 persons and its turnover of 833000000.00 XBL in 2025, by the Trade Accord's limits; identity of Kelpstone Gas (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **120000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Kelpstone Gas (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Gullhaven**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Gas sales**  
  The desk that handles this document; identity of Kelpstone Gas (world/parties.json).
- `Party/Contact/JobTitle` = **Gas sales manager**  
  The job of the person who answers at the desk; identity of Kelpstone Gas (world/parties.json).
- `Party/Contact/Department` = **Commercial**  
  The department the desk belongs to; identity of Kelpstone Gas (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38522 12877**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Kelpstone Gas (world/parties.json).
- `Party/Contact/ElectronicMail` = **gas@kelpstone.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelpstone Gas (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Kelpstone Gas (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412877** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Kelpstone Gas (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  Credit transfer. The code is from UBL's default Payment means (UN/EDIFACT 4461) list: 30 = Credit transfer.
- `PaymentID` = **RF41KGINV260157**  
  The invoice's creditor reference.
- `PayerFinancialAccount/ID` = **XU86CREV0005021992** (schemeID `urn:ubl-examples:world:account`)  
  The power station's account. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayerFinancialAccount/Name` = **Montebrio Power SUA**  
  The account holder, as the bank knows it.
- `PayerFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayerFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayerFinancialAccount/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PayerFinancialAccount/FinancialInstitutionBranch/ID` = **CREV-001**  
  The branch that keeps the account.
- `PayerFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREV**  
  The bank code, the part of every account number that names the bank; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca**  
  The bank's head office; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Its building number; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano**  
  Its town; identity of Crevalto Bank (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The bank's country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Ferrano**  
  The branch is at the bank's head office.
- `PayerFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayerFinancialAccount/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PayeeFinancialAccount/ID` = **XB30BLUM0004817534** (schemeID `urn:ubl-examples:world:account`)  
  The gas producer's account. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Kelpstone Gas Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **BLUM-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUM**  
  The bank code, the part of every account number that names the bank; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  The bank's head office; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Its building number; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  Its town; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The bank's country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The branch is at the bank's head office.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Remittance Advice Line

Inside `RemittanceAdviceLine`:

- `ID` = **1**  
  The invoice.
- `DebitLineAmount` = **132480000** (currencyID `XUF`)  
  Its amount.
- `BillingReference/InvoiceDocumentReference/ID` = **KG-INV-26-0157**  
  The invoice.
- `ID` = **2**  
  The surcharge.
- `DebitLineAmount` = **1987200** (currencyID `XUF`)  
  19872.00 lume in ferra.
- `BillingReference/ReminderDocumentReference/ID` = **KG-DOC-26-0159**  
  The reminder.
- `ExchangeRate/SourceCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The reminder's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `ExchangeRate/TargetCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The payment's. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `ExchangeRate/CalculationRate` = **100**  
  1 lume = 100 ferra.
- `ExchangeRate/MathematicOperatorCode` = **Multiply** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  Lume times the rate. The code is from the world's copy of UBL's Operator list, with a listID: Multiply.
- `ExchangeRate/Date` = **2026-06-06**  
  The payment date.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RemittanceAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:energy</cbc:ProfileID>
  <cbc:ProfileExecutionID>ENERGY-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>MP-RM-26-0160</cbc:ID>
  <cbc:UUID>a612b1d2-c2c5-5799-a3c2-b98476b55f88</cbc:UUID>
  <cbc:IssueDate>2026-06-06</cbc:IssueDate>
  <cbc:IssueTime>16:36:00</cbc:IssueTime>
  <cbc:Note languageID="qau">Drek March zhul tirnan, vek drek drastaz skul drek guzzhir.</cbc:Note>
  <cbc:Note languageID="en-XU">The March gas invoice, with the surcharge of the reminder.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cbc:TotalDebitAmount currencyID="XUF">134467200</cbc:TotalDebitAmount>
  <cbc:TotalCreditAmount currencyID="XUF">0</cbc:TotalCreditAmount>
  <cbc:TotalPaymentAmount currencyID="XUF">134467200</cbc:TotalPaymentAmount>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.montebrio.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3510</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-105918</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Montebrio Power</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Hekrul Trinskul</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via della Centrale</cbc:StreetName>
        <cbc:BuildingNumber>44</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
        <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
        <cbc:PostalZone>4130</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007414377</cbc:CompanyID>
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
        <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105918</cbc:CompanyID>
        <cbc:RegistrationDate>1974-06-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">400000000</cbc:CorporateStockAmount>
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
        <cbc:Name>Energy trading</cbc:Name>
        <cbc:JobTitle>Energy trader</cbc:JobTitle>
        <cbc:Department>Trading</cbc:Department>
        <cbc:Telephone>+999 1 0413 55918</cbc:Telephone>
        <cbc:ElectronicMail>trading@montebrio.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–19:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105918</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.kelpstone.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">0620</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412877</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelpstone Gas</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Shoreline Road</cbc:StreetName>
        <cbc:BuildingNumber>2</cbc:BuildingNumber>
        <cbc:CityName>Gullhaven</cbc:CityName>
        <cbc:PostalZone>38540</cbc:PostalZone>
        <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-NT</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.</cbc:Description>
        <cbc:InformationURI>https://www.kelpstone.example</cbc:InformationURI>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">52.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">18.00</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Kelpstone Gas Ltd</cbc:RegistrationName>
        <cbc:CompanyID>NT-1238631</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Kelpstone Gas Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20412877</cbc:CompanyID>
        <cbc:RegistrationDate>2011-04-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XBL">120000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Gullhaven</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Gas sales</cbc:Name>
        <cbc:JobTitle>Gas sales manager</cbc:JobTitle>
        <cbc:Department>Commercial</cbc:Department>
        <cbc:Telephone>+999 2 38522 12877</cbc:Telephone>
        <cbc:ElectronicMail>gas@kelpstone.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412877</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentID>RF41KGINV260157</cbc:PaymentID>
    <cac:PayerFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU86CREV0005021992</cbc:ID>
      <cbc:Name>Montebrio Power SUA</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
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
    </cac:PayerFinancialAccount>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB30BLUM0004817534</cbc:ID>
      <cbc:Name>Kelpstone Gas Ltd</cbc:Name>
      <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
      <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>BLUM-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>BLUM</cbc:ID>
          <cbc:Name>Bank of Lumeport</cbc:Name>
          <cac:Address>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
            <cbc:StreetName>Exchange Street</cbc:StreetName>
            <cbc:BuildingNumber>48</cbc:BuildingNumber>
            <cbc:CityName>Lumeport</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
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
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:RemittanceAdviceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DebitLineAmount currencyID="XUF">132480000</cbc:DebitLineAmount>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>KG-INV-26-0157</cbc:ID>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
  </cac:RemittanceAdviceLine>
  <cac:RemittanceAdviceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:DebitLineAmount currencyID="XUF">1987200</cbc:DebitLineAmount>
    <cac:BillingReference>
      <cac:ReminderDocumentReference>
        <cbc:ID>KG-DOC-26-0159</cbc:ID>
      </cac:ReminderDocumentReference>
    </cac:BillingReference>
    <cac:ExchangeRate>
      <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:SourceCurrencyCode>
      <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:TargetCurrencyCode>
      <cbc:CalculationRate>100</cbc:CalculationRate>
      <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Multiply</cbc:MathematicOperatorCode>
      <cbc:Date>2026-06-06</cbc:Date>
    </cac:ExchangeRate>
  </cac:RemittanceAdviceLine>
</RemittanceAdvice>
```
