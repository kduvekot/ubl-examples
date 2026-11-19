# Tender Contract: Lumeport Public Works Department to Valdara Industries

*Example 24 of the flow "A public tender (Bayvarra)" · [Tender Contract in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TENDER-CONTRACT-SCHEMA)*

After the standstill period the authority and the manufacturer conclude the contract.

[The XML file](24-TenderContract.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:tender-contract:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Tender contract"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0210**  
  The sender's number for this document.
- `UUID` = **14fc43bd-7919-515f-82c7-a02bb3605891**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-20**  
  Concluded on Friday 20 March, the day after the standstill period ended (D28 point 1, tender/24#F13).
- `IssueTime` = **17:24:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `ContractName` = **Park benches for the parks renewal programme**  
  The name of the contract the procedure is for.
- `Note` = **The framework contract, signed by both parties.**  
  What.
- `RegulatoryDomain` = **Bayvarra public procurement**  
  The rules the contract follows.

### Previous Document Reference

Inside `PreviousDocumentReference`:

- `ID` = **LPWD-DOC-26-0208**  
  The award notification.
- `DocumentTypeCode` = **AwardedNotification** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LPWD-DOC-26-0208 is the example tender/22, a AwardedNotification; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: AwardedNotification = Awarded Notification.

### Contract Document Reference

Inside `ContractDocumentReference`:

- `ID` = **PWD-CONTRACT-2026-PARKS**  
  The signed contract.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-CONTRACT**  
  The department's seal.
- `SignatoryParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
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

- `Party/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
- `Party/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The public body's official name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register (O142); identity of Lumeport Public Works Department (world/parties.json). The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FLPB**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal list of public bodies of Bayvarra**  
  The register the public body is entered in, kept by the Bayvarra Information Service: a public body is set up by law and is in no register of businesses (D46, O142).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **PUBLIC** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of public bodies, not a register of businesses. The code is from the Trade Accord's corporate registration type list: PUBLIC = Register of public bodies.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 8235 3927**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Economic Operator Party

Inside `EconomicOperatorParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/Contact/Name` = **Bids office**  
  The party's bids office desk: the desk for its role in this document (it bids); identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Bid manager**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **tenders@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Tendering Terms

Inside `TenderingTerms`:

- `PriceRevisionFormulaDescription` = **Steel index each January.**  
  How prices change.
- `PaymentFrequencyCode` = **PERRELEASE** (listID `urn:ubl-examples:world:codelist:PaymentFrequencyCode`)  
  Payment after each release. The code is from the Trade Accord's payment frequency list: PERRELEASE = After each release.
- `AdditionalConditions` = **Benches must carry the maker's serial number.**  
  A condition.
- `PenaltyClause/ID` = **PEN-1**  
  Late completion.
- `PenaltyClause/Content` = **0.5 % of the price of the late part of a release for each working day late, at most 10 % of that price.**  
  The penalty, with the base its percentages apply to (tender/01#F20).
- `RequiredFinancialGuarantee/GuaranteeTypeCode` = **PERFORMANCE** (listID `urn:ubl-examples:world:codelist:GuaranteeTypeCode`)  
  A performance guarantee. The code is from the Trade Accord's financial guarantee type list: PERFORMANCE = Performance guarantee.
- `RequiredFinancialGuarantee/Description` = **A bank guarantee of 5 % of the contract value, from the winner, for the execution of the contract.**  
  Announced in the notices and the call, carried by the contract (D28 point 5, tender/22#F4).
- `RequiredFinancialGuarantee/LiabilityAmount` = **6204.00** (currencyID `XBL`)  
  5 % of the contract value of 124,080.00 lume.
- `RequiredFinancialGuarantee/AmountRate` = **5**  
  Five per cent of the contract value.
- `CallForTendersDocumentReference/ID` = **LPWD-DOC-26-0189**  
  The call for tenders, the procurement documents the contract was tendered under.
- `WarrantyValidityPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `PaymentTerms/Note` = **30 days after each accepted release.**  
  The terms.
- `AllowedSubcontractTerms/Description` = **Installation may be subcontracted, up to 30 % of the contract value; the tenderer stays liable for it.**  
  What may be subcontracted; the limit is the maximum below, not a precise share (tender/01#F10).
- `AllowedSubcontractTerms/SubcontractingConditionsCode` = **ALLOWED** (listID `urn:ubl-examples:world:codelist:SubcontractingConditionsCode`)  
  As a code. The code is from the Trade Accord's subcontracting conditions list: ALLOWED = Allowed.
- `AllowedSubcontractTerms/MaximumPercent` = **30**  
  At most.
- `ContractExecutionRequirement/Name` = **Recycled metal**  
  A condition of execution.
- `ContractExecutionRequirement/ExecutionRequirementCode` = **ENVIRONMENTAL** (listID `urn:ubl-examples:world:codelist:ExecutionRequirementCode`)  
  Its kind. The code is from the Trade Accord's execution requirement list: ENVIRONMENTAL = Environmental requirement.
- `ContractExecutionRequirement/Description` = **At least 30 % recycled metal in the frames.**  
  What: the frames are cast iron, not steel; Valdara's carry 35 % steel and iron scrap (O225).
- `PostAwardProcess/ElectronicCatalogueUsageIndicator` = **true**  
  A catalogue of the benches.
- `PostAwardProcess/ElectronicInvoiceAcceptedIndicator` = **true**  
  Invoices in UBL.
- `PostAwardProcess/ElectronicOrderUsageIndicator` = **true**  
  Call-offs as UBL orders.
- `PostAwardProcess/ElectronicPaymentUsageIndicator` = **true**  
  Paid by transfer.

### Tendering Process

Inside `TenderingProcess`:

- `ID` = **PWD-2026-PARKS-P**  
  The procedure.
- `ProcedureCode` = **OPEN** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  Open. The code is from the Trade Accord's procurement procedure list: OPEN = Open procedure.

### Procurement Project

Inside `ProcurementProject`:

- `Name` = **Park benches for the parks renewal programme**  
  The project, or the lot, the document is about, by the name the notices give it (tender/08#F6).
- `ProcurementTypeCode` = **SUPPLIES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  The kind of procurement; the installation is services in every document (tender/01#F4). The code is from the Trade Accord's contract nature list: SUPPLIES = Supplies.

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
- `TenderResultCode` = **AWARDED** (listID `urn:ubl-examples:world:codelist:TenderResultCode`)  
  The contract is awarded. The code is from the Trade Accord's tender result list: AWARDED = Awarded.
- `Description` = **Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.**  
  Why it won.
- `AdvertisementAmount` = **320.00** (currencyID `XBL`)  
  What the winner pays for publishing the notice, below the maximum of 500 lume.
- `AwardDate` = **2026-03-09**  
  The day of the award decision.
- `AwardTime` = **09:30:00**  
  The time of the decision, before the tenderers are told.
- `ReceivedTenderQuantity` = **2** (unitCode `EA`)  
  Two tenders: the furniture maker's first tender was withdrawn and replaced.
- `LowerTenderAmount` = **117360.00** (currencyID `XBL`)  
  The lowest tender, the furniture maker's, at its auction price of 489 lume (D28 point 6).
- `HigherTenderAmount` = **124080.00** (currencyID `XBL`)  
  The highest, the manufacturer's.
- `StartDate` = **2026-03-20**  
  The contract starts when it is signed, on Friday 20 March.
- `ReceivedElectronicTenderQuantity` = **2** (unitCode `EA`)  
  Both through the platform.
- `ReceivedForeignTenderQuantity` = **1** (unitCode `EA`)  
  The manufacturer is established in Urvania.
- `Contract/ID` = **PWD-2026-PARKS**  
  The framework contract.
- `Contract/ContractTypeCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractTypeCode`)  
  A framework contract. The code is from the Trade Accord's contract type list: FRAMEWORK = Framework agreement.
- `Contract/ValidityPeriod/StartDate` = **2026-03-20**  
  From its signature.
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
- `AwardedTenderedProject/TenderLine/ID` = **1**  
  The awarded tender's line 1, lot 1.
- `AwardedTenderedProject/TenderLine/Note` = **499 lume a bench, the contract price of every release.**  
  The unit price the releases are ordered at.
- `AwardedTenderedProject/TenderLine/Quantity` = **240** (unitCode `EA`)  
  The benches of the base quantity, over two years.
- `AwardedTenderedProject/TenderLine/LineExtensionAmount` = **119760.00** (currencyID `XBL`)  
  240 at 499 lume.
- `AwardedTenderedProject/TenderLine/Item/Name` = **Park bench Serra 180**  
  The bench tendered.
- `AwardedTenderedProject/TenderLine/ID` = **2**  
  The awarded tender's line 2, lot 2.
- `AwardedTenderedProject/TenderLine/Note` = **18 lume an installation, the contract price of every release.**  
  The unit price the releases are ordered at.
- `AwardedTenderedProject/TenderLine/Quantity` = **240** (unitCode `EA`)  
  One installation a bench.
- `AwardedTenderedProject/TenderLine/LineExtensionAmount` = **4320.00** (currencyID `XBL`)  
  240 at 18 lume.
- `AwardedTenderedProject/TenderLine/Item/Name` = **Installation of a park bench**  
  The service tendered.
- `ContractFormalizationPeriod/StartDate` = **2026-03-20**  
  The day after the standstill period ended (tender/22#F5).
- `ContractFormalizationPeriod/EndDate` = **2026-03-23**  
  Before the first call-off.
- `SubcontractTerms/UnknownPriceIndicator` = **false**  
  The price of the subcontracted part is known: the tender's installation line.
- `SubcontractTerms/Description` = **Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.**  
  What is subcontracted, as the tender named it.
- `SubcontractTerms/Amount` = **4320.00** (currencyID `XBL`)  
  The value of the installation.
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
  <cbc:CustomizationID>urn:ubl-examples:world:trns:tender-contract:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0210</cbc:ID>
  <cbc:UUID>14fc43bd-7919-515f-82c7-a02bb3605891</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-20</cbc:IssueDate>
  <cbc:IssueTime>17:24:00-01:00</cbc:IssueTime>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:Note>The framework contract, signed by both parties.</cbc:Note>
  <cbc:RegulatoryDomain>Bayvarra public procurement</cbc:RegulatoryDomain>
  <cac:PreviousDocumentReference>
    <cbc:ID>LPWD-DOC-26-0208</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">AwardedNotification</cbc:DocumentTypeCode>
  </cac:PreviousDocumentReference>
  <cac:ContractDocumentReference>
    <cbc:ID>PWD-CONTRACT-2026-PARKS</cbc:ID>
  </cac:ContractDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-CONTRACT</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
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
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
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
        <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:CompanyID>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FLPB</cbc:ID>
          <cbc:Name>Federal list of public bodies of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">PUBLIC</cbc:CorporateRegistrationTypeCode>
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
        <cbc:Telephone>+999 2 38 8235 3927</cbc:Telephone>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:6250397184</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:ContractingParty>
  <cac:EconomicOperatorParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
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
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
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
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Bids office</cbc:Name>
        <cbc:JobTitle>Bid manager</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>tenders@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
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
    <cbc:PriceRevisionFormulaDescription>Steel index each January.</cbc:PriceRevisionFormulaDescription>
    <cbc:PaymentFrequencyCode listID="urn:ubl-examples:world:codelist:PaymentFrequencyCode">PERRELEASE</cbc:PaymentFrequencyCode>
    <cbc:AdditionalConditions>Benches must carry the maker's serial number.</cbc:AdditionalConditions>
    <cac:PenaltyClause>
      <cbc:ID>PEN-1</cbc:ID>
      <cbc:Content>0.5 % of the price of the late part of a release for each working day late, at most 10 % of that price.</cbc:Content>
    </cac:PenaltyClause>
    <cac:RequiredFinancialGuarantee>
      <cbc:GuaranteeTypeCode listID="urn:ubl-examples:world:codelist:GuaranteeTypeCode">PERFORMANCE</cbc:GuaranteeTypeCode>
      <cbc:Description>A bank guarantee of 5 % of the contract value, from the winner, for the execution of the contract.</cbc:Description>
      <cbc:LiabilityAmount currencyID="XBL">6204.00</cbc:LiabilityAmount>
      <cbc:AmountRate>5</cbc:AmountRate>
    </cac:RequiredFinancialGuarantee>
    <cac:CallForTendersDocumentReference>
      <cbc:ID>LPWD-DOC-26-0189</cbc:ID>
    </cac:CallForTendersDocumentReference>
    <cac:WarrantyValidityPeriod>
      <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
    </cac:WarrantyValidityPeriod>
    <cac:PaymentTerms>
      <cbc:Note>30 days after each accepted release.</cbc:Note>
    </cac:PaymentTerms>
    <cac:AllowedSubcontractTerms>
      <cbc:Description>Installation may be subcontracted, up to 30 % of the contract value; the tenderer stays liable for it.</cbc:Description>
      <cbc:SubcontractingConditionsCode listID="urn:ubl-examples:world:codelist:SubcontractingConditionsCode">ALLOWED</cbc:SubcontractingConditionsCode>
      <cbc:MaximumPercent>30</cbc:MaximumPercent>
    </cac:AllowedSubcontractTerms>
    <cac:ContractExecutionRequirement>
      <cbc:Name>Recycled metal</cbc:Name>
      <cbc:ExecutionRequirementCode listID="urn:ubl-examples:world:codelist:ExecutionRequirementCode">ENVIRONMENTAL</cbc:ExecutionRequirementCode>
      <cbc:Description>At least 30 % recycled metal in the frames.</cbc:Description>
    </cac:ContractExecutionRequirement>
    <cac:PostAwardProcess>
      <cbc:ElectronicCatalogueUsageIndicator>true</cbc:ElectronicCatalogueUsageIndicator>
      <cbc:ElectronicInvoiceAcceptedIndicator>true</cbc:ElectronicInvoiceAcceptedIndicator>
      <cbc:ElectronicOrderUsageIndicator>true</cbc:ElectronicOrderUsageIndicator>
      <cbc:ElectronicPaymentUsageIndicator>true</cbc:ElectronicPaymentUsageIndicator>
    </cac:PostAwardProcess>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:ID>PWD-2026-PARKS-P</cbc:ID>
    <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">OPEN</cbc:ProcedureCode>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:Name>Park benches for the parks renewal programme</cbc:Name>
    <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SUPPLIES</cbc:ProcurementTypeCode>
  </cac:ProcurementProject>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-1</cbc:ID>
  </cac:ProcurementProjectLot>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-2</cbc:ID>
  </cac:ProcurementProjectLot>
  <cac:TenderResult>
    <cbc:AwardID>PWD-2026-PARKS-AWARD-1</cbc:AwardID>
    <cbc:TenderResultCode listID="urn:ubl-examples:world:codelist:TenderResultCode">AWARDED</cbc:TenderResultCode>
    <cbc:Description>Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.</cbc:Description>
    <cbc:AdvertisementAmount currencyID="XBL">320.00</cbc:AdvertisementAmount>
    <cbc:AwardDate>2026-03-09</cbc:AwardDate>
    <cbc:AwardTime>09:30:00</cbc:AwardTime>
    <cbc:ReceivedTenderQuantity unitCode="EA">2</cbc:ReceivedTenderQuantity>
    <cbc:LowerTenderAmount currencyID="XBL">117360.00</cbc:LowerTenderAmount>
    <cbc:HigherTenderAmount currencyID="XBL">124080.00</cbc:HigherTenderAmount>
    <cbc:StartDate>2026-03-20</cbc:StartDate>
    <cbc:ReceivedElectronicTenderQuantity unitCode="EA">2</cbc:ReceivedElectronicTenderQuantity>
    <cbc:ReceivedForeignTenderQuantity unitCode="EA">1</cbc:ReceivedForeignTenderQuantity>
    <cac:Contract>
      <cbc:ID>PWD-2026-PARKS</cbc:ID>
      <cbc:ContractTypeCode listID="urn:ubl-examples:world:codelist:ContractTypeCode">FRAMEWORK</cbc:ContractTypeCode>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-03-20</cbc:StartDate>
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
      <cac:TenderLine>
        <cbc:ID>1</cbc:ID>
        <cbc:Note>499 lume a bench, the contract price of every release.</cbc:Note>
        <cbc:Quantity unitCode="EA">240</cbc:Quantity>
        <cbc:LineExtensionAmount currencyID="XBL">119760.00</cbc:LineExtensionAmount>
        <cac:Item>
          <cbc:Name>Park bench Serra 180</cbc:Name>
        </cac:Item>
      </cac:TenderLine>
      <cac:TenderLine>
        <cbc:ID>2</cbc:ID>
        <cbc:Note>18 lume an installation, the contract price of every release.</cbc:Note>
        <cbc:Quantity unitCode="EA">240</cbc:Quantity>
        <cbc:LineExtensionAmount currencyID="XBL">4320.00</cbc:LineExtensionAmount>
        <cac:Item>
          <cbc:Name>Installation of a park bench</cbc:Name>
        </cac:Item>
      </cac:TenderLine>
    </cac:AwardedTenderedProject>
    <cac:ContractFormalizationPeriod>
      <cbc:StartDate>2026-03-20</cbc:StartDate>
      <cbc:EndDate>2026-03-23</cbc:EndDate>
    </cac:ContractFormalizationPeriod>
    <cac:SubcontractTerms>
      <cbc:UnknownPriceIndicator>false</cbc:UnknownPriceIndicator>
      <cbc:Description>Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.</cbc:Description>
      <cbc:Amount currencyID="XBL">4320.00</cbc:Amount>
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
