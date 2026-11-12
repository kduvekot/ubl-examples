# LLM review: 04-TransportProgressStatusRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/04-TransportProgressStatusRequest.xml`, Git blob `1fc0afc119b31bbce07b12c53077e4e7f9cd7e51` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/04#F1 · Medium · Receiver is a terminal operator, not a transportation network manager
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cbc:IndustryClassificationCode` = `5221`
- Why: UBL defines the document as "A document sent from a transport service provider to a transportation network manager requesting a Transport Progress Status", and the Transport Progress Status answering it as giving "the status of the whereabouts and schedule of the transport means". The receiver here is the intermodal terminal (ISIC 5221, service activities incidental to land transportation; terminal operator of the main carriage in `07-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`). A terminal knows whether the train left its tracks, but it does not manage the rail network and cannot give the train's whereabouts and schedule on the way to Marrowdale, which the answer nevertheless does (estimated arrival on 15 April in `05-TransportProgressStatus.xml`). The party that manages the network for a train is the rail infrastructure manager (own knowledge of rail operations).
- Condition: the receiver of the request is a party that manages the transportation network the train runs on (e.g. Urvania's rail infrastructure manager), or the document is replaced by one whose definition fits a terminal's report.
- Options: (a) address the request to a rail infrastructure manager of the world (preferred if the world has one; it fits the definition and the cross-border schedule in the answer); (b) keep the hub but limit the exchange to what a terminal knows and record the deviation from the definition; (c) use Transportation Status from the terminal instead (as in `07-TransportationStatus.xml`).
- Needs decision: yes

### rail/04#F2 · Medium · Province in Region of both parties' addresses
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"); the flow's Bayvarran addresses do so (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/04#F3 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/04#F4 · Low · Status location is the company name, without identifier
- XPath: `/TransportProgressStatusRequest/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, and identifiers are given where the same place is identified elsewhere. The location is named only with the operator's name, while the plan gives the terminal an address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:BuildingNumber` = `59`) and the waybill identifies the loading place with a UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`). The request does not say which station or terminal track the status is asked for in a way a network system could resolve.
- Condition: the status location identifies the terminal (identifier and/or the terminal's name as a place) the same way the other examples of the flow do.
- Options: (a) add a location identifier for the terminal (e.g. a GLN or the UN/LOCODE with a terminal sub-code) and use it in every example (preferred); (b) at least the address used in the plan.
- Needs decision: no

### rail/04#F5 · Low · Terminal control reachable only from 08:00, asked at 06:30 about a 06:45 departure
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/TransportProgressStatusRequest/cbc:IssueTime` = `06:30:00`
- Why: Contact. Note describes "the circumstances under which this contact can be used". The receiver's operational contact, a terminal control desk, is said to be reachable on weekdays from 08:00, yet the request is sent at 06:30 on a Tuesday about a train planned to leave at 06:45 (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`), and the answer comes at 06:45. A terminal that receives trains at 05:30 has a control desk staffed at that time. The same note is on every contact of every party in the flow.
- Condition: the terminal's contact availability covers the hours in which the flow uses it (or the note is absent).
- Options: (a) operating hours of the terminal control that cover the train times (e.g. "Daily 05:00–22:00" or "24 hours") (preferred); (b) drop the note.
- Needs decision: no

## Checked and consistent
- Sender Ferrano Rail Cargo is the transport service provider of the plan (`03-TransportExecutionPlan.xml`), with the same register ID `XU-R-104685`, description and signatory as everywhere in the flow.
- The hub's full description (`XU-R-105096`, address Via del Terminal 59, 4180) is identical in `05-TransportProgressStatus.xml` and `07-TransportationStatus.xml`, and its address matches the ToLocation of `02-TransportExecutionPlanRequest.xml` and `03-TransportExecutionPlan.xml`.
- The signatory is the sender.

## Considered and refuted
- `/TransportProgressStatusRequest/cac:SenderParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`: the carrier's freight desk sends at 06:30 outside its own hours — refuted as a finding of its own: a request can be sent by the carrier's system at any time; the note says when a person answers. Only the terminal's case (F5) contradicts the role.
- `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: a small terminal operator — refuted: plausible for a single intermodal terminal, and nothing in the flow contradicts it.
