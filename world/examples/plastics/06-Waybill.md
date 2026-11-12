# Waybill: Fiumella Barges to Rinova Recovery

*Example 6 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The inland waterway consignment note, issued to the shipper.

[The XML file](06-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); PartyLegalEntity/EntitySizeCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **PLASTICS-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FB-WB-26-0890**  
  The consignment note number.
- `CarrierAssignedID` = **FB-CMNI-26-0882**  
  The carrier's own number for the carriage.
- `UUID` = **0a38e2bd-26a7-55f9-833d-9ab2e55cfd4a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-04-19**  
  Issued when the barge is loaded.
- `IssueTime` = **09:38:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Inland waterway consignment note under the CMNI**  
  The kind of transport document.
- `Description` = **The barge from the quay next to the recovery plant down the river to the packaging maker.**  
  The carriage in words.
- `Note` = **Gurbul mizstan: dadrek, miran, sundraz.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): As the convention prescribes.
- `Note` = **Three originals: consignor, consignee, carrier.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: As the convention prescribes.
- `ShippingOrderID` = **RR-CS-26-0885**  
  The shipper's booking the carriage fulfils.
- `WaybillTypeCode` = **CMNI** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: CMNI = Inland waterway waybill (CMNI).
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `AdValoremIndicator` = **false**  
  No value declared to raise the carrier's liability.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Fiumella Barges**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.fiumella.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Fiumella Barges (world/parties.json).
