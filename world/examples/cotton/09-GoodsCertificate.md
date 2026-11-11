# Goods Certificate: Selanu Chamber of Commerce to Selanu Cotton Ginnery

*Example 9 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Goods Certificate in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GOODS-CERTIFICATE-SCHEMA)*

The island's chamber of commerce certifies the bales for export, at the ginnery's application.

[The XML file](09-GoodsCertificate.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:cotton**  
  The business process the document belongs to: the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)".
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SCC-GC-26-0201**  
  The chamber's certificate number.
- `UUID` = **9d4c84eb-3f06-549a-83fe-14010b43c0bb**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-28**  
  Issued before shipment, at the ginnery's application.
- `IssueTime` = **11:39:00**  
  The time the sender's system issued the document, in the sender's local time.
- `TypeCode` = **PHYTO** (listID `urn:ubl-examples:world:codelist:GoodsCertificateTypeCode`)  
  A plant health certificate for the cotton. The code is from the Trade Accord's goods certificate type list: PHYTO = Phytosanitary certificate.
- `Description` = **The ginned cotton is free of the pests named by Bayvarra's plant health rules.**  
  What it certifies.
- `Note` = **Helatasa momai kelalahu filumuve.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): Where.
- `Note` = **Inspected at the ginnery's warehouse.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: Where.
- `VersionID` = **1**  
  The first version.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-02-28**  
  From the inspection.
- `EndDate` = **2026-03-14**  
  For two weeks: the bales must ship by then.

### Applicable Territory Address

Inside `ApplicableTerritoryAddress`:

- `Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  For import into Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Exporter Party

Inside `ExporterParty`:

- `WebsiteURI` = **https://www.selanuginnery.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Cotton Ginnery (world/parties.json).
- `IndustryClassificationCode` = **0163** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Cotton Ginnery (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 0163 = Post-harvest crop activities.
- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Selanu Cotton Ginnery (world/parties.json).
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Cotton Ginnery (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42681**  
  Number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Cotton Ginnery (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 22 persons and its turnover of 3660000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Cotton Ginnery (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Cotton sales**  
  The desk that handles this document; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Telephone` = **+999 3 721 2681**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/ElectronicMail` = **cotton@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Cotton Ginnery (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `WebsiteURI` = **https://www.lumeporttextile.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeport Textile Mill (world/parties.json).
- `IndustryClassificationCode` = **1312** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Textile Mill (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 1312 = Weaving of textiles.
- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-412603** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Textile Mill (world/parties.json).
- `PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; identity of Lumeport Textile Mill (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Textile Mill (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Textile Mill (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeport Textile Mill Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeport Textile Mill (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1237809**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeport Textile Mill (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Lumeport Textile Mill Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeport Textile Mill (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412603**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Lumeport Textile Mill (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 42 persons and its turnover of 4140000.00 XBL in 2025, by the Trade Accord's limits; identity of Lumeport Textile Mill (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Lumeport Textile Mill (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeport Textile Mill (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeport Textile Mill (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2303 2603**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Textile Mill (world/parties.json).
- `Contact/ElectronicMail` = **purchasing@lumeporttextile.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Textile Mill (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Textile Mill (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Textile Mill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Warehouse Party

Inside `WarehouseParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Party

Inside `IssuerParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Chamber of Commerce (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 9411 = Activities of business and employers membership organizations.
- `PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Chamber of Commerce**  
  The trading name; identity of Selanu Chamber of Commerce (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/BuildingNumber` = **30**  
  Building number of the postal address. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Selanu Chamber of Commerce (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42133**  
  Number in the Island companies register; identity of Selanu Chamber of Commerce (world/parties.json).
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
- `Contact/Name` = **Carnet office**  
  The desk that handles this document; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Telephone` = **+999 3 723 2133**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/ElectronicMail` = **carnet@chamber-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Chamber of Commerce (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42133** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Legal Authority Party

Inside `LegalAuthorityParty`:

- `PartyIdentification/ID` = **IC41448** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Island Customs Service**  
  A party referred to from another party's details: its identifier and name are enough.

### Applicant Party

Inside `ApplicantParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SCG-SH-26-0199**  
  The shipment certified.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Cotton lint, compressed bale**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **6055.452** (currencyID `XLC`)  
  The value of the bales, in coral.
- `GoodsItem/GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **6129** (unitCode `KGM`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.**  
  The seller's description; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `GoodsItem/Item/PackSizeNumeric` = **227**  
  The units in one pack: 227 kg in a bale; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/Name` = **Tekapa suhema, lafatite senehu** (languageID `qal`)  
  The item's name in Lisavan, the seller's language; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/Name` = **Cotton lint, compressed bale** (languageID `en-XL`)  
  The item's name in English, the working language between the countries; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ID` = **SCG-LINT**  
  The seller's own item number; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/StandardItemIdentification/ID` = **773020000137** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Where the item was produced; item cotton-bale of Selanu Cotton Ginnery (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **XI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XI = Textiles and textile articles.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item cotton-bale of Selanu Cotton Ginnery (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item cotton-bale of Selanu Cotton Ginnery (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01921 = Cotton, whether or not ginned.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Grade**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **Middling**  
  Its value; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Staple length**  
  A measured property of the item.
- `GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **28.6** (unitCode `MMT`)  
  Its measured value; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `GoodsItem/Item/OriginAddress/Region` = **North coast**  
  Where on the island the cotton was grown.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/Item/Certificate/ID` = **XL-CLS-2026-0042**  
  The number of the certificate.
- `GoodsItem/Item/Certificate/CertificateTypeCode` = **COTTONCLASS** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  The kind of certificate, as a code. The code is from the Trade Accord's certificate type list: COTTONCLASS = Cotton classing.
- `GoodsItem/Item/Certificate/CertificateType` = **Tekapa vekona** (languageID `qal`)  
  The name of code COTTONCLASS in the Trade Accord's certificate type list. In Lisavan, the sender's language.
- `GoodsItem/Item/Certificate/CertificateType` = **Cotton classing** (languageID `en-XL`)  
  The name of code COTTONCLASS in the Trade Accord's certificate type list. In English.
- `GoodsItem/Item/Certificate/Remarks` = **Grade Middling, staple 1-1/8 inch, micronaire 4.2.**  
  What the certificate states about the goods.
- `GoodsItem/Item/Certificate/IssuerParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/Certificate/IssuerParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/Certificate/Signature/ID` = **SCC-SIG-2026-0042**  
  The signature's identifier.
- `GoodsItem/Item/Certificate/Signature/Note` = **Signed by the cotton classer of the chamber.**  
  Who signed.
- `GoodsItem/Item/Certificate/Signature/ValidationDate` = **2026-02-20**  
  The day the signature was placed.
- `GoodsItem/Item/Certificate/Signature/SignatoryParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/Certificate/Signature/SignatoryParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

### Attestation

Inside `Attestation`:

- `ID` = **SCC-ATT-26-0042**  
  The inspector's attestation.
- `Name` = **Freedom from pests**  
  What is attested.
- `Description` = **Sampled and found free of boll weevil and pink bollworm.**  
  In words.
- `Note` = **10 bales sampled out of 80.**  
  The sample.
- `AcceptanceIndicator` = **true**  
  Accepted.
- `ValidityPeriod/EndDate` = **2026-03-14**  
  As the certificate.
- `IssuerParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuerParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `AttestationLine/ID` = **1**  
  The pest checked.
- `AttestationLine/TypeCode` = **PEST** (listID `urn:ubl-examples:world:codelist:AttestationTypeCode`)  
  A pest check. The code is from the Trade Accord's attestation type list: PEST = Pest check.
- `AttestationLine/Description` = **Boll weevil: none found.**  
  The finding.
- `AttestationLine/CriterionItem/ID` = **XB-PH-07**  
  Bayvarra's rule.
- `AttestationLine/CriterionItem/CriterionDescription` = **No live insects in a sample of 10 bales.**  
  The criterion.
- `AttestationLine/CriterionItem/DeclaredPropertyItem/Name` = **Cotton lint, compressed bale**  
  The goods it is about.
- `AttestationLine/SubAttestationLine/ID` = **1.1**  
  The second pest.
- `AttestationLine/SubAttestationLine/Description` = **Pink bollworm: none found.**  
  The finding.

### Goods Processing

Inside `GoodsProcessing`:

- `ID` = **SCG-PROC-26**  
  The processing on the island.
- `TypeCode` = **GINNING** (listID `urn:ubl-examples:world:codelist:GoodsProcessingTypeCode`)  
  The cotton was ginned. The code is from the Trade Accord's goods processing type list: GINNING = Ginning.
- `Description` = **Ginned, cleaned and pressed into bales.**  
  In words.
- `Note` = **At the Selanu cotton ginnery.**  
  Where.
- `Period/StartDate` = **2026-02-07**  
  The ginning.
- `Period/EndDate` = **2026-02-22**  
  Its end.
- `ProcessingParty/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ProcessingParty/PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.
- `CriterionItem/TypeCode` = **PROCESSING** (listID `urn:ubl-examples:world:codelist:GoodsProcessingTypeCode`)  
  A criterion on how the goods were processed. The code is from the Trade Accord's goods processing type list: PROCESSING = Processing.
- `CriterionItem/CriterionDescription` = **Seed removed; lint only.**  
  What processing the rule requires.
- `CriterionItem/DeclaredPropertyItem/Name` = **Cotton lint**  
  The goods.
- `SubGoodsProcessing/TypeCode` = **PRESSING** (listID `urn:ubl-examples:world:codelist:GoodsProcessingTypeCode`)  
  Pressed into bales. The code is from the Trade Accord's goods processing type list: PRESSING = Pressing.
- `SubGoodsProcessing/Description` = **Bales of about 227 kg.**  
  In words.

### Original Document Reference

Inside `OriginalDocumentReference`:

- `ID` = **XL-CLS-2026-0042**  
  The classing certificate of the cotton.

### Previous Document Reference

Inside `PreviousDocumentReference`:

- `ID` = **SCC-PH-25-0198**  
  Last season's certificate.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **LTM-PO-26-0197**  
  The mill's order.

### Signature

Inside `Signature`:

- `ID` = **SCC-SIG-26-PH**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GoodsCertificate xmlns="urn:oasis:names:specification:ubl:schema:xsd:GoodsCertificate-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:cotton</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SCC-GC-26-0201</cbc:ID>
  <cbc:UUID>9d4c84eb-3f06-549a-83fe-14010b43c0bb</cbc:UUID>
  <cbc:IssueDate>2026-02-28</cbc:IssueDate>
  <cbc:IssueTime>11:39:00</cbc:IssueTime>
  <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsCertificateTypeCode">PHYTO</cbc:TypeCode>
  <cbc:Description>The ginned cotton is free of the pests named by Bayvarra's plant health rules.</cbc:Description>
  <cbc:Note languageID="qal">Helatasa momai kelalahu filumuve.</cbc:Note>
  <cbc:Note languageID="en-XL">Inspected at the ginnery's warehouse.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-02-28</cbc:StartDate>
    <cbc:EndDate>2026-03-14</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ApplicableTerritoryAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
    </cac:Country>
  </cac:ApplicableTerritoryAddress>
  <cac:ExporterParty>
    <cbc:WebsiteURI>https://www.selanuginnery.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">0163</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-042681</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
      <cbc:BuildingNumber>42</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Selanu Cotton Ginnery Ltd</cbc:RegistrationName>
      <cbc:CompanyID>IC42681</cbc:CompanyID>
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
      <cbc:Name>Cotton sales</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 3 721 2681</cbc:Telephone>
      <cbc:ElectronicMail>cotton@selanuginnery.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:ImporterParty>
    <cbc:WebsiteURI>https://www.lumeporttextile.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">1312</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412603</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Mill Street</cbc:StreetName>
      <cbc:BuildingNumber>21</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38504</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeport Textile Mill Ltd</cbc:RegistrationName>
      <cbc:CompanyID>CO-1237809</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
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
      <cbc:RegistrationName>Lumeport Textile Mill Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20412603</cbc:CompanyID>
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
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 38 2303 2603</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@lumeporttextile.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:WarehouseParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:WarehouseParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
  </cac:FreightForwarderParty>
  <cac:IssuerParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>30</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Selanu Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID>IC42133</cbc:CompanyID>
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
      <cbc:Name>Carnet office</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 3 723 2133</cbc:Telephone>
      <cbc:ElectronicMail>carnet@chamber-selanu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42133</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:IssuerParty>
  <cac:LegalAuthorityParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41448</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Island Customs Service</cbc:Name>
    </cac:PartyName>
  </cac:LegalAuthorityParty>
  <cac:ApplicantParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:ApplicantParty>
  <cac:Shipment>
    <cbc:ID>SCG-SH-26-0199</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Cotton lint, compressed bale</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">6055.452</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">6190.29</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="KGM">6129</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.</cbc:Description>
        <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
        <cbc:PackSizeNumeric>227</cbc:PackSizeNumeric>
        <cbc:Name languageID="qal">Tekapa suhema, lafatite senehu</cbc:Name>
        <cbc:Name languageID="en-XL">Cotton lint, compressed bale</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>SCG-LINT</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">773020000137</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">XI</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">520100</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01921</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grade</cbc:Name>
          <cbc:Value>Middling</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Staple length</cbc:Name>
          <cbc:ValueQuantity unitCode="MMT">28.6</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:OriginAddress>
          <cbc:Region>North coast</cbc:Region>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
        <cac:Certificate>
          <cbc:ID>XL-CLS-2026-0042</cbc:ID>
          <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">COTTONCLASS</cbc:CertificateTypeCode>
          <cbc:CertificateType languageID="qal">Tekapa vekona</cbc:CertificateType>
          <cbc:CertificateType languageID="en-XL">Cotton classing</cbc:CertificateType>
          <cbc:Remarks>Grade Middling, staple 1-1/8 inch, micronaire 4.2.</cbc:Remarks>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
          <cac:Signature>
            <cbc:ID>SCC-SIG-2026-0042</cbc:ID>
            <cbc:Note>Signed by the cotton classer of the chamber.</cbc:Note>
            <cbc:ValidationDate>2026-02-20</cbc:ValidationDate>
            <cac:SignatoryParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
              </cac:PartyName>
            </cac:SignatoryParty>
          </cac:Signature>
        </cac:Certificate>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:Attestation>
    <cbc:ID>SCC-ATT-26-0042</cbc:ID>
    <cbc:Name>Freedom from pests</cbc:Name>
    <cbc:Description>Sampled and found free of boll weevil and pink bollworm.</cbc:Description>
    <cbc:Note>10 bales sampled out of 80.</cbc:Note>
    <cbc:AcceptanceIndicator>true</cbc:AcceptanceIndicator>
    <cac:ValidityPeriod>
      <cbc:EndDate>2026-03-14</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:AttestationLine>
      <cbc:ID>1</cbc:ID>
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:AttestationTypeCode">PEST</cbc:TypeCode>
      <cbc:Description>Boll weevil: none found.</cbc:Description>
      <cac:CriterionItem>
        <cbc:ID>XB-PH-07</cbc:ID>
        <cbc:CriterionDescription>No live insects in a sample of 10 bales.</cbc:CriterionDescription>
        <cac:DeclaredPropertyItem>
          <cbc:Name>Cotton lint, compressed bale</cbc:Name>
        </cac:DeclaredPropertyItem>
      </cac:CriterionItem>
      <cac:SubAttestationLine>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Description>Pink bollworm: none found.</cbc:Description>
      </cac:SubAttestationLine>
    </cac:AttestationLine>
  </cac:Attestation>
  <cac:GoodsProcessing>
    <cbc:ID>SCG-PROC-26</cbc:ID>
    <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsProcessingTypeCode">GINNING</cbc:TypeCode>
    <cbc:Description>Ginned, cleaned and pressed into bales.</cbc:Description>
    <cbc:Note>At the Selanu cotton ginnery.</cbc:Note>
    <cac:Period>
      <cbc:StartDate>2026-02-07</cbc:StartDate>
      <cbc:EndDate>2026-02-22</cbc:EndDate>
    </cac:Period>
    <cac:ProcessingParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:ProcessingParty>
    <cac:CriterionItem>
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsProcessingTypeCode">PROCESSING</cbc:TypeCode>
      <cbc:CriterionDescription>Seed removed; lint only.</cbc:CriterionDescription>
      <cac:DeclaredPropertyItem>
        <cbc:Name>Cotton lint</cbc:Name>
      </cac:DeclaredPropertyItem>
    </cac:CriterionItem>
    <cac:SubGoodsProcessing>
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsProcessingTypeCode">PRESSING</cbc:TypeCode>
      <cbc:Description>Bales of about 227 kg.</cbc:Description>
    </cac:SubGoodsProcessing>
  </cac:GoodsProcessing>
  <cac:OriginalDocumentReference>
    <cbc:ID>XL-CLS-2026-0042</cbc:ID>
  </cac:OriginalDocumentReference>
  <cac:PreviousDocumentReference>
    <cbc:ID>SCC-PH-25-0198</cbc:ID>
  </cac:PreviousDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>LTM-PO-26-0197</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>SCC-SIG-26-PH</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</GoodsCertificate>
```
