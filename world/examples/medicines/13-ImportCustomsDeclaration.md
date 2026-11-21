# Import Customs Declaration: Tevaro Customs Brokers to Island Customs Service

*Example 13 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The customs broker, as the hospital's direct representative, declares the import at Selanu airport in the hospital's name: no duty on medicines, and the exemption from the import consumption tax for medicines supplied to a public hospital.

[The XML file](13-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-1361**  
  The collaboration this document belongs to: Tevaro's import declaration of the hospital's medicines at Selanu airport, to their release for free circulation. Tevaro Customs Brokers started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-1362**  
  The customs broker's number of the declaration.
- `UUID` = **8f2e6a5d-e54e-599b-97f3-65f0e0767e2a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-15**  
  The customs broker declares the import at Selanu airport once the goods are unloaded.
- `IssueTime` = **11:40:00+00:00**  
  After the terminal reported the arrival; in the issuer's local time, with its offset from UTC.
- `Note` = **Lelaha namafe: liape nalana tefata India tofami Netherlands, tanapu Accord, sekila lifanaha tofami hakasute nualo kifupa sahona piseki tipako mutaki namafe tefata selune mutaki Lisavu. Musaka mofilufo vukape: talapa, lifanaha tofami hatoki vahita vevisi paveli pateta.** (languageID `qal`)  
  The note in Lisavan, the sender's language: What is due at import, by the importing country's rule: goods from outside the Accord claim no preference and pay the country's own tariff, which charges no duty on them.
- `Note` = **No duty: goods made in India and the Netherlands, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in the tariff of Lisavu. Import consumption tax: exempt, medicines and vaccines supplied to a public hospital.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: What is due at import, by the importing country's rule: goods from outside the Accord claim no preference and pay the country's own tariff, which charges no duty on them.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Selanu General Hospital gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu General Hospital**  
  The trading name; as Selanu General Hospital gives it.
- `PostalAddress/ID` = **52968014** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu General Hospital gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu General Hospital gives it.
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu General Hospital gives it.
- `PostalAddress/BuildingNumber` = **81**  
  Building number of the postal address. As Selanu General Hospital gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu General Hospital gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu General Hospital gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `AgentParty/PartyIdentification/ID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AgentParty/PartyName/Name` = **Tevaro Customs Brokers**  
  A party referred to from another party's details: its identifier and name are enough.
- `PowerOfAttorney/ID` = **POA-TT-2026-031**  
  The number of the power of attorney the hospital gave its customs broker.
- `PowerOfAttorney/IssueDate` = **2026-01-06**  
  Given at the start of the year, for all of the year's imports.
- `PowerOfAttorney/Description` = **Lodging import declarations as direct representative, in the name and on behalf of Selanu General Hospital, and claiming its exemptions.**  
  What the broker may do: it declares in the hospital's name, which stays the importer.
- `PowerOfAttorney/AgentParty/PartyIdentification/ID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PowerOfAttorney/AgentParty/PartyName/Name` = **Tevaro Customs Brokers**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Quillmoor Pharma Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-413425** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Quillmoor Pharma Distribution gives it.
- `PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; as Quillmoor Pharma Distribution gives it.
- `PostalAddress/ID` = **LUM-ADR-718264** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Quillmoor Pharma Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. As Quillmoor Pharma Distribution gives it.
- `PostalAddress/BuildingNumber` = **40**  
  Building number of the postal address. As Quillmoor Pharma Distribution gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Quillmoor Pharma Distribution gives it.
- `PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). As Quillmoor Pharma Distribution gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Quillmoor Pharma Distribution gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu General Hospital**  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.

### Customs Party

Inside `CustomsParty`:

- `PartyIdentification/ID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Island Customs Service**  
  The trading name; as Island Customs Service gives it.
- `PostalAddress/ID` = **65334843** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Island Customs Service gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Island Customs Service gives it.
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Island Customs Service gives it.
- `PostalAddress/BuildingNumber` = **53**  
  Building number of the postal address. As Island Customs Service gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Island Customs Service**  
  The public body's official name; as Island Customs Service gives it.
- `PartyLegalEntity/CompanyID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  Number in the Government list of public bodies of Lisavu, which gives every public body a number of its own (GOV- and 3 digits), derived from no other register ; as Island Customs Service gives it. The schemeID names the scheme it is from: the government list of public bodies of Lisavu (GOV- and 3 digits).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); as Island Customs Service gives it.
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Island Customs Service gives it.
- `Contact/Department` = **Customs**  
  The department the desk belongs to; as Island Customs Service gives it.
