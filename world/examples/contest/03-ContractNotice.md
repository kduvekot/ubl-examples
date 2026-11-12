# Contract Notice: Lumeport Public Works Department to Bayvarra Information Service

*Example 3 of the flow "A design contest for the promenade bench (Bayvarra)" · [Contract Notice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CONTRACT-NOTICE-SCHEMA)*

The contest notice: a restricted design contest with three prizes, relaunched after the earlier contest was cancelled; a group must form a limited company before the follow-up contract.

[The XML file](03-ContractNotice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:contract-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Contract notice"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **CONTEST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0634**  
  The notice number, the same in both versions.
- `UUID` = **88a68511-926f-5847-b468-9a248742facd**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PROM-DC**  
  The department's file number for the contest, the same on every document of it.
- `IssueDate` = **2026-03-19**  
  Published on the date the revised prior information notice gave.
- `IssueTime` = **08:51:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Restricted design contest for the harbour promenade bench, with three prizes.**  
  What.
- `VersionID` = **1**  
  The first version.
- `NoticeTypeCode` = **CN** (listID `urn:ubl-examples:world:codelist:NoticeTypeCode`)  
  A contract notice; that it corrects version 1 is said by its version identifiers. The code is from the Trade Accord's notice type list: CN = Contract notice.

### Contracting Party

Inside `ContractingParty`:

- `BuyerProfileURI` = **https://tenders.lumeport.example/buyers/pwd**  
  The buyer's profile.
- `ContractingPartyType/PartyTypeCode` = **LOCAL** (listID `urn:ubl-examples:world:codelist:ContractingPartyTypeCode`)  
  A local authority. The code is from the Trade Accord's contracting party type list: LOCAL = Local authority.
- `ContractingPartyType/PartyType` = **Local authority: a department of the city of Lumeport**  
  The name of code LOCAL in the Trade Accord's contracting party type list, followed by the detail of this case: the buyer is the city's parks department.
- `ContractingActivity/ActivityTypeCode` = **COMMUNITY** (listID `urn:ubl-examples:world:codelist:AuthorityActivityCode`)  
  Its activity. The code is from the Trade Accord's authority activity list: COMMUNITY = Housing and community amenities.
- `ContractingActivity/ActivityType` = **Housing and community amenities: public works and parks**  
  The name of code COMMUNITY in the Trade Accord's authority activity list, followed by the detail of this case: the department's field.
- `ContractingRepresentationType/RepresentationTypeCode` = **OWN** (listID `urn:ubl-examples:world:codelist:RepresentationTypeCode`)  
  On its own behalf. The code is from the Trade Accord's representation type list: OWN = On its own behalf.
- `ContractingRepresentationType/RepresentationType` = **On its own behalf**  
  The name of code OWN in the Trade Accord's representation type list.
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

- `TendererQualificationRequest/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form the department asks for: a group of designers and engineers must form a private limited company before the follow-up service contract is awarded, as the procurement act allows where the contract needs one liable contractor. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `TendererQualificationRequest/CompanyLegalForm` = **Limited company (private): a group of participants forms one before the follow-up contract is awarded; for the contest itself a group names a lead member**  
  The name of code LTD in Bayvarra's national company legal form list, followed by the detail of this case: the requirement applies to a group, and only before the follow-up contract.
- `TendererQualificationRequest/Description` = **The design lead is a registered architect.**  
  The professional qualification asked for.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/EvaluationCriterionTypeCode` = **REFERENCES** (listID `urn:ubl-examples:world:codelist:EvaluationCriterionTypeCode`)  
  References. The code is from the Trade Accord's evaluation criterion type list: REFERENCES = References.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/Description` = **Two completed designs of furniture or fittings for public spaces in the last five years.**  
  What the jury checks to select the participants.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/ThresholdQuantity` = **2** (unitCode `EA`)  
  Two references.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/DurationPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `TendererQualificationRequest/EconomicOperatorRole/RoleCode` = **LEAD** (listID `urn:ubl-examples:world:codelist:EconomicOperatorRoleCode`)  
  A group names a lead member for the contest. The code is from the Trade Accord's economic operator role list: LEAD = Consortium lead.
- `TendererQualificationRequest/EconomicOperatorRole/RoleDescription` = **Represents the group towards the department.**  
  The role in words.
- `AwardingTerms/Description` = **The jury ranks the designs anonymously, on design quality (40 %), durability and maintenance in salt air (30 %) and the cost of production (30 %).**  
  How the designs are judged.
- `AwardingTerms/TechnicalCommitteeDescription` = **A jury of five: the head of parks, the city architect, a representative of the disability council and two independent designers.**  
  Who judges.
- `AwardingTerms/PrizeIndicator` = **true**  
  A design contest with prizes.
- `AwardingTerms/PrizeDescription` = **Three prizes; the first is 8,000 lume.**  
  The prizes in words; each is given below.
- `AwardingTerms/PaymentDescription` = **Each selected participant that submits a design meeting the brief receives 1,000 lume towards its costs, whether or not it wins a prize.**  
  The payment to all participants, besides the prizes.
- `AwardingTerms/FollowupContractIndicator` = **true**  
  The winner of the first prize is invited to negotiate the service contract for the detailed design and the supervision of the production, without a new call for competition.
- `AwardingTerms/BindingOnBuyerIndicator` = **true**  
  The jury's ranking binds the department.
- `AwardingTerms/Prize/RankCode` = **FIRST** (listID `urn:ubl-examples:world:codelist:PrizeRankCode`)  
  The first prize. The code is from the Trade Accord's prize rank list: FIRST = First prize.
- `AwardingTerms/Prize/ValueAmount` = **8000.00** (currencyID `XBL`)  
  The first prize, as the city council raised it before the contest was announced.
- `AwardingTerms/Prize/Description` = **For the design the jury ranks first; its author is invited to negotiate the follow-up service contract.**  
  What comes with the prize.
- `AwardingTerms/Prize/RankCode` = **SECOND** (listID `urn:ubl-examples:world:codelist:PrizeRankCode`)  
  The second prize. The code is from the Trade Accord's prize rank list: SECOND = Second prize.
- `AwardingTerms/Prize/ValueAmount` = **4000.00** (currencyID `XBL`)  
  The second prize, unchanged since it was planned.
- `AwardingTerms/Prize/Description` = **For the design the jury ranks second.**  
  What it is for.
- `AwardingTerms/Prize/RankCode` = **THIRD** (listID `urn:ubl-examples:world:codelist:PrizeRankCode`)  
  The third prize. The code is from the Trade Accord's prize rank list: THIRD = Third prize.
- `AwardingTerms/Prize/ValueAmount` = **2000.00** (currencyID `XBL`)  
  The third prize.
- `AwardingTerms/Prize/Description` = **For the design the jury ranks third, if the jury finds it of prize standard.**  
  The jury may withhold it.
- `AppealTerms/Description` = **An appeal against the selection or the jury's ranking goes to the review board within ten days.**  
  How to appeal.
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
- `Language/ID` = **en** (schemeID `ISO 639`)  
  Designs and requests in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.

### Tendering Process

Inside `TenderingProcess`:

- `Description` = **A restricted design contest in two stages: requests to participate, then designs from three to five selected participants, judged anonymously.**  
  How the contest runs.
- `ProcedureCode` = **DESIGNCONTEST** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  A design contest. The code is from the Trade Accord's procurement procedure list: DESIGNCONTEST = Design contest.
- `SubmissionMethodCode` = **ELECTRONIC** (listID `urn:ubl-examples:world:codelist:SubmissionMethodCode`)  
  Requests and designs through the department's platform. The code is from the Trade Accord's submission method list: ELECTRONIC = Electronic.
- `CandidateReductionConstraintIndicator` = **true**  
  The number of participants is limited.
- `TenderSubmissionDeadlinePeriod/EndDate` = **2026-06-12**  
  Designs by then.
- `TenderSubmissionDeadlinePeriod/EndTime` = **12:00:00**  
  At noon.
- `ParticipationRequestReceptionPeriod/EndDate` = **2026-04-18**  
  Requests to participate by then.
- `NoticeDocumentReference/ID` = **LPWD-DOC-26-0633**  
  The prior information notice of the contest.
- `ProcessJustification/PreviousCancellationReasonCode` = **UNSUITABLE** (listID `urn:ubl-examples:world:codelist:CancellationReasonCode`)  
  Why the earlier contest for the same design was cancelled. The code is from the Trade Accord's cancellation reason list: UNSUITABLE = No suitable tender.
- `ProcessJustification/Description` = **Relaunch of the design contest PWD-2025-PROM-DC, cancelled on 20 November 2025: both designs received were unacceptable, one far above any production budget and one not accessible to wheelchair users. The brief now states both limits.**  
  The previous procedure and what changed.
- `EconomicOperatorShortList/LimitationDescription` = **The jury selects the participants on their references.**  
  How.
- `EconomicOperatorShortList/ExpectedQuantity` = **5**  
  Five participants are expected.
- `EconomicOperatorShortList/MaximumQuantity` = **5**  
  At most five, so that the jury can judge every design in depth.
- `EconomicOperatorShortList/MinimumQuantity` = **3**  
  At least three, for a real competition.

### Procurement Project

Inside `ProcurementProject`:

- `Name` = **Design of the harbour promenade bench**  
  The name of the contest.
- `Description` = **A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.**  
  What the department wants designed.
- `ProcurementTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  A design is a service. The code is from the Trade Accord's contract nature list: SERVICES = Services.
- `RequestedTenderTotal/EstimatedOverallContractAmount` = **54000.00** (currencyID `XBL`)  
  The prizes, 14,000 lume, and the follow-up service contract, estimated at 40,000 lume.
- `MainCommodityClassification/ItemClassificationCode` = **83912** (listID `UN CPC Ver.2.1`)  
  The contest is for an industrial design, as a subclass of the UN Central Product Classification. The code is from the world's copy of UN Central Product Classification, Version 2.1: 83912 = Industrial design services.
- `RealizedLocation/Name` = **Harbour promenade, Lumeport**  
  Where the furniture will stand.
- `RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `RealizedLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ContractNotice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ContractNotice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:contract-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>CONTEST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0634</cbc:ID>
  <cbc:UUID>88a68511-926f-5847-b468-9a248742facd</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PROM-DC</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-19</cbc:IssueDate>
  <cbc:IssueTime>08:51:00</cbc:IssueTime>
  <cbc:Note>Restricted design contest for the harbour promenade bench, with three prizes.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:NoticeTypeCode listID="urn:ubl-examples:world:codelist:NoticeTypeCode">CN</cbc:NoticeTypeCode>
  <cac:ContractingParty>
    <cbc:BuyerProfileURI>https://tenders.lumeport.example/buyers/pwd</cbc:BuyerProfileURI>
    <cac:ContractingPartyType>
      <cbc:PartyTypeCode listID="urn:ubl-examples:world:codelist:ContractingPartyTypeCode">LOCAL</cbc:PartyTypeCode>
      <cbc:PartyType>Local authority: a department of the city of Lumeport</cbc:PartyType>
    </cac:ContractingPartyType>
    <cac:ContractingActivity>
      <cbc:ActivityTypeCode listID="urn:ubl-examples:world:codelist:AuthorityActivityCode">COMMUNITY</cbc:ActivityTypeCode>
      <cbc:ActivityType>Housing and community amenities: public works and parks</cbc:ActivityType>
    </cac:ContractingActivity>
    <cac:ContractingRepresentationType>
      <cbc:RepresentationTypeCode listID="urn:ubl-examples:world:codelist:RepresentationTypeCode">OWN</cbc:RepresentationTypeCode>
      <cbc:RepresentationType>On its own behalf</cbc:RepresentationType>
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
    <cac:TendererQualificationRequest>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private): a group of participants forms one before the follow-up contract is awarded; for the contest itself a group names a lead member</cbc:CompanyLegalForm>
      <cbc:Description>The design lead is a registered architect.</cbc:Description>
      <cac:TechnicalEvaluationCriterion>
        <cbc:EvaluationCriterionTypeCode listID="urn:ubl-examples:world:codelist:EvaluationCriterionTypeCode">REFERENCES</cbc:EvaluationCriterionTypeCode>
        <cbc:Description>Two completed designs of furniture or fittings for public spaces in the last five years.</cbc:Description>
        <cbc:ThresholdQuantity unitCode="EA">2</cbc:ThresholdQuantity>
        <cac:DurationPeriod>
          <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
        </cac:DurationPeriod>
      </cac:TechnicalEvaluationCriterion>
      <cac:EconomicOperatorRole>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EconomicOperatorRoleCode">LEAD</cbc:RoleCode>
        <cbc:RoleDescription>Represents the group towards the department.</cbc:RoleDescription>
      </cac:EconomicOperatorRole>
    </cac:TendererQualificationRequest>
    <cac:AwardingTerms>
      <cbc:Description>The jury ranks the designs anonymously, on design quality (40 %), durability and maintenance in salt air (30 %) and the cost of production (30 %).</cbc:Description>
      <cbc:TechnicalCommitteeDescription>A jury of five: the head of parks, the city architect, a representative of the disability council and two independent designers.</cbc:TechnicalCommitteeDescription>
      <cbc:PrizeIndicator>true</cbc:PrizeIndicator>
      <cbc:PrizeDescription>Three prizes; the first is 8,000 lume.</cbc:PrizeDescription>
      <cbc:PaymentDescription>Each selected participant that submits a design meeting the brief receives 1,000 lume towards its costs, whether or not it wins a prize.</cbc:PaymentDescription>
      <cbc:FollowupContractIndicator>true</cbc:FollowupContractIndicator>
      <cbc:BindingOnBuyerIndicator>true</cbc:BindingOnBuyerIndicator>
      <cac:Prize>
        <cbc:RankCode listID="urn:ubl-examples:world:codelist:PrizeRankCode">FIRST</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">8000.00</cbc:ValueAmount>
        <cbc:Description>For the design the jury ranks first; its author is invited to negotiate the follow-up service contract.</cbc:Description>
      </cac:Prize>
      <cac:Prize>
        <cbc:RankCode listID="urn:ubl-examples:world:codelist:PrizeRankCode">SECOND</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">4000.00</cbc:ValueAmount>
        <cbc:Description>For the design the jury ranks second.</cbc:Description>
      </cac:Prize>
      <cac:Prize>
        <cbc:RankCode listID="urn:ubl-examples:world:codelist:PrizeRankCode">THIRD</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">2000.00</cbc:ValueAmount>
        <cbc:Description>For the design the jury ranks third, if the jury finds it of prize standard.</cbc:Description>
      </cac:Prize>
    </cac:AwardingTerms>
    <cac:AppealTerms>
      <cbc:Description>An appeal against the selection or the jury's ranking goes to the review board within ten days.</cbc:Description>
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
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
    </cac:Language>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:Description>A restricted design contest in two stages: requests to participate, then designs from three to five selected participants, judged anonymously.</cbc:Description>
    <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">DESIGNCONTEST</cbc:ProcedureCode>
    <cbc:SubmissionMethodCode listID="urn:ubl-examples:world:codelist:SubmissionMethodCode">ELECTRONIC</cbc:SubmissionMethodCode>
    <cbc:CandidateReductionConstraintIndicator>true</cbc:CandidateReductionConstraintIndicator>
    <cac:TenderSubmissionDeadlinePeriod>
      <cbc:EndDate>2026-06-12</cbc:EndDate>
      <cbc:EndTime>12:00:00</cbc:EndTime>
    </cac:TenderSubmissionDeadlinePeriod>
    <cac:ParticipationRequestReceptionPeriod>
      <cbc:EndDate>2026-04-18</cbc:EndDate>
    </cac:ParticipationRequestReceptionPeriod>
    <cac:NoticeDocumentReference>
      <cbc:ID>LPWD-DOC-26-0633</cbc:ID>
    </cac:NoticeDocumentReference>
    <cac:ProcessJustification>
      <cbc:PreviousCancellationReasonCode listID="urn:ubl-examples:world:codelist:CancellationReasonCode">UNSUITABLE</cbc:PreviousCancellationReasonCode>
      <cbc:Description>Relaunch of the design contest PWD-2025-PROM-DC, cancelled on 20 November 2025: both designs received were unacceptable, one far above any production budget and one not accessible to wheelchair users. The brief now states both limits.</cbc:Description>
    </cac:ProcessJustification>
    <cac:EconomicOperatorShortList>
      <cbc:LimitationDescription>The jury selects the participants on their references.</cbc:LimitationDescription>
      <cbc:ExpectedQuantity>5</cbc:ExpectedQuantity>
      <cbc:MaximumQuantity>5</cbc:MaximumQuantity>
      <cbc:MinimumQuantity>3</cbc:MinimumQuantity>
    </cac:EconomicOperatorShortList>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:Name>Design of the harbour promenade bench</cbc:Name>
    <cbc:Description>A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.</cbc:Description>
    <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SERVICES</cbc:ProcurementTypeCode>
    <cac:RequestedTenderTotal>
      <cbc:EstimatedOverallContractAmount currencyID="XBL">54000.00</cbc:EstimatedOverallContractAmount>
    </cac:RequestedTenderTotal>
    <cac:MainCommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">83912</cbc:ItemClassificationCode>
    </cac:MainCommodityClassification>
    <cac:RealizedLocation>
      <cbc:Name>Harbour promenade, Lumeport</cbc:Name>
      <cac:Address>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:RealizedLocation>
  </cac:ProcurementProject>
</ContractNotice>
```
