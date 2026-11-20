# Import Customs Declaration: Quillmoor Pharma Distribution to Customs and Border Service of Bayvarra

*Example 8 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The wholesaler declares the generator for import at Lumeport airport on the Sunday evening it arrives: no duty on radioactive isotopes for medicine.

[The XML file](08-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **MEDICINES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **QPD-IM-26-0332**  
  The importer's declaration number.
- `UUID` = **dec43f2a-2397-55dd-a970-1f967ceff30c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-14**  
  The wholesaler declares the goods for import at Lumeport airport on the Sunday evening the generator arrived.
- `IssueTime` = **21:40:00-01:00**  
  When the wholesaler lodged the declaration: the generator landed at 20:15 on the scheduled flight from Amsterdam; the airport's customs office works around the clock; in the issuer's local time, with its offset from UTC (D27).
- `Note` = **No duty: goods made in the Netherlands, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in Bayvarra's tariff. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.**  
  What is due at import, by the importing country's rule (D18, O229): goods from outside the Accord claim no preference and pay the country's own tariff, which charges no duty on them.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Quillmoor Pharma Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Quillmoor Pharma Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-413425** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Quillmoor Pharma Distribution (world/parties.json).
- `PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-718264** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **40**  
  Building number of the postal address. identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Quillmoor Pharma Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Quillmoor Pharma Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Quillmoor Pharma Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1239476** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Quillmoor Pharma Distribution (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
  The name under which the party is registered, with its legal form; identity of Quillmoor Pharma Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Quillmoor Pharma Distribution (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customs@quillmoor.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 07:00–19:00**  
  When the desk can be reached; identity of Quillmoor Pharma Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20413425** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Quillmoor Pharma Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyName/Name` = **Haarvliet Isotopes**  
  The trading name; identity of Haarvliet Isotopes, a maker outside the world (world/parties.json, abroad; O229). It carries no identifier of a real register: a Dutch Chamber of Commerce number or VAT number in the real format could be someone's (O229); the documents identify it by its name and address, as a supplier outside the world.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/StreetName` = **Isotopenweg**  
  Street of the postal address. identity of Haarvliet Isotopes (world/parties.json, abroad): a fictional address in a real town.
- `PostalAddress/BuildingNumber` = **14**  
  Building number. identity of Haarvliet Isotopes (world/parties.json, abroad): a fictional address in a real town.
- `PostalAddress/CityName` = **Alkmaar**  
  The town. identity of Haarvliet Isotopes (world/parties.json, abroad): a fictional address in a real town.
- `PostalAddress/PostalZone` = **1812 RN**  
  Postal code in the format of Netherlands. identity of Haarvliet Isotopes (world/parties.json, abroad): a fictional address in a real town.
- `PostalAddress/TimezoneOffset` = **+02:00**  
  The offset from UTC of Central European Summer Time, the legal time there in June.
- `PostalAddress/Country/IdentificationCode` = **NL** (listID `ISO 3166`)  
  Netherlands, a real country outside the world (O229). The code is from the world's copy of UBL's Country identification (ISO 3166) list: NL = Netherlands (the).
- `PostalAddress/Country/Name` = **Netherlands**  
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
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Customs and Border Service of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
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
- `PartyLegalEntity/CompanyID` = **3071845926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register (O142); identity of Customs and Border Service of Bayvarra (world/parties.json). The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Department` = **Customs**  
  The department the desk belongs to; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 503 398**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/ElectronicMail` = **import@customs-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:3071845926** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Customs and Border Service of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **HI-SH-26-0333**  
  The maker's shipment, as its invoice numbers it.
- `Consignment/ID` = **HI-CS-26-0334**  
  The consignment declared, as the maker booked it.
- `Consignment/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight arriving.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Technetium-99m generator, 20 GBq**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **1200.00** (currencyID `XBL`)  
  The customs value in lume: Bayvarra values goods as they left the exporting country (D16), the maker's price at the lume's rate to the euro (O229).
- `GoodsItem/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **1** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.**  
  The seller's description; item tc-generator of Haarvliet Isotopes (world/items.json).
- `GoodsItem/Item/Name` = **Technetium-99m generator, 20 GBq**  
  The item's short name; item tc-generator of Haarvliet Isotopes (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **NL** (listID `ISO 3166`)  
  Where the item was produced; item tc-generator of Haarvliet Isotopes (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: NL = Netherlands (the).
- `GoodsItem/Item/CommodityClassification/NatureCode` = **VI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VI = Products of the chemical or allied industries.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **284443** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item tc-generator of Haarvliet Isotopes (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 284443 = Radioactive elements, isotopes and compounds; other alloys, dispersions (including cermets), ceramic products and mixtures containing these elements, isotopes or compounds.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **33690** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item tc-generator of Haarvliet Isotopes (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 33690 = Other radioactive elements and isotopes and compounds; alloys, dispersions, ceramic products and mixtures containing these elements, isotopes or compounds; radioactive residues.
- `GoodsItem/Item/HazardousItem/ID` = **HI-TCG-20-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the hazard label of the packages.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h**  
  What the shipper adds about handling.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2915** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2915 = Radioactive material, Type A package, non-special form, non fissile or fissile-excepted.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **163** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 163 = Radioactive Materials (Low to High Level Radiation).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, Type A package, non-special form, non fissile or fissile-excepted**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2915**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)**  
  The radionuclide and the maximum activity during transport, which the transport document must state in becquerels (IAEA SSR-6 para 546): UBL has no element for the activity of contents that are not fissile, so the name carries it, a finding for the TC (O202 choice 6). The activity is the generator's at acceptance at the Lumeport cargo terminal, the highest it has on the way, as Mo-99 decays (O202 choice 4); the A2 value of Mo-99 allows up to 600 GBq in a Type A package.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.**  
  The physical and chemical form: not special form, so the A2 value applies.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **1.5**  
  The transport index of the package: the highest dose rate at 1 m in mSv/h times 100, rounded up to the first decimal (IAEA SSR-6 para 523); above 1, so the package carries the Category III-YELLOW label (para 529, the higher category winning over the surface rate; O202 choice 1).
- `ShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by air (worklist C12). The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **HI-INV-26-0331**  
  The maker's commercial invoice the customs value rests on.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: HI-INV-26-0331 is the example medicines/07, a Invoice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Invoice.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MEDICINES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>QPD-IM-26-0332</cbc:ID>
  <cbc:UUID>dec43f2a-2397-55dd-a970-1f967ceff30c</cbc:UUID>
  <cbc:IssueDate>2026-06-14</cbc:IssueDate>
  <cbc:IssueTime>21:40:00-01:00</cbc:IssueTime>
  <cbc:Note>No duty: goods made in the Netherlands, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in Bayvarra's tariff. No tax is due at import: Bayvarra's sales tax is charged once, at the final retail sale.</cbc:Note>
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
      <cbc:Name>Haarvliet Isotopes</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:StreetName>Isotopenweg</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Alkmaar</cbc:CityName>
      <cbc:PostalZone>1812 RN</cbc:PostalZone>
      <cbc:TimezoneOffset>+02:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">NL</cbc:IdentificationCode>
        <cbc:Name>Netherlands</cbc:Name>
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
    <cbc:ID>HI-SH-26-0333</cbc:ID>
    <cac:Consignment>
      <cbc:ID>HI-CS-26-0334</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">18</cbc:GrossWeightMeasure>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Technetium-99m generator, 20 GBq</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">1200.00</cbc:DeclaredCustomsValueAmount>
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
          <cbc:ID>HI-TCG-20-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2915</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
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
      </cac:Item>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>HI-INV-26-0331</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
</ImportCustomsDeclaration>
```
