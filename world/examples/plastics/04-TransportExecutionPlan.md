# Transport Execution Plan: Fiumella Barges to Rinova Recovery

*Example 4 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Transport Execution Plan in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORT-EXECUTION-PLAN-SCHEMA)*

The barge operator confirms the vessel and the sailing.

[The XML file](04-TransportExecutionPlan.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:transport-execution-plan:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Transport execution plan". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **PLASTICS-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FB-TEP-26-0886**  
  The carrier's number for the agreed plan.
- `VersionID` = **1**  
  The first version of the plan.
- `UUID` = **32791589-65d7-5d36-bda8-9b68dad29bdd**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-15**  
  The barge operator confirms the sailing.
- `IssueTime` = **13:10:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `DocumentStatusCode` = **Confirmed** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  The carrier confirms the plan as requested. A value of UBL's document status code list (2.1: Document has been confirmed). The code is from the world's copy of UBL's Document status list, with a listID: Confirmed = Document has been confirmed.
- `DocumentStatusReasonCode` = **ASREQUESTED** (listID `urn:ubl-examples:world:codelist:DocumentStatusReasonCode`)  
  Confirmed without changes. The code is from the Trade Accord's document status reason list: ASREQUESTED = As requested.
- `DocumentStatusReasonDescription` = **Capacity available on the requested day.**  
  Why it is confirmed.
- `Note` = **Drek bikrek mir drek nir nan krir drek balman halkan zir drek gakzaz krir drek zulskir nerzhek.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): The transport agreed.
- `Note` = **The barge from the quay next to the recovery plant down the river to the packaging maker.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: The transport agreed.
- `TransportUserRemarks` = **Please confirm by return.**  
  The user's remark from the request.
