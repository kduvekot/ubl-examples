# LLM review: 09-GoodsItemItinerary.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

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

### rail/09#F1 · High · "The itinerary of the two containers" references one container
- XPath: `/GoodsItemItinerary/cbc:Note[2]` = `The itinerary of the two containers.`
- XPath: `/GoodsItemItinerary/cac:ReferencedTransportEquipment/cbc:ID` = `FRXU1044175`
- Why: ReferencedTransportEquipment is "transport equipment being transported in the transport service associated with this Goods Item Itinerary". The note says the itinerary is for two containers, and the consignment travels in two (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:ID` = `FRXU1044180`), but only FRXU1044175 is referenced.
- Condition: the note and the referenced equipment agree (both containers referenced, or the note speaks of one).
- Options: (a) preferred: reference FRXU1044180 as well; (b) a note for one container, if a separate itinerary covers the other.
- Needs decision: no

### rail/09#F2 · Medium · An itinerary without places or times
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:TransportModeCode` = `2`
- Why: The document is "a document providing details relating to a transport service, such as transport movement, identification of equipment and goods". Its one segment says only that it is by rail under plan FRC-TEP-26-0328; the shipment stage gives no departure, arrival, place or time, so the itinerary does not tell the receiver where or when the containers move. The data exists in the flow (rail/03: departure 14 April 06:45 from the hub, arrival 15 April 10:30 in Marrowdale; the road collection from Castrano on 13 April).
- Condition: the itinerary gives, per segment or stage, where and when the goods move (at least departure and arrival with place and time).
- Options: (a) preferred: planned departure and arrival with locations in the stage, and a first segment (or stage) for the road collection to the hub; (b) none that keeps an itinerary without them.
- Needs decision: no

### rail/09#F3 · Medium · A package that exists nowhere in the flow
- XPath: `/GoodsItemItinerary/cac:ReferencedPackage/cbc:ID` = `KXU104413250000013`
- Why: ReferencedPackage is "a package being transported in the transport service associated with this Goods Item Itinerary". No other example describes packages for this consignment (`grep -rn --include='*.xml' KXU104413250000013 world/examples` finds only this file), and the consignment holds 192 benches, wrapped per bench (packaging waste "Stretch film and pallet straps, per bench" in rail/01). One package among them cannot be linked to anything and has no visible role in the itinerary of two containers.
- Condition: the referenced package is described in the documents of the consignment (packing list or waybill) and has a reason to be tracked on its own, or the reference is absent.
- Options: (a) preferred: drop it; (b) describe the packages (e.g. pallets with SSCCs) in the waybill and reference them all, which extends the story.
- Needs decision: no

### rail/09#F4 · Medium · Province in Region
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a Region.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/09#F5 · Low · Share listing and warehouse provider of the receiver
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:ServiceProviderParty`
- Why: The itinerary does nothing with Valdara's share listing or with its warehousing provider (the itinerary names no place at all, see F2).
- Condition: no party data without a reason in the itinerary.
- Options: (a) preferred: drop both here (keep the provider only if Castrano becomes a place of the itinerary).
- Needs decision: no

## Checked and consistent
- TransportExecutionPlanReferenceID FRC-TEP-26-0328 (document and segment) is rail/03; the service provider of the segment is its provider; the consignment VI-CS-26-0327 is the same.
- RAILCONT fits the container train (and contradicts rail/03's FTL, which is a finding of rail/03).

## Considered and refuted
- `/GoodsItemItinerary/cac:ReferencedGoodsItem/cbc:ID` = `1`: suspected unlinked — refuted because goods item 1 is the single goods item of the consignment in rail/06.
