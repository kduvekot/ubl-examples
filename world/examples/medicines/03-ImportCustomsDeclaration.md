# Import Customs Declaration: Quillmoor Pharma Distribution to Customs and Border Service of Bayvarra

*Example 3 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The wholesaler declares the vaccines and the insulin for import at Lumeport airport: goods from outside the Accord under Bayvarra's own tariff, which charges no duty on medicines.

[The XML file](03-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ID` = **QLM-IM-26-0643**  
  The importer's declaration number.
- `UUID` = **288dda29-bba9-5aaa-b84e-c91eac5c3161**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-11**  
  The wholesaler declares the goods for import at Lumeport airport on the Monday morning after they arrived.
- `IssueTime` = **08:30:00-01:00**  
  When the wholesaler lodged the declaration: first thing on Monday; in the issuer's local time, with its offset from UTC.
- `Note` = **No duty: goods made in India, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in Bayvarra's tariff. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.**  
  What is due at import, by the importing country's rule: goods from outside the Accord claim no preference and pay the country's own tariff, which charges no duty on them.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Quillmoor Pharma Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-413425** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Quillmoor Pharma Distribution gives it.
- `PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; as Quillmoor Pharma Distribution gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
- `PartyTaxScheme/RegistrationName` = **Quillmoor Pharma Distribution Ltd**  
  The name under which the party is registered for state sales tax; as Quillmoor Pharma Distribution gives it.
- `PartyTaxScheme/CompanyID` = **CO-1239476** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); as Quillmoor Pharma Distribution gives it. The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
- `PartyLegalEntity/RegistrationName` = **Quillmoor Pharma Distribution Ltd**  
  The name under which the party is registered, with its legal form; as Quillmoor Pharma Distribution gives it.
- `PartyLegalEntity/CompanyID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Quillmoor Pharma Distribution gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Quillmoor Pharma Distribution gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Quillmoor Pharma Distribution gives it.
- `Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Quillmoor Pharma Distribution gives it.
- `Contact/ElectronicMail` = **customs@quillmoor.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Quillmoor Pharma Distribution gives it.
- `Contact/Note` = **Weekdays 07:00–19:00**  
  When the desk can be reached; as Quillmoor Pharma Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20413425** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyName/Name` = **Nilavar Biologics**  
  The trading name; as Nilavar Biologics, a maker outside the three countries, gives it. It carries no identifier of a real register: an Indian company number, GSTIN or importer-exporter code in the real format could be someone's; the documents identify it by its name and address, as a supplier outside the world.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/StreetName` = **Biotech Park Road**  
  Street of the postal address. As Nilavar Biologics gives it; the address is fictional, in a real town.
- `PostalAddress/BuildingNumber` = **27**  
  Building number. As Nilavar Biologics gives it; the address is fictional, in a real town.
- `PostalAddress/CityName` = **Hyderabad**  
  The town. As Nilavar Biologics gives it; the address is fictional, in a real town.
- `PostalAddress/PostalZone` = **500078**  
  Postal code in the format of India. As Nilavar Biologics gives it; the address is fictional, in a real town.
- `PostalAddress/CountrySubentity` = **Telangana**  
  The state of India, part of an address there. As Nilavar Biologics gives it; the address is fictional, in a real town.
- `PostalAddress/TimezoneOffset` = **+05:30**  
  The offset from UTC of Indian Standard Time, the legal time there in June.
- `PostalAddress/Country/IdentificationCode` = **IN** (listID `ISO 3166`)  
  India, a real country outside the world. The code is from the world's copy of UBL's Country identification (ISO 3166) list: IN = India.
- `PostalAddress/Country/Name` = **India**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Quillmoor Pharma Distribution**  
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

- `ID` = **NLB-SH-26-1786**  
  The maker's shipment, as its invoice numbers it.
- `Consignment/ID` = **NLB-CS-26-1786**  
  The consignment declared, as the maker booked it.
- `Consignment/GrossWeightMeasure` = **172.8** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight arriving.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **32620.20** (currencyID `XBL`)  
  The customs value in lume: Bayvarra values goods as they left the exporting country; the maker's price is carriage paid to Lumeport and shows no freight apart, so the price paid is the value, converted at the Lumeport Exchange's fixing of the day the declaration is lodged.
- `GoodsItem/GrossWeightMeasure` = **120** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **600** (unitCode `EA`)  
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
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **16548.78** (currencyID `XBL`)  
  The customs value in lume: Bayvarra values goods as they left the exporting country; the maker's price is carriage paid to Lumeport and shows no freight apart, so the price paid is the value, converted at the Lumeport Exchange's fixing of the day the declaration is lodged.
- `GoodsItem/GrossWeightMeasure` = **48** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **960** (unitCode `EA`)  
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
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Varicella vaccine, live, frozen, single dose**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **4535.00** (currencyID `XBL`)  
  The customs value in lume: Bayvarra values goods as they left the exporting country; the maker's price is carriage paid to Lumeport and shows no freight apart, so the price paid is the value, converted at the Lumeport Exchange's fixing of the day the declaration is lodged.
- `GoodsItem/GrossWeightMeasure` = **4.8** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **120** (unitCode `EA`)  
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
- `ShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by air. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **NLB-INV-26-1731**  
  The maker's commercial invoice the customs value rests on.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: NLB-INV-26-1731 is the example medicines/02, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ID>QLM-IM-26-0643</cbc:ID>
  <cbc:UUID>288dda29-bba9-5aaa-b84e-c91eac5c3161</cbc:UUID>
  <cbc:IssueDate>2026-05-11</cbc:IssueDate>
  <cbc:IssueTime>08:30:00-01:00</cbc:IssueTime>
  <cbc:Note>No duty: goods made in India, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in Bayvarra's tariff. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.</cbc:Note>
  <cac:ImporterParty>
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
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
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
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Quillmoor Pharma Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1239476</cbc:CompanyID>
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
      <cbc:RegistrationName>Quillmoor Pharma Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 38 6047 1582</cbc:Telephone>
      <cbc:ElectronicMail>customs@quillmoor.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:00–19:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20413425</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyName>
      <cbc:Name>Nilavar Biologics</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:StreetName>Biotech Park Road</cbc:StreetName>
      <cbc:BuildingNumber>27</cbc:BuildingNumber>
      <cbc:CityName>Hyderabad</cbc:CityName>
      <cbc:PostalZone>500078</cbc:PostalZone>
      <cbc:CountrySubentity>Telangana</cbc:CountrySubentity>
      <cbc:TimezoneOffset>+05:30</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">IN</cbc:IdentificationCode>
        <cbc:Name>India</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
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
    <cbc:ID>NLB-SH-26-1786</cbc:ID>
    <cac:Consignment>
      <cbc:ID>NLB-CS-26-1786</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">172.8</cbc:GrossWeightMeasure>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">32620.20</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">120</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">600</cbc:Quantity>
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
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">16548.78</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">48</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">960</cbc:Quantity>
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
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Varicella vaccine, live, frozen, single dose</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">4535.00</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">4.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">120</cbc:Quantity>
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
      </cac:Item>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>NLB-INV-26-1731</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
</ImportCustomsDeclaration>
```
