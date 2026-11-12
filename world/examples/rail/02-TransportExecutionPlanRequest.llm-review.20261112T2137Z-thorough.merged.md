# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/02-TransportExecutionPlanRequest.xml`, Git blob `52257b380a8d27db0a94e9c2db9b3ccb9b645ca6` (committed)
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

### rail/02#F1 · High · Main service "Full truck load" for a container train service
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Full truck load`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription` = `192 park benches in two 40-foot containers.`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`
- Why: MainTransportationService is "A description of the main transportation service referenced in the Transport Execution Plan Request". In the world's TransportServiceCode list FTL is "One truck for one consignment, from the place of loading to the place of delivery". The request goes to a rail carrier, for a consignment in two 40-foot containers (one tractor does not carry two 40-foot containers), whose main carriage passes the rail border station and is delivered to Lumeway in Bayvarra; no truck goes from the place of loading to the place of delivery. The truck run in the Note ("Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub") is only the leg to the hub. The plan answering the request is carried by container train (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`), and the itinerary for that plan says RAILCONT, "Containers on a scheduled container train" (`09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`). Merge check: the list texts confirmed in `world/codelists/lists.json`; the contradiction with the request's own border waypoint and container count stands without the other examples.
- Condition: the main transportation service code and name describe the rail main carriage; the road leg, if requested, is an additional service or a pre-carriage stage.
- Options: (a) preferred: MainTransportationService RAILCONT, the road leg as a `cac:PreCarriageShipmentStage` (mode 3) or as AdditionalTransportationService (the list's CARRHAUL is defined for carriage "to or from the port arranged by the shipping line", so its text would need widening for a rail hub); (b) RAILWAGON if a whole wagon is meant; (c) restrict the request to the truck run and request the rail service separately (changes the flow).
- Needs decision: no
- From: broad (F3), context (F2), logistics (F1, first part)

### rail/02#F2 · High · Requested pickup lies before the period in which the service must begin
- XPath: `/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: ServiceStartTimePeriod is "The period within which the services referred to in the Transport Execution Plan Request must begin". The pickup at Castrano on 13 April 15:00, the first act of the requested service (the carrier's tractor collecting the boxes, as the Note says), is a day before that period opens. Merge check (refutation attempted): the pickup is a requested event of the same consignment and the haulage is part of the service the note describes, so it cannot be read as outside the service; the waybill confirms the pickup on 13 April (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cbc:ActualPickupDate` = `2026-04-13`).
- Condition: the requested pickup (and every other requested event of the service) lies within or after ServiceStartTimePeriod.
- Options: (a) preferred: start ServiceStartTimePeriod on 2026-04-13; (b) move the pickup to 14 April (hardly possible with a departure at 07:00 that morning); (c) request the road haulage separately.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F2)

### rail/02#F3 · High · ToLocation is the hub, but the consignment is to be delivered in Bayvarra
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`
- Why: ToLocation is "The destination location for the transport service referenced in the Transport Execution Plan Request". The same request asks for a main carriage across the border (waypoint at the rail border station, arrival on 15 April) and a delivery to the consignee Lumeway in Marrowdale on 16 April. The hub in Ferrano is only where the road leg ends and the rail carriage begins. The header thus describes the truck run (both locations in Ferrano), the consignment the rail transport to Bayvarra; the road leg has no pre-carriage stage of its own. The plan repeats this (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`).
- Condition: ToLocation is the place where the requested service ends (the Lumeway siding in Marrowdale), and From/To describe the same transport as the consignment's stages; or the request covers only the leg its From/To describe and carries no main carriage and delivery to Bayvarra.
- Options: (a) preferred: ToLocation = Lumeway's rail siding in Marrowdale (with GLN 9520610900015 as in the waybill), the hub becoming a stage location, and a `cac:PreCarriageShipmentStage` for the road leg; (b) split into two requests (road haulage; rail), which changes the flow.
- Needs decision: no
- From: broad (F2), context (F3), logistics (F1, second part)

### rail/02#F4 · Medium · Province in Region of four Urvanian addresses
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division, which UBL puts in CountrySubentity ("…such as the name of its county, province, or state"), as the consignee's Bayvarran address in the same document does (`/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) preferred: move it to CountrySubentity; (b) drop it where postal zone and city locate the address; (c) keep Region only if the world defines provinces as non-administrative regions, and record it.
- Needs decision: no
- From: broad (F4), context (F5), logistics (F4), parties (F1)

### rail/02#F5 · Medium · Language code in LocaleCode of the consignee
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` (listID ISO 639) is a language code and repeats `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`; it names no locale. 364 occurrences (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, recounted in the merge).
- Condition: LocaleCode is absent or a locale (language plus region) from a list of locales.
- Options: (a) preferred: drop it (nothing in the request depends on the locale); (b) `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no
- From: broad (F5), context (F4), parties (F2)

