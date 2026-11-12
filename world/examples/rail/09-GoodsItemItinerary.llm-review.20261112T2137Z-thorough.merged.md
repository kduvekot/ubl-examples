# LLM review: 09-GoodsItemItinerary.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/09-GoodsItemItinerary.xml`, Git blob `3dfd231396ba484476d5dfeef7a1accb9a1e27f9` (committed)
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

### rail/09#F1 · High · "The itinerary of the two containers" references one container
- XPath: `/GoodsItemItinerary/cbc:Note[2]` = `The itinerary of the two containers.`
- XPath: `/GoodsItemItinerary/cac:ReferencedTransportEquipment/cbc:ID` = `FRXU1044175`
- Why: ReferencedTransportEquipment is "Transport equipment being transported in the transport service associated with this Goods Item Itinerary". The note says the itinerary covers two containers, and the consignment travels in two (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:ID` = `FRXU1044180`), but only FRXU1044175 is referenced. Free text contradicts the structured value next to it (verified in the XML: one ReferencedTransportEquipment).
- Condition: The note and the referenced equipment agree: both containers referenced, or the note speaks of one.
- Options: (a) preferred: add FRXU1044180 as a second ReferencedTransportEquipment; (b) change the note (if a separate itinerary covers the other box).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### rail/09#F2 · High · The segment's service contradicts the plan it refers to
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cbc:TransportExecutionPlanReferenceID` = `FRC-TEP-26-0328`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- Why: TransportationSegment is "a part of a transport service that has its own Transport Execution Plan", and its TransportExecutionPlanReferenceID names the plan governing it, 03. That plan's main service is a full truck load (verified in 03: Name "Full truck load"), while this segment, governed by it, is a container train by rail (mode 2). The itinerary's value fits the rail stage; the plan's does not (a finding of 03, High in the other merger's decisions), but as they stand the two documents describe the same service differently.
- Condition: The service of the segment and the main service of the plan it refers to are the same service.
- Options: (a) preferred: correct the plan's main service to RAILCONT (with the road leg as pre-carriage there), leaving this segment as it is; (b) if the plan is really only the truck leg, the rail segment needs a plan of its own (adds a document).
- Needs decision: no (logistics said yes for option (b); the preferred fix is encoding in 03, aligned with the merge of rail 01–05)
- From: broad (F2), logistics (F2)

