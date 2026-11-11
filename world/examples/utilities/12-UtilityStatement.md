# Utility Statement: Selanu Telecom to Velumi Trading

*Example 12 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

Calls, data and subscriptions per telephone line of the buyer, in the telecommunications supply structure.

[The XML file](12-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:utilities**  
  The business process the document belongs to: the flow "Electricity, water and telecom (one utility in each country)".
- `ProfileExecutionID` = **UTILITIES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **ST-DOC-26-0324**  
  The utility's statement number.
- `UUID` = **7b60d4fc-8fd7-5124-9e01-cfc520caed86**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **17:37:00**  
  The time the sender's system issued the document, in the sender's local time.
- `UtilityStatementTypeCode` = **TEL** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of utility the statement is about. The code is from the Trade Accord's utility type list: TEL = Telephone.
- `Note` = **Mikake votetaka hanano mofilufo kisala vepili vafosu.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): What the statement is.
- `Note` = **This statement explains the consumption behind your bill.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: What the statement is.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the utility's currency; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `AccountingCostCode` = **500**  
  The customer's cost centre, as on the bill.
- `AccountingCost` = **Stock for municipal projects**  
  The cost centre in words.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **ST-INV-26-0323**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **ST-TARIFF-2026**  
  The utility's tariff sheet for 2026.
- `DocumentTypeCode` = **TARIFF** (listID `urn:ubl-examples:world:codelist:DocumentTypeCode`)  
  What the document is. The code is from the Trade Accord's document type list: TARIFF = Tariff.
- `DocumentDescription` = **Prices per unit and the terms of supply.**  
  What it holds.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.selanutelecom.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Telecom (world/parties.json).
