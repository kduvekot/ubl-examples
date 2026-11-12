# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/02-TransportExecutionPlanRequest.xml`, Git blob `52257b380a8d27db0a94e9c2db9b3ccb9b645ca6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0cafa9c 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### rail/02#F1 · High · Requested pickup lies before the service may begin
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- XPath: `/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- Why: ServiceStartTimePeriod is "The period within which the services referred to in the Transport Execution Plan Request must begin". The requested pickup of the consignment, the first act of the service (the carrier's tractor collecting the boxes at Castrano, as the Note says), is on 13 April, a day before that period starts.
- Condition: The requested pickup lies within (or after the start of) ServiceStartTimePeriod.
- Options: (a) preferred: start ServiceStartTimePeriod on 2026-04-13, since the carrier haulage is part of the requested service; (b) move the pickup to 14 April if the boxes are collected that morning (then the departure at 07:00 constrains it).
- Needs decision: no

### rail/02#F2 · High · ToLocation is the hub, but the consignment is to be delivered in Bayvarra
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`
- Why: ToLocation is "The destination location for the transport service referenced in the Transport Execution Plan Request". The request asks for a main carriage across the border (waypoint at the border station, arrival on 15 April) and a delivery to the consignee Lumeway in Marrowdale on 16 April. The hub in Ferrano is only the end of the carrier haulage leg, so the request names an intermediate point as the destination of the whole service. The plan repeats this (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`).
- Condition: ToLocation is the place where the requested service ends (the Lumeway siding in Marrowdale), or the request covers only the haulage to the hub and then contains no main carriage and delivery to Bayvarra.
- Options: (a) preferred: ToLocation = Lumeway's rail siding in Marrowdale (with its GLN 9520610900015 as used in the waybill), the hub becoming a stage location; (b) split into two requests (carrier haulage; rail).
- Needs decision: no

### rail/02#F3 · High · Main service "Full truck load" for a rail transport
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Full truck load`
- Why: In the world's TransportServiceCode list FTL is "One truck for one consignment, from the place of loading to the place of delivery". The request is sent to a rail carrier for a consignment in two 40-foot containers that crosses the border at the rail border station (see F2); the truck part is only the carrier haulage to the hub, for which the same list has CARRHAUL. Two 40-foot containers are not one truck load either. The list has RAILCONT "Containers on a scheduled container train", which the itinerary uses for the same plan (`09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`).
- Condition: The main transportation service code and name describe the rail main carriage; the haulage, if expressed, is an additional service.
- Options: (a) preferred: MainTransportationService RAILCONT, with CARRHAUL as AdditionalTransportationService; (b) RAILWAGON if the world means a whole wagon.
- Needs decision: no

### rail/02#F4 · Medium · Province given in Region
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division, which UBL puts in CountrySubentity ("such as the name of its county, province, or state"), as the Bayvarran address in the same document does with "Upland State". 219 occurrences over the examples (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: An administrative province of Urvania is in CountrySubentity; Region only for a non-administrative region.
- Options: (a) preferred: CountrySubentity; (b) keep Region only if the world defines provinces as non-administrative regions.
- Needs decision: yes (a fact of the world)

### rail/02#F5 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` repeats the language, it is not a locale (the flow's texts use `en-XB`/`en-XU`). 362 occurrences over the examples.
- Condition: LocaleCode absent or a locale such as `en-XB` with a matching listID.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/02#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is an access point for vehicles, not a street, and the delivery here is to a rail siding, not by road through a gate.
- Condition: AdditionalStreetName holds a street name or is absent.
- Options: (a) preferred: drop it from the postal address; (b) put access details in the delivery location if a road delivery needs them.
- Needs decision: no

### rail/02#F7 · Low · Contract number differs from the carrier's contract for the same consignment
- XPath: `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`
- Why: The request names the framework contract `VI-FRC-FW-2026`; the plan and the waybill name the contract for this consignment `FRC-CON-2026-005` (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`, `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`), described as "Framework contract for container slots". Both read as the same framework contract, so a reader cannot tell whether one or two contracts exist.
- Condition: The same contract carries the same identifier in the flow, or the documents show how the two contracts relate.
- Options: (a) preferred: use one identifier (the carrier's, as on the waybill); (b) if Valdara has its own number, give both and say which is whose.
- Needs decision: no

### rail/02#F8 · Low · FromLocation named after the company
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- Why: A Location's Name is "The name of this location"; here it is the name of the company operating the warehouse. The waybill names the same place "Castrano Logistics warehouse, Ferrano" (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`).
- Condition: The location is named as a place, consistently across the flow.
- Options: (a) preferred: "Castrano Logistics warehouse, Ferrano", as on the waybill; (b) add a location identifier (GLN or UN/LOCODE with a place).
- Needs decision: no

### rail/02#F9 · Low · Contacts do not fit the transport roles
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The transport user's contact for a transport request is the one who books and answers about transport (shipping, logistics); the consignee's contact is the one who receives the goods at the siding. Both are sales desks that serve customers.
- Condition: The sender's contact is a shipping/logistics function of Valdara; the consignee's contact is goods receiving at Lumeway.
- Options: (a) preferred: role-specific contacts; (b) accept the parties' one master contact and drop Contact where it does not fit.
- Needs decision: no

## Checked and consistent
- References: no document references; the consignment `VI-CS-26-0327`, its weight 7968 kg and description "192 park benches in two 40-foot containers" are the same in 03, 06 and 08.
- Response deadline 2026-04-08 is met by the plan issued 2026-04-08 16:46 (03).
- Parties: Valdara (sender, transport user, bill-to, consignor), Ferrano Rail Cargo (receiver, provider) and Lumeway (consignee) are described as in the other rail examples (compared element by element over all eleven XML files). BillToParty Valdara agrees with DAP (01) and with the freight invoice (10).
- Requested main carriage: departure 14 April 07:00, waypoint at the border on 14 April, arrival 15 April, delivery 16 April, service end 17 April: in order.
- Physics: 7968 kg gross for 192 benches = 41.5 kg per bench with packaging; 3984 kg per 40-foot container, far below payload.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`: suspected master data copied into a document that does not use it — refuted because the goods are collected at Castrano's warehouse (FromLocation), so the transport request has a reason to show who Valdara's warehousing provider is.
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: suspected a rendering not in the language `en-XU` names — refuted because the world uses Italian-styled names as the established English names of Urvanian places.
- `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`: suspected a filler — refuted because a first version of a request has no status and the code says so explicitly; harmless.
