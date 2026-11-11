# Waybill: Kelaro Air Cargo to Bayforth Forwarding

*Example 3 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The air waybill for cargo aircraft only, with the dangerous goods on it.

[The XML file](03-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:mast**  
  The business process the document belongs to: the flow "Batteries for the island's telecom mast, by air (dangerous goods)".
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **KAC-WB-26-0717**  
  The consignment note number.
- `CarrierAssignedID` = **KAC-AWB-26-0713**  
  The carrier's own number for the carriage.
- `UUID` = **bf007d9d-013c-5ef5-8c7c-b450b24811d3**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-06-04**  
  The air waybill, cargo aircraft only.
- `IssueTime` = **17:15:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Air waybill under the Montreal Convention**  
  The kind of transport document.
- `Description` = **A cargo-aircraft-only flight to the island.**  
  The carriage in words.
- `Note` = **Tasela kukohane: titoluva, hivokefi, topatu.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): As the convention prescribes.
- `Note` = **Three originals: consignor, consignee, carrier.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: As the convention prescribes.
- `ShippingOrderID` = **SE-CS-26-0716**  
  The shipper's booking the carriage fulfils.
- `WaybillTypeCode` = **AWB** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: AWB = Air waybill.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `AdValoremIndicator` = **false**  
  No value declared to raise the carrier's liability.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Lumeport Airport Cargo Terminal**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.kelaro.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Kelaro Air Cargo (world/parties.json).