- `Contact/Telephone` = **+999 3 728 6449**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Island Customs Service gives it.
- `Contact/ElectronicMail` = **import@customs-xl.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Island Customs Service gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Island Customs Service gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:GOV-118** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Notifier Party

Inside `NotifierParty`:

- `PartyIdentification/ID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Tevaro Customs Brokers gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tevaro Customs Brokers**  
  The trading name; as Tevaro Customs Brokers gives it.
- `Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: kopele.
- `PostalAddress/ID` = **24307810** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Tevaro Customs Brokers gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Tevaro Customs Brokers gives it.
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Tevaro Customs Brokers gives it.
- `PostalAddress/BuildingNumber` = **60**  
  Building number of the postal address. As Tevaro Customs Brokers gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Tevaro Customs Brokers gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Tevaro Customs Brokers gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Tevaro Customs Brokers Ltd**  
  The name under which the party is registered, with its legal form; as Tevaro Customs Brokers gives it.
- `PartyLegalEntity/CompanyID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Tevaro Customs Brokers gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Contact/Name` = **Declarations**  
  The party's main desk, which handles this document; as Tevaro Customs Brokers gives it.
- `Contact/JobTitle` = **Customs declarant**  
  The job of the person who answers at the desk; as Tevaro Customs Brokers gives it.
- `Contact/Department` = **Customs**  
  The department the desk belongs to; as Tevaro Customs Brokers gives it.