### rail/02#F6 · Medium · Gate in AdditionalStreetName of the consignee's postal address
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". "Gate 3" is a vehicle entrance, not a street name; in a transport request it could matter at a delivery place, but the goods go by rail to Lumeway's siding (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`), not through a road gate.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) preferred: remove it from the postal address; (b) state access details at a delivery location of the consignment if a road delivery needs them.
- Needs decision: no
- From: broad (F6), parties (F3)

### rail/02#F7 · Medium · Main carriage stage without mode, its requested departure and arrival without places
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: A transport request has to say what transport is asked for. The stage has no TransportModeCode (the plan answering it has `2`, rail), and the requested departure and arrival have no location, so the request does not say where the 07:00 departure and the arrival on 15 April are wanted; with the header pointing to the hub (F3) neither can be inferred. Merge check: confirmed, the stage holds only the three requested events.
- Condition: the main carriage stage carries its transport mode, and its requested departure and arrival name their places (by name and UN/LOCODE or GLN, as the waybill does for the same places).
- Options: (a) preferred: TransportModeCode 2 and `cac:Location` on both events (Ferrano Intermodal Hub / XUFER; Lumeway siding / XBMRW); (b) LoadingPortLocation/UnloadingPortLocation on the stage.
- Needs decision: no
- From: logistics (F3)

### rail/02#F8 · Low · DocumentStatusCode "NoStatus" states only that there is no status
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "A code signifying the status of the Transport Execution Plan Request"; NoStatus means "No status on document". The element states the absence of a status, which the absence of the element already says (no fillers, nothing implied by absence: IND5/IND6). Broad refuted this: a first version has no status and the code says so explicitly; harmless. The merge does not follow that refutation, in line with the wood and plastics merges, which treat NoStatus as a Low finding.
- Condition: DocumentStatusCode is absent, or carries a status the request actually has.
- Options: (a) preferred: drop it; (b) a real status if the story gives one.
- Needs decision: no
- From: merge (broad listed it under "Considered and refuted")

### rail/02#F9 · Low · "English" renderings of Urvanian street names and legal forms are Italian
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via del Terminal`
- Why: Each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings next to them are different names (e.g. `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`). Broad refuted the street name as the world's convention of Italian-styled English names for Urvanian places; that may hold for street names but not obviously for a legal form, and the merge cannot settle it. 217 such renderings in 102 files (`grep -rh --include='*.xml' -E 'languageID="en-X[UB]">(Via|Viale|Piazza|Valico|Corso|Largo|Strada|Banchina) ' world/examples | wc -l`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) preferred: record the convention in the world's story and keep the values, if intended (the legal form is the stronger case for English); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F4); broad listed the street name under "Considered and refuted"

### rail/02#F10 · Low · Legal-entity master data the transport request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: data copied from master data into a document that does not use it. A request for rail transport does nothing with the transport user's stock-exchange listing or with the share capital of the transport user or the consignee.
- Condition: every legal-entity element present has a purpose in the transport request.
- Options: (a) preferred: drop SecurityListing and CorporateStockAmount here; (b) a reduced party description for transport documents.
- Needs decision: no
- From: context (F6), parties (F8)

### rail/02#F11 · Low · Contacts do not fit the transport roles
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara sends the request as transport user and asks the carrier to "confirm by return"; that confirmation and questions about collection go to its shipping or logistics function, not to the order desk that takes customer orders. A consignee's contact receives goods; the plan makes the consignee unload (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`), so the carrier needs Lumeway's goods-in or siding contact, not its sales customer service. The carrier's own contact fits its role (`/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Freight desk`).
- Condition: the sender's contact is a shipping/logistics function of Valdara; the consignee's contact is Lumeway's goods-receiving function; names, job titles and departments agree.
- Options: (a) preferred: role-specific contacts; (b) drop Contact where the party's one master contact does not fit.
- Needs decision: no
- From: broad (F9), parties (F5, F6)

