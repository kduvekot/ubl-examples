# Tenderer Qualification: Valdara Industries to Lumeport Public Works Department

*Example 13 of the flow "A public tender (Bayvarra)" · [Tenderer Qualification in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TENDERER-QUALIFICATION-SCHEMA)*

The manufacturer declares its qualifications and those of its consortium partner.

[The XML file](13-TendererQualification.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Capability/ID first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:tenderer-qualification:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Tenderer qualification"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-DOC-26-0199**  
  The tenderer's number for its declaration.
- `UUID` = **544dae4e-ce5c-5e98-a9b3-2b79b00edc95**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-02-25**  
  Submitted with the tender.
- `IssueTime` = **08:52:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Drek mundran vek Saltmere dek zheksir gan drek dreknul.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): Who.
- `Note` = **The manufacturer with Saltmere as subcontractor for the installation.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: Who.
- `VersionID` = **1**  
  The first version.

### Signature

Inside `Signature`:

- `ID` = **VI-SIG-TQ**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Tenderer Party Qualification

Inside `TendererPartyQualification`:

- `InterestedProcurementProjectLot/ID` = **LOT-1**  
  Lot 1.
- `InterestedProcurementProjectLot/ID` = **LOT-2**  
  Lot 2.
- `MainQualifyingParty/ParticipationPercent` = **80**  
  The manufacturer's share.
- `MainQualifyingParty/PersonalSituation` = **No exclusion grounds apply.**  
  Declared.
- `MainQualifyingParty/OperatingYearsQuantity` = **41** (unitCode `ANN`)  
  In business since 1985.
- `MainQualifyingParty/EmployeeQuantity` = **180** (unitCode `IE`)  
  Employees, in persons.
- `MainQualifyingParty/BusinessClassificationEvidenceID` = **ISIC-3100**  
  Its class.
- `MainQualifyingParty/BusinessIdentityEvidenceID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Its registration. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `MainQualifyingParty/TendererRoleCode` = **LEAD** (listID `urn:ubl-examples:world:codelist:TendererRoleCode`)  
  The lead tenderer. The code is from the Trade Accord's tenderer role list: LEAD = Consortium lead.
- `MainQualifyingParty/BusinessClassificationScheme/ID` = **ISIC4**  
  ISIC Rev. 4.
- `MainQualifyingParty/BusinessClassificationScheme/ClassificationCategory/CodeValue` = **3100**  
  Furniture.
- `MainQualifyingParty/TechnicalCapability/ID` = **TC-1**  
  Production.
- `MainQualifyingParty/TechnicalCapability/Description` = **4,000 benches a year.**  
  Capacity.
- `MainQualifyingParty/TechnicalCapability/ValueQuantity` = **4000** (unitCode `EA`)  
  A year.
- `MainQualifyingParty/FinancialCapability/ID` = **FC-1**  
  Turnover.
- `MainQualifyingParty/FinancialCapability/ValueAmount` = **9200000.00** (currencyID `XBL`)  
  Yearly turnover, in lume.
- `MainQualifyingParty/CompletedTask/AnnualAverageAmount` = **180000.00** (currencyID `XBL`)  
  A year, similar supplies.
- `MainQualifyingParty/CompletedTask/TotalTaskAmount` = **540000.00** (currencyID `XBL`)  
  Three years.
- `MainQualifyingParty/CompletedTask/PartyCapacityAmount` = **540000.00** (currencyID `XBL`)  
  All by itself.
- `MainQualifyingParty/CompletedTask/Description` = **Benches for Ferrano's parks.**  
  The task.
- `MainQualifyingParty/CompletedTask/SuppliedEvidence/ID` = **EV-FER-PARKS**  
  Ferrano's reference letter.
- `MainQualifyingParty/CompletedTask/Period/StartDate` = **2023-01-01**  
  From.
- `MainQualifyingParty/CompletedTask/Period/EndDate` = **2025-12-31**  
  To.
- `MainQualifyingParty/CompletedTask/RecipientCustomerParty/Party/PartyName/Name` = **City of Ferrano**  
  The customer.
- `MainQualifyingParty/Declaration/ID` = **DEC-1**  
  A declaration.
- `MainQualifyingParty/Declaration/Name` = **No conflict of interest**  
  Name.
- `MainQualifyingParty/Declaration/DeclarationTypeCode` = **INTEGRITY** (listID `urn:ubl-examples:world:codelist:DeclarationTypeCode`)  
  Its kind. The code is from the Trade Accord's declaration type list: INTEGRITY = Integrity declaration.
- `MainQualifyingParty/Declaration/Description` = **No ties with the department's officers.**  
  What.
- `MainQualifyingParty/Declaration/SuppliedEvidence/ID` = **EV-DEC-1**  
  The signed declaration.
- `MainQualifyingParty/Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `MainQualifyingParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainQualifyingParty/Party/AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `MainQualifyingParty/Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `MainQualifyingParty/Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `MainQualifyingParty/Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `MainQualifyingParty/Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainQualifyingParty/Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainQualifyingParty/Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `MainQualifyingParty/Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyTaxScheme/CompanyID` = **XU007299291** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `MainQualifyingParty/Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `MainQualifyingParty/Party/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `MainQualifyingParty/Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `MainQualifyingParty/Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainQualifyingParty/Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `MainQualifyingParty/Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `MainQualifyingParty/Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `MainQualifyingParty/Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `MainQualifyingParty/Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 3083 persons and its turnover of 23600000000 XUF in 2025, by the Trade Accord's limits; identity of Valdara Industries (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `MainQualifyingParty/Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `MainQualifyingParty/Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `MainQualifyingParty/Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `MainQualifyingParty/Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
- `MainQualifyingParty/Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `MainQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `MainQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `MainQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainQualifyingParty/Party/PartyLegalEntity/SecurityListing/ID` = **XU0001042501** (schemeID `ISO 6166`)  
  The identifier of the listed shares, in the form of an ISIN with the world's country code. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `MainQualifyingParty/Party/PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `MainQualifyingParty/Party/PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The name of code XFER in the Trade Accord's market identifier list.
