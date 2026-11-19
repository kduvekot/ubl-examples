# Qualification Application Request: Lumeport Public Works Department to Brackenmere Furniture

*Example 6 of the flow "A public tender (Bayvarra)" · [Qualification Application Request in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-QUALIFICATION-APPLICATION-REQUEST-SCHEMA)*

The authority sends the furniture maker the self-declaration it must fill in: exclusion grounds and selection criteria.

[The XML file](06-QualificationApplicationRequest.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:qualification-application:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Qualification application"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
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
- `IssueTime` = **08:25:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `VersionID` = **1**  
  The first version.
- `ProcedureCode` = **OPEN** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  An open procedure. The code is from the Trade Accord's procurement procedure list: OPEN = Open procedure.
- `QualificationApplicationTypeCode` = **REGULATED** (listID `urn:ubl-examples:world:codelist:QualificationApplicationTypeCode`)  
  The regulated form of self-declaration. The code is from the Trade Accord's qualification application type list: REGULATED = Regulated.
- `WeightScoringMethodologyNote` = **Pass or fail; no weighting.**  
  How answers count.
- `WeightingTypeCode` = **NONE** (listID `urn:ubl-examples:world:codelist:WeightingTypeCode`)  
  No weighting. The code is from the Trade Accord's weighting type list: NONE = No weighting.
- `Note` = **Answer every criterion.**  
  What to do.

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

- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Bids office**  
  The party's bids office desk: the desk for its role in this document (it bids); identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/JobTitle` = **Bid manager**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 602 606**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/ElectronicMail` = **tenders@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `ID` = **CR-CONVICTIONS**  
  The exclusion ground.
- `CriterionTypeCode` = **EXCLUSION** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  An exclusion ground: a participant to which it applies is not selected. The code is from the Trade Accord's criterion type list: EXCLUSION = Exclusion ground.
- `Name` = **Convictions**  
  The ground.
- `Description` = **A participant is excluded if it, or a member of its management, has been convicted by final judgment in the last five years of participation in a criminal organisation, corruption, fraud or money laundering.**  
  What excludes a participant.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  It applies or not. The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `Legislation/ID` = **XB-PPA-2019**  
  Bayvarra's Public Procurement Act.
- `Legislation/Title` = **Public Procurement Act**  
  Its title.
- `Legislation/Article` = **Art. 57**  
  The article on the exclusion grounds.
- `TenderingCriterionPropertyGroup/ID` = **PG-CONVICTIONS**  
  The question on the ground.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered. The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-CONVICTIONS-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Convictions**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Whether the participant, or a member of its management, has been so convicted; in a group, each member answers.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the participant answers. The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **INDICATOR** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: INDICATOR = Indicator.
- `ID` = **CR-TAXES**  
  The criterion.
- `CriterionTypeCode` = **EXCLUSION** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: EXCLUSION = Exclusion ground.
- `Name` = **Payment of taxes and social security contributions**  
  The criterion.
- `Description` = **A tenderer that has not paid its taxes or social security contributions is excluded, unless only minor amounts are unpaid.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `Legislation/ID` = **XB-PPA-2019**  
  Bayvarra's Public Procurement Act.
- `Legislation/Title` = **Public Procurement Act**  
  Its title.
- `Legislation/Description` = **Exclusion grounds; the exception for minor amounts.**  
  What.
- `Legislation/Article` = **Art. 57**  
  The article.
- `TenderingCriterionPropertyGroup/ID` = **PG-TAXES**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on payment of taxes and social security contributions.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-TAXES-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Unpaid taxes and contributions**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **The amount of taxes and social security contributions due and unpaid.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **AMOUNT** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: AMOUNT = Amount.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  In lume. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MaximumAmount` = **1000.00** (currencyID `XBL`)  
  Arrears up to 1,000 lume count as minor amounts and do not exclude the tenderer.
- `ID` = **CR-REGISTER**  
  The criterion.
- `CriterionTypeCode` = **SUITABILITY** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: SUITABILITY = Suitability.
- `Name` = **Enrolment in a business register**  
  The criterion.
- `Description` = **The tenderer is entered in the business register of the country where it is established.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `Legislation/ID` = **XB-PPA-2019**  
  Bayvarra's Public Procurement Act.
- `Legislation/Title` = **Public Procurement Act**  
  Its title.
- `Legislation/Description` = **Selection criteria: suitability to pursue the activity.**  
  What.
- `Legislation/Article` = **Art. 58**  
  The article.
- `TenderingCriterionPropertyGroup/ID` = **PG-REGISTER**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on enrolment in a business register.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-REGISTER-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Registered in a business register**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Whether the tenderer is entered in a business register.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **INDICATOR** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: INDICATOR = Indicator.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedIndicator` = **true**  
  Only one answer meets the criterion: yes.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedDescription` = **Entered in the national business register of the tenderer's country.**  
  What a yes means; the register's address goes to the evidence, not to an expected identifier (tender/06#F7).
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TranslationTypeCode` = **NONE** (listID `urn:ubl-examples:world:codelist:TranslationTypeCode`)  
  An extract in another language is accepted as it is. The code is from the Trade Accord's translation type list: NONE = No translation.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/CertificationLevelDescription` = **A plain extract will do.**  
  The level.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/CopyQualityTypeCode` = **COPY** (listID `urn:ubl-examples:world:codelist:CopyQualityCode`)  
  A copy is enough. The code is from the Trade Accord's copy quality list: COPY = A copy is enough.
- `ID` = **CR-YEARS**  
  The criterion.
- `CriterionTypeCode` = **ECONOMIC** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: ECONOMIC = Economic and financial standing.
- `Name` = **Years in business**  
  The criterion.
- `Description` = **At least three full years in business, as the notices ask.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `TenderingCriterionPropertyGroup/ID` = **PG-YEARS**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on years in business.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-YEARS-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Years in business**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **The full years since the tenderer was founded.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **QUANTITY** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: QUANTITY = Quantity.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueUnitCode` = **ANN** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  Years. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: ANN = year.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumQuantity` = **3** (unitCode `ANN`)  
  At least three years, stated once, as a quantity (tender/06#F16).
- `ID` = **CR-TURNOVER**  
  The criterion.
- `CriterionTypeCode` = **ECONOMIC** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: ECONOMIC = Economic and financial standing.
- `Name` = **Yearly turnover**  
  The criterion.
- `Description` = **A yearly turnover of at least 124,800 lume, twice the yearly estimate of 62,400 lume, in the last financial year for which accounts are filed.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `ProcurementProjectLotReference/ID` = **LOT-1**  
  Lot 1 of the procedure.
- `CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  The benches, as a subclass of the UN Central Product Classification: seats with metal frames. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Legislation/ID` = **XB-PPA-2019**  
  Bayvarra's Public Procurement Act.
- `Legislation/Title` = **Public Procurement Act**  
  Its title.
- `Legislation/Description` = **Selection criteria: economic and financial standing.**  
  What.
- `Legislation/JurisdictionLevel` = **National**  
  The level.
- `Legislation/Article` = **Art. 58**  
  The article.
- `Legislation/URI` = **https://law.bayvarra.example/ppa**  
  Where.
- `Legislation/Language/ID` = **en** (schemeID `ISO 639`)  
  English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Legislation/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `TenderingCriterionPropertyGroup/ID` = **PG-TURNOVER**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on yearly turnover.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-TURNOVER-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Yearly turnover**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **The turnover of the last financial year for which accounts are filed.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **AMOUNT** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: AMOUNT = Amount.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  In lume. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumAmount` = **124800.00** (currencyID `XBL`)  
  At least, as in the notices: greater than or equal (D28 point 2, tender/06#F13).
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ApplicablePeriod/StartDate` = **2024-01-01**  
  The last financial year whose accounts are filed by the tender deadline
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ApplicablePeriod/EndDate` = **2024-12-31**  
  (accounts for 2025 are filed from April).
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TemplateEvidence/ID` = **EV-ACC**  
  The evidence asked.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TemplateEvidence/Name` = **Annual accounts**  
  Evidence.
- `ID` = **CR-STAFF**  
  The criterion.
- `CriterionTypeCode` = **TECHNICAL** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: TECHNICAL = Technical and professional ability.
- `Name` = **Staff**  
  The criterion.
- `Description` = **At least ten employees, as the notices ask.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `TenderingCriterionPropertyGroup/ID` = **PG-STAFF**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on staff.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-STAFF-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Employees**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **The number of persons employed.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **QUANTITY** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: QUANTITY = Quantity.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueUnitCode` = **IE** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  Persons. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: IE = person.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumQuantity` = **10** (unitCode `IE`)  
  At least ten.
- `ID` = **CR-REFERENCES**  
  The criterion.
- `CriterionTypeCode` = **TECHNICAL** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: TECHNICAL = Technical and professional ability.
- `Name` = **Similar supplies**  
  The criterion.
- `Description` = **Three supplies of park benches or similar street furniture in the last five years, as the notices ask.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `TenderingCriterionPropertyGroup/ID` = **PG-REFERENCES**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on similar supplies.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/FulfilmentIndicatorTypeCode` = **ALL** (listID `urn:ubl-examples:world:codelist:FulfilmentIndicatorCode`)  
  Both questions must be answered and met. The code is from the Trade Accord's fulfilment indicator list: ALL = All properties.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-REFERENCES-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **The supplies**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Each supply: the customer, the year, what was supplied and its value.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **DESCRIPTION** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: DESCRIPTION = Description.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-REFERENCES-2**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Number of supplies**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **How many such supplies.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **QUANTITY** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: QUANTITY = Quantity.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueUnitCode` = **EA** (listID `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade`)  
  Supplies. The code is from UBL's default Unit of measure (UNECE Recommendation 20) list: EA = each.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/MinimumQuantity` = **3** (unitCode `EA`)  
  At least three.
- `ID` = **CR-TIMBER**  
  The criterion.
- `CriterionTypeCode` = **TECHNICAL** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Its kind. The code is from the Trade Accord's criterion type list: TECHNICAL = Technical and professional ability.
- `Name` = **Certified timber**  
  The criterion.
- `Description` = **The slats come from forests managed for regrowth, with a forestry certificate valid for the contract, as the call asks.**  
  What it asks.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Met or not; the request states no fulfilment, since nobody has answered yet (tender/06#F5). The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `Legislation/ID` = **XB-PPA-2019**  
  Bayvarra's Public Procurement Act.
- `Legislation/Title` = **Public Procurement Act**  
  Its title.
- `Legislation/Description` = **Environmental requirements of the specification (XB-ENV-2021 art. 12).**  
  What.
- `Legislation/Article` = **Art. 70**  
  The article.
- `TenderingCriterionPropertyGroup/ID` = **PG-TIMBER**  
  The questions of the criterion.
- `TenderingCriterionPropertyGroup/Description` = **The questions on certified timber.**  
  What the group asks.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered: no indicator comes before it (tender/06#F14). The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-TIMBER-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Forestry certificate**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Whether the timber of the slats is covered by a forestry certificate valid for the two years of the contract.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **INDICATOR** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: INDICATOR = Indicator.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ExpectedIndicator` = **true**  
  Only one answer meets the criterion: yes.
- `ID` = **CR-GROUP**  
  The criterion on the tenderer's composition.
- `CriterionTypeCode` = **SUITABILITY** (listID `urn:ubl-examples:world:codelist:CriterionTypeCode`)  
  Who tenders. The code is from the Trade Accord's criterion type list: SUITABILITY = Suitability.
- `Name` = **Tendering as a group**  
  The criterion.
- `Description` = **A group of tenderers names its members and the share of each (tender/06#F4).**  
  What.
- `EvaluationMethodTypeCode` = **PASSFAIL** (listID `urn:ubl-examples:world:codelist:EvaluationMethodCode`)  
  Answered or not. The code is from the Trade Accord's evaluation method list: PASSFAIL = Pass or fail.
- `TenderingCriterionPropertyGroup/ID` = **PG-GROUP**  
  The question whether a group tenders.
- `TenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ON** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Always answered. The code is from the Trade Accord's property group type list: ON = Always.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-GROUP-1**  
  The question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **A group**  
  Its name.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **Whether the tenderer tenders as a member of a group.**  
  What to answer.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **INDICATOR** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: INDICATOR = Indicator.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/ID` = **PG-GROUP-1**  
  The questions for a group.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/Name` = **Group**  
  Name.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/PropertyGroupTypeCode` = **ONTRUE** (listID `urn:ubl-examples:world:codelist:PropertyGroupTypeCode`)  
  Answered only when the indicator before it is yes: a group tenders (tender/06#F14). The code is from the Trade Accord's property group type list: ONTRUE = When the indicator is true.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/ID` = **P-GROUP-2**  
  The question.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/Name` = **Share in the group**  
  Its name.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/Description` = **The share of the work of each member, in per cent.**  
  What to answer.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/TypeCode` = **QUESTION** (listID `urn:ubl-examples:world:codelist:CriterionPropertyTypeCode`)  
  A question the tenderer answers (tender/06#F15). The code is from the Trade Accord's criterion property type list: QUESTION = Question.
- `TenderingCriterionPropertyGroup/SubsidiaryTenderingCriterionPropertyGroup/TenderingCriterionProperty/ValueDataTypeCode` = **PERCENT** (listID `urn:ubl-examples:world:codelist:ResponseDataTypeCode`)  
  The kind of answer it takes. The code is from the Trade Accord's response data type list: PERCENT = Percentage.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **LPWD-DOC-26-0189**  
  The call for tenders, sent with this request (tender/06#F1).
- `DocumentTypeCode` = **CallForTenders** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LPWD-DOC-26-0189 is the example tender/03, a CallForTenders; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: CallForTenders = Call For Tenders.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-QAR**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<QualificationApplicationRequest xmlns="urn:oasis:names:specification:ubl:schema:xsd:QualificationApplicationRequest-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:qualification-application:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0192</cbc:ID>
  <cbc:UUID>3c06617e-8a80-509a-b64c-e7ad1ca81e2a</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:IssueDate>2026-02-13</cbc:IssueDate>
  <cbc:IssueTime>08:25:00-01:00</cbc:IssueTime>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">OPEN</cbc:ProcedureCode>
  <cbc:QualificationApplicationTypeCode listID="urn:ubl-examples:world:codelist:QualificationApplicationTypeCode">REGULATED</cbc:QualificationApplicationTypeCode>
  <cbc:WeightScoringMethodologyNote>Pass or fail; no weighting.</cbc:WeightScoringMethodologyNote>
  <cbc:WeightingTypeCode listID="urn:ubl-examples:world:codelist:WeightingTypeCode">NONE</cbc:WeightingTypeCode>
  <cbc:Note>Answer every criterion.</cbc:Note>
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
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
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
  <cac:ProcurementProject>
    <cbc:ID>PWD-2026-PARKS</cbc:ID>
  </cac:ProcurementProject>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-1</cbc:ID>
  </cac:ProcurementProjectLot>
  <cac:TenderingCriterion>
    <cbc:ID>CR-CONVICTIONS</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">EXCLUSION</cbc:CriterionTypeCode>
    <cbc:Name>Convictions</cbc:Name>
    <cbc:Description>A participant is excluded if it, or a member of its management, has been convicted by final judgment in the last five years of participation in a criminal organisation, corruption, fraud or money laundering.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:Legislation>
      <cbc:ID>XB-PPA-2019</cbc:ID>
      <cbc:Title>Public Procurement Act</cbc:Title>
      <cbc:Article>Art. 57</cbc:Article>
    </cac:Legislation>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-CONVICTIONS</cbc:ID>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-CONVICTIONS-1</cbc:ID>
        <cbc:Name>Convictions</cbc:Name>
        <cbc:Description>Whether the participant, or a member of its management, has been so convicted; in a group, each member answers.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">INDICATOR</cbc:ValueDataTypeCode>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-TAXES</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">EXCLUSION</cbc:CriterionTypeCode>
    <cbc:Name>Payment of taxes and social security contributions</cbc:Name>
    <cbc:Description>A tenderer that has not paid its taxes or social security contributions is excluded, unless only minor amounts are unpaid.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:Legislation>
      <cbc:ID>XB-PPA-2019</cbc:ID>
      <cbc:Title>Public Procurement Act</cbc:Title>
      <cbc:Description>Exclusion grounds; the exception for minor amounts.</cbc:Description>
      <cbc:Article>Art. 57</cbc:Article>
    </cac:Legislation>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-TAXES</cbc:ID>
      <cbc:Description>The questions on payment of taxes and social security contributions.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-TAXES-1</cbc:ID>
        <cbc:Name>Unpaid taxes and contributions</cbc:Name>
        <cbc:Description>The amount of taxes and social security contributions due and unpaid.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">AMOUNT</cbc:ValueDataTypeCode>
        <cbc:ValueCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:ValueCurrencyCode>
        <cbc:MaximumAmount currencyID="XBL">1000.00</cbc:MaximumAmount>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-REGISTER</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">SUITABILITY</cbc:CriterionTypeCode>
    <cbc:Name>Enrolment in a business register</cbc:Name>
    <cbc:Description>The tenderer is entered in the business register of the country where it is established.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:Legislation>
      <cbc:ID>XB-PPA-2019</cbc:ID>
      <cbc:Title>Public Procurement Act</cbc:Title>
      <cbc:Description>Selection criteria: suitability to pursue the activity.</cbc:Description>
      <cbc:Article>Art. 58</cbc:Article>
    </cac:Legislation>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-REGISTER</cbc:ID>
      <cbc:Description>The questions on enrolment in a business register.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-REGISTER-1</cbc:ID>
        <cbc:Name>Registered in a business register</cbc:Name>
        <cbc:Description>Whether the tenderer is entered in a business register.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">INDICATOR</cbc:ValueDataTypeCode>
        <cbc:ExpectedIndicator>true</cbc:ExpectedIndicator>
        <cbc:ExpectedDescription>Entered in the national business register of the tenderer's country.</cbc:ExpectedDescription>
        <cbc:TranslationTypeCode listID="urn:ubl-examples:world:codelist:TranslationTypeCode">NONE</cbc:TranslationTypeCode>
        <cbc:CertificationLevelDescription>A plain extract will do.</cbc:CertificationLevelDescription>
        <cbc:CopyQualityTypeCode listID="urn:ubl-examples:world:codelist:CopyQualityCode">COPY</cbc:CopyQualityTypeCode>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-YEARS</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">ECONOMIC</cbc:CriterionTypeCode>
    <cbc:Name>Years in business</cbc:Name>
    <cbc:Description>At least three full years in business, as the notices ask.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-YEARS</cbc:ID>
      <cbc:Description>The questions on years in business.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-YEARS-1</cbc:ID>
        <cbc:Name>Years in business</cbc:Name>
        <cbc:Description>The full years since the tenderer was founded.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">QUANTITY</cbc:ValueDataTypeCode>
        <cbc:ValueUnitCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">ANN</cbc:ValueUnitCode>
        <cbc:MinimumQuantity unitCode="ANN">3</cbc:MinimumQuantity>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-TURNOVER</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">ECONOMIC</cbc:CriterionTypeCode>
    <cbc:Name>Yearly turnover</cbc:Name>
    <cbc:Description>A yearly turnover of at least 124,800 lume, twice the yearly estimate of 62,400 lume, in the last financial year for which accounts are filed.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:ProcurementProjectLotReference>
      <cbc:ID>LOT-1</cbc:ID>
    </cac:ProcurementProjectLotReference>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:Legislation>
      <cbc:ID>XB-PPA-2019</cbc:ID>
      <cbc:Title>Public Procurement Act</cbc:Title>
      <cbc:Description>Selection criteria: economic and financial standing.</cbc:Description>
      <cbc:JurisdictionLevel>National</cbc:JurisdictionLevel>
      <cbc:Article>Art. 58</cbc:Article>
      <cbc:URI>https://law.bayvarra.example/ppa</cbc:URI>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
      </cac:Language>
      <cac:JurisdictionRegionAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:JurisdictionRegionAddress>
    </cac:Legislation>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-TURNOVER</cbc:ID>
      <cbc:Description>The questions on yearly turnover.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-TURNOVER-1</cbc:ID>
        <cbc:Name>Yearly turnover</cbc:Name>
        <cbc:Description>The turnover of the last financial year for which accounts are filed.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">AMOUNT</cbc:ValueDataTypeCode>
        <cbc:ValueCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:ValueCurrencyCode>
        <cbc:MinimumAmount currencyID="XBL">124800.00</cbc:MinimumAmount>
        <cac:ApplicablePeriod>
          <cbc:StartDate>2024-01-01</cbc:StartDate>
          <cbc:EndDate>2024-12-31</cbc:EndDate>
        </cac:ApplicablePeriod>
        <cac:TemplateEvidence>
          <cbc:ID>EV-ACC</cbc:ID>
          <cbc:Name>Annual accounts</cbc:Name>
        </cac:TemplateEvidence>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-STAFF</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">TECHNICAL</cbc:CriterionTypeCode>
    <cbc:Name>Staff</cbc:Name>
    <cbc:Description>At least ten employees, as the notices ask.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-STAFF</cbc:ID>
      <cbc:Description>The questions on staff.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-STAFF-1</cbc:ID>
        <cbc:Name>Employees</cbc:Name>
        <cbc:Description>The number of persons employed.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">QUANTITY</cbc:ValueDataTypeCode>
        <cbc:ValueUnitCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">IE</cbc:ValueUnitCode>
        <cbc:MinimumQuantity unitCode="IE">10</cbc:MinimumQuantity>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-REFERENCES</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">TECHNICAL</cbc:CriterionTypeCode>
    <cbc:Name>Similar supplies</cbc:Name>
    <cbc:Description>Three supplies of park benches or similar street furniture in the last five years, as the notices ask.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-REFERENCES</cbc:ID>
      <cbc:Description>The questions on similar supplies.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cbc:FulfilmentIndicatorTypeCode listID="urn:ubl-examples:world:codelist:FulfilmentIndicatorCode">ALL</cbc:FulfilmentIndicatorTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-REFERENCES-1</cbc:ID>
        <cbc:Name>The supplies</cbc:Name>
        <cbc:Description>Each supply: the customer, the year, what was supplied and its value.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">DESCRIPTION</cbc:ValueDataTypeCode>
      </cac:TenderingCriterionProperty>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-REFERENCES-2</cbc:ID>
        <cbc:Name>Number of supplies</cbc:Name>
        <cbc:Description>How many such supplies.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">QUANTITY</cbc:ValueDataTypeCode>
        <cbc:ValueUnitCode listID="UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade">EA</cbc:ValueUnitCode>
        <cbc:MinimumQuantity unitCode="EA">3</cbc:MinimumQuantity>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-TIMBER</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">TECHNICAL</cbc:CriterionTypeCode>
    <cbc:Name>Certified timber</cbc:Name>
    <cbc:Description>The slats come from forests managed for regrowth, with a forestry certificate valid for the contract, as the call asks.</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:Legislation>
      <cbc:ID>XB-PPA-2019</cbc:ID>
      <cbc:Title>Public Procurement Act</cbc:Title>
      <cbc:Description>Environmental requirements of the specification (XB-ENV-2021 art. 12).</cbc:Description>
      <cbc:Article>Art. 70</cbc:Article>
    </cac:Legislation>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-TIMBER</cbc:ID>
      <cbc:Description>The questions on certified timber.</cbc:Description>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-TIMBER-1</cbc:ID>
        <cbc:Name>Forestry certificate</cbc:Name>
        <cbc:Description>Whether the timber of the slats is covered by a forestry certificate valid for the two years of the contract.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">INDICATOR</cbc:ValueDataTypeCode>
        <cbc:ExpectedIndicator>true</cbc:ExpectedIndicator>
      </cac:TenderingCriterionProperty>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:TenderingCriterion>
    <cbc:ID>CR-GROUP</cbc:ID>
    <cbc:CriterionTypeCode listID="urn:ubl-examples:world:codelist:CriterionTypeCode">SUITABILITY</cbc:CriterionTypeCode>
    <cbc:Name>Tendering as a group</cbc:Name>
    <cbc:Description>A group of tenderers names its members and the share of each (tender/06#F4).</cbc:Description>
    <cbc:EvaluationMethodTypeCode listID="urn:ubl-examples:world:codelist:EvaluationMethodCode">PASSFAIL</cbc:EvaluationMethodTypeCode>
    <cac:TenderingCriterionPropertyGroup>
      <cbc:ID>PG-GROUP</cbc:ID>
      <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ON</cbc:PropertyGroupTypeCode>
      <cac:TenderingCriterionProperty>
        <cbc:ID>P-GROUP-1</cbc:ID>
        <cbc:Name>A group</cbc:Name>
        <cbc:Description>Whether the tenderer tenders as a member of a group.</cbc:Description>
        <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
        <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">INDICATOR</cbc:ValueDataTypeCode>
      </cac:TenderingCriterionProperty>
      <cac:SubsidiaryTenderingCriterionPropertyGroup>
        <cbc:ID>PG-GROUP-1</cbc:ID>
        <cbc:Name>Group</cbc:Name>
        <cbc:PropertyGroupTypeCode listID="urn:ubl-examples:world:codelist:PropertyGroupTypeCode">ONTRUE</cbc:PropertyGroupTypeCode>
        <cac:TenderingCriterionProperty>
          <cbc:ID>P-GROUP-2</cbc:ID>
          <cbc:Name>Share in the group</cbc:Name>
          <cbc:Description>The share of the work of each member, in per cent.</cbc:Description>
          <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CriterionPropertyTypeCode">QUESTION</cbc:TypeCode>
          <cbc:ValueDataTypeCode listID="urn:ubl-examples:world:codelist:ResponseDataTypeCode">PERCENT</cbc:ValueDataTypeCode>
        </cac:TenderingCriterionProperty>
      </cac:SubsidiaryTenderingCriterionPropertyGroup>
    </cac:TenderingCriterionPropertyGroup>
  </cac:TenderingCriterion>
  <cac:AdditionalDocumentReference>
    <cbc:ID>LPWD-DOC-26-0189</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">CallForTenders</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-QAR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</QualificationApplicationRequest>
```
