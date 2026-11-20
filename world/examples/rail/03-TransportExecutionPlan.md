# Transport Execution Plan: Ferrano Rail Cargo to Valdara Industries

*Example 3 of the flow "Containers by rail under the Accord's common transit (Urvania → Bayvarra)" · [Transport Execution Plan in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORT-EXECUTION-PLAN-SCHEMA)*

The rail carrier confirms the haulage to the hub and the slots on the container train to the distributor's siding.

[The XML file](03-TransportExecutionPlan.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:transport-execution-plan:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Transport execution plan". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900043586**  
  The collaboration this document belongs to: the rail carriage Valdara books with Ferrano Rail Cargo. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **9500055446**  
  The carrier's number for the agreed plan.
- `VersionID` = **1**  
  The first version of the plan.
- `UUID` = **eb749a49-fd81-59f8-9c7a-8cb356fa55f1**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-08**  
  The rail carrier confirms the slots on the container train.
- `IssueTime` = **16:46:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `DocumentStatusCode` = **Confirmed** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  The carrier confirms the plan as requested. A value of UBL's document status code list (2.1: Document has been confirmed). The code is from the world's copy of UBL's Document status list, with a listID: Confirmed = Document has been confirmed.
- `DocumentStatusReasonCode` = **ASREQUESTED** (listID `urn:ubl-examples:world:codelist:DocumentStatusReasonCode`)  
  Confirmed without changes. The code is from the Trade Accord's document status reason list: ASREQUESTED = As requested.
- `DocumentStatusReasonDescription` = **Capacity available in the requested window: slots on the train of 14 April.**  
  Why it is confirmed as requested.
- `Note` = **Kan trunskir mir drek mazmul trek Conciaro krir drek kaz nintrek trek Marrowdale: drek vuznek kazdrek krir drek gul, vabul drek titran sezhul.** (languageID `qau`)  
  The note in Urvanian, the sender's language: The transport asked for and agreed.
- `Note` = **Two containers from the warehouse in Conciaro to the rail siding in Marrowdale: the carrier's tractor to the hub, then the container train.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: The transport asked for and agreed.
- `TransportUserRemarks` = **Please confirm by return.**  
  The user's remark from the request.
- `TransportServiceProviderRemarks` = **Collection as requested; notice two hours before arrival.**  
  The carrier's remark.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Rail Cargo gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; as Ferrano Rail Cargo gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4170201115930918** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Rail Cargo gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Rumir Hekrul Zhuzkek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Rail Cargo gives it.
- `PostalAddress/StreetName` = **Viale della Stazione** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Rail Cargo gives it.
- `PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. As Ferrano Rail Cargo gives it.
- `PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Rail Cargo gives it.
- `PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Rail Cargo gives it.
- `PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). As Ferrano Rail Cargo gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Rail Cargo gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Freight desk**  
  The party's main desk, which handles this document; as Ferrano Rail Cargo gives it.
- `Contact/JobTitle` = **Freight planner**  
  The job of the person who answers at the desk; as Ferrano Rail Cargo gives it.
- `Contact/Department` = **Operations**  
  The department the desk belongs to; as Ferrano Rail Cargo gives it.
- `Contact/Telephone` = **+999 1 0413 67100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Rail Cargo gives it.
- `Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Ferrano Rail Cargo gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Ferrano Rail Cargo gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Rail Cargo gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); as Valdara Industries gives it.
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **logistics@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport User Party

Inside `TransportUserParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Transport Service Provider Party

Inside `TransportServiceProviderParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Bill To Party

Inside `BillToParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FRC-SIG-325**  
  The carrier's seal on the plan.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

### Transport Execution Plan Request Document Reference

Inside `TransportExecutionPlanRequestDocumentReference`:

- `ID` = **7000026152**  
  The request this plan answers.

### Transport Contract

Inside `TransportContract`:

- `ID` = **FRC-CON-2026-005**  
  The framework contract for container slots, in the carrier's numbering, the same in every document.
- `IssueDate` = **2026-01-05**  
  Signed at the start of the year: the time below has its date.
- `IssueTime` = **10:00:00-01:00**  
  Signed in the morning; in the local time of Urvania, where it happens, with its offset from UTC.
- `NominationDate` = **2026-04-08**  
  The deadline for booking this train's slots: the request of the day before met it.
- `NominationTime` = **09:00:00-01:00**  
  At that time; in the local time of Urvania, where it happens, with its offset from UTC.
- `ContractTypeCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractTypeCode`)  
  A framework contract. The code is from the Trade Accord's contract type list: FRAMEWORK = Framework agreement.
- `ContractType` = **Framework contract for container slots**  
  Its kind, as the consignment note names it.
- `Note` = **Call-off 88 of the year.**  
  Which call-off.
- `VersionID` = **2**  
  The contract as amended in March.
- `ModificationReasonCode` = **VOLUME** (listID `urn:ubl-examples:world:codelist:ContractModificationReasonCode`)  
  Amended for higher volumes. The code is from the Trade Accord's contract modification reason list: VOLUME = Volume change.
- `ModificationReasonDescription` = **Ten more slots a month from April.**  
  The change.
- `Description` = **Container slots on the trains from the Ferrano hub to Marrowdale, with the carrier's haulage of the boxes to the hub.**  
  What it covers.
- `ContractDocumentReference/ID` = **FRC-CON-2026-005-A1**  
  The amendment.
- `NominationPeriod/StartDate` = **2026-04-06**  
  Slots are booked from a week before the train
- `NominationPeriod/EndDate` = **2026-04-08**  
  until the deadline above, so period and deadline agree.
- `NominationPeriod/EndTime` = **09:00:00-01:00**  
  The deadline's time; in the issuer's local time, with its offset from UTC.
- `ContractualDelivery/LatestDeliveryDate` = **2026-04-16**  
  The contract's latest delivery for this call-off.

### Transport Service Provider Response Required Period

Inside `TransportServiceProviderResponseRequiredPeriod`:

- `EndDate` = **2026-04-08**  
  The carrier answered the same day.

### Transport User Response Required Period

Inside `TransportUserResponseRequiredPeriod`:

- `EndDate` = **2026-04-09**  
  The user may object until the next day.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-08**  
  From the confirmation.
- `EndDate` = **2026-04-16**  
  Until the carriage is done.

### Main Transportation Service

Inside `MainTransportationService`:

- `TransportServiceCode` = **RAILCONT** (listID `urn:ubl-examples:world:codelist:TransportServiceCode`)  
  The main service, by the carrier's main leg (rail) and what it carries. The code is from the Trade Accord's transport service list: RAILCONT = Container train.
- `Name` = **Container train**  
  In words.

### Service Start Time Period

Inside `ServiceStartTimePeriod`:

- `StartDate` = **2026-04-13**  
  Collection, as requested.

### Service End Time Period

Inside `ServiceEndTimePeriod`:

- `EndDate` = **2026-04-16**  
  Delivered within three days.

### From Location

Inside `FromLocation`:

- `ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Name` = **Castrano Logistics warehouse, Conciaro**  
  Where the carrier takes the packed boxes over.
- `Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### To Location

Inside `ToLocation`:

- `ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Name` = **Lumeway rail siding, Marrowdale**  
  Where the service ends: the boxes are placed on Lumeway's siding.

### Transport Execution Terms

Inside `TransportExecutionTerms`:

- `TransportServiceProviderSpecialTerms` = **Delivery within the agreed slot; the consignee unloads. Waiting time beyond two hours is charged.**  
  The carrier's terms.
- `ChangeConditions` = **Changes up to 24 hours before collection without charge.**  
  When the plan may change.
- `PaymentTerms/Note` = **30 days net from the consignment note.**  
  When the freight is paid: the term the carrier's invoices under this plan apply.
- `PenaltyPaymentTerms/Note` = **For late delivery the carrier is liable for 5 % of the freight per day late, at most 25 %.**  
  The carrier's liability for delay, in words: PenaltySurchargePercent is a surcharge for late payment, not for late delivery.
- `NotificationRequirement/NotificationTypeCode` = **PREARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportNotificationTypeCode`)  
  Notice before arrival. The code is from the Trade Accord's transport notification type list: PREARRIVAL = Pre-arrival notice.