- `Contact/Telephone` = **+999 3 725 3563**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Tevaro Customs Brokers gives it.
- `Contact/ElectronicMail` = **declarations@tevaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Tevaro Customs Brokers gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Tevaro Customs Brokers gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41585** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Tevaro Customs Brokers gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **QLM-SH-26-3980**  
  The shipment declared.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **8640.000** (currencyID `XLC`)  
  The customs value in coral: Lisavu values the goods landed, the wholesaler's price carriage paid to Selanu airport, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **60** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **300** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **IN** (listID `ISO 3166`)  
  Where the item was produced; as Nilavar Biologics describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: IN = India.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **VI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VI = Products of the chemical or allied industries.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **300241** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Nilavar Biologics describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 300241 = Vaccines, toxins, cultures of micro-organisms (excluding yeasts) and similar products; for human medicine.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **35270** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Nilavar Biologics describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 35270 = Other pharmaceutical products.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Exempt from the island's import consumption tax. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **MEDHOSP** (listID `urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode`)  
  The exemption as a code of Lisavu's national list: medicines and vaccines supplied to a public hospital. The code is from Lisavu's national import consumption tax exemption reason list: MEDHOSP = Medicines and vaccines for a public hospital.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Lifanaha tofami hatoki kifupa paveli pateta** (languageID `qal`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In Lisavan, the sender's language.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Medicines and vaccines for a public hospital** (languageID `en-XL`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In English.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **2064.000** (currencyID `XLC`)  
  The customs value in coral: Lisavu values the goods landed, the wholesaler's price carriage paid to Selanu airport, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **12** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **240** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **IN** (listID `ISO 3166`)  
  Where the item was produced; as Nilavar Biologics describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: IN = India.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **VI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VI = Products of the chemical or allied industries.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **300431** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Nilavar Biologics describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 300431 = Medicaments; containing insulin, for therapeutic or prophylactic uses, packaged for retail sale.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **35260** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Nilavar Biologics describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 35260 = Medicaments, for therapeutic or prophylactic uses.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Exempt from the island's import consumption tax. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **MEDHOSP** (listID `urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode`)  
  The exemption as a code of Lisavu's national list: medicines and vaccines supplied to a public hospital. The code is from Lisavu's national import consumption tax exemption reason list: MEDHOSP = Medicines and vaccines for a public hospital.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Lifanaha tofami hatoki kifupa paveli pateta** (languageID `qal`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In Lisavan, the sender's language.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Medicines and vaccines for a public hospital** (languageID `en-XL`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In English.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Varicella vaccine, live, frozen, single dose**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **768.000** (currencyID `XLC`)  
  The customs value in coral: Lisavu values the goods landed, the wholesaler's price carriage paid to Selanu airport, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **1.6** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **40** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Varicella vaccine, live, frozen, single dose**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **IN** (listID `ISO 3166`)  
  Where the item was produced; as Nilavar Biologics describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: IN = India.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **VI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VI = Products of the chemical or allied industries.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **300241** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Nilavar Biologics describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 300241 = Vaccines, toxins, cultures of micro-organisms (excluding yeasts) and similar products; for human medicine.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **35270** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Nilavar Biologics describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 35270 = Other pharmaceutical products.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Exempt from the island's import consumption tax. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **MEDHOSP** (listID `urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode`)  
  The exemption as a code of Lisavu's national list: medicines and vaccines supplied to a public hospital. The code is from Lisavu's national import consumption tax exemption reason list: MEDHOSP = Medicines and vaccines for a public hospital.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Lifanaha tofami hatoki kifupa paveli pateta** (languageID `qal`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In Lisavan, the sender's language.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Medicines and vaccines for a public hospital** (languageID `en-XL`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In English.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `GoodsItem/ID` = **4**  
  The goods item number.
- `GoodsItem/Description` = **Technetium-99m generator, 20 GBq**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **580.000** (currencyID `XLC`)  
  The customs value in coral: Lisavu values the goods landed, the wholesaler's price carriage paid to Selanu airport, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **1** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Technetium-99m generator, 20 GBq**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **NL** (listID `ISO 3166`)  
  Where the item was produced; as Haarvliet Isotopes describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: NL = Netherlands (the).
- `GoodsItem/Item/CommodityClassification/NatureCode` = **VI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VI = Products of the chemical or allied industries.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **284443** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Haarvliet Isotopes describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 284443 = Radioactive elements, isotopes and compounds; other alloys, dispersions (including cermets), ceramic products and mixtures containing these elements, isotopes or compounds.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **33690** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Haarvliet Isotopes describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 33690 = Other radioactive elements and isotopes and compounds; alloys, dispersions, ceramic products and mixtures containing these elements, isotopes or compounds; radioactive residues.
- `GoodsItem/Item/HazardousItem/ID` = **HVI-TCG-20-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the hazard label of the packages.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h**  
  What the shipper adds about handling.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2915** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2915 = Radioactive material, Type A package, non-special form, non fissile or fissile-excepted.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for gases, lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **Lelaha palavo molasu maloli** (languageID `qal`)  
  The name of code NA in the Trade Accord's packing group list. In Lisavan, the sender's language.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned** (languageID `en-XL`)  
  The name of code NA in the Trade Accord's packing group list. In English.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **163** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 163 = Radioactive Materials (Low to High Level Radiation).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, Type A package, non-special form, non fissile or fissile-excepted**  
  The proper shipping name of the UN entry, as the Dangerous Goods List gives it for that UN number and class.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2915**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)**  
  The radionuclide and the maximum activity during transport, which the transport document must state in becquerels (IAEA SSR-6 para 546): UBL has no element for the activity of contents that are not fissile, so the name carries it. The activity is the generator's at acceptance at the Lumeport cargo terminal, the highest it has on the way, as Mo-99 decays; the A2 value of Mo-99 allows up to 600 GBq in a Type A package.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.**  
  The physical and chemical form: not special form, so the A2 value applies.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **1.5**  
  The transport index of the package: the highest dose rate at 1 m in mSv/h times 100, rounded up to the first decimal (IAEA SSR-6 para 523); above 1, so the package carries the Category III-YELLOW label (para 529, the higher category winning over the surface rate).
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Exempt from the island's import consumption tax. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **MEDHOSP** (listID `urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode`)  
  The exemption as a code of Lisavu's national list: medicines and vaccines supplied to a public hospital. The code is from Lisavu's national import consumption tax exemption reason list: MEDHOSP = Medicines and vaccines for a public hospital.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Lifanaha tofami hatoki kifupa paveli pateta** (languageID `qal`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In Lisavan, the sender's language.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxExemptionReason` = **Medicines and vaccines for a public hospital** (languageID `en-XL`)  
  The name of code MEDHOSP in Lisavu's national import consumption tax exemption reason list. In English.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `ShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by air. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **KXL-00698121**  
  The air waybill of the goods.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: KXL-00698121 is the example medicines/11, a Waybill; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Waybill.
- `ID` = **QLM-INV-26-4080**  
  The commercial invoice the customs value rests on.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: QLM-INV-26-4080 is the example medicines/14, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-1361</cbc:ProfileExecutionID>
  <cbc:ID>26-1362</cbc:ID>
  <cbc:UUID>8f2e6a5d-e54e-599b-97f3-65f0e0767e2a</cbc:UUID>
  <cbc:IssueDate>2026-06-15</cbc:IssueDate>
  <cbc:IssueTime>11:40:00+00:00</cbc:IssueTime>
  <cbc:Note languageID="qal">Lelaha namafe: liape nalana tefata India tofami Netherlands, tanapu Accord, sekila lifanaha tofami hakasute nualo kifupa sahona piseki tipako mutaki namafe tefata selune mutaki Lisavu. Musaka mofilufo vukape: talapa, lifanaha tofami hatoki vahita vevisi paveli pateta.</cbc:Note>
  <cbc:Note languageID="en-XL">No duty: goods made in India and the Netherlands, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in the tariff of Lisavu. Import consumption tax: exempt, medicines and vaccines supplied to a public hospital.</cbc:Note>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu General Hospital</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">52968014</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>81</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:AgentParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41585</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tevaro Customs Brokers</cbc:Name>
      </cac:PartyName>
    </cac:AgentParty>
    <cac:PowerOfAttorney>
      <cbc:ID>POA-TT-2026-031</cbc:ID>
      <cbc:IssueDate>2026-01-06</cbc:IssueDate>
      <cbc:Description>Lodging import declarations as direct representative, in the name and on behalf of Selanu General Hospital, and claiming its exemptions.</cbc:Description>
      <cac:AgentParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41585</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Tevaro Customs Brokers</cbc:Name>
        </cac:PartyName>
      </cac:AgentParty>
    </cac:PowerOfAttorney>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9524910900003</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-413425</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-718264</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Airport Road</cbc:StreetName>
      <cbc:BuildingNumber>40</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38528</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu General Hospital</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:CustomsParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-118</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Island Customs Service</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">65334843</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>53</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Island Customs Service</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-118</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 3 728 6449</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xl.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-118</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:CustomsParty>
  <cac:NotifierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41585</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tevaro Customs Brokers</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">24307810</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>60</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Tevaro Customs Brokers Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41585</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Declarations</cbc:Name>
      <cbc:JobTitle>Customs declarant</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 3 725 3563</cbc:Telephone>
      <cbc:ElectronicMail>declarations@tevaro.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41585</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:NotifierParty>
  <cac:Shipment>
    <cbc:ID>QLM-SH-26-3980</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">8640.000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">60</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">300</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.</cbc:Description>
        <cbc:Name>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">IN</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">VI</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">300241</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35270</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode">MEDHOSP</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason languageID="qal">Lifanaha tofami hatoki kifupa paveli pateta</cbc:TaxExemptionReason>
          <cbc:TaxExemptionReason languageID="en-XL">Medicines and vaccines for a public hospital</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">2064.000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">12</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.</cbc:Description>
        <cbc:Name>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">IN</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">VI</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">300431</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35260</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode">MEDHOSP</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason languageID="qal">Lifanaha tofami hatoki kifupa paveli pateta</cbc:TaxExemptionReason>
          <cbc:TaxExemptionReason languageID="en-XL">Medicines and vaccines for a public hospital</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Varicella vaccine, live, frozen, single dose</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">768.000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">1.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">40</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.</cbc:Description>
        <cbc:Name>Varicella vaccine, live, frozen, single dose</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">IN</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">VI</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">300241</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35270</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode">MEDHOSP</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason languageID="qal">Lifanaha tofami hatoki kifupa paveli pateta</cbc:TaxExemptionReason>
          <cbc:TaxExemptionReason languageID="en-XL">Medicines and vaccines for a public hospital</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>4</cbc:ID>
      <cbc:Description>Technetium-99m generator, 20 GBq</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">580.000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">18</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cac:Item>
        <cbc:Description>A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.</cbc:Description>
        <cbc:Name>Technetium-99m generator, 20 GBq</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">NL</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">VI</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">284443</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">33690</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>HVI-TCG-20-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2915</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup languageID="qal">Lelaha palavo molasu maloli</cbc:UNPackingGroup>
          <cbc:UNPackingGroup languageID="en-XL">No packing group assigned</cbc:UNPackingGroup>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">163</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, Type A package, non-special form, non fissile or fissile-excepted</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2915</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
          <cac:RadioactiveMaterial>
            <cbc:Name>Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)</cbc:Name>
            <cbc:SpecialFormDescription>Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.</cbc:SpecialFormDescription>
            <cbc:TransportIndexNumeric>1.5</cbc:TransportIndexNumeric>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XL:codelist:TaxExemptionReasonCode">MEDHOSP</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason languageID="qal">Lifanaha tofami hatoki kifupa paveli pateta</cbc:TaxExemptionReason>
          <cbc:TaxExemptionReason languageID="en-XL">Medicines and vaccines for a public hospital</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
      </cac:Item>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>KXL-00698121</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>QLM-INV-26-4080</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
</ImportCustomsDeclaration>
```
