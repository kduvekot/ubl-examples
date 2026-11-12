# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/02-TransportExecutionPlanRequest.xml`, Git blob `52257b380a8d27db0a94e9c2db9b3ccb9b645ca6` (committed)
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

### rail/02#F1 · High · The requested service is a truck run to the hub, but the consignment is to go by rail to Marrowdale
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Full truck load`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`
- Why: MainTransportationService is "a description of the main transportation service referenced in the Transport Execution Plan Request", ToLocation "the destination location for the transport service". Here the main service is a full truck load from the Castrano warehouse to the Ferrano hub (both in Ferrano, Urvania), and the note explains it as carrier haulage to the hub. The consignment in the same request, however, has a main carriage that passes the Urvania–Bayvarra rail border station, arrives on 2026-04-15 and is delivered to the consignee Lumeway Distribution (Bayvarra) on 2026-04-16 — far beyond the requested destination. The plan that answers it (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`, train FRC 4417, shunting at Marrowdale) and the itinerary (`09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`) show that the service actually requested is the container train to Marrowdale with the truck leg as pre-carriage. The request thus describes two different services, and the road leg, which is the only one the header describes, has no pre-carriage stage.
- Condition: MainTransportationService, FromLocation and ToLocation describe the same transport as the consignment's main carriage stage and requested delivery; a road leg from the warehouse to the hub, if requested, is a pre-carriage stage (or an additional service) with its own mode.
- Options: (a) preferred: main service the container train (RAILCONT), FromLocation the warehouse or the hub, ToLocation the Lumeway siding in Marrowdale, and a `cac:PreCarriageShipmentStage` with TransportModeCode 3 for the carrier haulage; (b) if the request is really only for the truck run, remove the rail main carriage, the border waypoint and the delivery to the consignee, and make a separate request for the rail service. (a) matches the rest of the flow (plan, waybill, itinerary, freight invoice for container slots).
- Needs decision: yes

### rail/02#F2 · High · Requested pickup lies before the period in which the service must begin
- XPath: `/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: ServiceStartTimePeriod is "the period within which the services referred to in the Transport Execution Plan Request must begin" and starts on 2026-04-14. The pickup requested in the same document, the first act of the service, is on 2026-04-13 at 15:00, a day before the service may begin.
- Condition: The requested pickup (and any other requested event of the service) lies within or after ServiceStartTimePeriod.
- Options: (a) preferred: start ServiceStartTimePeriod on 2026-04-13 (the pickup), which the plan's planned pickup confirms; (b) move the pickup to 2026-04-14 — not possible with a train departing at 07:00 the same morning and the hub handling the boxes the evening before (rail/08).
- Needs decision: no

### rail/02#F3 · Medium · Main carriage stage without mode, and its requested departure and arrival without places
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: A transport request has to say what transport is asked for. The stage has no TransportModeCode (the plan answering it has `2`, rail), and the requested departure and arrival have no location, so the request does not say from where the departure at 07:00 is wanted or where the arrival on 2026-04-15 should be; with the header pointing to the hub (F1) neither can be inferred. The checklist asks for a location where an event would otherwise be meaningless.
- Condition: The main carriage stage carries its transport mode, and its requested departure and arrival name their places (by name and UN/LOCODE or GLN, as used for the same places in rail/08).
- Options: (a) preferred: TransportModeCode 2 and `cac:Location` on both events (Ferrano Intermodal Hub / XUFER; Lumeway siding / XBMRW); (b) use the stage's own LoadingPortLocation/UnloadingPortLocation where the request wants to name the rail terminals.
- Needs decision: no

### rail/02#F4 · Medium · Urvanian province in Region in the from and to locations
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL's Region is "the recognized geographic or economic region or group of countries in which this address is located"; a province, a country's administrative subdivision, belongs in CountrySubentity (as the Bayvarran states are given in this flow, e.g. `CountrySubentity` = Upland State in the consignee's address). The same "Province of …" value is in `cbc:Region` 219 times in 104 examples (`grep -rh --include='*.xml' '<cbc:Region>Province of'`), so it looks like a deliberate convention for Urvania; whether the world's address rules mean provinces as non-administrative regions is for the owner to confirm.
- Condition: An Urvanian province is in `cbc:CountrySubentity` (optionally with a code), or the world states that Urvanian provinces are economic regions and not subdivisions.
- Options: (a) preferred: move to CountrySubentity, as for Bayvarra; (b) keep and document the convention as a finding of the world's address rules.
- Needs decision: yes

### rail/02#F5 · Low · From location named after the company, not the place
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- Why: A Location's name is the place, not the company that runs it. The waybill names the same place `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`.
- Condition: The from location's name names the warehouse as a place, in the same words as the other examples of the flow.
- Options: use "Castrano Logistics warehouse, Ferrano" (preferred, matches rail/08), optionally with a GLN.
- Needs decision: no

## Checked and consistent
- Consignment VI-CS-26-0327, 192 benches, gross 7968 kg, two 40-foot containers, containerised: identical in 03 and, for the weight, in 06 (goods item). 7968 / 192 = 41.5 kg per bench.
- Requested delivery 2026-04-16 matches the plan's contractual latest delivery date and the waybill's latest delivery date of the containers (2026-04-16); requested arrival 2026-04-15 matches the plan's planned arrival.
- Response deadline 2026-04-08 lies after the issue (2026-04-07 10:32) and is met by the plan issued 2026-04-08 16:46 (the deadline has no time).
- Consignor Valdara Industries and consignee Lumeway Distribution agree with 03, 06 and 08; the GLN 9520610900008 passes check_ids.py.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent`: a pickup event without location — refuted, because the pickup point is unambiguously the FromLocation of the same request (the Castrano warehouse) and the plan, waybill and itinerary agree.
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription` = `192 park benches in two 40-foot containers.`: a request that names no equipment or goods items might not say what is to be carried — refuted: the summary, weight and containerised indicator say what is carried and in what equipment, which is enough for a request.
- `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`: does not resolve to an example — refuted as a broken reference, it names the framework contract, not a document of the flow; the double identification of that contract is raised in the review of rail/03.
