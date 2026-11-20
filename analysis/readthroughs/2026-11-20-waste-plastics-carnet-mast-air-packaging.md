# Read-through: flows `waste`, `plastics`, `carnet`, `mast`, `air`, `packaging` (O112/O248), 2026-11-20

Sources read:

- **Story.**
  - note/src/03-world.md: river quay, tax paragraphs, waste law, ATA carnet, timelines, air loading/DG, flight times.
  - world/documents.json: the six flows, their legs and collaborations, and every document's "why".
  - world/parties.json: 5-xu, 6-xb, 7-xu, 9-xl, 10-xb, 12-xl, 13-xu, 15-xu, 17-xb, 17-xl, 19-xl, 20-xu, 20-xl, 26-xb, 27-xb, 35-xl, 40-xb, 41-xb, 46-xu, c-xb, and the referenced cb-xu. This covers "what", "how", desks, fleet, numbering and wiki.
  - world/items.json: granulate-pe, waste-recovery, barge-freight, film-pe, garment-bag, shirt, shirt-r, bench-serra, bench-casting-b, air-freight, battery-pack, smoke-detector, coating-stripper.
  - world/countries.json: the tax blocks of XU, XB and XL.
  - analysis/worklist-decisions.md: D16, D27 calendar, D36, D39, D40, D41, D42; the story lines of these flows; C84 in analysis/worklist.md; O30, O49, O58, O62, O66, O78, O115, O123, O132–O134, O162, O168, O193, O197, O199, O209, O210, O213.
- **XML and .md.** All XML and .md of the six flows (no *.llm-review.*), flattened and read value by value.
- **Generator.** Generator passages in tools/examples_scenarios.py, tools/examples_kit.py and tools/build_examples.py, to locate sources.

Severity: High = breaks a publishing rule or the story's core; Medium = a stated fact or reason contradicts the story or another document; Low = cosmetic, internal-only or borderline.

---

## Flow `waste` (4 documents)

### What checks out

- **Weights.**
  - Gross 38,200 − tare 15,300 = 22,900 kg net. The tare is 7,800 + 7,500 from Trasvia's fleet data.
  - The gross is within the 40 t of `road_rules_accord`.
  - 54 bales × about 424 kg = 22.9 t, as D42 says.
- **Arithmetic.**
  - 22.9 × 12,350 = 282,815; VAT 20 % = 56,563; total 339,378.
  - The 2 % discount is 6,788, from 339,378.
  - The due date 6 May is 30 days after 6 April; the discount period ends 16 April.
- **Calendar.**
  - Notification Mon 23 Mar; acknowledgement Wed 25 Mar; load Thu 2 Apr; invoice Mon 6 Apr (D42).
  - Stream period 1 Apr 2026 – 31 Mar 2027, 12 loads, 275 t.
- **Times of the load.** Despatch 09:35, arrival 10:05, weighed loaded at 10:07 and empty at 10:46, ticket 10:50, report 11:45. All are within the desks' hours (agency 08:00–16:00).
- **Parties and roles.**
  - Every role matches documents.json, and the agency is both receiver and CustomsParty.
  - Trasvia carries the waste-carrier registration XU-ENV-T-2023-0187, and Rinova permit XU-ENV-2024-0311 with R3.
  - The notification type is DOMESTIC.
- **References.**
  - 02 cites 01, 04 and the waste-stream number XU-ENV-WS-2026-04417.
  - 03 cites 02 and 04 by type and date.
  - Shipment and consignment IDs agree between 02 and 04, and the stream has its own shipment ID in 01.
- **Codes.**
  - Waste code 150102, non-hazardous, explained.
  - Packaging BL with steel baling wire.
  - Truck 395 with plates UR 4160 KT / TR, from the fleet.
