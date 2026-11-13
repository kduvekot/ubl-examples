# LLM review: 14-BillOfLading.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/14-BillOfLading.xml`, Git blob `661653ae609f88a3a1ea21ce846d10c0b8de2faf` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/14#F1 · High · One SSCC for both the frames pallet and a box on it; package count of the pallet against the box
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TransportHandlingUnitTypeCode` = `PX`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:PackagingTypeCode` = `BX`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:Quantity` = `12`
- Why: an SSCC identifies exactly one logistic unit (own knowledge of the GS1 SSCC rules). Here the same SSCC is the ID of the 25th handling unit, a pallet (`PX`), and of a package of type box (`BX`) directly in the container. Either the pallet and the box are one object described twice with two packaging types, or two objects share a key. The counts do not agree either: `Package/Quantity` is "The quantity of items contained in this package", so the box holds the 12 frames; a pallet carrying that box then holds 1 package, while `TotalPackageQuantity` ("The total number of packages in this transport handling unit") says 12.
- Condition: each SSCC identifies one unit of one type, and the package count of the frames pallet agrees with how the frames are packed (12 loose frames, or 1 box of 12).
- Options: the frames travel as one box of 12 on pallet 25: give the box its own ID (or none), nest it in the pallet, and set the pallet's package count to 1 (preferred: keeps the "castings pallet" of the packing list); or the frames are 12 film-wrapped pieces on the pallet: drop the box package and keep 12.
- Needs decision: no

### sea/14#F2 · Medium · Consignor's and forwarder's consignment IDs hold other parties' document numbers
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `VT-PO-26-0127`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreightForwarderAssignedID` = `LD-FI-26-0131`
- Why: `ConsignorAssignedID` is "An identifier for this consignment, assigned by the consignor" and `FreightForwarderAssignedID` "An identifier for this consignment, assigned by the freight forwarder". The consignor is Lumeway; `VT-PO-26-0127` is the purchase order assigned by the buyer, Velumi (`05-Order.xml`), and an order number, not a consignment ID. The forwarder is Bayforth; `LD-FI-26-0131` is the number Lumeway gave its forwarding instructions (`09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0131`), i.e. a document of the consignor. The consignor's own consignment ID is `LD-CS-26-0133` (`Consignment/ID`); Bayforth's own reference is its shipping order `BF-FI-26-0137`.
- Condition: each party-assigned consignment ID is assigned by that party and identifies the consignment.
- Options: drop `ConsignorAssignedID` (the consignment's `ID` is Lumeway's) and set `FreightForwarderAssignedID` to a Bayforth reference (e.g. its file number, or leave it out since `ShippingOrderID` carries `BF-FI-26-0137`) (preferred); and, if the buyer's order number is wanted on the bill of lading, carry it as a document reference with type "order".
- Needs decision: no

### sea/14#F3 · Medium · Goods item container quantity counts pallets, not goods items
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem/cac:GoodsItemContainer/cbc:Quantity` = `25`
- Why: `GoodsItemContainer/Quantity` is "The number of goods items loaded into or onto one piece of transport equipment as a total consignment or part of a consignment". The container holds one goods item (`ID` 1, with two contained goods items 1.1 and 1.2); 25 is the number of pallets (`PackagedTransportHandlingUnit[1]` to `[25]`), and the quantity of goods is 96 + 12 pieces.
- Condition: the quantity is the number of goods items (or goods-item units) in the container, as the definition says.
- Options: 1 (the one goods item, all of which is in this container) (preferred); or drop it, since the goods item lies wholly in one container.
- Needs decision: no

### sea/14#F4 · Medium · Shipment gross weight excludes the transport equipment its definition includes
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The shipment's only piece of equipment weighs 7,856.4 kg gross (= 4,106.4 + tare 3,750, equal to the VGM), so under the definition the shipment weighs 7,856.4 kg; 4,106.4 kg is goods plus packaging (the gross weight practice prints on a bill of lading, which the semantic-conformance rule does not follow).
- Condition: the shipment's gross weight includes the transport equipment, or the goods-and-packaging weight is carried on the goods item.
- Options: put 4,106.4 kg on the goods item's `GrossWeightMeasure` (where its definition, "excluding the carrier's equipment", fits) and 7,856.4 kg or nothing on the shipment (preferred); or 7,856.4 kg on the shipment only.
- Needs decision: no

### sea/14#F5 · Low · Road chassis attached to a container stowed on the ship's deck
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:ID` = `BV CH 0412`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:TransportEquipmentTypeCode` = `TE`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:StowagePositionID` = `140282`
- Why: `AttachedTransportEquipment` is "A piece of transport equipment attached to this piece of transport equipment". The trailer `BV CH 0412` is the pre-carriage truck's trailer (`/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:TrailerLicensePlateID` = `BV CH 0412`); it was attached for the road leg to the port, which ended with the drop-off on 2026-05-13. On the bill of lading, which describes the container shipped on board in slot 14-02-82 on deck, the chassis is not attached to it.
- Condition: the container's attached equipment describes what is attached during the carriage the bill of lading covers.
- Options: drop the attached equipment here (preferred: the trailer is already given in the pre-carriage stage); or keep it only in a document about the road leg.
- Needs decision: no

