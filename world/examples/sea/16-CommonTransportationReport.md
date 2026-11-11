# Common Transportation Report: Tidewell Ocean Lines to Maritime Administration of Lisavu

*Example 16 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Common Transportation Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-COMMON-TRANSPORTATION-REPORT-SCHEMA)*

The ship flies the island's flag; before entering port the carrier reports to the maritime administration, which also issued the ship's security certificate.

[The XML file](16-CommonTransportationReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **TOL-CTR-26-0141**  
  The carrier's report number.
- `UUID` = **cd4e897c-62e6-5fb8-90e8-b04d34a9df22**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-16**  
  Sent before the ship enters the port of Selanu.
- `IssueTime` = **15:38:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DocumentStatusCode` = **NoStatus** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  A first report. The code is from the world's copy of UBL's Document status list, with a listID: NoStatus = No status on document.
- `ReportTypeCode` = **PREARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportReportTypeCode`)  
  The report before entering the port. The code is from the Trade Accord's transport report type list: PREARRIVAL = Pre-arrival report.
- `ReportType` = **Pre-arrival report**  
  The name of code PREARRIVAL in the Trade Accord's transport report type list.
- `Description` = **The ship's report before arrival at Selanu.**  
  What it is.
- `Note` = **No incidents on board.**  
  The master's note.
- `VersionID` = **1**  
  The first version.

### Reporter Party

Inside `ReporterParty`:

- `WebsiteURI` = **https://www.tidewell.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Tidewell Ocean Lines (world/parties.json).
- `IndustryClassificationCode` = **5012** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Tidewell Ocean Lines (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5012 = Sea and coastal freight water transport.
- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered for state sales tax; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1235754**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Tidewell Ocean Lines (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered, with its legal form; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411918**  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1974-03-01**  
  The day the company was entered in the register; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **CORP** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: CORP = Corporation (public).
- `PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The name of code CORP in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 776 persons and its turnover of 865000000.00 XBL in 2025, by the Trade Accord's limits; identity of Tidewell Ocean Lines (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **40000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Bookings**  
  The desk that handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2418 1918**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Authority Party

Inside `AuthorityParty`:

- `IndustryClassificationCode` = **8413** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Maritime Administration of Lisavu (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 8413 = Regulation of and contribution to more efficient operation of businesses.
- `PartyIdentification/ID` = **IC42270** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Maritime Administration of Lisavu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Maritime Administration of Lisavu**  
  The trading name; identity of Maritime Administration of Lisavu (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/BuildingNumber` = **37**  
  Building number of the postal address. identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Maritime Administration of Lisavu**  
  The name under which the party is registered, with its legal form; identity of Maritime Administration of Lisavu (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42270**  
  Number in the Island companies register; identity of Maritime Administration of Lisavu (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Contact/Name` = **Ship registry**  
  The desk that handles this document; identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/Telephone` = **+999 3 720 2270**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/ElectronicMail` = **ship@maritime-xl.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Maritime Administration of Lisavu (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42270** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Maritime Administration of Lisavu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC42270** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Maritime Administration of Lisavu**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.

### Reporting Location

Inside `ReportingLocation`:

- `Name` = **At sea, 40 nautical miles off Selanu**  
  Where the report was made.

### Shipment

Inside `Shipment`:

- `ID` = **LD-SH-26-0132**  
  The shipment the report is for.
- `ShipmentStage/ID` = **1**  
  The sea leg to Selanu.
- `ShipmentStage/TerminalOperatorParty/WebsiteURI` = **https://www.port-selanu.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/IndustryClassificationCode` = **5222** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Port of Selanu (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5222 = Service activities incidental to water transportation.
- `ShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Port of Selanu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ShipmentStage/TerminalOperatorParty/PartyName/Name` = **Port of Selanu**  
  The trading name; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `ShipmentStage/TerminalOperatorParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address. identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/Description` = **Port of Selanu**  
  Where the party actually operates, apart from its postal address.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/InformationURI` = **https://www.port-selanu.example**  
  Where to find more about the place.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **40** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **1.20** (unitCode `D61`)  
  The minutes of the latitude.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **8.40** (unitCode `D61`)  
  The minutes of the longitude.
- `ShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Port of Selanu Ltd**  
  The name under which the party is registered, with its legal form; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **IC41037**  
  Number in the Island companies register; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The name of code LTD in Lisavu's national company legal form list.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 28 persons and its turnover of 3490000.000 XLC in 2025, by the Trade Accord's limits; identity of Port of Selanu (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/TerminalOperatorParty/Contact/Name` = **Port control**  
  The desk that handles this document; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 3 727 1037**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **port@port-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41037** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Port of Selanu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `ShipmentStage/PassengerPerson/FirstName` = **Ines**  
  The one passenger, a supercargo.
- `ShipmentStage/PassengerPerson/FamilyName` = **Tavari**  
  The family name.
- `ShipmentStage/PassengerPerson/RoleCode` = **PASSENGER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: PASSENGER = Passenger.
- `ShipmentStage/ReportingPerson/FirstName` = **Corin**  
  The master reports.
- `ShipmentStage/ReportingPerson/FamilyName` = **Halvard**  
  The family name.
- `ShipmentStage/ReportingPerson/RoleCode` = **MASTER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MASTER = Master.
- `ShipmentStage/CrewMemberPerson/FirstName` = **Corin**  
  The master.
- `ShipmentStage/CrewMemberPerson/FamilyName` = **Halvard**  
  The family name.
- `ShipmentStage/CrewMemberPerson/RoleCode` = **MASTER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MASTER = Master.
- `ShipmentStage/CrewMemberPerson/FirstName` = **Elsbeth**  
  The chief officer, also the ship's medical officer.
- `ShipmentStage/CrewMemberPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/CrewMemberPerson/RoleCode` = **CHIEFOFFICER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFOFFICER = Chief officer.
- `ShipmentStage/CrewMemberPerson/FirstName` = **Rafe**  
  The chief engineer.
- `ShipmentStage/CrewMemberPerson/FamilyName` = **Dunmore**  
  The family name.
- `ShipmentStage/CrewMemberPerson/RoleCode` = **CHIEFENG** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFENG = Chief engineer.
- `ShipmentStage/SecurityOfficerPerson/FirstName` = **Elsbeth**  
  The ship security officer.
- `ShipmentStage/SecurityOfficerPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/SecurityOfficerPerson/RoleCode` = **SSO** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: SSO = Ship security officer.
- `ShipmentStage/ShipsSurgeonPerson/FirstName` = **Elsbeth**  
  No surgeon on a feeder: the chief officer is the medical officer.
- `ShipmentStage/ShipsSurgeonPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/ShipsSurgeonPerson/RoleCode` = **MEDICAL** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MEDICAL = Medical officer.
- `ShipmentStage/DestinationPortCall/ID` = **XLSEL-26-0517**  
  The port call at Selanu.
- `ShipmentStage/DestinationPortCall/PlannedOperationsDescription` = **Discharge one container, load six.**  
  What the ship will do.
- `ShipmentStage/DestinationPortCall/PlannedWorksDescription` = **None.**  
  No repairs planned.
- `ShipmentStage/DestinationPortCall/PlannedInspectionsDescription` = **Port state control is due.**  
  An inspection is expected.
- `ShipmentStage/DestinationPortCall/ExpectedAnchorageIndicator` = **false**  
  Straight to the berth.
- `ShipmentStage/DestinationPortCall/PositionInPortID` = **BERTH-2**  
  The container berth.
- `ShipmentStage/DestinationPortCall/CargoAndBallastTankConditionDescription` = **Tanks clean; ballast exchanged at sea.**  
  Their condition.
- `ShipmentStage/DestinationPortCall/ShipRequirement/ID` = **SR-1**  
  A need of the ship.
- `ShipmentStage/DestinationPortCall/ShipRequirement/Description` = **Fresh water, 40 tonnes.**  
  What it needs.
- `ShipmentStage/DestinationPortCall/PrimaryPortCallPurpose/PurposeTypeCode` = **CARGO** (listID `urn:ubl-examples:world:codelist:PortCallPurposeCode`)  
  Cargo operations. The code is from the Trade Accord's port call purpose list: CARGO = Cargo operations.
- `ShipmentStage/DestinationPortCall/PrimaryPortCallPurpose/PurposeType` = **Cargo operations**  
  The name of code CARGO in the Trade Accord's port call purpose list.
- `ShipmentStage/DestinationPortCall/PrimaryPortCallPurpose/Description` = **Discharge and load containers.**  
  The purpose.
- `ShipmentStage/DestinationPortCall/AdditionalPortCallPurpose/PurposeTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:PortCallPurposeCode`)  
  Taking on water. The code is from the Trade Accord's port call purpose list: WATER = Fresh water bunkering.
- `ShipmentStage/DestinationPortCall/AdditionalPortCallPurpose/PurposeType` = **Fresh water bunkering**  
  The name of code WATER in the Trade Accord's port call purpose list.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/IdentificationID` = **ARR-XLSEL-0517**  
  The requested arrival.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceDate` = **2026-05-18**  
  The day.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceTime` = **06:00:00**  
  At first light.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/TypeCode` = **ARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  An arrival. The code is from the Trade Accord's transport event type list: ARRIVAL = Arrival.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/Description` = **Pilot on board at the fairway buoy.**  
  What is asked.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/CompletionIndicator` = **false**  
  Not yet.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/CurrentStatus/ConditionCode` = **ONTIME** (listID `urn:ubl-examples:world:codelist:StatusConditionCode`)  
  Expected on time. The code is from the Trade Accord's status condition list: ONTIME = On time.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/Contact/Name` = **Bridge**  
  Whom to call.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/Contact/Telephone` = **+999 3 790 2117**  
  The ship's phone, in the island's maritime range (79), as the ship flies the island's flag.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceLocation/Name` = **Selanu fairway buoy**  
  Where the pilot boards.
- `ShipmentStage/ShipStoreArticle/ID` = **ST-1**  
  Spirits in the bonded store.
- `ShipmentStage/ShipStoreArticle/Name` = **Spirits**  
  What.
- `ShipmentStage/ShipStoreArticle/Quantity` = **24** (unitCode `LTR`)  
  Litres.
- `ShipmentStage/ShipStoreArticle/OfficialUse` = **Sealed by customs at Lumeport.**  
  Under seal.
- `ShipmentStage/ShipStoreArticle/Stowage/LocationID` = **BOND-1**  
  The bonded locker.
- `ShipmentStage/ShipStoreArticle/Stowage/Location` = **Bonded locker, accommodation deck**  
  Where.
- `ShipmentStage/ShipStoreArticle/ID` = **ST-2**  
  Cigarettes.
- `ShipmentStage/ShipStoreArticle/Name` = **Cigarettes**  
  What.
- `ShipmentStage/ShipStoreArticle/Quantity` = **2000** (unitCode `EA`)  
  Pieces, counted each (EA).
- `ShipmentStage/CrewPersonEffect/EffectDescription` = **One camera, one laptop.**  
  What the crew member declares.
- `ShipmentStage/CrewPersonEffect/CrewPerson/FirstName` = **Rafe**  
  The chief engineer.
- `ShipmentStage/CrewPersonEffect/CrewPerson/FamilyName` = **Dunmore**  
  The family name.
- `ShipmentStage/CrewPersonEffect/CrewPerson/RoleCode` = **CHIEFENG** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFENG = Chief engineer.
- `ShipmentStage/MaritimeWaste/ID` = **W-1**  
  Oily waste.
- `ShipmentStage/MaritimeWaste/Description` = **Sludge from the fuel separators.**  
  What.
- `ShipmentStage/MaritimeWaste/WasteTypeCode` = **OIL** (listID `urn:ubl-examples:world:codelist:ShipWasteTypeCode`)  
  MARPOL Annex I waste. The code is from the Trade Accord's ship waste type list: OIL = Oily waste.
- `ShipmentStage/MaritimeWaste/ToBeDeliveredMeasure` = **2.4** (unitCode `MTQ`)  
  To be delivered at Selanu.
- `ShipmentStage/MaritimeWaste/RetainedOnBoardMeasure` = **0.6** (unitCode `MTQ`)  
  Kept on board.
- `ShipmentStage/MaritimeWaste/MaxDedicatedStorageCapacityMeasure` = **8** (unitCode `MTQ`)  
  The tank's capacity.
- `ShipmentStage/MaritimeWaste/EstimatedGeneratedUntilNextPortMeasure` = **0.8** (unitCode `MTQ`)  
  Until Lumeport again.
- `ShipmentStage/MaritimeWaste/RemainingWasteDeliveryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/MaritimeWaste/RemainingWasteDeliveryPortLocation/Name` = **Port of Lumeport**  
  The rest goes ashore at Lumeport.
- `ShipmentStage/MaritimeWaste/RemainingWasteDeliveryPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/MaritimeWaste/ID` = **W-2**  
  Garbage.
- `ShipmentStage/MaritimeWaste/Description` = **Food and packaging waste.**  
  What.
- `ShipmentStage/MaritimeWaste/WasteTypeCode` = **GARBAGE** (listID `urn:ubl-examples:world:codelist:ShipWasteTypeCode`)  
  MARPOL Annex V waste. The code is from the Trade Accord's ship waste type list: GARBAGE = Garbage.
- `ShipmentStage/MaritimeWaste/ToBeDeliveredMeasure` = **1.5** (unitCode `MTQ`)  
  To be delivered.
- `ShipmentStage/BallastWaterSummary/ID` = **BW-26-0517**  
  The ballast water report.
- `ShipmentStage/BallastWaterSummary/ManagementPlanOnBoardIndicator` = **true**  
  The plan is on board.
- `ShipmentStage/BallastWaterSummary/ManagementPlanImplementedIndicator` = **true**  
  And followed.
- `ShipmentStage/BallastWaterSummary/IMOGuidelinesOnBoardIndicator` = **true**  
  The IMO guidelines are on board.
- `ShipmentStage/BallastWaterSummary/TotalBallastTanksOnBoardQuantity` = **8** (unitCode `EA`)  
  Ballast tanks.
- `ShipmentStage/BallastWaterSummary/TanksInBallastQuantity` = **4** (unitCode `EA`)  
  Tanks with ballast now.
- `ShipmentStage/BallastWaterSummary/TanksExchangedQuantity` = **4** (unitCode `EA`)  
  Exchanged at sea.
- `ShipmentStage/BallastWaterSummary/TanksNotExchangedQuantity` = **0** (unitCode `EA`)  
  None left unexchanged.
- `ShipmentStage/BallastWaterSummary/TotalBallastWaterOnBoardMeasure` = **1240** (unitCode `TNE`)  
  Ballast on board.
- `ShipmentStage/BallastWaterSummary/TotalBallastWaterCapacityMeasure` = **2480** (unitCode `TNE`)  
  The capacity.
- `ShipmentStage/BallastWaterSummary/OtherControlActions` = **None.**  
  No other measures.
- `ShipmentStage/BallastWaterSummary/NoControlActionsReason` = **Exchange done at more than 200 nautical miles from land.**  
  Why no treatment was needed.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankID` = **BT-3**  
  The tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankTypeCode` = **WING** (listID `urn:ubl-examples:world:codelist:BallastTankTypeCode`)  
  A wing tank. The code is from the Trade Accord's ballast tank type list: WING = Wing tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Taken up at Lumeport: 310 cubic metres. A volume needs a volume unit; the 310 were meant as tonnes of water, which is about the same number of cubic metres.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SeaHeightMeasure` = **2** (unitCode `MTR`)  
  The depth of the intake.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SalinityMeasure` = **30** (unitCode `GL`)  
  Salinity.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TransactionDate` = **2026-05-14**  
  At Lumeport.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Name` = **Port of Lumeport**  
  The port.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/AttributeID` = **Water**  
  The water.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/Measure` = **16** (unitCode `CEL`)  
  Its temperature.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TankID` = **BT-3**  
  The tank.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangeMethodCode` = **SEQ** (listID `urn:ubl-examples:world:codelist:BallastExchangeMethodCode`)  
  Emptied and refilled. The code is from the Trade Accord's ballast water exchange method list: SEQ = Sequential.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangedPercent` = **95**  
  Of the volume.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Exchanged: the same 310 cubic metres (a volume, so in cubic metres; a tonne of water is about a cubic metre).
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TransactionDate` = **2026-05-16**  
  At sea.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/Location/Name` = **At sea, 120 nautical miles west of Selanu**  
  Where.
- `ShipmentStage/BallastWaterSummary/DischargeBallastWaterTransaction/TankID` = **BT-3**  
  The tank.
- `ShipmentStage/BallastWaterSummary/DischargeBallastWaterTransaction/VolumeMeasure` = **120** (unitCode `MTQ`)  
  To be discharged at Selanu: 120 cubic metres (a volume; a tonne of water is about a cubic metre, so the number stays).
- `ShipmentStage/BallastWaterSummary/DischargeBallastWaterTransaction/TransactionDate` = **2026-05-18**  
  In port.
- `ShipmentStage/BallastWaterSummary/ResponsibleOfficerPerson/FirstName` = **Elsbeth**  
  The chief officer, also the ship's medical officer.
- `ShipmentStage/BallastWaterSummary/ResponsibleOfficerPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/BallastWaterSummary/ResponsibleOfficerPerson/RoleCode` = **CHIEFOFFICER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFOFFICER = Chief officer.
- `ShipmentStage/ISPSRequirements/ID` = **ISSC-XL-2026-0117**  
  The number of the ship's International Ship Security Certificate.
- `ShipmentStage/ISPSRequirements/ValidISSCIndicator` = **true**  
  The ship holds a valid security certificate.
- `ShipmentStage/ISPSRequirements/ISSCAbsenceReason` = **Not applicable: the certificate is on board.**  
  Stated, not left out.
- `ShipmentStage/ISPSRequirements/ISSCExpiryDate` = **2028-09-30**  
  The certificate is valid for five years from its issue.
- `ShipmentStage/ISPSRequirements/SSPOnBoardIndicator` = **true**  
  The security plan is on board.
- `ShipmentStage/ISPSRequirements/SSPSecurityMeasuresAppliedIndicator` = **true**  
  Its measures were applied.
- `ShipmentStage/ISPSRequirements/CurrentOperatingSecurityLevelCode` = **1** (listID `IMO ISPS security level`)  
  Security level 1, the normal level. The code is from the world's copy of IMO ISPS Code security level: 1 = Security level 1.
- `ShipmentStage/ISPSRequirements/AdditionalMattersDescription` = **None.**  
  Nothing else to report.
- `ShipmentStage/ISPSRequirements/AdditionalSecurityMeasure/ID` = **SM-1**  
  An extra measure.
- `ShipmentStage/ISPSRequirements/AdditionalSecurityMeasure/Description` = **Gangway watch at Selanu.**  
  What the ship adds.
- `ShipmentStage/ISPSRequirements/PortCallRecord/ID` = **PCR-1**  
  The last port call.
- `ShipmentStage/ISPSRequirements/PortCallRecord/SecurityLevelCode` = **1** (listID `IMO ISPS security level`)  
  Security level 1 at Lumeport. The code is from the world's copy of IMO ISPS Code security level: 1 = Security level 1.
- `ShipmentStage/ISPSRequirements/PortCallRecord/SecurityMeasure/Description` = **Normal access control.**  
  The measures.
- `ShipmentStage/ISPSRequirements/PortCallRecord/PortFacilityLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/ISPSRequirements/PortCallRecord/PortFacilityLocation/Name` = **Port of Lumeport**  
  The port facility.
- `ShipmentStage/ISPSRequirements/PortCallRecord/PortFacilityLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/ISPSRequirements/PortCallRecord/Period/StartDate` = **2026-05-13**  
  Arrived.
- `ShipmentStage/ISPSRequirements/PortCallRecord/Period/EndDate` = **2026-05-14**  
  Sailed.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/ID` = **STS-0**  
  Ship-to-ship activity.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Description` = **None during the last ten port calls.**  
  The record.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/AppliedSecurityMeasure/ID` = **SM-0**  
  No measure needed.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/AppliedSecurityMeasure/Description` = **None: no ship-to-ship activity.**  
  Stated.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Period/StartDate` = **2026-01-01**  
  Since.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Period/EndDate` = **2026-05-17**  
  Until now.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/Name` = **At sea, 120 nautical miles west of Selanu**  
  Where.
- `ShipmentStage/ISPSRequirements/ReportLocation/Name` = **At sea, 120 nautical miles west of Selanu**  
  Where.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyIdentification/ID` = **IC42270** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyName/Name` = **Maritime Administration of Lisavu**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `ShipmentStage/ISPSRequirements/SecurityOfficerPerson/FirstName` = **Elsbeth**  
  The chief officer, also the ship's medical officer.
- `ShipmentStage/ISPSRequirements/SecurityOfficerPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/ISPSRequirements/SecurityOfficerPerson/RoleCode` = **CHIEFOFFICER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFOFFICER = Chief officer.
- `ShipmentStage/MaritimeHealthDeclaration/ID` = **MDH-26-0517**  
  The maritime declaration of health.
- `ShipmentStage/MaritimeHealthDeclaration/InfectiousDiseaseCaseOnBoardIndicator` = **false**  
  No infectious disease.
- `ShipmentStage/MaritimeHealthDeclaration/MoreIllThanExpectedIndicator` = **false**  
  No more ill than usual.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalPractitionerConsultedIndicator` = **true**  
  A doctor was consulted by radio.
- `ShipmentStage/MaritimeHealthDeclaration/StowawaysFoundOnBoardIndicator` = **false**  
  No stowaways.
- `ShipmentStage/MaritimeHealthDeclaration/SickAnimalOnBoardIndicator` = **false**  
  No sick animals.
- `ShipmentStage/MaritimeHealthDeclaration/FumigatedCargoTransportIndicator` = **false**  
  No fumigated cargo.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasuresAppliedIndicator` = **true**  
  The galley was disinfected.
- `ShipmentStage/MaritimeHealthDeclaration/ValidSanitationCertificateOnBoardIndicator` = **true**  
  The certificate is valid.
- `ShipmentStage/MaritimeHealthDeclaration/ReinspectionRequiredIndicator` = **false**  
  No reinspection needed.
- `ShipmentStage/MaritimeHealthDeclaration/TotalDeadPersonQuantity` = **0** (unitCode `IE`)  
  No persons.
- `ShipmentStage/MaritimeHealthDeclaration/TotalIllPersonQuantity` = **1** (unitCode `IE`)  
  One person: a crew member with a sprained wrist.
- `ShipmentStage/MaritimeHealthDeclaration/SickAnimalDescription` = **None on board.**  
  No animals.
- `ShipmentStage/MaritimeHealthDeclaration/StowawayDescription` = **None found in the search before departure.**  
  The search.
- `ShipmentStage/MaritimeHealthDeclaration/LastDrinkingWaterAnalysisDate` = **2026-04-02**  
  The last water test.
- `ShipmentStage/MaritimeHealthDeclaration/WHOAffectedAreaVisit/VisitDate` = **2026-03-28**  
  No affected area in the last 30 days: the last port visited was Lumeport.
- `ShipmentStage/MaritimeHealthDeclaration/WHOAffectedAreaVisit/WHOAffectedAreaPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/MaritimeHealthDeclaration/WHOAffectedAreaVisit/WHOAffectedAreaPortLocation/Name` = **Port of Lumeport**  
  Not an affected area.
- `ShipmentStage/MaritimeHealthDeclaration/WHOAffectedAreaVisit/WHOAffectedAreaPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/ID` = **HI-1**  
  The one incident.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/JoinedShipDate` = **2025-11-01**  
  When the person joined.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/NatureOfIllnessDescription` = **Sprained wrist.**  
  What happened.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/OnsetDate` = **2026-05-16**  
  When.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/ReportedToMedicalOfficerIndicator` = **true**  
  Reported.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/GivenTreatmentDescription` = **Bandage and rest.**  
  Treatment.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/StillIllIndicator` = **true**  
  Still recovering.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/DiedIndicator` = **false**  
  No.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/StillOnBoardIndicator` = **true**  
  On board.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/EvacuatedIndicator` = **false**  
  Not evacuated.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/BuriedAtSeaIndicator` = **false**  
  No.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Note` = **Fit for light duty.**  
  The status.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Person/FirstName` = **Rafe**  
  The chief engineer.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Person/FamilyName` = **Dunmore**  
  The family name.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Person/RoleCode` = **CHIEFENG** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFENG = Chief engineer.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasure/SanitaryMeasureTypeCode` = **DISINFECT** (listID `urn:ubl-examples:world:codelist:SanitaryMeasureCode`)  
  The galley was disinfected. The code is from the Trade Accord's sanitary measure list: DISINFECT = Disinfection.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasure/ApplicationDate` = **2026-05-15**  
  When.
- `ShipmentStage/MaritimeHealthDeclaration/PlaceOfReportLocation/Name` = **At sea, 120 nautical miles west of Selanu**  
  Where.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalCertificate/ID` = **MC-TH-2026**  
  The ship's medicine chest certificate.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalCertificate/CertificateType` = **Medicine chest**  
  Its kind.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlCertificate/ID` = **SSCC-XB-2025-0911**  
  The sanitation control certificate.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlCertificate/CertificateType` = **Ship sanitation control**  
  Its kind.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/ID` = **none**  
  No exemption: the ship holds the control certificate.
- `ShipmentStage/FuelConsumption/ID` = **FC-26-19E**  
  The fuel of the voyage.
- `ShipmentStage/FuelConsumption/FuelTypeCode` = **MGO** (listID `urn:ubl-examples:world:codelist:FuelTypeCode`)  
  Marine gas oil. The code is from the Trade Accord's fuel type list: MGO = Marine gas oil.
- `ShipmentStage/FuelConsumption/FuelType` = **Marine gas oil, 0.1 % sulphur**  
  In words.
- `ShipmentStage/FuelConsumption/FuelConsumptionMeasure` = **38** (unitCode `TNE`)  
  Used from Lumeport.
- `ShipmentStage/FuelConsumption/AdditionalFuelProperty/TypeID` = **Sulphur**  
  The sulphur content.
- `ShipmentStage/FuelConsumption/AdditionalFuelProperty/Value` = **0.1 %**  
  Its value.
- `ShipmentStage/FuelConsumption/FuelMetering/TypeID` = **FlowMeter**  
  Measured by the flow meter.
- `ShipmentStage/FuelConsumption/FuelMetering/Value` = **38.2 t**  
  The reading.
- `ShipmentStage/FuelConsumption/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Carbon dioxide. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `ShipmentStage/FuelConsumption/EnvironmentalEmission/ValueMeasure` = **122** (unitCode `TNE`)  
  From 38 t of gas oil.
- `ShipmentStage/FuelConsumption/FuelProviderParty/PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/FuelConsumption/FuelProviderParty/PartyName/Name` = **Port of Lumeport**  
  A party referred to from another party's details: its identifier and name are enough.

### Transport Means

Inside `TransportMeans`:

- `JourneyID` = **TH-26-19E**  
  The voyage.
- `RegistrationNationalityID` = **XB**  
  The country the means of transport is registered in.
- `RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `DirectionCode` = **EB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: EB = Eastbound.
- `TransportMeansTypeCode` = **CONTAINERSHIP** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The kind of means of transport: tidewell harbour; the fleet of Tidewell Ocean Lines (world/parties.json). The code is from the Trade Accord's transport means type list: CONTAINERSHIP = Container ship.
- `MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines (world/parties.json).
- `MaritimeTransport/RadioCallSignID` = **XBTH7**  
  The radio call sign, with the world's country code.
- `MaritimeTransport/MMSIRegistrationID` = **999702117**  
  The Maritime Mobile Service Identity, nine digits; 999 is no real country's maritime identification digits.
- `MaritimeTransport/ShipsRequirements` = **Shore power at the container quay.**  
  What the ship needs in port.
- `MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `MaritimeTransport/SegregatedBallastMeasure` = **2480** (unitCode `TNE`)  
  The capacity of the tanks for ballast water only.
- `MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 1,000 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `MaritimeTransport/INFShipClassCode` = **INF1** (listID `IMO INF Code`)  
  IMO INF class 1: may not carry irradiated fuel in quantity. The code is from the world's copy of IMO INF Code ship class: INF1 = INF.1 ship.
- `MaritimeTransport/AntennaLocus` = **Mast, 28 m above the waterline**  
  Where the AIS antenna is.
- `MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `MaritimeTransport/VesselDynamics/NavigationStatusCode` = **0** (listID `ITU-R M.1371 Navigational status`)  
  AIS status 0: under way using engine. The code is from the world's copy of ITU-R M.1371 AIS navigational status: 0 = Under way using engine.
- `MaritimeTransport/VesselDynamics/AtAnchorageIndicator` = **false**  
  Not at anchor.
- `MaritimeTransport/VesselDynamics/CourseOverGroundDirection` = **088**  
  Course over ground, in degrees.
- `MaritimeTransport/VesselDynamics/SpeedOverGroundMeasure` = **13.5** (unitCode `KNT`)  
  Speed over ground.
- `MaritimeTransport/VesselDynamics/RateOfTurnMeasure` = **0** (unitCode `E96`)  
  Not turning: 0 degrees per second.

### Document Reference

Inside `DocumentReference`:

- `ID` = **TOL-MF-26-0140**  
  The cargo manifest.

### Signature

Inside `Signature`:

- `ID` = **TWL-SIG-CTR**  
  The master's signature.
- `SignatoryParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CommonTransportationReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:CommonTransportationReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TOL-CTR-26-0141</cbc:ID>
  <cbc:UUID>cd4e897c-62e6-5fb8-90e8-b04d34a9df22</cbc:UUID>
  <cbc:IssueDate>2026-05-16</cbc:IssueDate>
  <cbc:IssueTime>15:38:00</cbc:IssueTime>
  <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">NoStatus</cbc:DocumentStatusCode>
  <cbc:ReportTypeCode listID="urn:ubl-examples:world:codelist:TransportReportTypeCode">PREARRIVAL</cbc:ReportTypeCode>
  <cbc:ReportType>Pre-arrival report</cbc:ReportType>
  <cbc:Description>The ship's report before arrival at Selanu.</cbc:Description>
  <cbc:Note>No incidents on board.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ReporterParty>
    <cbc:WebsiteURI>https://www.tidewell.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5012</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
      <cbc:CompanyID>CO-1235754</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
      <cbc:CompanyID>20411918</cbc:CompanyID>
      <cbc:RegistrationDate>1974-03-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">CORP</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XBL">40000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Lumeport</cbc:CityName>
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
      <cbc:Name>Bookings</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38 2418 1918</cbc:Telephone>
      <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReporterParty>
  <cac:AuthorityParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">8413</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42270</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XB">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>37</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Maritime Administration of Lisavu</cbc:RegistrationName>
      <cbc:CompanyID>IC42270</cbc:CompanyID>
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
      <cbc:Name>Ship registry</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 3 720 2270</cbc:Telephone>
      <cbc:ElectronicMail>ship@maritime-xl.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42270</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:AuthorityParty>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42270</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:ReportingLocation>
    <cbc:Name>At sea, 40 nautical miles off Selanu</cbc:Name>
  </cac:ReportingLocation>
  <cac:Shipment>
    <cbc:ID>LD-SH-26-0132</cbc:ID>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cac:TerminalOperatorParty>
        <cbc:WebsiteURI>https://www.port-selanu.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5222</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Port of Selanu</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XB">Wharf Road</cbc:StreetName>
          <cbc:BuildingNumber>32</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PhysicalLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Description>Port of Selanu</cbc:Description>
          <cbc:InformationURI>https://www.port-selanu.example</cbc:InformationURI>
          <cac:LocationCoordinate>
            <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
            <cbc:LatitudeDegreesMeasure unitCode="DD">40</cbc:LatitudeDegreesMeasure>
            <cbc:LatitudeMinutesMeasure unitCode="D61">1.20</cbc:LatitudeMinutesMeasure>
            <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
            <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
            <cbc:LongitudeMinutesMeasure unitCode="D61">8.40</cbc:LongitudeMinutesMeasure>
            <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
          </cac:LocationCoordinate>
        </cac:PhysicalLocation>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Port of Selanu Ltd</cbc:RegistrationName>
          <cbc:CompanyID>IC41037</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
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
          <cbc:Name>Port control</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 3 727 1037</cbc:Telephone>
          <cbc:ElectronicMail>port@port-selanu.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41037</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
      <cac:PassengerPerson>
        <cbc:FirstName>Ines</cbc:FirstName>
        <cbc:FamilyName>Tavari</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">PASSENGER</cbc:RoleCode>
      </cac:PassengerPerson>
      <cac:ReportingPerson>
        <cbc:FirstName>Corin</cbc:FirstName>
        <cbc:FamilyName>Halvard</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MASTER</cbc:RoleCode>
      </cac:ReportingPerson>
      <cac:CrewMemberPerson>
        <cbc:FirstName>Corin</cbc:FirstName>
        <cbc:FamilyName>Halvard</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MASTER</cbc:RoleCode>
      </cac:CrewMemberPerson>
      <cac:CrewMemberPerson>
        <cbc:FirstName>Elsbeth</cbc:FirstName>
        <cbc:FamilyName>Marrin</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFOFFICER</cbc:RoleCode>
      </cac:CrewMemberPerson>
      <cac:CrewMemberPerson>
        <cbc:FirstName>Rafe</cbc:FirstName>
        <cbc:FamilyName>Dunmore</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFENG</cbc:RoleCode>
      </cac:CrewMemberPerson>
      <cac:SecurityOfficerPerson>
        <cbc:FirstName>Elsbeth</cbc:FirstName>
        <cbc:FamilyName>Marrin</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">SSO</cbc:RoleCode>
      </cac:SecurityOfficerPerson>
      <cac:ShipsSurgeonPerson>
        <cbc:FirstName>Elsbeth</cbc:FirstName>
        <cbc:FamilyName>Marrin</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MEDICAL</cbc:RoleCode>
      </cac:ShipsSurgeonPerson>
      <cac:DestinationPortCall>
        <cbc:ID>XLSEL-26-0517</cbc:ID>
        <cbc:PlannedOperationsDescription>Discharge one container, load six.</cbc:PlannedOperationsDescription>
        <cbc:PlannedWorksDescription>None.</cbc:PlannedWorksDescription>
        <cbc:PlannedInspectionsDescription>Port state control is due.</cbc:PlannedInspectionsDescription>
        <cbc:ExpectedAnchorageIndicator>false</cbc:ExpectedAnchorageIndicator>
        <cbc:PositionInPortID>BERTH-2</cbc:PositionInPortID>
        <cbc:CargoAndBallastTankConditionDescription>Tanks clean; ballast exchanged at sea.</cbc:CargoAndBallastTankConditionDescription>
        <cac:ShipRequirement>
          <cbc:ID>SR-1</cbc:ID>
          <cbc:Description>Fresh water, 40 tonnes.</cbc:Description>
        </cac:ShipRequirement>
        <cac:PrimaryPortCallPurpose>
          <cbc:PurposeTypeCode listID="urn:ubl-examples:world:codelist:PortCallPurposeCode">CARGO</cbc:PurposeTypeCode>
          <cbc:PurposeType>Cargo operations</cbc:PurposeType>
          <cbc:Description>Discharge and load containers.</cbc:Description>
        </cac:PrimaryPortCallPurpose>
        <cac:AdditionalPortCallPurpose>
          <cbc:PurposeTypeCode listID="urn:ubl-examples:world:codelist:PortCallPurposeCode">WATER</cbc:PurposeTypeCode>
          <cbc:PurposeType>Fresh water bunkering</cbc:PurposeType>
        </cac:AdditionalPortCallPurpose>
        <cac:RequestedArrivalEvent>
          <cbc:IdentificationID>ARR-XLSEL-0517</cbc:IdentificationID>
          <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:00:00</cbc:OccurrenceTime>
          <cbc:TypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">ARRIVAL</cbc:TypeCode>
          <cbc:Description>Pilot on board at the fairway buoy.</cbc:Description>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:CurrentStatus>
            <cbc:ConditionCode listID="urn:ubl-examples:world:codelist:StatusConditionCode">ONTIME</cbc:ConditionCode>
          </cac:CurrentStatus>
          <cac:Contact>
            <cbc:Name>Bridge</cbc:Name>
            <cbc:Telephone>+999 3 790 2117</cbc:Telephone>
          </cac:Contact>
          <cac:OccurrenceLocation>
            <cbc:Name>Selanu fairway buoy</cbc:Name>
          </cac:OccurrenceLocation>
        </cac:RequestedArrivalEvent>
      </cac:DestinationPortCall>
      <cac:ShipStoreArticle>
        <cbc:ID>ST-1</cbc:ID>
        <cbc:Name>Spirits</cbc:Name>
        <cbc:Quantity unitCode="LTR">24</cbc:Quantity>
        <cbc:OfficialUse>Sealed by customs at Lumeport.</cbc:OfficialUse>
        <cac:Stowage>
          <cbc:LocationID>BOND-1</cbc:LocationID>
          <cbc:Location>Bonded locker, accommodation deck</cbc:Location>
        </cac:Stowage>
      </cac:ShipStoreArticle>
      <cac:ShipStoreArticle>
        <cbc:ID>ST-2</cbc:ID>
        <cbc:Name>Cigarettes</cbc:Name>
        <cbc:Quantity unitCode="EA">2000</cbc:Quantity>
      </cac:ShipStoreArticle>
      <cac:CrewPersonEffect>
        <cbc:EffectDescription>One camera, one laptop.</cbc:EffectDescription>
        <cac:CrewPerson>
          <cbc:FirstName>Rafe</cbc:FirstName>
          <cbc:FamilyName>Dunmore</cbc:FamilyName>
          <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFENG</cbc:RoleCode>
        </cac:CrewPerson>
      </cac:CrewPersonEffect>
      <cac:MaritimeWaste>
        <cbc:ID>W-1</cbc:ID>
        <cbc:Description>Sludge from the fuel separators.</cbc:Description>
        <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:ShipWasteTypeCode">OIL</cbc:WasteTypeCode>
        <cbc:ToBeDeliveredMeasure unitCode="MTQ">2.4</cbc:ToBeDeliveredMeasure>
        <cbc:RetainedOnBoardMeasure unitCode="MTQ">0.6</cbc:RetainedOnBoardMeasure>
        <cbc:MaxDedicatedStorageCapacityMeasure unitCode="MTQ">8</cbc:MaxDedicatedStorageCapacityMeasure>
        <cbc:EstimatedGeneratedUntilNextPortMeasure unitCode="MTQ">0.8</cbc:EstimatedGeneratedUntilNextPortMeasure>
        <cac:RemainingWasteDeliveryPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:RemainingWasteDeliveryPortLocation>
      </cac:MaritimeWaste>
      <cac:MaritimeWaste>
        <cbc:ID>W-2</cbc:ID>
        <cbc:Description>Food and packaging waste.</cbc:Description>
        <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:ShipWasteTypeCode">GARBAGE</cbc:WasteTypeCode>
        <cbc:ToBeDeliveredMeasure unitCode="MTQ">1.5</cbc:ToBeDeliveredMeasure>
      </cac:MaritimeWaste>
      <cac:BallastWaterSummary>
        <cbc:ID>BW-26-0517</cbc:ID>
        <cbc:ManagementPlanOnBoardIndicator>true</cbc:ManagementPlanOnBoardIndicator>
        <cbc:ManagementPlanImplementedIndicator>true</cbc:ManagementPlanImplementedIndicator>
        <cbc:IMOGuidelinesOnBoardIndicator>true</cbc:IMOGuidelinesOnBoardIndicator>
        <cbc:TotalBallastTanksOnBoardQuantity unitCode="EA">8</cbc:TotalBallastTanksOnBoardQuantity>
        <cbc:TanksInBallastQuantity unitCode="EA">4</cbc:TanksInBallastQuantity>
        <cbc:TanksExchangedQuantity unitCode="EA">4</cbc:TanksExchangedQuantity>
        <cbc:TanksNotExchangedQuantity unitCode="EA">0</cbc:TanksNotExchangedQuantity>
        <cbc:TotalBallastWaterOnBoardMeasure unitCode="TNE">1240</cbc:TotalBallastWaterOnBoardMeasure>
        <cbc:TotalBallastWaterCapacityMeasure unitCode="TNE">2480</cbc:TotalBallastWaterCapacityMeasure>
        <cbc:OtherControlActions>None.</cbc:OtherControlActions>
        <cbc:NoControlActionsReason>Exchange done at more than 200 nautical miles from land.</cbc:NoControlActionsReason>
        <cac:UptakeBallastWaterTransaction>
          <cbc:TankID>BT-3</cbc:TankID>
          <cbc:TankTypeCode listID="urn:ubl-examples:world:codelist:BallastTankTypeCode">WING</cbc:TankTypeCode>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:SeaHeightMeasure unitCode="MTR">2</cbc:SeaHeightMeasure>
          <cbc:SalinityMeasure unitCode="GL">30</cbc:SalinityMeasure>
          <cbc:TransactionDate>2026-05-14</cbc:TransactionDate>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
          <cac:BallastWaterTemperature>
            <cbc:AttributeID>Water</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">16</cbc:Measure>
          </cac:BallastWaterTemperature>
        </cac:UptakeBallastWaterTransaction>
        <cac:ExchangeBallastWaterTransaction>
          <cbc:TankID>BT-3</cbc:TankID>
          <cbc:ExchangeMethodCode listID="urn:ubl-examples:world:codelist:BallastExchangeMethodCode">SEQ</cbc:ExchangeMethodCode>
          <cbc:ExchangedPercent>95</cbc:ExchangedPercent>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-16</cbc:TransactionDate>
          <cac:Location>
            <cbc:Name>At sea, 120 nautical miles west of Selanu</cbc:Name>
          </cac:Location>
        </cac:ExchangeBallastWaterTransaction>
        <cac:DischargeBallastWaterTransaction>
          <cbc:TankID>BT-3</cbc:TankID>
          <cbc:VolumeMeasure unitCode="MTQ">120</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-18</cbc:TransactionDate>
        </cac:DischargeBallastWaterTransaction>
        <cac:ResponsibleOfficerPerson>
          <cbc:FirstName>Elsbeth</cbc:FirstName>
          <cbc:FamilyName>Marrin</cbc:FamilyName>
          <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFOFFICER</cbc:RoleCode>
        </cac:ResponsibleOfficerPerson>
      </cac:BallastWaterSummary>
      <cac:ISPSRequirements>
        <cbc:ID>ISSC-XL-2026-0117</cbc:ID>
        <cbc:ValidISSCIndicator>true</cbc:ValidISSCIndicator>
        <cbc:ISSCAbsenceReason>Not applicable: the certificate is on board.</cbc:ISSCAbsenceReason>
        <cbc:ISSCExpiryDate>2028-09-30</cbc:ISSCExpiryDate>
        <cbc:SSPOnBoardIndicator>true</cbc:SSPOnBoardIndicator>
        <cbc:SSPSecurityMeasuresAppliedIndicator>true</cbc:SSPSecurityMeasuresAppliedIndicator>
        <cbc:CurrentOperatingSecurityLevelCode listID="IMO ISPS security level">1</cbc:CurrentOperatingSecurityLevelCode>
        <cbc:AdditionalMattersDescription>None.</cbc:AdditionalMattersDescription>
        <cac:AdditionalSecurityMeasure>
          <cbc:ID>SM-1</cbc:ID>
          <cbc:Description>Gangway watch at Selanu.</cbc:Description>
        </cac:AdditionalSecurityMeasure>
        <cac:PortCallRecord>
          <cbc:ID>PCR-1</cbc:ID>
          <cbc:SecurityLevelCode listID="IMO ISPS security level">1</cbc:SecurityLevelCode>
          <cac:SecurityMeasure>
            <cbc:Description>Normal access control.</cbc:Description>
          </cac:SecurityMeasure>
          <cac:PortFacilityLocation>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:PortFacilityLocation>
          <cac:Period>
            <cbc:StartDate>2026-05-13</cbc:StartDate>
            <cbc:EndDate>2026-05-14</cbc:EndDate>
          </cac:Period>
        </cac:PortCallRecord>
        <cac:ShipToShipActivityRecord>
          <cbc:ID>STS-0</cbc:ID>
          <cbc:Description>None during the last ten port calls.</cbc:Description>
          <cac:AppliedSecurityMeasure>
            <cbc:ID>SM-0</cbc:ID>
            <cbc:Description>None: no ship-to-ship activity.</cbc:Description>
          </cac:AppliedSecurityMeasure>
          <cac:Period>
            <cbc:StartDate>2026-01-01</cbc:StartDate>
            <cbc:EndDate>2026-05-17</cbc:EndDate>
          </cac:Period>
          <cac:Location>
            <cbc:Name>At sea, 120 nautical miles west of Selanu</cbc:Name>
          </cac:Location>
        </cac:ShipToShipActivityRecord>
        <cac:ReportLocation>
          <cbc:Name>At sea, 120 nautical miles west of Selanu</cbc:Name>
        </cac:ReportLocation>
        <cac:ISSCIssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42270</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
          </cac:PartyName>
        </cac:ISSCIssuerParty>
        <cac:SecurityOfficerPerson>
          <cbc:FirstName>Elsbeth</cbc:FirstName>
          <cbc:FamilyName>Marrin</cbc:FamilyName>
          <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFOFFICER</cbc:RoleCode>
        </cac:SecurityOfficerPerson>
      </cac:ISPSRequirements>
      <cac:MaritimeHealthDeclaration>
        <cbc:ID>MDH-26-0517</cbc:ID>
        <cbc:InfectiousDiseaseCaseOnBoardIndicator>false</cbc:InfectiousDiseaseCaseOnBoardIndicator>
        <cbc:MoreIllThanExpectedIndicator>false</cbc:MoreIllThanExpectedIndicator>
        <cbc:MedicalPractitionerConsultedIndicator>true</cbc:MedicalPractitionerConsultedIndicator>
        <cbc:StowawaysFoundOnBoardIndicator>false</cbc:StowawaysFoundOnBoardIndicator>
        <cbc:SickAnimalOnBoardIndicator>false</cbc:SickAnimalOnBoardIndicator>
        <cbc:FumigatedCargoTransportIndicator>false</cbc:FumigatedCargoTransportIndicator>
        <cbc:SanitaryMeasuresAppliedIndicator>true</cbc:SanitaryMeasuresAppliedIndicator>
        <cbc:ValidSanitationCertificateOnBoardIndicator>true</cbc:ValidSanitationCertificateOnBoardIndicator>
        <cbc:ReinspectionRequiredIndicator>false</cbc:ReinspectionRequiredIndicator>
        <cbc:TotalDeadPersonQuantity unitCode="IE">0</cbc:TotalDeadPersonQuantity>
        <cbc:TotalIllPersonQuantity unitCode="IE">1</cbc:TotalIllPersonQuantity>
        <cbc:SickAnimalDescription>None on board.</cbc:SickAnimalDescription>
        <cbc:StowawayDescription>None found in the search before departure.</cbc:StowawayDescription>
        <cbc:LastDrinkingWaterAnalysisDate>2026-04-02</cbc:LastDrinkingWaterAnalysisDate>
        <cac:WHOAffectedAreaVisit>
          <cbc:VisitDate>2026-03-28</cbc:VisitDate>
          <cac:WHOAffectedAreaPortLocation>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:WHOAffectedAreaPortLocation>
        </cac:WHOAffectedAreaVisit>
        <cac:PersonnelHealthIncident>
          <cbc:ID>HI-1</cbc:ID>
          <cbc:JoinedShipDate>2025-11-01</cbc:JoinedShipDate>
          <cbc:NatureOfIllnessDescription>Sprained wrist.</cbc:NatureOfIllnessDescription>
          <cbc:OnsetDate>2026-05-16</cbc:OnsetDate>
          <cbc:ReportedToMedicalOfficerIndicator>true</cbc:ReportedToMedicalOfficerIndicator>
          <cbc:GivenTreatmentDescription>Bandage and rest.</cbc:GivenTreatmentDescription>
          <cbc:StillIllIndicator>true</cbc:StillIllIndicator>
          <cbc:DiedIndicator>false</cbc:DiedIndicator>
          <cbc:StillOnBoardIndicator>true</cbc:StillOnBoardIndicator>
          <cbc:EvacuatedIndicator>false</cbc:EvacuatedIndicator>
          <cbc:BuriedAtSeaIndicator>false</cbc:BuriedAtSeaIndicator>
          <cbc:Note>Fit for light duty.</cbc:Note>
          <cac:Person>
            <cbc:FirstName>Rafe</cbc:FirstName>
            <cbc:FamilyName>Dunmore</cbc:FamilyName>
            <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFENG</cbc:RoleCode>
          </cac:Person>
        </cac:PersonnelHealthIncident>
        <cac:SanitaryMeasure>
          <cbc:SanitaryMeasureTypeCode listID="urn:ubl-examples:world:codelist:SanitaryMeasureCode">DISINFECT</cbc:SanitaryMeasureTypeCode>
          <cbc:ApplicationDate>2026-05-15</cbc:ApplicationDate>
        </cac:SanitaryMeasure>
        <cac:PlaceOfReportLocation>
          <cbc:Name>At sea, 120 nautical miles west of Selanu</cbc:Name>
        </cac:PlaceOfReportLocation>
        <cac:MedicalCertificate>
          <cbc:ID>MC-TH-2026</cbc:ID>
          <cbc:CertificateType>Medicine chest</cbc:CertificateType>
        </cac:MedicalCertificate>
        <cac:ShipSanitationControlCertificate>
          <cbc:ID>SSCC-XB-2025-0911</cbc:ID>
          <cbc:CertificateType>Ship sanitation control</cbc:CertificateType>
        </cac:ShipSanitationControlCertificate>
        <cac:ShipSanitationControlExemptionDocumentReference>
          <cbc:ID>none</cbc:ID>
        </cac:ShipSanitationControlExemptionDocumentReference>
      </cac:MaritimeHealthDeclaration>
      <cac:FuelConsumption>
        <cbc:ID>FC-26-19E</cbc:ID>
        <cbc:FuelTypeCode listID="urn:ubl-examples:world:codelist:FuelTypeCode">MGO</cbc:FuelTypeCode>
        <cbc:FuelType>Marine gas oil, 0.1 % sulphur</cbc:FuelType>
        <cbc:FuelConsumptionMeasure unitCode="TNE">38</cbc:FuelConsumptionMeasure>
        <cac:AdditionalFuelProperty>
          <cbc:TypeID>Sulphur</cbc:TypeID>
          <cbc:Value>0.1 %</cbc:Value>
        </cac:AdditionalFuelProperty>
        <cac:FuelMetering>
          <cbc:TypeID>FlowMeter</cbc:TypeID>
          <cbc:Value>38.2 t</cbc:Value>
        </cac:FuelMetering>
        <cac:EnvironmentalEmission>
          <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
          <cbc:ValueMeasure unitCode="TNE">122</cbc:ValueMeasure>
        </cac:EnvironmentalEmission>
        <cac:FuelProviderParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Port of Lumeport</cbc:Name>
          </cac:PartyName>
        </cac:FuelProviderParty>
      </cac:FuelConsumption>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:TransportMeans>
    <cbc:JourneyID>TH-26-19E</cbc:JourneyID>
    <cbc:RegistrationNationalityID>XB</cbc:RegistrationNationalityID>
    <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
    <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">EB</cbc:DirectionCode>
    <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">CONTAINERSHIP</cbc:TransportMeansTypeCode>
    <cac:MaritimeTransport>
      <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
      <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
      <cbc:RadioCallSignID>XBTH7</cbc:RadioCallSignID>
      <cbc:MMSIRegistrationID>999702117</cbc:MMSIRegistrationID>
      <cbc:ShipsRequirements>Shore power at the container quay.</cbc:ShipsRequirements>
      <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
      <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
      <cbc:SegregatedBallastMeasure unitCode="TNE">2480</cbc:SegregatedBallastMeasure>
      <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
      <cbc:INFShipClassCode listID="IMO INF Code">INF1</cbc:INFShipClassCode>
      <cbc:AntennaLocus>Mast, 28 m above the waterline</cbc:AntennaLocus>
      <cac:RegistryCertificateDocumentReference>
        <cbc:ID>REG-XB-S-20117</cbc:ID>
      </cac:RegistryCertificateDocumentReference>
      <cac:RegistryPortLocation>
        <cbc:Name>Lumeport</cbc:Name>
      </cac:RegistryPortLocation>
      <cac:VesselDynamics>
        <cbc:NavigationStatusCode listID="ITU-R M.1371 Navigational status">0</cbc:NavigationStatusCode>
        <cbc:AtAnchorageIndicator>false</cbc:AtAnchorageIndicator>
        <cbc:CourseOverGroundDirection>088</cbc:CourseOverGroundDirection>
        <cbc:SpeedOverGroundMeasure unitCode="KNT">13.5</cbc:SpeedOverGroundMeasure>
        <cbc:RateOfTurnMeasure unitCode="E96">0</cbc:RateOfTurnMeasure>
      </cac:VesselDynamics>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
  <cac:DocumentReference>
    <cbc:ID>TOL-MF-26-0140</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>TWL-SIG-CTR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</CommonTransportationReport>
```