- **ConsignmentQuantity 12 in 02.** It fits UBL's definition ("Estimated total number of shipments for the Waste Notification").

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| W1 | waste/03-Invoice.md, IssueDate | Load on Thu 2 Apr; Fri 3 Apr is a working day in Urvania (no holiday in the XU table). D42 moved the invoice from Sat 4 Apr to Mon 6 Apr. | "Issued on the next working day after the load." The next working day is Fri 3 Apr; 6 Apr is the second. | Medium | `tools/examples_scenarios.py` l. 3861 (invoice why text), or move the date to 3 Apr |
| W2 | waste/01, 02, 04 .md (ItemClassificationCode reason) | Published world text names no real law or specification (CLAUDE.md, two layers). | "numbered after the European List of Waste" (a real EU legal act; 03-world also says so). | Medium | The WasteCode reason in the generator (`WASTE_CODE` context, `tools/examples_scenarios.py` ~l. 3726) and `tools/codelists.py` l. 132/143 (list descriptions); note/src/03-world.md l. 1629 if the note counts as published |
| W3 | waste/03-Invoice.md, AccountingCostCode | No order exists in this flow; the service runs under the contract VI-WASTE-CONTRACT-26. | "The buyer's cost centre, quoted in its order". | Low | `tools/examples_kit.py` l. 1004, the shared cost-centre reason (same text in plastics/07, plastics/10, air/10, air/11 and others where there is no order) |
| W4 | waste/01 and waste/02 (NotifierParty), Contact | Valdara notifies the waste stream as producer; its desks are customs, despatch, goods-in, logistics, payables, purchasing, receivables, tenders. | The contact is Valdara's "Order desk" (department Sales). The mobile's reason says "The sales desk's mobile number". | Low | Desk choice for the notifier in the waste scenario; `tools/build_examples.py` l. 352 (mobile reason) |

### Consistent, but worth a second look

- **Who carries for whom.**
  - Rinova invoices "Collection at the factory and recovery" (items.json waste-recovery), but the load is carried by Trasvia.
  - No document says whether Trasvia works for Rinova or for Valdara, or who pays it.
  - The flow text says "Trasvia ... brings about 54 bales a load", and Rinova's wiki says "Rinova collects ... whose waste Trasvia brings". The reading that Rinova collects through a subcontracted haulier is implied, not stated.
- **Certificate of recovery 26-0020.** The certificate "to follow" already has a number below the movement's 26-0021. This is fine if Rinova numbers per kind of document, but it is a document not yet issued that holds a number (D24).
- **"Basel Convention Annex IV".** It is the listID of R3, and the .md names "the world's copy of Basel Convention". This is allowed as a real external code list. The story says the Basel procedure does not apply, so check that the two read together.
- **Tax point.** The tax point date is the invoice date (6 Apr) while the service date is 2 Apr. This is consistent with the .md ("due on the invoice date"), but no XU rule in countries.json states it.

---

## Flow `plastics` (12 documents)

### What checks out

- **Arithmetic.**
  - Goods: 120 × 83,200 = 9,984,000 ferra, the same in the order, invoice and remittance. The 2 % discount is 199,680.
  - Freight: 120 × 1,495 = 179,400, exempt with EXPTRANSPORT (D41). Due 20 May = 30 days from the waybill of 20 Apr.
  - Customs value 9,804,600 ferra = 98,046.00 lume at 100:1. The statistics value is 99,840.00.
- **Weights and volumes.**
  - 120 bags × 1,004 kg = 120,480 kg.
  - Gross volume 120 × 1.7 = 204 m³. Net 200 m³ at 0.6 t/m³ (D41 point 3).
  - The bag's height of 1,300 mm is on the bag.
- **CO2e.** 5,400 kWh × 0.268 = 1,447 kg (O209).
- **Calendar.**
  - Catalogue Wed 1 Apr; order Mon 13 Apr (Lumeport is open on Upland State Day); response and request Tue 14 Apr; plan Wed 15 Apr.
  - Loading Mon 20 Apr; invoice Tue 21 Apr; unloading and import Thu 23 Apr; remittance Tue 19 May, before the due date of 21 May.
  - The weekend dates of D41 are moved.
  - Catalogue lead time 5 days, order to loading.
- **Barge timeline.**
  - Takeover 09:00, loaded 13:30, cast off 15:10, waybill 15:26.
  - Exit at the river border on 21 Apr at 13:45, arrival on 22 Apr at about 16:15, unloading on 23 Apr at 08:00 with the morning shift.
  - About 250 km, daylight only, 3 days: as the leg (transit_days 3), 03-world and the Fiumella wiki say.
- **Parties, legs and vehicle.**
  - Fiumella IV (FB-4, XU-IW-08042, QUBF4, MMSI 297…) is from the fleet. Every role matches documents.json.
  - CPT river quay is stated once, in the order; the seller books the barge.