- `NotificationRequirement/PreEventNotificationDurationMeasure` = **2** (unitCode `HUR`)  
  Two hours before.
- `NotificationRequirement/NotifyParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `NotificationRequirement/NotifyParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `NotificationRequirement/NotificationLocation/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `NotificationRequirement/NotificationLocation/Name` = **Lumeway rail siding, Marrowdale**  
  The place the notice is for: where the goods arrive.
- `ServiceChargePaymentTerms/Note` = **Waiting time 4,000 ferra per hour beyond two hours.**  
  The service charge, in the carrier's currency, at the rate of its framework terms.

### Consignment

Inside `Consignment`:

- `ID` = **7300043586**  
  The manufacturer's consignment number.
- `SummaryDescription` = **192 park benches in two 40-foot containers.**  
  The goods in a few words.
- `GrossWeightMeasure` = **10377.6** (unitCode `KGM`)  
  The weight the plan is made for.
- `ContainerizedIndicator` = **true**  
  Two full containers.
- `PlannedPickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  The carrier collects the packed boxes, in two runs.
- `PlannedPickupTransportEvent/OccurrenceTime` = **13:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `PlannedPickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PlannedPickupTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `PlannedPickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PlannedDeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  And places them at the siding.
- `PlannedDeliveryTransportEvent/OccurrenceTime` = **11:00:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `PlannedDeliveryTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `PlannedDeliveryTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `ConsigneeParty/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Lumeway Distribution gives it.
- `ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `ConsigneeParty/Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `ConsigneeParty/Contact/ElectronicMail` = **goodsin@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `PrepaidPaymentTerms/Note` = **Freight prepaid by the consignor under DAP.**  
  The seller pays the carriage.
- `MainCarriageShipmentStage/ID` = **2**  
  The main carriage, by rail.
- `MainCarriageShipmentStage/TransportModeCode` = **2** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 2: rail transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 2 = Rail transport.
- `MainCarriageShipmentStage/LoadingSequenceID` = **7**  
  The order the boxes go on the train: these two are the seventh lift.
- `MainCarriageShipmentStage/SuccessiveSequenceID` = **1**  
  The first and only rail stage.
- `MainCarriageShipmentStage/Instructions` = **Shunt to the Lumeway siding in Marrowdale once the import is declared.**  
  What the railway must do.
- `MainCarriageShipmentStage/DemurrageInstructions` = **Free time five days at the siding, counted from the day after the boxes are placed; then demurrage of 7,500 ferra per container day, under framework contract FRC-CON-2026-005.**  
  What waiting costs: the framework contract's free time and rate.
- `MainCarriageShipmentStage/CrewQuantity` = **2** (unitCode `IE`)  
  Two persons: a driver and a train manager.
- `MainCarriageShipmentStage/TransportMeans/JourneyID` = **CT 4471**  
  The number of the container train in the hub's timetable.
- `MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `MainCarriageShipmentStage/TransportMeans/DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **2302** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container train Ferrano–Marrowdale; the fleet of Ferrano Rail Cargo. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 2302 = Train, container.
- `MainCarriageShipmentStage/TransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train number; the fleet of Ferrano Rail Cargo.
- `MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The timetable departure from the hub.
- `MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **06:45:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The timetable arrival at the siding in Marrowdale: the train reaches Marrowdale yard about 15:10 the day before, 173 km from the hub, and the next morning's shunting trip places the boxes on Lumeway's siding.
- `MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **10:30:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceDate` = **2026-04-14**  
  Planned departure from the border station, 63 km from the hub: the train stops there from about 08:00 for the crew change, the brake test and the customs' check of the seals, and leaves on its timetabled path into Bayvarra.
