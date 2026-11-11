# Common Transportation Report: Tidewell Ocean Lines to Port of Lumeport

*Example 14 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Common Transportation Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-COMMON-TRANSPORTATION-REPORT-SCHEMA)*

Before entering Lumeport the carrier reports its second feeder to the port. The ship came under Bayvarra's flag in January, so it sails with an interim security certificate, and it carries a sanitation control exemption certificate, as the inspection at Lumeport in January found no control measures needed.

[The XML file](14-CommonTransportationReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); PartyLegalEntity/EntitySizeCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:common-transportation-report:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Common transportation report"; the community specification "Lumeport port community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TOL-CTR-26-0207**  
  The carrier's report number.
- `UUID` = **149f7421-1d43-5c08-9504-00a7ea0b615b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-03**  
  Sent the day before the ship enters Lumeport.
- `IssueTime` = **11:22:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ReportTypeCode` = **PREARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportReportTypeCode`)  
  The report before entering the port. The code is from the Trade Accord's transport report type list: PREARRIVAL = Pre-arrival report.
- `ReportType` = **Pre-arrival report**  
  The name of code PREARRIVAL in the Trade Accord's transport report type list.

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
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Tidewell Ocean Lines (world/parties.json).
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
- `PartyTaxScheme/CompanyID` = **CO-1235754** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Tidewell Ocean Lines (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered, with its legal form; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
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

- `WebsiteURI` = **https://www.port-lumeport.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Port of Lumeport (world/parties.json).
- `IndustryClassificationCode` = **5222** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Port of Lumeport (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5222 = Service activities incidental to water transportation.
- `PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Port of Lumeport (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Port of Lumeport**  
  The trading name; identity of Port of Lumeport (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **LUM-ADR-030762** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Port of Lumeport (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Port of Lumeport (world/parties.json).
- `PostalAddress/BuildingNumber` = **11**  
  Building number of the postal address. identity of Port of Lumeport (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Port of Lumeport (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Port of Lumeport (world/parties.json).
- `PostalAddress/PostalZone` = **38526**  
  Postal code in Bayvarra's format (5 digits). identity of Port of Lumeport (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Port of Lumeport (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PhysicalLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PhysicalLocation/Description` = **Port of Lumeport**  
  Where the party actually operates, apart from its postal address.
- `PhysicalLocation/InformationURI` = **https://www.port-lumeport.example**  
  Where to find more about the place.
- `PhysicalLocation/SubsidiaryLocation/Name` = **Container quay**  
  A part of the port with its own location: where containers are handled.
- `PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **40** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **1.20** (unitCode `D61`)  
  The minutes of the latitude.
- `PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **12.60** (unitCode `D61`)  
  The minutes of the longitude.
- `PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `PartyLegalEntity/RegistrationName` = **Port of Lumeport Ltd**  
  The name under which the party is registered, with its legal form; identity of Port of Lumeport (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Port of Lumeport (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Port of Lumeport (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 31 persons and its turnover of 9210000.00 XBL in 2025, by the Trade Accord's limits; identity of Port of Lumeport (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
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
- `Contact/Name` = **Port control**  
  The desk that handles this document; identity of Port of Lumeport (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Port of Lumeport (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Port of Lumeport (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2281 1781**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Port of Lumeport (world/parties.json).
- `Contact/ElectronicMail` = **port@port-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Port of Lumeport (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Port of Lumeport (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Port of Lumeport (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Port of Lumeport**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **TOL-SH-26-0208**  
  The carrier's shipment number for the voyage's cargo.
- `ShipmentStage/ID` = **1**  
  The sea leg from Selanu to Lumeport.
- `ShipmentStage/ReportingPerson/FirstName` = **Hester**  
  The master.
- `ShipmentStage/ReportingPerson/FamilyName` = **Calloway**  
  The family name.
- `ShipmentStage/ReportingPerson/RoleCode` = **MASTER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MASTER = Master.
- `ShipmentStage/ISPSRequirements/ID` = **IISSC-XB-2026-0115**  
  The number of the ship's interim International Ship Security Certificate.
- `ShipmentStage/ISPSRequirements/ValidISSCIndicator` = **false**  
  The ship has no full certificate yet.
- `ShipmentStage/ISPSRequirements/ISSCAbsenceReason` = **The ship came under Bayvarra's flag on 15 January 2026 and sails with an interim certificate (ISPS Code A/19.4), valid for six months; the flag state's verification for the full certificate is set for April.**  
  Why the ship has no full certificate, which the port needs to know.
- `ShipmentStage/ISPSRequirements/ISSCExpiryDate` = **2026-07-14**  
  The interim certificate's last day: six months, the most the ISPS Code allows.
- `ShipmentStage/ISPSRequirements/SSPOnBoardIndicator` = **true**  
  The ship security plan is on board.
- `ShipmentStage/ISPSRequirements/CurrentOperatingSecurityLevelCode` = **1** (listID `IMO ISPS security level`)  
  Security level 1, the normal level. The code is from the world's copy of IMO ISPS Code security level: 1 = Security level 1.
- `ShipmentStage/ISPSRequirements/AdditionalMattersDescription` = **The ship was searched for stowaways before it left Selanu, because the port facility had reported a gap in its perimeter fence on 1 March. Nothing was found.**  
  A security matter the port should know about.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyIdentification/ID` = **20413014** (schemeID `urn:ubl-examples:world:XB:register`)  
  Bayvarra's flag state administration: keeps the register of Bayvarran ships and issues their international ship security certificates under the ISPS Code. Referenced only, as the issuer of the certificate of Tidewell Ocean Lines' ship. Its identifier and name are enough (world/parties.json, referenced).
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyName/Name` = **Maritime Administration of Bayvarra**  
  Bayvarra's flag state administration: keeps the register of Bayvarran ships and issues their international ship security certificates under the ISPS Code. Referenced only, as the issuer of the certificate of Tidewell Ocean Lines' ship. Its identifier and name are enough (world/parties.json, referenced).
- `ShipmentStage/MaritimeHealthDeclaration/ID` = **MDH-26-0303**  
  The maritime declaration of health.
- `ShipmentStage/MaritimeHealthDeclaration/InfectiousDiseaseCaseOnBoardIndicator` = **false**  
  No infectious disease.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasuresAppliedIndicator` = **false**  
  No sanitary measures on this voyage.
- `ShipmentStage/MaritimeHealthDeclaration/ValidSanitationCertificateOnBoardIndicator` = **true**  
  The exemption certificate is valid until July.
- `ShipmentStage/MaritimeHealthDeclaration/TotalIllPersonQuantity` = **0** (unitCode `IE`)  
  No one ill.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/ID` = **SSCEC-XB-2026-0114**  
  The ship sanitation control exemption certificate: the ship carries it instead of a control certificate. Unique only with its issuer (decision ID-Q10).
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/IssueDate` = **2026-01-14**  
  Issued after the inspection at Lumeport, before the ship's first voyage for the line; valid six months.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/DocumentDescription` = **Ship Sanitation Control Exemption Certificate (International Health Regulations 2005, Annex 3): the inspection found no evidence of infection or contamination, so no control measures were needed.**  
  What the document is.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/IssuerParty/PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/IssuerParty/PartyName/Name` = **Port of Lumeport**  
  A party referred to from another party's details: its identifier and name are enough.

### Transport Means

Inside `TransportMeans`:

- `JourneyID` = **TR-26-09W**  
  The voyage from Selanu back to Lumeport.
- `RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Reef; the fleet of Tidewell Ocean Lines (world/parties.json). The line's second feeder, bought second-hand in December 2025 and moved to Bayvarra's flag on 15 January 2026. Until the flag state verifies its security system, it sails with an interim International Ship Security Certificate (ISPS Code A/19.4). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `MaritimeTransport/VesselID` = **XB-S-20231** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `MaritimeTransport/VesselName` = **Tidewell Reef**  
  The vessel's name; the fleet of Tidewell Ocean Lines (world/parties.json).
- `MaritimeTransport/RadioCallSignID` = **QBTR4**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station (world/countries.json).
- `MaritimeTransport/MMSIRegistrationID` = **298702231**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `MaritimeTransport/ShipsRequirements` = **Shore power at the container quay.**  
  What the ship needs in port.
- `MaritimeTransport/GrossTonnageMeasure` = **7480** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `MaritimeTransport/NetTonnageMeasure` = **3910** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `MaritimeTransport/SegregatedBallastMeasure` = **1900** (unitCode `TNE`)  
  The capacity of the tanks for ballast water only.
- `MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 700 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20231**  
  The ship's certificate of registry.
- `MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CommonTransportationReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:CommonTransportationReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:common-transportation-report:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TOL-CTR-26-0207</cbc:ID>
  <cbc:UUID>149f7421-1d43-5c08-9504-00a7ea0b615b</cbc:UUID>
  <cbc:IssueDate>2026-03-03</cbc:IssueDate>
  <cbc:IssueTime>11:22:00</cbc:IssueTime>
  <cbc:ReportTypeCode listID="urn:ubl-examples:world:codelist:TransportReportTypeCode">PREARRIVAL</cbc:ReportTypeCode>
  <cbc:ReportType>Pre-arrival report</cbc:ReportType>
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
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-547539</cbc:ID>
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
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1235754</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
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
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:CompanyID>
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
    <cbc:WebsiteURI>https://www.port-lumeport.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5222</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Lumeport</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-030762</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>11</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38526</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PhysicalLocation>
      <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
      <cbc:Description>Port of Lumeport</cbc:Description>
      <cbc:InformationURI>https://www.port-lumeport.example</cbc:InformationURI>
      <cac:SubsidiaryLocation>
        <cbc:Name>Container quay</cbc:Name>
      </cac:SubsidiaryLocation>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure unitCode="DD">40</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure unitCode="D61">1.20</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure unitCode="D61">12.60</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:PhysicalLocation>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Port of Lumeport Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
      <cbc:Name>Port control</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38 2281 1781</cbc:Telephone>
      <cbc:ElectronicMail>port@port-lumeport.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411781</cbc:ElectronicAddressID>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Lumeport</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:Shipment>
    <cbc:ID>TOL-SH-26-0208</cbc:ID>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cac:ReportingPerson>
        <cbc:FirstName>Hester</cbc:FirstName>
        <cbc:FamilyName>Calloway</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MASTER</cbc:RoleCode>
      </cac:ReportingPerson>
      <cac:ISPSRequirements>
        <cbc:ID>IISSC-XB-2026-0115</cbc:ID>
        <cbc:ValidISSCIndicator>false</cbc:ValidISSCIndicator>
        <cbc:ISSCAbsenceReason>The ship came under Bayvarra's flag on 15 January 2026 and sails with an interim certificate (ISPS Code A/19.4), valid for six months; the flag state's verification for the full certificate is set for April.</cbc:ISSCAbsenceReason>
        <cbc:ISSCExpiryDate>2026-07-14</cbc:ISSCExpiryDate>
        <cbc:SSPOnBoardIndicator>true</cbc:SSPOnBoardIndicator>
        <cbc:CurrentOperatingSecurityLevelCode listID="IMO ISPS security level">1</cbc:CurrentOperatingSecurityLevelCode>
        <cbc:AdditionalMattersDescription>The ship was searched for stowaways before it left Selanu, because the port facility had reported a gap in its perimeter fence on 1 March. Nothing was found.</cbc:AdditionalMattersDescription>
        <cac:ISSCIssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413014</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Maritime Administration of Bayvarra</cbc:Name>
          </cac:PartyName>
        </cac:ISSCIssuerParty>
      </cac:ISPSRequirements>
      <cac:MaritimeHealthDeclaration>
        <cbc:ID>MDH-26-0303</cbc:ID>
        <cbc:InfectiousDiseaseCaseOnBoardIndicator>false</cbc:InfectiousDiseaseCaseOnBoardIndicator>
        <cbc:SanitaryMeasuresAppliedIndicator>false</cbc:SanitaryMeasuresAppliedIndicator>
        <cbc:ValidSanitationCertificateOnBoardIndicator>true</cbc:ValidSanitationCertificateOnBoardIndicator>
        <cbc:TotalIllPersonQuantity unitCode="IE">0</cbc:TotalIllPersonQuantity>
        <cac:ShipSanitationControlExemptionDocumentReference>
          <cbc:ID>SSCEC-XB-2026-0114</cbc:ID>
          <cbc:IssueDate>2026-01-14</cbc:IssueDate>
          <cbc:DocumentDescription>Ship Sanitation Control Exemption Certificate (International Health Regulations 2005, Annex 3): the inspection found no evidence of infection or contamination, so no control measures were needed.</cbc:DocumentDescription>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Port of Lumeport</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:ShipSanitationControlExemptionDocumentReference>
      </cac:MaritimeHealthDeclaration>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:TransportMeans>
    <cbc:JourneyID>TR-26-09W</cbc:JourneyID>
    <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
    <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
    <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
    <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
    <cac:MaritimeTransport>
      <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20231</cbc:VesselID>
      <cbc:VesselName>Tidewell Reef</cbc:VesselName>
      <cbc:RadioCallSignID>QBTR4</cbc:RadioCallSignID>
      <cbc:MMSIRegistrationID>298702231</cbc:MMSIRegistrationID>
      <cbc:ShipsRequirements>Shore power at the container quay.</cbc:ShipsRequirements>
      <cbc:GrossTonnageMeasure unitCode="C62">7480</cbc:GrossTonnageMeasure>
      <cbc:NetTonnageMeasure unitCode="C62">3910</cbc:NetTonnageMeasure>
      <cbc:SegregatedBallastMeasure unitCode="TNE">1900</cbc:SegregatedBallastMeasure>
      <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
      <cac:RegistryCertificateDocumentReference>
        <cbc:ID>REG-XB-S-20231</cbc:ID>
      </cac:RegistryCertificateDocumentReference>
      <cac:RegistryPortLocation>
        <cbc:Name>Lumeport</cbc:Name>
      </cac:RegistryPortLocation>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
</CommonTransportationReport>
```