- `IndustryClassificationCode` = **5022** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Fiumella Barges (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5022 = Inland freight water transport.
- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Fiumella Barges**  
  The trading name; identity of Fiumella Barges (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160204198475331** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Fiumella Barges (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Skikzek Han Nestan** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Fiumella Barges (world/parties.json).
- `PostalAddress/StreetName` = **Banchina del Fiume** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Fiumella Barges (world/parties.json).
- `PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits). identity of Fiumella Barges (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Fiumella Barges SRU**  
  The name under which the party is registered for value added tax; identity of Fiumella Barges (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007347248** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Fiumella Barges (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Fiumella Barges SRU**  
  The name under which the party is registered, with its legal form; identity of Fiumella Barges (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Fiumella Barges (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 30 persons and its turnover of 540000000 XUF in 2025, by the Trade Accord's limits; identity of Fiumella Barges (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
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
- `Contact/Name` = **Chartering desk**  
  The desk that handles this document; identity of Fiumella Barges (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Fiumella Barges (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Fiumella Barges (world/parties.json).
- `Contact/Telephone` = **+999 1 041 513 4959**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Fiumella Barges (world/parties.json).
- `Contact/ElectronicMail` = **chartering@fiumella.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Fiumella Barges (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Fiumella Barges (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Fiumella Barges (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.rinova.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rinova Recovery (world/parties.json).
- `IndustryClassificationCode` = **3830** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rinova Recovery (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3830 = Materials recovery.
- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Rinova Recovery (world/parties.json).
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered for value added tax; identity of Rinova Recovery (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007318479** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Rinova Recovery (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered, with its legal form; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 47 persons and its turnover of 722000000 XUF in 2025, by the Trade Accord's limits; identity of Rinova Recovery (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
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
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Rinova Recovery (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rinova Recovery (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rinova Recovery (world/parties.json).
- `Contact/Telephone` = **+999 1 041 836 4548**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Rinova Recovery (world/parties.json).
- `Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/PurposeCode` = **R3** (listID `Basel Convention Annex IV`)  
  The purpose as a code. The code is from the world's copy of Basel Convention, Annex IV: disposal and recovery operations: R3 = Recycling/reclamation of organic substances which are not used as solvents.
- `PartyAuthorization/Purpose` = **Recovery of non-hazardous plastic waste**  
  What the authority has authorized the party to do; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/ValidityPeriod/EndDate` = **2029-12-31**  
  The authorization expires on this date.
- `PartyAuthorization/Certificate/ID` = **XU-ENV-2024-0311** (schemeID `urn:ubl-examples:world:XU:waste-permit`)  
  The number of the permit in the register of waste treatment permits of Urvania; the schemeID names the register, and with it the authority that keeps it, so no issuer party is needed (decision ID-Q10).
- `PartyAuthorization/Certificate/CertificateTypeCode` = **PERMIT** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A permit issued by an authority of the party's country. The code is from the Trade Accord's certificate type list: PERMIT = Operating permit.
- `PartyAuthorization/Certificate/CertificateType` = **Kusul treznul** (languageID `qau`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `PartyAuthorization/Certificate/CertificateType` = **Operating permit** (languageID `en-XU`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In English.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rinova Recovery**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Fiumella Barges**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **RR-SH-26-0889**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight on board.
- `Consignment/ID` = **RR-CS-26-0885**  
  The seller's consignment number.
- `Consignment/CarrierAssignedID` = **FB4-26-031/2**  
  The barge operator's number: the second lot of the voyage.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.rivermouth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **2220** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rivermouth Packaging (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 2220 = Manufacture of plastics products.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **0990:20274** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `Consignment/ConsigneeParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyTaxScheme/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered for state sales tax; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyTaxScheme/CompanyID` = **CO-1238220** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Rivermouth Packaging (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered, with its legal form; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 23 persons and its turnover of 6800000.00 XBL in 2025, by the Trade Accord's limits; identity of Rivermouth Packaging (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 38 2440 2740**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/ID` = **XB96BLUM38020504712805** (schemeID `urn:ubl-examples:world:account`)  
  The party's account, given with its details so that payments can be sent to it. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `Consignment/ConsigneeParty/FinancialAccount/Name` = **Rivermouth Packaging Ltd**  
  The account holder, as the bank knows it.
- `Consignment/ConsigneeParty/FinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `Consignment/ConsigneeParty/FinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `Consignment/ConsigneeParty/FinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/ID` = **380205** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/Name` = **Harbour branch**  
  The branch's name.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BLUM, the country XB and the location LX; identity of Bank of Lumeport (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  Street of the postal address. identity of Bank of Lumeport (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Building number of the postal address. identity of Bank of Lumeport (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bank of Lumeport (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). identity of Bank of Lumeport (world/parties.json).
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bank of Lumeport (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `Consignment/ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/FinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The freight, a charge.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **River freight**  
  What it is for.
- `Consignment/FreightAllowanceCharge/Amount` = **179400** (currencyID `XUF`)  
  120 tonnes at 1,495 ferra.
- `Consignment/FreightAllowanceCharge/BaseAmount` = **1495** (currencyID `XUF`)  
  The rate per tonne.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  Down the river, from the recovery plant's quay to the river quay in Lumeport.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **8** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 8: inland water transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 8 = Inland water transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **FB4-26-031**  
  The barge operator's voyage number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **DS** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: DS = Downstream.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **815** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: fiumella IV; the fleet of Fiumella Barges (world/parties.json). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 815 = Freight barge.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XU-IW-08042** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Fiumella IV**  
  The vessel's name; the fleet of Fiumella Barges (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QUBF4**  
  The radio call sign, in Urvania's call sign series QU: no ITU series starts with Q, so the sign belongs to no real station (world/countries.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **297801042**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 297 of Urvania, which the ITU has not allocated to any real country, and the ship's six digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **1210** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **860** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **DRYBARGE** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel. The code is from the Trade Accord's ship configuration list: DRYBARGE = Dry cargo barge.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Ferrano**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Quay of Rinova Recovery, Ferrano**  
  Where the bags are loaded.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **River quay, Lumeport**  
  The place named in the CPT terms.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceDate` = **2026-04-19**  
  Loading finished: 120 bags in the hold.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceTime` = **13:30:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceDate` = **2026-04-20**  
  The barge leaves Urvania at the river border.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceTime` = **16:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-04-22**  
  Planned unloading at the Lumeport quay.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **08:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceDate` = **2026-04-19**  
  The barge operator takes over the bags at the quay.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceTime` = **09:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedTransitPeriod/DurationMeasure` = **3** (unitCode `DAY`)  
  Three days downstream, with the locks.
- `Consignment/MainCarriageShipmentStage/MasterPerson/FirstName` = **Tomaso**  
  The skipper of the barge.
- `Consignment/MainCarriageShipmentStage/MasterPerson/FamilyName` = **Riverra**  
  The family name.
- `Consignment/MainCarriageShipmentStage/MasterPerson/JobTitle` = **Skipper**  
  The person's position.
- `GoodsItem/ID` = **1**  
  The only goods item.
- `GoodsItem/SequenceNumberID` = **1**  
  Its place in the cargo list.
- `GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are.
- `GoodsItem/DeclaredForCarriageValueAmount` = **9984000** (currencyID `XUF`)  
  Declared to the barge operator, which raises its liability to this value.
- `GoodsItem/ValueAmount` = **9984000** (currencyID `XUF`)  
  The value of the goods, the sales price under CPT.
- `GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  With the bags.
- `GoodsItem/NetWeightMeasure` = **120000** (unitCode `KGM`)  
  The granulate alone.
- `GoodsItem/NetNetWeightMeasure` = **120000** (unitCode `KGM`)  
  No inner packaging: the same as the net weight.
- `GoodsItem/ChargeableWeightMeasure` = **120000** (unitCode `KGM`)  
  The freight is charged per tonne of granulate.
- `GoodsItem/GrossVolumeMeasure` = **204** (unitCode `MTQ`)  
  The 120 bags take 1.7 m³ each.
- `GoodsItem/NetVolumeMeasure` = **130** (unitCode `MTQ`)  
  The granulate's own volume, at 0.92 tonne per m³.
- `GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  120 tonnes.
- `GoodsItem/ChargeableQuantity` = **120** (unitCode `TNE`)  
  The tonnes charged.
- `GoodsItem/ReturnableQuantity` = **120** (unitCode `EA`)  
  The 120 jumbo bags go back to the recovery plant.
- `GoodsItem/TraceID` = **RR-PE-LOT-26-0416**  
  The lot on the bags' labels.
- `GoodsItem/OrderLineReference/LineID` = **1**  
  The order line.
- `GoodsItem/OrderLineReference/OrderReference/ID` = **RP-PO-26-0882**  
  The buyer's order.
- `GoodsItem/OriginAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `GoodsItem/OriginAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `GoodsItem/OriginAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `GoodsItem/OriginAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/OriginAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `GoodsItem/Delivery/LatestDeliveryDate` = **2026-04-23**  
  The packaging maker's production starts the day after.
- `GoodsItem/Pickup/EarliestPickupDate` = **2026-04-19**  
  The bags are ready on the quay.
- `GoodsItem/Pickup/EarliestPickupTime` = **08:00:00**  
  From eight.
- `GoodsItem/Pickup/LatestPickupDate` = **2026-04-19**  
  They must go the same day.
- `GoodsItem/Pickup/LatestPickupTime` = **16:00:00**  
  Before the quay closes.
- `GoodsItem/Despatch/ActualDespatchDate` = **2026-04-19**  
  The barge cast off.
- `GoodsItem/Despatch/ActualDespatchTime` = **15:10:00**  
  In the afternoon.
- `GoodsItem/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of one filled bag. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MeasurementDimension/Measure` = **1300** (unitCode `MMT`)  
  In millimetres.
- `GoodsItem/ContainingPackage/ID` = **RR-JB-0416**  
  The 120 bags of the lot as one package entry, with their number: the plant numbers its bags by lot.
- `GoodsItem/ContainingPackage/Quantity` = **120** (unitCode `EA`)  
  120 bags.
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The bags go back for reuse.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **JB** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code JB: bag, jumbo. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: JB = Bag, jumbo.
- `GoodsItem/ContainingPackage/PackagingType` = **Jumbo bag of one tonne with four lifting loops**  
  In words.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Woven polypropylene**  
  What the bags are made of.
- `GoodsItem/ShipmentDocumentReference/ID` = **FB-TEP-26-0886**  
  The transport plan of the sailing.
- `GoodsItem/EnergyConsumptionAllocation/EnergySourceTypeCode` = **DIESEL** (listID `urn:ubl-examples:world:codelist:EnergySourceCode`)  
  The barge's engine fuel. The code is from the Trade Accord's energy source list: DIESEL = Diesel.
- `GoodsItem/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **5400** (unitCode `KWH`)  
  The goods' share of the voyage's energy, as fuel energy.
- `GoodsItem/EnergyConsumptionAllocation/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `GoodsItem/EnergyConsumptionAllocation/EnvironmentalEmission/ValueMeasure` = **14.3** (unitCode `KGM`)  
  2.65 kg per litre of the diesel allocated.

### Document Reference

Inside `DocumentReference`:

- `ID` = **FB-TEP-26-0886**  
  The transport plan under which the carriage is performed.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The original for the consignee.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALWITHGOODS** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  One of the three originals travels with the goods to the consignee, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALWITHGOODS = Original, with the goods.
- `DistributionType` = **Rikzhek, vek drek valnir: drek trelgir rikzhek** (languageID `qau`)  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery. In Urvanian, the sender's language.
- `DistributionType` = **Original, with the goods: the consignee's original** (languageID `en-XU`)  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery. In English.
- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The electronic copy.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ELECTRONICCOPY** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The receiver of this message gets a copy, for its records; the originals are on paper. The code is from the Trade Accord's distribution type list: ELECTRONICCOPY = Electronic copy.
- `DistributionType` = **Viskir zuzzir** (languageID `qau`)  
  The name of code ELECTRONICCOPY in the Trade Accord's distribution type list. In Urvanian, the sender's language.
- `DistributionType` = **Electronic copy** (languageID `en-XU`)  
  The name of code ELECTRONICCOPY in the Trade Accord's distribution type list. In English.
- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FB-SIG-FB-WB-26-0890**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Fiumella Barges**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waybill:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PLASTICS-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FB-WB-26-0890</cbc:ID>
  <cbc:CarrierAssignedID>FB-CMNI-26-0882</cbc:CarrierAssignedID>
  <cbc:UUID>0a38e2bd-26a7-55f9-833d-9ab2e55cfd4a</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-04-19</cbc:IssueDate>
  <cbc:IssueTime>09:38:00</cbc:IssueTime>
  <cbc:Name>Inland waterway consignment note under the CMNI</cbc:Name>
  <cbc:Description>The barge from the quay next to the recovery plant down the river to the packaging maker.</cbc:Description>
  <cbc:Note languageID="qau">Gurbul mizstan: dadrek, miran, sundraz.</cbc:Note>
  <cbc:Note languageID="en-XU">Three originals: consignor, consignee, carrier.</cbc:Note>
  <cbc:ShippingOrderID>RR-CS-26-0885</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">CMNI</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Fiumella Barges</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.fiumella.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5022</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160204198475331</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Skikzek Han Nestan</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Banchina del Fiume</cbc:StreetName>
      <cbc:BuildingNumber>52</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4170</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Fiumella Barges SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007347248</cbc:CompanyID>
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
      <cbc:RegistrationName>Fiumella Barges SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
      <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
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
      <cbc:Name>Chartering desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 041 513 4959</cbc:Telephone>
      <cbc:ElectronicMail>chartering@fiumella.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104959</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.rinova.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3830</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202983340277</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007318479</cbc:CompanyID>
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
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
      <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 836 4548</cbc:Telephone>
      <cbc:ElectronicMail>customer@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:PartyAuthorization>
      <cbc:PurposeCode listID="Basel Convention Annex IV">R3</cbc:PurposeCode>
      <cbc:Purpose>Recovery of non-hazardous plastic waste</cbc:Purpose>
      <cac:ValidityPeriod>
        <cbc:EndDate>2029-12-31</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:Certificate>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:waste-permit">XU-ENV-2024-0311</cbc:ID>
        <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">PERMIT</cbc:CertificateTypeCode>
        <cbc:CertificateType languageID="qau">Kusul treznul</cbc:CertificateType>
        <cbc:CertificateType languageID="en-XU">Operating permit</cbc:CertificateType>
      </cac:Certificate>
    </cac:PartyAuthorization>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>RR-SH-26-0889</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>RR-CS-26-0885</cbc:ID>
      <cbc:CarrierAssignedID>FB4-26-031/2</cbc:CarrierAssignedID>
      <cac:ConsigneeParty>
        <cbc:WebsiteURI>https://www.rivermouth.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">2220</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="ISO 6523">0990:20274</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Rivermouth Packaging</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-411619</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Estuary Road</cbc:StreetName>
          <cbc:BuildingNumber>28</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38505</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1238220</cbc:CompanyID>
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
          <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:CompanyID>
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
          <cbc:Name>Order desk</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 2 38 2440 2740</cbc:Telephone>
          <cbc:ElectronicMail>order@rivermouth.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:FinancialAccount>
          <cbc:ID schemeID="urn:ubl-examples:world:account">XB96BLUM38020504712805</cbc:ID>
          <cbc:Name>Rivermouth Packaging Ltd</cbc:Name>
          <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
          <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:FinancialInstitutionBranch>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:bank-branch">380205</cbc:ID>
            <cbc:Name>Harbour branch</cbc:Name>
            <cac:FinancialInstitution>
              <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">BLUMXBLX</cbc:ID>
              <cbc:Name>Bank of Lumeport</cbc:Name>
              <cac:Address>
                <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
                <cbc:StreetName>Exchange Street</cbc:StreetName>
                <cbc:BuildingNumber>48</cbc:BuildingNumber>
                <cbc:CityName>Lumeport</cbc:CityName>
                <cbc:PostalZone>38523</cbc:PostalZone>
                <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
                <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
                  <cbc:Name>Bayvarra</cbc:Name>
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
        </cac:FinancialAccount>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>River freight</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XUF">179400</cbc:Amount>
        <cbc:BaseAmount currencyID="XUF">1495</cbc:BaseAmount>
      </cac:FreightAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">8</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>FB4-26-031</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">DS</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">815</cbc:TransportMeansTypeCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XU-IW-08042</cbc:VesselID>
            <cbc:VesselName>Fiumella IV</cbc:VesselName>
            <cbc:RadioCallSignID>QUBF4</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>297801042</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">1210</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">860</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">DRYBARGE</cbc:ShipConfigurationCode>
            <cac:RegistryPortLocation>
              <cbc:Name>Ferrano</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:Name>River quay, Lumeport</cbc:Name>
        </cac:UnloadingPortLocation>
        <cac:LoadingTransportEvent>
          <cbc:OccurrenceDate>2026-04-19</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:30:00</cbc:OccurrenceTime>
        </cac:LoadingTransportEvent>
        <cac:ExportationTransportEvent>
          <cbc:OccurrenceDate>2026-04-20</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>16:00:00</cbc:OccurrenceTime>
        </cac:ExportationTransportEvent>
        <cac:DischargeTransportEvent>
          <cbc:OccurrenceDate>2026-04-22</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>08:00:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        </cac:DischargeTransportEvent>
        <cac:TakeoverTransportEvent>
          <cbc:OccurrenceDate>2026-04-19</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>09:00:00</cbc:OccurrenceTime>
        </cac:TakeoverTransportEvent>
        <cac:EstimatedTransitPeriod>
          <cbc:DurationMeasure unitCode="DAY">3</cbc:DurationMeasure>
        </cac:EstimatedTransitPeriod>
        <cac:MasterPerson>
          <cbc:FirstName>Tomaso</cbc:FirstName>
          <cbc:FamilyName>Riverra</cbc:FamilyName>
          <cbc:JobTitle>Skipper</cbc:JobTitle>
        </cac:MasterPerson>
      </cac:MainCarriageShipmentStage>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
      <cbc:Description>Recycled PE granulate</cbc:Description>
      <cbc:DeclaredForCarriageValueAmount currencyID="XUF">9984000</cbc:DeclaredForCarriageValueAmount>
      <cbc:ValueAmount currencyID="XUF">9984000</cbc:ValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cbc:NetWeightMeasure unitCode="KGM">120000</cbc:NetWeightMeasure>
      <cbc:NetNetWeightMeasure unitCode="KGM">120000</cbc:NetNetWeightMeasure>
      <cbc:ChargeableWeightMeasure unitCode="KGM">120000</cbc:ChargeableWeightMeasure>
      <cbc:GrossVolumeMeasure unitCode="MTQ">204</cbc:GrossVolumeMeasure>
      <cbc:NetVolumeMeasure unitCode="MTQ">130</cbc:NetVolumeMeasure>
      <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
      <cbc:ChargeableQuantity unitCode="TNE">120</cbc:ChargeableQuantity>
      <cbc:ReturnableQuantity unitCode="EA">120</cbc:ReturnableQuantity>
      <cbc:TraceID>RR-PE-LOT-26-0416</cbc:TraceID>
      <cac:OrderLineReference>
        <cbc:LineID>1</cbc:LineID>
        <cac:OrderReference>
          <cbc:ID>RP-PO-26-0882</cbc:ID>
        </cac:OrderReference>
      </cac:OrderLineReference>
      <cac:OriginAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
        <cbc:BuildingNumber>31</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4140</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:OriginAddress>
      <cac:Delivery>
        <cbc:LatestDeliveryDate>2026-04-23</cbc:LatestDeliveryDate>
      </cac:Delivery>
      <cac:Pickup>
        <cbc:EarliestPickupDate>2026-04-19</cbc:EarliestPickupDate>
        <cbc:EarliestPickupTime>08:00:00</cbc:EarliestPickupTime>
        <cbc:LatestPickupDate>2026-04-19</cbc:LatestPickupDate>
        <cbc:LatestPickupTime>16:00:00</cbc:LatestPickupTime>
      </cac:Pickup>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-04-19</cbc:ActualDespatchDate>
        <cbc:ActualDespatchTime>15:10:00</cbc:ActualDespatchTime>
      </cac:Despatch>
      <cac:MeasurementDimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1300</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:ContainingPackage>
        <cbc:ID>RR-JB-0416</cbc:ID>
        <cbc:Quantity unitCode="EA">120</cbc:Quantity>
        <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">JB</cbc:PackagingTypeCode>
        <cbc:PackagingType>Jumbo bag of one tonne with four lifting loops</cbc:PackagingType>
        <cbc:PackingMaterial>Woven polypropylene</cbc:PackingMaterial>
      </cac:ContainingPackage>
      <cac:ShipmentDocumentReference>
        <cbc:ID>FB-TEP-26-0886</cbc:ID>
      </cac:ShipmentDocumentReference>
      <cac:EnergyConsumptionAllocation>
        <cbc:EnergySourceTypeCode listID="urn:ubl-examples:world:codelist:EnergySourceCode">DIESEL</cbc:EnergySourceTypeCode>
        <cbc:AllocatedEnergyMeasure unitCode="KWH">5400</cbc:AllocatedEnergyMeasure>
        <cac:EnvironmentalEmission>
          <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
          <cbc:ValueMeasure unitCode="KGM">14.3</cbc:ValueMeasure>
        </cac:EnvironmentalEmission>
      </cac:EnergyConsumptionAllocation>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>FB-TEP-26-0886</cbc:ID>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALWITHGOODS</cbc:DistributionTypeCode>
    <cbc:DistributionType languageID="qau">Rikzhek, vek drek valnir: drek trelgir rikzhek</cbc:DistributionType>
    <cbc:DistributionType languageID="en-XU">Original, with the goods: the consignee's original</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONICCOPY</cbc:DistributionTypeCode>
    <cbc:DistributionType languageID="qau">Viskir zuzzir</cbc:DistributionType>
    <cbc:DistributionType languageID="en-XU">Electronic copy</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FB-SIG-FB-WB-26-0890</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Fiumella Barges</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