- **Certificate.** CVC-RC-26-0118 is issued by Certovira (cb-xu, XU-R-106192), with 100 % recycled content (O193).
- **Tax treatment.**
  - Granulate: G/EXP.
  - Freight: E/EXPTRANSPORT.
  - Import: no duty under the Accord, criterion P, and no Bayvarran tax at import (sale for manufacture).

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| P1 | plastics/05-ExportCustomsDeclaration.md, IssueTime | Published text carries no finding IDs (CLAUDE.md, two layers). | "... so that customs releases them before the barge leaves **(timelines#F6)**". | High | `tools/examples_scenarios.py` l. 1459–1460 |
| P2 | plastics/05, IssueTime reason | 04/06: the barge took over the bags at 09:00, and loading finished at 13:30. | Declared at 12:40 "Before the bags are loaded". Loading had been under way for hours. | Medium | Same line (time or reason) |
| P3 | plastics/05, DeclaredCustomsValueAmount | D16: Urvania values goods "with freight and insurance to its border". The river border is 105 km below the quay, out of about 250 km (04/06). The plastics invoice says "the price includes the barge to the river quay" and has no separate freight line. | 9,804,600 = the price less the **whole** river freight 179,400. The reason reads "Urvania values the goods with freight and insurance to its border: ... **with less** the river freight after loading, which the seller distinguished from the price". So the Urvanian value is the FOB-quay value, the same as Bayvarra's. The grammar is broken ("with less"). The seller did not distinguish the freight on its own invoice. | Medium | `tools/build_examples.py` `VALUATION["plastics"]` (l. ~2327: `("all", -1794.00 …)` applies to both countries) and the reason builder around l. 2347 |
| P4 | plastics/06, plastics/12 .md; plastics/12 XML | Published world text names no real specification (CEN). | 06.md: CO2e reason "the order of the default factor for diesel in **EN 16258**". 12 XML `EnvironmentalCertificate/Remarks`: "... scheme, which follows **EN 15343:2007**". 12.md issuer reason (from cb-xu "what"): "... follows EN 15343:2007, as industry schemes such as **RecyClass** do". | Medium | `tools/examples_scenarios.py` l. 11173; world/items.json granulate-pe `env_certificate.remarks`; world/parties.json `referenced` cb-xu "what" (O132 put the parallels into world text) |
| P5 | plastics/02-OrderResponse (XML and documents.json "why") | documents.json: "The waste processor confirms the lot and the loading date." | The response is a bare AP with an order reference and no lot or date. The .md intro repeats the why. | Low | world/documents.json doc plastics OrderResponse "why", or add the promised loading date to the response in the generator |
| P6 | plastics/10-Invoice.md | IssueDate reason: "Issued the day after the granulate went on board". | Delivery/Despatch reason: "The invoice is issued on despatch: the day the goods left." The two reasons in the same document contradict each other. The same despatch text appears in mast/05 and packaging/07 (see K1). | Low | The shared despatch-date reason in `tools/examples_kit.py` (invoice builder) |
| P7 | plastics/12-Catalogue .md intro (documents.json "why") | Two layers: a value is explained by the world, not by the project. | "It is numbered after the flow's other documents although it comes first in time." This explains the example's file number (D28), a workshop fact. | Low | world/documents.json plastics/12 "why" (move the remark to `_refs`) |
| P8 | plastics/06, plastics/08 (TraceID, LotNumberID) | D41 point 3: "one lot number, `RR-PE-0416`, in the waybill and the despatch advice". | RR-PE-0417, ManufactureDate 17 Apr (consistent between 06 and 08). | Low (internal) | analysis/worklist-decisions.md D41 text (stale), or the lot day in the generator |

### Consistent, but worth a second look

- **Customs office address for the river import.** plastics/09's CustomsParty has an Upland State address (UL-ADR-479100), although the goods are cleared at the bonded store on the river quay in Lumeport, Coastal State. Check that the office named is the right one.
- **Discount period on a holiday.** plastics/10's discount period ends Fri 1 May, Labour Day in Urvania (the payee's country). Check the "due date on a holiday moves" rule for a discount deadline.
- **Despatch advice out of hours.** plastics/08 is issued at 17:57 by Rinova's Dispatch office (weekdays 08:00–17:00), nearly three hours after the barge cast off.
- **Returnable bags.** plastics/06 says the jumbo bags are returnable ("go back to the recovery plant for reuse"). Nothing in the flow brings them back across the border, and no document covers their return.
- **CMNI.** The waybill's Name is "Inland waterway consignment note under the CMNI", and WaybillTypeCode is CMNI. It names a real convention in published XML. The air waybills do the same with "the Montreal Convention" (see A, mast). Check against the "no real specification" rule; the ATA carnet is the precedent for adopted conventions.
- **Statistics value.** plastics/09's statistics value 99,840.00 is said to be "the invoice value at the border". It is the CPT value at the Lumeport quay.

