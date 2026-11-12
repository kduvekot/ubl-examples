# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

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

### rail/02#F1 · High · Requested pickup lies before the period in which the service must begin
- XPath: `/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: ServiceStartTimePeriod is "the period within which the services referred to in the Transport Execution Plan Request must begin". The request asks for the pickup at Castrano Logistics on 13 April 15:00, a day before that period opens. The pickup by the carrier's tractor (Note: "Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub") is part of the requested service, so the service begins on 13 April.
- Condition: the requested pickup lies within the service start period (or the service start period begins no later than the pickup).
- Options: (a) preferred: start the period on 2026-04-13; (b) if the road haulage is meant to be a separate service, request it separately and leave this request to the rail carriage.
- Needs decision: no

### rail/02#F2 · Medium · Main transportation service "Full truck load" for a container train service
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Full truck load`
- Why: The world's TransportService list defines FTL as "One truck for one consignment, from the place of loading to the place of delivery". The request goes to a rail carrier, the consignment is "192 park benches in two 40-foot containers", its main carriage runs via the "Rail border station Urvania–Bayvarra", and the goods item itinerary for the plan that answers it uses RAILCONT ("Containers on a scheduled container train"): `09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`. One tractor cannot carry two 40-foot containers, and no truck goes from the place of loading to the place of delivery.
- Condition: the main transportation service names the container train service (the road collection, if mentioned, as an additional service).
- Options: (a) preferred: RAILCONT as main service, with the road collection (carrier haulage) as AdditionalTransportationService; (b) FTL only if the request is narrowed to the road leg, which contradicts the main-carriage stage it carries.
- Needs decision: no

### rail/02#F3 · Medium · From and To locations describe the road collection only
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`
- Why: ToLocation is "the destination location for the transport service referenced in the Transport Execution Plan Request". The service requested goes beyond the hub: a main-carriage stage with a waypoint at the rail border station and a requested arrival on 15 April, and a requested delivery to the consignee Lumeway Distribution in Bayvarra on 16 April. The hub is a transhipment point, not the destination.
- Condition: ToLocation is the place where the requested service ends (the consignee's siding in Marrowdale), or the request covers only the leg its From/To describe.
- Options: (a) preferred: ToLocation = the Lumeway siding in Marrowdale; (b) split into two requests (road collection, rail carriage).
- Needs decision: no

### rail/02#F4 · Medium · LocaleCode holds a bare language code
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats Language/ID and names no locale. 362 occurrences over `*.xml`.
- Condition: LocaleCode is a locale (e.g. `en-XB`) or absent.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### rail/02#F5 · Medium · Province in Region
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: A province is "the political or administrative division of a country" (CountrySubentity), not a "geographic or economic region or group of countries" (Region). The consignee's Bayvarran address in the same document uses CountrySubentity for its state.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them as non-administrative regions.
- Options: (a) preferred: CountrySubentity; (b) keep Region with a stated world rule.
- Needs decision: yes

### rail/02#F6 · Low · Share listing of the transport user in a transport request
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing`
- Why: The listing of Valdara's shares on the Ferrano Stock Exchange plays no part in requesting rail transport; nothing in the request uses it.
- Condition: the request carries no party data without a reason in it.
- Options: (a) preferred: drop it here.
- Needs decision: no

## Checked and consistent
- Sender = transport user = bill-to party (Valdara), receiver = transport service provider (Ferrano Rail Cargo): fit a request under DAP where the seller pays the freight.
- The service provider response deadline (8 April) after the issue date (7 April) and before the service.
- ServiceProviderParty Castrano Logistics ("Warehousing and despatch") in the sender is used: the FromLocation is Castrano's warehouse.
- ContainerizedIndicator true with the summary "two 40-foot containers".

## Considered and refuted
- `/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.`: suspected filler — refuted because asking the provider to confirm is the normal remark of a transport user, and the plan answers it.
- `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`: checked that the waypoint has a location — it has.