- `MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceTime` = **13:00:00-01:00**  
  The issuer's local time, with its offset from UTC.
- `MainCarriageShipmentStage/PlannedWaypointTransportEvent/Location/Name` = **Rail border station Urvania–Bayvarra**  
  Where the train crosses the border.
- `MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The departure as expected that morning.
- `MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceTime` = **06:50:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The arrival as expected.
- `MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceTime` = **10:40:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/EstimatedArrivalTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `MainCarriageShipmentStage/EstimatedArrivalTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `PreCarriageShipmentStage/ID` = **1**  
  The pre-carriage: the carrier's tractor brings the packed boxes to the hub.
- `PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **37** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container tractor for carrier haulage; the fleet of Ferrano Rail Cargo. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 37 = Truck, container.
- `PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 RC** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Ferrano Rail Cargo. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `PreCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/LoadingPortLocation/Name` = **Castrano Logistics warehouse, Conciaro**  
  Where the boxes are collected.
- `PreCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/UnloadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/UnloadingPortLocation/Name` = **Ferrano Intermodal Hub**  
  Where they are handed to the terminal.
- `PreCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-04-13**  
  The first run leaves the warehouse.
- `PreCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **13:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `PreCarriageShipmentStage/PlannedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `PreCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-04-13**  
  The second box at the hub: 46 km each way, two runs.
