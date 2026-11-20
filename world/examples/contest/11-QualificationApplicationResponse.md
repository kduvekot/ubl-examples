# Qualification Application Response: Brackenmere Furniture to Lumeport Public Works Department

*Example 11 of the flow "A design contest for the promenade bench (Bayvarra)" · [Qualification Application Response in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-QUALIFICATION-APPLICATION-RESPONSE-SCHEMA)*

Version 2 of the team's self-declaration: the furniture maker's own industrial designer now leads the design.

[The XML file](11-QualificationApplicationResponse.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:qualification-application:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Qualification application"; the community specification "Public procurement community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **CONTEST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BF-DOC-26-0637**  
  The team's number for its self-declaration.
- `UUID` = **96bef55f-d029-56b6-bd03-038fe825ccdf**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PROM-DC**  
  The department's file number for the contest, the same on every document of it.
- `ContractName` = **Design of the harbour promenade bench**  
  The contest.
- `IssueDate` = **2026-04-14**  
  Before the extended deadline for requests.
- `IssueTime` = **14:18:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC.
- `EconomicOperatorGroupName` = **Brackenmere and Saltmere design team**  
  The group that enters.
- `VersionID` = **2**  
  The second version, which supersedes the first: the team answers version 2 of the request: the furniture maker's industrial designer now leads the design, and the engineering firm's architect stays in the team for the structure.
- `PreviousVersionID` = **1**  
  The version this one supersedes: version 1 of the same document, with the same number.
- `ProcedureCode` = **DESIGNCONTEST** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  The contest. The code is from the Trade Accord's procurement procedure list: DESIGNCONTEST = Design contest.
- `Note` = **Version 2: Brackenmere's own industrial designer, Ivo Harlan, now leads the design in place of Saltmere's architect, Edda Corwin.**  
  What version 2 changes, said in the document.

### Contracting Party

Inside `ContractingParty`:

- `Party/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; as Lumeport Public Works Department gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Public Works Department gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Lumeport Public Works Department gives it.
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). as Lumeport Public Works Department gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Lumeport Public Works Department gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The public body's official name; as Lumeport Public Works Department gives it.
- `Party/PartyLegalEntity/CompanyID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register ; as Lumeport Public Works Department gives it. The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Party/Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; as Lumeport Public Works Department gives it.
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; as Lumeport Public Works Department gives it.
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; as Lumeport Public Works Department gives it.
- `Party/Contact/Telephone` = **+999 2 38 8235 3927**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Lumeport Public Works Department gives it.
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeport Public Works Department gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Public Works Department gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Economic Operator Party

Inside `EconomicOperatorParty`:

- `EconomicOperatorRole/RoleCode` = **LEAD** (listID `urn:ubl-examples:world:codelist:EconomicOperatorRoleCode`)  
  Brackenmere answers as the lead member of the group. The code is from the Trade Accord's economic operator role list: LEAD = Consortium lead.
- `EconomicOperatorRole/RoleDescription` = **Represents the group towards the department.**  
  The role in words.
- `Party/WebsiteURI` = **https://www.brackenmere.example**  
  The party's website, under the reserved .example domain (RFC 2606); as Brackenmere Furniture gives it.
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; as Brackenmere Furniture gives it. The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Brackenmere Furniture gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. as Brackenmere Furniture gives it.
- `Party/PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. as Brackenmere Furniture gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Brackenmere Furniture gives it.
- `Party/PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). as Brackenmere Furniture gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Brackenmere Furniture gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered for state sales tax; as Brackenmere Furniture gives it.
- `Party/PartyTaxScheme/CompanyID` = **UL-1237398** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); as Brackenmere Furniture gives it. The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered, with its legal form; as Brackenmere Furniture gives it.
- `Party/PartyLegalEntity/CompanyID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **2000-01-12**  
  The day the company was entered in the register; as Brackenmere Furniture gives it.
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)** (languageID `en-XB`)  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 45 persons and its turnover of 6830000.00 XBL in 2025, by the Trade Accord's limits; as Brackenmere Furniture gives it. The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Bids office**  
  The party's bids office desk: the desk for its role in this document (it bids); as Brackenmere Furniture gives it.
- `Party/Contact/JobTitle` = **Bid manager**  
  The job of the person who answers at the desk; as Brackenmere Furniture gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Brackenmere Furniture gives it.
- `Party/Contact/Telephone` = **+999 2 7121 602 606**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Brackenmere Furniture gives it.
- `Party/Contact/ElectronicMail` = **tenders@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brackenmere Furniture gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Brackenmere Furniture gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `EconomicOperatorRole/RoleCode` = **MEMBER** (listID `urn:ubl-examples:world:codelist:EconomicOperatorRoleCode`)  
  Saltmere Engineering is the group's other member, for the structure and the anchoring. The code is from the Trade Accord's economic operator role list: MEMBER = Consortium member.
- `EconomicOperatorRole/RoleDescription` = **Designs the structure and the anchoring.**  
  The role in words.
- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Saltmere Engineering gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; as Saltmere Engineering gives it.

### Tendering Criterion

Inside `TenderingCriterion`:

- `ID` = **CR-CONVICTIONS**  
  A criterion of the request, answered below: the response answers every criterion it asks.
- `ID` = **CR-TAXES**  
  A criterion of the request, answered below: the response answers every criterion it asks.
- `ID` = **CR-PROF**  
  A criterion of the request, answered below: the response answers every criterion it asks.
- `ID` = **CR-REF-PUBLIC**  
  A criterion of the request, answered below: the response answers every criterion it asks.
- `ID` = **CR-REF-COAST**  
  A criterion of the request, answered below: the response answers every criterion it asks.

### Tendering Criterion Response

Inside `TenderingCriterionResponse`:

- `ID` = **CRR-CONVICTIONS**  
  The response on convictions.
- `ValidatedCriterionPropertyID` = **P-CONVICTIONS-1**  
  The question answered.
- `ResponseValue/ID` = **RV-CONVICTIONS-1**  
  The answer for Brackenmere Furniture: each member of the group answers the exclusion grounds.
- `ResponseValue/Description` = **Brackenmere Furniture: no conviction of the member or of its management.**  
  The answer, for this member.
- `ResponseValue/ResponseIndicator` = **false**  
  No: not convicted.
- `ResponseValue/ID` = **RV-CONVICTIONS-2**  
  The answer for Saltmere Engineering: each member of the group answers the exclusion grounds.
- `ResponseValue/Description` = **Saltmere Engineering: no conviction of the member or of its management.**  
  The answer, for this member.
- `ResponseValue/ResponseIndicator` = **false**  
  No: not convicted.
- `ID` = **CRR-TAXES**  
  The response on taxes and contributions.
- `ValidatedCriterionPropertyID` = **P-TAXES-1**  
  The question answered.
- `ResponseValue/ID` = **RV-TAXES-1**  
  The answer for Brackenmere Furniture: each member of the group answers the exclusion grounds.
- `ResponseValue/Description` = **Brackenmere Furniture: no taxes or social security contributions due and unpaid.**  
  The answer, for this member.
- `ResponseValue/ResponseIndicator` = **false**  
  No: nothing due is unpaid.
- `ResponseValue/ID` = **RV-TAXES-2**  
  The answer for Saltmere Engineering: each member of the group answers the exclusion grounds.
- `ResponseValue/Description` = **Saltmere Engineering: no taxes or social security contributions due and unpaid.**  
  The answer, for this member.
- `ResponseValue/ResponseIndicator` = **false**  
  No: nothing due is unpaid.
- `ID` = **CRR-PROF**  
  The response on the design lead.
- `ValidatedCriterionPropertyID` = **P-PROF-1**  
  The question answered.
- `ResponseValue/ID` = **RV-PROF**  
  The answer.
- `ResponseValue/Description` = **Ivo Harlan, Brackenmere Furniture's own industrial designer, is registered as an industrial designer, no. ID-2208, in the register of the Bayvarran Design Council.**  
  The answer, in words, as the question asks: the response itself repeats nothing.
- `ResponseValue/ResponseCode` = **MET** (listID `urn:ubl-examples:world:codelist:CriterionResponseCode`)  
  The criterion is met. The code is from the Trade Accord's criterion response list: MET = Criterion met.
- `SuppliedEvidence/ID` = **EV-REG-ID-2208**  
  The certificate that proves the registration.
- `ID` = **CRR-REF-PUBLIC**  
  The response on the references.
- `ValidatedCriterionPropertyID` = **P-REF-PUBLIC-1**  
  The question answered: one value for each of the two references.
- `ResponseValue/ID` = **RV-REF-PUBLIC-1**  
  The answer.
- `ResponseValue/Description` = **Seating for the reading garden of Lumeport's central library, 2024: client the City of Lumeport; Brackenmere designed the benches and the planter seats, made in Brackenmere's workshop.**  
  The project, the client, the year and what the team designed, as the question asks.
- `ResponseValue/ID` = **RV-REF-PUBLIC-2**  
  The answer.
- `ResponseValue/Description` = **Promenade benches for Larkmouth's seafront, 2023: client Larkmouth town council; Brackenmere designed the benches of the seafront promenade, bolted to the sea wall's walkway.**  
  The project, the client, the year and what the team designed, as the question asks.
- `ID` = **CRR-REF-COAST**  
  The response on the coastal site: which reference it is.
- `ValidatedCriterionPropertyID` = **P-REF-COAST-1**  
  The question answered.
- `ResponseValue/ID` = **RV-REF-COAST-1**  
  The answer.
- `ResponseValue/Description` = **Promenade benches for Larkmouth's seafront, 2023: client Larkmouth town council; Brackenmere designed the benches of the seafront promenade, bolted to the sea wall's walkway.**  
  The project, the client, the year and what the team designed, as the question asks.
- `ID` = **CRR-REF-COAST-SITE**  
  The response on the site of the coastal reference.
- `ValidatedCriterionPropertyID` = **P-REF-COAST-2**  
  The question answered.
- `ResponseValue/ID` = **RV-REF-COAST-2**  
  The answer.
- `ResponseValue/Description` = **On the seafront promenade of Larkmouth, Bayvarra's harbour town at the mouth of the east river: the benches stand on the sea wall's walkway, within 20 metres of the sea.**  
  Where it stands and how far from the sea.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **LPWD-DOC-26-0636**  
  The request this self-declaration answers.
- `DocumentTypeCode` = **QualificationApplicationRequest** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LPWD-DOC-26-0636 is the example contest/05, a QualificationApplicationRequest; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: QualificationApplicationRequest = Qualification Application Request.
- `VersionID` = **2**  
  The version of the request answered.

### Evidence

Inside `Evidence`:

- `ID` = **EV-REG-ID-2208**  
  The certificate of the design lead's registration.
- `EvidenceTypeCode` = **CERTIFICATE** (listID `urn:ubl-examples:world:codelist:EvidenceTypeCode`)  
  A certificate of registration. The code is from the Trade Accord's evidence type list: CERTIFICATE = Certificate.
- `Name` = **Certificate of registration of the design lead, Ivo Harlan**  
  What it is.
- `Description` = **Registration no. ID-2208 in the register of industrial designers that the Bayvarran Design Council keeps; the council issues the certificate.**  
  Which register, and who issues the certificate.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<QualificationApplicationResponse xmlns="urn:oasis:names:specification:ubl:schema:xsd:QualificationApplicationResponse-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:qualification-application:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>CONTEST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BF-DOC-26-0637</cbc:ID>
  <cbc:UUID>96bef55f-d029-56b6-bd03-038fe825ccdf</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PROM-DC</cbc:ContractFolderID>
  <cbc:ContractName>Design of the harbour promenade bench</cbc:ContractName>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>14:18:00-01:00</cbc:IssueTime>
  <cbc:EconomicOperatorGroupName>Brackenmere and Saltmere design team</cbc:EconomicOperatorGroupName>
  <cbc:VersionID>2</cbc:VersionID>
  <cbc:PreviousVersionID>1</cbc:PreviousVersionID>
  <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">DESIGNCONTEST</cbc:ProcedureCode>
  <cbc:Note>Version 2: Brackenmere's own industrial designer, Ivo Harlan, now leads the design in place of Saltmere's architect, Edda Corwin.</cbc:Note>
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
    <cac:EconomicOperatorRole>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EconomicOperatorRoleCode">LEAD</cbc:RoleCode>
      <cbc:RoleDescription>Represents the group towards the department.</cbc:RoleDescription>
    </cac:EconomicOperatorRole>
    <cac:Party>
      <cbc:WebsiteURI>https://www.brackenmere.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-821551</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Joiners Row</cbc:StreetName>
        <cbc:BuildingNumber>14</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71203</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1237398</cbc:CompanyID>
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
        <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:CompanyID>
        <cbc:RegistrationDate>2000-01-12</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="en-XB">Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
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
        <cbc:JobTitle>Bid manager</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 602 606</cbc:Telephone>
        <cbc:ElectronicMail>tenders@brackenmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:EconomicOperatorParty>
  <cac:EconomicOperatorParty>
    <cac:EconomicOperatorRole>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EconomicOperatorRoleCode">MEMBER</cbc:RoleCode>
      <cbc:RoleDescription>Designs the structure and the anchoring.</cbc:RoleDescription>
    </cac:EconomicOperatorRole>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saltmere Engineering</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:EconomicOperatorParty>
  <cac:TenderingCriterion>
    <cbc:ID>CR-CONVICTIONS</cbc:ID>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-TAXES</cbc:ID>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-PROF</cbc:ID>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-REF-PUBLIC</cbc:ID>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-REF-COAST</cbc:ID>
  </cac:TenderingCriterion>
  <cac:TenderingCriterionResponse>
    <cbc:ID>CRR-CONVICTIONS</cbc:ID>
    <cbc:ValidatedCriterionPropertyID>P-CONVICTIONS-1</cbc:ValidatedCriterionPropertyID>
    <cac:ResponseValue>
      <cbc:ID>RV-CONVICTIONS-1</cbc:ID>
      <cbc:Description>Brackenmere Furniture: no conviction of the member or of its management.</cbc:Description>
      <cbc:ResponseIndicator>false</cbc:ResponseIndicator>
    </cac:ResponseValue>
    <cac:ResponseValue>
      <cbc:ID>RV-CONVICTIONS-2</cbc:ID>
      <cbc:Description>Saltmere Engineering: no conviction of the member or of its management.</cbc:Description>
      <cbc:ResponseIndicator>false</cbc:ResponseIndicator>
    </cac:ResponseValue>
  </cac:TenderingCriterionResponse>
  <cac:TenderingCriterionResponse>
    <cbc:ID>CRR-TAXES</cbc:ID>
    <cbc:ValidatedCriterionPropertyID>P-TAXES-1</cbc:ValidatedCriterionPropertyID>
    <cac:ResponseValue>
      <cbc:ID>RV-TAXES-1</cbc:ID>
      <cbc:Description>Brackenmere Furniture: no taxes or social security contributions due and unpaid.</cbc:Description>
      <cbc:ResponseIndicator>false</cbc:ResponseIndicator>
    </cac:ResponseValue>
    <cac:ResponseValue>
      <cbc:ID>RV-TAXES-2</cbc:ID>
      <cbc:Description>Saltmere Engineering: no taxes or social security contributions due and unpaid.</cbc:Description>
      <cbc:ResponseIndicator>false</cbc:ResponseIndicator>
    </cac:ResponseValue>
  </cac:TenderingCriterionResponse>
  <cac:TenderingCriterionResponse>
    <cbc:ID>CRR-PROF</cbc:ID>
    <cbc:ValidatedCriterionPropertyID>P-PROF-1</cbc:ValidatedCriterionPropertyID>
    <cac:ResponseValue>
      <cbc:ID>RV-PROF</cbc:ID>
      <cbc:Description>Ivo Harlan, Brackenmere Furniture's own industrial designer, is registered as an industrial designer, no. ID-2208, in the register of the Bayvarran Design Council.</cbc:Description>
      <cbc:ResponseCode listID="urn:ubl-examples:world:codelist:CriterionResponseCode">MET</cbc:ResponseCode>
    </cac:ResponseValue>
    <cac:SuppliedEvidence>
      <cbc:ID>EV-REG-ID-2208</cbc:ID>
    </cac:SuppliedEvidence>
  </cac:TenderingCriterionResponse>
  <cac:TenderingCriterionResponse>
    <cbc:ID>CRR-REF-PUBLIC</cbc:ID>
    <cbc:ValidatedCriterionPropertyID>P-REF-PUBLIC-1</cbc:ValidatedCriterionPropertyID>
    <cac:ResponseValue>
      <cbc:ID>RV-REF-PUBLIC-1</cbc:ID>
      <cbc:Description>Seating for the reading garden of Lumeport's central library, 2024: client the City of Lumeport; Brackenmere designed the benches and the planter seats, made in Brackenmere's workshop.</cbc:Description>
    </cac:ResponseValue>
    <cac:ResponseValue>
      <cbc:ID>RV-REF-PUBLIC-2</cbc:ID>
      <cbc:Description>Promenade benches for Larkmouth's seafront, 2023: client Larkmouth town council; Brackenmere designed the benches of the seafront promenade, bolted to the sea wall's walkway.</cbc:Description>
    </cac:ResponseValue>
  </cac:TenderingCriterionResponse>
  <cac:TenderingCriterionResponse>
    <cbc:ID>CRR-REF-COAST</cbc:ID>
    <cbc:ValidatedCriterionPropertyID>P-REF-COAST-1</cbc:ValidatedCriterionPropertyID>
    <cac:ResponseValue>
      <cbc:ID>RV-REF-COAST-1</cbc:ID>
      <cbc:Description>Promenade benches for Larkmouth's seafront, 2023: client Larkmouth town council; Brackenmere designed the benches of the seafront promenade, bolted to the sea wall's walkway.</cbc:Description>
    </cac:ResponseValue>
  </cac:TenderingCriterionResponse>
  <cac:TenderingCriterionResponse>
    <cbc:ID>CRR-REF-COAST-SITE</cbc:ID>
    <cbc:ValidatedCriterionPropertyID>P-REF-COAST-2</cbc:ValidatedCriterionPropertyID>
    <cac:ResponseValue>
      <cbc:ID>RV-REF-COAST-2</cbc:ID>
      <cbc:Description>On the seafront promenade of Larkmouth, Bayvarra's harbour town at the mouth of the east river: the benches stand on the sea wall's walkway, within 20 metres of the sea.</cbc:Description>
    </cac:ResponseValue>
  </cac:TenderingCriterionResponse>
  <cac:AdditionalDocumentReference>
    <cbc:ID>LPWD-DOC-26-0636</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">QualificationApplicationRequest</cbc:DocumentTypeCode>
    <cbc:VersionID>2</cbc:VersionID>
  </cac:AdditionalDocumentReference>
  <cac:Evidence>
    <cbc:ID>EV-REG-ID-2208</cbc:ID>
    <cbc:EvidenceTypeCode listID="urn:ubl-examples:world:codelist:EvidenceTypeCode">CERTIFICATE</cbc:EvidenceTypeCode>
    <cbc:Name>Certificate of registration of the design lead, Ivo Harlan</cbc:Name>
    <cbc:Description>Registration no. ID-2208 in the register of industrial designers that the Bayvarran Design Council keeps; the council issues the certificate.</cbc:Description>
  </cac:Evidence>
</QualificationApplicationResponse>
```