---

## Flow `carnet` (4 documents)

### What checks out

- **Timeline (D40).**
  - Issued Mon 25 May.
  - Exportation stamped 1 June at Valico Euridice; importation 2 June at Selanu airport; re-exportation 9 June; re-importation 10 June at Valico Euridice.
  - Limit 30 June; request Fri 24 July; reminder Mon 24 Aug (instead of Sun 23 Aug); proof Fri 28 Aug.
  - The reminder's due date of 23 Sep is 30 days later.
- **Counterfoils.**
  - Six counterfoils, unstamped at issue: EXP-1, TRA-1 (in/out), IMP-1, REEXP-1, TRA-2 (in/out), REIMP-1, each with its office.
  - The transit country is XB.
  - The "subsequent entry" office is gone.
- **Value and claim.**
  - 2 × 49,900 = 99,800 ferra = 998 lume = 399.20 coral (2.5 lume to the coral, as in items.json bench-serra-x).
  - Tax 10 % = 39.920; surcharge 10 % = 3.992; total 43.912 coral, "about 44" (D40, 03-world).
- **Weight.** 94 kg = 2 × 47.0. The three parcels per bench are 12.2 + 13.0 + 21.8 kg, as in items.json.
- **Parties.**
  - IssuerParty 20-xu, HolderParty 5-xu, the two guarantors, the two customs parties and RepresentativeParty 5-xu, as documents.json says.
  - "Carnet office" is the contact on both sides.
  - The scan sits on the chamber's own domain (camera-ferrano.example).
- **Procedure code.** 2000 = temporary admission, in the world's list.
- **Missing voucher.** The request's note speaks of a missing voucher, not a missing stamp (D40 02#F4).
- **Legs.** The six legs are as in documents.json: road, air, road, road, air, road, with Trasvia, Kelaro and Nalevi.

### Mismatches

No mismatch between the story and the XML was found in this flow.

### Consistent, but worth a second look

- **Customs record numbers.**
  - Urvania's exportation (1 June) is XU-CUS/2026/39379 and the re-importation (10 June) is 39380. Two consecutive numbers nine days apart, at the road border post that also clears all of Trasvia's trucks.
  - On the island, the customs notice XL-CUS/2026/11199, sent after 30 June, is numbered below the June registrations 12905 (2 June) and 13127 (9 June).
  - If these are one series per office rising with time (D24), they do not fit.
- **IDs in the decision text.** D40's "Built with G2" names the customs records XL-CUS-ATA-26-0049 / -0053 and XU-CUS-EXP-26-0031. The XML has XL-CUS/2026/… and XU-CUS/2026/…. The decision text is stale (internal only).
- **Basis of the claim.** The claim is reckoned "on the declared value" (99,800 ferra, the list price ex works). The island values imports landed, with freight and insurance (D16; countries.json: "customs value plus duty"). Check whether the story wants the guarantee value or a landed value as the base.
- **Validity period.** It runs from 25 May 2026 to 25 May 2027 inclusive, a year and a day. Real carnets end the day before the anniversary.

---

## Flow `mast` (5 documents)

### What checks out

- **Arithmetic.**
  - 12 × 1,200 + 180 + 5 × 9.50 = 14,627.50 lume, the same in the order and the invoice.
  - Surcharge 1.5 % = 219.41.
  - The due date moves from Sat 4 Jul to Mon 6 Jul.
- **Weights.**
  - 12 × 27 + 3 + 5 × 1.35 = 333.75 kg.
  - The batteries are 324 kg gross and 288 kg net.
  - Each crate is within the 35 kg of PI 965 IA on cargo aircraft only; the stripper is under PI 855 CAO (O210).
