# LLM review: 05-TransportProgressStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/05-TransportProgressStatus.xml`, Git blob `973a4b0e2c9db9dec81b3d925185e8a004dcb691` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit abfa39e 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### rail/05#F1 · High · Actual departure after the time of the report
- XPath: `/TransportProgressStatus/cbc:IssueTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:ReferenceTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`
- Why: ActualDepartureTransportEvent is "The actual departure from a location". The report, issued on 14 April at 06:45 with the status referring to 06:45, states an actual departure at 06:52 the same day, seven minutes in the future. The waybill records the same actual departure (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`), so the departure time is the flow's fact and the report's time is the one that does not fit. Merge check (refutation attempted): issue date, reference date and event date are all 2026-04-14, and the document gives no time zone difference between them (both times are the hub's), so the event lies after the report.
- Condition: every actual event lies at or before the issue and reference time of the report.
- Options: (a) preferred: issue the report after the departure (e.g. 06:55) and refer the status to that time; (b) at 06:45, report only the estimate (06:50) and no actual departure.
- Needs decision: no
- From: broad (F1, first part), context (F1), logistics (F1, first part); parties noted it under "Outside this review"

### rail/05#F2 · Medium · Sender is a terminal operator, not a transportation network manager
- XPath: `/TransportProgressStatus/cac:SenderParty/cbc:IndustryClassificationCode` = `5221`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- Why: UBL defines the document as "A document sent from a Transportation Network Manager to a Transport Service Provider giving the status of the whereabouts and schedule of the transport means involved in a transport service." The sender and issuer is the intermodal terminal (ISIC 5221; terminal operator in `07-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`). Besides the departure from its own tracks it reports the train's schedule to the next day (`/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`, the arrival in Marrowdale in `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`), which the manager of the rail network has, not a terminal (own knowledge of rail operations). Context rated it Low (the hub can report departures from its yard); the merge follows parties' Medium, as for the request (rail/04 F2).
- Condition: sender and source issuer are a party that manages the transportation network the train runs on, or the story says the hub reports for the network and the document carries only what the hub can know or relays.
- Options: (a) preferred: a rail infrastructure manager of the world as sender (fits the definition and the schedule reported); (b) keep the hub, state its reporting role in the world, and restrict the content to the terminal's own events; (c) report the terminal's events in a Transportation Status instead.
- Needs decision: yes
- From: parties (F1), context (F5)

### rail/05#F3 · Medium · Province in Region of both parties' addresses
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division, which UBL puts in CountrySubentity; the flow's Bayvarran addresses do so (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files.
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) preferred: move it to CountrySubentity; (b) drop it; (c) keep Region only with a stated world rule.
- Needs decision: no
- From: broad (F3), context (F3), parties (F2)

### rail/05#F4 · Medium · Arrival events of Marrowdale under the hub's status location
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `05:30:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: StatusLocation is "The location for which status is reported", and the schedule's events carry no location of their own, so all of them read as events at the hub. The actual arrival (14 April 05:30) is the train's arrival at the hub, but the planned and estimated arrivals (15 April 10:30 and 10:40) are those at Marrowdale, as in the plan (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedArrivalTransportEvent/cbc:OccurrenceTime` = `10:30:00`). Read as written, the train is planned to arrive at the hub a day after it actually did. Logistics rated it High (a contradiction within the schedule); the merge keeps Medium (broad, context): the arrival events are defined as arrivals "at a specified location" and none specifies one, so the problem is that the 15 April values are given under the wrong location rather than two values of the same fact contradicting each other.
- Condition: each event is attributable to its place: the schedule reports only events at its status location, or events at other places carry their own Location or stand in a second TransportSchedule for Marrowdale.
- Options: (a) preferred: a second `cac:TransportSchedule` (SequenceNumeric 2) with StatusLocation Marrowdale (or the Lumeway siding) for the planned and estimated arrival; (b) give the Marrowdale arrival events a Location; (c) drop the 15 April arrivals from the hub schedule.
- Needs decision: no
- From: broad (F2), context (F2), logistics (F2)

### rail/05#F5 · Low · "On time" for a departure seven minutes after the planned time
- XPath: `/TransportProgressStatus/cbc:Note[2]` = `Left on time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:Remarks` = `On time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`
- Why: The planned departure is 06:45, the estimate 06:50 and the actual departure 06:52 (F1): seven minutes after the plan and two after the estimate. Whether seven minutes count as "on time" depends on a punctuality margin the document does not state; without one, the text and the times disagree.
- Condition: the note and remarks agree with the times (state the margin, or say "seven minutes late, within the slot").
- Options: (a) preferred: remarks that agree with the times (e.g. "Left 7 minutes late" or "On time within the 10-minute margin"); (b) move the actual departure within a stated margin.
- Needs decision: no
- From: context (F4), broad (F1, second part), logistics (F1, second part)

### rail/05#F6 · Low · "English" renderings of the street names and legal forms are Italian
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. Whether the world keeps Italianate names as English usage for Urvania (broad's argument in rail/01 and rail/02) cannot be settled by the merge; for the legal forms it is the weaker argument. 217 such renderings in 102 files (count as in rail/01 F10).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) preferred: record the convention in the world's story and keep the values, if intended; (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F3)

### rail/05#F7 · Low · Registration date 1996-01-01 of both companies
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Ferrano Intermodal Hub and Ferrano Rail Cargo, two different companies, share a registration date on New Year's Day, which reads as a placeholder (own knowledge of register practice); the same date occurs 271 times in 181 files (`grep -rh --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`). No part of this run raised it for rail 01–05; the merge adds it for consistency with the wood, plastics, air and rail 06–11 merges.
- Condition: each company has its own registration date, or the story records an event that explains the shared date.
- Options: (a) preferred: an own date per company from its history; (b) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: merge

### rail/05#F8 · Low · Terminal control reachable only from 08:00, reporting a 05:30 arrival at 06:45
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `05:30:00`
- Why: Contact/Note describes "the circumstances under which this contact can be used". The sender's operational contact is said to be reachable on weekdays from 08:00, while the same document, issued at 06:45, reports the train's arrival at 05:30 and its departure before 07:00 at the terminal. A terminal control desk that handles trains at those hours is reachable then.
- Condition: the terminal's contact availability covers the hours in which the flow uses it (or the note is absent).
- Options: (a) preferred: operating hours that cover the train times; (b) drop the note.
- Needs decision: no
- From: broad (F4), parties (F6)

### rail/05#F9 · Low · Source issuer repeats the sender
- XPath: `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyIdentification/cbc:ID` = `XU-R-105096`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyIdentification/cbc:ID` = `XU-R-105096`
- Why: SourceIssuerParty is "The Party who issues the Transport Progress Status." Next to SenderParty it has a reason where the status comes from a party other than the one transmitting it (e.g. a network manager's system relayed by a service). Here both are the hub, so the element adds nothing (section 4.8; no fillers). Broad refuted it: the element states who originates the status, which need not be the sender, and stating it when they coincide is harmless. The merge keeps it Low, because a value that only repeats another one is a filler under the repository's rules.
- Condition: SourceIssuerParty is absent, or names a party other than the sender that issued the status.
- Options: (a) preferred: drop it; (b) if F2 is resolved with a network manager whose status the hub relays, the network manager as source issuer and the hub as sender.
- Needs decision: no
- From: parties (F4); broad listed it under "Considered and refuted"

### rail/05#F10 · Low · Status location is the company name, without identifier
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, and identifiers are given where the same place is identified elsewhere. The location carries only the operator's name, while the plan gives the terminal an address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:BuildingNumber` = `59`) and the waybill identifies Ferrano with a UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`). Aligned with rail/04 F8 and the air merges.
- Condition: the status location identifies the terminal as a place the same way in every example of the flow.
- Options: (a) preferred: a location identifier for the terminal (UN/LOCODE XUFER or a GLN) used in every example; (b) at least the plan's address.
- Needs decision: no
- From: parties (F5)

## Checked and consistent
- Reference: `/TransportProgressStatus/cac:TransportProgressStatusRequestDocumentReference/cbc:ID` = `FRC-DOC-26-0329` resolves to 04 (request from Ferrano Rail Cargo to the hub); this answer goes from the hub back to the carrier, 15 minutes later, about the same journey CT 4471 and status location (broad, context, logistics, parties).
- Planned departure 06:45, estimated 06:50, planned arrival 2026-04-15 10:30 and estimated 10:40 equal the plan (03) and the waybill (08) (broad, context, logistics).
- Order of events at the hub: train arrival 05:30, loading of the containers at 05:40 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `05:40:00`), departure 06:52 (broad, logistics).
- StatusAvailableIndicator true agrees with the schedule reported (broad).
- Receiver Ferrano Rail Cargo is the sender of the request answered; sender and receiver swapped; the signatory is the sender; the hub's and the carrier's descriptions are identical to 04 and 07 (parties).

## Considered and refuted
- `/TransportProgressStatus/cac:TransportSchedule/cbc:ReliabilityPercent` = `95`: meaningless next to actual events — refuted because the reliability applies to the estimates the schedule also carries (arrival in Marrowdale) (broad, context, logistics).
- `/TransportProgressStatus/cac:TransportMeans/cbc:JourneyID` = `CT 4471`: the run identified only by its timetable service — refuted here, the response mirrors the request; raised for the request (rail/04 F7) (logistics).
- Not followed by the merge: broad's refutation of `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub` as a harmless repetition (kept as F9, with broad's argument).

## Changed in the merge
- broad/F1, logistics/F1 → F1 and F5: split into the actual departure after the report (High, with context/F1) and the "on time" wording (Low, with context/F4), because the second depends on an unstated punctuality margin and has a different fix.
- logistics/F2 (High) → F4: lowered to Medium (broad, context), reason in the finding.
- context/F5 (Low) → F2: raised to Medium (parties/F1), as for rail/04 F2.
- broad/F3, context/F3 → F3: Needs decision yes changed to no (parties); aligned with the earlier merges.
- broad/F4, parties/F6 → F8: combined.
- parties' "Outside this review" entry on the 06:52 departure → part of F1.
- F7 (registration date): added by the merge for consistency with the earlier merges.
