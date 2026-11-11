# Qualification Application Request: Lumeport Public Works Department to Brackenmere Furniture

*Example 6 of the flow "A public tender (Bayvarra)" · [Qualification Application Request in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-QUALIFICATION-APPLICATION-REQUEST-SCHEMA)*

The authority sends the furniture maker the self-declaration it must fill in: exclusion grounds and selection criteria.

[The XML file](06-QualificationApplicationRequest.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:tender**  
  The business process the document belongs to: the flow "A public tender (Bayvarra)".
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0192**  
  The sender's number for this document.
- `UUID` = **3c06617e-8a80-509a-b64c-e7ad1ca81e2a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `ContractName` = **Park benches for the parks renewal programme**  
  The contract.
- `IssueDate` = **2026-02-13**  
  Sent with the procurement documents.
- `IssueTime` = **08:25:00**  
  The time the sender's system issued the document, in the sender's local time.
- `VersionID` = **1**  
  The first version.
- `PreviousVersionID` = **0**  
  None.
- `ProcedureCode` = **Open**  
  An open procedure.
- `QualificationApplicationTypeCode` = **Regulated**  
  The regulated form of self-declaration.
- `WeightScoringMethodologyNote` = **Pass or fail; no weighting.**  
  How answers count.
- `WeightingTypeCode` = **None**  
  No weighting.
- `Note` = **Answer every criterion.**  
  What to do.

### Contracting Party

Inside `ContractingParty`:

- `Party/IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410548** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/ID` = **LUM-ADR-000417**  
  The address's number in the city's address register; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered for state sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-0900002**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/ExemptionReasonCode` = **XB-PUBLIC**  
  The exemption as a code of the world's exemption list (world/countries.json): sale to a public body.
- `Party/PartyTaxScheme/ExemptionReason` = **Public bodies are exempt from the state sales tax**  
  Why purchases by this party carry no sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/RegistrationAddress/CityName` = **Lumeport**  
  Where the party is registered for the tax.
- `Party/PartyTaxScheme/RegistrationAddress/CountrySubentity` = **Coastal State**  
  Its state.
- `Party/PartyTaxScheme/RegistrationAddress/Country/IdentificationCode` = **XB**  
  Its country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered, with its legal form; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410548**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Party/Contact/Name` = **Procurement office**  
  The desk that handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2648 0548**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Economic Operator Party

Inside `EconomicOperatorParty`:

- `Party/WebsiteURI` = **https://www.brackenmere.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brackenmere Furniture (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Party/PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered for state sales tax; identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1237398**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered, with its legal form; identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412466**  
  Number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Party/Contact/Name` = **Trade sales**  
  The desk that handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 266 466**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Procurement Project

Inside `ProcurementProject`:

- `ID` = **PWD-2026-PARKS**  
  The procedure.

### Procurement Project Lot

Inside `ProcurementProjectLot`:

- `ID` = **LOT-1**  
  Lot 1.

### Tendering Criterion

Inside `TenderingCriterion`:

- `ID` = **CR-TURNOVER**  
  The turnover criterion.
- `CriterionTypeCode` = **Economic**  
  Its kind.
- `Name` = **General yearly turnover**  
  The criterion.
- `Description` = **Turnover of the last three years.**  
  What.
- `WeightNumeric` = **0**  
  Pass or fail.
- `FulfilmentIndicator` = **true**  
  Must be met.
- `FulfilmentIndicatorTypeCode` = **All**  
  All its properties.
- `EvaluationMethodTypeCode` = **PassFail**  
  Pass or fail.
- `WeightingConsiderationDescription` = **Not weighted.**  
  Why.
- `ProcurementProjectLotReference/ID` = **LOT-1**  
  Lot 1 of the procedure.
- `CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  The benches.
- `SubTenderingCriterion/ID` = **CR-TURNOVER-A**  
  The average.
- `SubTenderingCriterion/Name` = **Average turnover**  
  Name.
- `Legislation/ID` = **XB-PPA-2019**  
  The act.
- `Legislation/Title` = **Public Procurement Act**  
  Title.
- `Legislation/Description` = **Selection criteria.**  
  What.
- `Legislation/JurisdictionLevel` = **National**  
  The level.
- `Legislation/Article` = **Art. 58**  
  The article.
- `Legislation/URI` = **https://law.bayvarra.example/ppa**  
  Where.
- `Legislation/Language/ID` = **en**  
  English.
- `Legislation/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  Bayvarra.
- `TenderingCriterionPropertyGroup/ID` = **PG-1**  
  The group.
- `TenderingCriterionPropertyGroup/Name` = **Turnover**  
  Name.
- `TenderingCriterionPropertyGroup/Description` = **The figures.**  
  What.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **OnTrue**  
  Answered when the criterion applies.
- `TenderingCriterionPropertyGroup/FulfilmentIndicator` = **true**  
  Must be met.
- `TenderingCriterionPropertyGroup/FulfilmentIndicatorTypeCode` = **All**  
  All properties.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-1**  
  The property.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Yearly turnover**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Answer: yearly turnover.**  
  What is asked.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **Requirement**  
  Question or requirement.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **Amount**  
  An amount.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueCurrencyCode` = **XBL**  
  In lume.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedAmount` = **250000.00** (currencyID `XBL`)  
  At least.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MaximumAmount` = **99999999.00** (currencyID `XBL`)  
  No real maximum.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumAmount` = **250000.00** (currencyID `XBL`)  
  The minimum.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ApplicablePeriod/StartDate` = **2023-01-01**  
  The three years
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ApplicablePeriod/EndDate` = **2025-12-31**  
  before the tender.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TemplateEvidence/ID` = **EV-ACC**  
  Annual accounts.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TemplateEvidence/Name` = **Accounts**  
  Evidence.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-2**  
  The property.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Years in business**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Answer: years in business.**  
  What is asked.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **Question**  
  Question or requirement.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **Quantity**  
  A number.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueUnitCode` = **ANN**  
  Years.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedValueNumeric` = **3**  
  At least.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MaximumValueNumeric` = **200**  
  Maximum.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumValueNumeric` = **3**  
  Minimum.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MaximumQuantity` = **200** (unitCode `ANN`)  
  No real maximum.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumQuantity` = **3** (unitCode `ANN`)  
  At least three.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-3**  
  The property.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Registered in a business register**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Answer: registered in a business register.**  
  What is asked.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **Question**  
  Question or requirement.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **Indicator**  
  Yes or no.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedID` = **REG**  
  The register.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedIndicator` = **true**  
  Yes.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedCode` = **Registered**  
  The status.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedDescription` = **Entered in a national register.**  
  Expected.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedURI` = **https://register.bayvarra.example**  
  A register.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TranslationTypeCode` = **None**  
  No translation needed.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/CertificationLevelDescription` = **A plain extract will do.**  
  The level.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/CopyQualityTypeCode` = **Copy**  
  A copy is enough.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/ID` = **PG-1.1**  
  If a consortium.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/Name` = **Consortium**  
  Name.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-4**  
  The property.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Share in the consortium**  
  Its name.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Answer: share in the consortium.**  
  What is asked.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **Question**  
  Question or requirement.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **Percent**  
  A percentage.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **PWD-2026-PARKS-CFT**  
  The call for tenders.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-QAR**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<QualificationApplicationRequest xmlns="urn:oasis:names:specification:ubl:schema:xsd:QualificationApplicationRequest-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:tender</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0192</cbc:ID>
  <cbc:UUID>3c06617e-8a80-509a-b64c-e7ad1ca81e2a</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:IssueDate>2026-02-13</cbc:IssueDate>
  <cbc:IssueTime>08:25:00</cbc:IssueTime>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:PreviousVersionID>0</cbc:PreviousVersionID>
  <cbc:ProcedureCode>Open</cbc:ProcedureCode>
  <cbc:QualificationApplicationTypeCode>Regulated</cbc:QualificationApplicationTypeCode>
  <cbc:WeightScoringMethodologyNote>Pass or fail; no weighting.</cbc:WeightScoringMethodologyNote>
  <cbc:WeightingTypeCode>None</cbc:WeightingTypeCode>
  <cbc:Note>Answer every criterion.</cbc:Note>
  <cac:ContractingParty>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410548</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID>LUM-ADR-000417</cbc:ID>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
        <cbc:Department>Procurement office</cbc:Department>
        <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>CO-0900002</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cbc:ExemptionReasonCode>XB-PUBLIC</cbc:ExemptionReasonCode>
        <cbc:ExemptionReason>Public bodies are exempt from the state sales tax</cbc:ExemptionReason>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>20410548</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Procurement office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 38 2648 0548</cbc:Telephone>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410548</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:ContractingParty>
  <cac:EconomicOperatorParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.brackenmere.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Joiners Row</cbc:StreetName>
        <cbc:BuildingNumber>14</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71203</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
        <cbc:CompanyID>UL-1237398</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20412466</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Marrowdale</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Trade sales</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 266 466</cbc:Telephone>
        <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:EconomicOperatorParty>
  <cac:ProcurementProject>
    <cbc:ID>PWD-2026-PARKS</cbc:ID>
  </cac:ProcurementProject>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-1</cbc:ID>
  </cac:ProcurementProjectLot>
  <cac:TenderingCriterion>
    <cbc:ID>CR-TURNOVER</cbc:ID>
    <cbc:CriterionTypeCode>Economic</cbc:CriterionTypeCode>
    <cbc:Name>General yearly turnover</cbc:Name>
    <cbc:Description>Turnover of the last three years.</cbc:Description>
    <cbc:WeightNumeric>0</cbc:WeightNumeric>
    <cbc:FulfilmentIndicator>true</cbc:FulfilmentIndicator>
    <cbc:FulfilmentIndicatorTypeCode>All</cbc:FulfilmentIndicatorTypeCode>
    <cbc:EvaluationMethodTypeCode>PassFail</cbc:EvaluationMethodTypeCode>
    <cbc:WeightingConsiderationDescription>Not weighted.</cbc:WeightingConsiderationDescription>
    <cac:ProcurementProjectLotReference>
      <cbc:ID>LOT-1</cbc:ID>
    </cac:ProcurementProjectLotReference>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:SubTenderingCriterion>
      <cbc:ID>CR-TURNOVER-A</cbc:ID>
      <cbc:Name>Average turnover</cbc:Name>
    </cac:SubTenderingCriterion>
    <cac:Legislation>
      <cbc:ID>XB-PPA-2019</cbc:ID>
      <cbc:Title>Public Procurement Act</cbc:Title>
      <cbc:Description>Selection criteria.</cbc:Description>
      <cbc:JurisdictionLevel>National</cbc:JurisdictionLevel>
      <cbc:Article>Art. 58</cbc:Article>
      <cbc:URI>https://law.bayvarra.example/ppa</cbc:URI>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
      </cac:Language>
      <cac:JurisdictionRegionAddress>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:JurisdictionRegionAddress>
    </cac:Legislation>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-1</cbc:ID>
      <cbc:Name>Turnover</cbc:Name>
      <cbc:Description>The figures.</cbc:Description>
      <cbc:PropertyGroupTypeCode>OnTrue</cbc:PropertyGroupTypeCode>
      <cbc:FulfilmentIndicator>true</cbc:FulfilmentIndicator>
      <cbc:FulfilmentIndicatorTypeCode>All</cbc:FulfilmentIndicatorTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-1</cbc:ID>
        <cbc:Name>Yearly turnover</cbc:Name>
        <cbc:Description>Answer: yearly turnover.</cbc:Description>
        <cbc:TypeCode>Requirement</cbc:TypeCode>
        <cbc:ValueDataTypeCode>Amount</cbc:ValueDataTypeCode>
        <cbc:ValueCurrencyCode>XBL</cbc:ValueCurrencyCode>
        <cbc:ExpectedAmount currencyID="XBL">250000.00</cbc:ExpectedAmount>
        <cbc:MaximumAmount currencyID="XBL">99999999.00</cbc:MaximumAmount>
        <cbc:MinimumAmount currencyID="XBL">250000.00</cbc:MinimumAmount>
        <cac:ApplicablePeriod>
          <cbc:StartDate>2023-01-01</cbc:StartDate>
          <cbc:EndDate>2025-12-31</cbc:EndDate>
        </cac:ApplicablePeriod>
        <cac:TemplateEvidence>
          <cbc:ID>EV-ACC</cbc:ID>
          <cbc:Name>Accounts</cbc:Name>
        </cac:TemplateEvidence>
      </cac:TenderingCriterionProperty>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-2</cbc:ID>
        <cbc:Name>Years in business</cbc:Name>
        <cbc:Description>Answer: years in business.</cbc:Description>
        <cbc:TypeCode>Question</cbc:TypeCode>
        <cbc:ValueDataTypeCode>Quantity</cbc:ValueDataTypeCode>
        <cbc:ValueUnitCode>ANN</cbc:ValueUnitCode>
        <cbc:ExpectedValueNumeric>3</cbc:ExpectedValueNumeric>
        <cbc:MaximumValueNumeric>200</cbc:MaximumValueNumeric>
        <cbc:MinimumValueNumeric>3</cbc:MinimumValueNumeric>
        <cbc:MaximumQuantity unitCode="ANN">200</cbc:MaximumQuantity>
        <cbc:MinimumQuantity unitCode="ANN">3</cbc:MinimumQuantity>
      </cac:TenderingCriterionProperty>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-3</cbc:ID>
        <cbc:Name>Registered in a business register</cbc:Name>
        <cbc:Description>Answer: registered in a business register.</cbc:Description>
        <cbc:TypeCode>Question</cbc:TypeCode>
        <cbc:ValueDataTypeCode>Indicator</cbc:ValueDataTypeCode>
        <cbc:ExpectedID>REG</cbc:ExpectedID>
        <cbc:ExpectedIndicator>true</cbc:ExpectedIndicator>
        <cbc:ExpectedCode>Registered</cbc:ExpectedCode>
        <cbc:ExpectedDescription>Entered in a national register.</cbc:ExpectedDescription>
        <cbc:ExpectedURI>https://register.bayvarra.example</cbc:ExpectedURI>
        <cbc:TranslationTypeCode>None</cbc:TranslationTypeCode>
        <cbc:CertificationLevelDescription>A plain extract will do.</cbc:CertificationLevelDescription>
        <cbc:CopyQualityTypeCode>Copy</cbc:CopyQualityTypeCode>
      </cac:TenderingCriterionProperty>
      <cac:SubsidiaryTenderingCriterionPropertyGroup>
        <cbc:ID>PG-1.1</cbc:ID>
        <cbc:Name>Consortium</cbc:Name>
        <cac:TenderingCriterionProperty>
          <cbc:ID>P-4</cbc:ID>
          <cbc:Name>Share in the consortium</cbc:Name>
          <cbc:Description>Answer: share in the consortium.</cbc:Description>
          <cbc:TypeCode>Question</cbc:TypeCode>
          <cbc:ValueDataTypeCode>Percent</cbc:ValueDataTypeCode>
        </cac:TenderingCriterionProperty>
      </cac:SubsidiaryTenderingCriterionPropertyGroup>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:AdditionalDocumentReference>
    <cbc:ID>PWD-2026-PARKS-CFT</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-QAR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</QualificationApplicationRequest>
```
