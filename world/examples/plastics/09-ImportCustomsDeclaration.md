# Import Customs Declaration: Rivermouth Packaging to Customs and Border Service of Bayvarra

*Example 9 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The packaging maker declares the import in Bayvarra.

[The XML file](09-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **PLASTICS-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **RP-IM-26-0893**  
  The importer's declaration number.
- `UUID` = **3ab58340-2ba7-5229-ab1a-e01715bcc1ef**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-22**  
  Declared when the barge arrives at the coast.
- `IssueTime` = **10:35:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `TypeCode` = **IMPORT** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode`)  
  An import declaration. The code is from the Trade Accord's customs declaration type list: IMPORT = Import declaration.
- `SubTypeCode` = **FREECIRC** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode`)  
  For release into free circulation. The code is from the Trade Accord's customs declaration subtype list: FREECIRC = Release for free circulation.
- `NatureOfTransactionCode` = **PURCHASE** (listID `urn:ubl-examples:world:codelist:NatureOfTransactionCode`)  
  The goods were bought. The code is from the Trade Accord's nature of transaction list: PURCHASE = Outright purchase or sale.
- `Note` = **No duty: goods of Accord origin. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.**  
  What is due at import, by the importing country's rule (D18).
- `VersionID` = **1**  
  The first version.

### Jurisdiction Region Address

Inside `JurisdictionRegionAddress`:

- `Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The customs territory of import. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:20274** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Rivermouth Packaging (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Rivermouth Packaging (world/parties.json).
- `PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Rivermouth Packaging (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Rivermouth Packaging (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered for state sales tax; identity of Rivermouth Packaging (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1238220** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Rivermouth Packaging (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
- `PartyLegalEntity/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered, with its legal form; identity of Rivermouth Packaging (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk desk: the desk for its role in this document (it deals with customs); identity of Rivermouth Packaging (world/parties.json).
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2440 2740**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Rivermouth Packaging (world/parties.json).
- `Contact/ElectronicMail` = **customs@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Rinova Recovery (world/parties.json).
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
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
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rivermouth Packaging**  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.

### Customs Party

Inside `CustomsParty`:

- `PartyIdentification/ID` = **20410137** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Customs and Border Service of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs and Border Service of Bayvarra**  
  The trading name; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-479100** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Border Crossing Road**  
  Street of the postal address. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/BuildingNumber` = **36**  
  Building number of the postal address. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/PostalZone` = **71213**  
  Postal code in Bayvarra's format (5 digits). identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Customs and Border Service of Bayvarra (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Customs and Border Service of Bayvarra**  
  The public body's official name; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Department` = **Customs**  
  The department the desk belongs to; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 337 137**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/ElectronicMail` = **import@customs-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410137** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs and Border Service of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **RR-SH-26-0889**  
  The shipment declared.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **99840.00** (currencyID `XBL`)  
  The customs value in lume: the invoice value in ferra at the world's reference rate (1 ferra = 0.01 lume).
- `GoodsItem/DeclaredStatisticsValueAmount` = **99840.00** (currencyID `XBL`)  
  The value for the trade statistics: the invoice value at the border.
- `GoodsItem/FreeOnBoardValueAmount` = **98046.00** (currencyID `XBL`)  
  The value at the loading quay: the CPT price less the river freight of 179,400 ferra, in lume.
- `GoodsItem/InsuranceValueAmount` = **0.00** (currencyID `XBL`)  
  The buyer did not insure the river carriage.
- `GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **P** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XU origin under the Trade Accord, by this criterion: the preference claimed, free of duty (D18). The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/RequiredCustomsID` = **3901.10.00**  
  The tariff code Bayvarra's customs requires on the declaration.
- `GoodsItem/CustomsStatusCode` = **FOREIGN** (listID `urn:ubl-examples:world:codelist:CustomsStatusCode`)  
  Bayvarra's customs status: goods from abroad, not yet released for free circulation. The code is from the Trade Accord's customs status list: FOREIGN = Not in free circulation.
- `GoodsItem/CustomsProcedureCode` = **1000** (listID `urn:ubl-examples:world:codelist:CustomsProcedureCode`)  
  Release for free circulation, with no previous procedure. The code is from the Trade Accord's customs procedure list: 1000 = Release for free circulation, no previous procedure.
- `GoodsItem/CustomsTariffQuantity` = **120000** (unitCode `KGM`)  
  The quantity in the tariff's unit: net kilograms.
- `GoodsItem/CustomsImportClassifiedIndicator` = **true**  
  Classified by the importer before arrival.
- `GoodsItem/Item/Description` = **Zhaldrek skalsir razkir mir huntaz drunvir, tidrek krirstul 0.94, trek sazdran nihan skul 1 zhurkaz.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/Name` = **Ranstan PE skalsir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/Name` = **Recycled PE granulate** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ID` = **RR-PE-R1**  
  The seller's own item number; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/StandardItemIdentification/ID` = **771030000048** (schemeID `urn:ubl-examples:world:item`)  
  The Codana item number of the maker, issued by the Codana Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a number of the world, not a GTIN; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item granulate-pe of Rinova Recovery (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **VII** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VII = Plastics and articles thereof; rubber and articles thereof.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **390110** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item granulate-pe of Rinova Recovery (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 390110 = Polyethylene having a specific gravity of less than 0.94, in primary forms.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **34710** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item granulate-pe of Rinova Recovery (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 34710 = Polymers of ethylene, in primary forms.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Density**  
  A measured property of the item.
- `GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **0.92** (unitCode `23`)  
  Its measured value; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Recycled content**  
  A measured property of the item.
- `GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **100** (unitCode `P1`)  
  Its measured value; item granulate-pe of Rinova Recovery (world/items.json).
- `GoodsItem/Item/EnvironmentalCertificate/ID` = **XU-RC-2026-007**  
  The number of the environmental certificate, unique only with its issuer, who is named with it (decision ID-Q10).
- `GoodsItem/Item/EnvironmentalCertificate/CertificateTypeCode` = **RECYCLED** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  The kind of claim, as a code. The code is from the Trade Accord's certificate type list: RECYCLED = Recycled content.
- `GoodsItem/Item/EnvironmentalCertificate/CertificateType` = **Recycled content**  
  The name of code RECYCLED in the Trade Accord's certificate type list.
- `GoodsItem/Item/EnvironmentalCertificate/Remarks` = **Made entirely from sorted production waste recovered in Urvania.**  
  What the certificate states.
- `GoodsItem/Item/EnvironmentalCertificate/IssuerParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/EnvironmentalCertificate/IssuerParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/BondedWarehouseLocation/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `GoodsItem/BondedWarehouseLocation/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state as a code of Bayvarra's national list. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `GoodsItem/BondedWarehouseLocation/LocationTypeCode` = **BONDEDSTORE** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs bonded store. The code is from the Trade Accord's customs location type list: BONDEDSTORE = Customs bonded store.
- `GoodsItem/BondedWarehouseLocation/Name` = **Bonded store at the river quay, Lumeport**  
  Where the bags wait until released.
- `GoodsItem/BondedWarehouseLocation/ValidityPeriod/StartDate` = **2025-01-01**  
  The store's licence runs
- `GoodsItem/BondedWarehouseLocation/ValidityPeriod/EndDate` = **2027-12-31**  
  until the end of 2027.
- `GoodsItem/BondedWarehouseLocation/Storage/ID` = **RQ-BOND-03**  
  Hall 3 of the bonded store.
- `GoodsItem/BondedWarehouseLocation/Storage/Name` = **Hall 3**  
  Its name.
- `GoodsItem/BondedWarehouseLocation/Storage/GateID` = **Gate B**  
  The gate the barge's bags go through.
- `GoodsItem/BondedWarehouseLocation/Storage/AirFlowPercent` = **0**  
  No forced ventilation.
- `GoodsItem/BondedWarehouseLocation/Storage/HumidityPercent` = **60**  
  The hall's humidity limit; granulate must stay dry.
- `GoodsItem/BondedWarehouseLocation/Storage/AnimalFoodApprovedIndicator` = **false**  
  Not approved for animal feed.
- `GoodsItem/BondedWarehouseLocation/Storage/HumanFoodApprovedIndicator` = **false**  
  Not approved for food.
- `GoodsItem/BondedWarehouseLocation/Storage/DangerousGoodsApprovedIndicator` = **false**  
  Not approved for dangerous goods.
- `GoodsItem/BondedWarehouseLocation/Storage/RefrigeratedIndicator` = **false**  
  Not refrigerated.
- `GoodsItem/BondedWarehouseLocation/Storage/PowerIndicator` = **true**  
  Power for the forklifts and lighting.
- `GoodsItem/BondedWarehouseLocation/Storage/MinimumTemperature/AttributeID` = **AMBIENT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The temperature of the hall. The code is from the Trade Accord's temperature attribute list: AMBIENT = Ambient temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/BondedWarehouseLocation/Storage/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  At least 5 °C.
- `GoodsItem/BondedWarehouseLocation/Storage/MinimumTemperature/Description` = **Kept frost-free.**  
  Why.
- `GoodsItem/BondedWarehouseLocation/Storage/MaximumTemperature/AttributeID` = **AMBIENT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The temperature of the hall. The code is from the Trade Accord's temperature attribute list: AMBIENT = Ambient temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/BondedWarehouseLocation/Storage/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  At most 35 °C.
- `GoodsItem/BondedWarehouseLocation/Storage/Certificate/ID` = **XB-BOND-LIC-0388** (schemeID `urn:ubl-examples:world:XB:bonded-warehouse`)  
  The bonded store's licence, by its number in the register of customs; the schemeID names the register and its authority (decision ID-Q10).
- `GoodsItem/BondedWarehouseLocation/Storage/Certificate/CertificateTypeCode` = **BONDEDSTORE** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A licence of customs. The code is from the Trade Accord's certificate type list: BONDEDSTORE = Bonded store licence.
- `GoodsItem/BondedWarehouseLocation/Storage/Certificate/CertificateType` = **Bonded store licence**  
  The name of code BONDEDSTORE in the Trade Accord's certificate type list.
- `GoodsItem/AdditionalDocumentReference/ID` = **FB-WB-26-0890**  
  The barge's consignment note.
- `GoodsItem/AdditionalDocumentReference/DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: FB-WB-26-0890 is the example plastics/06, a Waybill; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Waybill.
- `ShipmentStage/TransportModeCode` = **8** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by river (worklist C12). The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 8 = Inland water transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **RR-EX-26-0887**  
  The export declaration of the goods in the country of departure, for information.
- `DocumentTypeCode` = **ExportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: RR-EX-26-0887 is the example plastics/05, a ExportCustomsDeclaration; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: ExportCustomsDeclaration = Export Customs Declaration.
- `ID` = **RR-INV-26-0894**  
  The commercial invoice the customs value rests on (worklist C12); its statement on origin is the proof of origin the preference claim refers to (D18).
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: RR-INV-26-0894 is the example plastics/10, a Invoice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Invoice.

### Signature

Inside `Signature`:

- `ID` = **RP-SIG-IM-plastics**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Rivermouth Packaging**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PLASTICS-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>RP-IM-26-0893</cbc:ID>
  <cbc:UUID>3ab58340-2ba7-5229-ab1a-e01715bcc1ef</cbc:UUID>
  <cbc:IssueDate>2026-04-22</cbc:IssueDate>
  <cbc:IssueTime>10:35:00-01:00</cbc:IssueTime>
  <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode">IMPORT</cbc:TypeCode>
  <cbc:SubTypeCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode">FREECIRC</cbc:SubTypeCode>
  <cbc:NatureOfTransactionCode listID="urn:ubl-examples:world:codelist:NatureOfTransactionCode">PURCHASE</cbc:NatureOfTransactionCode>
  <cbc:Note>No duty: goods of Accord origin. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:JurisdictionRegionAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
    </cac:Country>
  </cac:JurisdictionRegionAddress>
  <cac:ImporterParty>
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
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
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
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
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
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 38 2440 2740</cbc:Telephone>
      <cbc:ElectronicMail>customs@rivermouth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
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
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rivermouth Packaging</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:CustomsParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410137</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Customs and Border Service of Bayvarra</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-479100</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Border Crossing Road</cbc:StreetName>
      <cbc:BuildingNumber>36</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71213</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Customs and Border Service of Bayvarra</cbc:RegistrationName>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 2 7121 337 137</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xb.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410137</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:CustomsParty>
  <cac:Shipment>
    <cbc:ID>RR-SH-26-0889</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Recycled PE granulate</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">99840.00</cbc:DeclaredCustomsValueAmount>
      <cbc:DeclaredStatisticsValueAmount currencyID="XBL">99840.00</cbc:DeclaredStatisticsValueAmount>
      <cbc:FreeOnBoardValueAmount currencyID="XBL">98046.00</cbc:FreeOnBoardValueAmount>
      <cbc:InsuranceValueAmount currencyID="XBL">0.00</cbc:InsuranceValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">P</cbc:PreferenceCriterionCode>
      <cbc:RequiredCustomsID>3901.10.00</cbc:RequiredCustomsID>
      <cbc:CustomsStatusCode listID="urn:ubl-examples:world:codelist:CustomsStatusCode">FOREIGN</cbc:CustomsStatusCode>
      <cbc:CustomsProcedureCode listID="urn:ubl-examples:world:codelist:CustomsProcedureCode">1000</cbc:CustomsProcedureCode>
      <cbc:CustomsTariffQuantity unitCode="KGM">120000</cbc:CustomsTariffQuantity>
      <cbc:CustomsImportClassifiedIndicator>true</cbc:CustomsImportClassifiedIndicator>
      <cac:Item>
        <cbc:Description languageID="qau">Zhaldrek skalsir razkir mir huntaz drunvir, tidrek krirstul 0.94, trek sazdran nihan skul 1 zhurkaz.</cbc:Description>
        <cbc:Description languageID="en-XB">Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.</cbc:Description>
        <cbc:Name languageID="qau">Ranstan PE skalsir</cbc:Name>
        <cbc:Name languageID="en-XB">Recycled PE granulate</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>RR-PE-R1</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">771030000048</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">VII</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">390110</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">34710</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Density</cbc:Name>
          <cbc:ValueQuantity unitCode="23">0.92</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Recycled content</cbc:Name>
          <cbc:ValueQuantity unitCode="P1">100</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:EnvironmentalCertificate>
          <cbc:ID>XU-RC-2026-007</cbc:ID>
          <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">RECYCLED</cbc:CertificateTypeCode>
          <cbc:CertificateType>Recycled content</cbc:CertificateType>
          <cbc:Remarks>Made entirely from sorted production waste recovered in Urvania.</cbc:Remarks>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:EnvironmentalCertificate>
      </cac:Item>
      <cac:BondedWarehouseLocation>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">BONDEDSTORE</cbc:LocationTypeCode>
        <cbc:Name>Bonded store at the river quay, Lumeport</cbc:Name>
        <cac:ValidityPeriod>
          <cbc:StartDate>2025-01-01</cbc:StartDate>
          <cbc:EndDate>2027-12-31</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:Storage>
          <cbc:ID>RQ-BOND-03</cbc:ID>
          <cbc:Name>Hall 3</cbc:Name>
          <cbc:GateID>Gate B</cbc:GateID>
          <cbc:AirFlowPercent>0</cbc:AirFlowPercent>
          <cbc:HumidityPercent>60</cbc:HumidityPercent>
          <cbc:AnimalFoodApprovedIndicator>false</cbc:AnimalFoodApprovedIndicator>
          <cbc:HumanFoodApprovedIndicator>false</cbc:HumanFoodApprovedIndicator>
          <cbc:DangerousGoodsApprovedIndicator>false</cbc:DangerousGoodsApprovedIndicator>
          <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
          <cbc:PowerIndicator>true</cbc:PowerIndicator>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">AMBIENT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
            <cbc:Description>Kept frost-free.</cbc:Description>
          </cac:MinimumTemperature>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">AMBIENT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:Certificate>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:bonded-warehouse">XB-BOND-LIC-0388</cbc:ID>
            <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">BONDEDSTORE</cbc:CertificateTypeCode>
            <cbc:CertificateType>Bonded store licence</cbc:CertificateType>
          </cac:Certificate>
        </cac:Storage>
      </cac:BondedWarehouseLocation>
      <cac:AdditionalDocumentReference>
        <cbc:ID>FB-WB-26-0890</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
      </cac:AdditionalDocumentReference>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">8</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>RR-EX-26-0887</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ExportCustomsDeclaration</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>RR-INV-26-0894</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>RP-SIG-IM-plastics</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ImportCustomsDeclaration>
```