- **Calendar and flight.**
  - Order Mon 1 June; instructions Wed 3 June.
  - Thu 4 June: truck out 09:40, about an hour to the airport; accepted 11:15 Lumeport time, before the 12:00 cut-off.
  - KXL209 15:00−01:00 → 18:45+00:00, a block of 2 h 45 (O123). Delivery on 5 June, "the next morning", within the requested 4–5 June.
- **Stowage (O210).**
  - Batteries in a net-door AKE at MD-1; the stripper in a net-door AKE at MD-3; MD-2 empty for segregation; the detectors in a closed AKE at MD-6.
  - The ULD IDs are only in the waybill; the instructions state the requirement.
  - This matches documents.json legs, 03-world and the D36 story line.
- **DG data.**
  - UN3480 / 9 / NA; UN2911 / 7 excepted, with no label and the activity "Am-241, 10 × 37 kBq (370 kBq)" in the name; UN2920 / 8 (3) / PG II / flash point 28.
  - ERG guides 147, 161 and 132; emergency line "every day, around the clock" (parties.json desk).
- **Tax and origin.** Export G/EXP; statement of origin criterion S.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| M1 | mast/01, 04, 05 .md (ProfileExecutionID reason) and documents.json collaboration "what" | Selanu Telecom buys back-up batteries, smoke detectors and coating stripper **for** its mast (flow text, D36 story line, Saltmere and Selanu Telecom wikis). | "The collaboration this document belongs to: Selanu Telecom's **order of a mast** from Saltmere Engineering." | Medium | world/documents.json mast collaboration "what" (l. ~1998) |
| M2 | mast/03-Waybill.md, LoadedHazardousItem/NetVolumeMeasure | Two layers: no change words or project history in published text. | "The modules' volume: the same cells as the six larger packs **first planned**." This explains the value by the D36 redesign. | Medium | `tools/examples_scenarios.py` l. 8558 |
| M3 | mast/01-Order (lines) | D36 point 5: "the order and the despatch advice keep the identification (UN number, class, proper shipping name) and the handling instructions". | The order lines carry only `HazardousRiskIndicator` true; there is no HazardousItem (the despatch advice has it). | Low–Medium | `mast()` Order branch in `tools/examples_scenarios.py`, or D36 text if D11/O86 overrode it (record which wins) |
| M4 | mast/05-Invoice (and documents.json "why") | documents.json: "Goods and carriage to the site; an export, so no sales tax." CPT mast site: Saltmere pays the forwarder and the air freight. | Three goods lines only, with no line, charge or note saying the carriage is in the prices (contrast plastics/10's note "the price includes the barge"). | Low | The mast invoice in `tools/examples_scenarios.py` (a note like plastics/10's), or the "why" |

### Consistent, but worth a second look

- **Pallet weight.** The battery handling unit SE-PL-1 is a pallet, but no weight for it enters the 333.75 kg consignment gross weight (goods with packaging) or the ULD load.
- **Out-of-hours and wording.**
  - mast/05 is issued at 17:34 by Saltmere's Accounts receivable (weekdays 08:00–17:00).
  - mast/01's IssueDate reason, "orders before the storm season", has no support in the story.
- **Statement on origin.** Saltmere is an engineering and installation firm, and its invoice declares "Bayvarran preferential origin (criterion S)" for batteries, detectors and stripper. Nothing in the story says it makes them; check whether it may make the statement (it is the "exporter" here, which is fine).
- **Real names in .md texts.**
  - 02 and 04 .md: "as the IMDG Code **no longer** gives medical first aid table numbers". This names a real code and uses a change word, though about the real world.
  - 02 .md (EmergencyProceduresCode): the IMDG Code.
  - 03: "Air waybill under the Montreal Convention".
  - The listIDs "ERG 2024" and "IATA SSIM Aircraft Types".
  - These are code lists or real regimes the world adopts; confirm they are acceptable.
- **Lower case in a reason.** mast/03's LoadedHazardousItem/ID reason reads "The lithium-ion battery module 48 **v** 50 **ah** in the container". The generator lower-cases the item name.
- **Inconsistent flight duration.**
  - 03-world l. 1525 says "about 2 h 10 to 2 h 15 are needed".
  - The D36 story line says "about 2 h 20".
  - O123 says "about 2 h 27 at 1,076 km".
  - The Kelaro wiki says "about 2½ hours".
  - air/09's landing at 10:30 gives 2 h 30.
  - The D27 calendar story line still says "leaves Lumeport at 07:00 and lands in Selanu at 10:00 … two hours in the air" (internal; 03-world l. 1524 already says 10:45).
