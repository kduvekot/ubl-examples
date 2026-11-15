# Consistency review: items

Run: `20261114T2143Z-consistency` · Review date: 2026-11-15 · Topic: items
Examples: 250 in 18 flows, at commit 9bdf89a (claude/stoic-noether-5pboei); tables current for that commit (extract_tables.py --check: "current (250 examples and the script unchanged)").
Inputs: the XML examples, the extraction tables, the merged per-example reviews. No world data, generators or companion documentation were read. Also read: `analysis/review-merge-decisions.md`, the conditions, timelines and equipment files of this run, the output of `check_consistency.py`, and own knowledge of the HS nomenclature, GS1 rules and timber and steel densities where said.

## What is expected

Every finding below, and every entry under "Considered and refuted", "Leads" and "Cannot be told", is looked into and ends either resolved (its condition holds in the XML) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by the owner first, because the fix changes the world's item master data or story (which lot is where, who numbers an item, what a bench is made of), not only an encoding. This review describes what is inconsistent about the items across documents and flows; it does not say where or how the examples are produced.

## The world as the documents state it

### Item register

Every item of the 224 `cac:Item` aggregates (items.csv), grouped into one physical item wherever two rows share any identifier (seller's, manufacturer's, standard or additional ID); items without any identifier stand alone (the tender's call-for-tenders lines, service lines, the ground anchors, the cotton fund levy). Prices are the line prices of lines.csv with the issuer of the document they stand in (an order is issued by the buyer, so buyer and seller show the same price). Names are the English rendering.

| Item (English name) | Seller's IDs | Manufacturer's ID | Standard ID (scheme) | Additional ID | Buyer's IDs | HS / CPC | Origin | Flows (items) | Prices (issuer of the document: price) |
|---|---|---|---|---|---|---|---|---|---|
| Park bench Serra 180 | BM-551210; LD-10442; VI-B180; VT-PB-180 | VI-B180 | 771020000027 (item); 9520610000012 (GS1 GTIN) | 771020000027 | BM-551210; LD-10442; VT-PB-180 | 940179/38111 | XU | carnet 1, rail 3, retail 19, road 10, sea 10, tender 7 | Brightmarket Stores: 674.1 XBL; Brightmarket Stores: 520 XBL; Lumeway Distribution: 520 XBL; Velumi Trading: 520 XBL; Lumeport Public Works Department: 499 XBL; Lumeway Distribution: 49900 XUF; Valdara Industries: 499 XBL; Valdara Industries: 49900 XUF; Velumi Trading: 289 XLC |
| Bench side frame casting | LD-10443; VI-C180 | VI-C180 | 771020000034 (item); 9520610000029 (GS1 GTIN) | 771020000034 | LD-10443 | 732599/42999 | XU | air 4, retail 1, road 12, sea 10 | Lumeway Distribution: 64 XBL; Velumi Trading: 64 XBL; Lumeway Distribution: 5980 XUF; Valdara Industries: 5980 XUF |
| Garden bench set Marrow | BF-GS-01; BM-551004 | BF-GS-01 | 9523710000012 (GS1 GTIN) | – | BM-551004 | 940169/38112 | XB | furniture 13, retail 1 | Brackenmere Furniture: 610 XBL; Brightmarket Stores: 610 XBL; Robin Ashdale: 899 XBL |
| Ground anchor set | – | – | – | – | – | – | – | tender 11 | – |
| Cotton lint, compressed bale | SCG-LINT | – | – | – | LT-RAW-COT | 520100/01921 | XL | cotton 7 | Lumeport Textile Mill: 0.988 XLC; Selanu Cotton Ginnery: 0.988 XLC |
| Park bench, 1800 mm | – | – | – | – | – | – | – | tender 7 | – |
| Hardwood bench slat 1800 | MS-SL-1800 | – | – | – | VI-R-SL1800 | 440799/31102 | XB | wood 7 | Marrowdale Sawmill: 7.2 XBL; Valdara Industries: 7.2 XBL |
| Cotton shirt | BM-778120; LT-SH-01 | LT-SH-01 | 772030000090 (item); 9522610000016 (GS1 GTIN) | 772030000090 | BM-778120 | 620520/28232 | XB | packaging 5 | Brightmarket Stores: 11.98 XLC; Brightmarket Stores: 29.95 XBL; Brightmarket Stores: 14.5 XBL; Lumeport Textile Mill: 14.5 XBL |
| Recycled PE granulate | RR-PE-R1 | – | 771030000048 (item) | – | – | 390110/34710 | XU | plastics 5 | Rinova Recovery: 83200 XUF; Rivermouth Packaging: 83200 XUF |
| Seed cotton | LCF-SC | – | – | – | – | 520100/01921 | XL | cotton 4 | Selanu Cotton Ginnery: 0.03 XLC; Selanu Cotton Ginnery: 0.226 XLC |
| Natural gas | KG-NG | – | 772060000015 (item) | – | – | 271121/12020 | XB | energy 4 | Kelpstone Gas: 3600 XUF |
| Lithium-ion battery pack 48 V 100 Ah | SE-BAT-48100 | – | – | – | – | 850760/46420 | XB | mast 4 | Saltmere Engineering: 2400 XBL; Selanu Telecom: 2400 XBL |
| Ionisation smoke detector set | SE-SMK-10 | – | – | – | – | 853110/46921 | XB | mast 4 | Saltmere Engineering: 180 XBL; Selanu Telecom: 180 XBL |
| Coating stripper for electronics | SE-CS-05 | – | – | – | – | 381400/35110 | XB | mast 4 | Saltmere Engineering: 9.5 XBL; Selanu Telecom: 9.5 XBL |
| Park bench Serra 180 | – | – | – | – | – | – | – | retail 1, sea 1, tender 2 | – |
| Garden bench Marrow, 1400 mm | BF-GS-01-B | – | – | – | – | – | – | furniture 3 | Brackenmere Furniture: 380 XBL; Brightmarket Stores: 380 XBL |
| Garden chair Marrow | BF-GS-01-C | – | – | – | – | – | – | furniture 3 | Brackenmere Furniture: 115 XBL; Brightmarket Stores: 115 XBL |
| Iron ore, lump | SM-ORE-L | – | 771010000013 (item) | – | – | 260111/14100 | XU | ore 3 | Serravona Mining: 8060 XUF; Valdara Industries: 8060 XUF |
| Installation of a park bench | – | – | – | – | – | – | – | tender 3 | – |
| Installation of a park bench | VI-INST-B | – | – | – | – | – | – | tender 3 | Valdara Industries: 18 XBL |
| Sewage levy of the city of Lumeport | CSW-LEVY | – | – | – | – | – | – | utilities 3 | Coastal State Water Company: 0.42 XBL |
| Drinking water | CW-M3 | – | – | – | – | – | – | utilities 3 | Coastal State Water Company: 2.35 XBL |
| Cotton fund levy | – | – | – | – | – | – | – | cotton 2 | – |
| Sea freight, 40-foot container | BF-SEA40 | – | – | – | – | – | – | cotton 1, sea 1 | Bayforth Forwarding: 2950 XBL |
| Electricity network use | FG-NET-E | – | – | – | – | – | – | energy 2 | Ferrano Grid: 6.2 XUF |
| Office desk | BF-DK-16 | – | 9523710000029 (GS1 GTIN) | – | – | 940330/38122 | XB | furniture 2 | Brackenmere Furniture: 880 XBL; Lumeport Public Works Department: 880 XBL |
| Installation work | BF-INST | – | – | – | – | – | – | furniture 2 | Brackenmere Furniture: 48 XBL; Lumeport Public Works Department: 48 XBL |
| Recycled stretch film | RP-SF-23 | – | 772040000103 (item) | – | – | 392010/36330 | XB | packaging 2 | Rivermouth Packaging: 3.1 XBL; Valdara Industries: 3.1 XBL |
| Garment bag | RP-GB-60 | – | 772040000110 (item) | – | – | 392321/36410 | XB | packaging 2 | Lumeport Textile Mill: 0.08 XBL; Rivermouth Packaging: 0.08 XBL |
| Park bench Brackenmere PB-2 | – | – | – | – | – | – | – | tender 2 | – |
| Electricity | FE-KWH | – | – | – | – | – | – | utilities 2 | Ferrano Energy: 27.3 XUF |
| Hardwood timber | MS-TB | – | – | – | – | 440799/31102 | XB | wood 2 | Brackenmere Furniture: 540 XBL; Marrowdale Sawmill: 540 XBL |
| Air freight | BF-AIR | – | – | – | – | – | – | air 1 | Bayforth Forwarding: 6.8 XBL |
| Gas network use | FG-NET-G | – | – | – | – | – | – | energy 1 | Ferrano Grid: 1.9 XUF |
| Electricity, wholesale | MB-MWH | – | – | – | – | – | – | energy 1 | Montebrio Power: 9800 XUF |
| Care kit for the garden bench set | – | – | – | – | – | – | – | furniture 1 | – |
| Return transport | BM-SVC-RT | – | – | – | – | – | – | furniture 1 | Brackenmere Furniture: 85 XBL |
| Rail freight, ore in bulk wagons | FRC-ORE | – | – | – | – | – | – | ore 1 | Ferrano Rail Cargo: 962 XUF |
| River freight, bulk | FB-BULK | – | – | – | – | – | – | plastics 1 | Fiumella Barges: 1495 XUF |
| Rail freight, container slot | FRC-CTR | – | – | – | – | – | – | rail 1 | Ferrano Rail Cargo: 54600 XUF |
| Bench side frame casting | – | – | – | – | – | – | – | retail 1 | – |
| Road transport in Bayvarra | BF-ROAD | – | – | – | – | – | – | retail 1 | Bayforth Forwarding: 2.85 XBL |
| Road transport, full truck load | TH-FTL | – | – | – | – | – | – | road 1 | Trasvia Haulage: 240.5 XUF |
| Export customs clearance | BF-CLR | – | – | – | – | – | – | sea 1 | Bayforth Forwarding: 85 XBL |
| Cargo insurance | BF-INS | – | – | – | – | – | – | sea 1 | Bayforth Forwarding: 140 XBL |
| Container storage at the port of Selanu | – | – | – | – | – | – | – | sea 1 | – |
| Customs inspection of container TWLU4120872 | – | – | – | – | – | – | – | sea 1 | – |
| Customs inspection fee | – | – | – | – | – | – | – | sea 1 | – |
| Storage at the port | – | – | – | – | – | – | – | sea 1 | – |
| Fixing bolt M12 | – | – | – | – | – | – | – | tender 1 | – |
| Side frames of the bench | – | – | – | – | – | – | – | tender 1 | – |
| Penalty for late installation | – | – | – | – | – | – | – | tender 1 | – |
| Natural gas supply | FE-GAS | – | – | – | – | – | – | utilities 1 | Ferrano Energy: 8.4 XUF |
| Business telephone line | ST-BL | – | – | – | – | – | – | utilities 1 | Selanu Telecom: 21.18 XLC |
| Mobile data | ST-GB | – | – | – | – | – | – | utilities 1 | Selanu Telecom: 0.424 XLC |
| Collection and recovery of production waste | RR-SVC-01 | – | – | – | – | – | – | waste 1 | Rinova Recovery: 12350 XUF |
| Hardwood bench slat 1800 × 95 × 35 | – | – | – | – | – | – | – | wood 1 | – |
| Oak bench slat 1800 | – | – | – | – | – | – | – | wood 1 | – |

Canonical description of the two items that travel through most flows (the same in every document that carries the full description, apart from the language tag of the English rendering):
- **Park bench Serra 180** (brand Valdara, model Serra 180): 1800 mm over the armrests × 620 × 780 mm, seat height 450 mm (440–460), frame of cast and hot-dip galvanised steel in Ferro grey (`GRY`; moss green `GRN` as a variant in retail/08 only), five kiln-dried hardwood slats, three seats, load capacity 450 kg (test `UR-SF-0450`), four ground anchors and bolts, five years' warranty on the frame, HS 940179 / Urvanian tariff 94017910, CPC 38111, origin XU, 96 kg CO2e cradle to gate, 34 kg steel and 22.5 kg hardwood consumed, 0.4 kg packaging waste, data sheet `VI-DS-B180`, repair manual `VI-RM-B180`. Gross 41.5 kg per bench in every flow that ships it (road, rail, sea, tender, carnet). Seller's IDs: `VI-B180` (Valdara), `LD-10442` (Lumeway), `BM-551210` (Brightmarket), `VT-PB-180` (Velumi).
- **Bench side frame casting** (model "Serra 180 side frame"): HS 732599, CPC 42999, origin XU, gross 10.2 kg per casting (road, sea, air), serial numbers `VI-SF-…`, melt `M-26-0412` (timelines#F2). Seller's IDs `VI-C180` (Valdara, with extended IDs `2025`/`2026` in road/02) and `LD-10443` (Lumeway).

Prices along the chain (XBL; 1 XBL = 100 XUF = 0.4 XLC, conditions register):

| Item | Manufacturer → distributor | Manufacturer → public buyer | Distributor → retailer / importer | Retailer → consumer |
|---|---|---|---|---|
| Serra 180 bench | Valdara → Lumeway 49900 XUF = 499.00 (road/15, rail/11) | Valdara → department 499.00 (tender/32) | Lumeway → Brightmarket 520.00 (retail/18), → Velumi 520.00 (sea/22) | Brightmarket 674.10 (retail/21), Velumi 289.000 XLC = 722.50 (sea/29) |
| Side frame | Valdara → Lumeway 5980 XUF = 59.80 (road/15) | — | Lumeway → Velumi 64.00 (sea/22, air/01); revised list 58.00 (retail/03) | — |
| Garden bench set Marrow | — | — | Brackenmere → Brightmarket 610.00 (furniture/09) | Brightmarket 899.00 (retail/22) |
| Cotton shirt | — | — | Textile Mill → Brightmarket 14.50 (packaging/07) | Brightmarket 29.95 (packaging/08), 11.980 XLC = 29.95 (packaging/09) |

The margins that are odd (distributor price equal to the public price, frame resold below cost) are conditions#F11; the rest are positive and plausible.

## Known from the per-example reviews

| Problem | Decision already made (severity, needs decision) | Cross-flow extent |
|---|---|---|
| Bench emission triple: 96 kg, factor 0.82, base 1 EA | High, no | 39 files in carnet, rail, retail, road, sea, tender (`grep -l 'ValueFactorNumeric>0.82<'`); the same triple in every flow that carries the bench |
| `FullnessIndicationCode` `CRADLETOGATE`; `LifecycleStageCode` MANUFACTURING with a cradle-to-gate text | Medium, no | the same 39 files |
| Catalogue and product-passport data (circularity, properties, emissions, warranty, dimensions) copied into business documents | Low, no | the full bench description stands in the same 39 files of 6 flows, also in customs declarations, despatch advices and invoices |
| Side frame classified HS 732599 instead of 9401.99 (part of a seat) | Medium, no | every frame item: road (Valdara), sea, air, retail (Lumeway), 22 files; both sellers use the same code, so the fix is one master-data change |
| World item numbers (`771…`, `772…`) are valid GTIN-12s; GTINs in Lumeway's GS1 company prefix | Low, yes | 8 world item numbers in 64 files of 11 flows; Lumeway's prefix `9520610` on Valdara's bench and frame (items#F2) |
| Benches described as assembled that do not fit pallet, trailer or container | Low–Medium, yes | dimensions 1800 × 620 × 780 mm wherever the bench is fully described; no document says the bench ships knocked down; equipment#F1 depends on it |
| English renderings tagged after the issuing country (`en-XB`/`en-XU`/`en-XL`), Urvanian or Lisavan rendering first | Low, yes | item names and descriptions follow the same rule as the party addresses (parties Known table): bench `en-XU` in 13 items, `en-XB` in 7; PE granulate `en-XU` 3, `en-XB` 2; cotton lint `en-XL` 3, `en-XB` 4 |
| One melt, one coating batch and serials against manufacture dates | High, no (timelines#F2) | not repeated here |

## Findings

### items#F1 · High · The sea export names the March road import as the goods' previous declaration, but the benches and castings it exports were made in May
- XPath: `sea/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`
- XPath: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`
- XPath: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-03-24`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `VI-LOT-260320`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `VI-LOT-260510`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-05-10`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01230`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01490`
- Why: sea/11 is Lumeway's export of 96 benches and 12 castings from Bayvarra to Lisavu (issued 2026-05-12). Its previous customs declaration is road/10, Lumeway's import of 96 benches and 12 castings from Urvania on 2026-03-24, i.e. the declaration under which the exported goods entered Bayvarra. But the goods themselves, as sea/20 identifies them, are lot `VI-LOT-260510`, made 2026-05-10, and castings `VI-SF-01230`… made the same day; the goods of road/10 are lot `VI-LOT-260320` and castings `VI-SF-01490`… (road/04). Goods made on 10 May cannot have been declared for import on 24 March. The per-example review of sea/11 saw only that `PreviousCustomsDeclaration` is not a previous version of the same declaration (sea/11, finding on the element); timelines#F4 saw that the May lots reach Lumeway's stock through no document. Together they contradict each other: the identifiers on the goods say "made in May, not yet imported", the customs reference says "imported in March". The castings show the same: 12 castings imported by road (serials `VI-SF-01490`…), 12 castings exported by sea with serials `VI-SF-01230`… that road/10 never covered.
- Condition: the declaration that sea/11 cites as the goods' previous customs declaration covers the lot and serial numbers that sea/20 despatches; or sea/11 cites no previous declaration and the May lots are imported into Bayvarra by a documented declaration.
- Options: (a) preferred: decide the stock story of timelines#F4 first; if the sea goods come from the March import, give sea/20 (and air/06, air/08, retail/12) the March lot and serials; (b) if they are new production, add or cite their own import declaration and drop the reference to road/10.
- Needs decision: yes
- Seen in reviews: sea/11 (the element's meaning); timelines#F4 (the lots); leads sea/20 (132)

### items#F2 · Low · The bench and its side frame have a different "standard" identity depending on who sells them
- XPath: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `road/15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `road/15-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000034`
- XPath: `sea/22-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `sea/22-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `sea/22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- XPath: `sea/22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- XPath: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:BrandName` = `Valdara`
- Why: in Valdara's documents (carnet, rail, road, tender: 29 items) the bench and the frame carry the world item numbers `771020000027` and `771020000034` as `StandardItemIdentification`; in Lumeway's documents (air, retail, sea: 32 items) the same items carry GTINs in Lumeway's own GS1 prefix `9520610` as standard identification and the world item numbers as `AdditionalItemIdentification` (item_ids.csv). Both are valid uses of the elements, and the identification convention per party is part of the world (CLAUDE.md: GS1 / ISO via Codana / own numbers), so this is not a contradiction. But the result is that one physical item has two standard identifiers, and the GTIN is assigned by the distributor to an item whose brand owner is Valdara (brand `Valdara` in every document): under GS1 rules the brand owner allocates the GTIN (own knowledge), and Valdara, which has no GS1 prefix in the world, never uses it. The merge decision on GTINs in Lumeway's prefix (Low, needs decision) was made per example; across flows it concerns two items in 61 item occurrences.
- Condition: every item has one standard identification that all its sellers use, or the world states which party's scheme is standard and why a distributor's GTIN identifies a manufacturer's branded item.
- Options: (a) the world item number as the one standard ID everywhere and Lumeway's GTIN as additional; (b) a GTIN allocated by Valdara (a GS1 prefix of its own) used by both; (c) keep it and state the rule (distributor-assigned GTINs for imported brands). Preferred (a), because it leaves the party conventions intact and needs no new prefix.
- Needs decision: yes
- Seen in reviews: merge decision "World item numbers … GTINs in Lumeway's GS1 company prefix"

### items#F3 · Low · The bench weighs less than its parts as other flows ship them
- XPath: `road/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:GrossWeightMeasure` = `3984`   (96 benches: 41.5 kg each)
- XPath: `road/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:GrossWeightMeasure` = `122.4`   (12 side frames: 10.2 kg each)
- XPath: `wood/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21600`
- XPath: `wood/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800`   (4.5 kg per slat)
- XPath: `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- Why: the per-example reviews (rail/06, retail/02, tender/29) compared the consumption of 34 kg steel + 22.5 kg hardwood with the 41.5 kg gross per bench and refuted the difference, because consumption may include production losses. The cross-flow view takes that argument away for the wood: the sawmill ships the bench slats at 21600 kg / 4800 = 4.5 kg each (wood/05, wood/07; 1800 × 95 × 38 mm at about 690 kg/m³, plausible for kiln-dried hardwood, own knowledge), and five of them are exactly the 22.5 kg of hardwood "consumed" per bench: the wood consumption is the wood in the bench. The remaining 41.5 − 22.5 = 19.0 kg (gross, with film and straps of 0.4 kg and a share of the pallet) must hold the whole steel frame, four ground anchors and the bolts, while one spare side frame alone ships at 10.2 kg gross (road/05, sea/10, air). If the bench has two side frames, as a bench of this design normally has (own knowledge; the documents do not say), frames and slats alone come to 2 × 10.2 + 22.5 = 42.9 kg, above the bench's 41.5 kg; and 34 kg of steel against at most about 19 kg in the product would be a casting loss of over 40 %. No single number is impossible, but the four statements (bench gross, slat weight, frame weight, material consumption) cannot all be true of one bench.
- Condition: the bench's gross weight per unit is at least the weight of its parts as shipped elsewhere (slats, side frames, anchors) less their own packaging, and the steel consumption is consistent with the steel in the bench plus a stated or plausible loss.
- Options: (a) preferred: raise the bench's gross weight to fit its parts (e.g. about 50 kg) in every flow that ships it, with the consignment and container weights that follow (equipment register); (b) lighter slats or frames in the wood and road flows; (c) state the number of side frames and the casting yield, if the figures are meant as they are.
- Needs decision: yes
- Seen in reviews: rail/06, retail/02, tender/29 (refuted there as single-flow comparisons); equipment "Checked and consistent" (41.5 kg in every flow)

### items#F4 · Low · `VI-C180-2026` replaces the side frame in Lumeway's catalogue and the whole bench in Valdara's tender
- XPath: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `tender/15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `road/01-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000034`
- Why: `ReplacementRelatedItem` is "an item that may replace this item". In retail/02 the item replaced is the side frame casting (catalogue line 2), in tender/15 it is the park bench (tender line 1). The value is the seller's ID of the side frame `VI-C180` joined to the extended ID `2026` that road/02 gives the 2026 casting; no document identifies an item by `VI-C180-2026` (item_ids.csv), so the receiver cannot resolve it, and across flows it stands for a frame in one place and a bench replacement in the other. tender/15#F17 found that nothing describes the item; that it means another thing in retail is new.
- Condition: an item identifier used as a replacement means the same item in every document, it is identified somewhere the receiver can see (an item ID with its scheme), and it replaces an item of the same kind.
- Options: (a) preferred: drop the replacement from the tender line (a side frame does not replace a bench) and identify the 2026 casting in retail/02 by `VI-C180` with extended ID `2026` or by its own item number; (b) if a 2026 bench model is meant in tender/15, give it its own identifier.
- Needs decision: no
- Seen in reviews: tender/15#F17; lead retail/02 (79)

## Mechanical hits

Group 3 of `check_consistency.py` (same item main identifier, different values; 10 hits):
- name and description of `SellersItemIdentification=VI-B180`, `RR-PE-R1`, `SCG-LINT`: the English rendering tagged `en-XU`/`en-XB`/`en-XL` after the issuing country: known (Known table, language tags); one `VI-B180` variant in road/02 has only the English name, untagged: a difference within one example, left to road/02.
- name and description of `SellersItemIdentification=VI-C180` (5 name variants, 2 description variants): the substitute lines of road/02 (`…, 2025, from stock`, `…, 2026`) and the language renderings: intended (substitution), the rest known.
- name and description of `SellersItemIdentification=LD-10442`: the moss green buyer-proposed substitute in retail/08 (extended ID `GRN`) and retail/04's new slat wood ("another kiln-dried hardwood"): intended; that retail/04 changes only the text is retail/04's own Medium finding.

Group 1 hits on items (7, same identifier with different names): the same items in other renderings or substitute lines; see the identifiers file, "Mechanical hits".

## Checked and consistent

- Prices and units of the same item from the same seller agree in every document (lines.csv, 283 lines; also conditions "Checked"), and every order, response, invoice and credit note of one sale uses the same price and base quantity.
- Price chain: every resale price is above the purchase price except conditions#F11's frame; retail mark-ups: bench 520 → 674.10 (+30 %) and 722.50 (+39 %), garden set 610 → 899 (+47 %), shirt 14.50 → 29.95 (+107 %, plausible for apparel).
- Item data of the bench, frame, slat, PE granulate, cotton lint and shirt: identical names, brands, models, classification codes (HS with Urvanian tariff code, CPC 2.1), origin, dimensions, properties and warranty in every document that carries them, apart from the language tags (items.csv grouped by main identifier).
- Gross weights per unit across flows: 41.5 kg per bench in road, rail, sea, tender and carnet (3984/96, 7968/192, 1660/40, 83/2); 10.2 kg per frame in road, sea and air; 4.5 kg per slat in wood (export and import); 120 t of PE granulate in 120 bags of 1 t with 480 kg packaging (plastics/05, 06, 09); cotton 6129 kg net, 6190.29 kg gross in cotton/10, 11, 15.
- Production capacity against what is shipped: Valdara states 4000 benches a year (tender/13) and buys 4800 slats = 960 benches (wood/03); it ships 96 + 192 + 40 + 2 = 330 benches in road, rail, tender and carnet between March and May: within capacity. (The 6000 benches of tender/12 against the 4000 of tender/13 are tender/12#F15, tender/13#F11.)
- Variants: colour told apart by `SellersItemIdentification/ExtendedID` (`GRY`, `GRN`) and `PhysicalAttribute` the same way in every flow; the garden set's parts (`BF-GS-01-B`, `-C`) consistently as separate seller's IDs.
- Buyer's and seller's IDs per party: Lumeway's `LD-10442`/`LD-10443` appear as buyer's IDs in Valdara's documents (road, rail) and as seller's IDs in its own (retail, sea, air); Brightmarket's `BM-551210`, `BM-551004`, `BM-778120` likewise; Velumi's `VT-PB-180`; Valdara's `VI-R-SL1800` for the sawmill's slat. No ID changes its kind between flows other than as buyer/seller of the same party.
- Lots and serials of the same item across flows: one lot per production date (`VI-LOT-260320`, `260327`, `260426`, `260510`); the melt, coating batch and serial order are timelines#F2.

## Considered and refuted

- Slat length 1800 mm against the bench's 1800 mm "over the armrests": slats flush with the outer faces of the side frames fit; not a contradiction.
- `771020000027` as standard ID in one flow and additional ID in another (group 1): both element uses are valid; the issue is F2 (two standard identities), not a kind confusion.
- Lumeway's bench description "The manufacturer's Serra bench, from the distributor's stock." against Valdara's technical description: a distributor's catalogue text; not a contradiction.
- Velumi's consumer price 289.000 XLC (722.50 XBL) above Brightmarket's 674.10 XBL: different countries and costs (sea freight, insurance, import); plausible.
- Item names in the Urvanian rendering in Bayvarran buyers' orders (road/01, plastics/01): the buyer copies the seller's item master data; part of the language-tag rule, not a separate problem.

## Leads from the per-example reviews

All 221 "Outside this review" entries of the 250 merged files were read (numbering of the timelines file). Entries on this topic:

| Source (entry) | Entry in short | Outcome |
|---|---|---|
| ore/07 (67) | the same item number `771010000013` in ore/01 and ore/04 | known (world item numbers as GTIN-12, Known table); the ore item has it as standard ID in every ore document: consistent |
| retail/02 (79) | `VI-C180-2026` replaces the whole bench in tender/15 but the frame here | F4 |
| road/01 (90) | emission, lifecycle, fullness, item-number and catalogue data recur in 04–15 | known (Known table); extent counted over all flows |
| road/02 (92), road/16 (109) | later documents identify the frame as `VI-C180` without extended ID `2026`; "line 2 matched the substituted casting" | per-example (road/04, road/13#F18, road/15#F13); within road |
| retail/17 (85), retail/19 (87) | what the four packages per pallet of retail/12 are | per-example (retail/12, retail/17#F12); the cartons are not described in any flow; equipment#F1 for the pallets |
| tender/23 (175) | Brackenmere's warranty five years on the line, six in the criterion response | per-example (tender/19#F3); within tender |
| tender/24 (178) | "ten years of warranty on the coating" against the tender | per-example (tender/15, tender/21); the frame's warranty is five years in every other flow, the coating warranty appears only in tender: nothing contradicts across flows |
| utilities/05 (200) | the same "Maximum flow" property in utilities/08 | per-example (utilities/08); within utilities |
| equipment "For other topics" | the bench is described as assembled in every flow | Known table (merge decision on benches that do not fit) |
| timelines "For other topics" | one coating batch `ZN-26-114` for lots of 20 March to 10 May | timelines#F2 (its condition covers the coating batch); not repeated |

## Cannot be told from the documents

1. How many side frames does a Serra 180 bench have, and does it ship assembled or knocked down? (F3, equipment#F1)
2. Which lot did Lumeway export to Lisavu in May, and under which declaration did it enter Bayvarra? (F1, timelines#F4)
3. Who is meant to allocate the standard item identifier in the world: the brand owner, or each seller under its own convention? (F2)
4. What is `VI-C180-2026`: a 2026 version of the side frame, or something else? (F4)
5. Are the steel consumption (34 kg) and the 96 kg CO2e per bench meant per finished bench or per bench including the casting yield? (F3)

## For other topics

- Equipment: if the bench's gross weight changes (F3), the consignment, container and VGM weights of road, rail, sea and tender change with it.
- Timelines: F1 is a further consequence of timelines#F4 (the May lots).