### sea/14#F6 · Low · On-carriage events without place and time
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:WarehousingTransportEvent/cbc:OccurrenceDate` = `2026-05-19`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:ReceiptTransportEvent/cbc:OccurrenceDate` = `2026-05-19`
- Why: the two planned on-carriage events have a date and `CompletionIndicator` false but no location; where the goods are warehoused and received is only implied by the on-carriage carrier (Nalevi Warehousing). Under the checklist, an event needs a location where it would otherwise be meaningless; the place of receipt is also the end of the carrier's information chain to the consignee.
- Condition: each on-carriage event carries its location (the warehouse in Selanu, identified as in `20-DespatchAdvice.xml`).
- Options: add the warehouse's location to both events (preferred); or one location for the on-carriage stage.
- Needs decision: no

### sea/14#F7 · Low · Port of registry named but not identified
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- Why: the port of registry is given by name only, while the same document identifies Lumeport as UN/LOCODE `XBLMP` (loading port, freight charge location, last exit port).
- Condition: the registry port carries the LOCODE `XBLMP`.
- Options: add `ID` `XBLMP` (preferred).
- Needs decision: no

## Checked and consistent
- Weights (calculated): 3,984 + 122.4 = 4,106.4 kg of goods and packaging (`10-PackingList.xml`); + tare 3,750 = 7,856.4 kg = container gross = VGM `GrossMassMeasure`. Method `SM2` (weighing all packages and adding the tare, own knowledge of SOLAS VI/2) is consistent with this sum; weighed 2026-05-12 15:30, before the packing list (15:59) and the drop-off (2026-05-13 10:15).
- Container `TWLU4120872`: ISO 6346 check digit valid (`check_ids.py`); `42G1` with tare 3,750 kg is typical; 7,856 kg gross is far below a 40-foot box's 30,480 kg maximum gross; 41.5 m³ gross volume against about 67.7 m³ inside fits (61 %).
- Stowage `140282` read as bay 14, row 02, tier 82 (ISO 9711, own knowledge): an even bay is a 40-foot slot, tier 82 is on deck, consistent with "On deck" and with the slot length of 12.2 m (a 40-foot box is 12.19 m). The handling code `DECK` allows on-deck stowage; "Keep dry" is met by a closed general-purpose box.
- SSCCs `095206101230000018` … `095206101230000254`: all 25 check digits valid (`check_ids.py`); 24 bench pallets × 4 + 12 frames = 108 packages, as in `06-OrderResponse.xml` (apart from F1).
- Vessel: gross tonnage 9,940 and net tonnage 5,120 fit a feeder of about 1,000 TEU (`08-TransportServiceDescription.xml`); the same vessel ID, name, call sign, MMSI, tonnages and voyage in `15-Manifest.xml`. Call sign `QBTH7` starts with Q, a prefix the ITU does not allocate to countries; the MMSI's MID 298 is, to my knowledge, not allocated to any administration (Europe uses 201–279), so neither can be mistaken for a real ship (own knowledge, not checked against the current ITU tables).
- Values: CIF value 53,778 = 50,688 + 2,700 + 250 + 140 (`DeclaredCustomsValueAmount` and `DeliveryTerms/Amount`); insured value 59,155.80 = 110 % of 53,778.
- References: `LD-PL-26-0134` → `10-PackingList.xml`; `BF-FI-26-0137` (document reference and shipping order) → `12-ForwardingInstructions.xml`; the booking number `TWL-BK-26-55710` is the same as there.
- Events: drop-off at the terminal and acceptance on 2026-05-13 10:15, storage from 10:30, availability at Selanu 2026-05-18 14:00 (not completed) — consistent with each other and with the issue on 2026-05-14.

## Considered and refuted
- `/BillOfLading/cbc:Description` = `Shipped on board.` with the issue at 10:54, while the status report `13-TransportationStatus.xml` reports the loading at 16:05 and the departure at 18:10: suspected a shipped-on-board bill issued before loading — refuted because no example gives the loading time; loading can have taken place before 10:54 and the status report can report it later.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem` (one goods item) against `/BillOfLading/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2`: refuted, the goods item contains two goods items (1.1 benches, 1.2 frames), which are the shipment's two goods items as in the packing list.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:Stowage/cbc:Location` = `On deck, aft of the bridge` with bay 14: suspected a forward bay described as aft of an aft bridge — refuted because nothing in the flow places the bridge; a feeder with a forward or midship bridge has bay 14 aft of it.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealIssuerTypeCode` = `CARRIER` with `SealingPartyType` `Shipper`: refuted, a carrier-issued seal applied by the shipper at stuffing is common practice for FCL.
