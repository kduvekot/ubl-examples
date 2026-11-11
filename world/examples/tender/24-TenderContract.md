# Tender Contract: Lumeport Public Works Department to Valdara Industries

*Example 24 of the flow "A public tender (Bayvarra)" · [Tender Contract in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TENDER-CONTRACT-SCHEMA)*

After the standstill period the authority and the manufacturer conclude the contract.

[The XML file](24-TenderContract.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **LPWD-DOC-26-0210**  
  The sender's number for this document.
- `UUID` = **14fc43bd-7919-515f-82c7-a02bb3605891**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-19**  
  Concluded after the ten-day standstill period.
- `IssueTime` = **17:24:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ContractName` = **Park benches for the parks renewal programme**  
  The name of the contract the procedure is for.
- `Note` = **The framework contract, signed by both parties.**  
  What.
- `RegulatoryDomain` = **Bayvarra public procurement**  
  The rules the contract follows.
- `PublishAwardIndicator` = **true**  
  The award was published.

### Previous Document Reference

Inside `PreviousDocumentReference`:

- `ID` = **LPWD-DOC-26-0208**  
  The award notification.

### Contract Document Reference

Inside `ContractDocumentReference`:

- `ID` = **PWD-CONTRACT-2026-PARKS**  
  The signed contract.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-CONTRACT**  
  The department's seal.
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **VI-SIG-CONTRACT**  
  The manufacturer's seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

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
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
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
- `Party/Contact/Telephone` = **+999 2 3851 0548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeport Public Works Department (world/parties.json).
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

- `Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Party/PartyLegalEntity/SecurityListing/ID` = **XU0001042505**  
  The identifier of the listed shares, in the form of an ISIN with the world's country code.
- `Party/PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `Party/PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The regulated market where the shares are listed.
- `Party/PartyLegalEntity/SecurityListing/MarketCode` = **FSE**  
  The market's code.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ServiceProviderParty/ID` = **5-xu-SP-8-xu**  
  The service contract between the two.
- `Party/ServiceProviderParty/ServiceTypeCode` = **Logistics**  
  The kind of service, as a code.
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Tendering Terms

Inside `TenderingTerms`:

- `AwardingMethodTypeCode` = **BestValue**  
  The best price-quality ratio.
- `PriceEvaluationCode` = **UnitPrice**  
  Evaluated on the unit prices.
- `MaximumVariantQuantity` = **1**  
  One variant allowed.
- `VariantConstraintIndicator` = **true**  
  Variants are allowed.
- `AcceptedVariantsDescription` = **A bench of recycled plastic slats.**  
  The variant allowed.
- `VariantConstraintCode` = **Allowed**  
  As a code.
- `PriceRevisionFormulaDescription` = **Steel index each January.**  
  How prices change.
- `FundingProgramCode` = **PARKS-26**  
  The programme.
- `FundingProgram` = **Parks renewal programme 2026**  
  In words.
- `MaximumAdvertisementAmount` = **500.00** (currencyID `XBL`)  
  The most the winner pays for publication.
- `Note` = **Questions through the platform only.**  
  How to ask.
- `PaymentFrequencyCode` = **PerRelease**  
  Payment after each release.
- `EconomicOperatorRegistryURI` = **https://register.bayvarra.example**  
  Where tenderers are registered.
- `RequiredCurriculaIndicator` = **true**  
  The installers' qualifications are asked.
- `RequiredCurriculaCode` = **Installers**  
  For lot 2.
- `OtherConditionsIndicator` = **true**  
  There are other conditions.
- `RecurringProcurementIndicator` = **true**  
  The parks are renewed every few years.
- `RecurringProcurementDescription` = **A next procedure in about four years.**  
  When.
- `EstimatedTimingFurtherPublication` = **2030**  
  The next notice.
- `AdditionalConditions` = **Benches must carry the maker's serial number.**  
  A condition.
- `LatestSecurityClearanceDate` = **2026-02-21**  
  No clearance is needed; the date is the latest for site access passes.
- `DocumentationFeeAmount` = **50.00** (currencyID `XBL`)  
  For paper documents.
- `MultipleTendersCode` = **NotAllowed**  
  One tender per tenderer.
- `PenaltyClause/ID` = **PEN-1**  
  Late delivery.
- `PenaltyClause/Content` = **0.5 % per day late, at most 10 %.**  
  The penalty.
- `RequiredFinancialGuarantee/GuaranteeTypeCode` = **TenderGuarantee**  
  A tender guarantee.
- `RequiredFinancialGuarantee/Description` = **A bank guarantee for the tender.**  
  What.
- `RequiredFinancialGuarantee/LiabilityAmount` = **2400.00** (currencyID `XBL`)  
  Its amount.
- `RequiredFinancialGuarantee/AmountRate` = **2**  
  2 % of the estimated value of 120,000 lume.
- `RequiredFinancialGuarantee/ConstitutionPeriod/EndDate` = **2026-02-26**  
  With the tender.
- `ProcurementLegislationDocumentReference/ID` = **XB-PPA-2019**  
  Bayvarra's public procurement act.
- `FiscalLegislationDocumentReference/ID` = **XB-STT-ACT**  
  The state sales tax acts.
- `EnvironmentalLegislationDocumentReference/ID` = **XB-ENV-2021**  
  The environmental act.
- `EmploymentLegislationDocumentReference/ID` = **XB-LAB-2018**  
  The labour act.
- `ContractualDocumentReference/ID` = **PWD-CONTRACT-DRAFT**  
  The draft framework contract.
- `CallForTendersDocumentReference/ID` = **PWD-2026-PARKS-CFT**  
  The call for tenders.
- `WarrantyValidityPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `PaymentTerms/Note` = **30 days after each accepted release.**  
  The terms.
- `TendererQualificationRequest/CompanyLegalFormCode` = **Any**  
  Any legal form.
- `TendererQualificationRequest/CompanyLegalForm` = **Consortia must name a lead member.**  
  The rule.
- `TendererQualificationRequest/PersonalSituation` = **No exclusion grounds.**  
  The tenderer's situation.
- `TendererQualificationRequest/OperatingYearsQuantity` = **3** (unitCode `ANN`)  
  At least three years in business.
- `TendererQualificationRequest/EmployeeQuantity` = **10** (unitCode `C62`)  
  At least ten employees.
- `TendererQualificationRequest/Description` = **Economic and technical capacity.**  
  What is asked.
- `TendererQualificationRequest/RequiredBusinessClassificationScheme/ID` = **ISIC4**  
  ISIC Rev. 4.
- `TendererQualificationRequest/RequiredBusinessClassificationScheme/Name` = **ISIC Rev. 4**  
  The classification.
- `TendererQualificationRequest/RequiredBusinessClassificationScheme/ClassificationCategory/Name` = **Manufacture of furniture**  
  In words.
- `TendererQualificationRequest/RequiredBusinessClassificationScheme/ClassificationCategory/CodeValue` = **3100**  
  Furniture manufacture.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/EvaluationCriterionTypeCode` = **References**  
  References.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/Description` = **Three similar supplies in five years.**  
  What.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/ThresholdQuantity` = **3** (unitCode `C62`)  
  Three.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/DurationPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/SuggestedEvidence/ID` = **EV-REF**  
  Reference letters.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/SuggestedEvidence/Name` = **References**  
  What.
- `TendererQualificationRequest/FinancialEvaluationCriterion/EvaluationCriterionTypeCode` = **Turnover**  
  Turnover.
- `TendererQualificationRequest/FinancialEvaluationCriterion/Description` = **Yearly turnover of at least twice the estimate.**  
  What.
- `TendererQualificationRequest/FinancialEvaluationCriterion/ThresholdAmount` = **250000.00** (currencyID `XBL`)  
  The minimum.
- `TendererQualificationRequest/FinancialEvaluationCriterion/ExpressionCode` = **GreaterThan**  
  As a rule.
- `TendererQualificationRequest/FinancialEvaluationCriterion/Expression` = **Turnover > 2 × estimate**  
  The formula.
- `TendererQualificationRequest/SpecificTendererRequirement/Name` = **Certified timber**  
  The requirement.
- `TendererQualificationRequest/SpecificTendererRequirement/TendererRequirementTypeCode` = **Environmental**  
  Its kind.
- `TendererQualificationRequest/SpecificTendererRequirement/Description` = **Slats from forests managed for regrowth.**  
  What.
- `TendererQualificationRequest/SpecificTendererRequirement/LegalReference` = **XB-ENV-2021 art. 12**  
  The rule.
- `TendererQualificationRequest/SpecificTendererRequirement/SuggestedEvidence/ID` = **EV-FOR**  
  A forestry certificate.
- `TendererQualificationRequest/SpecificTendererRequirement/SuggestedEvidence/Name` = **Forestry certificate**  
  What.
- `TendererQualificationRequest/EconomicOperatorRole/RoleCode` = **Lead**  
  The lead tenderer.
- `TendererQualificationRequest/EconomicOperatorRole/RoleDescription` = **Leads a consortium.**  
  In words.
- `AllowedSubcontractTerms/Rate` = **30**  
  Up to 30 % subcontracted.
- `AllowedSubcontractTerms/UnknownPriceIndicator` = **false**  
  The subcontracting share is known.
- `AllowedSubcontractTerms/Description` = **Installation may be subcontracted.**  
  What.
- `AllowedSubcontractTerms/Amount` = **4320.00** (currencyID `XBL`)  
  Lot 2's value.
- `AllowedSubcontractTerms/SubcontractingConditionsCode` = **Allowed**  
  As a code.
- `AllowedSubcontractTerms/MaximumPercent` = **30**  
  At most.
- `AllowedSubcontractTerms/MinimumPercent` = **0**  
  At least.
- `TenderPreparation/TenderEnvelopeID` = **ENV-1**  
  One envelope.
- `TenderPreparation/TenderEnvelopeTypeCode` = **Combined**  
  Technical and price together.
- `TenderPreparation/Description` = **One encrypted envelope per tender.**  
  How.
- `TenderPreparation/OpenTenderID` = **OPEN-1**  
  Opened at the opening.
- `TenderPreparation/ProcurementProjectLot/ID` = **LOT-1**  
  For lot 1 and lot 2 alike.
- `TenderPreparation/DocumentTenderRequirement/Name` = **Price schedule**  
  A document to submit.
- `TenderPreparation/DocumentTenderRequirement/Description` = **Unit prices per lot.**  
  What.
- `TenderPreparation/DocumentTenderRequirement/TemplateDocumentReference/ID` = **PWD-PRICE-TPL**  
  The template.
- `TenderPreparation/TenderEncryptionData/MessageFormat` = **CMS**  
  Cryptographic Message Syntax.
- `TenderPreparation/TenderEncryptionData/EncryptionCertificateAttachment/ExternalReference/URI` = **https://tenders.lumeport.example/cert.pem**  
  The certificate.
- `TenderPreparation/TenderEncryptionData/EncryptionCertificatePathChain/Value` = **PWD-CA > PWD-TENDER**  
  The chain.
- `TenderPreparation/TenderEncryptionData/EncryptionCertificatePathChain/URI` = **https://tenders.lumeport.example/chain.pem**  
  Where.
- `TenderPreparation/TenderEncryptionData/EncryptionSymmetricAlgorithm/ID` = **AES-256-GCM**  
  The algorithm.
- `TenderPreparation/TenderEncryptionData/EncryptionSymmetricAlgorithm/OID` = **2.16.840.1.101.3.4.1.46**  
  Its OID.
- `ContractExecutionRequirement/Name` = **Recycled steel**  
  A condition of execution.
- `ContractExecutionRequirement/ExecutionRequirementCode` = **Environmental**  
  Its kind.
- `ContractExecutionRequirement/Description` = **At least 30 % recycled steel in the frames.**  
  What.
- `AwardingTerms/WeightingAlgorithmCode` = **WeightedSum**  
  A weighted sum.
- `AwardingTerms/Description` = **Price 60 %, quality 40 %.**  
  The award.
- `AwardingTerms/TechnicalCommitteeDescription` = **Three officers of the department.**  
  Who evaluates.
- `AwardingTerms/LowTendersDescription` = **Prices 30 % below the average are examined.**  
  Abnormally low.
- `AwardingTerms/PrizeIndicator` = **false**  
  Not a design contest.
- `AwardingTerms/PrizeDescription` = **None.**  
  No prize.
- `AwardingTerms/PaymentDescription` = **No payment for tendering.**  
  None.
- `AwardingTerms/FollowupContractIndicator` = **false**  
  No follow-up contract.
- `AwardingTerms/BindingOnBuyerIndicator` = **true**  
  The evaluation binds the buyer.
- `AwardingTerms/NoFurtherNegotiationIndicator` = **true**  
  No negotiation after the award.
- `AwardingTerms/AwardingCriterion/ID` = **AC-1**  
  Price.
- `AwardingTerms/AwardingCriterion/AwardingCriterionTypeCode` = **Price**  
  Its kind.
- `AwardingTerms/AwardingCriterion/Name` = **Price**  
  Name.
- `AwardingTerms/AwardingCriterion/Description` = **The lowest total of unit prices.**  
  How.
- `AwardingTerms/AwardingCriterion/WeightNumeric` = **60**  
  Weight.
- `AwardingTerms/AwardingCriterion/Weight` = **60 %**  
  In words.
- `AwardingTerms/AwardingCriterion/CalculationExpression` = **60 × lowest / tendered**  
  The formula.
- `AwardingTerms/AwardingCriterion/CalculationExpressionCode` = **Inverse**  
  As a code.
- `AwardingTerms/AwardingCriterion/MinimumAmount` = **350.00** (currencyID `XBL`)  
  Unit price at least.
- `AwardingTerms/AwardingCriterion/MaximumAmount` = **600.00** (currencyID `XBL`)  
  At most.
- `AwardingTerms/AwardingCriterion/MinimumImprovementBid` = **Not applicable: no auction.**  
  Stated.
- `AwardingTerms/AwardingCriterion/ID` = **AC-2**  
  Quality.
- `AwardingTerms/AwardingCriterion/AwardingCriterionTypeCode` = **Quality**  
  Its kind.
- `AwardingTerms/AwardingCriterion/Name` = **Quality**  
  Name.
- `AwardingTerms/AwardingCriterion/WeightNumeric` = **40**  
  Weight.
- `AwardingTerms/AwardingCriterion/MinimumQuantity` = **5** (unitCode `ANN`)  
  Warranty of at least five years.
- `AwardingTerms/AwardingCriterion/MaximumQuantity` = **10** (unitCode `ANN`)  
  Up to ten years counts.
- `AwardingTerms/AwardingCriterion/SubordinateAwardingCriterion/ID` = **AC-2.1**  
  Durability.
- `AwardingTerms/AwardingCriterion/SubordinateAwardingCriterion/Name` = **Durability of the coating**  
  Name.
- `AwardingTerms/AwardingCriterion/SubordinateAwardingCriterion/WeightNumeric` = **20**  
  Half of quality.
- `AwardingTerms/TechnicalCommitteePerson/FirstName` = **Mara**  
  The head of parks on the committee.
- `AwardingTerms/TechnicalCommitteePerson/FamilyName` = **Delling**  
  The family name.
- `AwardingTerms/TechnicalCommitteePerson/JobTitle` = **Head of parks**  
  The person's position.
- `AwardingTerms/Prize/RankCode` = **None**  
  No prizes in a tender.
- `AwardingTerms/Prize/ValueAmount` = **0.00** (currencyID `XBL`)  
  No prize money.
- `AwardingTerms/Prize/Description` = **Not a contest.**  
  Why.
- `AdditionalInformationParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AdditionalInformationParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `DocumentProviderParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DocumentProviderParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderRecipientParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderRecipientParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `ContractResponsibleParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ContractResponsibleParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderEvaluationParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderEvaluationParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `QualificationRequestRecipientParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `QualificationRequestRecipientParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderValidityPeriod/DurationMeasure` = **90** (unitCode `DAY`)  
  Tenders hold for 90 days.
- `ContractAcceptancePeriod/DurationMeasure` = **10** (unitCode `DAY`)  
  The standstill: ten days.
- `AppealTerms/Description` = **Appeals to the review board within ten days of the award.**  
  How.
- `AppealTerms/PresentationPeriod/DurationMeasure` = **10** (unitCode `DAY`)  
  Ten days.
- `AppealTerms/AppealInformationParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AppealTerms/AppealInformationParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.
- `Language/ID` = **en**  
  English.
- `Language/Name` = **English**  
  In words.
- `Language/LocaleCode` = **EN**  
  As an ISO 639 code.
- `BudgetAccountLine/ID` = **BL-PARKS-26**  
  The budget line.
- `BudgetAccountLine/TotalAmount` = **124080.00** (currencyID `XBL`)  
  Its amount.
- `BudgetAccountLine/BudgetAccount/ID` = **4.2.110**  
  The city's budget account.
- `BudgetAccountLine/BudgetAccount/BudgetYearNumeric` = **2026**  
  The budget year.
- `BudgetAccountLine/BudgetAccount/RequiredClassificationScheme/ID` = **LUM-BUDGET**  
  The city's budget classification.
- `BudgetAccountLine/BudgetAccount/RequiredClassificationScheme/ClassificationCategory/Name` = **Parks**  
  In words.
- `BudgetAccountLine/BudgetAccount/RequiredClassificationScheme/ClassificationCategory/CodeValue` = **4.2**  
  Parks and green spaces.
- `ReplacedNoticeDocumentReference/ID` = **PWD-2026-PARKS-PIN**  
  The prior information notice this notice follows.
- `LotDistribution/MaximumLotsAwardedNumeric` = **2**  
  Both lots to one tenderer if best.
- `LotDistribution/MaximumLotsSubmittedNumeric` = **2**  
  Tenders for both lots allowed.
- `LotDistribution/GroupingLots` = **Lots 1 and 2 may be awarded together.**  
  The grouping.
- `LotDistribution/LotsGroup/LotsGroupID` = **G-1**  
  The group.
- `LotDistribution/LotsGroup/ProcurementProjectLotReference/ID` = **LOT-1**  
  Lot 1 of the procedure.
- `LotDistribution/LotsGroup/ProcurementProjectLotReference/ID` = **LOT-2**  
  Lot 2 of the procedure.
- `PostAwardProcess/ElectronicCatalogueUsageIndicator` = **true**  
  A catalogue of the benches.
- `PostAwardProcess/ElectronicInvoiceAcceptedIndicator` = **true**  
  Invoices in UBL.
- `PostAwardProcess/ElectronicOrderUsageIndicator` = **true**  
  Call-offs as UBL orders.
- `PostAwardProcess/ElectronicPaymentUsageIndicator` = **true**  
  Paid by transfer.
- `EconomicOperatorShortList/LimitationDescription` = **No short list.**  
  An open procedure.
- `SecurityClearanceTerm/Code` = **None**  
  No security clearance.
- `SecurityClearanceTerm/Description` = **Parks are public places.**  
  Why.

### Tendering Process

Inside `TenderingProcess`:

- `ID` = **PWD-2026-PARKS-P**  
  The procedure.
- `ProcedureCode` = **Open**  
  Open.

### Procurement Project

Inside `ProcurementProject`:

- `Name` = **Park benches for the city parks**  
  The project, or the lot, the document is about.
- `ProcurementTypeCode` = **Supplies**  
  The kind of procurement.

### Procurement Project Lot

Inside `ProcurementProjectLot`:

- `ID` = **LOT-1**  
  Lot 1.
- `ID` = **LOT-2**  
  Lot 2.

### Tender Result

Inside `TenderResult`:

- `AwardID` = **PWD-2026-PARKS-AWARD-1**  
  The award decision.
- `TenderResultCode` = **Awarded**  
  The contract is awarded.
- `Description` = **Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.**  
  Why it won.
- `AdvertisementAmount` = **320.00** (currencyID `XBL`)  
  What the winner pays for publishing the notice, below the maximum of 500 lume.
- `AwardDate` = **2026-03-09**  
  The day of the award decision.
- `AwardTime` = **09:30:00**  
  The time of the decision, before the tenderers are told.
- `ReceivedTenderQuantity` = **2** (unitCode `C62`)  
  Two tenders: the furniture maker's first tender was withdrawn and replaced.
- `LowerTenderAmount` = **119040.00** (currencyID `XBL`)  
  The lowest tender, the furniture maker's.
- `HigherTenderAmount` = **124080.00** (currencyID `XBL`)  
  The highest, the manufacturer's.
- `StartDate` = **2026-03-23**  
  The contract starts with the first call-off.
- `ReceivedElectronicTenderQuantity` = **2** (unitCode `C62`)  
  Both through the platform.
- `ReceivedForeignTenderQuantity` = **1** (unitCode `C62`)  
  The manufacturer is established in Urvania.
- `Contract/ID` = **PWD-2026-PARKS**  
  The framework contract.
- `Contract/ContractTypeCode` = **Framework**  
  A framework contract.
- `Contract/ValidityPeriod/StartDate` = **2026-03-23**  
  From the first call-off.
- `Contract/ValidityPeriod/DurationMeasure` = **24** (unitCode `MON`)  
  Two years.
- `AwardedTenderedProject/VariantID` = **V0**  
  The main offer.
- `AwardedTenderedProject/ProcurementProjectLot/ID` = **LOT-1**  
  Lot 1 of the procedure.
- `AwardedTenderedProject/ProcurementProjectLot/ID` = **LOT-2**  
  Lot 2 of the procedure.
- `AwardedTenderedProject/LegalMonetaryTotal/PayableAmount` = **124080.00** (currencyID `XBL`)  
  240 benches at 499 lume and their installation at 18 lume each.
- `ContractFormalizationPeriod/StartDate` = **2026-03-19**  
  After the standstill period.
- `ContractFormalizationPeriod/EndDate` = **2026-03-22**  
  Before the first call-off.
- `SubcontractTerms/Rate` = **0**  
  The manufacturer installs with its own staff.
- `SubcontractTerms/UnknownPriceIndicator` = **false**  
  Nothing is subcontracted.
- `SubcontractTerms/Description` = **No subcontracting.**  
  The tender's terms.
- `WinningParty/Rank` = **1**  
  First in the evaluation.
- `WinningParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `WinningParty/Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TenderContract xmlns="urn:oasis:names:specification:ubl:schema:xsd:TenderContract-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:tender</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0210</cbc:ID>
  <cbc:UUID>14fc43bd-7919-515f-82c7-a02bb3605891</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-19</cbc:IssueDate>
  <cbc:IssueTime>17:24:00</cbc:IssueTime>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:Note>The framework contract, signed by both parties.</cbc:Note>
  <cbc:RegulatoryDomain>Bayvarra public procurement</cbc:RegulatoryDomain>
  <cbc:PublishAwardIndicator>true</cbc:PublishAwardIndicator>
  <cac:PreviousDocumentReference>
    <cbc:ID>LPWD-DOC-26-0208</cbc:ID>
  </cac:PreviousDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>PWD-CONTRACT-2026-PARKS</cbc:ID>
  </cac:ContractDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-CONTRACT</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:Signature>
    <cbc:ID>VI-SIG-CONTRACT</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
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
        <cbc:Telephone>+999 2 3851 0548</cbc:Telephone>
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
      <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
        <cbc:StreetName languageID="en">Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en">Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007299291</cbc:CompanyID>
        <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
          <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
        <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
        <cac:SecurityListing>
          <cbc:ID>XU0001042505</cbc:ID>
          <cbc:Description>Ordinary shares of Valdara Industries</cbc:Description>
          <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
          <cbc:MarketCode>FSE</cbc:MarketCode>
        </cac:SecurityListing>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4120 4274</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode>AL</cbc:ChannelCode>
          <cbc:Value>+999 1 7000 4274</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
      <cac:ServiceProviderParty>
        <cbc:ID>5-xu-SP-8-xu</cbc:ID>
        <cbc:ServiceTypeCode>Logistics</cbc:ServiceTypeCode>
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
  </cac:EconomicOperatorParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:TenderingTerms>
    <cbc:AwardingMethodTypeCode>BestValue</cbc:AwardingMethodTypeCode>
    <cbc:PriceEvaluationCode>UnitPrice</cbc:PriceEvaluationCode>
    <cbc:MaximumVariantQuantity>1</cbc:MaximumVariantQuantity>
    <cbc:VariantConstraintIndicator>true</cbc:VariantConstraintIndicator>
    <cbc:AcceptedVariantsDescription>A bench of recycled plastic slats.</cbc:AcceptedVariantsDescription>
    <cbc:VariantConstraintCode>Allowed</cbc:VariantConstraintCode>
    <cbc:PriceRevisionFormulaDescription>Steel index each January.</cbc:PriceRevisionFormulaDescription>
    <cbc:FundingProgramCode>PARKS-26</cbc:FundingProgramCode>
    <cbc:FundingProgram>Parks renewal programme 2026</cbc:FundingProgram>
    <cbc:MaximumAdvertisementAmount currencyID="XBL">500.00</cbc:MaximumAdvertisementAmount>
    <cbc:Note>Questions through the platform only.</cbc:Note>
    <cbc:PaymentFrequencyCode>PerRelease</cbc:PaymentFrequencyCode>
    <cbc:EconomicOperatorRegistryURI>https://register.bayvarra.example</cbc:EconomicOperatorRegistryURI>
    <cbc:RequiredCurriculaIndicator>true</cbc:RequiredCurriculaIndicator>
    <cbc:RequiredCurriculaCode>Installers</cbc:RequiredCurriculaCode>
    <cbc:OtherConditionsIndicator>true</cbc:OtherConditionsIndicator>
    <cbc:RecurringProcurementIndicator>true</cbc:RecurringProcurementIndicator>
    <cbc:RecurringProcurementDescription>A next procedure in about four years.</cbc:RecurringProcurementDescription>
    <cbc:EstimatedTimingFurtherPublication>2030</cbc:EstimatedTimingFurtherPublication>
    <cbc:AdditionalConditions>Benches must carry the maker's serial number.</cbc:AdditionalConditions>
    <cbc:LatestSecurityClearanceDate>2026-02-21</cbc:LatestSecurityClearanceDate>
    <cbc:DocumentationFeeAmount currencyID="XBL">50.00</cbc:DocumentationFeeAmount>
    <cbc:MultipleTendersCode>NotAllowed</cbc:MultipleTendersCode>
    <cac:PenaltyClause>
      <cbc:ID>PEN-1</cbc:ID>
      <cbc:Content>0.5 % per day late, at most 10 %.</cbc:Content>
    </cac:PenaltyClause>
    <cac:RequiredFinancialGuarantee>
      <cbc:GuaranteeTypeCode>TenderGuarantee</cbc:GuaranteeTypeCode>
      <cbc:Description>A bank guarantee for the tender.</cbc:Description>
      <cbc:LiabilityAmount currencyID="XBL">2400.00</cbc:LiabilityAmount>
      <cbc:AmountRate>2</cbc:AmountRate>
      <cac:ConstitutionPeriod>
        <cbc:EndDate>2026-02-26</cbc:EndDate>
      </cac:ConstitutionPeriod>
    </cac:RequiredFinancialGuarantee>
    <cac:ProcurementLegislationDocumentReference>
      <cbc:ID>XB-PPA-2019</cbc:ID>
    </cac:ProcurementLegislationDocumentReference>
    <cac:FiscalLegislationDocumentReference>
      <cbc:ID>XB-STT-ACT</cbc:ID>
    </cac:FiscalLegislationDocumentReference>
    <cac:EnvironmentalLegislationDocumentReference>
      <cbc:ID>XB-ENV-2021</cbc:ID>
    </cac:EnvironmentalLegislationDocumentReference>
    <cac:EmploymentLegislationDocumentReference>
      <cbc:ID>XB-LAB-2018</cbc:ID>
    </cac:EmploymentLegislationDocumentReference>
    <cac:ContractualDocumentReference>
      <cbc:ID>PWD-CONTRACT-DRAFT</cbc:ID>
    </cac:ContractualDocumentReference>
    <cac:CallForTendersDocumentReference>
      <cbc:ID>PWD-2026-PARKS-CFT</cbc:ID>
    </cac:CallForTendersDocumentReference>
    <cac:WarrantyValidityPeriod>
      <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
    </cac:WarrantyValidityPeriod>
    <cac:PaymentTerms>
      <cbc:Note>30 days after each accepted release.</cbc:Note>
    </cac:PaymentTerms>
    <cac:TendererQualificationRequest>
      <cbc:CompanyLegalFormCode>Any</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Consortia must name a lead member.</cbc:CompanyLegalForm>
      <cbc:PersonalSituation>No exclusion grounds.</cbc:PersonalSituation>
      <cbc:OperatingYearsQuantity unitCode="ANN">3</cbc:OperatingYearsQuantity>
      <cbc:EmployeeQuantity unitCode="C62">10</cbc:EmployeeQuantity>
      <cbc:Description>Economic and technical capacity.</cbc:Description>
      <cac:RequiredBusinessClassificationScheme>
        <cbc:ID>ISIC4</cbc:ID>
        <cbc:Name>ISIC Rev. 4</cbc:Name>
        <cac:ClassificationCategory>
          <cbc:Name>Manufacture of furniture</cbc:Name>
          <cbc:CodeValue>3100</cbc:CodeValue>
        </cac:ClassificationCategory>
      </cac:RequiredBusinessClassificationScheme>
      <cac:TechnicalEvaluationCriterion>
        <cbc:EvaluationCriterionTypeCode>References</cbc:EvaluationCriterionTypeCode>
        <cbc:Description>Three similar supplies in five years.</cbc:Description>
        <cbc:ThresholdQuantity unitCode="C62">3</cbc:ThresholdQuantity>
        <cac:DurationPeriod>
          <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
        </cac:DurationPeriod>
        <cac:SuggestedEvidence>
          <cbc:ID>EV-REF</cbc:ID>
          <cbc:Name>References</cbc:Name>
        </cac:SuggestedEvidence>
      </cac:TechnicalEvaluationCriterion>
      <cac:FinancialEvaluationCriterion>
        <cbc:EvaluationCriterionTypeCode>Turnover</cbc:EvaluationCriterionTypeCode>
        <cbc:Description>Yearly turnover of at least twice the estimate.</cbc:Description>
        <cbc:ThresholdAmount currencyID="XBL">250000.00</cbc:ThresholdAmount>
        <cbc:ExpressionCode>GreaterThan</cbc:ExpressionCode>
        <cbc:Expression>Turnover &gt; 2 × estimate</cbc:Expression>
      </cac:FinancialEvaluationCriterion>
      <cac:SpecificTendererRequirement>
        <cbc:Name>Certified timber</cbc:Name>
        <cbc:TendererRequirementTypeCode>Environmental</cbc:TendererRequirementTypeCode>
        <cbc:Description>Slats from forests managed for regrowth.</cbc:Description>
        <cbc:LegalReference>XB-ENV-2021 art. 12</cbc:LegalReference>
        <cac:SuggestedEvidence>
          <cbc:ID>EV-FOR</cbc:ID>
          <cbc:Name>Forestry certificate</cbc:Name>
        </cac:SuggestedEvidence>
      </cac:SpecificTendererRequirement>
      <cac:EconomicOperatorRole>
        <cbc:RoleCode>Lead</cbc:RoleCode>
        <cbc:RoleDescription>Leads a consortium.</cbc:RoleDescription>
      </cac:EconomicOperatorRole>
    </cac:TendererQualificationRequest>
    <cac:AllowedSubcontractTerms>
      <cbc:Rate>30</cbc:Rate>
      <cbc:UnknownPriceIndicator>false</cbc:UnknownPriceIndicator>
      <cbc:Description>Installation may be subcontracted.</cbc:Description>
      <cbc:Amount currencyID="XBL">4320.00</cbc:Amount>
      <cbc:SubcontractingConditionsCode>Allowed</cbc:SubcontractingConditionsCode>
      <cbc:MaximumPercent>30</cbc:MaximumPercent>
      <cbc:MinimumPercent>0</cbc:MinimumPercent>
    </cac:AllowedSubcontractTerms>
    <cac:TenderPreparation>
      <cbc:TenderEnvelopeID>ENV-1</cbc:TenderEnvelopeID>
      <cbc:TenderEnvelopeTypeCode>Combined</cbc:TenderEnvelopeTypeCode>
      <cbc:Description>One encrypted envelope per tender.</cbc:Description>
      <cbc:OpenTenderID>OPEN-1</cbc:OpenTenderID>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-1</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:DocumentTenderRequirement>
        <cbc:Name>Price schedule</cbc:Name>
        <cbc:Description>Unit prices per lot.</cbc:Description>
        <cac:TemplateDocumentReference>
          <cbc:ID>PWD-PRICE-TPL</cbc:ID>
        </cac:TemplateDocumentReference>
      </cac:DocumentTenderRequirement>
      <cac:TenderEncryptionData>
        <cbc:MessageFormat>CMS</cbc:MessageFormat>
        <cac:EncryptionCertificateAttachment>
          <cac:ExternalReference>
            <cbc:URI>https://tenders.lumeport.example/cert.pem</cbc:URI>
          </cac:ExternalReference>
        </cac:EncryptionCertificateAttachment>
        <cac:EncryptionCertificatePathChain>
          <cbc:Value>PWD-CA &gt; PWD-TENDER</cbc:Value>
          <cbc:URI>https://tenders.lumeport.example/chain.pem</cbc:URI>
        </cac:EncryptionCertificatePathChain>
        <cac:EncryptionSymmetricAlgorithm>
          <cbc:ID>AES-256-GCM</cbc:ID>
          <cbc:OID>2.16.840.1.101.3.4.1.46</cbc:OID>
        </cac:EncryptionSymmetricAlgorithm>
      </cac:TenderEncryptionData>
    </cac:TenderPreparation>
    <cac:ContractExecutionRequirement>
      <cbc:Name>Recycled steel</cbc:Name>
      <cbc:ExecutionRequirementCode>Environmental</cbc:ExecutionRequirementCode>
      <cbc:Description>At least 30 % recycled steel in the frames.</cbc:Description>
    </cac:ContractExecutionRequirement>
    <cac:AwardingTerms>
      <cbc:WeightingAlgorithmCode>WeightedSum</cbc:WeightingAlgorithmCode>
      <cbc:Description>Price 60 %, quality 40 %.</cbc:Description>
      <cbc:TechnicalCommitteeDescription>Three officers of the department.</cbc:TechnicalCommitteeDescription>
      <cbc:LowTendersDescription>Prices 30 % below the average are examined.</cbc:LowTendersDescription>
      <cbc:PrizeIndicator>false</cbc:PrizeIndicator>
      <cbc:PrizeDescription>None.</cbc:PrizeDescription>
      <cbc:PaymentDescription>No payment for tendering.</cbc:PaymentDescription>
      <cbc:FollowupContractIndicator>false</cbc:FollowupContractIndicator>
      <cbc:BindingOnBuyerIndicator>true</cbc:BindingOnBuyerIndicator>
      <cbc:NoFurtherNegotiationIndicator>true</cbc:NoFurtherNegotiationIndicator>
      <cac:AwardingCriterion>
        <cbc:ID>AC-1</cbc:ID>
        <cbc:AwardingCriterionTypeCode>Price</cbc:AwardingCriterionTypeCode>
        <cbc:Name>Price</cbc:Name>
        <cbc:Description>The lowest total of unit prices.</cbc:Description>
        <cbc:WeightNumeric>60</cbc:WeightNumeric>
        <cbc:Weight>60 %</cbc:Weight>
        <cbc:CalculationExpression>60 × lowest / tendered</cbc:CalculationExpression>
        <cbc:CalculationExpressionCode>Inverse</cbc:CalculationExpressionCode>
        <cbc:MinimumAmount currencyID="XBL">350.00</cbc:MinimumAmount>
        <cbc:MaximumAmount currencyID="XBL">600.00</cbc:MaximumAmount>
        <cbc:MinimumImprovementBid>Not applicable: no auction.</cbc:MinimumImprovementBid>
      </cac:AwardingCriterion>
      <cac:AwardingCriterion>
        <cbc:ID>AC-2</cbc:ID>
        <cbc:AwardingCriterionTypeCode>Quality</cbc:AwardingCriterionTypeCode>
        <cbc:Name>Quality</cbc:Name>
        <cbc:WeightNumeric>40</cbc:WeightNumeric>
        <cbc:MinimumQuantity unitCode="ANN">5</cbc:MinimumQuantity>
        <cbc:MaximumQuantity unitCode="ANN">10</cbc:MaximumQuantity>
        <cac:SubordinateAwardingCriterion>
          <cbc:ID>AC-2.1</cbc:ID>
          <cbc:Name>Durability of the coating</cbc:Name>
          <cbc:WeightNumeric>20</cbc:WeightNumeric>
        </cac:SubordinateAwardingCriterion>
      </cac:AwardingCriterion>
      <cac:TechnicalCommitteePerson>
        <cbc:FirstName>Mara</cbc:FirstName>
        <cbc:FamilyName>Delling</cbc:FamilyName>
        <cbc:JobTitle>Head of parks</cbc:JobTitle>
      </cac:TechnicalCommitteePerson>
      <cac:Prize>
        <cbc:RankCode>None</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">0.00</cbc:ValueAmount>
        <cbc:Description>Not a contest.</cbc:Description>
      </cac:Prize>
    </cac:AwardingTerms>
    <cac:AdditionalInformationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:AdditionalInformationParty>
    <cac:DocumentProviderParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:DocumentProviderParty>
    <cac:TenderRecipientParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:TenderRecipientParty>
    <cac:ContractResponsibleParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:ContractResponsibleParty>
    <cac:TenderEvaluationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:TenderEvaluationParty>
    <cac:QualificationRequestRecipientParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:QualificationRequestRecipientParty>
    <cac:TenderValidityPeriod>
      <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
    </cac:TenderValidityPeriod>
    <cac:ContractAcceptancePeriod>
      <cbc:DurationMeasure unitCode="DAY">10</cbc:DurationMeasure>
    </cac:ContractAcceptancePeriod>
    <cac:AppealTerms>
      <cbc:Description>Appeals to the review board within ten days of the award.</cbc:Description>
      <cac:PresentationPeriod>
        <cbc:DurationMeasure unitCode="DAY">10</cbc:DurationMeasure>
      </cac:PresentationPeriod>
      <cac:AppealInformationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
        </cac:PartyName>
      </cac:AppealInformationParty>
    </cac:AppealTerms>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:BudgetAccountLine>
      <cbc:ID>BL-PARKS-26</cbc:ID>
      <cbc:TotalAmount currencyID="XBL">124080.00</cbc:TotalAmount>
      <cac:BudgetAccount>
        <cbc:ID>4.2.110</cbc:ID>
        <cbc:BudgetYearNumeric>2026</cbc:BudgetYearNumeric>
        <cac:RequiredClassificationScheme>
          <cbc:ID>LUM-BUDGET</cbc:ID>
          <cac:ClassificationCategory>
            <cbc:Name>Parks</cbc:Name>
            <cbc:CodeValue>4.2</cbc:CodeValue>
          </cac:ClassificationCategory>
        </cac:RequiredClassificationScheme>
      </cac:BudgetAccount>
    </cac:BudgetAccountLine>
    <cac:ReplacedNoticeDocumentReference>
      <cbc:ID>PWD-2026-PARKS-PIN</cbc:ID>
    </cac:ReplacedNoticeDocumentReference>
    <cac:LotDistribution>
      <cbc:MaximumLotsAwardedNumeric>2</cbc:MaximumLotsAwardedNumeric>
      <cbc:MaximumLotsSubmittedNumeric>2</cbc:MaximumLotsSubmittedNumeric>
      <cbc:GroupingLots>Lots 1 and 2 may be awarded together.</cbc:GroupingLots>
      <cac:LotsGroup>
        <cbc:LotsGroupID>G-1</cbc:LotsGroupID>
        <cac:ProcurementProjectLotReference>
          <cbc:ID>LOT-1</cbc:ID>
        </cac:ProcurementProjectLotReference>
        <cac:ProcurementProjectLotReference>
          <cbc:ID>LOT-2</cbc:ID>
        </cac:ProcurementProjectLotReference>
      </cac:LotsGroup>
    </cac:LotDistribution>
    <cac:PostAwardProcess>
      <cbc:ElectronicCatalogueUsageIndicator>true</cbc:ElectronicCatalogueUsageIndicator>
      <cbc:ElectronicInvoiceAcceptedIndicator>true</cbc:ElectronicInvoiceAcceptedIndicator>
      <cbc:ElectronicOrderUsageIndicator>true</cbc:ElectronicOrderUsageIndicator>
      <cbc:ElectronicPaymentUsageIndicator>true</cbc:ElectronicPaymentUsageIndicator>
    </cac:PostAwardProcess>
    <cac:EconomicOperatorShortList>
      <cbc:LimitationDescription>No short list.</cbc:LimitationDescription>
    </cac:EconomicOperatorShortList>
    <cac:SecurityClearanceTerm>
      <cbc:Code>None</cbc:Code>
      <cbc:Description>Parks are public places.</cbc:Description>
    </cac:SecurityClearanceTerm>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:ID>PWD-2026-PARKS-P</cbc:ID>
    <cbc:ProcedureCode>Open</cbc:ProcedureCode>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:Name>Park benches for the city parks</cbc:Name>
    <cbc:ProcurementTypeCode>Supplies</cbc:ProcurementTypeCode>
  </cac:ProcurementProject>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-1</cbc:ID>
  </cac:ProcurementProjectLot>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-2</cbc:ID>
  </cac:ProcurementProjectLot>
  <cac:TenderResult>
    <cbc:AwardID>PWD-2026-PARKS-AWARD-1</cbc:AwardID>
    <cbc:TenderResultCode>Awarded</cbc:TenderResultCode>
    <cbc:Description>Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.</cbc:Description>
    <cbc:AdvertisementAmount currencyID="XBL">320.00</cbc:AdvertisementAmount>
    <cbc:AwardDate>2026-03-09</cbc:AwardDate>
    <cbc:AwardTime>09:30:00</cbc:AwardTime>
    <cbc:ReceivedTenderQuantity unitCode="C62">2</cbc:ReceivedTenderQuantity>
    <cbc:LowerTenderAmount currencyID="XBL">119040.00</cbc:LowerTenderAmount>
    <cbc:HigherTenderAmount currencyID="XBL">124080.00</cbc:HigherTenderAmount>
    <cbc:StartDate>2026-03-23</cbc:StartDate>
    <cbc:ReceivedElectronicTenderQuantity unitCode="C62">2</cbc:ReceivedElectronicTenderQuantity>
    <cbc:ReceivedForeignTenderQuantity unitCode="C62">1</cbc:ReceivedForeignTenderQuantity>
    <cac:Contract>
      <cbc:ID>PWD-2026-PARKS</cbc:ID>
      <cbc:ContractTypeCode>Framework</cbc:ContractTypeCode>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-03-23</cbc:StartDate>
        <cbc:DurationMeasure unitCode="MON">24</cbc:DurationMeasure>
      </cac:ValidityPeriod>
    </cac:Contract>
    <cac:AwardedTenderedProject>
      <cbc:VariantID>V0</cbc:VariantID>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-1</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-2</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:LegalMonetaryTotal>
        <cbc:PayableAmount currencyID="XBL">124080.00</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:AwardedTenderedProject>
    <cac:ContractFormalizationPeriod>
      <cbc:StartDate>2026-03-19</cbc:StartDate>
      <cbc:EndDate>2026-03-22</cbc:EndDate>
    </cac:ContractFormalizationPeriod>
    <cac:SubcontractTerms>
      <cbc:Rate>0</cbc:Rate>
      <cbc:UnknownPriceIndicator>false</cbc:UnknownPriceIndicator>
      <cbc:Description>No subcontracting.</cbc:Description>
    </cac:SubcontractTerms>
    <cac:WinningParty>
      <cbc:Rank>1</cbc:Rank>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:WinningParty>
  </cac:TenderResult>
</TenderContract>
```
