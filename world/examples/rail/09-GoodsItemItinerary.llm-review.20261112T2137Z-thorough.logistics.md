# LLM review: 09-GoodsItemItinerary.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/09-GoodsItemItinerary.xml`, Git blob `3dfd231396ba484476d5dfeef7a1accb9a1e27f9` (committed)
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

### rail/09#F1 · High · "The itinerary of the two containers" lists one container
- XPath: `/GoodsItemItinerary/cbc:Note[2]` = `The itinerary of the two containers.`
- XPath: `/GoodsItemItinerary/cac:ReferencedTransportEquipment/cbc:ID` = `FRXU1044175`
- Why: ReferencedTransportEquipment is "transport equipment being transported in the transport service associated with this Goods Item Itinerary". The note says the itinerary covers two containers, and the consignment has two (FRXU1044175 and FRXU1044180, `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:ID` = `FRXU1044180`), but only one is referenced. The free text contradicts the structured value next to it.
- Condition: The itinerary references every container its note says it covers (both), or the note says it covers one.
- Options: (a) preferred: add FRXU1044180 as a second ReferencedTransportEquipment; (b) change the note.
- Needs decision: no

### rail/09#F2 · High · The segment governed by the plan is a container train, the plan a full truck load
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cbc:TransportExecutionPlanReferenceID` = `FRC-TEP-26-0328`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`
- Why: TransportationSegment is "a part of a transport service that has its own Transport Execution Plan", and its TransportExecutionPlanReferenceID names the plan governing it, rail/03. That plan's main transportation service is a full truck load from the warehouse to the hub (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`), while this segment, governed by it, is a container train by rail (mode 2). The itinerary and the plan it refers to describe different services. The cause lies mainly in the plan (rail/03#F1), but the contradiction is visible here too.
- Condition: The service of the segment and the main service of the plan it refers to are the same service.
- Options: (a) preferred: fix the plan's main service to the container train (rail/03#F1), leaving this segment as it is; (b) if the plan is really only the truck leg, the rail segment needs a plan of its own.
- Needs decision: yes

### rail/09#F3 · Medium · An itinerary without places or times
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:TransportModeCode` = `2`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment`
- Why: A Goods Item Itinerary provides "details relating to a transport service, such as transport movement, identification of equipment and goods". Its only segment carries a sequence number, a plan reference, a service code, a provider, the consignment and a stage with only the mode. It says nothing about where the goods go from and to or when: no departure, arrival, loading or unloading location, no planned or estimated event. Without them, the document cannot serve as the itinerary its note announces; the flow has all the data (departure from the hub 06:45, arrival in Marrowdale 2026-04-15 10:30, rail/03 and rail/08).
- Condition: Each segment states at least its start and end places and the planned (or estimated) departure and arrival.
- Options: (a) preferred: add PlannedDeparture/PlannedArrival transport events with locations (XUFER, XBMRW) to the segment's shipment stage, and the train in its TransportMeans; (b) at least LoadingPortLocation/UnloadingPortLocation on the stage.
- Needs decision: no

### rail/09#F4 · Medium · A referenced package that appears nowhere else in the flow
- XPath: `/GoodsItemItinerary/cac:ReferencedPackage/cbc:ID` = `KXU104413250000013`
- Why: ReferencedPackage is "a package being transported in the transport service associated with this Goods Item Itinerary". No other example of the flow describes packages, and this package ID occurs in no other example (`grep -rl --include='*.xml' KXU1044132 world/examples` finds only this file). The itinerary names one package among 192 benches in two containers, without saying which goods or container it belongs to. The ID's structure (licence-plate format like the Castrano package `KXU104411490000015` in road/08) also does not contain Castrano's register number 104411, so its issuer cannot be identified.
- Condition: Every package the itinerary references is described in the flow (e.g. in the waybill or a packing list) and can be linked to its goods item or container, or the reference is absent.
- Options: (a) preferred: remove the package reference, since the flow tracks containers, not packages; (b) describe the packages (e.g. bench bundles) in the waybill with these IDs, issued under the packer's own prefix.
- Needs decision: no

### rail/09#F5 · Low · The road leg of the same carrier is not in the itinerary
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cbc:SequenceNumeric` = `1`
- Why: The carrier also hauls the containers from the Castrano warehouse to the hub (`08-Waybill.xml:/Waybill/cbc:Description` = `Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.`, pickup 2026-04-13 15:00). The itinerary sent to the transport user has only the rail segment, so the goods' itinerary starts at the hub, not where the goods are taken over. Whether the road leg is a segment of its own depends on how rail/03#F1 is resolved.
- Condition: The itinerary covers the goods from their takeover to delivery, or it states that it covers the rail segment only.
- Options: (a) preferred: add a segment 1 for the carrier haulage (mode 3) and renumber the rail segment 2; (b) state the scope in the note.
- Needs decision: yes

## Checked and consistent
- TransportExecutionPlanReferenceID FRC-TEP-26-0328 (header and segment) resolves to rail/03; consignment VI-CS-26-0327 and provider Ferrano Rail Cargo agree with rail/03 and rail/08.
- Container FRXU1044175 passes the ISO 6346 check digit (check_ids.py) and is one of the two containers of rail/06 and rail/08.
- ReferencedGoodsItem 1 matches the goods item 1 of the transit declaration rail/06 (192 park benches).
- Issue 2026-04-14 09:00, after the departure 06:52, by the carrier to the transport user: fits a confirmation of the itinerary of goods under way.

## Considered and refuted
- `/GoodsItemItinerary/cac:ReferencedGoodsItem/cbc:ID` = `1`: a goods item ID without the document it belongs to — refuted: in the flow only the transit declaration has goods items, and its item 1 is the whole consignment.
