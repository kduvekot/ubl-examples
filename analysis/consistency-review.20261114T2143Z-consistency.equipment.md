# Consistency review: equipment

Run: `20261114T2143Z-consistency` · Review date: 2026-11-14 · Topic: equipment
Examples: 250 in 18 flows, at commit c41ed3c (claude/stoic-noether-5pboei); tables rebuilt from the same commit (README of `.review/tables`: "examples changed against the commit: no").
Inputs: the XML examples, the extraction tables, the merged per-example reviews, `analysis/review-merge-decisions.md`, the finished conditions review of this run (for its notes to this topic), the output of `check_consistency.py` (group 1), and own knowledge of ISO 6346 containers, pallets, trucks, ships and aircraft where stated. No world data, generators or companion documentation were read.

## What is expected

Every finding below, and every entry under "Considered and refuted", "Leads" and "Cannot be told", is looked into and ends either resolved (its condition holds in the XML) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by the owner first, because the fix changes the story of the world (how goods are packed and carried, which vehicle or route), not only an encoding. This review describes where physical objects are inconsistent across documents and flows; it does not say where or how the examples are produced.

## The world as the documents state it

### Register of physical objects

Every vehicle, vessel, train, wagon, aircraft, container, ULD, identified handling unit, seal, meter, pipeline and named crew member in the 250 examples (from `transport_means.csv`, `transport_equipment.csv`, `handling_units.csv`, `contacts.csv`, the meter rows of the generic tables, and a text search for vehicles named only in notes), with the documents that name it, where and when they place it, and its stated properties.

