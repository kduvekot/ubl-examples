# LLM review: 05-TransportProgressStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/05-TransportProgressStatus.xml`, Git blob `973a4b0e2c9db9dec81b3d925185e8a004dcb691` (committed)
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

### rail/05#F1 · Medium · Sender is a terminal operator, not a transportation network manager
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatus/cac:SenderParty/cbc:IndustryClassificationCode` = `5221`
- XPath: `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- Why: UBL defines the document as "A document sent from a Transportation Network Manager to a Transport Service Provider giving the status of the whereabouts and schedule of the transport means involved in a transport service." The sender and issuer is the intermodal terminal (ISIC 5221; terminal operator in `07-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`). It reports, besides the departure from its own tracks, the train's schedule to the next day (`/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`, the date of arrival in Marrowdale in `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`) — information the manager of the rail network has, not a terminal (own knowledge of rail operations).
- Condition: sender and source issuer are a party that manages the transportation network the train runs on, or the document carries only what its sender can know and the deviation from the definition is recorded.
- Options: (a) a rail infrastructure manager of the world as sender (preferred; matches the definition and the schedule reported); (b) keep the hub and restrict the content to the terminal's own events; (c) report the terminal's events in a Transportation Status instead.
- Needs decision: yes

### rail/05#F2 · Medium · Province in Region of both parties' addresses
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"); the flow's Bayvarran addresses do so (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/05#F3 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/05#F4 · Low · Source issuer repeats the sender
- XPath: `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyIdentification/cbc:ID` = `XU-R-105096`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PartyIdentification/cbc:ID` = `XU-R-105096`
- Why: Transport Progress Status. Source Issuer_ Party is "The Party who issues the Transport Progress Status." Next to SenderParty it has a reason where the status comes from a party other than the one transmitting it (a network manager's system relayed by a service). Here both are the hub, so the element adds nothing (section 4.8).
- Condition: SourceIssuerParty is absent, or names a party other than the sender that issued the status.
- Options: (a) drop it (preferred); (b) if F1 is resolved with a network manager whose status the hub relays, the network manager as source issuer and the hub as sender.
- Needs decision: no

### rail/05#F5 · Low · Status location is the company name, without identifier
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, and identifiers are given where the same place is identified elsewhere. The location is named only with the operator's name, while the plan gives the terminal an address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:BuildingNumber` = `59`) and the waybill identifies Ferrano with a UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`).
- Condition: the status location identifies the terminal the same way the other examples of the flow do.
- Options: (a) a location identifier for the terminal used in every example (preferred); (b) at least the plan's address.
- Needs decision: no

### rail/05#F6 · Low · Terminal control reachable only from 08:00, reporting at 06:45 on a 05:30 arrival
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `05:30:00`
- Why: Contact. Note describes "the circumstances under which this contact can be used". The sender's operational contact is said to be reachable on weekdays from 08:00, while the same document, issued at 06:45, reports the train's arrival at 05:30 and its departure before 07:00 at the terminal. A terminal control desk that handles trains at those hours is reachable at those hours.
- Condition: the terminal's contact availability covers the hours in which the flow uses it (or the note is absent).
- Options: (a) operating hours that cover the train times (preferred); (b) drop the note.
- Needs decision: no

## Checked and consistent
- Receiver Ferrano Rail Cargo is the sender of the request answered (`04-TransportProgressStatusRequest.xml`); sender and receiver are swapped against the request; the signatory is the sender.
- The hub's and the carrier's full descriptions are identical to those in `04-TransportProgressStatusRequest.xml` and `07-TransportationStatus.xml`.

## Outside this review
- `/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00` is later than `/TransportProgressStatus/cbc:IssueTime` = `06:45:00`: an actual event after the issue time (outside the parties lens; for the logistics part).