- **Saltmere described two ways.** Its "what" calls it an "east-coast village" and its wiki an "east-coast town". The "what" also names the architect "Edda Corwin"; check whether "what" is published on the party pages.

---

## Flow `air` (11 documents)

### What checks out

- **Weights and charges.**
  - 8 × 12.2 = 97.6 kg of cartons; with the 7 kg skid, 104.6 kg gross; chargeable 105 kg.
  - Volume 0.52 m³ × 167 = 86.8 kg, below the gross weight.
  - Freight 105 × 6.80 = 714.00 (O162, O213).
  - air/11: 512.00 + 714.00 = 1,226.00, surcharge 18.39; air/10 surcharge 10.71. Both are due Mon 15 June (14 June is a Sunday).
- **Flight story (D39).**
  - Change Mon 11 May; response and instructions 12 May; cast 12 May at 14:15; packed 13 May.
  - Cut-off 12:00; accepted 19:10; waybill 19:15 Lumeport (20:15+00:00); status 19:20; cancellation 19:50, citing LAC-TS-26-13099; replacement 20:05, referring to LMW-DA-26-1017.
  - KXL207 07:00−01:00 → 10:45+00:00; landed 10:30; collection from 12:00 on 14 May.
- **Line and terms.**
  - Order-change line 4: 8 × 64.00, CPT Selanu airport once, "the rest stays CIF".
  - The response has no validity period and promises 13 May at 18:45.
