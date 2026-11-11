# Call For Tenders: Lumeport Public Works Department to Valdara Industries

*Example 3 of the flow "A public tender (Bayvarra)" · [Call For Tenders in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CALL-FOR-TENDERS-SCHEMA)*

The manufacturer retrieves the procurement documents.

[The XML file](03-CallForTenders.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **LPWD-DOC-26-0189**  
  The number of the procurement documents.
- `UUID` = **a65b4330-4332-51c0-84c8-c60e521470b2**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `ApprovalDate` = **2026-01-25**  
  Approved by the department's head.
- `IssueDate` = **2026-02-12**  
  Retrieved by the manufacturer after the notice was published.
- `IssueTime` = **13:26:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **The documents of the procedure.**  
  What.
- `VersionID` = **1**  
  The first version.
- `PreviousVersionID` = **0**  
  None.

### Legal Document Reference

Inside `LegalDocumentReference`:

- `ID` = **PWD-LEGAL-26**  
  The legal conditions.

### Technical Document Reference

Inside `TechnicalDocumentReference`:

- `ID` = **PWD-SPEC-BENCH-26**  
  The specification.

### Required Document Reference

Inside `RequiredDocumentReference`:

- `ID` = **PWD-PRICE-TPL**  
  The price schedule.

### Provided Document Reference

Inside `ProvidedDocumentReference`:

- `ID` = **PWD-SITE-PLAN**  
  The site plan.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **PWD-QA-26**  
  Questions and answers.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-CFT**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Contracting Party

Inside `ContractingParty`:

- `BuyerProfileURI` = **https://tenders.lumeport.example/buyers/pwd**  
  The buyer's profile.
- `ContractingPartyType/PartyTypeCode` = **Local**  
  A local authority.
- `ContractingPartyType/PartyType` = **Department of a city**  
  In words.
- `ContractingActivity/ActivityTypeCode` = **Public works**  
  Its activity.
- `ContractingActivity/ActivityType` = **Public works and parks**  
  In words.
- `ContractingRepresentationType/RepresentationTypeCode` = **Own**  
  On its own behalf.
- `ContractingRepresentationType/RepresentationType` = **Buys for itself**  
  In words.
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

### Originator Customer Party

Inside `OriginatorCustomerParty`:

- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Beneficiary Party

Inside `BeneficiaryParty`:

- `PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Ganluar Vindoov Budunuov** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `PartyLegalEntity/SecurityListing/ID` = **XU0001042505**  
  The identifier of the listed shares, in the form of an ISIN with the world's country code.
- `PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The regulated market where the shares are listed.
- `PartyLegalEntity/SecurityListing/MarketCode` = **FSE**  
  The market's code.
- `Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `ServiceProviderParty/ID` = **5-xu-SP-8-xu**  
  The service contract between the two.
- `ServiceProviderParty/ServiceTypeCode` = **Logistics**  
  The kind of service, as a code.
- `ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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
- `AppealTerms/AppealReceiverParty/IndustryClassificationCode` = **8423** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AppealTerms/AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  The trading name; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Language/ID` = **en**  
  English, the language the party does business in.
- `AppealTerms/AppealReceiverParty/Language/Name` = **English**  
  The language's name.
- `AppealTerms/AppealReceiverParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `AppealTerms/AppealReceiverParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `AppealTerms/AppealReceiverParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `AppealTerms/AppealReceiverParty/PostalAddress/StreetName` = **Justice Row**  
  Street of the postal address. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/BuildingNumber` = **20**  
  Building number of the postal address. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/PostalZone` = **38519**  
  Postal code in Bayvarra's format (5 digits). identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `AppealTerms/AppealReceiverParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/RegistrationName` = **Procurement Review Board of Bayvarra**  
  The name under which the party is registered, with its legal form; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CompanyID` = **20410822**  
  Number in the Federal business register of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `AppealTerms/AppealReceiverParty/Contact/Name` = **Registry**  
  The desk that handles this document; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/Telephone` = **+999 2 3851 0822**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/ElectronicMail` = **registry@review-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `AppealTerms/AppealReceiverParty/ElectronicAddress/ElectronicAddressID` = **XB:20410822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Procurement Review Board of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
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
- `OriginalContractingSystemID` = **PWD-FW-2024-PARKS**  
  The framework this one follows.
- `Description` = **Open procedure with two lots.**  
  The procedure.
- `NegotiationDescription` = **No negotiation: the award is on the tenders as submitted.**  
  Why none.
- `ProcedureCode` = **Open**  
  An open procedure.
- `UrgencyCode` = **Normal**  
  No urgency.
- `ExpenseCode` = **Investment**  
  Paid from the investment budget.
- `PartPresentationCode` = **OneOrMore**  
  Tenders for one or both lots.
- `ContractingSystemCode` = **Framework**  
  A framework agreement.
- `SubmissionMethodCode` = **Electronic**  
  Tenders are submitted electronically.
- `CandidateReductionConstraintIndicator` = **false**  
  No reduction of candidates.
- `GovernmentAgreementConstraintIndicator` = **true**  
  Covered by the trade accord's procurement chapter.
- `AccessToolsURI` = **https://tenders.lumeport.example/PWD-2026-PARKS**  
  Where the documents are.
- `TerminatedIndicator` = **false**  
  The procedure runs.
- `DocumentAvailabilityPeriod/StartDate` = **2026-01-26**  
  From the notice.
- `DocumentAvailabilityPeriod/EndDate` = **2026-02-25**  
  Until the day before the deadline.
- `TenderSubmissionDeadlinePeriod/EndDate` = **2026-02-26**  
  The deadline.
- `TenderSubmissionDeadlinePeriod/EndTime` = **12:00:00**  
  At noon.
- `InvitationSubmissionPeriod/StartDate` = **2026-01-26**  
  Invitations from.
- `InvitationSubmissionPeriod/EndDate` = **2026-02-01**  
  To.
- `ParticipationInvitationPeriod/StartDate` = **2026-01-26**  
  Participation invited from.
- `ParticipationInvitationPeriod/EndDate` = **2026-02-11**  
  To.
- `ParticipationRequestReceptionPeriod/EndDate` = **2026-02-11**  
  Requests to participate by then.
- `AdditionalInformationRequestPeriod/EndDate` = **2026-02-19**  
  Questions by then.
- `NoticeDocumentReference/ID` = **LPWD-DOC-26-0187**  
  The prior information notice.
- `AdditionalDocumentReference/ID` = **PWD-SPEC-BENCH-26**  
  The specification.
- `ProcessJustification/PreviousCancellationReasonCode` = **None**  
  No earlier procedure was cancelled.
- `ProcessJustification/ProcessReasonCode` = **Standard**  
  The open procedure is the rule.
- `ProcessJustification/ProcessReason` = **Value above the threshold for open procedures.**  
  Why.
- `ProcessJustification/Description` = **No exception applies.**  
  In words.
- `EconomicOperatorShortList/LimitationDescription` = **No short list in an open procedure.**  
  Why.
- `EconomicOperatorShortList/ExpectedQuantity` = **0**  
  None expected.
- `EconomicOperatorShortList/MaximumQuantity` = **0**  
  None.
- `EconomicOperatorShortList/MinimumQuantity` = **0**  
  None.
- `EconomicOperatorShortList/PreSelectedParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EconomicOperatorShortList/PreSelectedParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `OpenTenderEvent/IdentificationID` = **OPEN-1**  
  The opening of the tenders.
- `OpenTenderEvent/OccurrenceDate` = **2026-02-26**  
  The deadline day.
- `OpenTenderEvent/OccurrenceTime` = **14:00:00**  
  Two hours after the deadline.
- `OpenTenderEvent/TypeCode` = **Opening**  
  A tender opening.
- `OpenTenderEvent/Description` = **Electronic opening; tenderers may follow it online.**  
  How.
- `OpenTenderEvent/CompletionIndicator` = **false**  
  To come.
- `OpenTenderEvent/CurrentStatus/ConditionCode` = **Scheduled**  
  Planned.
- `OpenTenderEvent/Contact/Name` = **Procurement office**  
  Whom to ask.
- `OpenTenderEvent/OccurrenceLocation/Name` = **Lumeport Public Works Department, Civic Square**  
  Where.
- `AuctionTerms/AuctionConstraintIndicator` = **false**  
  No electronic auction.
- `AuctionTerms/JustificationDescription` = **The award uses quality as well as price.**  
  Why not.
- `AuctionTerms/Description` = **No auction.**  
  In words.
- `AuctionTerms/ProcessDescription` = **Not applicable.**  
  No process.
- `AuctionTerms/ConditionsDescription` = **Not applicable.**  
  No conditions.
- `AuctionTerms/ElectronicDeviceDescription` = **Not applicable.**  
  No device.
- `AuctionTerms/AuctionURI` = **https://tenders.lumeport.example/auctions**  
  The platform, unused.
- `FrameworkAgreement/ExpectedOperatorQuantity` = **1**  
  One supplier.
- `FrameworkAgreement/MaximumOperatorQuantity` = **1**  
  At most one.
- `FrameworkAgreement/Justification` = **Uniform benches across the parks.**  
  Why one.
- `FrameworkAgreement/Frequency` = **Releases every few months.**  
  How often.
- `FrameworkAgreement/EstimatedMaximumValueAmount` = **148896.00** (currencyID `XBL`)  
  The estimated maximum.
- `FrameworkAgreement/MaximumValueAmount` = **186120.00** (currencyID `XBL`)  
  With the extension.
- `FrameworkAgreement/DurationPeriod/DurationMeasure` = **24** (unitCode `MON`)  
  Two years.
- `FrameworkAgreement/SubsequentProcessTenderRequirement/Name` = **Release order**  
  Each release is a call-off order.
- `FrameworkAgreement/SubsequentProcessTenderRequirement/Description` = **No new competition.**  
  How.
- `ContractingSystem/ID` = **FW-1**  
  The framework.
- `ContractingSystem/ContractingSystemTypeCode` = **Framework**  
  A framework agreement.
- `ContractingSystem/Description` = **Framework with one supplier.**  
  In words.

### Procurement Project

Inside `ProcurementProject`:

- `ID` = **PWD-2026-PARKS**  
  The project's identifier.
- `Name` = **Park benches for the parks renewal programme**  
  The project's name.
- `Description` = **240 steel park benches with hardwood slats over two years, delivered and anchored.**  
  What is bought.
- `ProcurementTypeCode` = **Supplies**  
  Supplies or services.
- `ProcurementSubTypeCode` = **Purchase**  
  The kind within it.
- `QualityControlCode` = **Inspection**  
  Each release is inspected on delivery.
- `RequiredFeeAmount` = **50.00** (currencyID `XBL`)  
  The fee for the tender documents on paper.
- `FeeDescription` = **Electronic documents are free; paper copies cost 50 lume.**  
  The fee.
- `RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `EstimatedOverallContractQuantity` = **240** (unitCode `H87`)  
  240 benches over the contract.
- `Note` = **Part of the parks renewal programme 2026.**  
  The programme.
- `SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementAdditionalType/ProcurementTypeCode` = **Green**  
  Green public procurement.
- `ProcurementAdditionalType/ProcurementType` = **Recycled steel and certified timber are asked.**  
  In words.
- `RequestedTenderTotal/EstimatedOverallContractAmount` = **124080.00** (currencyID `XBL`)  
  The estimated value.
- `RequestedTenderTotal/EstimatedOverallFrameworkContractsAmount` = **124080.00** (currencyID `XBL`)  
  The framework's estimate.
- `RequestedTenderTotal/TotalAmount` = **124080.00** (currencyID `XBL`)  
  The budget.
- `RequestedTenderTotal/TaxIncludedIndicator` = **false**  
  Without tax: a public body pays no sales tax.
- `RequestedTenderTotal/MinimumAmount` = **62040.00** (currencyID `XBL`)  
  At least half will be called off.
- `RequestedTenderTotal/MaximumAmount` = **148896.00** (currencyID `XBL`)  
  At most 20 % more.
- `RequestedTenderTotal/MonetaryScope` = **Two years of releases.**  
  What the amount covers.
- `RequestedTenderTotal/AverageSubsequentContractAmount` = **20680.00** (currencyID `XBL`)  
  Six releases on average.
- `RequestedTenderTotal/ApplicableTaxCategory/ID` = **E**  
  A sale to a public body is exempt from the state sales tax (category E).
- `RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **XB-PUBLIC**  
  The world's code for the exemption reason (world/countries.json).
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Sale to a public body**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `MainCommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  The goods' HS subheading.
- `AdditionalCommodityClassification/CommodityCode` = **PARKS-FURN**  
  The department's own category: park furniture.
- `RealizedLocation/Name` = **Harbour park and town parks, Lumeport**  
  Where the benches go.
- `RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `RealizedLocation/Address/Country/IdentificationCode` = **XB**  
  Bayvarra.
- `PlannedPeriod/StartDate` = **2026-03-23**  
  From the first release.
- `PlannedPeriod/EndDate` = **2028-03-22**  
  For two years.
- `ContractExtension/OptionsDescription` = **One extension of a year with 120 more benches.**  
  The option.
- `ContractExtension/MinimumNumberNumeric` = **0**  
  None need be used.
- `ContractExtension/MaximumNumberNumeric` = **1**  
  At most one.
- `ContractExtension/RenewalsIndicator` = **true**  
  The contract may be renewed.
- `ContractExtension/OptionValidityPeriod/EndDate` = **2028-03-22**  
  Decided before it ends.
- `ContractExtension/Renewal/Amount` = **62040.00** (currencyID `XBL`)  
  The value of a renewal.
- `ContractExtension/Renewal/Period/DurationMeasure` = **12** (unitCode `MON`)  
  Twelve months.
- `RequestForTenderLine/ID` = **1**  
  The benches.
- `RequestForTenderLine/UUID` = **b98b5bc4-6b96-59da-b8e9-89fc28afcae4**  
  Its UUID.
- `RequestForTenderLine/Note` = **Steel frame, five hardwood slats, ground anchors.**  
  The requirement.
- `RequestForTenderLine/Quantity` = **240** (unitCode `H87`)  
  Over the contract.
- `RequestForTenderLine/MinimumQuantity` = **120** (unitCode `H87`)  
  At least.
- `RequestForTenderLine/MaximumQuantity` = **288** (unitCode `H87`)  
  At most.
- `RequestForTenderLine/TaxIncludedIndicator` = **false**  
  Prices without tax.
- `RequestForTenderLine/MinimumAmount` = **350.00** (currencyID `XBL`)  
  A unit price below this would be abnormally low.
- `RequestForTenderLine/MaximumAmount` = **600.00** (currencyID `XBL`)  
  The most the budget allows per bench.
- `RequestForTenderLine/EstimatedAmount` = **119760.00** (currencyID `XBL`)  
  The estimate.
- `RequestForTenderLine/DocumentReference/ID` = **PWD-SPEC-BENCH-26**  
  The technical specification.
- `RequestForTenderLine/DeliveryPeriod/StartDate` = **2026-04-02**  
  Releases from.
- `RequestForTenderLine/DeliveryPeriod/EndDate` = **2028-03-22**  
  To.
- `RequestForTenderLine/RequiredItemLocationQuantity/LeadTimeMeasure` = **10** (unitCode `DAY`)  
  Ten days per release.
- `RequestForTenderLine/WarrantyValidityPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `RequestForTenderLine/Item/Name` = **Park bench, 1800 mm**  
  The item asked for.
- `RequestForTenderLine/SubRequestForTenderLine/ID` = **1.1**  
  The anchors.
- `RequestForTenderLine/SubRequestForTenderLine/Quantity` = **240** (unitCode `SET`)  
  One set per bench.
- `RequestForTenderLine/SubRequestForTenderLine/Item/Name` = **Ground anchor set**  
  Part of the bench.

### Procurement Project Lot

Inside `ProcurementProjectLot`:

- `ID` = **LOT-1**  
  Lot 1.
- `LegalDocumentReference/ID` = **XB-PPA-2019**  
  The procurement act.
- `TechnicalDocumentReference/ID` = **PWD-SPEC-LOT-1**  
  The lot's specification.
- `RequiredDocumentReference/ID` = **PWD-PRICE-TPL**  
  The price schedule to submit.
- `ProvidedDocumentReference/ID` = **PWD-SITE-PLAN**  
  The parks' site plan.
- `AdditionalDocumentReference/ID` = **PWD-QA-26**  
  Questions and answers.
- `TenderingTerms/Note` = **As for the procedure.**  
  The lot's terms.
- `TenderingProcess/Description` = **As for the procedure.**  
  The lot's process.
- `ProcurementProject/ID` = **LOT-1**  
  The project's identifier.
- `ProcurementProject/Name` = **Park benches**  
  The project's name.
- `ProcurementProject/Description` = **240 steel park benches with hardwood slats over two years, delivered and anchored.**  
  What is bought.
- `ProcurementProject/ProcurementTypeCode` = **Supplies**  
  Supplies or services.
- `ProcurementProject/ProcurementSubTypeCode` = **Purchase**  
  The kind within it.
- `ProcurementProject/QualityControlCode` = **Inspection**  
  Each release is inspected on delivery.
- `ProcurementProject/RequiredFeeAmount` = **50.00** (currencyID `XBL`)  
  The fee for the tender documents on paper.
- `ProcurementProject/FeeDescription` = **Electronic documents are free; paper copies cost 50 lume.**  
  The fee.
- `ProcurementProject/RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `ProcurementProject/EstimatedOverallContractQuantity` = **240** (unitCode `H87`)  
  240 benches over the contract.
- `ProcurementProject/Note` = **Part of the parks renewal programme 2026.**  
  The programme.
- `ProcurementProject/SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementProject/ProcurementAdditionalType/ProcurementTypeCode` = **Green**  
  Green public procurement.
- `ProcurementProject/ProcurementAdditionalType/ProcurementType` = **Recycled steel and certified timber are asked.**  
  In words.
- `ProcurementProject/RequestedTenderTotal/EstimatedOverallContractAmount` = **119760.00** (currencyID `XBL`)  
  The estimated value.
- `ProcurementProject/RequestedTenderTotal/EstimatedOverallFrameworkContractsAmount` = **119760.00** (currencyID `XBL`)  
  The framework's estimate.
- `ProcurementProject/RequestedTenderTotal/TotalAmount` = **119760.00** (currencyID `XBL`)  
  The budget.
- `ProcurementProject/RequestedTenderTotal/TaxIncludedIndicator` = **false**  
  Without tax: a public body pays no sales tax.
- `ProcurementProject/RequestedTenderTotal/MinimumAmount` = **59880.00** (currencyID `XBL`)  
  At least half will be called off.
- `ProcurementProject/RequestedTenderTotal/MaximumAmount` = **143712.00** (currencyID `XBL`)  
  At most 20 % more.
- `ProcurementProject/RequestedTenderTotal/MonetaryScope` = **Two years of releases.**  
  What the amount covers.
- `ProcurementProject/RequestedTenderTotal/AverageSubsequentContractAmount` = **19960.00** (currencyID `XBL`)  
  Six releases on average.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/ID` = **E**  
  A sale to a public body is exempt from the state sales tax (category E).
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **XB-PUBLIC**  
  The world's code for the exemption reason (world/countries.json).
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Sale to a public body**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `ProcurementProject/MainCommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  The goods' HS subheading.
- `ProcurementProject/AdditionalCommodityClassification/CommodityCode` = **PARKS-FURN**  
  The department's own category: park furniture.
- `ProcurementProject/RealizedLocation/Name` = **Harbour park and town parks, Lumeport**  
  Where the benches go.
- `ProcurementProject/RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `ProcurementProject/RealizedLocation/Address/Country/IdentificationCode` = **XB**  
  Bayvarra.
- `ProcurementProject/PlannedPeriod/StartDate` = **2026-03-23**  
  From the first release.
- `ProcurementProject/PlannedPeriod/EndDate` = **2028-03-22**  
  For two years.
- `ProcurementProject/ContractExtension/OptionsDescription` = **One extension of a year with 120 more benches.**  
  The option.
- `ProcurementProject/ContractExtension/MinimumNumberNumeric` = **0**  
  None need be used.
- `ProcurementProject/ContractExtension/MaximumNumberNumeric` = **1**  
  At most one.
- `ProcurementProject/ContractExtension/RenewalsIndicator` = **true**  
  The contract may be renewed.
- `ProcurementProject/ContractExtension/OptionValidityPeriod/EndDate` = **2028-03-22**  
  Decided before it ends.
- `ProcurementProject/ContractExtension/Renewal/Amount` = **59880.00** (currencyID `XBL`)  
  The value of a renewal.
- `ProcurementProject/ContractExtension/Renewal/Period/DurationMeasure` = **12** (unitCode `MON`)  
  Twelve months.
- `ProcurementProject/RequestForTenderLine/ID` = **1**  
  The benches.
- `ProcurementProject/RequestForTenderLine/UUID` = **b98b5bc4-6b96-59da-b8e9-89fc28afcae4**  
  Its UUID.
- `ProcurementProject/RequestForTenderLine/Note` = **Steel frame, five hardwood slats, ground anchors.**  
  The requirement.
- `ProcurementProject/RequestForTenderLine/Quantity` = **240** (unitCode `H87`)  
  Over the contract.
- `ProcurementProject/RequestForTenderLine/MinimumQuantity` = **120** (unitCode `H87`)  
  At least.
- `ProcurementProject/RequestForTenderLine/MaximumQuantity` = **288** (unitCode `H87`)  
  At most.
- `ProcurementProject/RequestForTenderLine/TaxIncludedIndicator` = **false**  
  Prices without tax.
- `ProcurementProject/RequestForTenderLine/MinimumAmount` = **350.00** (currencyID `XBL`)  
  A unit price below this would be abnormally low.
- `ProcurementProject/RequestForTenderLine/MaximumAmount` = **600.00** (currencyID `XBL`)  
  The most the budget allows per bench.
- `ProcurementProject/RequestForTenderLine/EstimatedAmount` = **119760.00** (currencyID `XBL`)  
  The estimate.
- `ProcurementProject/RequestForTenderLine/DocumentReference/ID` = **PWD-SPEC-BENCH-26**  
  The technical specification.
- `ProcurementProject/RequestForTenderLine/DeliveryPeriod/StartDate` = **2026-04-02**  
  Releases from.
- `ProcurementProject/RequestForTenderLine/DeliveryPeriod/EndDate` = **2028-03-22**  
  To.
- `ProcurementProject/RequestForTenderLine/RequiredItemLocationQuantity/LeadTimeMeasure` = **10** (unitCode `DAY`)  
  Ten days per release.
- `ProcurementProject/RequestForTenderLine/WarrantyValidityPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `ProcurementProject/RequestForTenderLine/Item/Name` = **Park bench, 1800 mm**  
  The item asked for.
- `ProcurementProject/RequestForTenderLine/SubRequestForTenderLine/ID` = **1.1**  
  The anchors.
- `ProcurementProject/RequestForTenderLine/SubRequestForTenderLine/Quantity` = **240** (unitCode `SET`)  
  One set per bench.
- `ProcurementProject/RequestForTenderLine/SubRequestForTenderLine/Item/Name` = **Ground anchor set**  
  Part of the bench.
- `ID` = **LOT-2**  
  Lot 2.
- `LegalDocumentReference/ID` = **XB-PPA-2019**  
  The procurement act.
- `TechnicalDocumentReference/ID` = **PWD-SPEC-LOT-2**  
  The lot's specification.
- `RequiredDocumentReference/ID` = **PWD-PRICE-TPL**  
  The price schedule to submit.
- `ProvidedDocumentReference/ID` = **PWD-SITE-PLAN**  
  The parks' site plan.
- `AdditionalDocumentReference/ID` = **PWD-QA-26**  
  Questions and answers.
- `TenderingTerms/Note` = **As for the procedure.**  
  The lot's terms.
- `TenderingProcess/Description` = **As for the procedure.**  
  The lot's process.
- `ProcurementProject/ID` = **LOT-2**  
  The project's identifier.
- `ProcurementProject/Name` = **Installation of the benches**  
  The project's name.
- `ProcurementProject/Description` = **240 steel park benches with hardwood slats over two years, delivered and anchored.**  
  What is bought.
- `ProcurementProject/ProcurementTypeCode` = **Services**  
  Supplies or services.
- `ProcurementProject/ProcurementSubTypeCode` = **Installation**  
  The kind within it.
- `ProcurementProject/QualityControlCode` = **Inspection**  
  Each release is inspected on delivery.
- `ProcurementProject/RequiredFeeAmount` = **50.00** (currencyID `XBL`)  
  The fee for the tender documents on paper.
- `ProcurementProject/FeeDescription` = **Electronic documents are free; paper copies cost 50 lume.**  
  The fee.
- `ProcurementProject/RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `ProcurementProject/EstimatedOverallContractQuantity` = **240** (unitCode `H87`)  
  240 benches over the contract.
- `ProcurementProject/Note` = **Part of the parks renewal programme 2026.**  
  The programme.
- `ProcurementProject/SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementProject/ProcurementAdditionalType/ProcurementTypeCode` = **Green**  
  Green public procurement.
- `ProcurementProject/ProcurementAdditionalType/ProcurementType` = **Recycled steel and certified timber are asked.**  
  In words.
- `ProcurementProject/RequestedTenderTotal/EstimatedOverallContractAmount` = **4320.00** (currencyID `XBL`)  
  The estimated value.
- `ProcurementProject/RequestedTenderTotal/EstimatedOverallFrameworkContractsAmount` = **4320.00** (currencyID `XBL`)  
  The framework's estimate.
- `ProcurementProject/RequestedTenderTotal/TotalAmount` = **4320.00** (currencyID `XBL`)  
  The budget.
- `ProcurementProject/RequestedTenderTotal/TaxIncludedIndicator` = **false**  
  Without tax: a public body pays no sales tax.
- `ProcurementProject/RequestedTenderTotal/MinimumAmount` = **2160.00** (currencyID `XBL`)  
  At least half will be called off.
- `ProcurementProject/RequestedTenderTotal/MaximumAmount` = **5184.00** (currencyID `XBL`)  
  At most 20 % more.
- `ProcurementProject/RequestedTenderTotal/MonetaryScope` = **Two years of releases.**  
  What the amount covers.
- `ProcurementProject/RequestedTenderTotal/AverageSubsequentContractAmount` = **720.00** (currencyID `XBL`)  
  Six releases on average.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/ID` = **E**  
  A sale to a public body is exempt from the state sales tax (category E).
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **XB-PUBLIC**  
  The world's code for the exemption reason (world/countries.json).
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Sale to a public body**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `ProcurementProject/MainCommodityClassification/ItemClassificationCode` = **9988.00** (listID `HS`)  
  A service: no HS subheading.
- `ProcurementProject/AdditionalCommodityClassification/CommodityCode` = **PARKS-FURN**  
  The department's own category: park furniture.
- `ProcurementProject/RealizedLocation/Name` = **Harbour park and town parks, Lumeport**  
  Where the benches go.
- `ProcurementProject/RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `ProcurementProject/RealizedLocation/Address/Country/IdentificationCode` = **XB**  
  Bayvarra.
- `ProcurementProject/PlannedPeriod/StartDate` = **2026-03-23**  
  From the first release.
- `ProcurementProject/PlannedPeriod/EndDate` = **2028-03-22**  
  For two years.
- `ProcurementProject/ContractExtension/OptionsDescription` = **One extension of a year with 120 more benches.**  
  The option.
- `ProcurementProject/ContractExtension/MinimumNumberNumeric` = **0**  
  None need be used.
- `ProcurementProject/ContractExtension/MaximumNumberNumeric` = **1**  
  At most one.
- `ProcurementProject/ContractExtension/RenewalsIndicator` = **true**  
  The contract may be renewed.
- `ProcurementProject/ContractExtension/OptionValidityPeriod/EndDate` = **2028-03-22**  
  Decided before it ends.
- `ProcurementProject/ContractExtension/Renewal/Amount` = **2160.00** (currencyID `XBL`)  
  The value of a renewal.
- `ProcurementProject/ContractExtension/Renewal/Period/DurationMeasure` = **12** (unitCode `MON`)  
  Twelve months.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CallForTenders xmlns="urn:oasis:names:specification:ubl:schema:xsd:CallForTenders-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:tender</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0189</cbc:ID>
  <cbc:UUID>a65b4330-4332-51c0-84c8-c60e521470b2</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:ApprovalDate>2026-01-25</cbc:ApprovalDate>
  <cbc:IssueDate>2026-02-12</cbc:IssueDate>
  <cbc:IssueTime>13:26:00</cbc:IssueTime>
  <cbc:Note>The documents of the procedure.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:PreviousVersionID>0</cbc:PreviousVersionID>
  <cac:LegalDocumentReference>
    <cbc:ID>PWD-LEGAL-26</cbc:ID>
  </cac:LegalDocumentReference>
  <cac:TechnicalDocumentReference>
    <cbc:ID>PWD-SPEC-BENCH-26</cbc:ID>
  </cac:TechnicalDocumentReference>
  <cac:RequiredDocumentReference>
    <cbc:ID>PWD-PRICE-TPL</cbc:ID>
  </cac:RequiredDocumentReference>
  <cac:ProvidedDocumentReference>
    <cbc:ID>PWD-SITE-PLAN</cbc:ID>
  </cac:ProvidedDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>PWD-QA-26</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-CFT</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:ContractingParty>
    <cbc:BuyerProfileURI>https://tenders.lumeport.example/buyers/pwd</cbc:BuyerProfileURI>
    <cac:ContractingPartyType>
      <cbc:PartyTypeCode>Local</cbc:PartyTypeCode>
      <cbc:PartyType>Department of a city</cbc:PartyType>
    </cac:ContractingPartyType>
    <cac:ContractingActivity>
      <cbc:ActivityTypeCode>Public works</cbc:ActivityTypeCode>
      <cbc:ActivityType>Public works and parks</cbc:ActivityType>
    </cac:ContractingActivity>
    <cac:ContractingRepresentationType>
      <cbc:RepresentationTypeCode>Own</cbc:RepresentationTypeCode>
      <cbc:RepresentationType>Buys for itself</cbc:RepresentationType>
    </cac:ContractingRepresentationType>
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
  <cac:OriginatorCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:OriginatorCustomerParty>
  <cac:BeneficiaryParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Public Works Department</cbc:Name>
    </cac:PartyName>
  </cac:BeneficiaryParty>
  <cac:ReceiverParty>
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
      <cbc:StreetName languageID="qau">Ganluar Vindoov Budunuov</cbc:StreetName>
      <cbc:StreetName languageID="en">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
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
      <cac:AppealReceiverParty>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">8423</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
          <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
          <cbc:StreetName>Justice Row</cbc:StreetName>
          <cbc:BuildingNumber>20</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38519</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Procurement Review Board of Bayvarra</cbc:RegistrationName>
          <cbc:CompanyID>20410822</cbc:CompanyID>
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
          <cbc:Name>Registry</cbc:Name>
          <cbc:JobTitle>Procurement officer</cbc:JobTitle>
          <cbc:Department>Procurement</cbc:Department>
          <cbc:Telephone>+999 2 3851 0822</cbc:Telephone>
          <cbc:ElectronicMail>registry@review-xb.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410822</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:AppealReceiverParty>
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
    <cbc:OriginalContractingSystemID>PWD-FW-2024-PARKS</cbc:OriginalContractingSystemID>
    <cbc:Description>Open procedure with two lots.</cbc:Description>
    <cbc:NegotiationDescription>No negotiation: the award is on the tenders as submitted.</cbc:NegotiationDescription>
    <cbc:ProcedureCode>Open</cbc:ProcedureCode>
    <cbc:UrgencyCode>Normal</cbc:UrgencyCode>
    <cbc:ExpenseCode>Investment</cbc:ExpenseCode>
    <cbc:PartPresentationCode>OneOrMore</cbc:PartPresentationCode>
    <cbc:ContractingSystemCode>Framework</cbc:ContractingSystemCode>
    <cbc:SubmissionMethodCode>Electronic</cbc:SubmissionMethodCode>
    <cbc:CandidateReductionConstraintIndicator>false</cbc:CandidateReductionConstraintIndicator>
    <cbc:GovernmentAgreementConstraintIndicator>true</cbc:GovernmentAgreementConstraintIndicator>
    <cbc:AccessToolsURI>https://tenders.lumeport.example/PWD-2026-PARKS</cbc:AccessToolsURI>
    <cbc:TerminatedIndicator>false</cbc:TerminatedIndicator>
    <cac:DocumentAvailabilityPeriod>
      <cbc:StartDate>2026-01-26</cbc:StartDate>
      <cbc:EndDate>2026-02-25</cbc:EndDate>
    </cac:DocumentAvailabilityPeriod>
    <cac:TenderSubmissionDeadlinePeriod>
      <cbc:EndDate>2026-02-26</cbc:EndDate>
      <cbc:EndTime>12:00:00</cbc:EndTime>
    </cac:TenderSubmissionDeadlinePeriod>
    <cac:InvitationSubmissionPeriod>
      <cbc:StartDate>2026-01-26</cbc:StartDate>
      <cbc:EndDate>2026-02-01</cbc:EndDate>
    </cac:InvitationSubmissionPeriod>
    <cac:ParticipationInvitationPeriod>
      <cbc:StartDate>2026-01-26</cbc:StartDate>
      <cbc:EndDate>2026-02-11</cbc:EndDate>
    </cac:ParticipationInvitationPeriod>
    <cac:ParticipationRequestReceptionPeriod>
      <cbc:EndDate>2026-02-11</cbc:EndDate>
    </cac:ParticipationRequestReceptionPeriod>
    <cac:AdditionalInformationRequestPeriod>
      <cbc:EndDate>2026-02-19</cbc:EndDate>
    </cac:AdditionalInformationRequestPeriod>
    <cac:NoticeDocumentReference>
      <cbc:ID>LPWD-DOC-26-0187</cbc:ID>
    </cac:NoticeDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>PWD-SPEC-BENCH-26</cbc:ID>
    </cac:AdditionalDocumentReference>
    <cac:ProcessJustification>
      <cbc:PreviousCancellationReasonCode>None</cbc:PreviousCancellationReasonCode>
      <cbc:ProcessReasonCode>Standard</cbc:ProcessReasonCode>
      <cbc:ProcessReason>Value above the threshold for open procedures.</cbc:ProcessReason>
      <cbc:Description>No exception applies.</cbc:Description>
    </cac:ProcessJustification>
    <cac:EconomicOperatorShortList>
      <cbc:LimitationDescription>No short list in an open procedure.</cbc:LimitationDescription>
      <cbc:ExpectedQuantity>0</cbc:ExpectedQuantity>
      <cbc:MaximumQuantity>0</cbc:MaximumQuantity>
      <cbc:MinimumQuantity>0</cbc:MinimumQuantity>
      <cac:PreSelectedParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:PreSelectedParty>
    </cac:EconomicOperatorShortList>
    <cac:OpenTenderEvent>
      <cbc:IdentificationID>OPEN-1</cbc:IdentificationID>
      <cbc:OccurrenceDate>2026-02-26</cbc:OccurrenceDate>
      <cbc:OccurrenceTime>14:00:00</cbc:OccurrenceTime>
      <cbc:TypeCode>Opening</cbc:TypeCode>
      <cbc:Description>Electronic opening; tenderers may follow it online.</cbc:Description>
      <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
      <cac:CurrentStatus>
        <cbc:ConditionCode>Scheduled</cbc:ConditionCode>
      </cac:CurrentStatus>
      <cac:Contact>
        <cbc:Name>Procurement office</cbc:Name>
      </cac:Contact>
      <cac:OccurrenceLocation>
        <cbc:Name>Lumeport Public Works Department, Civic Square</cbc:Name>
      </cac:OccurrenceLocation>
    </cac:OpenTenderEvent>
    <cac:AuctionTerms>
      <cbc:AuctionConstraintIndicator>false</cbc:AuctionConstraintIndicator>
      <cbc:JustificationDescription>The award uses quality as well as price.</cbc:JustificationDescription>
      <cbc:Description>No auction.</cbc:Description>
      <cbc:ProcessDescription>Not applicable.</cbc:ProcessDescription>
      <cbc:ConditionsDescription>Not applicable.</cbc:ConditionsDescription>
      <cbc:ElectronicDeviceDescription>Not applicable.</cbc:ElectronicDeviceDescription>
      <cbc:AuctionURI>https://tenders.lumeport.example/auctions</cbc:AuctionURI>
    </cac:AuctionTerms>
    <cac:FrameworkAgreement>
      <cbc:ExpectedOperatorQuantity>1</cbc:ExpectedOperatorQuantity>
      <cbc:MaximumOperatorQuantity>1</cbc:MaximumOperatorQuantity>
      <cbc:Justification>Uniform benches across the parks.</cbc:Justification>
      <cbc:Frequency>Releases every few months.</cbc:Frequency>
      <cbc:EstimatedMaximumValueAmount currencyID="XBL">148896.00</cbc:EstimatedMaximumValueAmount>
      <cbc:MaximumValueAmount currencyID="XBL">186120.00</cbc:MaximumValueAmount>
      <cac:DurationPeriod>
        <cbc:DurationMeasure unitCode="MON">24</cbc:DurationMeasure>
      </cac:DurationPeriod>
      <cac:SubsequentProcessTenderRequirement>
        <cbc:Name>Release order</cbc:Name>
        <cbc:Description>No new competition.</cbc:Description>
      </cac:SubsequentProcessTenderRequirement>
    </cac:FrameworkAgreement>
    <cac:ContractingSystem>
      <cbc:ID>FW-1</cbc:ID>
      <cbc:ContractingSystemTypeCode>Framework</cbc:ContractingSystemTypeCode>
      <cbc:Description>Framework with one supplier.</cbc:Description>
    </cac:ContractingSystem>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:ID>PWD-2026-PARKS</cbc:ID>
    <cbc:Name>Park benches for the parks renewal programme</cbc:Name>
    <cbc:Description>240 steel park benches with hardwood slats over two years, delivered and anchored.</cbc:Description>
    <cbc:ProcurementTypeCode>Supplies</cbc:ProcurementTypeCode>
    <cbc:ProcurementSubTypeCode>Purchase</cbc:ProcurementSubTypeCode>
    <cbc:QualityControlCode>Inspection</cbc:QualityControlCode>
    <cbc:RequiredFeeAmount currencyID="XBL">50.00</cbc:RequiredFeeAmount>
    <cbc:FeeDescription>Electronic documents are free; paper copies cost 50 lume.</cbc:FeeDescription>
    <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
    <cbc:EstimatedOverallContractQuantity unitCode="H87">240</cbc:EstimatedOverallContractQuantity>
    <cbc:Note>Part of the parks renewal programme 2026.</cbc:Note>
    <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
    <cac:ProcurementAdditionalType>
      <cbc:ProcurementTypeCode>Green</cbc:ProcurementTypeCode>
      <cbc:ProcurementType>Recycled steel and certified timber are asked.</cbc:ProcurementType>
    </cac:ProcurementAdditionalType>
    <cac:RequestedTenderTotal>
      <cbc:EstimatedOverallContractAmount currencyID="XBL">124080.00</cbc:EstimatedOverallContractAmount>
      <cbc:EstimatedOverallFrameworkContractsAmount currencyID="XBL">124080.00</cbc:EstimatedOverallFrameworkContractsAmount>
      <cbc:TotalAmount currencyID="XBL">124080.00</cbc:TotalAmount>
      <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
      <cbc:MinimumAmount currencyID="XBL">62040.00</cbc:MinimumAmount>
      <cbc:MaximumAmount currencyID="XBL">148896.00</cbc:MaximumAmount>
      <cbc:MonetaryScope>Two years of releases.</cbc:MonetaryScope>
      <cbc:AverageSubsequentContractAmount currencyID="XBL">20680.00</cbc:AverageSubsequentContractAmount>
      <cac:ApplicableTaxCategory>
        <cbc:ID>E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-PUBLIC</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Sale to a public body</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequestedTenderTotal>
    <cac:MainCommodityClassification>
      <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
    </cac:MainCommodityClassification>
    <cac:AdditionalCommodityClassification>
      <cbc:CommodityCode>PARKS-FURN</cbc:CommodityCode>
    </cac:AdditionalCommodityClassification>
    <cac:RealizedLocation>
      <cbc:Name>Harbour park and town parks, Lumeport</cbc:Name>
      <cac:Address>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:RealizedLocation>
    <cac:PlannedPeriod>
      <cbc:StartDate>2026-03-23</cbc:StartDate>
      <cbc:EndDate>2028-03-22</cbc:EndDate>
    </cac:PlannedPeriod>
    <cac:ContractExtension>
      <cbc:OptionsDescription>One extension of a year with 120 more benches.</cbc:OptionsDescription>
      <cbc:MinimumNumberNumeric>0</cbc:MinimumNumberNumeric>
      <cbc:MaximumNumberNumeric>1</cbc:MaximumNumberNumeric>
      <cbc:RenewalsIndicator>true</cbc:RenewalsIndicator>
      <cac:OptionValidityPeriod>
        <cbc:EndDate>2028-03-22</cbc:EndDate>
      </cac:OptionValidityPeriod>
      <cac:Renewal>
        <cbc:Amount currencyID="XBL">62040.00</cbc:Amount>
        <cac:Period>
          <cbc:DurationMeasure unitCode="MON">12</cbc:DurationMeasure>
        </cac:Period>
      </cac:Renewal>
    </cac:ContractExtension>
    <cac:RequestForTenderLine>
      <cbc:ID>1</cbc:ID>
      <cbc:UUID>b98b5bc4-6b96-59da-b8e9-89fc28afcae4</cbc:UUID>
      <cbc:Note>Steel frame, five hardwood slats, ground anchors.</cbc:Note>
      <cbc:Quantity unitCode="H87">240</cbc:Quantity>
      <cbc:MinimumQuantity unitCode="H87">120</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="H87">288</cbc:MaximumQuantity>
      <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
      <cbc:MinimumAmount currencyID="XBL">350.00</cbc:MinimumAmount>
      <cbc:MaximumAmount currencyID="XBL">600.00</cbc:MaximumAmount>
      <cbc:EstimatedAmount currencyID="XBL">119760.00</cbc:EstimatedAmount>
      <cac:DocumentReference>
        <cbc:ID>PWD-SPEC-BENCH-26</cbc:ID>
      </cac:DocumentReference>
      <cac:DeliveryPeriod>
        <cbc:StartDate>2026-04-02</cbc:StartDate>
        <cbc:EndDate>2028-03-22</cbc:EndDate>
      </cac:DeliveryPeriod>
      <cac:RequiredItemLocationQuantity>
        <cbc:LeadTimeMeasure unitCode="DAY">10</cbc:LeadTimeMeasure>
      </cac:RequiredItemLocationQuantity>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
      </cac:WarrantyValidityPeriod>
      <cac:Item>
        <cbc:Name>Park bench, 1800 mm</cbc:Name>
      </cac:Item>
      <cac:SubRequestForTenderLine>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Quantity unitCode="SET">240</cbc:Quantity>
        <cac:Item>
          <cbc:Name>Ground anchor set</cbc:Name>
        </cac:Item>
      </cac:SubRequestForTenderLine>
    </cac:RequestForTenderLine>
  </cac:ProcurementProject>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-1</cbc:ID>
    <cac:LegalDocumentReference>
      <cbc:ID>XB-PPA-2019</cbc:ID>
    </cac:LegalDocumentReference>
    <cac:TechnicalDocumentReference>
      <cbc:ID>PWD-SPEC-LOT-1</cbc:ID>
    </cac:TechnicalDocumentReference>
    <cac:RequiredDocumentReference>
      <cbc:ID>PWD-PRICE-TPL</cbc:ID>
    </cac:RequiredDocumentReference>
    <cac:ProvidedDocumentReference>
      <cbc:ID>PWD-SITE-PLAN</cbc:ID>
    </cac:ProvidedDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>PWD-QA-26</cbc:ID>
    </cac:AdditionalDocumentReference>
    <cac:TenderingTerms>
      <cbc:Note>As for the procedure.</cbc:Note>
    </cac:TenderingTerms>
    <cac:TenderingProcess>
      <cbc:Description>As for the procedure.</cbc:Description>
    </cac:TenderingProcess>
    <cac:ProcurementProject>
      <cbc:ID>LOT-1</cbc:ID>
      <cbc:Name>Park benches</cbc:Name>
      <cbc:Description>240 steel park benches with hardwood slats over two years, delivered and anchored.</cbc:Description>
      <cbc:ProcurementTypeCode>Supplies</cbc:ProcurementTypeCode>
      <cbc:ProcurementSubTypeCode>Purchase</cbc:ProcurementSubTypeCode>
      <cbc:QualityControlCode>Inspection</cbc:QualityControlCode>
      <cbc:RequiredFeeAmount currencyID="XBL">50.00</cbc:RequiredFeeAmount>
      <cbc:FeeDescription>Electronic documents are free; paper copies cost 50 lume.</cbc:FeeDescription>
      <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
      <cbc:EstimatedOverallContractQuantity unitCode="H87">240</cbc:EstimatedOverallContractQuantity>
      <cbc:Note>Part of the parks renewal programme 2026.</cbc:Note>
      <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
      <cac:ProcurementAdditionalType>
        <cbc:ProcurementTypeCode>Green</cbc:ProcurementTypeCode>
        <cbc:ProcurementType>Recycled steel and certified timber are asked.</cbc:ProcurementType>
      </cac:ProcurementAdditionalType>
      <cac:RequestedTenderTotal>
        <cbc:EstimatedOverallContractAmount currencyID="XBL">119760.00</cbc:EstimatedOverallContractAmount>
        <cbc:EstimatedOverallFrameworkContractsAmount currencyID="XBL">119760.00</cbc:EstimatedOverallFrameworkContractsAmount>
        <cbc:TotalAmount currencyID="XBL">119760.00</cbc:TotalAmount>
        <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
        <cbc:MinimumAmount currencyID="XBL">59880.00</cbc:MinimumAmount>
        <cbc:MaximumAmount currencyID="XBL">143712.00</cbc:MaximumAmount>
        <cbc:MonetaryScope>Two years of releases.</cbc:MonetaryScope>
        <cbc:AverageSubsequentContractAmount currencyID="XBL">19960.00</cbc:AverageSubsequentContractAmount>
        <cac:ApplicableTaxCategory>
          <cbc:ID>E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode>XB-PUBLIC</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason>Sale to a public body</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID>STT</cbc:ID>
          </cac:TaxScheme>
        </cac:ApplicableTaxCategory>
      </cac:RequestedTenderTotal>
      <cac:MainCommodityClassification>
        <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
      </cac:MainCommodityClassification>
      <cac:AdditionalCommodityClassification>
        <cbc:CommodityCode>PARKS-FURN</cbc:CommodityCode>
      </cac:AdditionalCommodityClassification>
      <cac:RealizedLocation>
        <cbc:Name>Harbour park and town parks, Lumeport</cbc:Name>
        <cac:Address>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:RealizedLocation>
      <cac:PlannedPeriod>
        <cbc:StartDate>2026-03-23</cbc:StartDate>
        <cbc:EndDate>2028-03-22</cbc:EndDate>
      </cac:PlannedPeriod>
      <cac:ContractExtension>
        <cbc:OptionsDescription>One extension of a year with 120 more benches.</cbc:OptionsDescription>
        <cbc:MinimumNumberNumeric>0</cbc:MinimumNumberNumeric>
        <cbc:MaximumNumberNumeric>1</cbc:MaximumNumberNumeric>
        <cbc:RenewalsIndicator>true</cbc:RenewalsIndicator>
        <cac:OptionValidityPeriod>
          <cbc:EndDate>2028-03-22</cbc:EndDate>
        </cac:OptionValidityPeriod>
        <cac:Renewal>
          <cbc:Amount currencyID="XBL">59880.00</cbc:Amount>
          <cac:Period>
            <cbc:DurationMeasure unitCode="MON">12</cbc:DurationMeasure>
          </cac:Period>
        </cac:Renewal>
      </cac:ContractExtension>
      <cac:RequestForTenderLine>
        <cbc:ID>1</cbc:ID>
        <cbc:UUID>b98b5bc4-6b96-59da-b8e9-89fc28afcae4</cbc:UUID>
        <cbc:Note>Steel frame, five hardwood slats, ground anchors.</cbc:Note>
        <cbc:Quantity unitCode="H87">240</cbc:Quantity>
        <cbc:MinimumQuantity unitCode="H87">120</cbc:MinimumQuantity>
        <cbc:MaximumQuantity unitCode="H87">288</cbc:MaximumQuantity>
        <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
        <cbc:MinimumAmount currencyID="XBL">350.00</cbc:MinimumAmount>
        <cbc:MaximumAmount currencyID="XBL">600.00</cbc:MaximumAmount>
        <cbc:EstimatedAmount currencyID="XBL">119760.00</cbc:EstimatedAmount>
        <cac:DocumentReference>
          <cbc:ID>PWD-SPEC-BENCH-26</cbc:ID>
        </cac:DocumentReference>
        <cac:DeliveryPeriod>
          <cbc:StartDate>2026-04-02</cbc:StartDate>
          <cbc:EndDate>2028-03-22</cbc:EndDate>
        </cac:DeliveryPeriod>
        <cac:RequiredItemLocationQuantity>
          <cbc:LeadTimeMeasure unitCode="DAY">10</cbc:LeadTimeMeasure>
        </cac:RequiredItemLocationQuantity>
        <cac:WarrantyValidityPeriod>
          <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
        </cac:WarrantyValidityPeriod>
        <cac:Item>
          <cbc:Name>Park bench, 1800 mm</cbc:Name>
        </cac:Item>
        <cac:SubRequestForTenderLine>
          <cbc:ID>1.1</cbc:ID>
          <cbc:Quantity unitCode="SET">240</cbc:Quantity>
          <cac:Item>
            <cbc:Name>Ground anchor set</cbc:Name>
          </cac:Item>
        </cac:SubRequestForTenderLine>
      </cac:RequestForTenderLine>
    </cac:ProcurementProject>
  </cac:ProcurementProjectLot>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-2</cbc:ID>
    <cac:LegalDocumentReference>
      <cbc:ID>XB-PPA-2019</cbc:ID>
    </cac:LegalDocumentReference>
    <cac:TechnicalDocumentReference>
      <cbc:ID>PWD-SPEC-LOT-2</cbc:ID>
    </cac:TechnicalDocumentReference>
    <cac:RequiredDocumentReference>
      <cbc:ID>PWD-PRICE-TPL</cbc:ID>
    </cac:RequiredDocumentReference>
    <cac:ProvidedDocumentReference>
      <cbc:ID>PWD-SITE-PLAN</cbc:ID>
    </cac:ProvidedDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>PWD-QA-26</cbc:ID>
    </cac:AdditionalDocumentReference>
    <cac:TenderingTerms>
      <cbc:Note>As for the procedure.</cbc:Note>
    </cac:TenderingTerms>
    <cac:TenderingProcess>
      <cbc:Description>As for the procedure.</cbc:Description>
    </cac:TenderingProcess>
    <cac:ProcurementProject>
      <cbc:ID>LOT-2</cbc:ID>
      <cbc:Name>Installation of the benches</cbc:Name>
      <cbc:Description>240 steel park benches with hardwood slats over two years, delivered and anchored.</cbc:Description>
      <cbc:ProcurementTypeCode>Services</cbc:ProcurementTypeCode>
      <cbc:ProcurementSubTypeCode>Installation</cbc:ProcurementSubTypeCode>
      <cbc:QualityControlCode>Inspection</cbc:QualityControlCode>
      <cbc:RequiredFeeAmount currencyID="XBL">50.00</cbc:RequiredFeeAmount>
      <cbc:FeeDescription>Electronic documents are free; paper copies cost 50 lume.</cbc:FeeDescription>
      <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
      <cbc:EstimatedOverallContractQuantity unitCode="H87">240</cbc:EstimatedOverallContractQuantity>
      <cbc:Note>Part of the parks renewal programme 2026.</cbc:Note>
      <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
      <cac:ProcurementAdditionalType>
        <cbc:ProcurementTypeCode>Green</cbc:ProcurementTypeCode>
        <cbc:ProcurementType>Recycled steel and certified timber are asked.</cbc:ProcurementType>
      </cac:ProcurementAdditionalType>
      <cac:RequestedTenderTotal>
        <cbc:EstimatedOverallContractAmount currencyID="XBL">4320.00</cbc:EstimatedOverallContractAmount>
        <cbc:EstimatedOverallFrameworkContractsAmount currencyID="XBL">4320.00</cbc:EstimatedOverallFrameworkContractsAmount>
        <cbc:TotalAmount currencyID="XBL">4320.00</cbc:TotalAmount>
        <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
        <cbc:MinimumAmount currencyID="XBL">2160.00</cbc:MinimumAmount>
        <cbc:MaximumAmount currencyID="XBL">5184.00</cbc:MaximumAmount>
        <cbc:MonetaryScope>Two years of releases.</cbc:MonetaryScope>
        <cbc:AverageSubsequentContractAmount currencyID="XBL">720.00</cbc:AverageSubsequentContractAmount>
        <cac:ApplicableTaxCategory>
          <cbc:ID>E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode>XB-PUBLIC</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason>Sale to a public body</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID>STT</cbc:ID>
          </cac:TaxScheme>
        </cac:ApplicableTaxCategory>
      </cac:RequestedTenderTotal>
      <cac:MainCommodityClassification>
        <cbc:ItemClassificationCode listID="HS">9988.00</cbc:ItemClassificationCode>
      </cac:MainCommodityClassification>
      <cac:AdditionalCommodityClassification>
        <cbc:CommodityCode>PARKS-FURN</cbc:CommodityCode>
      </cac:AdditionalCommodityClassification>
      <cac:RealizedLocation>
        <cbc:Name>Harbour park and town parks, Lumeport</cbc:Name>
        <cac:Address>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:RealizedLocation>
      <cac:PlannedPeriod>
        <cbc:StartDate>2026-03-23</cbc:StartDate>
        <cbc:EndDate>2028-03-22</cbc:EndDate>
      </cac:PlannedPeriod>
      <cac:ContractExtension>
        <cbc:OptionsDescription>One extension of a year with 120 more benches.</cbc:OptionsDescription>
        <cbc:MinimumNumberNumeric>0</cbc:MinimumNumberNumeric>
        <cbc:MaximumNumberNumeric>1</cbc:MaximumNumberNumeric>
        <cbc:RenewalsIndicator>true</cbc:RenewalsIndicator>
        <cac:OptionValidityPeriod>
          <cbc:EndDate>2028-03-22</cbc:EndDate>
        </cac:OptionValidityPeriod>
        <cac:Renewal>
          <cbc:Amount currencyID="XBL">2160.00</cbc:Amount>
          <cac:Period>
            <cbc:DurationMeasure unitCode="MON">12</cbc:DurationMeasure>
          </cac:Period>
        </cac:Renewal>
      </cac:ContractExtension>
    </cac:ProcurementProject>
  </cac:ProcurementProjectLot>
</CallForTenders>
```
