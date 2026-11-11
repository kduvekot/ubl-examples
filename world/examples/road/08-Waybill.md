# Waybill: Trasvia Haulage to Lumeway Distribution

*Example 8 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The road consignment note goes to the party that booked the truck, the distributor; it names the manufacturer as consignor.

[The XML file](08-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:road**  
  The business process the document belongs to: the flow "Finished goods by truck across the land border (Urvania → Bayvarra)".
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TH-WB-26-0159**  
  The consignment note number.
- `CarrierAssignedID` = **TH-CMR-26-0149**  
  The carrier's own number for the carriage.
- `UUID` = **4891662e-273a-5190-9aa7-edb87e35d8b5**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-03-23**  
  Issued when the carrier collects the goods at the warehouse.
- `IssueTime` = **08:16:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Consignment note under the road convention, the CMR**  
  The kind of transport document.
- `Description` = **The truck the distributor booked, from the 3PL's warehouse across the border.**  
  The carriage in words.
- `Note` = **Gurbul mizstan: dadrek, miran, sundraz.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): As the convention prescribes.
- `Note` = **Three originals: consignor, consignee, carrier.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: As the convention prescribes.
- `ShippingOrderID` = **LD-CS-26-0152**  
  The shipper's booking the carriage fulfils.
- `WaybillTypeCode` = **CMR** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: CMR = Road consignment note (CMR).
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `AdValoremIndicator` = **false**  
  No value declared to raise the carrier's liability.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Castrano Logistics**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.trasvia.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Trasvia Haulage (world/parties.json).