- `MainQualifyingParty/Party/PartyLegalEntity/SecurityListing/MarketCode` = **XFER** (listID `urn:ubl-examples:world:codelist:MarketCode`)  
  The market's code. The code is from the Trade Accord's market identifier list: XFER = Ferrano Stock Exchange.
- `MainQualifyingParty/Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `MainQualifyingParty/Party/Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `MainQualifyingParty/Party/ServiceProviderParty/ID` = **VI-SP-2026-01**  
  The number of the service contract between the two; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/ServiceProviderParty/ServiceTypeCode` = **LOGISTICS** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  The kind of service, as a code. The code is from the Trade Accord's service type list: LOGISTICS = Logistics service.
- `MainQualifyingParty/Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `MainQualifyingParty/Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `MainQualifyingParty/Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `MainQualifyingParty/Party/ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `MainQualifyingParty/Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainQualifyingParty/Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainQualifyingParty/EconomicOperatorRole/RoleCode` = **LEAD** (listID `urn:ubl-examples:world:codelist:EconomicOperatorRoleCode`)  
  The lead. The code is from the Trade Accord's economic operator role list: LEAD = Consortium lead.
- `MainQualifyingParty/EconomicOperatorRole/RoleDescription` = **Leads.**  
  Role.
- `AdditionalQualifyingParty/ParticipationPercent` = **20**  
  Saltmere's share.
- `AdditionalQualifyingParty/TendererRoleCode` = **SUBCONTRACTOR** (listID `urn:ubl-examples:world:codelist:TendererRoleCode`)  
  For the installation. The code is from the Trade Accord's tenderer role list: SUBCONTRACTOR = Subcontractor.
- `AdditionalQualifyingParty/Party/IndustryClassificationCode` = **4290** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Saltmere Engineering (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4290 = Construction of other civil engineering projects.
- `AdditionalQualifyingParty/Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalQualifyingParty/Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `AdditionalQualifyingParty/Party/Language/Name` = **English**  
  The language's name.
