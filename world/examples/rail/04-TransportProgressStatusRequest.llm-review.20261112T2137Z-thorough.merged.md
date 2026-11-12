# LLM review: 04-TransportProgressStatusRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/04-TransportProgressStatusRequest.xml`, Git blob `1fc0afc119b31bbce07b12c53077e4e7f9cd7e51` (committed)
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

### rail/04#F1 · Medium · Province in Region of both parties' addresses
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, which UBL puts in CountrySubentity ("…such as the name of its county, province, or state"); the flow's Bayvarran addresses do so (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) preferred: move it to CountrySubentity; (b) drop it; (c) keep Region only with a stated world rule that provinces are not administrative.
- Needs decision: no
- From: broad (F1), context (F1), parties (F2)

### rail/04#F2 · Medium · Receiver is a terminal operator, the document is addressed to a transportation network manager
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cbc:IndustryClassificationCode` = `5221`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- Why: UBL defines the document as "A document sent from a transport service provider to a transportation network manager requesting a Transport Progress Status", and the Transport Progress Status answering it as giving "the status of the whereabouts and schedule of the transport means". The receiver is the intermodal terminal (ISIC 5221; terminal operator of the main carriage in `07-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`). A terminal knows whether the train left its tracks, but it does not manage the rail network and cannot give the train's schedule on the way to Marrowdale, which the answer nevertheless does (`05-TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`). The party that manages the network for a train is the rail infrastructure manager (own knowledge of rail operations). Context rated it Low ("a stretch rather than wrong": a terminal can report departures from its yard); the merge follows parties' Medium, because the receiver's role differs from the one the document type's definition names, and the answer contains data only a network manager has.
- Condition: the receiver is a party that manages the transportation network the train runs on, or the story says the hub reports for the network (and the answer then carries only what the hub can know or relays).
- Options: (a) preferred: address the request to a rail infrastructure manager of the world, if it has one (fits the definition and the cross-border schedule in the answer); (b) keep the hub, state its reporting role in the world, and limit the exchange to what a terminal knows; (c) report the terminal's events in a Transportation Status instead (as in 07).
- Needs decision: yes
- From: parties (F1), context (F3)

### rail/04#F3 · Low · "Has the container train left?" asked before the planned departure
- XPath: `/TransportProgressStatusRequest/cbc:IssueTime` = `06:30:00`
- XPath: `/TransportProgressStatusRequest/cbc:Note[2]` = `Has the container train left?`
- Why: The plan has the train leaving at 06:45 and estimated at 06:50 (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`). Asking at 06:30 whether it has left makes sense only if an early departure were expected; otherwise the natural question is whether it will leave on time. Counter-arguments: broad put it under "Outside this review" as a timeline question; logistics refuted it, since a carrier may ask shortly before departure and the answer is dated later. The merge keeps it Low, because the note and the time in the same document do not fit each other, and links it to rail/05 F1: if the answer is moved after the departure, this request may stay as it is only if its wording asks for the departure status rather than presuming it.
- Condition: the question in the note fits the time of the request (asked after the planned departure, or asking about the expected or actual departure without presuming it).
- Options: (a) preferred: rephrase the note (e.g. "Please report the departure of the container train."); (b) issue the request after 06:45.
- Needs decision: no
- From: context (F2); broad (Outside this review), logistics (Considered and refuted)

