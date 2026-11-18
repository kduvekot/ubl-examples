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
- `ID` = **LPWD-DOC-26-0207**  
  The notice number.
- `UUID` = **12583d9b-2491-50ee-89c4-489940d246f5**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-13**  
  Published four days after the award decision, while the standstill period runs.
- `IssueTime` = **13:55:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
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
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Contracting Party

Inside `ContractingParty`:

- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
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
- `Party/Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; identity of Lumeport Public Works Department (world/parties.json).
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

- `PartyIdentification/ID` = **20410959** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayvarra Information Service (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
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

- `AppealTerms/AppealReceiverParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AppealTerms/AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  The trading name; identity of Procurement Review Board of Bayvarra (world/parties.json).

### Tendering Process

Inside `TenderingProcess`:

- `ID` = **PWD-2026-PARKS-P**  
  The procedure.
- `OriginalContractingSystemID` = **PWD-FW-2024-PARKS**  
  The framework this one follows.
- `Description` = **Open procedure with two lots.**  
  The procedure.
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
- `AdditionalDocumentReference/DocumentType` = **Technical specification**  
  The kind of document referred to, the department's technical specification of the bench, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `ProcessJustification/ProcessReasonCode` = **STANDARD** (listID `urn:ubl-examples:world:codelist:ProcessReasonCode`)  
  The open procedure is the rule. The code is from the Trade Accord's process reason list: STANDARD = Standard.
- `ProcessJustification/ProcessReason` = **Value above the threshold for open procedures.**  
  Why.
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
- `AuctionTerms/AuctionConstraintIndicator` = **true**  
  An electronic auction is held before the award.
- `AuctionTerms/JustificationDescription` = **The benches are a standard product whose quality is fully scored before the auction; the price can then be improved in open competition.**  
  Why the department uses an auction.
- `AuctionTerms/Description` = **After the full evaluation of the tenders, every tenderer with an admissible tender is invited to an electronic auction on the unit prices of both lots. The quality scores stay as evaluated; only the price score changes with the new prices. The auction was held on 6 March 2026 with both admissible tenderers and closed after its first round without a new bid, so the prices of the tenders stand.**  
  The terms of the auction for the tenderers. The award notice adds what happened: neither tenderer lowered its price.
- `AuctionTerms/ProcessDescription` = **One round, opened by an invitation sent two working days ahead. After each bid every tenderer sees its current rank. The round closes when ten minutes pass without a new bid.**  
  How the auction runs.
- `AuctionTerms/ConditionsDescription` = **A bid may only lower the unit prices of the tender, by at least the minimum step of the price criterion; all other terms of the tender stay binding.**  
  The conditions for bidding.
- `AuctionTerms/ElectronicDeviceDescription` = **The auction module of the department's tender platform, in a current web browser over HTTPS; tenderers log in with the platform account they submitted their tender with.**  
  The device and how to connect.