- **Waybill.** It is direct (ConsolidatedIndicator false), with Nalevi as notify party and the transit declaration cited.
- **Castings.** Serials VI-SF-03190…03197 and melt M-26-0094; one manufacture date (D21).
- **Tax.** Bayforth's freight to Lumeway is E/SVCB2B.
- **Legs and parties.** The four legs and all parties are as in documents.json.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| A1 | air/07-FulfilmentCancellation.md, CancellationNote | Published text carries no finding IDs. | "... the flight and the arrival it gave no longer hold **(F7)**." | High | `tools/examples_scenarios.py` l. 5973 |
| A2 | air/04-Waybill.md, ChargeableWeightMeasure | The chargeable weight is 105 kg from the gross 104.6 kg with the skid (O162, O213; 04's own Consignment/GrossWeightMeasure 104.6). | "The gross weight of **97.6 kg**, rounded up to the next half kilogram: it is higher than the volume weight". 97.6 rounds to 98, not 105. air/10.md: "the gross weight of the frame cartons, rounded up" (also without the skid). | Medium | `tools/examples_scenarios.py` l. 2986 (uses `w`, the cartons, instead of `air_gross(f)`); the air/10 line reason |
| A3 | air/06 (IssueTime 12:15), air/05 (acceptance 19:10), air/07, air/08 | 03-world: Marrowdale to Lumeport is about 81 km, and mast/04 says Marrowdale to the airport is "about an hour away". The terminal works around the clock. D39: the truck is late and reaches the terminal after the 12:00 cut-off. | Bayforth's truck leaves the cross-dock at 12:15, already after the cut-off, so it should reach the terminal about 13:15. The terminal accepts at 19:10, about six hours later, and nothing explains the gap. Also, at 12:15 Lumeway still announces KXL209 and an 18:45 arrival, although the cut-off has passed. | Medium | `tools/examples_scenarios.py` l. 2779–2784 (D39 comment, `AIR_CUTOFF`) and l. 3009/3016 (times), or a stated reason in the world (e.g. galvanising late, truck leaves later) |
| A4 | air/01, air/02, air/11 (tax category G/EXP, "An export from Bayvarra", "no tax on an export"); air/03 DeclaredStatisticsValueAmount "The value for the export statistics" | D39 point 2: the frames cross Bayvarra under the Accord's common transit, from Ferrano to Selanu airport, and are "neither imported into Bayvarra nor exported from it". | Lumeway's documents treat the sale as a Bayvarran export, and the forwarding instructions give an export statistics value. This is the same pattern as wood/08 in the earlier read-through: the goods never were in Bayvarra's free circulation. | Medium | The XB tax-category choice for a foreign buyer in `tools/examples_kit.py` (G/EXP branch) for goods in transit; `tools/examples_scenarios.py` l. 2848 (statistics value) |
| A5 | air/11-Invoice Note (statement on origin) | The frames are exported from Urvania by Valdara under Valdara's transit declaration (04: "Valdara's transit declaration ..."). | "The exporter of the goods covered by this document declares that these goods are of Urvanian preferential origin". Lumeway, the issuer, is not the exporter of record. | Low | The origin statement in `tools/examples_kit.py` (~l. 1254) and its reason in `tools/build_examples.py` (~l. 2360); same root as the wood/08 finding |
| A6 | air/04 (DocumentReference ID 7800004419) | D39 "Built with G2": "the transit declaration `VI-TD-26-0513`". | 7800004419 (Valdara's range-style number). | Low (internal) | analysis/worklist-decisions.md D39 text (stale) |
| A7 | air/06, air/08 ManufactureTime reason (items.json `poured_why`) and the melt-number reason | Melt number: "one per casting day, in the foundry's running count" (examples_kit l. 874). | ManufactureTime: "**An extra melt** in the afternoon". An extra melt on a day with one melt contradicts "one per casting day". | Low | world/items.json bench-casting-b `poured_why`, or the melt reason in `tools/examples_kit.py` l. 874 |

### Consistent, but worth a second look

- **Out-of-hours issuing.**
  - air/07 (19:50) and air/08 (20:05) are issued by Lumeway's Sales and Dispatch offices (weekdays 08:00–17:00), and air/10 at 17:03.
  - air/01 at 07:50+00:00 by Velumi's Purchasing desk (Mon–Sat 09:00–18:00).
  - The story needs the evening documents; the desks' hours say otherwise.
- **OrderChange charge.** air/02 says the 714.00 surcharge was quoted "for the eight frame cartons" on 12 May, before the frames were cast and packed. The skid is in the 105 kg; the wording leaves it out.
- **Pricing below cost.** air/11 sells at 64.00 "carriage paid" while the island CIF price is 68.00. O30 notes the air frames are below cost after the freight. Recorded as open (O30, O162); nothing new.

---

## Flow `packaging` (9 documents)

### What checks out

- **Arithmetic.**
  - Film 480 × 3.10 = 1,488.00 (surcharge 22.32); bags 20,000 × 0.08 = 1,600.00 (24.00); shirts 600 × 14.50 = 8,700.00 (130.50).
  - Due dates: 31 May (Sunday) → 1 June; 11 June.
- **Receipts.**
  - 08: 2 × 29.95 − 5.00 = 54.90; tax 6.5 % = 3.57; 58.47 rounded to 58.45; cash 70.00, change 11.55; tax-inclusive price 31.90.
  - 09: 3 × 29.95 = 89.85 lume, tax 5.84; at 2.5 lume to the coral, 11.98 coral a shirt, 35.940 + 2.336 = 38.276 coral.
  - The exchange rate XLC→XBL is 2.5 (multiply).
  - The pair offer is "Friday 22 May only" (C84), and the next day's three shirts are at full price.
- **Weights.** 600 × 0.28 = 168 kg in 20 cartons of 30 (C84; items.json carton note).
- **Calendar.**
  - Orders Mon 27 Apr, Wed 29 Apr and Thu 7 May.
  - Both Rivermouth invoices are on Fri 1 May, a working day in Bayvarra (O78).
  - Despatch and invoice 12 May; receipts Fri 22 May and Sat 23 May (the shop week).
  - O133: the receipt for the Selanu fair is in early June.
- **Tax.**
  - Film to Urvania: G/EXP with a statement of origin, criterion S.
  - Garment bags and shirts: E/RESALE (packaging that goes to the customer; resale).
  - Consumer: S, 6.5 % of Coastal State. This matches countries.json XB.
- **Parties and legs.** Every role is as in documents.json.
  - FCA Rivermouth with Trasvia collecting.
  - DAP mill with Bayforth.
  - DDP store with Bayforth's consignment note.
  - The store's goods-in GLN 9522610900019.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| K1 | packaging/05-Order.md, IssueDate | C84 / G7 (O115, D34): the shirts are "the store's order of shirts for its winter range", no spring. In May (late autumn in the south), spring is wrong. | IssueDate reason: "The store orders shirts **for spring**." The line in the same document says "winter range". | Medium | `tools/examples_scenarios.py` l. 5694 |
| K2 | packaging/07-Invoice.md | Despatch 12 May, expected delivery 13 May (06). | IssueDate reason: "Issued **on delivery**" (12 May). Delivery/Despatch reason: "The invoice is issued **on despatch**". The two disagree, and delivery is 13 May. | Low | `tools/examples_scenarios.py` l. 5716 and the shared despatch reason (see P6) |
| K3 | packaging/02-Invoice, Delivery/DeliveryLocation | Order 01: FCA Rivermouth Packaging, dispatch, Lumeport; the buyer's carrier collects. | "Valdara Industries works, Ferrano" :: "Where the goods billed are delivered". Under FCA the delivery is at the seller's dispatch. | Low–Medium | The packaging invoice builder in `tools/examples_scenarios.py` (`packaging()`), or the kit's default delivery location for FCA |
| K4 | packaging/08-PurchaseReceipt (IssueDate reason, XML) and documents.json | documents.json: "The consumer buys **a shirt**"; collaboration "the store's sale of **a shirt** at the till". | Two shirts with the pair offer (C84), and the .md says "A consumer buys two shirts." | Low | world/documents.json packaging/08 "why" and collaboration "what" |
| K5 | packaging/06-DespatchAdvice.md, CarrierAssignedID | Clear wording. | "its consignment note, consignment note under the national road carriage law, which travels with the truck". The phrase "consignment note" is doubled (the kit's name glued after the text). The value BYF-CR-26-0127 differs from C84's recorded "BF-NATROAD-26-0521" (internal text stale). | Low | `tools/examples_kit.py` l. 1317 (`DOMESTIC_KIND`) and its use in the despatch reason; C84 text in analysis/worklist.md |

### Consistent, but worth a second look

- **Cash receipt with a bank account.** packaging/08 is paid in cash, yet AccountingCustomerParty carries Robin Ashdale's bank account ("from which the bills are paid"). This is party data the document does nothing with (O86).
- **Receipt contact.** packaging/08 and 09: the store's contact on a till receipt is "Accounts receivable"; the point-of-sale contact is separate.
- **PCI DSS.** packaging/09.md (PrimaryAccountNumberID) says "PCI DSS allows at most the first six and the last four". This names a real industry standard in published text; source `tools/examples_kit.py` l. 2312.
- **Requested delivery dates.** packaging/01 asks for delivery 30 Apr – 2 May at Valdara: 1 May is Labour Day in Urvania and 2 May a Saturday, so Valdara's goods-in (office week) is closed on two of the three days. Under FCA the date is really the collection date at Rivermouth.
- **Delivery date the order did not ask for.** packaging/03 asks for 1–3 May (3 May is a Sunday; the mill works weekdays). packaging/04 is issued "on delivery" on 1 May at 08:11. That is consistent, but the morning time is tight.

---

## Points across the six flows

- **Published text that explains by the model or the project (two layers).**
  - The shared invoice reason "(UBL 2.5, 2.2.2 Manifest Values)" appears in every invoice here (waste/03, plastics/07, plastics/10, mast/05, air/10, air/11, packaging/02, 04, 07).
  - plastics/11 has "as in the OASIS example UBL-RemittanceAdvice-2.0-Example".
  - waste/01's intro explains the CustomsParty by UBL's requirement.
  - The mast RadioactiveMaterial reason explains by UBL's definition (O127).
  - The first two were already flagged in the wood read-through; they are listed again because they repeat here.
- **"Quoted in its order" without an order.** The shared cost-centre reason appears on invoices that answer no order: waste/03, plastics/07 (answers a transport plan), air/10 (answers forwarding instructions). Source `tools/examples_kit.py` l. 1004.
- **Times without an offset.**
  - Event times without an offset are frequent in these flows: delivery and despatch times, transport events, ManufactureTime, PickupTime, PurchaseTime, TransactionTime.
  - Already decided (O78); no inconsistency beyond that.
  - The offsets that are given are right everywhere: −01:00 mainland, +00:00 island.
- **Stale identifiers in decision texts (internal only).**
  - D39: VI-TD-26-0513.
  - D40: XL-CUS-ATA-…, XU-CUS-EXP-….
  - D41: RR-PE-0416.
  - C84: BF-NATROAD-26-0521.
  - These no longer match the XML. Renumbering under D24 explains it; the decision texts were not brought along.
