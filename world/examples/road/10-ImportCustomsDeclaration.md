# Import Customs Declaration: Lumeway Distribution to Customs and Border Service of Bayvarra

*Example 10 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The distributor, as importer, declares the goods in Bayvarra and claims the preferential duty rate with the certificate of origin.

[The XML file](10-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-IM-26-0161**  
  The importer's declaration number.
- `UUID` = **d05f73ca-d179-5742-b609-b8871aacb98b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-24**  
  Declared when the goods arrive in Bayvarra.
- `IssueTime` = **09:54:00-01:00**  
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

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
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
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
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
- `Contact/Name` = **Customs desk**  
  The party's customs desk desk: the desk for its role in this document (it deals with customs); identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customs@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Lumeway Distribution**  
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
- `PostalAddress/StreetName` = **Border Road**  
  Street of the postal address. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/BuildingNumber` = **36**  
  Building number of the postal address. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/CityName` = **Euridice Crossing**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `PostalAddress/PostalZone` = **71950**  
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

- `ID` = **CL-SH-26-0154**  
  The shipment of the despatch advice.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **47904.00** (currencyID `XBL`)  
  The customs value in lume, Bayvarra's currency: the invoice value in ferra at the world's reference rate (1 ferra = 0.01 lume).
- `GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **S** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XU origin under the Trade Accord, by this criterion: the preference claimed, free of duty (D18). The code is from the Trade Accord's preference criterion list: S = Sufficiently processed.
- `GoodsItem/Item/Description` = **Haz nanskir, 1800 mm, manskan skul stezir stan vazzhan nibir, bukdrek serskek kalnan, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/Name` = **Park bench Serra 180** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `GoodsItem/DespatchLineReference/LineID` = **1**  
  The despatch advice line of these goods.
- `GoodsItem/DespatchLineReference/DocumentReference/ID` = **CL-DA-26-0153**  
  The despatch advice.
- `GoodsItem/DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CL-DA-26-0153 is the example road/04, a DespatchAdvice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **717.60** (currencyID `XBL`)  
  The customs value in lume, Bayvarra's currency: the invoice value in ferra at the world's reference rate (1 ferra = 0.01 lume).
- `GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **S** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XU origin under the Trade Accord, by this criterion: the preference claimed, free of duty (D18). The code is from the Trade Accord's preference criterion list: S = Sufficiently processed.
- `GoodsItem/Item/Description` = **Zudrir drir manskan gan drek Serra nanskir, stezir nibir, vazzhan.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, cast steel, galvanised.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/Name` = **Bench side frame casting** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **732599** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 732599 = Other cast articles of iron or steel: other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **42999** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 42999 = Metal goods n.e.c..
- `GoodsItem/DespatchLineReference/LineID` = **2**  
  The despatch advice line of these goods.
- `GoodsItem/DespatchLineReference/DocumentReference/ID` = **CL-DA-26-0153**  
  The despatch advice.
- `GoodsItem/DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CL-DA-26-0153 is the example road/04, a DespatchAdvice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `ShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by road (worklist C12). The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **FCC-CO-26-0157**  
  The certificate of origin, to claim the preferential duty rate; the proof of origin the preference claim refers to (D18).
- `DocumentTypeCode` = **CertificateOfOrigin** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: FCC-CO-26-0157 is the example road/06, a CertificateOfOrigin; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: CertificateOfOrigin = Certificate Of Origin.
- `ID` = **VI-EX-26-0155**  
  The export declaration of the goods in the country of departure, for information.
- `DocumentTypeCode` = **ExportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: VI-EX-26-0155 is the example road/05, a ExportCustomsDeclaration; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: ExportCustomsDeclaration = Export Customs Declaration.
- `ID` = **VI-INV-26-0166**  
  The commercial invoice the customs value rests on (worklist C12).
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: VI-INV-26-0166 is the example road/15, a Invoice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Invoice.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-IM-road**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-IM-26-0161</cbc:ID>
  <cbc:UUID>d05f73ca-d179-5742-b609-b8871aacb98b</cbc:UUID>
  <cbc:IssueDate>2026-03-24</cbc:IssueDate>
  <cbc:IssueTime>09:54:00-01:00</cbc:IssueTime>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
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
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
      <cbc:ElectronicMail>customs@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
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
      <cbc:StreetName>Border Road</cbc:StreetName>
      <cbc:BuildingNumber>36</cbc:BuildingNumber>
      <cbc:CityName>Euridice Crossing</cbc:CityName>
      <cbc:PostalZone>71950</cbc:PostalZone>
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
    <cbc:ID>CL-SH-26-0154</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">47904.00</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">S</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul stezir stan vazzhan nibir, bukdrek serskek kalnan, gan zharsul krir drek tarkul.</cbc:Description>
        <cbc:Description languageID="en-XB">Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
        <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
        <cbc:Name languageID="en-XB">Park bench Serra 180</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:DespatchLineReference>
        <cbc:LineID>1</cbc:LineID>
        <cac:DocumentReference>
          <cbc:ID>CL-DA-26-0153</cbc:ID>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
        </cac:DocumentReference>
      </cac:DespatchLineReference>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Bench side frame casting</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">717.60</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">S</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description languageID="qau">Zudrir drir manskan gan drek Serra nanskir, stezir nibir, vazzhan.</cbc:Description>
        <cbc:Description languageID="en-XB">Replacement side frame for the Serra bench, cast steel, galvanised.</cbc:Description>
        <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
        <cbc:Name languageID="en-XB">Bench side frame casting</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">732599</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">42999</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:DespatchLineReference>
        <cbc:LineID>2</cbc:LineID>
        <cac:DocumentReference>
          <cbc:ID>CL-DA-26-0153</cbc:ID>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
        </cac:DocumentReference>
      </cac:DespatchLineReference>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>FCC-CO-26-0157</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">CertificateOfOrigin</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-EX-26-0155</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ExportCustomsDeclaration</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-INV-26-0166</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>LD-SIG-IM-road</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ImportCustomsDeclaration>
```
