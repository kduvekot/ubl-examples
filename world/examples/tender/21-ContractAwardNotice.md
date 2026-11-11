# Contract Award Notice: Lumeport Public Works Department to Bayvarra Information Service

*Example 21 of the flow "A public tender (Bayvarra)" · [Contract Award Notice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CONTRACT-AWARD-NOTICE-SCHEMA)*

The award is published; the review body is named for appeals.

[The XML file](21-ContractAwardNotice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:contract-award-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Contract award notice"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0207**  
  The notice number.
- `UUID` = **12583d9b-2491-50ee-89c4-489940d246f5**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-13**  
  Published four days after the award decision, while the standstill period runs.
- `IssueTime` = **13:55:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Award of the framework contract for park benches.**  
  What.
- `VersionID` = **1**  
  The first version.
- `RequestedPublicationDate` = **2026-03-14**  
  When to publish.
- `RegulatoryDomain` = **Bayvarra public procurement**  
  The rules the notice follows.
- `NoticeTypeCode` = **CAN** (listID `urn:ubl-examples:world:codelist:NoticeTypeCode`)  
  The kind of notice. The code is from the Trade Accord's notice type list: CAN = Contract award notice.
- `PublishAwardIndicator` = **true**  
  The award is published.
- `NoticeLanguageCode` = **en** (listID `ISO 639`)  
  In English, as an ISO 639 code. The code is from the world's copy of ISO 639 Language: en = English.

### Additional Notice Language

Inside `AdditionalNoticeLanguage`:

- `ID` = **qau** (schemeID `ISO 639`)  
  Also published in Urvanian, for tenderers from Urvania (a code from ISO 639's local-use range: the world's languages are invented). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Name` = **Urvanian**  
  The language's name.

### Previous Document Reference

Inside `PreviousDocumentReference`:

- `ID` = **LPWD-DOC-26-0188**  
  The contract notice.

### Minutes Document Reference

Inside `MinutesDocumentReference`:

- `ID` = **PWD-MIN-AWARD-26**  
  The minutes of the evaluation.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-CAN**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

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

- `IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Bayvarra Information Service (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 8411 = General public administration activities.
- `PartyIdentification/ID` = **20410959** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayvarra Information Service (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayvarra Information Service**  
  The trading name; identity of Bayvarra Information Service (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **LUM-ADR-634627** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/BuildingNumber` = **27**  
  Building number of the postal address. identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/PostalZone` = **38520**  
  Postal code in Bayvarra's format (5 digits). identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayvarra Information Service (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Bayvarra Information Service**  
  The name under which the party is registered, with its legal form; identity of Bayvarra Information Service (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410959** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Bayvarra Information Service (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
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
- `Contact/Name` = **Publications and register**  
  The desk that handles this document; identity of Bayvarra Information Service (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Bayvarra Information Service (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Bayvarra Information Service (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2259 0959**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayvarra Information Service (world/parties.json).
- `Contact/ElectronicMail` = **publications@info-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayvarra Information Service (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayvarra Information Service (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayvarra Information Service (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tendering Terms

Inside `TenderingTerms`:

- `AppealTerms/AppealReceiverParty/IndustryClassificationCode` = **8423** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Procurement Review Board of Bayvarra (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 8423 = Public order and safety activities.
- `AppealTerms/AppealReceiverParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AppealTerms/AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  The trading name; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `AppealTerms/AppealReceiverParty/Language/Name` = **English**  
  The language's name.
- `AppealTerms/AppealReceiverParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `AppealTerms/AppealReceiverParty/PostalAddress/ID` = **LUM-ADR-075593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `AppealTerms/AppealReceiverParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `AppealTerms/AppealReceiverParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Procurement Review Board of Bayvarra (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `AppealTerms/AppealReceiverParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `AppealTerms/AppealReceiverParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AppealTerms/AppealReceiverParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/RegistrationName` = **Procurement Review Board of Bayvarra**  
  The name under which the party is registered, with its legal form; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CompanyID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `AppealTerms/AppealReceiverParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AppealTerms/AppealReceiverParty/Contact/Name` = **Registry**  
  The desk that handles this document; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/Telephone` = **+999 2 38 2122 0822**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/ElectronicMail` = **registry@review-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealTerms/AppealReceiverParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `AppealTerms/AppealReceiverParty/ElectronicAddress/ElectronicAddressID` = **XB:20410822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Procurement Review Board of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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
- `ProcedureCode` = **OPEN** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  An open procedure. The code is from the Trade Accord's procurement procedure list: OPEN = Open procedure.
- `UrgencyCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:UrgencyCode`)  
  No urgency. The code is from the Trade Accord's urgency list: NORMAL = Normal.
- `ExpenseCode` = **INVESTMENT** (listID `urn:ubl-examples:world:codelist:ExpenseTypeCode`)  
  Paid from the investment budget. The code is from the Trade Accord's expense type list: INVESTMENT = Investment budget.
- `PartPresentationCode` = **ONEORMORE** (listID `urn:ubl-examples:world:codelist:LotSubmissionCode`)  
  Tenders for one or both lots. The code is from the Trade Accord's lot submission list: ONEORMORE = One or more lots.
- `ContractingSystemCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractingSystemCode`)  
  A framework agreement. The code is from the Trade Accord's contracting system list: FRAMEWORK = Framework agreement.
- `SubmissionMethodCode` = **ELECTRONIC** (listID `urn:ubl-examples:world:codelist:SubmissionMethodCode`)  
  Tenders are submitted electronically. The code is from the Trade Accord's submission method list: ELECTRONIC = Electronic.
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
- `ProcessJustification/ProcessReasonCode` = **STANDARD** (listID `urn:ubl-examples:world:codelist:ProcessReasonCode`)  
  The open procedure is the rule. The code is from the Trade Accord's process reason list: STANDARD = Standard.
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
- `OpenTenderEvent/TypeCode` = **OPENING** (listID `urn:ubl-examples:world:codelist:TenderEventTypeCode`)  
  A tender opening. The code is from the Trade Accord's tender event type list: OPENING = Opening of tenders.
- `OpenTenderEvent/Description` = **Electronic opening; tenderers may follow it online.**  
  How.
- `OpenTenderEvent/CompletionIndicator` = **false**  
  To come.
- `OpenTenderEvent/CurrentStatus/ConditionCode` = **SCHEDULED** (listID `urn:ubl-examples:world:codelist:StatusConditionCode`)  
  Planned. The code is from the Trade Accord's status condition list: SCHEDULED = Scheduled.
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
- `ContractingSystem/ContractingSystemTypeCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractingSystemTypeCode`)  
  A framework agreement. The code is from the Trade Accord's contracting system type list: FRAMEWORK = Framework agreement.
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
- `ProcurementTypeCode` = **SUPPLIES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  Supplies or services. The code is from the Trade Accord's contract nature list: SUPPLIES = Supplies.
- `ProcurementSubTypeCode` = **PURCHASE** (listID `urn:ubl-examples:world:codelist:ProcurementSubTypeCode`)  
  The kind within it. The code is from the Trade Accord's procurement subtype list: PURCHASE = Purchase.
- `QualityControlCode` = **INSPECTION** (listID `urn:ubl-examples:world:codelist:QualityControlCode`)  
  Each release is inspected on delivery. The code is from the Trade Accord's quality control list: INSPECTION = Inspection on delivery.
- `RequiredFeeAmount` = **50.00** (currencyID `XBL`)  
  The fee for the tender documents on paper.
- `FeeDescription` = **Electronic documents are free; paper copies cost 50 lume.**  
  The fee.
- `RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `EstimatedOverallContractQuantity` = **240** (unitCode `EA`)  
  240 benches over the contract.
- `Note` = **Part of the parks renewal programme 2026.**  
  The programme.
- `SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementAdditionalType/ProcurementTypeCode` = **GREEN** (listID `urn:ubl-examples:world:codelist:StrategicProcurementCode`)  
  Green public procurement. The code is from the Trade Accord's strategic procurement list: GREEN = Environmental impact.
- `ProcurementAdditionalType/ProcurementType` = **Environmental impact: recycled steel and certified timber are asked**  
  The name of code GREEN in the Trade Accord's strategic procurement list, followed by the detail of this case: what the green criteria ask for.
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
- `RequestedTenderTotal/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a public body is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **PUBLIC** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Sale to a public body.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Sale to a public body**  
  The name of code PUBLIC in Bayvarra's national sales tax exemption reason list.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `MainCommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What is bought, as a subclass of the UN Central Product Classification, which classifies goods and services alike: seats with metal frames. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `AdditionalCommodityClassification/ItemClassificationCode` = **381** (listID `UN CPC Ver.2.1`)  
  The wider category of the procurement, as a group of the UN CPC: furniture. The code is from the world's copy of UN Central Product Classification, Version 2.1: 381 = Furniture.
- `RealizedLocation/Name` = **Harbour park and town parks, Lumeport**  
  Where the benches go.
- `RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `RealizedLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
- `RequestForTenderLine/Quantity` = **240** (unitCode `EA`)  
  Over the contract.
- `RequestForTenderLine/MinimumQuantity` = **120** (unitCode `EA`)  
  At least.
- `RequestForTenderLine/MaximumQuantity` = **288** (unitCode `EA`)  
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
- `ProcurementProject/ProcurementTypeCode` = **SUPPLIES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  Supplies or services. The code is from the Trade Accord's contract nature list: SUPPLIES = Supplies.
- `ProcurementProject/ProcurementSubTypeCode` = **PURCHASE** (listID `urn:ubl-examples:world:codelist:ProcurementSubTypeCode`)  
  The kind within it. The code is from the Trade Accord's procurement subtype list: PURCHASE = Purchase.
- `ProcurementProject/QualityControlCode` = **INSPECTION** (listID `urn:ubl-examples:world:codelist:QualityControlCode`)  
  Each release is inspected on delivery. The code is from the Trade Accord's quality control list: INSPECTION = Inspection on delivery.
- `ProcurementProject/RequiredFeeAmount` = **50.00** (currencyID `XBL`)  
  The fee for the tender documents on paper.
- `ProcurementProject/FeeDescription` = **Electronic documents are free; paper copies cost 50 lume.**  
  The fee.
- `ProcurementProject/RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `ProcurementProject/EstimatedOverallContractQuantity` = **240** (unitCode `EA`)  
  240 benches over the contract.
- `ProcurementProject/Note` = **Part of the parks renewal programme 2026.**  
  The programme.
- `ProcurementProject/SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementProject/ProcurementAdditionalType/ProcurementTypeCode` = **GREEN** (listID `urn:ubl-examples:world:codelist:StrategicProcurementCode`)  
  Green public procurement. The code is from the Trade Accord's strategic procurement list: GREEN = Environmental impact.
- `ProcurementProject/ProcurementAdditionalType/ProcurementType` = **Environmental impact: recycled steel and certified timber are asked**  
  The name of code GREEN in the Trade Accord's strategic procurement list, followed by the detail of this case: what the green criteria ask for.
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
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a public body is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **PUBLIC** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Sale to a public body.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Sale to a public body**  
  The name of code PUBLIC in Bayvarra's national sales tax exemption reason list.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `ProcurementProject/MainCommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What is bought, as a subclass of the UN Central Product Classification, which classifies goods and services alike: seats with metal frames. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `ProcurementProject/AdditionalCommodityClassification/ItemClassificationCode` = **381** (listID `UN CPC Ver.2.1`)  
  The wider category of the procurement, as a group of the UN CPC: furniture. The code is from the world's copy of UN Central Product Classification, Version 2.1: 381 = Furniture.
- `ProcurementProject/RealizedLocation/Name` = **Harbour park and town parks, Lumeport**  
  Where the benches go.
- `ProcurementProject/RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `ProcurementProject/RealizedLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
- `ProcurementProject/RequestForTenderLine/Quantity` = **240** (unitCode `EA`)  
  Over the contract.
- `ProcurementProject/RequestForTenderLine/MinimumQuantity` = **120** (unitCode `EA`)  
  At least.
- `ProcurementProject/RequestForTenderLine/MaximumQuantity` = **288** (unitCode `EA`)  
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
- `ProcurementProject/ProcurementTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  Supplies or services. The code is from the Trade Accord's contract nature list: SERVICES = Services.
- `ProcurementProject/ProcurementSubTypeCode` = **INSTALL** (listID `urn:ubl-examples:world:codelist:ProcurementSubTypeCode`)  
  The kind within it. The code is from the Trade Accord's procurement subtype list: INSTALL = Installation.
- `ProcurementProject/QualityControlCode` = **INSPECTION** (listID `urn:ubl-examples:world:codelist:QualityControlCode`)  
  Each release is inspected on delivery. The code is from the Trade Accord's quality control list: INSPECTION = Inspection on delivery.
- `ProcurementProject/RequiredFeeAmount` = **50.00** (currencyID `XBL`)  
  The fee for the tender documents on paper.
- `ProcurementProject/FeeDescription` = **Electronic documents are free; paper copies cost 50 lume.**  
  The fee.
- `ProcurementProject/RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `ProcurementProject/EstimatedOverallContractQuantity` = **240** (unitCode `EA`)  
  240 benches over the contract.
- `ProcurementProject/Note` = **Part of the parks renewal programme 2026.**  
  The programme.
- `ProcurementProject/SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementProject/ProcurementAdditionalType/ProcurementTypeCode` = **GREEN** (listID `urn:ubl-examples:world:codelist:StrategicProcurementCode`)  
  Green public procurement. The code is from the Trade Accord's strategic procurement list: GREEN = Environmental impact.
- `ProcurementProject/ProcurementAdditionalType/ProcurementType` = **Environmental impact: recycled steel and certified timber are asked**  
  The name of code GREEN in the Trade Accord's strategic procurement list, followed by the detail of this case: what the green criteria ask for.
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
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a public body is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **PUBLIC** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Sale to a public body.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Sale to a public body**  
  The name of code PUBLIC in Bayvarra's national sales tax exemption reason list.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `ProcurementProject/MainCommodityClassification/ItemClassificationCode` = **87390** (listID `UN CPC Ver.2.1`)  
  What is bought, as a subclass of the UN Central Product Classification, which classifies services as well: installation services of other goods. The code is from the world's copy of UN Central Product Classification, Version 2.1: 87390 = Installation services of other goods n.e.c..
- `ProcurementProject/AdditionalCommodityClassification/ItemClassificationCode` = **381** (listID `UN CPC Ver.2.1`)  
  The wider category of the procurement, as a group of the UN CPC: furniture. The code is from the world's copy of UN Central Product Classification, Version 2.1: 381 = Furniture.
- `ProcurementProject/RealizedLocation/Name` = **Harbour park and town parks, Lumeport**  
  Where the benches go.
- `ProcurementProject/RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `ProcurementProject/RealizedLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
  The day the authority decided the award.
- `AwardTime` = **09:30:00**  
  The time of the decision, before the tenderers are told.
- `ReceivedTenderQuantity` = **2** (unitCode `EA`)  
  Two tenders: the furniture maker's first tender was withdrawn and replaced.
- `LowerTenderAmount` = **119040.00** (currencyID `XBL`)  
  The lowest tender, the furniture maker's.
- `HigherTenderAmount` = **124080.00** (currencyID `XBL`)  
  The highest, the manufacturer's.
- `StartDate` = **2026-03-23**  
  The contract starts with the first call-off.
- `ReceivedElectronicTenderQuantity` = **2** (unitCode `EA`)  
  Both through the platform.
- `ReceivedForeignTenderQuantity` = **1** (unitCode `EA`)  
  The manufacturer is established in Urvania.
- `Contract/ID` = **PWD-2026-PARKS**  
  The framework contract.
- `Contract/ContractTypeCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractTypeCode`)  
  A framework contract. The code is from the Trade Accord's contract type list: FRAMEWORK = Framework agreement.
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
- `WinningParty/Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `WinningParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `WinningParty/Party/AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `WinningParty/Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `WinningParty/Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `WinningParty/Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `WinningParty/Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XB`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XB`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `WinningParty/Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `WinningParty/Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `WinningParty/Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PartyTaxScheme/CompanyID` = **XU007299291** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `WinningParty/Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `WinningParty/Party/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `WinningParty/Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `WinningParty/Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `WinningParty/Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `WinningParty/Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `WinningParty/Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The name of code SUA in Urvania's national company legal form list.
- `WinningParty/Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 3083 persons and its turnover of 23600000000 XUF in 2025, by the Trade Accord's limits; identity of Valdara Industries (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `WinningParty/Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `WinningParty/Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `WinningParty/Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `WinningParty/Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `WinningParty/Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `WinningParty/Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `WinningParty/Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `WinningParty/Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `WinningParty/Party/PartyLegalEntity/SecurityListing/ID` = **XU0001042501** (schemeID `ISO 6166`)  
  The identifier of the listed shares, in the form of an ISIN with the world's country code. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `WinningParty/Party/PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `WinningParty/Party/PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The name of code XFER in the Trade Accord's market identifier list.
- `WinningParty/Party/PartyLegalEntity/SecurityListing/MarketCode` = **XFER** (listID `urn:ubl-examples:world:codelist:MarketCode`)  
  The market's code. The code is from the Trade Accord's market identifier list: XFER = Ferrano Stock Exchange.
- `WinningParty/Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `WinningParty/Party/Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `WinningParty/Party/ServiceProviderParty/ID` = **VI-SP-2026-01**  
  The number of the service contract between the two; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/ServiceProviderParty/ServiceTypeCode` = **LOGISTICS** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  The kind of service, as a code. The code is from the Trade Accord's service type list: LOGISTICS = Logistics service.
- `WinningParty/Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `WinningParty/Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `WinningParty/Party/ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `WinningParty/Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `WinningParty/Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ContractAwardNotice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ContractAwardNotice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:contract-award-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0207</cbc:ID>
  <cbc:UUID>12583d9b-2491-50ee-89c4-489940d246f5</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-13</cbc:IssueDate>
  <cbc:IssueTime>13:55:00</cbc:IssueTime>
  <cbc:Note>Award of the framework contract for park benches.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:RequestedPublicationDate>2026-03-14</cbc:RequestedPublicationDate>
  <cbc:RegulatoryDomain>Bayvarra public procurement</cbc:RegulatoryDomain>
  <cbc:NoticeTypeCode listID="urn:ubl-examples:world:codelist:NoticeTypeCode">CAN</cbc:NoticeTypeCode>
  <cbc:PublishAwardIndicator>true</cbc:PublishAwardIndicator>
  <cbc:NoticeLanguageCode listID="ISO 639">en</cbc:NoticeLanguageCode>
  <cac:AdditionalNoticeLanguage>
    <cbc:ID schemeID="ISO 639">qau</cbc:ID>
    <cbc:Name>Urvanian</cbc:Name>
  </cac:AdditionalNoticeLanguage>
  <cac:PreviousDocumentReference>
    <cbc:ID>LPWD-DOC-26-0188</cbc:ID>
  </cac:PreviousDocumentReference>
  <cac:MinutesDocumentReference>
    <cbc:ID>PWD-MIN-AWARD-26</cbc:ID>
  </cac:MinutesDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-CAN</cbc:ID>
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
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayvarra Information Service</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-634627</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Civic Square</cbc:StreetName>
      <cbc:BuildingNumber>27</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38520</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Bayvarra Information Service</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410959</cbc:CompanyID>
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
      <cbc:Name>Publications and register</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 2 38 2259 0959</cbc:Telephone>
      <cbc:ElectronicMail>publications@info-xb.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410959</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:TenderingTerms>
    <cac:AppealTerms>
      <cac:AppealReceiverParty>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">8423</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-075593</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Justice Row</cbc:StreetName>
          <cbc:BuildingNumber>20</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38519</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Procurement Review Board of Bayvarra</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:CompanyID>
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
          <cbc:Name>Registry</cbc:Name>
          <cbc:JobTitle>Procurement officer</cbc:JobTitle>
          <cbc:Department>Procurement</cbc:Department>
          <cbc:Telephone>+999 2 38 2122 0822</cbc:Telephone>
          <cbc:ElectronicMail>registry@review-xb.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410822</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:AppealReceiverParty>
    </cac:AppealTerms>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:ID>PWD-2026-PARKS-P</cbc:ID>
    <cbc:OriginalContractingSystemID>PWD-FW-2024-PARKS</cbc:OriginalContractingSystemID>
    <cbc:Description>Open procedure with two lots.</cbc:Description>
    <cbc:NegotiationDescription>No negotiation: the award is on the tenders as submitted.</cbc:NegotiationDescription>
    <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">OPEN</cbc:ProcedureCode>
    <cbc:UrgencyCode listID="urn:ubl-examples:world:codelist:UrgencyCode">NORMAL</cbc:UrgencyCode>
    <cbc:ExpenseCode listID="urn:ubl-examples:world:codelist:ExpenseTypeCode">INVESTMENT</cbc:ExpenseCode>
    <cbc:PartPresentationCode listID="urn:ubl-examples:world:codelist:LotSubmissionCode">ONEORMORE</cbc:PartPresentationCode>
    <cbc:ContractingSystemCode listID="urn:ubl-examples:world:codelist:ContractingSystemCode">FRAMEWORK</cbc:ContractingSystemCode>
    <cbc:SubmissionMethodCode listID="urn:ubl-examples:world:codelist:SubmissionMethodCode">ELECTRONIC</cbc:SubmissionMethodCode>
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
      <cbc:ProcessReasonCode listID="urn:ubl-examples:world:codelist:ProcessReasonCode">STANDARD</cbc:ProcessReasonCode>
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
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:TenderEventTypeCode">OPENING</cbc:TypeCode>
      <cbc:Description>Electronic opening; tenderers may follow it online.</cbc:Description>
      <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
      <cac:CurrentStatus>
        <cbc:ConditionCode listID="urn:ubl-examples:world:codelist:StatusConditionCode">SCHEDULED</cbc:ConditionCode>
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
      <cbc:ContractingSystemTypeCode listID="urn:ubl-examples:world:codelist:ContractingSystemTypeCode">FRAMEWORK</cbc:ContractingSystemTypeCode>
      <cbc:Description>Framework with one supplier.</cbc:Description>
    </cac:ContractingSystem>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:ID>PWD-2026-PARKS</cbc:ID>
    <cbc:Name>Park benches for the parks renewal programme</cbc:Name>
    <cbc:Description>240 steel park benches with hardwood slats over two years, delivered and anchored.</cbc:Description>
    <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SUPPLIES</cbc:ProcurementTypeCode>
    <cbc:ProcurementSubTypeCode listID="urn:ubl-examples:world:codelist:ProcurementSubTypeCode">PURCHASE</cbc:ProcurementSubTypeCode>
    <cbc:QualityControlCode listID="urn:ubl-examples:world:codelist:QualityControlCode">INSPECTION</cbc:QualityControlCode>
    <cbc:RequiredFeeAmount currencyID="XBL">50.00</cbc:RequiredFeeAmount>
    <cbc:FeeDescription>Electronic documents are free; paper copies cost 50 lume.</cbc:FeeDescription>
    <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
    <cbc:EstimatedOverallContractQuantity unitCode="EA">240</cbc:EstimatedOverallContractQuantity>
    <cbc:Note>Part of the parks renewal programme 2026.</cbc:Note>
    <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
    <cac:ProcurementAdditionalType>
      <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:StrategicProcurementCode">GREEN</cbc:ProcurementTypeCode>
      <cbc:ProcurementType>Environmental impact: recycled steel and certified timber are asked</cbc:ProcurementType>
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
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">PUBLIC</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Sale to a public body</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequestedTenderTotal>
    <cac:MainCommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
    </cac:MainCommodityClassification>
    <cac:AdditionalCommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">381</cbc:ItemClassificationCode>
    </cac:AdditionalCommodityClassification>
    <cac:RealizedLocation>
      <cbc:Name>Harbour park and town parks, Lumeport</cbc:Name>
      <cac:Address>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
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
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cbc:MinimumQuantity unitCode="EA">120</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">288</cbc:MaximumQuantity>
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
      <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SUPPLIES</cbc:ProcurementTypeCode>
      <cbc:ProcurementSubTypeCode listID="urn:ubl-examples:world:codelist:ProcurementSubTypeCode">PURCHASE</cbc:ProcurementSubTypeCode>
      <cbc:QualityControlCode listID="urn:ubl-examples:world:codelist:QualityControlCode">INSPECTION</cbc:QualityControlCode>
      <cbc:RequiredFeeAmount currencyID="XBL">50.00</cbc:RequiredFeeAmount>
      <cbc:FeeDescription>Electronic documents are free; paper copies cost 50 lume.</cbc:FeeDescription>
      <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
      <cbc:EstimatedOverallContractQuantity unitCode="EA">240</cbc:EstimatedOverallContractQuantity>
      <cbc:Note>Part of the parks renewal programme 2026.</cbc:Note>
      <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
      <cac:ProcurementAdditionalType>
        <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:StrategicProcurementCode">GREEN</cbc:ProcurementTypeCode>
        <cbc:ProcurementType>Environmental impact: recycled steel and certified timber are asked</cbc:ProcurementType>
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
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">PUBLIC</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason>Sale to a public body</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          </cac:TaxScheme>
        </cac:ApplicableTaxCategory>
      </cac:RequestedTenderTotal>
      <cac:MainCommodityClassification>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
      </cac:MainCommodityClassification>
      <cac:AdditionalCommodityClassification>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">381</cbc:ItemClassificationCode>
      </cac:AdditionalCommodityClassification>
      <cac:RealizedLocation>
        <cbc:Name>Harbour park and town parks, Lumeport</cbc:Name>
        <cac:Address>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
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
        <cbc:Quantity unitCode="EA">240</cbc:Quantity>
        <cbc:MinimumQuantity unitCode="EA">120</cbc:MinimumQuantity>
        <cbc:MaximumQuantity unitCode="EA">288</cbc:MaximumQuantity>
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
      <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SERVICES</cbc:ProcurementTypeCode>
      <cbc:ProcurementSubTypeCode listID="urn:ubl-examples:world:codelist:ProcurementSubTypeCode">INSTALL</cbc:ProcurementSubTypeCode>
      <cbc:QualityControlCode listID="urn:ubl-examples:world:codelist:QualityControlCode">INSPECTION</cbc:QualityControlCode>
      <cbc:RequiredFeeAmount currencyID="XBL">50.00</cbc:RequiredFeeAmount>
      <cbc:FeeDescription>Electronic documents are free; paper copies cost 50 lume.</cbc:FeeDescription>
      <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
      <cbc:EstimatedOverallContractQuantity unitCode="EA">240</cbc:EstimatedOverallContractQuantity>
      <cbc:Note>Part of the parks renewal programme 2026.</cbc:Note>
      <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
      <cac:ProcurementAdditionalType>
        <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:StrategicProcurementCode">GREEN</cbc:ProcurementTypeCode>
        <cbc:ProcurementType>Environmental impact: recycled steel and certified timber are asked</cbc:ProcurementType>
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
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">PUBLIC</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason>Sale to a public body</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          </cac:TaxScheme>
        </cac:ApplicableTaxCategory>
      </cac:RequestedTenderTotal>
      <cac:MainCommodityClassification>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">87390</cbc:ItemClassificationCode>
      </cac:MainCommodityClassification>
      <cac:AdditionalCommodityClassification>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">381</cbc:ItemClassificationCode>
      </cac:AdditionalCommodityClassification>
      <cac:RealizedLocation>
        <cbc:Name>Harbour park and town parks, Lumeport</cbc:Name>
        <cac:Address>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
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
  <cac:TenderResult>
    <cbc:AwardID>PWD-2026-PARKS-AWARD-1</cbc:AwardID>
    <cbc:TenderResultCode listID="urn:ubl-examples:world:codelist:TenderResultCode">AWARDED</cbc:TenderResultCode>
    <cbc:Description>Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.</cbc:Description>
    <cbc:AdvertisementAmount currencyID="XBL">320.00</cbc:AdvertisementAmount>
    <cbc:AwardDate>2026-03-09</cbc:AwardDate>
    <cbc:AwardTime>09:30:00</cbc:AwardTime>
    <cbc:ReceivedTenderQuantity unitCode="EA">2</cbc:ReceivedTenderQuantity>
    <cbc:LowerTenderAmount currencyID="XBL">119040.00</cbc:LowerTenderAmount>
    <cbc:HigherTenderAmount currencyID="XBL">124080.00</cbc:HigherTenderAmount>
    <cbc:StartDate>2026-03-23</cbc:StartDate>
    <cbc:ReceivedElectronicTenderQuantity unitCode="EA">2</cbc:ReceivedElectronicTenderQuantity>
    <cbc:ReceivedForeignTenderQuantity unitCode="EA">1</cbc:ReceivedForeignTenderQuantity>
    <cac:Contract>
      <cbc:ID>PWD-2026-PARKS</cbc:ID>
      <cbc:ContractTypeCode listID="urn:ubl-examples:world:codelist:ContractTypeCode">FRAMEWORK</cbc:ContractTypeCode>
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
          <cbc:StreetName languageID="en-XB">Via delle Officine</cbc:StreetName>
          <cbc:BuildingNumber>17</cbc:BuildingNumber>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XB">Ferrano</cbc:CityName>
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
          <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
          <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
          <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
          <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
          <cac:RegistrationAddress>
            <cbc:CityName>Ferrano</cbc:CityName>
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
    </cac:WinningParty>
  </cac:TenderResult>
</ContractAwardNotice>
```
