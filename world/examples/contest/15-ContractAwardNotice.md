# Contract Award Notice: Lumeport Public Works Department to Bayvarra Information Service

*Example 15 of the flow "A design contest for the promenade bench (Bayvarra)" · [Contract Award Notice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CONTRACT-AWARD-NOTICE-SCHEMA)*

The results of the contest are published: first prize to the furniture maker's team, second to the manufacturer.

[The XML file](15-ContractAwardNotice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:contract-award-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Contract award notice"; the community specification "Public procurement community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **PWD/2026/PROM-DC**  
  The collaboration this document belongs to: the department's design contest for the promenade bench. Lumeport Public Works Department started it and gave it this identifier, which every document of it repeats.
- `ID` = **PWD/2026/1250**  
  The notice number, the same in both versions.
- `UUID` = **c61705b1-9bf8-569a-ab88-3def7dd13ffb**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD/2026/PROM-DC**  
  The department's file number for the contest, the same on every document of it.
- `IssueDate` = **2026-07-02**  
  Published after the jury's decision.
- `IssueTime` = **11:31:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **Results of the design contest for the harbour promenade bench.**  
  What.
- `VersionID` = **1**  
  The first version.
- `NoticeTypeCode` = **CAN-DESG** (listID `urn:ubl-examples:world:codelist:NoticeTypeCode`)  
  A design contest result notice (the Accord's list, after the eForms notice type can-desg). The code is from the Trade Accord's notice type list: CAN-DESG = Design contest result notice.

### Previous Document Reference

Inside `PreviousDocumentReference`:

- `ID` = **PWD/2026/0530**  
  The contest notice.
- `DocumentTypeCode` = **ContractNotice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: PWD/2026/0530 is the example contest/03, a ContractNotice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ContractNotice = Contract Notice.

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
  Street of the postal address. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Public Works Department gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Public Works Department gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeport Public Works Department gives it.
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  The contact's e-mail address; as Lumeport Public Works Department gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Public Works Department gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **1906473852** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Bayvarra Information Service gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayvarra Information Service**  
  The trading name; as Bayvarra Information Service gives it.
- `PostalAddress/ID` = **LUM-ADR-634627** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Bayvarra Information Service gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. As Bayvarra Information Service gives it.
- `PostalAddress/BuildingNumber` = **27**  
  Building number of the postal address. As Bayvarra Information Service gives it.
- `PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Bayvarra Information Service gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bayvarra Information Service gives it.
- `PostalAddress/PostalZone` = **38520**  
  Postal code in Bayvarra's format (5 digits). As Bayvarra Information Service gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bayvarra Information Service gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Publications and register**  
  The party's main desk, which handles this document; as Bayvarra Information Service gives it.
- `Contact/JobTitle` = **Publications officer**  
  The job of the person who answers at the desk; as Bayvarra Information Service gives it.
- `Contact/Department` = **Publications**  
  The department the desk belongs to; as Bayvarra Information Service gives it.
- `Contact/Telephone` = **+999 2 38 5339 4832**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bayvarra Information Service gives it.
- `Contact/ElectronicMail` = **publications@info-xb.example**  
  The contact's e-mail address; as Bayvarra Information Service gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayvarra Information Service gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:1906473852** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Bayvarra Information Service gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tendering Terms

Inside `TenderingTerms`:

- `AwardingTerms/Prize/RankCode` = **FIRST** (listID `urn:ubl-examples:world:codelist:PrizeRankCode`)  
  The first prize. The code is from the Trade Accord's prize rank list: FIRST = First prize.
- `AwardingTerms/Prize/ValueAmount` = **6000.00** (currencyID `XBL`)  
  Wrongly given as the amount first planned.
- `AwardingTerms/Prize/Description` = **For the design the jury ranks first; its author is invited to negotiate the follow-up service contract.**  
  What comes with the prize.
- `AwardingTerms/Prize/RankCode` = **SECOND** (listID `urn:ubl-examples:world:codelist:PrizeRankCode`)  
  The second prize. The code is from the Trade Accord's prize rank list: SECOND = Second prize.
- `AwardingTerms/Prize/ValueAmount` = **4000.00** (currencyID `XBL`)  
  The second prize, unchanged since it was planned.
- `AwardingTerms/Prize/Description` = **For the design the jury ranks second.**  
  What it is for.

### Tendering Process

Inside `TenderingProcess`:

- `NegotiationDescription` = **The service contract for the detailed design and the supervision of the production is negotiated with the first-prize winner, without a new call for competition, on fees, timetable and the number of prototypes.**  
  The negotiation that follows the contest.
- `ProcedureCode` = **DESIGNCONTEST** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  A design contest. The code is from the Trade Accord's procurement procedure list: DESIGNCONTEST = Design contest.
- `CandidateReductionConstraintIndicator` = **true**  
  The number of candidates was reduced: the jury selected five participants from the requests, as the notice announced. Stated here, after the selection, not in the notice and the call.
- `EconomicOperatorShortList/LimitationDescription` = **Only the winner of the first prize is invited to negotiate the follow-up contract, as the contest notice announced.**  
  Why one party.
- `EconomicOperatorShortList/PreSelectedParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EconomicOperatorShortList/PreSelectedParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `EconomicOperatorShortList/PreSelectedParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EconomicOperatorShortList/PreSelectedParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.

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
- `RequestedTenderTotal/MonetaryScope` = **The three prizes (14,000 lume) and the follow-up service contract for the detailed design and the supervision of the production (about 40,000 lume). The production of the benches is not part of it.**  
  What the estimate covers, in words.
- `MainCommodityClassification/ItemClassificationCode` = **83912** (listID `UN CPC Ver.2.1`)  
  The contest is for an industrial design, as a subclass of the UN Central Product Classification. The code is from the world's copy of UN Central Product Classification, Version 2.1: 83912 = Industrial design services.
- `RealizedLocation/Name` = **Harbour promenade, Lumeport**  
  Where the furniture will stand.
- `RealizedLocation/Address/CityName` = **Lumeport**  
  The city.
- `RealizedLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Tender Result

Inside `TenderResult`:

- `TenderResultCode` = **AWARDED** (listID `urn:ubl-examples:world:codelist:TenderResultCode`)  
  The prizes are awarded. The code is from the Trade Accord's tender result list: AWARDED = Awarded.
- `Description` = **First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.**  
  The jury's decision.
- `AwardDate` = **2026-06-26**  
  The day the jury decided: Friday 26 June.
- `ReceivedTenderQuantity` = **4** (unitCode `EA`)  
  Four of the five selected participants submitted a design.
- `ReceivedForeignTenderQuantity` = **1** (unitCode `EA`)  
  Valdara Industries, from Urvania.
- `WinningParty/Rank` = **1**  
  First prize: the lead member of the winning team.
- `WinningParty/Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `WinningParty/Party/AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `WinningParty/Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.
- `WinningParty/Rank` = **1**  
  First prize: the team's other member, a winner as much as its lead.
- `WinningParty/Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Saltmere Engineering gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `WinningParty/Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; as Saltmere Engineering gives it.
- `WinningParty/Rank` = **2**  
  Second prize.
- `WinningParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `WinningParty/Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `WinningParty/Party/PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ContractAwardNotice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ContractAwardNotice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:contract-award-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PWD/2026/PROM-DC</cbc:ProfileExecutionID>
  <cbc:ID>PWD/2026/1250</cbc:ID>
  <cbc:UUID>c61705b1-9bf8-569a-ab88-3def7dd13ffb</cbc:UUID>
  <cbc:ContractFolderID>PWD/2026/PROM-DC</cbc:ContractFolderID>
  <cbc:IssueDate>2026-07-02</cbc:IssueDate>
  <cbc:IssueTime>11:31:00-01:00</cbc:IssueTime>
  <cbc:Note>Results of the design contest for the harbour promenade bench.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:NoticeTypeCode listID="urn:ubl-examples:world:codelist:NoticeTypeCode">CAN-DESG</cbc:NoticeTypeCode>
  <cac:PreviousDocumentReference>
    <cbc:ID>PWD/2026/0530</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ContractNotice</cbc:DocumentTypeCode>
  </cac:PreviousDocumentReference>
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
    <cac:AwardingTerms>
      <cac:Prize>
        <cbc:RankCode listID="urn:ubl-examples:world:codelist:PrizeRankCode">FIRST</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">6000.00</cbc:ValueAmount>
        <cbc:Description>For the design the jury ranks first; its author is invited to negotiate the follow-up service contract.</cbc:Description>
      </cac:Prize>
      <cac:Prize>
        <cbc:RankCode listID="urn:ubl-examples:world:codelist:PrizeRankCode">SECOND</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">4000.00</cbc:ValueAmount>
        <cbc:Description>For the design the jury ranks second.</cbc:Description>
      </cac:Prize>
    </cac:AwardingTerms>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:NegotiationDescription>The service contract for the detailed design and the supervision of the production is negotiated with the first-prize winner, without a new call for competition, on fees, timetable and the number of prototypes.</cbc:NegotiationDescription>
    <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">DESIGNCONTEST</cbc:ProcedureCode>
    <cbc:CandidateReductionConstraintIndicator>true</cbc:CandidateReductionConstraintIndicator>
    <cac:EconomicOperatorShortList>
      <cbc:LimitationDescription>Only the winner of the first prize is invited to negotiate the follow-up contract, as the contest notice announced.</cbc:LimitationDescription>
      <cac:PreSelectedParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brackenmere Furniture</cbc:Name>
        </cac:PartyName>
      </cac:PreSelectedParty>
      <cac:PreSelectedParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
      </cac:PreSelectedParty>
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
  <cac:TenderResult>
    <cbc:TenderResultCode listID="urn:ubl-examples:world:codelist:TenderResultCode">AWARDED</cbc:TenderResultCode>
    <cbc:Description>First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.</cbc:Description>
    <cbc:AwardDate>2026-06-26</cbc:AwardDate>
    <cbc:ReceivedTenderQuantity unitCode="EA">4</cbc:ReceivedTenderQuantity>
    <cbc:ReceivedForeignTenderQuantity unitCode="EA">1</cbc:ReceivedForeignTenderQuantity>
    <cac:WinningParty>
      <cbc:Rank>1</cbc:Rank>
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
      </cac:Party>
    </cac:WinningParty>
    <cac:WinningParty>
      <cbc:Rank>1</cbc:Rank>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:WinningParty>
    <cac:WinningParty>
      <cbc:Rank>2</cbc:Rank>
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