- `IndustryClassificationCode` = **4923** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Trasvia Haulage (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4923 = Freight transport by road.
- `PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Trasvia Haulage**  
  The trading name; identity of Trasvia Haulage (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Trasvia Haulage (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered for value added tax; identity of Trasvia Haulage (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007337656** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Trasvia Haulage (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered, with its legal form; identity of Trasvia Haulage (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Trasvia Haulage (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 27 persons and its turnover of 386000000 XUF in 2025, by the Trade Accord's limits; identity of Trasvia Haulage (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Contact/Name` = **Planning desk**  
  The desk that handles this document; identity of Trasvia Haulage (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Trasvia Haulage (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Trasvia Haulage (world/parties.json).
- `Contact/Telephone` = **+999 1 041 354 4822**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Trasvia Haulage (world/parties.json).
- `Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `PartyAuthorization/Purpose` = **International road haulage**  
  What the authority has authorized the party to do; identity of Trasvia Haulage (world/parties.json).
- `PartyAuthorization/ValidityPeriod/EndDate` = **2030-06-30**  
  The authorization expires on this date.
- `PartyAuthorization/Certificate/ID` = **XU-HAUL-2020-0877**  
  The number of the permit.
- `PartyAuthorization/Certificate/CertificateTypeCode` = **PERMIT** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A permit issued by an authority of the party's country. The code is from the Trade Accord's certificate type list: PERMIT = Operating permit.
- `PartyAuthorization/Certificate/CertificateType` = **Kusul treznul** (languageID `qau`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `PartyAuthorization/Certificate/CertificateType` = **Operating permit** (languageID `en-XU`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In English.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Trasvia Haulage (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1230822** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **MEDIUM** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 183 persons and its turnover of 33900000.00 XBL in 2025, by the Trade Accord's limits; identity of Lumeway Distribution (world/parties.json). The code is from the Trade Accord's entity size list: MEDIUM = Medium-sized enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
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
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007299291** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 3083 persons and its turnover of 23600000000 XUF in 2025, by the Trade Accord's limits; identity of Valdara Industries (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/SecurityListing/ID` = **XU0001042501** (schemeID `ISO 6166`)  
  The identifier of the listed shares, in the form of an ISIN with the world's country code. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The name of code XFER in the Trade Accord's market identifier list.
- `PartyLegalEntity/SecurityListing/MarketCode` = **XFER** (listID `urn:ubl-examples:world:codelist:MarketCode`)  
  The market's code. The code is from the Trade Accord's market identifier list: XFER = Ferrano Stock Exchange.
- `Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `ServiceProviderParty/ID` = **VI-SP-2026-01**  
  The number of the service contract between the two; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/ServiceTypeCode` = **LOGISTICS** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  The kind of service, as a code. The code is from the Trade Accord's service type list: LOGISTICS = Logistics service.
- `ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Trasvia Haulage**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **CL-SH-26-0154**  
  The shipment as the despatching party numbered it.
- `HandlingCode` = **UPRIGHT** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: keep upright. The code is from the Trade Accord's handling instruction list: UPRIGHT = Keep upright.
- `Information` = **Steel street furniture for resale.**  
  What the goods are, for the driver.
- `GrossWeightMeasure` = **4106.4** (unitCode `KGM`)  
  The gross weight the carrier takes over.
- `NetNetWeightMeasure` = **3762** (unitCode `KGM`)  
  The goods alone, without any packaging.
- `GrossVolumeMeasure` = **41.5** (unitCode `MTQ`)  
  The volume of the 25 loaded pallets.
- `TotalGoodsItemQuantity` = **2** (unitCode `EA`)  
  Two kinds of goods: benches and side frames.
- `SplitConsignmentIndicator` = **false**  
  The whole consignment travels on this truck.
- `ConsignmentQuantity` = **1** (unitCode `EA`)  
  One consignment on the truck.
- `Consignment/ID` = **LD-CS-26-0152**  
  The distributor's consignment number, from its booking.
- `Consignment/CarrierAssignedID` = **TH-26-04471**  
  The carrier's job number.
- `Consignment/ConsigneeAssignedID` = **LD-GI-0412**  
  The distributor's goods-in booking for the slot.
- `Consignment/ConsignorAssignedID` = **CL-DA-26-0153**  
  The consignor's reference: its despatch advice.
- `Consignment/SummaryDescription` = **Park benches and spare side frames on 25 pallets.**  
  The goods in a few words, as on the consignment note.
- `Consignment/NetWeightMeasure` = **3762** (unitCode `KGM`)  
  The weight of the goods without packaging.
- `Consignment/LoadingLengthMeasure` = **9.3** (unitCode `MTR`)  
  Five rows of bench pallets, two high, and the castings: 9.3 m of the 13.6 m floor.
- `Consignment/Remarks` = **Received in apparent good order; seals XU-CL-77310 on the trailer doors.**  
  The driver's remarks at taking over, as the consignment note asks.
- `Consignment/ContainerizedIndicator` = **false**  
  The pallets are loaded on the truck, not in a container.
- `Consignment/GeneralCargoIndicator` = **true**  
  Packed goods on pallets.
- `Consignment/ThirdPartyPayerIndicator` = **false**  
  The consignee, who booked the truck, pays the freight.
- `Consignment/CustomsClearanceServiceInstructions` = **The export is declared by the 3PL in Ferrano; the import by the distributor at the border.**  
  Who clears the goods through customs.
- `Consignment/TotalTransportHandlingUnitQuantity` = **25** (unitCode `EA`)  
  25 pallets.
- `Consignment/DeliveryInstructions` = **Unload at dock 4; report to the gatehouse first.**  
  Where to go on arrival.
- `Consignment/HaulageInstructions` = **Wait at the warehouse until customs has released the export declaration.**  
  What the driver must do before leaving.
- `Consignment/TotalPackagesQuantity` = **108** (unitCode `EA`)  
  96 benches and 12 boxed frames.
- `Consignment/CustomsDeclaration/ID` = **VI-CD-26-0156**  
  The export declaration the goods travel under.
- `Consignment/CustomsDeclaration/IssuerParty/PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/CustomsDeclaration/IssuerParty/PartyName/Name` = **Customs Administration of Urvania**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/ActualPickupTransportEvent/OccurrenceDate` = **2026-03-23**  
  When the carrier took over the goods.
- `Consignment/ActualPickupTransportEvent/OccurrenceTime` = **15:05:00**  
  The local time.
- `Consignment/ActualPickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/ActualPickupTransportEvent/Location/Name` = **Ferrano**  
  The 3PL's warehouse.
- `Consignment/ActualPickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Consignment/OriginalDepartureCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The goods start in Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/FinalDestinationCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  And end in Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/DeliveryTerms/ID` = **FCA** (schemeID `INCOTERMS`)  
  Incoterms 2020: free carrier at the seller's warehouse. The code is from the world's copy of Incoterms 2020: FCA = Free Carrier. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/DeliveryTerms/SpecialTerms` = **The buyer's carrier presents the truck; the seller loads it.**  
  Who loads, under FCA at the seller's premises.
- `Consignment/DeliveryTerms/LossRiskResponsibilityCode` = **BUYER** (listID `urn:ubl-examples:world:codelist:RiskResponsiblePartyCode`)  
  The risk passed to the buyer when the goods were loaded on the truck. The code is from the Trade Accord's party bearing the risk list: BUYER = Buyer.
- `Consignment/DeliveryTerms/LossRisk` = **The risk passes on loading at the 3PL's warehouse.**  
  In words.
- `Consignment/CollectPaymentTerms/Note` = **The freight is paid by the consignee under its contract with the carrier.**  
  Freight collect: the consignee pays.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The only stage: one truck from the warehouse to the distribution centre.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/MainCarriageShipmentStage/TransportMeansTypeCode` = **TRUCKTRAILER** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The truck pulls a trailer. The code is from the Trade Accord's transport means type list: TRUCKTRAILER = Truck with trailer.
- `Consignment/MainCarriageShipmentStage/TransitDirectionCode` = **EXPORT** (listID `urn:ubl-examples:world:codelist:TransitDirectionCode`)  
  The goods leave Urvania by this stage. The code is from the Trade Accord's transit direction list: EXPORT = Export.
- `Consignment/MainCarriageShipmentStage/CabotageIndicator` = **false**  
  A carriage between two countries, not within a foreign one.
- `Consignment/MainCarriageShipmentStage/EstimatedDeliveryDate` = **2026-03-25**  
  The carrier's estimate when it takes over the goods.
- `Consignment/MainCarriageShipmentStage/EstimatedDeliveryTime` = **09:00:00**  
  Early in the working day.
- `Consignment/MainCarriageShipmentStage/RequiredDeliveryDate` = **2026-03-25**  
  The distributor's goods-in slot.
- `Consignment/MainCarriageShipmentStage/RequiredDeliveryTime` = **10:00:00**  
  The slot starts at ten.
- `Consignment/MainCarriageShipmentStage/TransitPeriod/StartDate` = **2026-03-23**  
  Collected in the afternoon.
- `Consignment/MainCarriageShipmentStage/TransitPeriod/EndDate` = **2026-03-25**  
  Delivered in the morning, after the night rest of the driver and the border.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **TH-26-04471**  
  The carrier's job number, the same on every document of this truck.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **TRUCKTRAILER** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The kind of means of transport: tractor unit 07 with curtain-side trailer; the fleet of Trasvia Haulage (world/parties.json). The code is from the Trade Accord's transport means type list: TRUCKTRAILER = Truck with trailer.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 KT** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Trasvia Haulage (world/parties.json). The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `Consignment/MainCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **UR 4160 TR** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `Consignment/MainCarriageShipmentStage/TransportMeans/OwnerParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/TransportMeans/OwnerParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **LOADINGLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The length of the loading floor. The code is from the Trade Accord's dimension attribute list: LOADINGLENGTH = Loading length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/Measure` = **13.6** (unitCode `MTR`)  
  Room for 33 pallets.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Ferrano**  
  Loaded at the 3PL's warehouse in Ferrano.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Marrowdale**  
  Unloaded at the distributor's distribution centre.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/ExaminationTransportEvent/OccurrenceDate` = **2026-03-24**  
  Customs looked at the seals at the border.
- `Consignment/MainCarriageShipmentStage/ExaminationTransportEvent/OccurrenceTime` = **07:45:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ExaminationTransportEvent/Description` = **Seal check, no inspection of the goods.**  
  What happened, in words.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/OccurrenceDate` = **2026-03-23**  
  The truck left the warehouse.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/OccurrenceTime` = **16:20:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/Location/Name` = **Ferrano**  
  Castrano Logistics warehouse.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/DriverPerson/ID` = **XU-DL-0417722**  
  The number of the driving licence.
- `Consignment/MainCarriageShipmentStage/DriverPerson/FirstName` = **Ilario**  
  The driver of the truck.
- `Consignment/MainCarriageShipmentStage/DriverPerson/FamilyName` = **Bencetti**  
  The family name.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-001**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 001 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-001**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-001**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-001-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-002**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 002 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-002**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-002**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-002-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-003**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 003 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-003**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-003**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-003-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-004**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 004 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-004**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-004**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-004-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-005**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 005 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-005**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-005**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-005-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-006**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 006 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-006**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-006**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-006-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-007**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 007 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-007**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-007**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-007-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-008**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 008 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-008**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-008**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-008-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-009**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 009 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-009**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-009**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-009-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-010**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 010 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-010**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-010**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-010-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-011**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 011 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-011**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-011**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-011-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-012**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 012 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-012**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-012**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-012-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-013**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 013 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-013**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-013**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-013-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-014**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 014 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-014**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-014**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-014-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-015**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 015 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-015**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-015**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-015-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-016**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 016 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-016**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-016**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-016-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-017**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 017 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-017**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-017**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-017-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-018**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 018 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-018**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-018**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-018-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-019**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 019 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-019**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-019**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-019-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-020**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 020 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-020**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-020**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-020-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-021**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 021 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-021**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-021**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-021-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-022**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 022 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-022**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-022**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-022-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-023**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 023 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-023**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-023**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-023-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-024**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **May be stacked two high, steel frames on steel frames.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 024 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-024**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-024**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **650** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1650** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.2** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-024-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **4** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **SW** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: shrinkwrapped, each bench in film. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SW = Shrinkwrapped.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Bench in stretch film**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Recycled PE stretch film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/ID` = **CL-26-025**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingCode` = **NOSTACK** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: NOSTACK = Do not stack.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Load on top: nothing may be stacked on the boxes.**  
  The handling, in words.
- `Consignment/TransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  12 boxed side frames on the pallet.
- `Consignment/TransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 025 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TraceID` = **CL-26-025**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/ActualPackage/ID` = **CL-26-025**  
  The pallet itself, as packed.
- `Consignment/TransportHandlingUnit/ActualPackage/Quantity` = **1** (unitCode `EA`)  
  One pallet.
- `Consignment/TransportHandlingUnit/ActualPackage/ReturnableMaterialIndicator` = **true**  
  The pallet is exchanged with the carrier and goes back.
- `Consignment/TransportHandlingUnit/ActualPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **1200** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **800** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MeasurementDimension/Measure` = **900** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **0.96** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **1** (unitCode `C62`)  
  Half a place when two pallets are stacked; the castings take a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/Package/ID` = **CL-26-025-1**  
  The packages on the pallet.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **12** (unitCode `EA`)  
  The packages of this kind on the pallet.
- `Consignment/TransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The packaging is not returned.
- `Consignment/TransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  The inner packaging, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/PackagingType` = **Cardboard box**  
  The packaging in words.
- `Consignment/TransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard**  
  What the packaging is made of.
- `Delivery/LatestDeliveryDate` = **2026-03-25**  
  The goods-in slot cannot move.
- `Delivery/LatestDeliveryTime` = **12:00:00**  
  Dock 4 closes for the lunch change.
- `Delivery/TrackingID` = **TH-26-04471**  
  Track the truck with the carrier's job number.
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-03-25**  
  The morning of the third day.
- `Delivery/EstimatedDeliveryPeriod/StartTime` = **09:00:00**  
  From nine.
- `Delivery/EstimatedDeliveryPeriod/EndTime` = **11:00:00**  
  Until eleven.
- `Delivery/FuelConsumption/ID` = **TH-FC-26-0159**  
  The fuel of this delivery.
- `Delivery/FuelConsumption/FuelTypeCode` = **DIESEL** (listID `urn:ubl-examples:world:codelist:FuelTypeCode`)  
  The truck runs on diesel. The code is from the Trade Accord's fuel type list: DIESEL = Diesel.
- `Delivery/FuelConsumption/FuelConsumptionMeasure` = **61** (unitCode `LTR`)  
  About 33 litres per 100 km over 186 km.
- `ReturnAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ReturnAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `ReturnAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/BuildingNumber` = **24**  
  Building number of the postal address. identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Castrano Logistics (world/parties.json).
- `ReturnAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ReturnAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ReturnAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `OriginAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `OriginAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `OriginAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Castrano Logistics (world/parties.json).
- `OriginAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Castrano Logistics (world/parties.json).
- `OriginAddress/BuildingNumber` = **24**  
  Building number of the postal address. identity of Castrano Logistics (world/parties.json).
- `OriginAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Castrano Logistics (world/parties.json).
- `OriginAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Castrano Logistics (world/parties.json).
- `OriginAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Castrano Logistics (world/parties.json).
- `OriginAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Castrano Logistics (world/parties.json).
- `OriginAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `OriginAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `OriginAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `ExportCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The goods are exported from Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The first original.
- `DocumentTypeCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:DocumentCopyTypeCode`)  
  An original. The code is from the Trade Accord's document copy type list: ORIGINAL = Original.
- `DistributionTypeCode` = **PAPER** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  Handed over on paper. The code is from the Trade Accord's distribution type list: PAPER = Paper.
- `DistributionType` = **With the goods**  
  It travels with the goods.
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The electronic copy.
- `DocumentTypeCode` = **COPY** (listID `urn:ubl-examples:world:codelist:DocumentCopyTypeCode`)  
  A copy. The code is from the Trade Accord's document copy type list: COPY = Copy.
- `DistributionTypeCode` = **ELECTRONIC** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  Sent as this UBL document. The code is from the Trade Accord's distribution type list: ELECTRONIC = Electronic.
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **TH-SIG-TH-WB-26-0159**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:road</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TH-WB-26-0159</cbc:ID>
  <cbc:CarrierAssignedID>TH-CMR-26-0149</cbc:CarrierAssignedID>
  <cbc:UUID>4891662e-273a-5190-9aa7-edb87e35d8b5</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>08:16:00</cbc:IssueTime>
  <cbc:Name>Consignment note under the road convention, the CMR</cbc:Name>
  <cbc:Description>The truck the distributor booked, from the 3PL's warehouse across the border.</cbc:Description>
  <cbc:Note languageID="qau">Gurbul mizstan: dadrek, miran, sundraz.</cbc:Note>
  <cbc:Note languageID="en-XU">Three originals: consignor, consignee, carrier.</cbc:Note>
  <cbc:ShippingOrderID>LD-CS-26-0152</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">CMR</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Castrano Logistics</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.trasvia.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4923</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Trasvia Haulage</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Ban Kumek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via dei Trasporti</cbc:StreetName>
      <cbc:BuildingNumber>45</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4160</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Trasvia Haulage SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007337656</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Trasvia Haulage SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
      <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Planning desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 041 354 4822</cbc:Telephone>
      <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:PartyAuthorization>
      <cbc:Purpose>International road haulage</cbc:Purpose>
      <cac:ValidityPeriod>
        <cbc:EndDate>2030-06-30</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:Certificate>
        <cbc:ID>XU-HAUL-2020-0877</cbc:ID>
        <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">PERMIT</cbc:CertificateTypeCode>
        <cbc:CertificateType languageID="qau">Kusul treznul</cbc:CertificateType>
        <cbc:CertificateType languageID="en-XU">Operating permit</cbc:CertificateType>
      </cac:Certificate>
    </cac:PartyAuthorization>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104822</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
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
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1230822</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:CompanyID>
      <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">MEDIUM</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Marrowdale</cbc:CityName>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
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
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
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
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007299291</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
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
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
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
        <cbc:ID schemeID="ISO 6166">XU0001042501</cbc:ID>
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
      <cbc:ID>VI-SP-2026-01</cbc:ID>
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
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Trasvia Haulage</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>CL-SH-26-0154</cbc:ID>
    <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">UPRIGHT</cbc:HandlingCode>
    <cbc:Information>Steel street furniture for resale.</cbc:Information>
    <cbc:GrossWeightMeasure unitCode="KGM">4106.4</cbc:GrossWeightMeasure>
    <cbc:NetNetWeightMeasure unitCode="KGM">3762</cbc:NetNetWeightMeasure>
    <cbc:GrossVolumeMeasure unitCode="MTQ">41.5</cbc:GrossVolumeMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="EA">2</cbc:TotalGoodsItemQuantity>
    <cbc:SplitConsignmentIndicator>false</cbc:SplitConsignmentIndicator>
    <cbc:ConsignmentQuantity unitCode="EA">1</cbc:ConsignmentQuantity>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0152</cbc:ID>
      <cbc:CarrierAssignedID>TH-26-04471</cbc:CarrierAssignedID>
      <cbc:ConsigneeAssignedID>LD-GI-0412</cbc:ConsigneeAssignedID>
      <cbc:ConsignorAssignedID>CL-DA-26-0153</cbc:ConsignorAssignedID>
      <cbc:SummaryDescription>Park benches and spare side frames on 25 pallets.</cbc:SummaryDescription>
      <cbc:NetWeightMeasure unitCode="KGM">3762</cbc:NetWeightMeasure>
      <cbc:LoadingLengthMeasure unitCode="MTR">9.3</cbc:LoadingLengthMeasure>
      <cbc:Remarks>Received in apparent good order; seals XU-CL-77310 on the trailer doors.</cbc:Remarks>
      <cbc:ContainerizedIndicator>false</cbc:ContainerizedIndicator>
      <cbc:GeneralCargoIndicator>true</cbc:GeneralCargoIndicator>
      <cbc:ThirdPartyPayerIndicator>false</cbc:ThirdPartyPayerIndicator>
      <cbc:CustomsClearanceServiceInstructions>The export is declared by the 3PL in Ferrano; the import by the distributor at the border.</cbc:CustomsClearanceServiceInstructions>
      <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">25</cbc:TotalTransportHandlingUnitQuantity>
      <cbc:DeliveryInstructions>Unload at dock 4; report to the gatehouse first.</cbc:DeliveryInstructions>
      <cbc:HaulageInstructions>Wait at the warehouse until customs has released the export declaration.</cbc:HaulageInstructions>
      <cbc:TotalPackagesQuantity unitCode="EA">108</cbc:TotalPackagesQuantity>
      <cac:CustomsDeclaration>
        <cbc:ID>VI-CD-26-0156</cbc:ID>
        <cac:IssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Customs Administration of Urvania</cbc:Name>
          </cac:PartyName>
        </cac:IssuerParty>
      </cac:CustomsDeclaration>
      <cac:ActualPickupTransportEvent>
        <cbc:OccurrenceDate>2026-03-23</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>15:05:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualPickupTransportEvent>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:ConsigneeParty>
      <cac:OriginalDepartureCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:FinalDestinationCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:FinalDestinationCountry>
      <cac:DeliveryTerms>
        <cbc:ID schemeID="INCOTERMS">FCA</cbc:ID>
        <cbc:SpecialTerms>The buyer's carrier presents the truck; the seller loads it.</cbc:SpecialTerms>
        <cbc:LossRiskResponsibilityCode listID="urn:ubl-examples:world:codelist:RiskResponsiblePartyCode">BUYER</cbc:LossRiskResponsibilityCode>
        <cbc:LossRisk>The risk passes on loading at the 3PL's warehouse.</cbc:LossRisk>
      </cac:DeliveryTerms>
      <cac:CollectPaymentTerms>
        <cbc:Note>The freight is paid by the consignee under its contract with the carrier.</cbc:Note>
      </cac:CollectPaymentTerms>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">TRUCKTRAILER</cbc:TransportMeansTypeCode>
        <cbc:TransitDirectionCode listID="urn:ubl-examples:world:codelist:TransitDirectionCode">EXPORT</cbc:TransitDirectionCode>
        <cbc:CabotageIndicator>false</cbc:CabotageIndicator>
        <cbc:EstimatedDeliveryDate>2026-03-25</cbc:EstimatedDeliveryDate>
        <cbc:EstimatedDeliveryTime>09:00:00</cbc:EstimatedDeliveryTime>
        <cbc:RequiredDeliveryDate>2026-03-25</cbc:RequiredDeliveryDate>
        <cbc:RequiredDeliveryTime>10:00:00</cbc:RequiredDeliveryTime>
        <cac:TransitPeriod>
          <cbc:StartDate>2026-03-23</cbc:StartDate>
          <cbc:EndDate>2026-03-25</cbc:EndDate>
        </cac:TransitPeriod>
        <cac:TransportMeans>
          <cbc:JourneyID>TH-26-04471</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">TRUCKTRAILER</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 KT</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 TR</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
          <cac:OwnerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Trasvia Haulage</cbc:Name>
            </cac:PartyName>
          </cac:OwnerParty>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LOADINGLENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MTR">13.6</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBMRW</cbc:ID>
          <cbc:Name>Marrowdale</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:ExaminationTransportEvent>
          <cbc:OccurrenceDate>2026-03-24</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>07:45:00</cbc:OccurrenceTime>
          <cbc:Description>Seal check, no inspection of the goods.</cbc:Description>
        </cac:ExaminationTransportEvent>
        <cac:ActualDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-03-23</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>16:20:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:ActualDepartureTransportEvent>
        <cac:DriverPerson>
          <cbc:ID>XU-DL-0417722</cbc:ID>
          <cbc:FirstName>Ilario</cbc:FirstName>
          <cbc:FamilyName>Bencetti</cbc:FamilyName>
        </cac:DriverPerson>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-001</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 001 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-001</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-001</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-001-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-002</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 002 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-002</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-002</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-002-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-003</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 003 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-003</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-003</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-003-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-004</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 004 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-004</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-004</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-004-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-005</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 005 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-005</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-005</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-005-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-006</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 006 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-006</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-006</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-006-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-007</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 007 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-007</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-007</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-007-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-008</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 008 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-008</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-008</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-008-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-009</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 009 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-009</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-009</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-009-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-010</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 010 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-010</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-010</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-010-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-011</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 011 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-011</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-011</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-011-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-012</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 012 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-012</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-012</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-012-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-013</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 013 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-013</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-013</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-013-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-014</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 014 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-014</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-014</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-014-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-015</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 015 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-015</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-015</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-015-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-016</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 016 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-016</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-016</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-016-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-017</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 017 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-017</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-017</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-017-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-018</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 018 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-018</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-018</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-018-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-019</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 019 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-019</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-019</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-019-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-020</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 020 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-020</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-020</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-020-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-021</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 021 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-021</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-021</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-021-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-022</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 022 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-022</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-022</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-022-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-023</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 023 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-023</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-023</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-023-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-024</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
        <cbc:HandlingInstructions>May be stacked two high, steel frames on steel frames.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 024 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-024</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-024</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1850</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1650</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">1.2</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">0.5</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-024-1</cbc:ID>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SW</cbc:PackagingTypeCode>
          <cbc:PackagingType>Bench in stretch film</cbc:PackagingType>
          <cbc:PackingMaterial>Recycled PE stretch film</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>CL-26-025</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">NOSTACK</cbc:HandlingCode>
        <cbc:HandlingInstructions>Load on top: nothing may be stacked on the boxes.</cbc:HandlingInstructions>
        <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>LD MARROWDALE / 025 of 025</cbc:ShippingMarks>
        <cbc:TraceID>CL-26-025</cbc:TraceID>
        <cac:ActualPackage>
          <cbc:ID>CL-26-025</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        </cac:ActualPackage>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1200</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">800</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">900</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:FloorSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
          <cbc:Measure unitCode="MTK">0.96</cbc:Measure>
        </cac:FloorSpaceMeasurementDimension>
        <cac:PalletSpaceMeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
          <cbc:Measure unitCode="C62">1</cbc:Measure>
        </cac:PalletSpaceMeasurementDimension>
        <cac:Package>
          <cbc:ID>CL-26-025-1</cbc:ID>
          <cbc:Quantity unitCode="EA">12</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
          <cbc:PackagingType>Cardboard box</cbc:PackagingType>
          <cbc:PackingMaterial>Corrugated cardboard</cbc:PackingMaterial>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:Delivery>
      <cbc:LatestDeliveryDate>2026-03-25</cbc:LatestDeliveryDate>
      <cbc:LatestDeliveryTime>12:00:00</cbc:LatestDeliveryTime>
      <cbc:TrackingID>TH-26-04471</cbc:TrackingID>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-03-25</cbc:StartDate>
        <cbc:StartTime>09:00:00</cbc:StartTime>
        <cbc:EndTime>11:00:00</cbc:EndTime>
      </cac:EstimatedDeliveryPeriod>
      <cac:FuelConsumption>
        <cbc:ID>TH-FC-26-0159</cbc:ID>
        <cbc:FuelTypeCode listID="urn:ubl-examples:world:codelist:FuelTypeCode">DIESEL</cbc:FuelTypeCode>
        <cbc:FuelConsumptionMeasure unitCode="LTR">61</cbc:FuelConsumptionMeasure>
      </cac:FuelConsumption>
    </cac:Delivery>
    <cac:ReturnAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
      <cbc:BuildingNumber>24</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4130</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:ReturnAddress>
    <cac:OriginAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
      <cbc:BuildingNumber>24</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4130</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:OriginAddress>
    <cac:ExportCountry>
      <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
    </cac:ExportCountry>
  </cac:Shipment>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentCopyTypeCode">ORIGINAL</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">PAPER</cbc:DistributionTypeCode>
    <cbc:DistributionType>With the goods</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentCopyTypeCode">COPY</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONIC</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>TH-SIG-TH-WB-26-0159</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Trasvia Haulage</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