### rail/02#F12 · Low · Registration date 1996-01-01 of the carrier
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: A company's registration date on New Year's Day, a public holiday on which registers are closed, reads as a placeholder rather than the date of a real registration (own knowledge of register practice). The same date occurs 271 times in 181 files (`grep -rh --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, and `-l` for files), for many different companies, which the wood, plastics and air merges raised as a finding; a register's start date or a general re-registration in 1996 would explain it only if the story says so. No part of this run raised it for rail 01–05; the merge adds it for consistency with those merges and with the rail 06–11 merge.
- Condition: each company has its own registration date, or the story records an event (e.g. a re-registration of all companies in 1996) that explains the shared date.
- Options: (a) preferred: an own date per company from its history; (b) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: merge

### rail/02#F13 · Low · Contract number differs from the carrier's contract for the same consignment
- XPath: `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`
- Why: The request names the framework contract `VI-FRC-FW-2026`; the consignment's contract in the plan and the waybill is `FRC-CON-2026-005` (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`, `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`), described as "Framework contract for container slots", and the plan links VI-FRC-FW-2026 to the contract document FRC-CON-2026-005-A1. A reader cannot tell whether one or two contracts exist (see rail/03 F9).
- Condition: the same contract carries the same identifier in the flow, or the documents show how the two identifiers relate.
- Options: (a) preferred: one identifier (the carrier's, as on the waybill); (b) if Valdara has its own number, give both and say which is whose.
- Needs decision: no
- From: broad (F7); logistics refuted the reference as broken and pointed to rail/03

### rail/02#F14 · Low · From location named after the company, not the place
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- Why: A Location's Name is "The name of this location"; here it is the name of the company operating the warehouse. The waybill names the same place `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`, so the place has two names in the flow, and no identifier links them. The ToLocation "Ferrano Intermodal Hub" is the terminal's name and doubles as the operator's name; acceptable for a terminal (parties), but it too has no identifier.
- Condition: the from location's name names the warehouse as a place, in the same words as the other examples of the flow.
- Options: (a) preferred: "Castrano Logistics warehouse, Ferrano", as on the waybill; (b) add a location identifier (GLN) used wherever the warehouse and the terminal occur.
- Needs decision: no
- From: broad (F8), logistics (F5), parties (F7)

## Checked and consistent
- No document references; consignment `VI-CS-26-0327`, 192 benches, gross 7968 kg, two 40-foot containers, containerised: identical in 03, and the weight in 06 (broad, logistics). 7968 / 192 = 41.5 kg per bench; 3984 kg per 40-foot container, far below payload (broad, logistics; redone).
- Response deadline 2026-04-08 lies after the issue (2026-04-07 10:32) and is met by the plan issued 2026-04-08 16:46 (broad, context, logistics).
- Requested delivery 2026-04-16 = plan's contractual latest delivery date and the waybill's latest delivery date; requested arrival 2026-04-15 = plan's planned arrival (logistics).
- Requested main carriage: departure 14 April 07:00, waypoint on 14 April, arrival 15 April, delivery 16 April, service end 17 April: in order (broad).
- Roles: Valdara sender, transport user, bill-to party and consignor; Ferrano Rail Cargo receiver and provider; Lumeway consignee; the same in 03; the freight invoice 10 is addressed to Valdara, matching BillToParty under DAP (01) (broad, context, parties).
- Valdara, Ferrano Rail Cargo and Lumeway described identically in every rail example carrying their full description (broad, parties).
- ToLocation address = the hub's postal address in 04 (Via del Terminal 59, 4180 Ferrano) (parties).
- ServiceProviderParty Castrano Logistics in the sender is used: the FromLocation is Castrano's warehouse (context; see refuted).
- ContainerizedIndicator true with the summary "two 40-foot containers" (context).
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass; prefix 952 is GS1's demonstration range, XU a user-assigned code (logistics, parties).

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: master data copied into the request — refuted because Castrano Logistics, Valdara's warehousing and despatch provider, is where the carrier collects the goods (`/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`) (broad, parties).
- `/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.`: suspected filler — refuted because asking the provider to confirm is the normal remark of a transport user, and the plan answers it (context).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`: waypoint without location, or location without identifier — refuted: it has a location, its name is a place name, and no other example of the flow identifies the border station with a code (context, parties).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent`: pickup event without location — refuted because the pickup point is unambiguously the FromLocation (the Castrano warehouse), and the plan, waybill and itinerary agree (logistics).
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription` = `192 park benches in two 40-foot containers.`: a request that might not say what is to be carried — refuted: summary, weight and containerised indicator say what is carried and in what equipment (logistics).
- `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`: does not resolve to an example — refuted as a broken reference: it names a framework contract, not a document of the flow (logistics; the double identification is F13).
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: an international rail freight operator as a small enterprise — refuted because nothing in the flow states staff, turnover or fleet that contradicts it (parties).
- Not followed by the merge (made findings): broad's refutations of `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus` (F8) and of `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine` (F9).

## Changed in the merge
- logistics/F1 → F1 and F3: split into the service code (F1) and the From/To locations (F3), because they are different elements with different fixes; logistics' Needs decision yes changed to no, because the preferred option is an encoding change and only option (b) would change the flow.
- context/F2 → F1: Medium raised to High (broad, logistics): FTL contradicts values of the same request (two 40-foot containers, rail border waypoint, delivery in Bayvarra).
- context/F3 → F3: Medium raised to High (broad): the hub as destination contradicts the requested main carriage and delivery in the same document.
- broad/F4, context/F5, logistics/F4 → F4: Needs decision yes changed to no (parties): the value says "Province"; moving it is encoding; aligned with the earlier merges.
- broad/F5, context/F4, parties/F2 → F5: preferred option "drop" (parties) instead of `en-XB`; count recounted (364).
- broad/F9, parties/F5, parties/F6 → F11: combined into one contact finding with one line per place.
- broad/F8, logistics/F5, parties/F7 → F14: combined.
- context/F6, parties/F8 → F10: combined.
- F8 (NoStatus) and F12 (registration date): added by the merge for consistency with the wood, plastics, air and rail 06–11 merges; F8 overrides broad's refutation.