### rail/04#F4 · Low · "English" renderings of the street names and legal forms are Italian
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. Whether the world keeps Italianate names as English usage for Urvania (broad's argument in rail/01 and rail/02) cannot be settled by the merge; for the legal forms it is the weaker argument. 217 such renderings in 102 files (count as in rail/01 F10).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) preferred: record the convention in the world's story and keep the values, if intended; (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F3)

### rail/04#F5 · Low · Registration date 1996-01-01 of both companies
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Ferrano Rail Cargo and Ferrano Intermodal Hub, two different companies, share a registration date on New Year's Day, which reads as a placeholder (own knowledge of register practice); the same date occurs 271 times in 181 files (`grep -rh --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`). No part of this run raised it for rail 01–05; the merge adds it for consistency with the wood, plastics, air and rail 06–11 merges.
- Condition: each company has its own registration date, or the story records an event that explains the shared date.
- Options: (a) preferred: an own date per company from its history; (b) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: merge

### rail/04#F6 · Low · Terminal control reachable only from 08:00, asked at 06:30 about a 06:45 departure
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/TransportProgressStatusRequest/cbc:IssueTime` = `06:30:00`
- Why: Contact/Note is "a textual description of the circumstances under which this contact can be used". The hub's terminal control is said to be reachable on weekdays from 08:00, yet it is asked at 06:30 on Tuesday 14 April about a train planned to leave at 06:45 (03), answers at 06:45 (05), and the train arrived at the hub at 05:30 (05). A terminal control that works trains at those hours is reachable then. The same note is on every contact of every party in the flow.
- Condition: the terminal's contact availability covers the hours in which the flow uses it (or the note is absent).
- Options: (a) preferred: operating hours that cover the train times (e.g. "Daily 05:00–22:00" or "Round the clock"); (b) drop the note.
- Needs decision: no
- From: broad (F2), parties (F5)

### rail/04#F7 · Low · The train asked about is identified only by its timetable service
- XPath: `/TransportProgressStatusRequest/cac:TransportMeans/cbc:JourneyID` = `CT 4471`
- Why: TransportMeans here is "the transport means by which the current transport service is effectuated and for which status is requested", but JourneyID is "an identifier for the regular service schedule of this means of transport", which runs on other days too. The train itself is identified elsewhere in the flow (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`). The request works only because its issue date is the departure day. Broad refuted this: a scheduled journey identifies the train for the hub, nothing more is needed. The merge keeps it Low: the condition is cheap to meet and makes the request unambiguous.
- Condition: the request identifies the specific train run, by TrainID or by the journey together with its date.
- Options: (a) preferred: add `cac:RailTransport/cbc:TrainID` = FRC 4417 next to the JourneyID, as the waybill does; (b) refer to the plan FRC-TEP-26-0328 or state the date of the run.
- Needs decision: no
- From: logistics (F1); broad listed it under "Considered and refuted"

### rail/04#F8 · Low · Status location is the company name, without identifier
- XPath: `/TransportProgressStatusRequest/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, and identifiers are given where the same place is identified elsewhere. The location carries only the operator's name, while the plan gives the terminal an address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:BuildingNumber` = `59`) and the waybill identifies the loading place with a UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`). Logistics refuted it: the name is unambiguous in the flow, and no other example identifies the hub as a status location. The merge keeps it Low, aligned with the air merges (status location = company name, Low): XUFER identifies Ferrano, so a code for the place exists in the flow.
- Condition: the status location identifies the terminal as a place (name of the terminal as a place and/or identifier) the same way in every example of the flow.
- Options: (a) preferred: add a location identifier (e.g. UN/LOCODE XUFER, or a GLN for the terminal) and use it in every example; (b) at least the address used in the plan.
- Needs decision: no
- From: parties (F4); logistics listed it under "Considered and refuted"

## Checked and consistent
- The request is answered by 05 (`05-TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportProgressStatusRequestDocumentReference/cbc:ID` = `FRC-DOC-26-0329`), from the receiver back to the sender, about the same journey CT 4471 and status location (broad, context, logistics).
- The journey CT 4471 is the one planned in 03 and carried on the waybill 08 (broad).
- Issue time 06:30 lies before the response at 06:45; status location Ferrano Intermodal Hub is where the train departs (08's actual departure location) (logistics).
- Sender Ferrano Rail Cargo is the transport service provider of 03 with the same register ID `XU-R-104685`; it is the signatory. The hub's full description (`XU-R-105096`, Via del Terminal 59, 4180) is identical in 05 and 07, and its address matches the ToLocation of 02 and 03 (parties, broad).
- 14 April 2026 is a Tuesday (merge, computed).

## Considered and refuted
- `/TransportProgressStatusRequest/cac:SenderParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`: the carrier's freight desk sends at 06:30 outside its own hours — refuted because a request can be sent by the carrier's system at any time; the note says when a person answers (broad, parties).
- `/TransportProgressStatusRequest/cac:Signature/cbc:ID` = `FRC-SIG-TPSR`: suspected filler — refuted because a signature on a request to another company is a legitimate optional element (context).
- `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: a small terminal operator — refuted: plausible for a single intermodal terminal, and nothing in the flow contradicts it (parties).
- Not followed by the merge (kept as findings, with the part's argument): broad's refutation of `/TransportProgressStatusRequest/cac:TransportMeans/cbc:JourneyID` = `CT 4471` as sufficient (F7); logistics' refutations of `/TransportProgressStatusRequest/cbc:Note[2]` = `Has the container train left?` (F3) and of `/TransportProgressStatusRequest/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub` without identifier (F8).

## Changed in the merge
- broad/F1, context/F1 → F1: Needs decision yes changed to no (parties); aligned with the earlier merges.
- context/F3 (Low) → F2: raised to Medium (parties/F1): the receiver does not have the role the document type's definition names.
- broad/F2, parties/F5 → F6: combined.
- broad's "Outside this review" entry on the 06:30 question → part of F3 (context/F2), with broad's and logistics' arguments.
- F5 (registration date): added by the merge for consistency with the earlier merges.