### rail/09#F3 · Medium · An itinerary without places or times
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cac:ShipmentStage/cbc:TransportModeCode` = `2`
- Why: A Goods Item Itinerary provides "details relating to a transport service, such as transport movement, identification of equipment and goods". Its only segment carries a sequence number, a plan reference, a service code, a provider, the consignment and a stage with only the mode: no departure, arrival, loading or unloading place, no planned or estimated event, no train. The document's purpose depends on them; the flow has the data (hub 14 April 06:45, Marrowdale 15 April 10:30, train FRC 4417; 03, 08).
- Condition: Each segment states at least its start and end places and the planned (or estimated) departure and arrival.
- Options: (a) preferred: planned departure and arrival events with locations (XUFER, XBMRW) in the stage, and the train in its TransportMeans; (b) at least loading/unloading locations on the stage; (c) drop the itinerary from the flow if it adds nothing to the plan (broad).
- Needs decision: no
- From: broad (F3), logistics (F3), context (F2)

### rail/09#F4 · Medium · A referenced package that appears nowhere else in the flow
- XPath: `/GoodsItemItinerary/cac:ReferencedPackage/cbc:ID` = `KXU104413250000013`
- Why: ReferencedPackage is "A package being transported in the transport service associated with this Goods Item Itinerary". No other example has this package or any package for this consignment (`grep -rl --include='*.xml' 'KXU1044132' world/examples` finds only this file; 06 and 08 describe goods and containers but no packages). One package among 192 benches in two containers, without its goods item or container, cannot be linked to anything. Its licence-plate structure (like the Castrano packages `KXU104411490000015` in road/08) does not contain Castrano's register number 104411, so its issuer cannot be identified either.
- Condition: Every referenced package is described (with its ID) in the documents of the consignment and linked to its goods or container, or the reference is absent.
- Options: (a) preferred: drop ReferencedPackage (the flow tracks containers, not packages); (b) describe the packages (e.g. bench bundles with SSCCs) in the waybill and the declaration, under the packer's prefix, and reference all of them.
- Needs decision: no
- From: broad (F4), logistics (F4), context (F3)

### rail/09#F5 · Medium · Province given in Region
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (CountrySubentity), as the flow's Bayvarran addresses use (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 example files.
- Condition: No address in this example carries the province in Region; where given, it is in CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it.
- Needs decision: no (broad, context yes; aligned with rail 01–05, wood, plastics)
- From: broad (F5), parties (F1), context (F4)

### rail/09#F6 · Low · The carrier haulage of the same plan is not in the itinerary
- XPath: `/GoodsItemItinerary/cac:TransportationSegment/cbc:SequenceNumeric` = `1`
- Why: The carrier also hauls the containers from Castrano's warehouse to the hub (`08-Waybill.xml:/Waybill/cbc:Description` = `Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.`, pickup 13 April 15:00), under the same plan. The itinerary sent to the transport user starts at the hub, not where the goods are taken over.
- Condition: The itinerary covers the goods from takeover to delivery, or states that it covers the rail segment only.
- Options: (a) preferred: a first segment for the haulage (mode 3), the rail segment second; (b) a note limiting the itinerary to the rail stage.
- Needs decision: no (logistics said yes because it depends on how 03's FTL finding is resolved; either option is encoding)
- From: broad (F6), logistics (F5)

### rail/09#F7 · Low · Package ID in a real scheme, issuing agency not checked
- XPath: `/GoodsItemItinerary/cac:ReferencedPackage/cbc:ID` = `KXU104413250000013`
- Why: The schemeID is ISO 15459, the real standard for unique transport unit identifiers, whose leading characters are an issuing agency code from the real register. Whether `K` is an issuing agency code assigned in the real ISO 15459 register could not be checked (neither by broad nor in the merge); if it is, the value could be mistaken for a real licence plate of that agency. The same prefix is used in road/08.
- Condition: The identifier is either in a world scheme or uses an issuing agency code that the sources record as unassigned (or as the world's own agency).
- Options: (a) check the code against the ISO 15459 register and record it in the sources; (b) preferred if unsure: a world package-ID scheme.
- Needs decision: yes (could not be settled)
- From: broad (F8)

### rail/09#F8 · Low · Receiver's contact is the sales order desk
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara receives the itinerary of its containers as transport user; it is used by whoever follows the shipment (shipping, logistics), not by the order desk that takes customer orders.
- Condition: The receiver's contact is Valdara's shipping or logistics function, or absent.
- Options: (a) preferred: a shipping/logistics contact; (b) role-specific contacts in Valdara's master data.
- Needs decision: no
- From: parties (F3), broad (F7, contact part)

### rail/09#F9 · Low · Receiver's master data the itinerary does nothing with
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: An itinerary does nothing with the receiver's stock-exchange listing or share capital; Valdara's warehousing provider is not a provider of the transport service described (the only segment is the container train from the hub), and nothing in the itinerary refers to it (section 4.8).
- Condition: Every legal-entity and service-provider element present has a purpose in the itinerary.
- Options: (a) preferred: drop them here (keep the provider only if Castrano's warehouse becomes a place of the itinerary, see F6); (b) a reduced party description for transport documents.
- Needs decision: no
- From: parties (F4), context (F5), broad (F7, provider part)

### rail/09#F10 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5); these are tagged `en-XU` but are Italian (own knowledge). A world convention for street names cannot be ruled out; the legal forms are the stronger case. 217 such renderings in 102 example files.
- Condition: Every rendering tagged as English is English, or the world records the Italianate English usage.
- Options: (a) record the convention (preferred if intended); (b) translate; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F2)

### rail/09#F11 · Low · Sender's registration date 1996-01-01
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Not raised by any part of this run; added by the merge for consistency with rail 01–05 and earlier flows (271 occurrences in 181 example files): the date reads as a default, unless a 1996 (re-)registration is part of the story.
- Condition: Each company's registration date is its own, or the world records a general 1996 registration.
- Options: (a) preferred: own date per company; (b) record a 1996 re-registration in the story.
- Needs decision: yes
- From: merge

## Checked and consistent
- References: TransportExecutionPlanReferenceID `FRC-TEP-26-0328` (document and segment) resolves to 03; consignment VI-CS-26-0327 and provider Ferrano Rail Cargo agree with 03 and 08; container FRXU1044175 is one of the two containers of 06 and 08 (ISO 6346 check digit passes); mode 2 agrees with the rail stage of 03 and 08; RAILCONT fits the container train.
- ReferencedGoodsItem 1 matches the single goods item of the transit declaration 06 (192 park benches).
- Issue 2026-04-14 09:00, after the departure 06:52, by the carrier to the transport user: fits a confirmation of the itinerary of goods under way.
- Sender, signatory and segment provider Ferrano Rail Cargo (`XU-R-104685`), receiver Valdara (`XU-R-104274`): the parties of the plan 03, with identical descriptions; ISIN `XU0001042501` check digit correct.

## Considered and refuted
- `/GoodsItemItinerary/cac:ReferencedTransportEquipment/cbc:ID` = `FRXU1044175`: a container not in the consignment — refuted because 06 and 08 list it in consignment VI-CS-26-0327. (from broad)
- `/GoodsItemItinerary/cac:ReferencedGoodsItem/cbc:ID` = `1`: a goods item ID without the document it belongs to, or unlinked — refuted: in the flow only the transit declaration has goods items, and its item 1 is the whole consignment. (from logistics, context)

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1; broad/F3, logistics/F3, context/F2 → F3; broad/F4, logistics/F4, context/F3 → F4: combined.
- broad/F2, logistics/F2 → F2: needs decision no (logistics yes), aligned with the merge of 01–05, which sets RAILCONT in 03 as the preferred fix.
- broad/F5, parties/F1, context/F4 → F5: needs decision no (broad, context yes).
- broad/F6, logistics/F5 → F6: needs decision no (logistics yes): both options are encoding.
- broad/F7 split: contact part → F8 (with parties/F3), provider part → F9 (with parties/F4, context/F5).
- parties/F2 → F10: count replaced by 217 in 102 files.
- F11 added by the merge (registration date 1996-01-01).
