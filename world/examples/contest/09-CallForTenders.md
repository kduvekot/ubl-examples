# Call For Tenders: Lumeport Public Works Department to Brackenmere Furniture

*Example 9 of the flow "A design contest for the promenade bench (Bayvarra)" · [Call For Tenders in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CALL-FOR-TENDERS-SCHEMA)*

Version 2 of the contest documents, with the corrected site plan.

[The XML file](09-CallForTenders.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:call-for-tenders:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Call for tenders"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **CONTEST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0635**  
  The number of the contest documents.
- `UUID` = **14a2c6de-5d51-5968-b1ad-5cfe506bac85**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PROM-DC**  
  The department's file number for the contest, the same on every document of it.
- `IssueDate` = **2026-04-06**  
  The revised documents, sent with the corrigendum to everyone who retrieved them.
- `IssueTime` = **16:45:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Note` = **The brief, the site plan and the rules of the contest. The contest documents are available to everyone on the department's platform from the contest notice; this is the set Brackenmere Furniture obtained. Version 2: the site plan revision B replaces revision A, and the design lead may also be a registered industrial designer, as the corrigendum says.**  
  What the documents are, and why they name one receiver before the selection (D29 point 7, contest/04#F7). What version 2 changes, said in the document (D29 point 4).
- `VersionID` = **2**  
  The second version, which supersedes the first: the site plan is replaced by revision B and the selection criterion widened, as the corrigendum says.
- `PreviousVersionID` = **1**  
  The version this one supersedes: version 1 of the same document, with the same number.

### Technical Document Reference

Inside `TechnicalDocumentReference`:

- `ID` = **PWD-PROM-BRIEF**  
  The design brief.
- `DocumentType` = **Design brief**  
  What it is (contest/04#F3).
- `Attachment/ExternalReference/URI` = **https://tenders.lumeport.example/PWD-2026-PROM-DC/brief**  
  Where it is obtained: the contest's page on the department's platform.

### Provided Document Reference

Inside `ProvidedDocumentReference`:

- `ID` = **PWD-PROM-SITE-PLAN-B**  
  The site plan, revision B: the sea wall is 420 m long, not 240 m as revision A showed.
- `DocumentType` = **Site plan**  
  What it is.
- `VersionID` = **B**  
  Its revision, so the change between the versions can be read (contest/09#F8).
- `DocumentDescription` = **Revision B replaces revision A: the sea wall is 420 m long, not 240 m.**  
  What the revision changes.
- `Attachment/ExternalReference/URI` = **https://tenders.lumeport.example/PWD-2026-PROM-DC/site-plan-b**  
  Where it is obtained.

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

- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brackenmere Furniture (world/parties.json).
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Trade sales**  
  The party's main desk, which handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Contact/JobTitle` = **Trade sales manager**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 602 606**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brackenmere Furniture (world/parties.json).
- `Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tendering Terms

Inside `TenderingTerms`:

- `TendererQualificationRequest/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form the department asks for: a group of designers and engineers must form a private limited company before the follow-up service contract is awarded, as the procurement act allows where the contract needs one liable contractor. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `TendererQualificationRequest/CompanyLegalForm` = **Limited company (private): required of a group of participants, which forms one before the follow-up contract is awarded**  
  The name of code LTD in Bayvarra's national company legal form list, followed by the detail of this case: the requirement on groups, as the code states it (D29 point 8, contest/03#F7); for the contest itself a group names a lead member (below).
- `TendererQualificationRequest/Description` = **The design lead is a registered architect or a registered industrial designer.**  
  The professional qualification asked for, widened by the corrigendum to industrial designers, whom the earlier text excluded without reason.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/EvaluationCriterionTypeCode` = **REFERENCES** (listID `urn:ubl-examples:world:codelist:EvaluationCriterionTypeCode`)  
  References. The code is from the Trade Accord's evaluation criterion type list: REFERENCES = References.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/Description` = **Two completed designs of furniture or fittings for public spaces in the last five years.**  
  What the jury checks to select the participants.
- `TendererQualificationRequest/TechnicalEvaluationCriterion/ThresholdQuantity` = **2** (unitCode `EA`)  
  Two references; the five years are the window the references fall in, stated in the description, not a period the criterion is valid for (contest/03#F8).
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
- `AppealTerms/AppealReceiverParty/PartyIdentification/ID` = **4718260539** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AppealTerms/AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  The trading name; identity of Procurement Review Board of Bayvarra (world/parties.json).
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
- `TenderSubmissionDeadlinePeriod/EndDate` = **2026-06-12**  
  Designs by then.
- `TenderSubmissionDeadlinePeriod/EndTime` = **12:00:00**  
  At noon.
- `ParticipationRequestReceptionPeriod/EndDate` = **2026-04-30**  
  Requests to participate by then: Thursday 30 April, later than the Friday 17 April of version 1, to give time for the corrected site plan (D29 point 10).
- `NoticeDocumentReference/ID` = **LPWD-DOC-26-0633**  
  The prior information notice of the contest.
- `NoticeDocumentReference/ID` = **LPWD-DOC-26-0634**  
  The contest notice the documents belong to (contest/04#F13).
- `NoticeDocumentReference/VersionID` = **2**  
  The version of the notice they go with.
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
  The prizes, 14,000 lume, and the follow-up service contract, estimated at 40,000 lume (contest/01#F6).
- `RequestedTenderTotal/MonetaryScope` = **The three prizes (14,000 lume) and the follow-up service contract for the detailed design and the supervision of the production (about 40,000 lume). The production of the benches is not part of it.**  
  What the estimate covers, in words (D29 point 5).
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
<CallForTenders xmlns="urn:oasis:names:specification:ubl:schema:xsd:CallForTenders-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:call-for-tenders:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>CONTEST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0635</cbc:ID>
  <cbc:UUID>14a2c6de-5d51-5968-b1ad-5cfe506bac85</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PROM-DC</cbc:ContractFolderID>
  <cbc:IssueDate>2026-04-06</cbc:IssueDate>
  <cbc:IssueTime>16:45:00-01:00</cbc:IssueTime>
  <cbc:Note>The brief, the site plan and the rules of the contest. The contest documents are available to everyone on the department's platform from the contest notice; this is the set Brackenmere Furniture obtained. Version 2: the site plan revision B replaces revision A, and the design lead may also be a registered industrial designer, as the corrigendum says.</cbc:Note>
  <cbc:VersionID>2</cbc:VersionID>
  <cbc:PreviousVersionID>1</cbc:PreviousVersionID>
  <cac:TechnicalDocumentReference>
    <cbc:ID>PWD-PROM-BRIEF</cbc:ID>
    <cbc:DocumentType>Design brief</cbc:DocumentType>
    <cac:Attachment>
      <cac:ExternalReference>
        <cbc:URI>https://tenders.lumeport.example/PWD-2026-PROM-DC/brief</cbc:URI>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:TechnicalDocumentReference>
  <cac:ProvidedDocumentReference>
    <cbc:ID>PWD-PROM-SITE-PLAN-B</cbc:ID>
    <cbc:DocumentType>Site plan</cbc:DocumentType>
    <cbc:VersionID>B</cbc:VersionID>
    <cbc:DocumentDescription>Revision B replaces revision A: the sea wall is 420 m long, not 240 m.</cbc:DocumentDescription>
    <cac:Attachment>
      <cac:ExternalReference>
        <cbc:URI>https://tenders.lumeport.example/PWD-2026-PROM-DC/site-plan-b</cbc:URI>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:ProvidedDocumentReference>
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
      <cbc:Name>Trade sales</cbc:Name>
      <cbc:JobTitle>Trade sales manager</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 602 606</cbc:Telephone>
      <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:TenderingTerms>
    <cac:TendererQualificationRequest>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private): required of a group of participants, which forms one before the follow-up contract is awarded</cbc:CompanyLegalForm>
      <cbc:Description>The design lead is a registered architect or a registered industrial designer.</cbc:Description>
      <cac:TechnicalEvaluationCriterion>
        <cbc:EvaluationCriterionTypeCode listID="urn:ubl-examples:world:codelist:EvaluationCriterionTypeCode">REFERENCES</cbc:EvaluationCriterionTypeCode>
        <cbc:Description>Two completed designs of furniture or fittings for public spaces in the last five years.</cbc:Description>
        <cbc:ThresholdQuantity unitCode="EA">2</cbc:ThresholdQuantity>
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
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">4718260539</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
        </cac:PartyName>
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
    <cac:TenderSubmissionDeadlinePeriod>
      <cbc:EndDate>2026-06-12</cbc:EndDate>
      <cbc:EndTime>12:00:00</cbc:EndTime>
    </cac:TenderSubmissionDeadlinePeriod>
    <cac:ParticipationRequestReceptionPeriod>
      <cbc:EndDate>2026-04-30</cbc:EndDate>
    </cac:ParticipationRequestReceptionPeriod>
    <cac:NoticeDocumentReference>
      <cbc:ID>LPWD-DOC-26-0633</cbc:ID>
    </cac:NoticeDocumentReference>
    <cac:NoticeDocumentReference>
      <cbc:ID>LPWD-DOC-26-0634</cbc:ID>
      <cbc:VersionID>2</cbc:VersionID>
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
      <cbc:MonetaryScope>The three prizes (14,000 lume) and the follow-up service contract for the detailed design and the supervision of the production (about 40,000 lume). The production of the benches is not part of it.</cbc:MonetaryScope>
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
</CallForTenders>
```