- `AdditionalQualifyingParty/Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `AdditionalQualifyingParty/Party/PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `AdditionalQualifyingParty/Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `AdditionalQualifyingParty/Party/PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `AdditionalQualifyingParty/Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `AdditionalQualifyingParty/Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `AdditionalQualifyingParty/Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AdditionalQualifyingParty/Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `AdditionalQualifyingParty/Party/PartyTaxScheme/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered for state sales tax; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PartyTaxScheme/CompanyID` = **UL-1232055** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Saltmere Engineering (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `AdditionalQualifyingParty/Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `AdditionalQualifyingParty/Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `AdditionalQualifyingParty/Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `AdditionalQualifyingParty/Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `AdditionalQualifyingParty/Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered, with its legal form; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CompanyID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `AdditionalQualifyingParty/Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AdditionalQualifyingParty/Party/Contact/Name` = **Bids office**  
  The desk that handles this document; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/Telephone` = **+999 2 7121 885 685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `AdditionalQualifyingParty/Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `AdditionalQualifyingParty/Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Contracting Party

Inside `ContractingParty`:

- `Party/IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Public Works Department (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 8411 = General public administration activities.
- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410548** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered for state sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-0900002** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeport Public Works Department (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/ExemptionReasonCode` = **PUBLIC** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption as a code of Bayvarra's national list of exemption reasons: sale to a public body. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Sale to a public body.
- `Party/PartyTaxScheme/ExemptionReason` = **Sale to a public body: public bodies are exempt from the state sales tax**  
  The name of code PUBLIC in Bayvarra's national sales tax exemption reason list, followed by the detail of this case: why purchases by this party carry no sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/RegistrationAddress/CityName` = **Lumeport**  
  Where the party is registered for the tax.
- `Party/PartyTaxScheme/RegistrationAddress/CountrySubentity` = **Coastal State**  
  Its state or territory.
- `Party/PartyTaxScheme/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered, with its legal form; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Procurement office**  
  The desk that handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2648 0548**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Evidence

Inside `Evidence`:

- `ID` = **EV-FER-PARKS**  
  The reference.
- `Name` = **Ferrano reference**  
  Name.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **VI-ESPD-26**  
  The self-declaration.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TendererQualification xmlns="urn:oasis:names:specification:ubl:schema:xsd:TendererQualification-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:tenderer-qualification:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-DOC-26-0199</cbc:ID>
  <cbc:UUID>544dae4e-ce5c-5e98-a9b3-2b79b00edc95</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-25</cbc:IssueDate>
  <cbc:IssueTime>08:52:00</cbc:IssueTime>
  <cbc:Note languageID="qau">Drek mundran vek Saltmere dek zheksir gan drek dreknul.</cbc:Note>
  <cbc:Note languageID="en-XU">The manufacturer with Saltmere as subcontractor for the installation.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:Signature>
    <cbc:ID>VI-SIG-TQ</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:TendererPartyQualification>
    <cac:InterestedProcurementProjectLot>
      <cbc:ID>LOT-1</cbc:ID>
    </cac:InterestedProcurementProjectLot>
    <cac:InterestedProcurementProjectLot>
      <cbc:ID>LOT-2</cbc:ID>
    </cac:InterestedProcurementProjectLot>
    <cac:MainQualifyingParty>
      <cbc:ParticipationPercent>80</cbc:ParticipationPercent>
      <cbc:PersonalSituation>No exclusion grounds apply.</cbc:PersonalSituation>
      <cbc:OperatingYearsQuantity unitCode="ANN">41</cbc:OperatingYearsQuantity>
      <cbc:EmployeeQuantity unitCode="IE">180</cbc:EmployeeQuantity>
      <cbc:BusinessClassificationEvidenceID>ISIC-3100</cbc:BusinessClassificationEvidenceID>
      <cbc:BusinessIdentityEvidenceID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:BusinessIdentityEvidenceID>
      <cbc:TendererRoleCode listID="urn:ubl-examples:world:codelist:TendererRoleCode">LEAD</cbc:TendererRoleCode>
      <cac:BusinessClassificationScheme>
        <cbc:ID>ISIC4</cbc:ID>
        <cac:ClassificationCategory>
          <cbc:CodeValue>3100</cbc:CodeValue>
        </cac:ClassificationCategory>
      </cac:BusinessClassificationScheme>
      <cac:TechnicalCapability>
        <cbc:ID>TC-1</cbc:ID>
        <cbc:Description>4,000 benches a year.</cbc:Description>
        <cbc:ValueQuantity unitCode="EA">4000</cbc:ValueQuantity>
      </cac:TechnicalCapability>
      <cac:FinancialCapability>
        <cbc:ID>FC-1</cbc:ID>
        <cbc:ValueAmount currencyID="XBL">9200000.00</cbc:ValueAmount>
      </cac:FinancialCapability>
      <cac:CompletedTask>
        <cbc:AnnualAverageAmount currencyID="XBL">180000.00</cbc:AnnualAverageAmount>
        <cbc:TotalTaskAmount currencyID="XBL">540000.00</cbc:TotalTaskAmount>
        <cbc:PartyCapacityAmount currencyID="XBL">540000.00</cbc:PartyCapacityAmount>
        <cbc:Description>Benches for Ferrano's parks.</cbc:Description>
        <cac:SuppliedEvidence>
          <cbc:ID>EV-FER-PARKS</cbc:ID>
        </cac:SuppliedEvidence>
        <cac:Period>
          <cbc:StartDate>2023-01-01</cbc:StartDate>
          <cbc:EndDate>2025-12-31</cbc:EndDate>
        </cac:Period>
        <cac:RecipientCustomerParty>
          <cac:Party>
            <cac:PartyName>
              <cbc:Name>City of Ferrano</cbc:Name>
            </cac:PartyName>
          </cac:Party>
        </cac:RecipientCustomerParty>
      </cac:CompletedTask>
      <cac:Declaration>
        <cbc:ID>DEC-1</cbc:ID>
        <cbc:Name>No conflict of interest</cbc:Name>
        <cbc:DeclarationTypeCode listID="urn:ubl-examples:world:codelist:DeclarationTypeCode">INTEGRITY</cbc:DeclarationTypeCode>
        <cbc:Description>No ties with the department's officers.</cbc:Description>
        <cac:SuppliedEvidence>
          <cbc:ID>EV-DEC-1</cbc:ID>
        </cac:SuppliedEvidence>
      </cac:Declaration>
      <cac:Party>
        <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
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
        <cac:Language>
          <cbc:ID schemeID="ISO 639">qau</cbc:ID>
          <cbc:Name>Urvanian</cbc:Name>
        </cac:Language>
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
          <cbc:Region>Province of Ferrano</cbc:Region>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007299291</cbc:CompanyID>
          <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
            <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
            <cac:JurisdictionRegionAddress>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
          <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
          <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
          <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
          <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
          <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
          <cac:RegistrationAddress>
            <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
            <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:RegistrationAddress>
          <cac:CorporateRegistrationScheme>
            <cbc:ID>XU:CR</cbc:ID>
            <cbc:Name>Commercial register of Urvania</cbc:Name>
            <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
            <cac:JurisdictionRegionAddress>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:CorporateRegistrationScheme>
          <cac:SecurityListing>
            <cbc:ID schemeID="ISO 6166">XU0001042501</cbc:ID>
            <cbc:Description>Ordinary shares of Valdara Industries</cbc:Description>
            <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
            <cbc:MarketCode listID="urn:ubl-examples:world:codelist:MarketCode">XFER</cbc:MarketCode>
          </cac:SecurityListing>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Order desk</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
          <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
          <cac:OtherCommunication>
            <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
            <cbc:Value>+999 1 344 474 4274</cbc:Value>
          </cac:OtherCommunication>
        </cac:Contact>
        <cac:ServiceProviderParty>
          <cbc:ID>VI-SP-2026-01</cbc:ID>
          <cbc:ServiceTypeCode listID="urn:ubl-examples:world:codelist:ServiceTypeCode">LOGISTICS</cbc:ServiceTypeCode>
          <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
          <cac:Party>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Castrano Logistics</cbc:Name>
            </cac:PartyName>
          </cac:Party>
          <cac:SellerContact>
            <cbc:Name>Key account desk</cbc:Name>
          </cac:SellerContact>
        </cac:ServiceProviderParty>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:Party>
      <cac:EconomicOperatorRole>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EconomicOperatorRoleCode">LEAD</cbc:RoleCode>
        <cbc:RoleDescription>Leads.</cbc:RoleDescription>
      </cac:EconomicOperatorRole>
    </cac:MainQualifyingParty>
    <cac:AdditionalQualifyingParty>
      <cbc:ParticipationPercent>20</cbc:ParticipationPercent>
      <cbc:TendererRoleCode listID="urn:ubl-examples:world:codelist:TendererRoleCode">SUBCONTRACTOR</cbc:TendererRoleCode>
      <cac:Party>
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
      </cac:Party>
    </cac:AdditionalQualifyingParty>
  </cac:TendererPartyQualification>
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
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-000417</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
        <cbc:Department>Procurement office</cbc:Department>
        <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-0900002</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cbc:ExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">PUBLIC</cbc:ExemptionReasonCode>
        <cbc:ExemptionReason>Sale to a public body: public bodies are exempt from the state sales tax</cbc:ExemptionReason>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
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
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:CompanyID>
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
  <cac:Evidence>
    <cbc:ID>EV-FER-PARKS</cbc:ID>
    <cbc:Name>Ferrano reference</cbc:Name>
  </cac:Evidence>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-ESPD-26</cbc:ID>
  </cac:AdditionalDocumentReference>
</TendererQualification>
```