- `PreCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **15:50:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `PreCarriageShipmentStage/PlannedArrivalTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `PreCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportExecutionPlan xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportExecutionPlan-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:transport-execution-plan:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900043586</cbc:ProfileExecutionID>
  <cbc:ID>9500055446</cbc:ID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:UUID>eb749a49-fd81-59f8-9c7a-8cb356fa55f1</cbc:UUID>
  <cbc:IssueDate>2026-04-08</cbc:IssueDate>
  <cbc:IssueTime>16:46:00-01:00</cbc:IssueTime>
  <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">Confirmed</cbc:DocumentStatusCode>
  <cbc:DocumentStatusReasonCode listID="urn:ubl-examples:world:codelist:DocumentStatusReasonCode">ASREQUESTED</cbc:DocumentStatusReasonCode>
  <cbc:DocumentStatusReasonDescription>Capacity available in the requested window: slots on the train of 14 April.</cbc:DocumentStatusReasonDescription>
  <cbc:Note languageID="qau">Kan trunskir mir drek mazmul trek Conciaro krir drek kaz nintrek trek Marrowdale: drek vuznek kazdrek krir drek gul, vabul drek titran sezhul.</cbc:Note>
  <cbc:Note languageID="en-XU">Two containers from the warehouse in Conciaro to the rail siding in Marrowdale: the carrier's tractor to the hub, then the container train.</cbc:Note>
  <cbc:TransportUserRemarks>Please confirm by return.</cbc:TransportUserRemarks>
  <cbc:TransportServiceProviderRemarks>Collection as requested; notice two hours before arrival.</cbc:TransportServiceProviderRemarks>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4170201115930918</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Rumir Hekrul Zhuzkek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Viale della Stazione</cbc:StreetName>
      <cbc:BuildingNumber>38</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
      <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
      <cbc:PostalZone>4310</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Freight desk</cbc:Name>
      <cbc:JobTitle>Freight planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 0413 67100</cbc:Telephone>
      <cbc:ElectronicMail>freight@ferranorail.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104685</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
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
      <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
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
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>logistics@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:TransportUserParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:TransportUserParty>
  <cac:TransportServiceProviderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
  </cac:TransportServiceProviderParty>
  <cac:BillToParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:BillToParty>
  <cac:Signature>
    <cbc:ID>FRC-SIG-325</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:TransportExecutionPlanRequestDocumentReference>
    <cbc:ID>7000026152</cbc:ID>
  </cac:TransportExecutionPlanRequestDocumentReference>
  <cac:TransportContract>
    <cbc:ID>FRC-CON-2026-005</cbc:ID>
    <cbc:IssueDate>2026-01-05</cbc:IssueDate>
    <cbc:IssueTime>10:00:00-01:00</cbc:IssueTime>
    <cbc:NominationDate>2026-04-08</cbc:NominationDate>
    <cbc:NominationTime>09:00:00-01:00</cbc:NominationTime>
    <cbc:ContractTypeCode listID="urn:ubl-examples:world:codelist:ContractTypeCode">FRAMEWORK</cbc:ContractTypeCode>
    <cbc:ContractType>Framework contract for container slots</cbc:ContractType>
    <cbc:Note>Call-off 88 of the year.</cbc:Note>
    <cbc:VersionID>2</cbc:VersionID>
    <cbc:ModificationReasonCode listID="urn:ubl-examples:world:codelist:ContractModificationReasonCode">VOLUME</cbc:ModificationReasonCode>
    <cbc:ModificationReasonDescription>Ten more slots a month from April.</cbc:ModificationReasonDescription>
    <cbc:Description>Container slots on the trains from the Ferrano hub to Marrowdale, with the carrier's haulage of the boxes to the hub.</cbc:Description>
    <cac:ContractDocumentReference>
      <cbc:ID>FRC-CON-2026-005-A1</cbc:ID>
    </cac:ContractDocumentReference>
    <cac:NominationPeriod>
      <cbc:StartDate>2026-04-06</cbc:StartDate>
      <cbc:EndDate>2026-04-08</cbc:EndDate>
      <cbc:EndTime>09:00:00-01:00</cbc:EndTime>
    </cac:NominationPeriod>
    <cac:ContractualDelivery>
      <cbc:LatestDeliveryDate>2026-04-16</cbc:LatestDeliveryDate>
    </cac:ContractualDelivery>
  </cac:TransportContract>
  <cac:TransportServiceProviderResponseRequiredPeriod>
    <cbc:EndDate>2026-04-08</cbc:EndDate>
  </cac:TransportServiceProviderResponseRequiredPeriod>
  <cac:TransportUserResponseRequiredPeriod>
    <cbc:EndDate>2026-04-09</cbc:EndDate>
  </cac:TransportUserResponseRequiredPeriod>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-08</cbc:StartDate>
    <cbc:EndDate>2026-04-16</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:MainTransportationService>
    <cbc:TransportServiceCode listID="urn:ubl-examples:world:codelist:TransportServiceCode">RAILCONT</cbc:TransportServiceCode>
    <cbc:Name>Container train</cbc:Name>
  </cac:MainTransportationService>
  <cac:ServiceStartTimePeriod>
    <cbc:StartDate>2026-04-13</cbc:StartDate>
  </cac:ServiceStartTimePeriod>
  <cac:ServiceEndTimePeriod>
    <cbc:EndDate>2026-04-16</cbc:EndDate>
  </cac:ServiceEndTimePeriod>
  <cac:FromLocation>
    <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
    <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:FromLocation>
  <cac:ToLocation>
    <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
    <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
  </cac:ToLocation>
  <cac:TransportExecutionTerms>
    <cbc:TransportServiceProviderSpecialTerms>Delivery within the agreed slot; the consignee unloads. Waiting time beyond two hours is charged.</cbc:TransportServiceProviderSpecialTerms>
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
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:NotifyParty>
      <cac:NotificationLocation>
        <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
        <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
      </cac:NotificationLocation>
    </cac:NotificationRequirement>
    <cac:ServiceChargePaymentTerms>
      <cbc:Note>Waiting time 4,000 ferra per hour beyond two hours.</cbc:Note>
    </cac:ServiceChargePaymentTerms>
  </cac:TransportExecutionTerms>
  <cac:Consignment>
    <cbc:ID>7300043586</cbc:ID>
    <cbc:SummaryDescription>192 park benches in two 40-foot containers.</cbc:SummaryDescription>
    <cbc:GrossWeightMeasure unitCode="KGM">10377.6</cbc:GrossWeightMeasure>
    <cbc:ContainerizedIndicator>true</cbc:ContainerizedIndicator>
    <cac:PlannedPickupTransportEvent>
      <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
      <cbc:OccurrenceTime>13:00:00-01:00</cbc:OccurrenceTime>
      <cac:Location>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
    </cac:PlannedPickupTransportEvent>
    <cac:PlannedDeliveryTransportEvent>
      <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
      <cbc:OccurrenceTime>11:00:00-01:00</cbc:OccurrenceTime>
      <cac:Location>
        <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
        <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
      </cac:Location>
    </cac:PlannedDeliveryTransportEvent>
    <cac:ConsigneeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Distribution Drive</cbc:StreetName>
        <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
        <cbc:BuildingNumber>43</cbc:BuildingNumber>
        <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71214</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
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
        <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
    </cac:ConsigneeParty>
    <cac:PrepaidPaymentTerms>
      <cbc:Note>Freight prepaid by the consignor under DAP.</cbc:Note>
    </cac:PrepaidPaymentTerms>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>2</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">2</cbc:TransportModeCode>
      <cbc:LoadingSequenceID>7</cbc:LoadingSequenceID>
      <cbc:SuccessiveSequenceID>1</cbc:SuccessiveSequenceID>
      <cbc:Instructions>Shunt to the Lumeway siding in Marrowdale once the import is declared.</cbc:Instructions>
      <cbc:DemurrageInstructions>Free time five days at the siding, counted from the day after the boxes are placed; then demurrage of 7,500 ferra per container day, under framework contract FRC-CON-2026-005.</cbc:DemurrageInstructions>
      <cbc:CrewQuantity unitCode="IE">2</cbc:CrewQuantity>
      <cac:TransportMeans>
        <cbc:JourneyID>CT 4471</cbc:JourneyID>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
        <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">2302</cbc:TransportMeansTypeCode>
        <cac:RailTransport>
          <cbc:TrainID>FRC 4417</cbc:TrainID>
        </cac:RailTransport>
      </cac:TransportMeans>
      <cac:PlannedDepartureTransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>06:45:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:PlannedDepartureTransportEvent>
      <cac:PlannedArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>10:30:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
          <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
        </cac:Location>
      </cac:PlannedArrivalTransportEvent>
      <cac:PlannedWaypointTransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>13:00:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:Name>Rail border station Urvania–Bayvarra</cbc:Name>
        </cac:Location>
      </cac:PlannedWaypointTransportEvent>
      <cac:EstimatedDepartureTransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>06:50:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:EstimatedDepartureTransportEvent>
      <cac:EstimatedArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>10:40:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
          <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
        </cac:Location>
      </cac:EstimatedArrivalTransportEvent>
    </cac:MainCarriageShipmentStage>
    <cac:PreCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">37</cbc:TransportMeansTypeCode>
        <cac:RoadTransport>
          <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 RC</cbc:LicensePlateID>
        </cac:RoadTransport>
      </cac:TransportMeans>
      <cac:LoadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:LoadingPortLocation>
      <cac:UnloadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:UnloadingPortLocation>
      <cac:PlannedDepartureTransportEvent>
        <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>13:00:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:PlannedDepartureTransportEvent>
      <cac:PlannedArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>15:50:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:PlannedArrivalTransportEvent>
    </cac:PreCarriageShipmentStage>
  </cac:Consignment>
</TransportExecutionPlan>
```
