# Contract Award Notice: Lumeport Public Works Department to Bayvarra Information Service

*Example 21 of the flow "A public tender (Bayvarra)" · [Contract Award Notice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CONTRACT-AWARD-NOTICE-SCHEMA)*

The award is published; the review body is named for appeals.

[The XML file](21-ContractAwardNotice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:contract-award-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Contract award notice"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0211**  
  The notice number.
- `UUID` = **12583d9b-2491-50ee-89c4-489940d246f5**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-23**  
  Monday 23 March, published after the contract was signed (D28 point 1, tender/21#F12).
- `IssueTime` = **13:55:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Note` = **Award of the framework contract for park benches.**  
  What.
- `VersionID` = **1**  
  The first version.
- `RequestedPublicationDate` = **2026-03-23**  
  When to publish.
- `RegulatoryDomain` = **Bayvarra public procurement**  
  The rules the notice follows.
- `NoticeTypeCode` = **CAN** (listID `urn:ubl-examples:world:codelist:NoticeTypeCode`)  
  The kind of notice. The code is from the Trade Accord's notice type list: CAN = Contract award notice.
- `NoticeLanguageCode` = **en** (listID `ISO 639`)  
  In English, as an ISO 639 code. The code is from the world's copy of ISO 639 Language: en = English.

### Previous Document Reference

Inside `PreviousDocumentReference`:

- `ID` = **LPWD-DOC-26-0188**  
  The contract notice.
- `DocumentTypeCode` = **ContractNotice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LPWD-DOC-26-0188 is the example tender/02, a ContractNotice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: ContractNotice = Contract Notice.

### Minutes Document Reference

Inside `MinutesDocumentReference`:

- `ID` = **PWD-MIN-AWARD-26**  
  The minutes of the evaluation.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-CAN**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
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

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **1906473852** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Bayvarra Information Service (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayvarra Information Service**  
  The trading name; identity of Bayvarra Information Service (world/parties.json).
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
- `PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/PostalZone` = **38520**  
  Postal code in Bayvarra's format (5 digits). identity of Bayvarra Information Service (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayvarra Information Service (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Publications and register**  
  The party's main desk, which handles this document; identity of Bayvarra Information Service (world/parties.json).
- `Contact/JobTitle` = **Publications officer**  
  The job of the person who answers at the desk; identity of Bayvarra Information Service (world/parties.json).
- `Contact/Department` = **Publications**  
  The department the desk belongs to; identity of Bayvarra Information Service (world/parties.json).
- `Contact/Telephone` = **+999 2 38 5339 4832**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayvarra Information Service (world/parties.json).
- `Contact/ElectronicMail` = **publications@info-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayvarra Information Service (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayvarra Information Service (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:1906473852** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Bayvarra Information Service (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tendering Terms

Inside `TenderingTerms`:

- `AppealTerms/AppealReceiverParty/PartyIdentification/ID` = **4718260539** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AppealTerms/AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  The trading name; identity of Procurement Review Board of Bayvarra (world/parties.json).

### Tendering Process

Inside `TenderingProcess`:

- `ID` = **PWD-2026-PARKS-P**  
  The procedure; it reopens no earlier framework (tender/02#F12).
- `Description` = **Open procedure with two lots for a framework agreement with one supplier, with an electronic auction on the unit prices after the evaluation.**  
  The procedure, with the framework and the auction it plans (tender/01#F22).
- `ProcedureCode` = **OPEN** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  An open procedure. The code is from the Trade Accord's procurement procedure list: OPEN = Open procedure.
- `ContractingSystemCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractingSystemCode`)  
  A framework agreement. The code is from the Trade Accord's contracting system list: FRAMEWORK = Framework agreement.
- `OpenTenderEvent/IdentificationID` = **OPEN-1**  
  The opening of the tenders.
- `OpenTenderEvent/OccurrenceDate` = **2026-02-26**  
  Thursday 26 February, the day after the deadline (D28 point 1).
- `OpenTenderEvent/OccurrenceTime` = **10:00:00**  
  In the morning.
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
- `AuctionTerms/AuctionConstraintIndicator` = **true**  
  An electronic auction is held before the award.
- `AuctionTerms/Description` = **After the full evaluation of the tenders, every tenderer with an admissible tender is invited to an electronic auction on the unit prices of both lots. The quality scores stay as evaluated; only the price score changes with the new prices. The auction was held on 4 March 2026 with both admissible tenderers: Brackenmere Furniture lowered its unit price from 496 to 489 lume a bench with its installation; Valdara Industries kept 517 (499 and 18) and still ranks first on price and quality.**  
  The terms of the auction for the tenderers. The award documents add what happened (D28 point 6, tender/02#F37).

### Procurement Project

Inside `ProcurementProject`:

- `ID` = **PWD-2026-PARKS**  
  The project's identifier.
- `Name` = **Park benches for the parks renewal programme**  
  The project's name, the same in every document (tender/01#F4, 08#F6).
- `Description` = **240 park benches with galvanised metal frames and hardwood slats over two years, delivered with their ground anchors and anchored.**  
  What is bought; each lot describes its own part (tender/02#F32).
- `ProcurementTypeCode` = **SUPPLIES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  Supplies or services; the installation is services in every document. The code is from the Trade Accord's contract nature list: SUPPLIES = Supplies.
- `ProcurementSubTypeCode` = **PURCHASE** (listID `urn:ubl-examples:world:codelist:ProcurementSubTypeCode`)  
  The kind within it. The code is from the Trade Accord's procurement subtype list: PURCHASE = Purchase.
- `RequestedDeliveryDate` = **2026-04-02**  
  The first release.
- `EstimatedOverallContractQuantity` = **240** (unitCode `EA`)  
  240 benches over the contract.
- `Note` = **Part of the parks renewal programme 2026. Each release is inspected on delivery and accepted with its installation.**  
  The programme, and the inspection as an acceptance term (tender/01#F28).
- `SMESuitableIndicator` = **true**  
  Small and medium firms can tender.
- `ProcurementAdditionalType/ProcurementTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  The procurement buys supplies with services as a second type: the installation of the benches (tender/01#F12). The code is from the Trade Accord's contract nature list: SERVICES = Services.
- `ProcurementAdditionalType/ProcurementType` = **Services: the installation of the benches, lot 2**  
  The name of code SERVICES in the Trade Accord's contract nature list, followed by the detail of this case: what the services are; the environmental aims are in the execution requirement and the tenderer requirement.
- `RequestedTenderTotal/EstimatedOverallContractAmount` = **124800.00** (currencyID `XBL`)  
  The estimated value.
- `RequestedTenderTotal/EstimatedOverallFrameworkContractsAmount` = **124800.00** (currencyID `XBL`)  
  The framework's estimate.
- `RequestedTenderTotal/TotalAmount` = **124800.00** (currencyID `XBL`)  
  The budget: the estimate.
- `RequestedTenderTotal/TaxIncludedIndicator` = **false**  
  Without tax: a public body pays no sales tax.
- `RequestedTenderTotal/MinimumAmount` = **62400.00** (currencyID `XBL`)  
  At least half will be called off.
- `RequestedTenderTotal/MaximumAmount` = **149760.00** (currencyID `XBL`)  
  At most 20 % more.
- `RequestedTenderTotal/MonetaryScope` = **Two years of releases, without tax: a two-year commitment of the 2026 budget, estimated at 500 lume a bench and 20 lume an installation.**  
  What the amount covers, and that the department made the estimate before the tenders (D28 point 2, tender/01#F27, F29).
- `RequestedTenderTotal/AverageSubsequentContractAmount` = **20800.00** (currencyID `XBL`)  
  Six releases on average.
- `RequestedTenderTotal/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a public body is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `RequestedTenderTotal/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReasonCode` = **PUBLIC** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Public body.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Public body**  
  The name of code PUBLIC in Bayvarra's national sales tax exemption reason list.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `MainCommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What is bought, as a subclass of the UN Central Product Classification, which classifies goods and services alike: seats with metal frames. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `AdditionalCommodityClassification/ItemClassificationCode` = **87390** (listID `UN CPC Ver.2.1`)  
  The installation the project buys besides the benches, as a subclass of the UN CPC: installation services of other goods (tender/01#F30). The code is from the world's copy of UN Central Product Classification, Version 2.1: 87390 = Installation services of other goods n.e.c..
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
- `ContractExtension/OptionsDescription` = **One extension of a year with 120 more benches and their installation.**  
  The option.
- `ContractExtension/MaximumNumberNumeric` = **1**  
  At most one.
- `ContractExtension/RenewalsIndicator` = **true**  
  The contract may be renewed.
- `ContractExtension/OptionValidityPeriod/EndDate` = **2028-03-22**  
  Decided before it ends.
- `ContractExtension/Renewal/Amount` = **62400.00** (currencyID `XBL`)  
  The value of a renewal.
- `ContractExtension/Renewal/Period/DurationMeasure` = **12** (unitCode `MON`)  
  Twelve months.
- `RequestForTenderLine/ID` = **1**  
  The benches.
- `RequestForTenderLine/UUID` = **b98b5bc4-6b96-59da-b8e9-89fc28afcae4**  
  Its UUID.
- `RequestForTenderLine/Note` = **Galvanised metal frame, five hardwood slats, ground anchors.**  
  The requirement.
- `RequestForTenderLine/Quantity` = **240** (unitCode `EA`)  
  Over the contract.
- `RequestForTenderLine/MinimumQuantity` = **120** (unitCode `EA`)  
  At least.
- `RequestForTenderLine/MaximumQuantity` = **288** (unitCode `EA`)  
  At most.
- `RequestForTenderLine/TaxIncludedIndicator` = **false**  
  Prices without tax.
- `RequestForTenderLine/MinimumAmount` = **84000.00** (currencyID `XBL`)  
  The line's total at 350 lume a bench, below which a tender would be abnormally low: on the same basis as the estimate (tender/01#F13).
- `RequestForTenderLine/MaximumAmount` = **144000.00** (currencyID `XBL`)  
  The line's total at the most the budget allows per bench, 600 lume.
- `RequestForTenderLine/EstimatedAmount` = **120000.00** (currencyID `XBL`)  
  The estimate: 240 benches at 500 lume.
- `RequestForTenderLine/DocumentReference/ID` = **PWD-SPEC-BENCH-26**  
  The technical specification.
- `RequestForTenderLine/DocumentReference/DocumentType` = **Technical specification**  
  The kind of document referred to, the department's technical specification of the bench, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
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
  Part of the bench: the anchors are in lot 1, the anchoring in lot 2.
- `RequestForTenderLine/ID` = **2**  
  The installation.
- `RequestForTenderLine/Note` = **Assembly of each bench and anchoring in the ground with its anchor set.**  
  The requirement.
- `RequestForTenderLine/Quantity` = **240** (unitCode `EA`)  
  One installation per bench.
- `RequestForTenderLine/TaxIncludedIndicator` = **false**  
  Prices without tax.
- `RequestForTenderLine/EstimatedAmount` = **4800.00** (currencyID `XBL`)  
  The estimate: 240 installations at 20 lume.
- `RequestForTenderLine/Item/Name` = **Installation of a park bench**  
  The service asked for.

### Procurement Project Lot

Inside `ProcurementProjectLot`:

- `ID` = **LOT-1**  
  Lot 1.
- `ProcurementProject/Name` = **Park benches**  
  The project, or the lot, the document is about, by the name the notices give it (tender/08#F6).
- `ProcurementProject/ProcurementTypeCode` = **SUPPLIES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  The kind of procurement; the installation is services in every document (tender/01#F4). The code is from the Trade Accord's contract nature list: SUPPLIES = Supplies.
- `ID` = **LOT-2**  
  Lot 2.
- `ProcurementProject/Name` = **Installation of the benches**  
  The project, or the lot, the document is about, by the name the notices give it (tender/08#F6).
- `ProcurementProject/ProcurementTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  The kind of procurement; the installation is services in every document (tender/01#F4). The code is from the Trade Accord's contract nature list: SERVICES = Services.

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
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `WinningParty/Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `WinningParty/Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ContractAwardNotice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ContractAwardNotice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:contract-award-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0211</cbc:ID>
  <cbc:UUID>12583d9b-2491-50ee-89c4-489940d246f5</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>13:55:00-01:00</cbc:IssueTime>
  <cbc:Note>Award of the framework contract for park benches.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:RequestedPublicationDate>2026-03-23</cbc:RequestedPublicationDate>
  <cbc:RegulatoryDomain>Bayvarra public procurement</cbc:RegulatoryDomain>
  <cbc:NoticeTypeCode listID="urn:ubl-examples:world:codelist:NoticeTypeCode">CAN</cbc:NoticeTypeCode>
  <cbc:NoticeLanguageCode listID="ISO 639">en</cbc:NoticeLanguageCode>
  <cac:PreviousDocumentReference>
    <cbc:ID>LPWD-DOC-26-0188</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ContractNotice</cbc:DocumentTypeCode>
  </cac:PreviousDocumentReference>
  <cac:MinutesDocumentReference>
    <cbc:ID>PWD-MIN-AWARD-26</cbc:ID>
  </cac:MinutesDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-CAN</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
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
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">1906473852</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayvarra Information Service</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-634627</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Civic Square</cbc:StreetName>
      <cbc:BuildingNumber>27</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38520</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Publications and register</cbc:Name>
      <cbc:JobTitle>Publications officer</cbc:JobTitle>
      <cbc:Department>Publications</cbc:Department>
      <cbc:Telephone>+999 2 38 5339 4832</cbc:Telephone>
      <cbc:ElectronicMail>publications@info-xb.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:1906473852</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:TenderingTerms>
    <cac:AppealTerms>
      <cac:AppealReceiverParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">4718260539</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
        </cac:PartyName>
      </cac:AppealReceiverParty>
    </cac:AppealTerms>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:ID>PWD-2026-PARKS-P</cbc:ID>
    <cbc:Description>Open procedure with two lots for a framework agreement with one supplier, with an electronic auction on the unit prices after the evaluation.</cbc:Description>
    <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">OPEN</cbc:ProcedureCode>
    <cbc:ContractingSystemCode listID="urn:ubl-examples:world:codelist:ContractingSystemCode">FRAMEWORK</cbc:ContractingSystemCode>
    <cac:OpenTenderEvent>
      <cbc:IdentificationID>OPEN-1</cbc:IdentificationID>
      <cbc:OccurrenceDate>2026-02-26</cbc:OccurrenceDate>
      <cbc:OccurrenceTime>10:00:00</cbc:OccurrenceTime>
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
      <cbc:AuctionConstraintIndicator>true</cbc:AuctionConstraintIndicator>
      <cbc:Description>After the full evaluation of the tenders, every tenderer with an admissible tender is invited to an electronic auction on the unit prices of both lots. The quality scores stay as evaluated; only the price score changes with the new prices. The auction was held on 4 March 2026 with both admissible tenderers: Brackenmere Furniture lowered its unit price from 496 to 489 lume a bench with its installation; Valdara Industries kept 517 (499 and 18) and still ranks first on price and quality.</cbc:Description>
    </cac:AuctionTerms>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:ID>PWD-2026-PARKS</cbc:ID>
    <cbc:Name>Park benches for the parks renewal programme</cbc:Name>
    <cbc:Description>240 park benches with galvanised metal frames and hardwood slats over two years, delivered with their ground anchors and anchored.</cbc:Description>
    <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SUPPLIES</cbc:ProcurementTypeCode>
    <cbc:ProcurementSubTypeCode listID="urn:ubl-examples:world:codelist:ProcurementSubTypeCode">PURCHASE</cbc:ProcurementSubTypeCode>
    <cbc:RequestedDeliveryDate>2026-04-02</cbc:RequestedDeliveryDate>
    <cbc:EstimatedOverallContractQuantity unitCode="EA">240</cbc:EstimatedOverallContractQuantity>
    <cbc:Note>Part of the parks renewal programme 2026. Each release is inspected on delivery and accepted with its installation.</cbc:Note>
    <cbc:SMESuitableIndicator>true</cbc:SMESuitableIndicator>
    <cac:ProcurementAdditionalType>
      <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SERVICES</cbc:ProcurementTypeCode>
      <cbc:ProcurementType>Services: the installation of the benches, lot 2</cbc:ProcurementType>
    </cac:ProcurementAdditionalType>
    <cac:RequestedTenderTotal>
      <cbc:EstimatedOverallContractAmount currencyID="XBL">124800.00</cbc:EstimatedOverallContractAmount>
      <cbc:EstimatedOverallFrameworkContractsAmount currencyID="XBL">124800.00</cbc:EstimatedOverallFrameworkContractsAmount>
      <cbc:TotalAmount currencyID="XBL">124800.00</cbc:TotalAmount>
      <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
      <cbc:MinimumAmount currencyID="XBL">62400.00</cbc:MinimumAmount>
      <cbc:MaximumAmount currencyID="XBL">149760.00</cbc:MaximumAmount>
      <cbc:MonetaryScope>Two years of releases, without tax: a two-year commitment of the 2026 budget, estimated at 500 lume a bench and 20 lume an installation.</cbc:MonetaryScope>
      <cbc:AverageSubsequentContractAmount currencyID="XBL">20800.00</cbc:AverageSubsequentContractAmount>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">PUBLIC</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Public body</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequestedTenderTotal>
    <cac:MainCommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
    </cac:MainCommodityClassification>
    <cac:AdditionalCommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">87390</cbc:ItemClassificationCode>
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
      <cbc:OptionsDescription>One extension of a year with 120 more benches and their installation.</cbc:OptionsDescription>
      <cbc:MaximumNumberNumeric>1</cbc:MaximumNumberNumeric>
      <cbc:RenewalsIndicator>true</cbc:RenewalsIndicator>
      <cac:OptionValidityPeriod>
        <cbc:EndDate>2028-03-22</cbc:EndDate>
      </cac:OptionValidityPeriod>
      <cac:Renewal>
        <cbc:Amount currencyID="XBL">62400.00</cbc:Amount>
        <cac:Period>
          <cbc:DurationMeasure unitCode="MON">12</cbc:DurationMeasure>
        </cac:Period>
      </cac:Renewal>
    </cac:ContractExtension>
    <cac:RequestForTenderLine>
      <cbc:ID>1</cbc:ID>
      <cbc:UUID>b98b5bc4-6b96-59da-b8e9-89fc28afcae4</cbc:UUID>
      <cbc:Note>Galvanised metal frame, five hardwood slats, ground anchors.</cbc:Note>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cbc:MinimumQuantity unitCode="EA">120</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">288</cbc:MaximumQuantity>
      <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
      <cbc:MinimumAmount currencyID="XBL">84000.00</cbc:MinimumAmount>
      <cbc:MaximumAmount currencyID="XBL">144000.00</cbc:MaximumAmount>
      <cbc:EstimatedAmount currencyID="XBL">120000.00</cbc:EstimatedAmount>
      <cac:DocumentReference>
        <cbc:ID>PWD-SPEC-BENCH-26</cbc:ID>
        <cbc:DocumentType>Technical specification</cbc:DocumentType>
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
    <cac:RequestForTenderLine>
      <cbc:ID>2</cbc:ID>
      <cbc:Note>Assembly of each bench and anchoring in the ground with its anchor set.</cbc:Note>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
      <cbc:EstimatedAmount currencyID="XBL">4800.00</cbc:EstimatedAmount>
      <cac:Item>
        <cbc:Name>Installation of a park bench</cbc:Name>
      </cac:Item>
    </cac:RequestForTenderLine>
  </cac:ProcurementProject>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-1</cbc:ID>
    <cac:ProcurementProject>
      <cbc:Name>Park benches</cbc:Name>
      <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SUPPLIES</cbc:ProcurementTypeCode>
    </cac:ProcurementProject>
  </cac:ProcurementProjectLot>
  <cac:ProcurementProjectLot>
    <cbc:ID>LOT-2</cbc:ID>
    <cac:ProcurementProject>
      <cbc:Name>Installation of the benches</cbc:Name>
      <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SERVICES</cbc:ProcurementTypeCode>
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
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:WinningParty>
  </cac:TenderResult>
</ContractAwardNotice>
```
