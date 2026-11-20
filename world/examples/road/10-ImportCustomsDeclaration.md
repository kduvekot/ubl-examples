# Import Customs Declaration: Lumeway Distribution to Customs and Border Service of Bayvarra

*Example 10 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The distributor, as importer, declares the goods in Bayvarra and claims the preferential duty rate with the certificate of origin.

[The XML file](10-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ID` = **LMW-IM-26-0127**  
  The importer's declaration number.
- `UUID` = **d05f73ca-d179-5742-b609-b8871aacb98b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-24**  
  Declared when the goods arrive in Bayvarra.
- `IssueTime` = **09:54:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `TypeCode` = **IMPORT** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode`)  
  An import declaration. The code is from the Trade Accord's customs declaration type list: IMPORT = Import declaration.
- `SubTypeCode` = **FREECIRC** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode`)  
  For release into free circulation. The code is from the Trade Accord's customs declaration subtype list: FREECIRC = Release for free circulation.
- `NatureOfTransactionCode` = **PURCHASE** (listID `urn:ubl-examples:world:codelist:NatureOfTransactionCode`)  
  The goods were bought. The code is from the Trade Accord's nature of transaction list: PURCHASE = Outright purchase or sale.
- `Note` = **No duty: goods of Accord origin. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.**  
  What is due at import, by the importing country's rule.
- `VersionID` = **1**  
  The first version.

### Jurisdiction Region Address

Inside `JurisdictionRegionAddress`:

- `Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The customs territory of import. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; as Lumeway Distribution gives it.
- `PartyTaxScheme/CompanyID` = **UL-1230822** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); as Lumeway Distribution gives it. The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
  The name under which the party is registered, with its legal form; as Lumeway Distribution gives it.
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **customs@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
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

- `PartyIdentification/ID` = **3071845926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Customs and Border Service of Bayvarra gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs and Border Service of Bayvarra**  
  The trading name; as Customs and Border Service of Bayvarra gives it.
- `PostalAddress/ID` = **UL-ADR-479100** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Customs and Border Service of Bayvarra gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Border Road**  
  Street of the postal address. As Customs and Border Service of Bayvarra gives it.
- `PostalAddress/BuildingNumber` = **36**  
  Building number of the postal address. As Customs and Border Service of Bayvarra gives it.
- `PostalAddress/CityName` = **Euridice Crossing**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Customs and Border Service of Bayvarra gives it.
- `PostalAddress/PostalZone` = **71950**  
  Postal code in Bayvarra's format (5 digits). As Customs and Border Service of Bayvarra gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Customs and Border Service of Bayvarra gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Customs and Border Service of Bayvarra**  
  The public body's official name; as Customs and Border Service of Bayvarra gives it.
- `PartyLegalEntity/CompanyID` = **3071845926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register ; as Customs and Border Service of Bayvarra gives it. The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); as Customs and Border Service of Bayvarra gives it.
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Customs and Border Service of Bayvarra gives it.
- `Contact/Department` = **Customs**  
  The department the desk belongs to; as Customs and Border Service of Bayvarra gives it.
- `Contact/Telephone` = **+999 2 7121 503 398**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Customs and Border Service of Bayvarra gives it.
- `Contact/ElectronicMail` = **import@customs-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Customs and Border Service of Bayvarra gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Customs and Border Service of Bayvarra gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:3071845926** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Customs and Border Service of Bayvarra gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **CAS-SH-26-1291**  
  The shipment of the despatch advice.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **38304.00** (currencyID `XBL`)  
  The customs value in lume, Bayvarra's currency: the invoice value in ferra at the world's reference rate (1 ferra = 0.01 lume).
- `GoodsItem/GrossWeightMeasure` = **5188.8** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **S** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XU origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: S = Sufficiently processed.
- `GoodsItem/Item/Description` = **Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries.
- `GoodsItem/Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `GoodsItem/Item/Name` = **Park bench Serra 180** (languageID `en-XB`)  
  The item's name in English, the working language between the countries.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `GoodsItem/DespatchLineReference/LineID` = **1**  
  The despatch advice line of these goods.
- `GoodsItem/DespatchLineReference/DocumentReference/ID` = **CAS-DA-26-1342**  
  The despatch advice.
- `GoodsItem/DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CAS-DA-26-1342 is the example road/04, a DespatchAdvice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `GoodsItem/ContainingPackage/Quantity` = **4** (unitCode `EA`)  
  4 benches to a pallet; the goods item travels on 24 pallets.
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The pallet goes back to the party that loaded it.
- `GoodsItem/ContainingPackage/PackageLevelCode` = **3** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 3: the outer level, the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 3 = Outer.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **570.00** (currencyID `XBL`)  
  The customs value in lume, Bayvarra's currency: the invoice value in ferra at the world's reference rate (1 ferra = 0.01 lume).
