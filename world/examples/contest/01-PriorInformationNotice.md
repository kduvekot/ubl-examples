# Prior Information Notice: Lumeport Public Works Department to Bayvarra Information Service

*Example 1 of the flow "A design contest for the promenade bench (Bayvarra)" · [Prior Information Notice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PRIOR-INFORMATION-NOTICE-SCHEMA)*

The authority announces the relaunched design contest for the promenade bench, with its planned prizes.

[The XML file](01-PriorInformationNotice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:prior-information-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Prior information notice"; the community specification "Public procurement community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **PWD/2026/PROM-DC**  
  The collaboration this document belongs to: the department's design contest for the promenade bench. Lumeport Public Works Department started it and gave it this identifier, which every document of it repeats.
- `ID` = **PWD/2026/0223**  
  The notice number, the same in both versions.
- `UUID` = **9bb74e2c-2e0d-59c8-9355-433e68c3b317**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD/2026/PROM-DC**  
  The department's file number for the contest, the same on every document of it.
- `IssueDate` = **2026-02-02**  
  Published early, so that designers can plan.
- `IssueTime` = **10:07:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **Advance notice of the design contest for the harbour promenade bench.**  
  What it announces.
- `VersionID` = **1**  
  The first version.
- `PlannedDate` = **2026-03-04**  
  When the contest notice is planned.
- `NoticeTypeCode` = **PIN** (listID `urn:ubl-examples:world:codelist:NoticeTypeCode`)  
  A prior information notice. The code is from the Trade Accord's notice type list: PIN = Prior information notice.

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

- `AwardingTerms/Description` = **The jury ranks the designs anonymously, on design quality (40 %), durability and maintenance in salt air (30 %) and the cost of production (30 %).**  
  How the designs are judged.
- `AwardingTerms/TechnicalCommitteeDescription` = **A jury of five: the head of parks, the city architect, a representative of the disability council and two independent designers.**  
  Who judges.
- `AwardingTerms/PrizeIndicator` = **true**  
  A design contest with prizes.
- `AwardingTerms/PrizeDescription` = **Three prizes; the first is 6,000 lume.**  
  The prizes in words; each is given below.
- `AwardingTerms/PaymentDescription` = **Each selected participant that submits a design meeting the brief receives 1,000 lume towards its costs, whether or not it wins a prize.**  
  The payment to all participants, besides the prizes.
- `AwardingTerms/FollowupContractIndicator` = **true**  
  The winner of the first prize is invited to negotiate the service contract for the detailed design and the supervision of the production, without a new call for competition.
- `AwardingTerms/BindingOnBuyerIndicator` = **true**  
  The jury's ranking binds the department.
- `AwardingTerms/Prize/RankCode` = **FIRST** (listID `urn:ubl-examples:world:codelist:PrizeRankCode`)  
  The first prize. The code is from the Trade Accord's prize rank list: FIRST = First prize.
- `AwardingTerms/Prize/ValueAmount` = **6000.00** (currencyID `XBL`)  
  The first prize as first planned.
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
- `EconomicOperatorShortList/LimitationDescription` = **A restricted contest: the jury will select the participants on their references.**  
  How the number of participants will be limited, announced early.
- `EconomicOperatorShortList/MaximumQuantity` = **5**  
  At most five.
- `EconomicOperatorShortList/MinimumQuantity` = **3**  
  At least three participants are planned.

### Tendering Process

Inside `TenderingProcess`:

- `ProcedureCode` = **DESIGNCONTEST** (listID `urn:ubl-examples:world:codelist:ProcurementProcedureCode`)  
  A design contest is planned. The code is from the Trade Accord's procurement procedure list: DESIGNCONTEST = Design contest.

### Procurement Project

Inside `ProcurementProject`:

- `Name` = **Design of the harbour promenade bench**  
  The name of the contest.
- `Description` = **A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.**  
  What the department wants designed.
- `ProcurementTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:ContractNatureCode`)  
  A design is a service. The code is from the Trade Accord's contract nature list: SERVICES = Services.