| Object | Identity and stated properties | Documents | Where and when |
|---|---|---|---|
| Vessel `Tidewell Harbour` | `XB-S-20117` (world vessel scheme), call sign `QBTH7`, MMSI `298702117`, flag XB, feeder, GT 9940, NT 5120, segregated ballast 2480 t, registry `REG-XB-S-20117`, crew 14 (sea/15), owner/operator Tidewell Ocean Lines; voyage `TH-26-19E`, direction EB, service `TWL-ISL` | sea/14, 15, 16 (sea/13, 17 name the voyage's port events, not the vessel) | Port call Lumeport 2026-05-13 → 05-14; bunkering from the port's barge at the Lumeport anchorage 05-13 05:40–08:15; container loaded 05-14, departure 05-14 18:10; 40 nm off Selanu 05-16 15:38 at 13.5 kn; ballast exchange 05-16 "120 nm west of Selanu"; arrival Selanu 05-18 06:30, discharge 11:20 |
| Vessel `Tidewell Reef` | `XB-S-20231`, call sign `QBTR4`, MMSI `298702231`, flag XB, feeder, GT 7480, NT 3910, ballast 1900 t; voyage `TR-26-09W`, direction WB | cotton/14 (cotton/13 names no vessel) | Pre-arrival report for Lumeport issued 2026-03-03 11:22; no times of loading, departure or arrival |
| Barge `Fiumella IV` | `XU-IW-08042`, call sign `QUBF4`, MMSI `297801042`, flag XU, dry barge, GT 1210, NT 860, registry port Ferrano; journey `FB4-26-031`, direction DS | plastics/04, 06 | Quay of Rinova Recovery, Ferrano: takeover 2026-04-19 09:00, loading 13:30, despatch 15:10; exit 04-20 16:00; River quay, Lumeport: discharge 04-22 08:00 |
| Bunker barge of the Port of Lumeport | not identified | sea/16 | Alongside at the Lumeport anchorage 2026-05-13 05:40–08:15 |
| Aircraft `QL-KXA` | XL aircraft register, type `ATF` (IATA SSIM), operator Kelaro Air Cargo | air/04 (flight `KXL207`), mast/03 (flight `KXL209`) | KXL207 Lumeport airport `XBLMA` → Selanu airport `XLSLA`, requested 2026-05-14 07:00–10:00; KXL209: no date or airports (mast/03#F5), waybill issued 2026-06-04 17:15 at the Lumeport terminal |
| Train `FRC 4417` | journey `CT 4471`, direction WB, flag XU, Ferrano Rail Cargo | rail/03, 04, 05, 08 | Ferrano Intermodal Hub departure 2026-04-14 06:52 → rail border 13:20 → Lumeway's siding, Marrowdale 2026-04-15 11:00 |
| Wagon `31 46 4521 042-3` | XU rail-vehicle register, type RR | rail/08 (container 1 only; container 2 has no wagon) | On train FRC 4417, 2026-04-14/15 |
| Ore train | "30 wagons of about 60 tonnes" (ore/04), not identified | ore/02–05 | Serravona mine siding → Valdara, Ferrano; despatched 2026-03-10; arrival not stated |
| Truck `UR 4160 KT` + trailer `UR 4160 TR` | XU vehicle register, type 395 (truck with trailer), loading length 13.6 m, owner Trasvia Haulage; driver Ilario Bencetti; trailer seals `XU-CL-77310` (remark) | road/08 (also road/09 tracking) | Castrano warehouse, Ferrano: pickup 2026-03-23 15:05, departure 16:20; border 03-24 07:30–08:55; rest night Marrowdale; delivered Lumeway 03-25 09:40 |
| Truck `BV LP 2203` + trailer `BV TR 0817` | XB vehicle register, type 395, loading length 13.6 m, Bayforth Forwarding | retail/12 | Lumeway Marrowdale → Brightmarket, Lumeport: "on its way" 2026-04-29 11:49 (Marrowdale ring road), received 04-30 |
| Container truck `BV LP 2205` + chassis `BV CH 0412` | XB vehicle register, type 37 (truck, container), Bayforth Forwarding; chassis also as equipment attached to the container | sea/14 | Drop-off of the container at the Port of Lumeport 2026-05-13 10:15; the chassis is still attached to the container in the shipped-on-board bill (sea/14#F8) |
| Other road vehicles | not identified: three farm trailer loads (cotton/03), the farm's own trailer (sea/29), Trasvia's vehicles in wood, tender, waste and packaging, the tender lorry (tender/29) | — | dates in the timelines review |
| Container `TWLU4120872` | ISO 6346 (check digit correct), 42G1, tare 3750 kg, gross 7856.4 kg, VGM `VGM-26-0510` 7856.4 kg weighed 2026-05-12 15:30 on `LD-SCALE-03`, seal `TWL-S-0884213` (carrier seal applied by the shipper), stowage 140282 on deck aft of the bridge, supplied by Tidewell Ocean Lines | sea/10, 13, 14, 15, 17; sea/28 as a reference | Weighed 05-12; dropped off and accepted at Lumeport 05-13 10:15, stored from 10:30; loaded 05-14; on board to Selanu; discharged 05-18 11:20, event 11:40, detention 12:00, released after the pallet-mark check 15:00; held in port storage 05-18 → 05-19 (sea/28); return not documented |
| Container `TWLU4123110` | ISO 6346 (check digit correct), tare 3750 kg, gross 9940.29 kg, "40-foot" (cotton/17), no size type | cotton/12 (cotton/17 by description) | Port of Selanu weighing, issued 2026-03-01; the bill of lading names no container (cotton/13#F2) |
| Containers `FRXU1044175`, `FRXU1044180` | ISO 6346 (check digits correct), 45G1, gross 7884 kg each, `FRXU1044175` gross volume 76.3 m³, length 12192 mm, "steel, high cube, wooden floor", dent in the left panel, owner and provider Ferrano Rail Cargo, operator Ferrano Intermodal Hub, seals `XU-VI-30411`, `XU-VI-30412` (shipper) | rail/06, 08; rail/09 (`FRXU1044175` only) | Positioned 2026-04-12 08:00, picked up at Castrano 04-13 15:00, at the hub (stack C) 18:30, loaded 04-14 05:40, delivered at Marrowdale 04-15 11:00; "return empty to the Ferrano hub within five days" |
| ULD `RKN41207K0` | type AM (refrigerated ULD), product 5–35 °C, dangerous goods approved, position MD-2 "Main deck, accessible" | mast/02, 03 | Flight KXL209, date not stated |
| ULD `AKE20514K0` | type UL, dangerous goods approved, position MD-6 | mast/02, 03 | Flight KXL209 |
| Pallets of the sea shipment | 25 SSCCs `095206101230000018` … `095206101230000254` (24 bench pallets of 4, one castings pallet of 12) | sea/14 (sea/10 counts 25; sea/28 cites `095206101230000070`) | In `TWLU4120872` |
| Pallets of the road shipment | 25 SSCCs `KXU104411490000015` … `KXU104411490000251`; bench pallets 1850 × 650 × 1650 mm, castings pallet 1200 × 800 × 900 mm | road/08 | On `UR 4160 TR` |
| Pallets of the retail shipment | 6 SSCCs `095206102170000014` … `095206102170000069` | retail/12; retail/17 cites `095206102170000038` | On `BV TR 0817` |
| Air skid | SSCC `095206103190000015`, box 800 × 300 × 300 mm with 8 castings | air/03 | Flight KXL207 |
| Package in the rail itinerary | `KXU104413250000013` | rail/09 only | — (rail/09#F4) |
| Meters | `FG-G-20417` gas (constant 1), `FE-M-881204` electricity (constant 40), `FE-M-881377` electricity, `CSW-W-55102` water, `CSW-W-71844` water | energy/01, utilities/01, 03, 05, 08 (and utilities/11's meter test) | One reading period each, 2026-02-28 → 2026-03-31 |
| Pipeline | Kelpstone gas from field `33/03` through the plant on the north coast to Urvania, journey `KG-P1-2603` (March 2026) | energy/04, 05 (quantities also energy/06, 07) | "measured at the border station" |
| Crew of `Tidewell Harbour` | master Corin Halvard; chief officer, security officer and medical officer Elsbeth Marrin; chief engineer Rafe Dunmore; passenger Ines Tavari | sea/15, 16 | On board 2026-05-14 → 05-18 |
| Master of `Tidewell Reef` | Hester Calloway | cotton/14 | Voyage TR-26-09W, early March |
| Skipper of `Fiumella IV` | Tomaso Riverra | plastics/04, 06 | 2026-04-19 → 04-22 |
| Driver of `UR 4160 KT` | Ilario Bencetti | road/08 | 2026-03-23 → 03-25 |

### Register of places and legs

Places as the documents identify them (UN/LOCODE where given), with the coordinates the documents state, and every leg with the times, distances and durations the documents give. Distances from coordinates are great-circle distances recalculated in this review.

| Place | Identifier | Coordinates stated | Documents |
|---|---|---|---|
| Port of Lumeport | `XBLMP` | 40°1.20′ S 15°12.60′ W (also given for the "Lumeport anchorage") | sea/13, 14, 15, 16; cotton/14 |
| Port of Selanu | `XLSEL` | 40°1.20′ S 15°8.40′ W | cotton/12; sea/14, 15, 16, 17 |
| Lumeport airport | `XBLMA` | 39°59.40′ S 15°16.20′ W | air/04, 05 |
| Selanu airport | `XLSLA` | none | air/04 |
| Ferrano (Castrano warehouse, Intermodal Hub, Rinova quay) | `XUFER` | none | road, rail, plastics, tender, wood |
| Marrowdale (Lumeway, Lumeway's siding, sawmill) | `XBMRW` | none | road, rail, retail, wood |
| Serravona mine siding | `XUSRV` | 39°54.00′ S 15°30.60′ W | ore |
| Kelpstone gas plant / field 33/03 | — | 39°52.80′ S 15°18.00′ W / 39°49.80′ S 15°16.20′ W | energy/04–09 |
| Lisavu Cotton Farm | — | 39°58.80′ S 15°7.80′ W | cotton/01–06, sea/29 |
| Land border Urvania–Bayvarra (road) | none | none; customs posts "Urvanian side" (road, tender, carnet) and "Bayvarran side" (wood) | road/05, 09, 10; tender/30, 31; wood/05, 07 |
| Rail border station Urvania–Bayvarra | none | none | rail/02, 06 |
| River border | none | none | plastics/05, 09 |

| Leg | Mode, means | Documents | Times stated | Distance or duration stated | From coordinates |
|---|---|---|---|---|---|
| Ferrano → Marrowdale | road, `UR 4160 KT` | road/03, 08, 09, 14 | 2026-03-23 16:20 → 03-25 09:40 (border 03-24 07:30–08:55) | 186 km loaded (road/14) | — |
| Ferrano hub → Marrowdale siding | rail, `FRC 4417` | rail/03, 05, 07, 08 | 2026-04-14 06:52 → 04-15 11:00 (border 13:20) | none | — |
| Marrowdale → Ferrano | road, Trasvia | wood/04–07 | despatch 2026-02-26 (08:31 advice) → import clearance 02-27 11:05 | none | — |
| Ferrano → Lumeport depot | road, lorry | tender/29–31 | despatch 2026-03-30 (17:37 advice) → import 03-31 11:14 | none | — |
| Ferrano quay → Lumeport river quay | inland waterway, `Fiumella IV` | plastics/04, 06 | 2026-04-19 15:10 → 04-22 08:00 | estimated transit 3 days | — |
| Serravona mine → Ferrano | rail, ore train | ore/02–05 | despatch 2026-03-10, arrival not stated | window 03-10 → 03-13 | Ferrano not located |
| Marrowdale → Lumeport store | road, `BV LP 2203` | retail/11–17 | "on its way" 2026-04-29 11:49, expected 14:00, received 04-30 | 38 km loaded (retail/16) | — |
| Marrowdale (Lumeway) → Port of Lumeport | road, `BV LP 2205` | sea/14, 20 | despatch advice 2026-05-13 08:52, drop-off 10:15 | none | — |
| Lumeport → Selanu | sea, `Tidewell Harbour` | sea/08, 13–17 | 2026-05-14 18:10 → 05-18 06:30 | "two days at sea" (sea/08); 64 h estimated (sea/15) | 6.0 km (3.2 nm) |
| Selanu → Lumeport | sea, `Tidewell Reef` | cotton/13, 14 | none | none | 6.0 km |
| Lumeport airport → Selanu airport | air, `QL-KXA` KXL207 | air/04, 05, 09 | requested 2026-05-14 07:00 → 10:00 | 3 h | Selanu airport not located; 11.6 km to the Port of Selanu |
| Lumeport → Selanu (mast) | air, `QL-KXA` KXL209 | mast/03 | none | none | — |
| Kelpstone field → plant | pipeline | energy/04–07 | — | "four kilometres out" | 6.1 km |
| Kelpstone plant → Urvania | pipeline | energy/04, 05 | March 2026 | — | — |

The scale contradiction between the coordinates and the stated distances and durations is timelines#F1; the different durations of the Lumeport–Selanu crossing are timelines#F5.

## Findings

### equipment#F1 · Medium · The same load of 24 bench pallets and a castings pallet is "one full truck" and "one 40-foot container", but fits neither on the pallet size the road waybill states
- XPath: `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[1]/cbc:Measure` = `1850`   (length; width `650`, height `1650` mm; the same for pallets 1–24)
- XPath: `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[1]/cbc:Measure` = `1200`   (castings pallet 1200 × 800 × 900 mm)
- XPath: `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MeasurementDimension/cbc:Measure` = `13.6`   (loading length, m)
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `24 pallets of 4 benches: one full truck.`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `One 40-foot container: 24 pallets of 4 benches.`
- XPath: `sea/10-PackingList.xml:/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:SizeTypeCode` = `42G1`
- XPath: `rail/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:SizeTypeCode` = `45G1`
- XPath: `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `192`   (in two full containers: 96 benches, 24 pallets each)
- Why: the bench is sold everywhere by the pallet of four (`PAL-4` in retail/02 and sea/02, "Pallet of 4" in tender/15, 17, 19) and only road/08 states the pallet's size. With it, single layer (the pallets are 1.65 m high; two layers need 3.30 m, more than the inside height of a 42G1, about 2.39 m, a 45G1, about 2.70 m, or a curtain-side trailer, about 2.70 m; own knowledge of ISO 668 and EU trailers): a 13.6 m × 2.45 m trailer floor takes at most 22 bench pallets (seven rows of three lengthwise, 7 × 1.85 = 12.95 m, plus one crosswise row of one, 0.65 m), with no room left for the 1.2 × 0.8 m castings pallet; a 40-foot container floor, about 12.03 m × 2.35 m, takes at most 19 (six rows of three, 11.10 m, plus one crosswise, 0.65 m). The documents put 24 + 1 pallets on the trailer (road), 24 + 1 in the 42G1 (sea) and 24 in each 45G1 (rail, 192 benches in two containers). By floor area alone the trailer would hold them (25 pallets = 29.8 m² of 33.3 m²), which is why the per-example reviews disagreed in severity; by geometry none of the three holds the load. road/08#F12 found the trailer, rail/06#F15 and rail/08#F16 the rail containers by volume; the sea container was not checked, and the cross-flow view shows that the same packing unit is used for three different holds with the same count.
- Condition: for each of the three holds (13.6 m trailer, 42G1, 45G1) the number of bench pallets the documents load is at most what the stated pallet size allows, or the documents state a pallet size, a stacking or a knocked-down packing that makes the stated count fit.
- Options: (a) preferred: ship the benches knocked down (frames and slats in flat packs), state the flat-pack pallet size wherever pallets are measured, and keep the counts, because the counts, weights and invoices of five flows rest on "24 pallets of 4" and the merge decision already names this direction; (b) keep assembled benches and reduce the load per hold (at most 22 on the trailer, 19 in a container), which changes quantities, invoices and receipts in road, sea and rail.
- Needs decision: yes
- Seen in reviews: road/08#F12, road/08#F17, road/08#F28, rail/06#F15, rail/08#F16, sea/05#F1; merge decision "Benches that do not fit pallet, trailer or container when assembled"

## Checked and consistent

- One place at a time: no vehicle, vessel, aircraft, wagon, container, ULD or handling unit appears on two journeys that overlap in time. The only objects named in more than one flow are the aircraft `QL-KXA` (air 2026-05-14, mast with no date but a waybill of 2026-06-04: no overlap) and the vessel operator Tidewell Ocean Lines with two different ships (cotton in March, sea in May). Bayforth's trucks `BV LP 2203` (retail, 04-29/30) and `BV LP 2205` (sea, 05-13) are different vehicles on different days; Trasvia's named truck runs only in road (03-23/25), and its other legs (wood 02-26/27, tender 03-30/31, waste around 04-02) do not overlap with it or with each other.
- Each move starts where the previous one ended, where documents state both ends: `TWLU4120872` weighed (05-12) → dropped off and accepted at Lumeport (05-13) → loaded (05-14) → discharged at Selanu (05-18) → port storage (05-18/19); `FRXU1044175` positioned (04-12) → picked up at Castrano (04-13 15:00) → hub stack C (18:30) → loaded (04-14 05:40) → delivered at Marrowdale (04-15 11:00); `Fiumella IV` takeover → loading → exit → discharge; `UR 4160 KT` pickup → departure → border → Marrowdale → delivery.
- Same object, same description: `Tidewell Harbour` has the same identifiers, tonnages, ballast capacity and configuration in sea/14, 15 and 16; `Fiumella IV` the same in plastics/04 and 06; train `FRC 4417` and journey `CT 4471` the same in rail/03, 04, 05, 08; `TWLU4120872` has tare 3750 kg and gross 7856.4 kg in sea/10, 14 and 15, size type 42G1 and seal `TWL-S-0884213` in sea/14 and 15 (sea/10, 13 and 17 give fewer properties, none contradicting; this is the only equipment hit of `check_consistency.py` group 1, the other group-1 transport-means hits group empty identifiers); the rail containers have the same size type, gross weight, seals and consignment in rail/06 and 08; the ULDs the same type, temperatures and positions in mast/02 and 03. All four ISO 6346 container numbers have correct check digits (`check_ids.py`).
- Directions: voyage `TH-26-19E` EB Lumeport → Selanu and `TR-26-09W` WB Selanu → Lumeport agree with the coordinates (Lumeport lies west of Selanu).
- Gross weights per unit, across flows: 41.5 kg per bench gross in every flow that ships benches (road/05 and sea/10 goods item 1: 3984 kg / 96; rail: 7968 kg / 192; retail: 996 kg / 24; tender: 1660 kg / 40) and 10.2 kg per casting (road and sea goods item 2: 122.4 kg / 12; air: 81.6 kg / 8). Container gross = cargo + tare: sea 4106.4 + 3750 = 7856.4 kg (= VGM); cotton 6190.29 + 3750 = 9940.29 kg; rail 3984 + 3900 = 7884 kg (the 45G1 tare is not stated; 3.9 t is a usual tare for a steel high cube, own knowledge). The shipments' gross weights that leave out the equipment are the per-example findings under the merge decision "Shipment GrossWeightMeasure without the transport equipment".
- Continuity of goods within the flows: sea 4106.4 kg gross, 3762 kg net, 25 pallets, 96 benches and 12 castings in sea/06, 09–12, 14, 15, 19, 20 and 21 (received 96 benches and 11 castings, one casting rejected; the damage in sea/21, 26, 28); road the same figures and 108 packages (24 × 4 + 12) in road/03–10; rail 7968 kg in rail/02, 03, 06, 08; cotton 6129 kg net (27 bales of 227 kg) and 6190.29 kg gross in cotton/09, 11, 13, 15, 16; plastics 120480 kg in plastics/03–09; wood 21600 kg in wood/04–07; tender 1660 kg in tender/29–31. The sea pallet `095206101230000070` cited in sea/28 is pallet 7 of sea/14; the retail pallet `095206102170000038` of retail/17 is pallet 3 of retail/12.
- Capacity where it follows from the documents: the 42G1 carries 4.1 t cargo, the 45G1 4.0 t, far below their payloads (about 26–28 t, own knowledge); `Fiumella IV` (GT 1210) carries 120.5 t, well inside the deadweight of a barge that size (own knowledge: some 1500 t); the ore train carries 1788.4 t on 30 wagons, 59.6 t per wagon against "about 60 tonnes" (ore/04); the tender's 10 pallets (40 benches) and the retail's 6 pallets need 12.0 m² and 7.2 m² of a trailer floor; the air skid (81.6 kg) and the mast ULDs (376 kg) are far below what any freighter carries.
- Seals: `XU-VI-30411`/`30412` identical in rail/06 and 08; `TWL-S-0884213` identical in sea/14 and 15; the road trailer's seal is named in the remark of road/08 and photographed in road/09 (its structured absence is road/08#F26).
- Crews and drivers: every named person is on one vehicle or vessel only; the master (Corin Halvard) and chief officer (Elsbeth Marrin) are the same in sea/15 and 16; the crew size 14 is stated once (sea/15) and the partial crew lists are per-example (sea/15#F7, sea/16#F15).
- Meters: each meter has one reading period; delivered quantity = latest − previous reading (× 40 for `FE-M-881204`): 1350 m³ (`FG-G-20417`), 412800 kWh, 18600 kWh, 86 m³; the gas conversion 1350 m³ → 61200 kWh is recalculated in energy/01's review; the same quantities are billed in energy/02 (412800, 18600, 61200 kWh) and utilities/02.
- Pipeline balance: Kelpstone's export declaration (39200 MWh, 2940000 kg) equals the two invoices (36800 MWh to Montebrio Power, energy/06, plus 2400 MWh to Ferrano Energy, energy/07) at 75 kg/MWh (39200 × 75 = 2940000; 36800 × 75 = 2760000, the import declaration's weight). The import declaration covers only Montebrio's 36800 MWh; the 2400 MWh have no import declaration (energy/04#F1, F2; 05#F1; 07#F1 stand; the arithmetic shows the export covers both buyers). Downstream, Ferrano Energy's gas sale to Valdara (61.2 MWh, utilities/02) fits inside its 2400 MWh; Montebrio's 18400 MWh of electricity sold to Ferrano Energy (energy/03) is 50 % of its 36800 MWh of gas, a plausible efficiency for a gas-fired plant (own knowledge).

## Considered and refuted

- Two transport means with the same empty identifier (`check_consistency.py` group 1, `transport_means.vessel_id`, `license_plate`, `rail_car_id`, `aircraft_id` with value `''`): refuted; the script groups transport means that lack that identifier, not one object.
- Pallet tare too light (leads tender/29, 30, 31): (4106.4 − 3762) kg / 25 handling units = 13.8 kg per pallet including film, straps and the castings box (road/08, sea/10); tender 1660 kg = 40 × 41.5 kg leaves the pallets inside the same 41.5 kg per bench as everywhere else. Light for a 1.85 m pallet but within one-way pallets (own knowledge: about 8–15 kg); consistent across all flows, so not a contradiction.
- Cotton lot of 6.2 t in a 40-foot container (lead cotton/12): refuted as a capacity problem; the load is far below the box's payload and volume, and the forwarder's invoice (cotton/17) bills exactly one 40-foot container. A smaller box would be cheaper; that is commercial.
- Retailer buys 18400 MWh but its network use is 431.4 MWh (leads energy/02, 03): refuted; energy/02 bills only Valdara's two connections (412800 + 18600 kWh = 431.4 MWh); other customers are not in the documents.
- Container `TWLU4120872` both on the road chassis and on the vessel (sea/14 lists `BV CH 0412` as attached equipment): the contradiction lies inside sea/14 (sea/14#F8); no other document puts the chassis on board.
- Trasvia's vehicles in two flows at once (leads waste/01, waste/02, wood/02, wood/04): refuted at company level (no overlapping dates); vehicles are not named outside road.
- MMSI with MID 297/298 and call signs beginning with Q (lead cotton/14): refuted; no such MID or call-sign series is allocated (merge decision).

## Leads from the per-example reviews

All 221 "Outside this review" entries of the 250 merged files were extracted and read. Entries on this topic:

| Source (entry) | Entry in short | Outcome |
|---|---|---|
| air/10 (14) | waybill volume 0.576 m³ against the package dimensions | per-example (air/03, air/04); nothing cross-flow |
| cotton/12 (36) | bill of lading names no container | per-example (cotton/13#F2); register above |
| cotton/12 (37) | 27 bales in a 40-foot container | refuted |
| cotton/13 (39), cotton/14 (42) | the voyage and the vessel against other flows; WB against the course | checked: `Tidewell Reef` in no other flow; WB agrees with the coordinates; times: cannot be told (timelines file) |
| energy/02 (45), energy/03 (47) | 18400 MWh bought, 431.4 MWh network use | refuted |
| energy/04 (48), energy/05 (49), energy/06 (50, 51), energy/07 (52) | 39200 vs 36800 MWh; 2400 MWh not imported | checked: pipeline balance (per-example findings stand) |
| mast/02 (59), mast/03 (60) | RKN and AKE on an ATR 72 freighter at MD-2 and MD-6 with the other loads of KXL209 | cannot be told |
| ore/02 (62), ore/03 (63) | 30 loaded wagons at the siding within the window; the route | weight per wagon checked; availability and route: cannot be told |
| plastics/09 (74) | Marrowdale office competent for river arrivals at Lumeport | cannot be told |
| retail/21 (89) | whether 26 benches suffice for the promotion | cannot be told |
| sea/19 (131), sea/20 (133) | 4106.4 kg in many documents | checked (continuity); the gross-weight definition is per-example |
| tender/29 (180), tender/30 (185), tender/31 (188) | pallet tare in 1660 kg | refuted |
| tender/29 (182) | 40 benches on 10 pallets in one road vehicle; route | checked (12.0 m² of floor); route: cannot be told |
| tender/30 (184) | which border post lies on the road Ferrano–Lumeport | cannot be told; the documents name one land border with an Urvanian and a Bayvarran post |
| waste/01 (206, 208), waste/02 (210), waste/03 (212) | Trasvia vehicle free; 38.2 t in one road load | vehicle: refuted at company level; load: per-example (waste/01#F5, waste/02#F7); capacity: cannot be told |
| wood/02 (213), wood/04 (214) | 21.6 t on Trasvia's vehicle | cannot be told (no vehicle or capacity stated; within the usual payload of an articulated truck, own knowledge) |

The timeline, map-scale and route entries (2–11, 13, 15, 17, 29, 35, 40, 44, 53, 54, 57, 58, 61, 64, 66, 69, 71–73, 75–77, 81, 83, 84, 88, 91, 93–96, 102–105, 107, 111, 113–127, 130, 132, 134, 136, 140, 141, 143, 149–151, 153, 163, 170, 189, 190, 192, 193, 202–205, 209, 215–219) are in the timelines review; the remaining entries are parties, items, identifiers, money, customs rules or flow composition (listed there).

## Cannot be told from the documents

1. What does the ATR 72 freighter `QL-KXA` carry on flight KXL209, can its main deck take an RKN and an AKE at MD-2 and MD-6 (door size, contour), and is the RKN powered on board? (mast/02, 03)
2. On which wagon does `FRXU1044180` travel (rail/08 gives a wagon only for `FRXU1044175`), and does the wagon type take two 40-foot boxes?
3. Where does `TWLU4120872` go after Selanu, and is it returned empty? Where do the rail containers go after Marrowdale ("return within five days")?
4. Which vehicles carry the wood (21.6 t), the waste (38.2 t), the tender release and the packaging goods, and what are their payloads?
5. Where was `TWLU4120872` weighed on 2026-05-12 (scale `LD-SCALE-03`), and where did the pre-carriage start?
6. Which customs office is competent for goods arriving by river at Lumeport (plastics/09)?
7. How large is a bench pallet in the sea, rail, retail and tender flows (only road/08 states it), and are the benches assembled? (F1)
8. Where are Ferrano, Marrowdale and Selanu airport on the map? (timelines#F1)

## For other topics

- Identifiers: the ULD numbers `RKN41207K0` and `AKE20514K0` end in owner code `K0`; whether `K0` is an assigned IATA airline designator should be checked against the sources.
- Identifiers: the package licence plate `KXU104413250000013` (rail/09) and the road SSCCs `KXU1044114…` use an ISO 15459 issuing-agency prefix not checked against the register (rail/09#F7).
- Items: the bench is described as assembled (1800 mm, five slats) in every flow while its pallet (road/08) cannot hold four assembled benches (road/08#F17); F1 depends on it.