- `IndustryClassificationCode` = **5120** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Kelaro Air Cargo (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5120 = Freight air transport.
- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; identity of Kelaro Air Cargo (world/parties.json).
- `Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/ID` = **58930746** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Kelaro Air Cargo Ltd**  
  The name under which the party is registered, with its legal form; identity of Kelaro Air Cargo (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Kelaro Air Cargo (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 13 persons and its turnover of 2590000.000 XLC in 2025, by the Trade Accord's limits; identity of Kelaro Air Cargo (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Cargo sales**  
  The desk that handles this document; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Telephone` = **+999 3 721 1311**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Kelaro Air Cargo (world/parties.json).
- `Contact/ElectronicMail` = **cargo@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Kelaro Air Cargo (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41311** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Kelaro Air Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.bayforth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Bayforth Forwarding (world/parties.json).
- `IndustryClassificationCode` = **5229** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Bayforth Forwarding (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5229 = Other transportation support activities.
- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered for state sales tax; identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1234932** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
- `PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 40 persons and its turnover of 6660000.00 XBL in 2025, by the Trade Accord's limits; identity of Bayforth Forwarding (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Export desk**  
  The desk that handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2144 1644**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `IndustryClassificationCode` = **4290** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Saltmere Engineering (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4290 = Construction of other civil engineering projects.
- `PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered for state sales tax; identity of Saltmere Engineering (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1232055** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Saltmere Engineering (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
- `PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered, with its legal form; identity of Saltmere Engineering (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
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
- `Contact/Name` = **Bids office**  
  The desk that handles this document; identity of Saltmere Engineering (world/parties.json).
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 885 685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Bayforth Forwarding**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SE-SH-26-0715**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **376** (unitCode `KGM`)  
  The gross weight.
- `Consignment/ID` = **SE-CS-26-0716**  
  The consignment of the transport booking.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.selanutelecom.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **6110** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Telecom (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 6110 = Wired telecommunications activities.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/ConsigneeParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 20 persons and its turnover of 3230000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Telecom (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/Contact/Name` = **Business accounts**  
  The desk that handles this document; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 727 2407**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/HazardousItemNotificationParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/HazardousItemNotificationParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Air transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.
- `Consignment/MainCarriageShipmentStage/HazardousRiskIndicator` = **true**  
  Dangerous goods on the flight.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **KAC209**  
  The cargo flight of the day.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XL** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Lisavu**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **CARGOAIRCRAFT** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The kind of means of transport: freighter of kelaro air cargo; the fleet of Kelaro Air Cargo (world/parties.json). The code is from the Trade Accord's transport means type list: CARGOAIRCRAFT = Cargo aircraft.
- `Consignment/MainCarriageShipmentStage/TransportMeans/AirTransport/AircraftID` = **QL-KAC** (schemeID `urn:ubl-examples:world:XL:aircraft-register`)  
  The aircraft's registration: the nationality mark QL of Lisavu, a mark no real state uses, and three letters; the fleet of Kelaro Air Cargo (world/parties.json). The schemeID names the scheme it is from: the civil aircraft register of Lisavu (the nationality mark QL, a hyphen and three letters).
- `Consignment/TransportHandlingUnit/ID` = **RKN41207K0**  
  The container as a handling unit.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods inside.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **RKN41207K0**  
  The temperature-controlled air container, numbered as unit load devices are: its type RKN, its serial number 41207 and the designator of its owner, the airline Kelaro Air Cargo (world/parties.json).
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **AM** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code AM: refrigerated container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: AM = Refrigerated container.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  The unit is switched on.
- `Consignment/TransportHandlingUnit/TransportEquipment/AirFlowPercent` = **40**  
  The fan's air flow.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumidityPercent` = **50**  
  Humidity kept below 50 %.
- `Consignment/TransportHandlingUnit/TransportEquipment/AnimalFoodApprovedIndicator` = **false**  
  Not for feed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumanFoodApprovedIndicator` = **false**  
  Not for food.
- `Consignment/TransportHandlingUnit/TransportEquipment/DangerousGoodsApprovedIndicator` = **true**  
  Approved for dangerous goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **true**  
  A temperature-controlled unit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **true**  
  Battery-powered cooling and heating.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %.**  
  The conditions.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ID` = **SE-BAT-48100-DG**  
  The battery packs in the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations UN number`)  
  The UN number of the battery packs. The code is from the world's copy of UN Model Regulations dangerous goods list (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/CategoryName` = **Miscellaneous dangerous goods**  
  Class 9 in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ProperShippingName` = **Lithium ion batteries**  
  As on the declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UpperOrangeHazardPlacardID` = **90**  
  The hazard identification number for road transport.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/LowerOrangeHazardPlacardID` = **3480**  
  The UN number on the orange plate.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  Class 9. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousTypeCode` = **ARTICLE** (listID `urn:ubl-examples:world:codelist:HazardousGoodsTypeCode`)  
  Batteries are articles, not substances. The code is from the Trade Accord's dangerous goods type list: ARTICLE = Article.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PackagingDangerLevelCode` = **4** (listID `UN/EDIFACT EDED 8339`)  
  The packaging danger level of UN/EDIFACT 8339 that matches the packing group: lithium batteries have none, which 8339 codes as not assigned. The code is from the world's copy of UN/EDIFACT 8339 Packaging danger level: 4 = Not assigned.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/GrossWeightMeasure` = **348** (unitCode `KGM`)  
  Six packs, packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetWeightMeasure` = **312** (unitCode `KGM`)  
  The packs alone.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetVolumeMeasure` = **0.24** (unitCode `MTQ`)  
  Their volume.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Quantity` = **6** (unitCode `EA`)  
  Six packs.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %.**  
  The conditions.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/EmergencyTemperature/AttributeID` = **EMERGENCY** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Above this, emergency procedures. The code is from the Trade Accord's temperature attribute list: EMERGENCY = Emergency temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/EmergencyTemperature/Measure` = **60** (unitCode `CEL`)  
  Thermal runaway risk.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/AdditionalTemperature/AttributeID` = **STORAGE** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Recommended storage. The code is from the Trade Accord's temperature attribute list: STORAGE = Storage temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/AdditionalTemperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/LocationID` = **MD-L2**  
  Main deck, position L2.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/Location` = **Main deck, accessible**  
  Where it flies.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/Quantity` = **6** (unitCode `EA`)  
  Six crates, one battery pack in each; each crate is listed with its own number in the unit load device below.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %.**  
  The conditions.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-1**  
  Crate 1 of six: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery pack in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0001**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-2**  
  Crate 2 of six: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery pack in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0002**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-3**  
  Crate 3 of six: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery pack in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0003**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-4**  
  Crate 4 of six: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery pack in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0004**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-5**  
  Crate 5 of six: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery pack in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0005**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-6**  
  Crate 6 of six: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery pack in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0006**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.

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
- `Party/PartyIdentification/ID` = **IC41174** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Selanu Airport Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The electronic copy.
- `DocumentTypeCode` = **COPY** (listID `urn:ubl-examples:world:codelist:DocumentCopyTypeCode`)  
  A copy. The code is from the Trade Accord's document copy type list: COPY = Copy.
- `DistributionTypeCode` = **ELECTRONIC** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  Sent as this UBL document. The code is from the Trade Accord's distribution type list: ELECTRONIC = Electronic.
- `Party/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **KAC-SIG-KAC-WB-26-0717**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Kelaro Air Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:mast</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>KAC-WB-26-0717</cbc:ID>
  <cbc:CarrierAssignedID>KAC-AWB-26-0713</cbc:CarrierAssignedID>
  <cbc:UUID>bf007d9d-013c-5ef5-8c7c-b450b24811d3</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-06-04</cbc:IssueDate>
  <cbc:IssueTime>17:15:00</cbc:IssueTime>
  <cbc:Name>Air waybill under the Montreal Convention</cbc:Name>
  <cbc:Description>A cargo-aircraft-only flight to the island.</cbc:Description>
  <cbc:Note languageID="qal">Tasela kukohane: titoluva, hivokefi, topatu.</cbc:Note>
  <cbc:Note languageID="en-XL">Three originals: consignor, consignee, carrier.</cbc:Note>
  <cbc:ShippingOrderID>SE-CS-26-0716</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">AWB</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.kelaro.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5120</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">58930746</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Airfield Road</cbc:StreetName>
      <cbc:BuildingNumber>46</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Kelaro Air Cargo Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:CompanyID>
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
      <cbc:Name>Cargo sales</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 3 721 1311</cbc:Telephone>
      <cbc:ElectronicMail>cargo@kelaro.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41311</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.bayforth.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5229</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1234932</cbc:CompanyID>
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
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:CompanyID>
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
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38 2144 1644</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4290</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Saltmere Engineering</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-587295</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Foundry Road</cbc:StreetName>
      <cbc:BuildingNumber>13</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71218</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1232055</cbc:CompanyID>
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
      <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:CompanyID>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
      <cbc:Name>Bids office</cbc:Name>
      <cbc:JobTitle>Procurement officer</cbc:JobTitle>
      <cbc:Department>Procurement</cbc:Department>
      <cbc:Telephone>+999 2 7121 885 685</cbc:Telephone>
      <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>SE-SH-26-0715</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">376</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>SE-CS-26-0716</cbc:ID>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:ConsigneeParty>
        <cbc:WebsiteURI>https://www.selanutelecom.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">6110</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Telecom</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">34928611</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Mast Hill Road</cbc:StreetName>
          <cbc:BuildingNumber>58</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Selanu Telecom Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:CompanyID>
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
          <cbc:Name>Business accounts</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 3 727 2407</cbc:Telephone>
          <cbc:ElectronicMail>business@selanutelecom.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
      <cac:HazardousItemNotificationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
      </cac:HazardousItemNotificationParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportMeans>
          <cbc:JourneyID>KAC209</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XL</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Lisavu</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">CARGOAIRCRAFT</cbc:TransportMeansTypeCode>
          <cac:AirTransport>
            <cbc:AircraftID schemeID="urn:ubl-examples:world:XL:aircraft-register">QL-KAC</cbc:AircraftID>
          </cac:AirTransport>
        </cac:TransportMeans>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cbc:ID>RKN41207K0</cbc:ID>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportEquipment>
          <cbc:ID>RKN41207K0</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">AM</cbc:TransportEquipmentTypeCode>
          <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
          <cbc:AirFlowPercent>40</cbc:AirFlowPercent>
          <cbc:HumidityPercent>50</cbc:HumidityPercent>
          <cbc:AnimalFoodApprovedIndicator>false</cbc:AnimalFoodApprovedIndicator>
          <cbc:HumanFoodApprovedIndicator>false</cbc:HumanFoodApprovedIndicator>
          <cbc:DangerousGoodsApprovedIndicator>true</cbc:DangerousGoodsApprovedIndicator>
          <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
          <cbc:PowerIndicator>true</cbc:PowerIndicator>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
          </cac:MinimumTemperature>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:HazardousGoodsTransit>
            <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
            <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
            <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
            <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
            <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
            <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %.</cbc:TransitDescription>
            <cac:MaximumTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">35</cbc:Measure>
            </cac:MaximumTemperature>
            <cac:MinimumTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">5</cbc:Measure>
            </cac:MinimumTemperature>
          </cac:HazardousGoodsTransit>
          <cac:LoadedHazardousItem>
            <cbc:ID>SE-BAT-48100-DG</cbc:ID>
            <cbc:UNDGCode listID="UN Model Regulations UN number">3480</cbc:UNDGCode>
            <cbc:CategoryName>Miscellaneous dangerous goods</cbc:CategoryName>
            <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
            <cbc:UpperOrangeHazardPlacardID>90</cbc:UpperOrangeHazardPlacardID>
            <cbc:LowerOrangeHazardPlacardID>3480</cbc:LowerOrangeHazardPlacardID>
            <cbc:HazardClassID schemeID="UN Model Regulations hazard class">9</cbc:HazardClassID>
            <cbc:HazardousTypeCode listID="urn:ubl-examples:world:codelist:HazardousGoodsTypeCode">ARTICLE</cbc:HazardousTypeCode>
            <cbc:PackagingDangerLevelCode listID="UN/EDIFACT EDED 8339">4</cbc:PackagingDangerLevelCode>
            <cbc:GrossWeightMeasure unitCode="KGM">348</cbc:GrossWeightMeasure>
            <cbc:NetWeightMeasure unitCode="KGM">312</cbc:NetWeightMeasure>
            <cbc:NetVolumeMeasure unitCode="MTQ">0.24</cbc:NetVolumeMeasure>
            <cbc:Quantity unitCode="EA">6</cbc:Quantity>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Saltmere Engineering</cbc:Name>
              </cac:PartyName>
            </cac:ContactParty>
            <cac:HazardousGoodsTransit>
              <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
              <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
              <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
              <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
              <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
              <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %.</cbc:TransitDescription>
              <cac:MaximumTemperature>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
                <cbc:Measure unitCode="CEL">35</cbc:Measure>
              </cac:MaximumTemperature>
              <cac:MinimumTemperature>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
                <cbc:Measure unitCode="CEL">5</cbc:Measure>
              </cac:MinimumTemperature>
            </cac:HazardousGoodsTransit>
            <cac:EmergencyTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">EMERGENCY</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">60</cbc:Measure>
            </cac:EmergencyTemperature>
            <cac:AdditionalTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">STORAGE</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">20</cbc:Measure>
            </cac:AdditionalTemperature>
            <cac:PositionOnBoardStowage>
              <cbc:LocationID>MD-L2</cbc:LocationID>
              <cbc:Location>Main deck, accessible</cbc:Location>
            </cac:PositionOnBoardStowage>
            <cac:Package>
              <cbc:Quantity unitCode="EA">6</cbc:Quantity>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
            </cac:Package>
          </cac:LoadedHazardousItem>
        </cac:TransportEquipment>
        <cac:HazardousGoodsTransit>
          <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
          <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
          <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
          <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
          <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %.</cbc:TransitDescription>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
          </cac:MinimumTemperature>
        </cac:HazardousGoodsTransit>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">5</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">35</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:Package>
          <cbc:ID>SE-CR-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0001</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-2</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0002</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-3</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0003</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-4</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0004</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-5</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0005</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-6</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0006</cbc:TraceID>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
  </cac:Shipment>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentCopyTypeCode">ORIGINAL</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">PAPER</cbc:DistributionTypeCode>
    <cbc:DistributionType>With the goods</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41174</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Airport Cargo</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentCopyTypeCode">COPY</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONIC</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bayforth Forwarding</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>KAC-SIG-KAC-WB-26-0717</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelaro Air Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