- `IndustryClassificationCode` = **6110** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Telecom (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 6110 = Wired telecommunications activities.
- `PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
- `PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Telecom (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42407**  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Telecom (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 20 persons and its turnover of 3230000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Telecom (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Business accounts**  
  The desk that handles this document; identity of Selanu Telecom (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Contact/Telephone` = **+999 3 727 2407**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 34 persons and its turnover of 1940000.000 XLC in 2025, by the Trade Accord's limits; identity of Velumi Trading (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Contact/Telephone` = **+999 3 729 1859**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
- `Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customer Party

Inside `CustomerParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Velumi Trading**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **ST-1077-2603**  
  The telecom consumption of March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  With the calls. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `TotalMeteredQuantity` = **35** (unitCode `E34`)  
  The data beyond the subscriptions.
- `UtilityConsumptionPoint/ID` = **ST-CP-1077**  
  The company's connection.
- `UtilityConsumptionPoint/Description` = **Office of Velumi Trading, Selanu**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **ST-C-1077**  
  The contract.
- `UtilityConsumptionPoint/SubscriberType` = **Business**  
  The name of code BUS in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **BUS** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: BUS = Business.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `UtilityConsumptionPoint/Address/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `UtilityConsumptionPoint/Address/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `UtilityConsumptionPoint/Address/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `UtilityConsumptionPoint/Address/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `UtilityConsumptionPoint/Address/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consumption/UtilityStatementTypeCode` = **TEL** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: TEL = Telephone.
- `Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `Consumption/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/AllowanceCharge/Amount` = **6.354** (currencyID `XLC`)  
  5 % of the six subscriptions.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyType` = **Business lines and data**  
  The name of code BUS in the Trade Accord's telecommunications supply type list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyTypeCode` = **BUS** (listID `urn:ubl-examples:world:codelist:TelecomSupplyTypeCode`)  
  As a code. The code is from the Trade Accord's telecommunications supply type list: BUS = Business lines and data.
- `Consumption/TelecommunicationsSupply/PrivacyCode` = **MASKED** (listID `urn:ubl-examples:world:codelist:PrivacyCode`)  
  Numbers called inside the island are not listed; calls abroad are. The code is from the Trade Accord's privacy list: MASKED = Numbers masked.
- `Consumption/TelecommunicationsSupply/Description` = **Six business lines and a mobile data pool.**  
  In words.
- `Consumption/TelecommunicationsSupply/TotalAmount` = **141.920** (currencyID `XLC`)  
  The telecom supply of March.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **1**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1850**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line with calls on the island included.**  
  The subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ExchangeRate/SourceCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The currency the roaming partner charged in. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ExchangeRate/TargetCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The bill's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ExchangeRate/CalculationRate` = **0.4**  
  The reference rate.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ExchangeRate/MathematicOperatorCode` = **Multiply** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  Lume times the rate. The code is from the world's copy of UBL's Operator list, with a listID: Multiply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ExchangeRate/Date` = **2026-03-31**  
  The rate at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/Amount` = **1.059** (currencyID `XLC`)  
  The line's share of the bundle discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-1**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **140** (unitCode `MIN`)  
  Minutes called on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **C-0311-01**  
  A call.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-11**  
  The day.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **10:14:00**  
  The time.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **+999 2 7121 474 274**  
  The distributor in Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **International**  
  The name of code INT in the Trade Accord's telecommunications service category list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategoryCode` = **INT** (listID `urn:ubl-examples:world:codelist:TelecomServiceCategoryCode`)  
  As a code. The code is from the Trade Accord's telecommunications service category list: INT = International.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **12** (unitCode `MIN`)  
  Twelve minutes.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCall` = **Outgoing**  
  The name of code OUT in the Trade Accord's telecommunications call type list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCallCode` = **OUT** (listID `urn:ubl-examples:world:codelist:TelecomCallTypeCode`)  
  As a code. The code is from the Trade Accord's telecommunications call type list: OUT = Outgoing.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallBaseAmount` = **0.000** (currencyID `XLC`)  
  No set-up charge: included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Calls to the trade accord countries are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/PriceAmount` = **0** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country called. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/AllowanceChargeReasonCode` = **64** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 64 = Special agreement.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/AllowanceChargeReason` = **Calls to the trade accord countries are included in the subscription**  
  Why the call costs nothing.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/Amount` = **2.400** (currencyID `XLC`)  
  All of it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/BaseAmount` = **2.400** (currencyID `XLC`)  
  Twelve minutes at the 0.200 tariff for calls abroad.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/Amount` = **0.000** (currencyID `XLC`)  
  No call duty: included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/Duty` = **Set-up**  
  The name of code SETUP in the Trade Accord's telecommunications duty list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/DutyCode` = **SETUP** (listID `urn:ubl-examples:world:codelist:TelecomDutyCode`)  
  As a code. The code is from the Trade Accord's telecommunications duty list: SETUP = Set-up.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/TaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TimeDuty/Amount` = **0.000** (currencyID `XLC`)  
  No time duty: included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TimeDuty/Duty` = **Per minute**  
  The name of code MIN in the Trade Accord's telecommunications duty list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TimeDuty/DutyCode` = **MIN** (listID `urn:ubl-examples:world:codelist:TelecomDutyCode`)  
  As a code. The code is from the Trade Accord's telecommunications duty list: MIN = Per minute.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **D-0318-01**  
  Mobile data abroad.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-18**  
  The day.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **08:00:00**  
  From the morning.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **data**  
  Mobile data, no number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Roaming**  
  The name of code ROAM in the Trade Accord's telecommunications service category list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategoryCode` = **ROAM** (listID `urn:ubl-examples:world:codelist:TelecomServiceCategoryCode`)  
  As a code. The code is from the Trade Accord's telecommunications service category list: ROAM = Roaming.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/RoamingPartnerName` = **Lumeport mobile network**  
  The network used in Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **35** (unitCode `E34`)  
  35 gigabytes beyond the subscriptions, at the trade fair in Lumeport.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ExchangeRate/SourceCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The partner network's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ExchangeRate/TargetCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The bill's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ExchangeRate/CalculationRate` = **0.4**  
  The reference rate.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **2**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1851**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line with calls on the island included.**  
  The subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/Amount` = **1.059** (currencyID `XLC`)  
  The line's share of the bundle discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-2**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **165** (unitCode `MIN`)  
  Minutes called on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **V-0320-02**  
  A film rented on line 2.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-20**  
  The day.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **12:30:00**  
  At lunch.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **video**  
  The operator's video service, no number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Video on demand**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/MovieTitle` = **Safe Lifting in the Warehouse**  
  A training film the trader's staff watched.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/PayPerView` = **true**  
  Paid per film.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **1** (unitCode `EA`)  
  One film.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Training films are included in the business bundle.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **3**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1852**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line with calls on the island included.**  
  The subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/Amount` = **1.059** (currencyID `XLC`)  
  The line's share of the bundle discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-3**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **190** (unitCode `MIN`)  
  Minutes called on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **4**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1853**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line with calls on the island included.**  
  The subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/Amount` = **1.059** (currencyID `XLC`)  
  The line's share of the bundle discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-4**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **215** (unitCode `MIN`)  
  Minutes called on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **5**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1854**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line with calls on the island included.**  
  The subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/Amount` = **1.059** (currencyID `XLC`)  
  The line's share of the bundle discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-5**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **240** (unitCode `MIN`)  
  Minutes called on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **6**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1855**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line with calls on the island included.**  
  The subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/AllowanceCharge/Amount` = **1.059** (currencyID `XLC`)  
  The line's share of the bundle discount.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-6**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy).
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **265** (unitCode `MIN`)  
  Minutes called on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **7**  
  The data pool.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **data pool**  
  No number: the company's data pool.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Mobile data beyond the subscriptions.**  
  What it is.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **14.840** (currencyID `XLC`)  
  35 GB at the data tariff.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **D-03**  
  The month's data beyond the subscriptions.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-31**  
  Summed at the end of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **23:59:00**  
  At the close of the month.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **data**  
  Mobile data.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/PayPerView` = **false**  
  Not a pay-per-view service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **35** (unitCode `E34`)  
  Gigabytes.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **14.840** (currencyID `XLC`)  
  At the data tariff.
- `Consumption/LegalMonetaryTotal/LineExtensionAmount` = **141.920** (currencyID `XLC`)  
  The supply.
- `Consumption/LegalMonetaryTotal/AllowanceTotalAmount` = **6.354** (currencyID `XLC`)  
  The bundle discount.
- `Consumption/LegalMonetaryTotal/PayableAmount` = **135.566** (currencyID `XLC`)  
  The supply less the discount; no tax.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Selanu Telecom**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **141.920** (currencyID `XLC`)  
  The supply.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/AllowanceTotalAmount` = **6.354** (currencyID `XLC`)  
  The bundle discount.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **135.566** (currencyID `XLC`)  
  The supply less the discount.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **6** (unitCode `MON`)  
  Six business lines for the month.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **127.080** (currencyID `XLC`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **127.080** (currencyID `XLC`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `SupplierConsumption/ConsumptionLine/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `SupplierConsumption/ConsumptionLine/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `SupplierConsumption/ConsumptionLine/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `SupplierConsumption/ConsumptionLine/AllowanceCharge/Amount` = **6.354** (currencyID `XLC`)  
  On the subscriptions of this line.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  0 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **ST-BL**  
  The utility's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **ST-C-1077**  
  The customer's contract.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Telephone**  
  The name of code TEL in the Trade Accord's utility type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **TEL** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The supply the item is for, as a code. The code is from the Trade Accord's utility type list: TEL = Telephone.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Business telephone and data line, monthly subscription.**  
  The tariff in words.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Subscription**  
  The name of code SUB in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **SUB** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: SUB = Subscription.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **ST-C-1077**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **21.18** (currencyID `XLC`)  
  The tariff (world/items.json).
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `MON`)  
  Per unit.
- `SupplierConsumption/ConsumptionLine/UnstructuredPrice/PriceAmount` = **21.18** (currencyID `XLC`)  
  The subscription price as the tariff sheet states it.
- `SupplierConsumption/ConsumptionLine/UnstructuredPrice/TaxInclusivePriceAmount` = **21.18** (currencyID `XLC`)  
  No tax on the island.
- `SupplierConsumption/ConsumptionLine/UnstructuredPrice/TimeAmount` = **per month**  
  The period the price is for.
- `SupplierConsumption/ConsumptionLine/ID` = **2**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **2**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **35** (unitCode `E34`)  
  Mobile data beyond the subscriptions.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **14.840** (currencyID `XLC`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **14.840** (currencyID `XLC`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/Delivery/DeliveryLocation/Description` = **The consumption point of the statement.**  
  Where it was delivered.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  0 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **ST-GB**  
  The utility's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **ST-C-1077**  
  The customer's contract.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Telephone**  
  The name of code TEL in the Trade Accord's utility type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **TEL** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The supply the item is for, as a code. The code is from the Trade Accord's utility type list: TEL = Telephone.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Mobile data beyond the subscription, per gigabyte.**  
  The tariff in words.
- `SupplierConsumption/ConsumptionLine/UtilityItem/PackQuantity` = **5** (unitCode `E34`)  
  Data beyond the subscriptions is sold in packs of 5 GB.
- `SupplierConsumption/ConsumptionLine/UtilityItem/PackSizeNumeric` = **7**  
  Seven packs: the 35 GB of March.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **ST-C-1077**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **0.424** (currencyID `XLC`)  
  The tariff (world/items.json).
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `E34`)  
  Per unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:utilities</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>ST-DOC-26-0324</cbc:ID>
  <cbc:UUID>7b60d4fc-8fd7-5124-9e01-cfc520caed86</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>17:37:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">TEL</cbc:UtilityStatementTypeCode>
  <cbc:Note languageID="qal">Mikake votetaka hanano mofilufo kisala vepili vafosu.</cbc:Note>
  <cbc:Note languageID="en-XL">This statement explains the consumption behind your bill.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>500</cbc:AccountingCostCode>
  <cbc:AccountingCost>Stock for municipal projects</cbc:AccountingCost>
  <cac:ParentDocumentReference>
    <cbc:ID>ST-INV-26-0323</cbc:ID>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>ST-TARIFF-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentTypeCode">TARIFF</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Prices per unit and the terms of supply.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.selanutelecom.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">6110</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Telecom</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
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
      <cbc:CompanyID>IC42407</cbc:CompanyID>
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
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.velumi.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
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
      <cbc:BuildingNumber>16</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
      <cbc:CompanyID>IC41859</cbc:CompanyID>
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
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 3 729 1859</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:CustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:CustomerParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>ST-1077-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:TotalMeteredQuantity unitCode="E34">35</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>ST-CP-1077</cbc:ID>
      <cbc:Description>Office of Velumi Trading, Selanu</cbc:Description>
      <cbc:SubscriberID>ST-C-1077</cbc:SubscriberID>
      <cbc:SubscriberType>Business</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">BUS</cbc:SubscriberTypeCode>
      <cac:Address>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:Address>
    </cac:UtilityConsumptionPoint>
    <cac:Consumption>
      <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">TEL</cbc:UtilityStatementTypeCode>
      <cac:MainPeriod>
        <cbc:StartDate>2026-03-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:MainPeriod>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="XLC">6.354</cbc:Amount>
      </cac:AllowanceCharge>
      <cac:TelecommunicationsSupply>
        <cbc:TelecommunicationsSupplyType>Business lines and data</cbc:TelecommunicationsSupplyType>
        <cbc:TelecommunicationsSupplyTypeCode listID="urn:ubl-examples:world:codelist:TelecomSupplyTypeCode">BUS</cbc:TelecommunicationsSupplyTypeCode>
        <cbc:PrivacyCode listID="urn:ubl-examples:world:codelist:PrivacyCode">MASKED</cbc:PrivacyCode>
        <cbc:Description>Six business lines and a mobile data pool.</cbc:Description>
        <cbc:TotalAmount currencyID="XLC">141.920</cbc:TotalAmount>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>1</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1850</cbc:PhoneNumber>
          <cbc:Description>Business line with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:ExchangeRate>
            <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:SourceCurrencyCode>
            <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TargetCurrencyCode>
            <cbc:CalculationRate>0.4</cbc:CalculationRate>
            <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Multiply</cbc:MathematicOperatorCode>
            <cbc:Date>2026-03-31</cbc:Date>
          </cac:ExchangeRate>
          <cac:AllowanceCharge>
            <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
            <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
            <cbc:Amount currencyID="XLC">1.059</cbc:Amount>
          </cac:AllowanceCharge>
          <cac:TaxTotal>
            <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
          </cac:TaxTotal>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-1</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">140</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
          <cac:TelecommunicationsService>
            <cbc:ID>C-0311-01</cbc:ID>
            <cbc:CallDate>2026-03-11</cbc:CallDate>
            <cbc:CallTime>10:14:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>+999 2 7121 474 274</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>International</cbc:TelecommunicationsServiceCategory>
            <cbc:TelecommunicationsServiceCategoryCode listID="urn:ubl-examples:world:codelist:TelecomServiceCategoryCode">INT</cbc:TelecommunicationsServiceCategoryCode>
            <cbc:Quantity unitCode="MIN">12</cbc:Quantity>
            <cbc:TelecommunicationsServiceCall>Outgoing</cbc:TelecommunicationsServiceCall>
            <cbc:TelecommunicationsServiceCallCode listID="urn:ubl-examples:world:codelist:TelecomCallTypeCode">OUT</cbc:TelecommunicationsServiceCallCode>
            <cbc:CallBaseAmount currencyID="XLC">0.000</cbc:CallBaseAmount>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
            <cac:Price>
              <cbc:PriceAmount currencyID="XLC">0</cbc:PriceAmount>
            </cac:Price>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
            <cac:AllowanceCharge>
              <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
              <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">64</cbc:AllowanceChargeReasonCode>
              <cbc:AllowanceChargeReason>Calls to the trade accord countries are included in the subscription</cbc:AllowanceChargeReason>
              <cbc:Amount currencyID="XLC">2.400</cbc:Amount>
              <cbc:BaseAmount currencyID="XLC">2.400</cbc:BaseAmount>
            </cac:AllowanceCharge>
            <cac:TaxTotal>
              <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
            </cac:TaxTotal>
            <cac:CallDuty>
              <cbc:Amount currencyID="XLC">0.000</cbc:Amount>
              <cbc:Duty>Set-up</cbc:Duty>
              <cbc:DutyCode listID="urn:ubl-examples:world:codelist:TelecomDutyCode">SETUP</cbc:DutyCode>
              <cac:TaxCategory>
                <cbc:ID>O</cbc:ID>
                <cbc:Percent>0</cbc:Percent>
                <cac:TaxScheme>
                  <cbc:Name>No general sales tax</cbc:Name>
                </cac:TaxScheme>
              </cac:TaxCategory>
            </cac:CallDuty>
            <cac:TimeDuty>
              <cbc:Amount currencyID="XLC">0.000</cbc:Amount>
              <cbc:Duty>Per minute</cbc:Duty>
              <cbc:DutyCode listID="urn:ubl-examples:world:codelist:TelecomDutyCode">MIN</cbc:DutyCode>
            </cac:TimeDuty>
          </cac:TelecommunicationsService>
          <cac:TelecommunicationsService>
            <cbc:ID>D-0318-01</cbc:ID>
            <cbc:CallDate>2026-03-18</cbc:CallDate>
            <cbc:CallTime>08:00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>data</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Roaming</cbc:TelecommunicationsServiceCategory>
            <cbc:TelecommunicationsServiceCategoryCode listID="urn:ubl-examples:world:codelist:TelecomServiceCategoryCode">ROAM</cbc:TelecommunicationsServiceCategoryCode>
            <cbc:RoamingPartnerName>Lumeport mobile network</cbc:RoamingPartnerName>
            <cbc:Quantity unitCode="E34">35</cbc:Quantity>
            <cac:ExchangeRate>
              <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:SourceCurrencyCode>
              <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TargetCurrencyCode>
              <cbc:CalculationRate>0.4</cbc:CalculationRate>
            </cac:ExchangeRate>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>2</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1851</cbc:PhoneNumber>
          <cbc:Description>Business line with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:AllowanceCharge>
            <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
            <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
            <cbc:Amount currencyID="XLC">1.059</cbc:Amount>
          </cac:AllowanceCharge>
          <cac:TaxTotal>
            <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
          </cac:TaxTotal>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-2</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">165</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
          <cac:TelecommunicationsService>
            <cbc:ID>V-0320-02</cbc:ID>
            <cbc:CallDate>2026-03-20</cbc:CallDate>
            <cbc:CallTime>12:30:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>video</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Video on demand</cbc:TelecommunicationsServiceCategory>
            <cbc:MovieTitle>Safe Lifting in the Warehouse</cbc:MovieTitle>
            <cbc:PayPerView>true</cbc:PayPerView>
            <cbc:Quantity unitCode="EA">1</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>3</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1852</cbc:PhoneNumber>
          <cbc:Description>Business line with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:AllowanceCharge>
            <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
            <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
            <cbc:Amount currencyID="XLC">1.059</cbc:Amount>
          </cac:AllowanceCharge>
          <cac:TaxTotal>
            <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
          </cac:TaxTotal>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-3</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">190</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>4</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1853</cbc:PhoneNumber>
          <cbc:Description>Business line with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:AllowanceCharge>
            <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
            <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
            <cbc:Amount currencyID="XLC">1.059</cbc:Amount>
          </cac:AllowanceCharge>
          <cac:TaxTotal>
            <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
          </cac:TaxTotal>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-4</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">215</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>5</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1854</cbc:PhoneNumber>
          <cbc:Description>Business line with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:AllowanceCharge>
            <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
            <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
            <cbc:Amount currencyID="XLC">1.059</cbc:Amount>
          </cac:AllowanceCharge>
          <cac:TaxTotal>
            <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
          </cac:TaxTotal>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-5</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">240</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>6</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1855</cbc:PhoneNumber>
          <cbc:Description>Business line with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:AllowanceCharge>
            <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
            <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
            <cbc:Amount currencyID="XLC">1.059</cbc:Amount>
          </cac:AllowanceCharge>
          <cac:TaxTotal>
            <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
          </cac:TaxTotal>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-6</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">265</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>7</cbc:ID>
          <cbc:PhoneNumber>data pool</cbc:PhoneNumber>
          <cbc:Description>Mobile data beyond the subscriptions.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">14.840</cbc:LineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>D-03</cbc:ID>
            <cbc:CallDate>2026-03-31</cbc:CallDate>
            <cbc:CallTime>23:59:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>data</cbc:ServiceNumberCalled>
            <cbc:PayPerView>false</cbc:PayPerView>
            <cbc:Quantity unitCode="E34">35</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">14.840</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
      </cac:TelecommunicationsSupply>
      <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="XLC">141.920</cbc:LineExtensionAmount>
        <cbc:AllowanceTotalAmount currencyID="XLC">6.354</cbc:AllowanceTotalAmount>
        <cbc:PayableAmount currencyID="XLC">135.566</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:Consumption>
    <cac:SupplierConsumption>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Telecom</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Velumi Trading</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XLC">141.920</cbc:LineExtensionAmount>
          <cbc:AllowanceTotalAmount currencyID="XLC">6.354</cbc:AllowanceTotalAmount>
          <cbc:PayableAmount currencyID="XLC">135.566</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:ConsumptionLine>
        <cbc:ID>1</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MON">6</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XLC">127.080</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">127.080</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:AllowanceCharge>
          <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
          <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
          <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
          <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
          <cbc:Amount currencyID="XLC">6.354</cbc:Amount>
        </cac:AllowanceCharge>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>ST-BL</cbc:ID>
          <cbc:SubscriberID>ST-C-1077</cbc:SubscriberID>
          <cbc:SubscriberType>Telephone</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">TEL</cbc:SubscriberTypeCode>
          <cbc:Description>Business telephone and data line, monthly subscription.</cbc:Description>
          <cbc:ConsumptionType>Subscription</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">SUB</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID>O</cbc:ID>
            <cbc:Percent>0</cbc:Percent>
            <cac:TaxScheme>
              <cbc:Name>No general sales tax</cbc:Name>
            </cac:TaxScheme>
          </cac:TaxCategory>
          <cac:Contract>
            <cbc:ID>ST-C-1077</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XLC">21.18</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="MON">1</cbc:BaseQuantity>
        </cac:Price>
        <cac:UnstructuredPrice>
          <cbc:PriceAmount currencyID="XLC">21.18</cbc:PriceAmount>
          <cbc:TaxInclusivePriceAmount currencyID="XLC">21.18</cbc:TaxInclusivePriceAmount>
          <cbc:TimeAmount>per month</cbc:TimeAmount>
        </cac:UnstructuredPrice>
      </cac:ConsumptionLine>
      <cac:ConsumptionLine>
        <cbc:ID>2</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>2</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="E34">35</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XLC">14.840</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">14.840</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:Delivery>
          <cac:DeliveryLocation>
            <cbc:Description>The consumption point of the statement.</cbc:Description>
          </cac:DeliveryLocation>
        </cac:Delivery>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>ST-GB</cbc:ID>
          <cbc:SubscriberID>ST-C-1077</cbc:SubscriberID>
          <cbc:SubscriberType>Telephone</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">TEL</cbc:SubscriberTypeCode>
          <cbc:Description>Mobile data beyond the subscription, per gigabyte.</cbc:Description>
          <cbc:PackQuantity unitCode="E34">5</cbc:PackQuantity>
          <cbc:PackSizeNumeric>7</cbc:PackSizeNumeric>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID>O</cbc:ID>
            <cbc:Percent>0</cbc:Percent>
            <cac:TaxScheme>
              <cbc:Name>No general sales tax</cbc:Name>
            </cac:TaxScheme>
          </cac:TaxCategory>
          <cac:Contract>
            <cbc:ID>ST-C-1077</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XLC">0.424</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="E34">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