- `RequestedTenderTotal/EstimatedOverallContractAmount` = **52000.00** (currencyID `XBL`)  
  The prizes, 12,000 lume, and the follow-up service contract, estimated at 40,000 lume.
- `RequestedTenderTotal/MonetaryScope` = **The three prizes (12,000 lume) and the follow-up service contract for the detailed design and the supervision of the production (about 40,000 lume). The production of the benches is not part of it.**  
  What the estimate covers, in words.
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
<PriorInformationNotice xmlns="urn:oasis:names:specification:ubl:schema:xsd:PriorInformationNotice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:prior-information-notice:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PWD/2026/PROM-DC</cbc:ProfileExecutionID>
  <cbc:ID>PWD/2026/0223</cbc:ID>
  <cbc:UUID>9bb74e2c-2e0d-59c8-9355-433e68c3b317</cbc:UUID>
  <cbc:ContractFolderID>PWD/2026/PROM-DC</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-02</cbc:IssueDate>
  <cbc:IssueTime>10:07:00-01:00</cbc:IssueTime>
  <cbc:Note>Advance notice of the design contest for the harbour promenade bench.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:PlannedDate>2026-03-04</cbc:PlannedDate>
  <cbc:NoticeTypeCode listID="urn:ubl-examples:world:codelist:NoticeTypeCode">PIN</cbc:NoticeTypeCode>
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
      <cbc:Description>The jury ranks the designs anonymously, on design quality (40 %), durability and maintenance in salt air (30 %) and the cost of production (30 %).</cbc:Description>
      <cbc:TechnicalCommitteeDescription>A jury of five: the head of parks, the city architect, a representative of the disability council and two independent designers.</cbc:TechnicalCommitteeDescription>
      <cbc:PrizeIndicator>true</cbc:PrizeIndicator>
      <cbc:PrizeDescription>Three prizes; the first is 6,000 lume.</cbc:PrizeDescription>
      <cbc:PaymentDescription>Each selected participant that submits a design meeting the brief receives 1,000 lume towards its costs, whether or not it wins a prize.</cbc:PaymentDescription>
      <cbc:FollowupContractIndicator>true</cbc:FollowupContractIndicator>
      <cbc:BindingOnBuyerIndicator>true</cbc:BindingOnBuyerIndicator>
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
      <cac:Prize>
        <cbc:RankCode listID="urn:ubl-examples:world:codelist:PrizeRankCode">THIRD</cbc:RankCode>
        <cbc:ValueAmount currencyID="XBL">2000.00</cbc:ValueAmount>
        <cbc:Description>For the design the jury ranks third, if the jury finds it of prize standard.</cbc:Description>
      </cac:Prize>
    </cac:AwardingTerms>
    <cac:EconomicOperatorShortList>
      <cbc:LimitationDescription>A restricted contest: the jury will select the participants on their references.</cbc:LimitationDescription>
      <cbc:MaximumQuantity>5</cbc:MaximumQuantity>
      <cbc:MinimumQuantity>3</cbc:MinimumQuantity>
    </cac:EconomicOperatorShortList>
  </cac:TenderingTerms>
  <cac:TenderingProcess>
    <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:ProcurementProcedureCode">DESIGNCONTEST</cbc:ProcedureCode>
  </cac:TenderingProcess>
  <cac:ProcurementProject>
    <cbc:Name>Design of the harbour promenade bench</cbc:Name>
    <cbc:Description>A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.</cbc:Description>
    <cbc:ProcurementTypeCode listID="urn:ubl-examples:world:codelist:ContractNatureCode">SERVICES</cbc:ProcurementTypeCode>
    <cac:RequestedTenderTotal>
      <cbc:EstimatedOverallContractAmount currencyID="XBL">52000.00</cbc:EstimatedOverallContractAmount>
      <cbc:MonetaryScope>The three prizes (12,000 lume) and the follow-up service contract for the detailed design and the supervision of the production (about 40,000 lume). The production of the benches is not part of it.</cbc:MonetaryScope>
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
</PriorInformationNotice>
```