- `GoodsItem/GrossWeightMeasure` = **174.6** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **S** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XU origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: S = Sufficiently processed.
- `GoodsItem/Item/Description` = **Zudrir drir manskan gan drek Serra nanskir, zhukvan stezir gek, vazzhan stan krarhir-trunnir.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, ductile cast iron, galvanised and powder-coated.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries.
- `GoodsItem/Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `GoodsItem/Item/Name` = **Bench side frame casting** (languageID `en-XB`)  
  The item's name in English, the working language between the countries.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940199** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940199 = Parts of seats, other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38160** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38160 = Parts of furniture.
- `GoodsItem/DespatchLineReference/LineID` = **2**  
  The despatch advice line of these goods.
- `GoodsItem/DespatchLineReference/DocumentReference/ID` = **CAS-DA-26-1342**  
  The despatch advice.
- `GoodsItem/DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CAS-DA-26-1342 is the example road/04, a DespatchAdvice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `GoodsItem/ContainingPackage/Quantity` = **12** (unitCode `EA`)  
  12 side frames to a pallet; the goods item travels on 1 pallet.
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The pallet goes back to the party that loaded it.
- `GoodsItem/ContainingPackage/PackageLevelCode` = **3** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 3: the outer level, the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 3 = Outer.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `GoodsItem/ContainingPackage/ContainedPackage/Quantity` = **1** (unitCode `EA`)  
  One side frame in each carton.
- `GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The carton stays with the frame.
- `GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton, one side frame**  
  The carton in words; the goods item's frames travel one to a carton.
- `GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `ShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by road. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **FCC/CO/2026/0090**  
  The certificate of origin, to claim the preferential duty rate; the proof of origin the preference claim refers to.
- `DocumentTypeCode` = **CertificateOfOrigin** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: FCC/CO/2026/0090 is the example road/07, a CertificateOfOrigin; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: CertificateOfOrigin = Certificate Of Origin.
- `ID` = **7600008669**  
  The export declaration of the goods in the country of departure, for information.
- `DocumentTypeCode` = **ExportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 7600008669 is the example road/05, a ExportCustomsDeclaration; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ExportCustomsDeclaration = Export Customs Declaration.
- `ID` = **2026/1409**  
  The commercial invoice the customs value rests on.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 2026/1409 is the example road/15, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

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
  <cbc:ID>LMW-IM-26-0127</cbc:ID>
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
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
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
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">3071845926</cbc:ID>
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
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">3071845926</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 2 7121 503 398</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xb.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:3071845926</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:CustomsParty>
  <cac:Shipment>
    <cbc:ID>CAS-SH-26-1291</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">38304.00</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">5188.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">S</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.</cbc:Description>
        <cbc:Description languageID="en-XB">Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.</cbc:Description>
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
          <cbc:ID>CAS-DA-26-1342</cbc:ID>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
        </cac:DocumentReference>
      </cac:DespatchLineReference>
      <cac:ContainingPackage>
        <cbc:Quantity unitCode="EA">4</cbc:Quantity>
        <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">3</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        <cac:ContainedPackage>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
          <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
          <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">790</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">680</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">100</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:ContainedPackage>
        <cac:ContainedPackage>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
          <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
          <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">790</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">680</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">100</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="KGM">13</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:ContainedPackage>
        <cac:ContainedPackage>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
          <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
          <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">1810</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">295</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">100</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:ContainedPackage>
      </cac:ContainingPackage>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Bench side frame casting</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">570.00</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">174.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">S</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description languageID="qau">Zudrir drir manskan gan drek Serra nanskir, zhukvan stezir gek, vazzhan stan krarhir-trunnir.</cbc:Description>
        <cbc:Description languageID="en-XB">Replacement side frame for the Serra bench, ductile cast iron, galvanised and powder-coated.</cbc:Description>
        <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
        <cbc:Name languageID="en-XB">Bench side frame casting</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940199</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38160</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:DespatchLineReference>
        <cbc:LineID>2</cbc:LineID>
        <cac:DocumentReference>
          <cbc:ID>CAS-DA-26-1342</cbc:ID>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
        </cac:DocumentReference>
      </cac:DespatchLineReference>
      <cac:ContainingPackage>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
        <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">3</cbc:PackageLevelCode>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
        <cac:ContainedPackage>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
          <cbc:PackagingType>Frame carton, one side frame</cbc:PackagingType>
          <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
        </cac:ContainedPackage>
      </cac:ContainingPackage>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>FCC/CO/2026/0090</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">CertificateOfOrigin</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>7600008669</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ExportCustomsDeclaration</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>2026/1409</cbc:ID>
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
