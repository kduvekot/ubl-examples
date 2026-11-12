# LLM review: 09-GoodsItemItinerary.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/09-GoodsItemItinerary.xml`, Git blob `3dfd231396ba484476d5dfeef7a1accb9a1e27f9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/09#F1 · High · "Itinerary of the two containers" lists one container
- XPath: `/GoodsItemItinerary/cbc:Note[2]` = `The itinerary of the two containers.`
- XPath: `/GoodsItemItinerary/cac:ReferencedTransportEquipment/cbc:ID` = `FRXU1044175`
- Why: The note says the itinerary is that of the two containers; ReferencedTransportEquipment ("Transport equipment being transported in the transport service associated with this Goods Item Itinerary") names only FRXU1044175. The second container of the consignment, FRXU1044180 (06, 08), is missing.
- Condition: The referenced equipment and the note agree: both containers are referenced, or the note speaks of one.
- Options: (a) preferred: add FRXU1044180 as a second ReferencedTransportEquipment; (b) change the note.
- Needs decision: no

### rail/09#F2 · High · Service of the segment contradicts the plan it refers to
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cbc:TransportExecutionPlanReferenceID` = `FRC-TEP-26-0328`
- Why: The segment is governed by FRC-TEP-26-0328 and calls its service a container train; that plan calls its main service a full truck load (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`). The itinerary's value fits the rail stage (mode 2); the plan's does not (see the review of 03), but as they stand the two documents describe the same service differently.
- Condition: The itinerary and the plan it refers to state the same transportation service.
- Options: (a) preferred: correct the plan to RAILCONT and keep the itinerary; (b) none other that keeps the rail stage.
- Needs decision: no

### rail/09#F3 · Medium · An itinerary without places or times
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:TransportModeCode` = `2`
- Why: A Goods Item Itinerary provides "details relating to a transport service, such as transport movement, identification of equipment and goods ..."; its point is to say where the goods go and when. The only stage gives a mode of transport and nothing else: no departure or arrival place, no times, no train. The plan and the waybill hold all of these (hub 14 April 06:45, Marrowdale 15 April 10:30, train FRC 4417).
- Condition: Each segment's stage states at least where it begins and ends and the planned (or estimated) departure and arrival.
- Options: (a) preferred: the stage with planned departure and arrival events and their locations (hub, Marrowdale) and the transport means; (b) drop the itinerary from the flow if it adds nothing to the plan.
- Needs decision: no

### rail/09#F4 · Medium · A referenced package that no other document knows
- XPath: `/GoodsItemItinerary/cac:ReferencedPackage/cbc:ID` = `KXU104413250000013`
- Why: ReferencedPackage is "A package being transported in the transport service associated with this Goods Item Itinerary". No other example has this package or any package at all for this consignment (`grep -rl --include='*.xml' 'KXU104413250000013' world/examples` finds only this file; 06 and 08 describe goods and containers but no packages). A single package also does not fit 192 benches in two containers. The reference cannot be linked to anything.
- Condition: Every referenced package is described (with its ID) in the documents that describe the goods, or the reference is absent.
- Options: (a) preferred: drop ReferencedPackage; (b) describe the packages (e.g. one per pallet) in the waybill and the declaration, with these IDs, and reference all of them.
- Needs decision: no

### rail/09#F5 · Medium · Province given in Region
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity). 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as non-administrative.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/09#F6 · Low · The haulage leg of the same plan is missing
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cbc:SequenceNumeric` = `1`
- Why: The plan FRC-TEP-26-0328 covers the carrier haulage from Castrano's warehouse to the hub (13 April) as well as the rail stage; the itinerary of the goods starts only with the rail segment, so the goods' first movement is not in their itinerary.
- Condition: The itinerary covers every movement of the goods under the plan, or says that it covers the rail stage only.
- Options: (a) preferred: a first segment for the haulage (road), the rail segment second; (b) a note limiting the itinerary to the rail stage.
- Needs decision: no

### rail/09#F7 · Low · Receiver's warehouse provider and sales contact copied in
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The itinerary does nothing with Valdara's warehousing provider (its segment starts at the hub); Valdara is reached at its sales order desk although it receives a transport itinerary.
- Condition: ServiceProviderParty only where the document uses it; the receiver's contact is a shipping/logistics function (or absent).
- Options: (a) preferred: drop ServiceProviderParty; a logistics contact.
- Needs decision: no

### rail/09#F8 · Low · Package ID in a real scheme that could be mistaken for a real licence plate
- XPath: `/GoodsItemItinerary/cac:ReferencedPackage/cbc:ID` = `KXU104413250000013`
- Why: The schemeID is ISO 15459, the real standard for unique transport unit identifiers (licence plates), whose first characters are the issuing agency code from the real register. Whether the leading `K` is an issuing agency code assigned in the real ISO 15459 register could not be checked here; if it is, the value can be mistaken for a real licence plate of that agency.
- Condition: The identifier is either in a world scheme or uses an issuing agency code that the sources record as unassigned (or the world's own agency).
- Options: (a) check the code against the ISO 15459 register and record it in the sources; (b) preferred if unsure: use a world package-ID scheme.
- Needs decision: yes (could not be settled here)

## Checked and consistent
- References: `FRC-TEP-26-0328` (document and segment) resolves to 03; consignment VI-CS-26-0327 and goods item 1 exist in 06 and 08; container FRXU1044175 exists in 06 and 08 (check digit OK); provider Ferrano Rail Cargo is the carrier of 03 and 08; mode 2 agrees with the rail stage of 03 and 08.
- Parties described as in the other rail examples.

## Considered and refuted
- `/GoodsItemItinerary/cac:ReferencedTransportEquipment/cbc:ID` = `FRXU1044175`: suspected a container that is not in the consignment — refuted because 06 and 08 list it in consignment VI-CS-26-0327.