- `AuctionTerms/AuctionURI` = **https://tenders.lumeport.example/auctions**  
  The auction module's address.
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
- `FrameworkAgreement/SubsequentProcessTenderRequirement/Description` = **Each release is ordered from the framework supplier at the framework prices, without a new competition.**  
  How a release is placed.
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
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Public body.
- `RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Public body**  
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
- `RequiredDocumentReference/DocumentType` = **Price schedule template**  
  The kind of document referred to, the template for the tenderers' prices, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `ProvidedDocumentReference/ID` = **PWD-SITE-PLAN**  
  The parks' site plan.
- `ProvidedDocumentReference/DocumentTypeCode` = **174** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, the public works department's site plan of the parks, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 174 = Drawing.
- `AdditionalDocumentReference/ID` = **PWD-QA-26**  
  Questions and answers.
- `AdditionalDocumentReference/DocumentType` = **Questions and answers**  
  The kind of document referred to, the questions and answers of the procedure, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
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
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Public body.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Public body**  
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
- `ProcurementProject/RequestForTenderLine/DocumentReference/DocumentType` = **Technical specification**  
  The kind of document referred to, the department's technical specification of the bench, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
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
- `RequiredDocumentReference/DocumentType` = **Price schedule template**  
  The kind of document referred to, the template for the tenderers' prices, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `ProvidedDocumentReference/ID` = **PWD-SITE-PLAN**  
  The parks' site plan.
- `ProvidedDocumentReference/DocumentTypeCode` = **174** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, the public works department's site plan of the parks, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 174 = Drawing.
- `AdditionalDocumentReference/ID` = **PWD-QA-26**  
  Questions and answers.
- `AdditionalDocumentReference/DocumentType` = **Questions and answers**  
  The kind of document referred to, the questions and answers of the procedure, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
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
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Public body.
- `ProcurementProject/RequestedTenderTotal/ApplicableTaxCategory/TaxExemptionReason` = **Public body**  
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
- `SubcontractTerms/Rate` = **3.5**  
  The installation's share of the contract value: 4,320 of 124,080.00 lume, rounded.
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
- `WinningParty/Party/AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
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
  <cbc:ID>LPWD-DOC-26-0207</cbc:ID>
  <cbc:UUID>12583d9b-2491-50ee-89c4-489940d246f5</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-13</cbc:IssueDate>
  <cbc:IssueTime>13:55:00-01:00</cbc:IssueTime>
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
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ContractNotice</cbc:DocumentTypeCode>
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
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
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
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410959</cbc:ID>
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
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
        </cac:PartyName>
      </cac:AppealReceiverParty>
    </cac:AppealTerms>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:ID>PWD-2026-PARKS-P</cbc:ID>
    <cbc:OriginalContractingSystemID>PWD-FW-2024-PARKS</cbc:OriginalContractingSystemID>
    <cbc:Description>Open procedure with two lots.</cbc:Description>
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
      <cbc:DocumentType>Technical specification</cbc:DocumentType>
    </cac:AdditionalDocumentReference>
    <cac:ProcessJustification>
      <cbc:ProcessReasonCode listID="urn:ubl-examples:world:codelist:ProcessReasonCode">STANDARD</cbc:ProcessReasonCode>
      <cbc:ProcessReason>Value above the threshold for open procedures.</cbc:ProcessReason>
    </cac:ProcessJustification>
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
      <cbc:AuctionConstraintIndicator>true</cbc:AuctionConstraintIndicator>
      <cbc:JustificationDescription>The benches are a standard product whose quality is fully scored before the auction; the price can then be improved in open competition.</cbc:JustificationDescription>
      <cbc:Description>After the full evaluation of the tenders, every tenderer with an admissible tender is invited to an electronic auction on the unit prices of both lots. The quality scores stay as evaluated; only the price score changes with the new prices. The auction was held on 6 March 2026 with both admissible tenderers and closed after its first round without a new bid, so the prices of the tenders stand.</cbc:Description>
      <cbc:ProcessDescription>One round, opened by an invitation sent two working days ahead. After each bid every tenderer sees its current rank. The round closes when ten minutes pass without a new bid.</cbc:ProcessDescription>
      <cbc:ConditionsDescription>A bid may only lower the unit prices of the tender, by at least the minimum step of the price criterion; all other terms of the tender stay binding.</cbc:ConditionsDescription>
      <cbc:ElectronicDeviceDescription>The auction module of the department's tender platform, in a current web browser over HTTPS; tenderers log in with the platform account they submitted their tender with.</cbc:ElectronicDeviceDescription>
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
        <cbc:Description>Each release is ordered from the framework supplier at the framework prices, without a new competition.</cbc:Description>
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
      <cbc:DocumentType>Price schedule template</cbc:DocumentType>
    </cac:RequiredDocumentReference>
    <cac:ProvidedDocumentReference>
      <cbc:ID>PWD-SITE-PLAN</cbc:ID>
      <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">174</cbc:DocumentTypeCode>
    </cac:ProvidedDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>PWD-QA-26</cbc:ID>
      <cbc:DocumentType>Questions and answers</cbc:DocumentType>
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
      <cbc:DocumentType>Price schedule template</cbc:DocumentType>
    </cac:RequiredDocumentReference>
    <cac:ProvidedDocumentReference>
      <cbc:ID>PWD-SITE-PLAN</cbc:ID>
      <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">174</cbc:DocumentTypeCode>
    </cac:ProvidedDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>PWD-QA-26</cbc:ID>
      <cbc:DocumentType>Questions and answers</cbc:DocumentType>
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
          <cbc:TaxExemptionReason>Public body</cbc:TaxExemptionReason>
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
      <cbc:Rate>3.5</cbc:Rate>
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
          <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:WinningParty>
  </cac:TenderResult>
</ContractAwardNotice>
```