- `TransportServiceProviderRemarks` = **Collection as requested; notice two hours before arrival.**  
  The carrier's remark.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Fiumella Barges**  
  The trading name; identity of Fiumella Barges (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160204198475331** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Fiumella Barges (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Skikzek Han Nestan** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Fiumella Barges (world/parties.json).
- `PostalAddress/StreetName` = **Banchina del Fiume** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Fiumella Barges (world/parties.json).
- `PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits). identity of Fiumella Barges (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Fiumella Barges (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Chartering desk**  
  The party's main desk, which handles this document; identity of Fiumella Barges (world/parties.json).
- `Contact/JobTitle` = **Chartering manager**  
  The job of the person who answers at the desk; identity of Fiumella Barges (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Fiumella Barges (world/parties.json).
- `Contact/Telephone` = **+999 1 041 513 4959**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Fiumella Barges (world/parties.json).
- `Contact/ElectronicMail` = **chartering@fiumella.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Fiumella Barges (world/parties.json).
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Fiumella Barges (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Fiumella Barges (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); identity of Rinova Recovery (world/parties.json).
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; identity of Rinova Recovery (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Rinova Recovery (world/parties.json).
- `Contact/Telephone` = **+999 1 041 836 4548**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Rinova Recovery (world/parties.json).
- `Contact/ElectronicMail` = **logistics@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rinova Recovery (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport User Party

Inside `TransportUserParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rinova Recovery**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Transport Service Provider Party

Inside `TransportServiceProviderParty`:

- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Fiumella Barges**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Bill To Party

Inside `BillToParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FB-SIG-882**  
  The carrier's seal on the plan.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Fiumella Barges**  
  A party referred to from another party's details: its identifier and name are enough.

### Transport Execution Plan Request Document Reference

Inside `TransportExecutionPlanRequestDocumentReference`:

- `ID` = **RR-TR-26-0884**  
  The request this plan answers.

### Transport Contract

Inside `TransportContract`:

- `ID` = **RR-FB-FW-2026**  
  The framework agreement.
- `ContractType` = **Framework transport agreement**  
  Its kind.

### Transport Service Provider Response Required Period

Inside `TransportServiceProviderResponseRequiredPeriod`:

- `EndDate` = **2026-04-15**  
  The carrier answered the same day.

### Transport User Response Required Period

Inside `TransportUserResponseRequiredPeriod`:

- `EndDate` = **2026-04-16**  
  The user may object until the next day.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-15**  
  From the confirmation.
- `EndDate` = **2026-04-22**  
  Until the carriage is done.

### Main Transportation Service

Inside `MainTransportationService`:

- `TransportServiceCode` = **RIVERBARGE** (listID `urn:ubl-examples:world:codelist:TransportServiceCode`)  
  The main service, by the carrier's main leg (river) and what it carries. The code is from the Trade Accord's transport service list: RIVERBARGE = River barge.
- `Name` = **River barge**  
  In words.

### Additional Transportation Service

Inside `AdditionalTransportationService`:

- `TransportServiceCode` = **NOTIFY** (listID `urn:ubl-examples:world:codelist:TransportServiceCode`)  
  Pre-arrival notice. The code is from the Trade Accord's transport service list: NOTIFY = Pre-arrival notice.
- `Name` = **Notice two hours before arrival**  
  In words.

### Service Start Time Period

Inside `ServiceStartTimePeriod`:

- `StartDate` = **2026-04-19**  
  Collection, as requested.

### Service End Time Period

Inside `ServiceEndTimePeriod`:

- `EndDate` = **2026-04-22**  
  Delivered within three days.

### From Location

Inside `FromLocation`:

- `ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Name` = **Quay of Rinova Recovery, Ferrano**  
  Where the goods are taken over.
- `Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### To Location

Inside `ToLocation`:

- `Name` = **River quay of Rivermouth Packaging, Lumeport**  
  Where the goods are handed over.

### Transport Execution Terms

Inside `TransportExecutionTerms`:

- `TransportUserSpecialTerms` = **Delivery within the agreed slot; the consignee unloads.**  
  The user's terms.
- `TransportServiceProviderSpecialTerms` = **Waiting time beyond two hours is charged.**  
  The carrier's.
- `ChangeConditions` = **Changes up to 24 hours before collection without charge.**  
  When the plan may change.
- `PaymentTerms/Note` = **30 days net from the consignment note.**  
  When the freight is paid: the term the carrier's invoices under this plan apply (D22).
- `PenaltyPaymentTerms/Note` = **For late delivery the carrier is liable for 5 % of the freight per day late, at most 25 %.**  
  The carrier's liability for delay, in words: PenaltySurchargePercent is a surcharge for late payment, not for late delivery (worklist C19).
- `NotificationRequirement/NotificationTypeCode` = **PREARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportNotificationTypeCode`)  
  Notice before arrival. The code is from the Trade Accord's transport notification type list: PREARRIVAL = Pre-arrival notice.
- `NotificationRequirement/PreEventNotificationDurationMeasure` = **2** (unitCode `HUR`)  
  Two hours before.
- `NotificationRequirement/NotifyParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `NotificationRequirement/NotifyParty/PartyName/Name` = **Rivermouth Packaging**  
  A party referred to from another party's details: its identifier and name are enough.
- `NotificationRequirement/NotificationLocation/Name` = **River quay of Rivermouth Packaging, Lumeport**  
  The place the notice is for: where the goods arrive.
- `ServiceChargePaymentTerms/Note` = **Waiting time 4,000 ferra per hour beyond two hours.**  
  The service charge, in the carrier's currency, at the rate of its framework terms.

### Consignment

Inside `Consignment`:

- `ID` = **RR-CS-26-0885**  
  The seller's consignment number.
- `SummaryDescription` = **120 t of Recycled PE granulate**  
  What is to be carried, in a few words (worklist C21).
- `GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The weight the plan is made for.
- `TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  The number of goods items.
- `ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **0990:20274** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Telephone` = **+999 2 38 2440 2740**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/ElectronicMail` = **goodsin@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `MainCarriageShipmentStage/ID` = **1**  
  Down the river, from the recovery plant's quay to the river quay in Lumeport.
- `MainCarriageShipmentStage/TransportModeCode` = **8** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 8: inland water transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 8 = Inland water transport.
- `MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `MainCarriageShipmentStage/TransportMeans/DirectionCode` = **DS** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: DS = Downstream.
- `MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **815** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: fiumella IV; the fleet of Fiumella Barges (world/parties.json). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 815 = Freight barge.
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XU-IW-08042** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Fiumella IV**  
  The vessel's name; the fleet of Fiumella Barges (world/parties.json).
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QUBF4**  
  The radio call sign, in Urvania's call sign series QU: no ITU series starts with Q, so the sign belongs to no real station (world/countries.json).
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **297801042**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 297 of Urvania, which the ITU has not allocated to any real country, and the ship's six digits.
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **1210** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **860** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **DRYBARGE** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel. The code is from the Trade Accord's ship configuration list: DRYBARGE = Dry cargo barge.
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Ferrano**  
  The port the vessel is registered in.
- `MainCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `MainCarriageShipmentStage/LoadingPortLocation/Name` = **Quay of Rinova Recovery, Ferrano**  
  Where the bags are loaded.
- `MainCarriageShipmentStage/UnloadingPortLocation/Name` = **River quay, Lumeport**  
  The place named in the CPT terms.
- `MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceDate` = **2026-04-19**  
  Loading finished: 120 bags in the hold.
- `MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceTime` = **13:30:00**  
  The local time.
- `MainCarriageShipmentStage/LoadingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/LoadingTransportEvent/Location/Name` = **Quay of Rinova Recovery, Ferrano**  
  At the recovery plant's own quay on the river.
- `MainCarriageShipmentStage/LoadingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceDate` = **2026-04-20**  
  The barge leaves Urvania at the river border, 105 km below the quay: sailing from the afternoon of loading and through the next day from first light.
- `MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceTime` = **13:45:00**  
  The local time.
- `MainCarriageShipmentStage/ExportationTransportEvent/Location/Name` = **River border Urvania–Bayvarra**  
  Where the barge leaves Urvania.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-04-22**  
  Planned unloading at the Lumeport quay, with the consignee's morning shift: the barge arrives about 16:15 the day before and moors at the quay overnight.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **08:00:00**  
  The local time.
- `MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/Name` = **River quay, Lumeport**  
  The quay named in the CPT terms, where the bags are unloaded.
- `MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceDate` = **2026-04-19**  
  The barge operator takes over the bags at the quay.
- `MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceTime` = **09:00:00**  
  The local time.
- `MainCarriageShipmentStage/TakeoverTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/TakeoverTransportEvent/Location/Name` = **Quay of Rinova Recovery, Ferrano**  
  At the recovery plant's own quay on the river.
- `MainCarriageShipmentStage/TakeoverTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/EstimatedTransitPeriod/DurationMeasure` = **3** (unitCode `DAY`)  
  Three days from takeover to discharge: about 250 km downstream, with no locks, sailing by day.
- `MainCarriageShipmentStage/MasterPerson/FirstName` = **Tomaso**  
  The skipper of the barge.
- `MainCarriageShipmentStage/MasterPerson/FamilyName` = **Riverra**  
  The family name.
- `MainCarriageShipmentStage/MasterPerson/JobTitle` = **Skipper**  
  The person's position.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportExecutionPlan xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportExecutionPlan-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:transport-execution-plan:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PLASTICS-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FB-TEP-26-0886</cbc:ID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:UUID>32791589-65d7-5d36-bda8-9b68dad29bdd</cbc:UUID>
  <cbc:IssueDate>2026-04-15</cbc:IssueDate>
  <cbc:IssueTime>13:10:00-01:00</cbc:IssueTime>
  <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">Confirmed</cbc:DocumentStatusCode>
  <cbc:DocumentStatusReasonCode listID="urn:ubl-examples:world:codelist:DocumentStatusReasonCode">ASREQUESTED</cbc:DocumentStatusReasonCode>
  <cbc:DocumentStatusReasonDescription>Capacity available on the requested day.</cbc:DocumentStatusReasonDescription>
  <cbc:Note languageID="qau">Drek bikrek mir drek nir nan krir drek balman halkan zir drek gakzaz krir drek zulskir nerzhek.</cbc:Note>
  <cbc:Note languageID="en-XU">The barge from the quay next to the recovery plant down the river to the packaging maker.</cbc:Note>
  <cbc:TransportUserRemarks>Please confirm by return.</cbc:TransportUserRemarks>
  <cbc:TransportServiceProviderRemarks>Collection as requested; notice two hours before arrival.</cbc:TransportServiceProviderRemarks>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160204198475331</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Skikzek Han Nestan</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Banchina del Fiume</cbc:StreetName>
      <cbc:BuildingNumber>52</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4170</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Chartering desk</cbc:Name>
      <cbc:JobTitle>Chartering manager</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 041 513 4959</cbc:Telephone>
      <cbc:ElectronicMail>chartering@fiumella.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104959</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202983340277</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 836 4548</cbc:Telephone>
      <cbc:ElectronicMail>logistics@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:TransportUserParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:TransportUserParty>
  <cac:TransportServiceProviderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
  </cac:TransportServiceProviderParty>
  <cac:BillToParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:BillToParty>
  <cac:Signature>
    <cbc:ID>FB-SIG-882</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Fiumella Barges</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:TransportExecutionPlanRequestDocumentReference>
    <cbc:ID>RR-TR-26-0884</cbc:ID>
  </cac:TransportExecutionPlanRequestDocumentReference>
  <cac:TransportContract>
    <cbc:ID>RR-FB-FW-2026</cbc:ID>
    <cbc:ContractType>Framework transport agreement</cbc:ContractType>
  </cac:TransportContract>
  <cac:TransportServiceProviderResponseRequiredPeriod>
    <cbc:EndDate>2026-04-15</cbc:EndDate>
  </cac:TransportServiceProviderResponseRequiredPeriod>
  <cac:TransportUserResponseRequiredPeriod>
    <cbc:EndDate>2026-04-16</cbc:EndDate>
  </cac:TransportUserResponseRequiredPeriod>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-15</cbc:StartDate>
    <cbc:EndDate>2026-04-22</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:MainTransportationService>
    <cbc:TransportServiceCode listID="urn:ubl-examples:world:codelist:TransportServiceCode">RIVERBARGE</cbc:TransportServiceCode>
    <cbc:Name>River barge</cbc:Name>
  </cac:MainTransportationService>
  <cac:AdditionalTransportationService>
    <cbc:TransportServiceCode listID="urn:ubl-examples:world:codelist:TransportServiceCode">NOTIFY</cbc:TransportServiceCode>
    <cbc:Name>Notice two hours before arrival</cbc:Name>
  </cac:AdditionalTransportationService>
  <cac:ServiceStartTimePeriod>
    <cbc:StartDate>2026-04-19</cbc:StartDate>
  </cac:ServiceStartTimePeriod>
  <cac:ServiceEndTimePeriod>
    <cbc:EndDate>2026-04-22</cbc:EndDate>
  </cac:ServiceEndTimePeriod>
  <cac:FromLocation>
    <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
    <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:FromLocation>
  <cac:ToLocation>
    <cbc:Name>River quay of Rivermouth Packaging, Lumeport</cbc:Name>
  </cac:ToLocation>
  <cac:TransportExecutionTerms>
    <cbc:TransportUserSpecialTerms>Delivery within the agreed slot; the consignee unloads.</cbc:TransportUserSpecialTerms>
    <cbc:TransportServiceProviderSpecialTerms>Waiting time beyond two hours is charged.</cbc:TransportServiceProviderSpecialTerms>
    <cbc:ChangeConditions>Changes up to 24 hours before collection without charge.</cbc:ChangeConditions>
    <cac:PaymentTerms>
      <cbc:Note>30 days net from the consignment note.</cbc:Note>
    </cac:PaymentTerms>
    <cac:PenaltyPaymentTerms>
      <cbc:Note>For late delivery the carrier is liable for 5 % of the freight per day late, at most 25 %.</cbc:Note>
    </cac:PenaltyPaymentTerms>
    <cac:NotificationRequirement>
      <cbc:NotificationTypeCode listID="urn:ubl-examples:world:codelist:TransportNotificationTypeCode">PREARRIVAL</cbc:NotificationTypeCode>
      <cbc:PreEventNotificationDurationMeasure unitCode="HUR">2</cbc:PreEventNotificationDurationMeasure>
      <cac:NotifyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Rivermouth Packaging</cbc:Name>
        </cac:PartyName>
      </cac:NotifyParty>
      <cac:NotificationLocation>
        <cbc:Name>River quay of Rivermouth Packaging, Lumeport</cbc:Name>
      </cac:NotificationLocation>
    </cac:NotificationRequirement>
    <cac:ServiceChargePaymentTerms>
      <cbc:Note>Waiting time 4,000 ferra per hour beyond two hours.</cbc:Note>
    </cac:ServiceChargePaymentTerms>
  </cac:TransportExecutionTerms>
  <cac:Consignment>
    <cbc:ID>RR-CS-26-0885</cbc:ID>
    <cbc:SummaryDescription>120 t of Recycled PE granulate</cbc:SummaryDescription>
    <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
    <cac:ConsigneeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:20274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-411619</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Estuary Road</cbc:StreetName>
        <cbc:BuildingNumber>28</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38505</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 2 38 2440 2740</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@rivermouth.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
    </cac:ConsigneeParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">8</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
        <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">DS</cbc:DirectionCode>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">815</cbc:TransportMeansTypeCode>
        <cac:MaritimeTransport>
          <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XU-IW-08042</cbc:VesselID>
          <cbc:VesselName>Fiumella IV</cbc:VesselName>
          <cbc:RadioCallSignID>QUBF4</cbc:RadioCallSignID>
          <cbc:MMSIRegistrationID>297801042</cbc:MMSIRegistrationID>
          <cbc:GrossTonnageMeasure unitCode="C62">1210</cbc:GrossTonnageMeasure>
          <cbc:NetTonnageMeasure unitCode="C62">860</cbc:NetTonnageMeasure>
          <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">DRYBARGE</cbc:ShipConfigurationCode>
          <cac:RegistryPortLocation>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano</cbc:Name>
          </cac:RegistryPortLocation>
        </cac:MaritimeTransport>
      </cac:TransportMeans>
      <cac:LoadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
      </cac:LoadingPortLocation>
      <cac:UnloadingPortLocation>
        <cbc:Name>River quay, Lumeport</cbc:Name>
      </cac:UnloadingPortLocation>
      <cac:LoadingTransportEvent>
        <cbc:OccurrenceDate>2026-04-19</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>13:30:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:LoadingTransportEvent>
      <cac:ExportationTransportEvent>
        <cbc:OccurrenceDate>2026-04-20</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>13:45:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:Name>River border Urvania–Bayvarra</cbc:Name>
        </cac:Location>
      </cac:ExportationTransportEvent>
      <cac:DischargeTransportEvent>
        <cbc:OccurrenceDate>2026-04-22</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>08:00:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:Name>River quay, Lumeport</cbc:Name>
        </cac:Location>
      </cac:DischargeTransportEvent>
      <cac:TakeoverTransportEvent>
        <cbc:OccurrenceDate>2026-04-19</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>09:00:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:TakeoverTransportEvent>
      <cac:EstimatedTransitPeriod>
        <cbc:DurationMeasure unitCode="DAY">3</cbc:DurationMeasure>
      </cac:EstimatedTransitPeriod>
      <cac:MasterPerson>
        <cbc:FirstName>Tomaso</cbc:FirstName>
        <cbc:FamilyName>Riverra</cbc:FamilyName>
        <cbc:JobTitle>Skipper</cbc:JobTitle>
      </cac:MasterPerson>
    </cac:MainCarriageShipmentStage>
  </cac:Consignment>
</TransportExecutionPlan>
```
