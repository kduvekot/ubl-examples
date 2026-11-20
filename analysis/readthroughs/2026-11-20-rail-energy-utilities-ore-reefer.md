# Read-through: flows `rail`, `energy`, `utilities`, `ore`, `reefer` (O112/O248), 2026-11-20

Sources read:
- **Story:** note/src/03-world.md (countries/energy paragraphs, history 2007/2011, places, distances, billing, utilities, reefer paragraph, pipelines); world/documents.json (the five flows: text, legs, collaborations, every document's "why" and parties, the cited entries they use); world/parties.json (4-xu, 5-xu, 6-xb, 8-xu, 10-xb, 11-xb, 14-xu, 18-xu, 33-xu, 34-xb, 35-xl, 42-xb, 43-xu, 44-xu, 47-xu, 55-xb, 56-xl, 57-xb, 9-xl and the other parties of these flows, with fleets, desks, hours and "wiki"); world/map.json (routes ore, rail-x, sea, gas, gas-grid; platform, metering station, villages); analysis/place-list.md; world/countries.json (calendars, parities, Bayvarra's states and rates).
- **Decisions:** analysis/worklist-decisions.md (D31, D37, D44, D45, the story lines of these flows, payment and calendar story lines; O64, O78, O128, O129, O135, O137, O194, O197, O204, O205, O212, O214, O219, O235–O240, O242, O244).
- **XML and .md:** all XML and .md of the five flows (no `*.llm-review.*`), and the generator sections in tools/examples_scenarios.py where a finding needed its source.
- **Mechanical checks** run on all of it: ISO 11649 RF check digits (15, all valid); ISO 6346 container check digits (FRXU1044175, FRXU1044180, TWLU5316047, all valid); UIC wagon check digits (all valid); GS1 GTIN/SSCC/GLN check digits (all valid); map leg lengths with `tools/world_map.leg_km`.

The known open points were left out unless inconsistent: event times without offset (O78), and the gas imports on 3 April citing their invoices (energy/05 at 16:55 after energy/06 at 11:25; energy/10 at 15:35 after energy/07 at 15:31: consistent).

---

## Flow `ore`

### What checks out

- **Arithmetic.**
  - Order: 1,800 t × 8,060 = 14,508,000; VAT 2,901,600.
  - Freight (ore/06): 1,788.4 × 962 = 1,720,441; bonus 2 % = 34,409; taxable 1,754,850; VAT 350,970; total 2,105,820.
  - Ore (ore/07): 1,788.4 × 8,060 = 14,414,504; moisture 1.5 % = 216,218; net 14,198,286; VAT 2,839,657; total 17,037,943. The discount amount 340,759 is 2 % of the gross.
  - The remittance (ore/08) pays 17,037,943 on 9 April, the day before the due date.
- **Times.** Departure 10:05 + 159 km at 40 km/h + 0.25 h shunt = 14:18.
  - The despatch advice is sent at 10:20, after departure.
  - The waybill records the arrival at 14:18 and is issued at 14:36.
  - Arrival on 10 March, the first day of the window: the bonus applies (D45).
- **Calendar.**
  - Order Mon 2 March; window Tue 10 to Fri 13 March, after Independence Day on Mon 9 March.
  - Due dates: 9 April is 30 days from the consignment note; 10 April is 30 days from 11 March.
- **References and parties.** All references between documents exist and match, and all parties and roles match documents.json:
  - order 4500042994;
  - consignment 7300043010, shipment 7400004875;
  - plan 9500054926 and standing plan 9500054909;
  - waybill 7200091692;
  - contracts VI-FRC-FW-2026 and SM-VI-SA-2026.
- **Codes.** The call-off is type 226, the delivery term FCA at XUFNT, the commodity HS 260111.
- **Distance.** The leg is 158.7 km on the map, stated as 159 km in ore/05.md.
- **Published text.** No D/O numbers in ore XML.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | ore/01-Order.xml and .md (Delivery/Shipment) | Iron ore in open wagons. Nothing in the story asks for a temperature. | `Delivery/Shipment/GoodsItem/Temperature` with TRANSPORT / **CHILLED**, "Chilled, not frozen". The .md says "The shipment the order asks for: **one reefer**", "**The fruit** of the order", "The wholesaler asks for the fruit to travel chilled". The reefer order's block has landed in the ore order. reefer/01 itself carries no CHILLED, although O238/O240 say it should. | High | `ore()` Order branch in `tools/examples_scenarios.py` (lines ~78–86): move the `Delivery.Shipment` block back to the reefer's Order branch |
| 2 | ore/02-TransportExecutionPlanRequest.md (TransportExecutionPlanDocumentReference/DocumentDescription) | Published text carries no finding IDs. | "How this request updates the standing plan **(F5)**." | Medium | `tools/examples_scenarios.py` ~line 11037, the reason text |
| 3 | ore/01.md (DeliveryTerms/ID) | Published text explains values by the world. | "Stated, because leaving it out would carry no meaning (**UBL rule IND6**)." | Low | `tools/examples_scenarios.py` line 67 |
| 4 | parties.json 4-xu and 14-xu wiki; map.json route `ore` wiki ("Length: about 166 km") | ore/05.md: the train "ran 159 km on the line past Ferrano". D45 story line: 159 km. Place list: leg 158.7 km. | The wikis say the train runs "about 166 km down to the works" (4-xu) and "about 166 km … from the mine siding to the works" (14-xu). 03-world also says the ore line runs about 166 km. Line length and leg length are not told apart, so a reader sees 166 against 159. | Low | parties.json wiki texts of 4-xu and 14-xu (say the line's length, or the leg's 159 km) |
| 5 | ore/02 (AdditionalDocumentReference SM-ASSAY-26-11) | The assay of March's train is SM-ASSAY-26-12, taken at loading on 10 March (ore/07, cited register). | The request of 3 March cites a different assay, "-11", "The assay of the ore lot". No lot is known before loading, and the cited entry only says "Serravona Mining's assay of the ore lot". | Low | `tools/examples_scenarios.py` ~line 11039 and documents.json `cited` SM-ASSAY-26-11: remove it, or describe it as a prior assay with its purpose |
| 6 | ore/07 Invoice Delivery/DeliveryLocation | FCA Fucinalta mine siding: the seller delivers at the siding (order DeliveryTerms XUFNT). | Mine's invoice: Delivery at "Valdara Industries works, Ferrano", 10 March, "Where the goods billed are delivered". | Low | ore/07 branch of `ore()` (use the FCA place) |
| 7 | ore/07.md (InvoiceLine/LineExtensionAmount) | — | "…under the moisture clause of supply agreement **sm-vi-sa-2026**": the ID is lower-cased in running text. | Low | the line-extension reason that lower-cases the allowance reason, in `tools/examples_kit.py` / `build_examples.py` |
| 8 | ore/02, ore/03 ServiceEndTimePeriod/EndDate .md | The window is 10–13 March; the train runs the same day. | "Delivered within three days." This is generic text, as in wood finding 7. | Low | `tools/examples_kit.py` tep/tep_request service-end reason |
| 9 | ore/05.md (Note, WaybillTypeCode, DistributionTypeCode) | NATRAIL: a domestic note "under the national rail carriage law". | Three reasons speak of "the convention" ("the originals the convention prescribes", "The convention the document follows"). The note also lists three originals, but only the consignor's is in DocumentDistribution. | Low | `kit.waybill` reason texts (national law vs convention) |

### Consistent, but worth a second look

- ore/05 IssueLocation is the mine siding, while IssueTime 14:36 follows the delivery at the factory. The IssueDate reason explains it as "made out at the siding, completed at delivery, the receiver's copy". This is coherent (O214) but easy to misread.
- The settlement discount of ore/07 is 2 % of the tax-inclusive amount. Check that this is the world's XU-STD rule everywhere.

---

## Flow `rail`

### What checks out

- **Arithmetic.**
  - Goods: 192 × 39,900 = 7,660,800 (D37). Discount 153,216.
  - Freight: 2 × 54,600 = 109,200 (E/EXPTRANSPORT, O214).
  - Demurrage: 2 × 7,500 = 15,000 in both debit notes; the passed-on note at G/EXP (O212). Discount 300; due Sun 24 May moves to Mon 25 May.
  - Customs value: 7,660,800 ferra = 76,608.00 lume at 1 lume = 100 ferra.
- **Weights.**
  - 10,377.6 kg of goods; each container 5,188.8 + 3,900 tare = 9,088.8 kg; the shipment 18,177.6 kg.
  - 48 pallets of 4 benches, 24 per box.
- **Timeline.**
  - Order Mon 6 April; request Tue 7; plan Wed 8.
  - Pre-carriage on Mon 13 April: two runs, picked up 13:00 and 15:00, stacked 14:00 and 16:00, arrival 15:50, 46 km. This is the place list's 45.7 km.
  - The transit declaration at 16:45 on 13 April comes after the second box, and before the waybill that cites it.
  - On 14 April: loading 05:40 and 05:55; terminal status 06:05; waybill 06:10; status request 06:30; departure 06:52, 7 minutes late, 2 after the estimate; status 06:55.
  - Border station: planned 08:01, estimated 08:08; it is 63 km away (O214).
  - Marrowdale yard about 15:10, 173 km (place list 172.8 km).
  - The import declaration is lodged at 08:20 on 15 April, inside Lumeway's desk hours; the boxes are placed 10:30/11:00.
  - Demurrage: free 16–20 April, charged 21–22 April.
- **Calendar.** 13 April is Upland State Day, and Lumeway issues nothing that day.
- **References.** All references match:
  - LMW-PO-26-0734;
  - FRC-CON-2026-005 with call-off /88;
  - 7000026152, 9500055446, 7800004369, 7200092547;
  - 2026/2732, 2026/1770, 9200001856;
  - LMW-IM-26-0161, which the sea flow cites as the previous declaration.
- **Identifiers.**
  - Train FRC 4417, journey CT 4471, wagons as in the 14-xu fleet, tractor UR 4160 RC.
  - Valdara's invoice numbers 1768, 1769, 1770 on 14 April are in order across flows.
- **Parties and roles.** These match documents.json:
  - 47-xu as network manager;
  - 18-xu as terminal operator;
  - the consignment note type CIM;
  - TransitExporterParty 5-xu, CustomsParty 19-xu.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | rail/02.md and rail/03.md (TransportContract/ID) | Published text carries no finding IDs. | "The framework contract for container slots, in the carrier's numbering, the same in every document **(03#F14)**." | Medium | `tools/examples_scenarios.py` line 1035 |
| 2 | rail/01.md (DeliveryTerms) | Published text explains values by the world. | "…so the order names no carrier (**UBL rule IND6**: the terms say who transports…)". | Low | `tools/examples_scenarios.py` line 1140 |
| 3 | rail/08 Waybill DocumentDistribution ID 2 | Story/.md: one original "travels with the goods to the consignee"; its DistributionType reads "the consignee's original". | The party of that distribution is **Ferrano Intermodal Hub (18-xu)**, not the consignee Lumeway. | Medium | waybill distribution in the rail branch of `tools/examples_scenarios.py` (party for ORIGINALWITHGOODS) |
| 4 | D37 decision text "The delivery gets lot numbers (O64)"; O128 "the lot numbers of the delivery" | The delivery should carry its lots, which later supply the island's 96 benches. | No rail XML carries a lot number or serial range: no LotIdentification in rail/01–14. The flow has no despatch advice that could carry them. | Medium | rail branch of `tools/examples_scenarios.py` (GoodsItem/Item/ItemInstance/LotIdentification in the waybill/transit/import), or record that the lots appear only downstream |
| 5 | parties.json 18-xu wiki ("History") | O214/D37: the hub is in Ferrano, 63 km from the border; 03-world: "the intermodal hub at Ferrano". | "The hub was built as a **border terminal** for the traffic of the Lumeport Trade Accord". map.json route `rail-x` label: "Containers from Ferrano past the **border hub**…". | Low | parties.json 18-xu wiki; map.json `rail-x` label |
| 6 | rail/06 IssueTime 16:45 and .md "the evening before" | D37: lodged "on the evening of 13 April". | 16:45 is late afternoon. | Low | the time value in the rail TransitCustomsDeclaration branch |

### Consistent, but worth a second look

- **Waybill issue.** The waybill is issued at the hub on 14 April at 06:10. The carrier took over the goods at Castrano's warehouse on 13 April at 13:00, the pre-carriage being part of the same contract. Its Note says the consignor's original was "handed over when the carrier took over the goods". Decide whether the note is made out at the warehouse on the 13th.
- **Pre-carriage distance.** The place list puts it at 45.7 km on roads `road`, `waste` and `road-farm`, against 14.8 km straight: a detour factor of **3.08**. The 8-xu wiki says Conciaro is "a village east of Ferrano on the main road to the border", and the hub is "east of the centre" of Ferrano. Check the road laid on the map.
- **Locations under Ferrano's LOCODE.** Castrano's warehouse in Conciaro carries Ferrano's LOCODE XUFER everywhere (documents.json leg, rail/02, 03, 07, 08), and the equipment's LoadingLocation is named "Ferrano". Check whether a village outside the town should carry the town's LOCODE.
- **Debit-note due date.** The carrier's debit note (rail/12) falls due on 14 May, "30 days net from the consignment note". That is only 21 days after the note is issued, for a charge that arose after the consignment note. Check that the framework terms are meant to run from the note for demurrage too.
- **Debit-note numbering.**
  - The debit notes of FRC and Valdara are 9200001856 and 9200000878, plain numeric ranges without the year.
  - Valdara's invoices and its credit note are numbered "2026/NNNN" by Urvania's VAT rule (D24: "an invoice is numbered within the year, and the year is part of the number").
  - Check whether a debit note, also a VAT document, should follow the same rule.
- **Real specification names in published text.** "modelled on the CIM" appears in the rail/08 Name, the WaybillTypeCode name and documents.json texts. D37 decided this, but CLAUDE.md says the world's pages name no real specification.
- **Long border stop.** The train waits about five hours at the border station (08:01 to 13:00: "crew change, brake test, customs' check of the seals"), then stands overnight at Marrowdale yard before the shunt at 10:30. This is coherent, but the story only says the train "arrives on 15 April".
- **Terminal status time.** rail/07's OptionalTakeoverTransportEvent of 17:00, "the evening train", is a carried-over fallback. Fine, if intended.

---

## Flow `energy`

### What checks out

- **Arithmetic.**
  - energy/01 metering: 1,350 m³ × 4.9477 (from 4 bar gauge) = 6,679 m³ × 9.163 kWh/m³ = 61,200 kWh. Network 116,280; VAT 139,536.
  - energy/02: 412,800 × 6.2 + 19,350 × 6.2 + 61,200 × 1.9 − 750 × 6.2 = 2,790,960; VAT 558,192; total 3,349,152; discount 66,983.
  - energy/03: 18,400 MWh × 9,800 = 180,320,000; VAT 36,064,000; total 216,384,000; discount 4,327,680.
  - energy/06 and 07: 36,800 × 3,600 = 132,480,000 and 2,400 × 3,600 = 8,640,000 (36.0 lume a MWh). Surcharges 1,987,200 and 129,600.
  - energy/04 customs values: 1,324,800.00 and 86,400.00 lume. Weights 75 kg a MWh, plausible.
  - energy/05 and 10: VAT 26,496,000 and 1,728,000.
  - energy/08 reminder: 134,467,200; energy/09 remittance on Mon 8 June.
- **Balance (D44).** 36,800 + 2,400 = 39,200 MWh. 18,400 MWh of electricity is 50 % of the gas, about 25 MW on average for a 40 MW station.
- **Due dates.**
  - 2 May (Sat) moves to Mon 4 May for XU payees.
  - 3 May (Sun) moves to **Tue 5 May** for the XB payee, because Mon 4 May is Labour Day in Bayvarra.
- **Places.**
  - The platform at map 78/15 is offshore block 19/03 of 14 km.
  - The plant at 76/39 is about 84 km away: "about 80 kilometres out".
  - The metering station is at 72/52, XB, in the Northern Territory.
  - The pipeline is 207 km (place list 206.6 km).
- **Consistency with utilities.** The consumption figures match utilities/01–03: 412,800 kWh, 19,350 kWh, −750 kWh, 61,200 kWh.
- **Dates in the story.** Founding dates fit the story: Kelpstone 2011-04-01 (gas since 2011), Ferrano Grid 2007-01-02.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | documents.json energy collaborations "Ferrano Grid's network bill **for April** to Ferrano Energy" and "Kelpstone's gas bill **for April** to Montebrio Power"; hence energy/01, 02, 06, 08, 09 .md (ProfileExecutionID) | All five documents bill or remind of **March** (InvoicePeriod 1–31 March, "March 2026", "The invoice for March's gas"). | ProfileExecutionID reason: "…network bill for April…", "…gas bill for April…". | Medium | world/documents.json, flow `energy`, collaborations[0] and [1] `what` |
| 2 | energy/01.md (IssueTime) | Published text carries no finding IDs. | "…before the retail company bills the gas by it **(timelines#F8)**…" | Medium | `tools/examples_scenarios.py` line 12573 |
| 3 | documents.json energy UtilityStatement parties: `"CustomerParty": "33-xu"` | The role list of the document. | energy/01-UtilityStatement.xml has no CustomerParty (Sender 44-xu, Receiver 33-xu, Subscriber 5-xu only). | Low | documents.json doc (or the energy/01 branch, if the role is wanted) |
| 4 | energy/01.md and 02.md (IssueDate) | Meters read 31 March; issued Thu 2 April. 1 April is a working day. | "…the morning after the meters were read". That would be 1 April. | Low | `tools/examples_scenarios.py` ~line 12636 (and the statement's reason) |
| 5 | energy/09.md (TotalPaymentAmount) | The Trade Accord's name is capitalised everywhere. | "Transferred in ferra over the **trade accord's** link." | Low | the remittance reason text in the energy branch |

### Consistent, but worth a second look

- **Settlement period ending on a Sunday.** energy/02's settlement period ends on **Sun 12 April**, and energy/03's on Mon 13 April. This is the same pattern as wood (O254 (4)).
- **Generic-reference article.** Generic-reference reasons say "is the example energy/06, **a** Invoice" (also energy/10 and other flows). This is generator wording.
- **Payment across currencies.** energy/06 and 07: the invoice is in XUF, but the payee account is XBL. The Montebrio remittance (energy/09) pays from an XUF account to the XBL account without stating the conversion. The flow text promises "a reminder across currencies", and the .md of energy/08 says "the currency of the debt".
- **Founding vs registration year.** 03-world and the wikis say Kelpstone sold gas "since 2011", while it registered with Codana only in October 2012. This is consistent: it is a registration date, not a founding date.

---

## Flow `utilities`

### What checks out

- **Electricity (utilities/01–04).**
  - Readings: (1,427.2 − 1,324) × 4000 = 412,800 kWh; 135,850 − 116,500 = 19,350 kWh.
  - The February correction: estimate 117,250 against profile 116,500, so 750 kWh. February used 16,450, not 17,200.
  - Energy tax tiers on 432,150 kWh: 60,000 + 229,290 − 450 = 288,840.
  - VAT base 12,580,140; VAT 2,516,028; total 15,096,168.
  - The statements' supplier splits add up: 21.1 + 6.2 = 27.3.
  - Three-month averages: 405,433 and 17,900 kWh, with their amounts.
  - The remittance on Mon 20 April pays 15,096,168.
- **Water, shop (utilities/05–07).** 86 m³ × 2.35 = 202.10; levy 86 × 0.42 = 36.12; total 238.22; average 82 m³ = 192.70.
- **Household (utilities/08–11).**
  - 170 m³ × 2.35 = 399.50; levy 71.40; heat 6.6 × 92.50 = 610.50; cooling 6.6 × 4 × 1.00 = 26.40; tax 6.5 % of 636.90 = 41.40.
  - Total 1,149.20, less 1,008.00 (12 × 84) = 141.20.
  - Reminder: interest 141.20 × 7 % × 8/365 = 0.22; with the 5.00 fee, 146.42.
  - Credit note: 2 × (2.35 + 0.42) = 5.54, leaving 135.66 (D31, O219).
  - The mandate maximum of 150 covers the balance.
- **Telecom (utilities/12–14).** 6 × 21.18 = 127.08; 31 GB × 0.424 = 13.144; 4 GB × 1.5 = 6.000; 5 % discount of 127.08 = 6.354; total 139.870 (D31).
- **Due dates.** 21 days (TA-UTIL), 23 April for all four bills.
- **Calendar.** Remittances on Mon 20 April (D31 point 7); reminder Fri 1 May, a working day in Bayvarra.
- **References.** All references between documents match.
- **Roles.** The utilities/03 roles match D31 point 4: Receiver 8-xu; Subscriber and Customer 5-xu.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | utilities/02-Invoice.xml PaymentTerms, and .md | A utility bill carries the Accord's terms TA-UTIL, "21 days net from the bill". Its own terms text offers no discount, and no discount percent or settlement period is stated. | `SettlementDiscountAmount` 301,923, "The 2 % discount on the amount payable, if paid in time". The XU-STD discount sits under TA-UTIL terms. | Medium | `tools/examples_scenarios.py` lines 4339–4341 (drop it for TA-UTIL) |
| 2 | utilities/06, 09 and 11 TaxTotal, subtotal O/LEVY, and .md | The city's levy (36.12, 71.40 and 0.84 credited) is category O, "outside the scope". | `TaxSubtotal/TaxableAmount` **0.00** for category O. The .md says "The lines of this category plus the document's charges less its allowances of the category", which would give 36.12 / 71.40 / 0.84. The CollectionInvoiceLine amounts are left out of their own subtotal. | Medium | the tax-subtotal calculation for Collection(Invoice/CreditNote)Line in `tools/examples_kit.py` / `build_examples.py` (or the reason, if the exclusion is meant) |
| 3 | documents.json utilities Invoice 35-xl `why`, shown at the head of utilities/13.md | "The island has no sales tax or VAT, and the invoice **says that no tax applies rather than leaving it out**." | utilities/13-Invoice.xml has no TaxTotal and no ClassifiedTaxCategory at all. Its .md says "Lisavu has no sales tax or value added tax, so no tax is due and **the document has no tax section**." The other island invoices (cotton/16) do the same. | Medium | world/documents.json, utilities Invoice 35-xl `why` (or the XML, if D15 wants a stated O category) |
| 4 | documents.json utilities Invoice 34-xb `why`, the head of utilities/06.md | Published text carries no decision or rule IDs. | "…leaving the tax out would say nothing **(IND6)**." | Medium | world/documents.json line 4470 |
| 5 | utilities/02, 06 and 13 .md (IssueDate) | Issued Thu 2 April. | "The monthly bill, issued on **the first day** of the next month." | Low | `tools/examples_scenarios.py` ~line 4907 |
| 6 | utilities/01 and 03 ConsumptionHistory/Amount and ConsumptionAverage/AverageAmount (inside Ferrano Energy's SupplierConsumption) | The energy supplier's own part is priced at 21.1 a kWh (its ConsumptionLine). | The history amounts are priced at the combined 27.3 (398,400 × 27.3 = 10,876,320 …). The .md says "at the tariff of the bill", inside the energy-only supplier block. | Low | the utility statement builder in `tools/examples_scenarios.py` (history at 21.1, or moved out of the supplier split) |
| 7 | utilities/12-UtilityStatement.xml (call allowance reason) | The Trade Accord's name is capitalised. | "Calls to the **trade accord** countries are included in the subscription". | Low | the telecom statement branch in `tools/examples_scenarios.py` |

### Consistent, but worth a second look

- **Estimates without the heat tax.** The new advance (utilities/08) is 39.24 for water and levy plus 50.88 for heat = 90.12, rounded up to 91.00.
  - The heat part is 6.6 × 92.50 / 12 **without** Coastal State's 6.5 % and without the cooling correction, both of which the settlement bill charges (O219).
  - Last year's 84.00 was built the same way (998.20 a year).
  - These are the owner's O219 figures, but the estimate leaves out a tax the bill charges: with tax the heat part would be about 54.18 a month.
- **One quantity for the whole debit.** MainOnAccountPayment/EstimatedConsumedQuantity holds 170 m³ for a debit that covers water, levy and heat. The .md says why: UBL gives one quantity.
- **Annual statement after the credit note.** The credit note corrects the year to 168 m³. The next year's estimate in utilities/08 (170 m³) is not corrected. That may be intended, because the statement predates the test.
- **Shared .md boilerplate (workshop layer), as in wood:**
  - "as in the OASIS example UBL-RemittanceAdvice-2.0-Example" in utilities/04, 07 and 14;
  - "(UBL 2.5, 2.2.2 Manifest Values)" in utilities/06 and 11.

---

## Flow `reefer`

### What checks out

- **Arithmetic.**
  - Order: 672 × 26 + 224 × 24.5 + 224 × 27 = 29,008.00.
  - Order response: 672 + 280 + 168 = 1,120 cartons = 20 pallets of 56. 17,472 + 6,860 + 4,536 = 28,868.00, which the invoice and remittance repeat.
  - Insured value: 110 % = 31,754.80.
  - Surcharge: 1.5 % = 433.02.
- **Weights.** 19.4 kg a carton gross gives 21,728 kg; with the 4,800 kg tare, 26,528 kg. This is the VGM, method SM2.
- **Customs values.**
  - Export (reefer/05): 28,868 − 4,869.86 (freight 4,400, bunker 400, insurance) = 23,998.14, shared by value.
  - Import (reefer/09): CIP value × 0.4 coral = 11,547.200; consumption tax 10 % = 1,154.720.
- **Timeline.**
  - Order Wed 8 April; response Thu 9 April, valid to Fri 17 April noon. Forwarding is booked on Fri 17 April at 10:40.
  - Inspection and certificate Tue 21 April 11:30; export 14:20.
  - Packing 20–21 April; despatch Wed 22 April 12:05; at the port 17:40. The road leg is 261 km on the map, "about five hours and a half".
  - Bill of lading and invoice Thu 23 April; ETD 18:00; import lodged Fri 24 April at sea.
  - Arrival Sun 26 April 06:40; discharge 08:10, on power 08:25. The status is sent at 07:45 −01:00, which is 08:45 at Selanu.
  - Receipt Mon 27 April; remittance Mon 25 May (due 23 May, a Saturday, moved to Monday).
- **Temperatures.** Log 0.2–0.9 °C, pulp 0.6–0.8 °C, set point 0.5, range 0–1 °C, humidity 90 %, air flow 15 %.
- **Parties and roles.** Parties, roles and legs match documents.json, with the vehicles from the fleets: BV LP 2208 with chassis BV CH 0436 and genset (10-xb); Tidewell Harbour TH-26-17E; Nalevi on-carriage. Express release.
- **Product data.** Class I, grower lots and packing dates as decided (O235, O236, O238–O240, O242).

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | documents.json reefer leg 2 (sea, 16-xb → 16-xl) `"transit_days": 5` | 03-world: Thursday sailing, "off Selanu on the Saturday evening, two days later". 11-xb wiki and the map's `sea` route: "about 48 hours". reefer/07.md: "the fruit is at Selanu in two days". The XML: ETD Thu 18:00, arrival Sun 06:40. | The leg data says 5 days. The despatch advice's estimate of 27 April (22 April + 5) and its "usual transit by sea" seem to rest on it: door to door, not the sea leg. | Medium | world/documents.json reefer legs[1].transit_days (2), and check the despatch-advice estimate that uses it |
| 2 | reefer/01-Order.xml (Delivery) | O238/O240: "Hafefo's order asks for transport 'chilled' as `Temperature/MeasureCode`"; 03-world: "The wholesaler's order asks only that the fruit travel chilled". | reefer/01 has no Temperature at all. The block is in ore/01 instead (see ore finding 1). | High | `tools/examples_scenarios.py`: move the block from `ore()` back to the reefer Order branch |
| 3 | reefer/01.md (IssueDate) | Gala and Packham's are picked in February and March and stored; Granny Smith in April (55-xb wiki, item descriptions). | "Ordered in the **second week of the apple season**, when the cooperative's price list for the island came out." On 8 April the season is two months old. | Low | the reefer Order branch's IssueDate reason |
| 4 | reefer/09 IssueTime 17:32 +00:00 (Fri) and reefer/11 IssueTime 14:27 +00:00; 56-xl contact hours | Hafefo: "Monday to Saturday 05:00–14:00". The customs desk has no hours of its own. reefer/11.md: "on the Monday morning". | Both are issued after the desk closes, and 14:27 is not morning. | Low | the time values in the reefer branch (or Hafefo's hours) |

### Consistent, but worth a second look

- **Payment and conversion.**
  - O242 (internal) says the remittance goes to the cooperative's lume account "**without conversion**".
  - reefer/12 pays 28,868.00 XBL from a **coral** account (PayerFinancialAccount XLC, "kept in the currency of the bank's country"), so the bank converts.
  - 03-world agrees with the XML: "from its account at the Bank of Selanu, which changes its coral".
  - Bring O242's wording into line.
- **Delivery place on the invoice.** reefer/08's Delivery/DeliveryLocation is Hafefo's cold store, while the CIP place and the transfer of risk are the Port of Selanu (the bill of lading's LossRisk: "Risk passes when the reefer is handed to the carrier at Lumeport").
- **Booking before acceptance.** The cooperative books the reefer (reefer/03, 17 April 10:40) "the wholesaler having agreed to the changed mix". No document shows that agreement before the cut-off, which is accepted by design (O236: shown only in the receipt and payment).
- **Granny Smith packed on the inspection day.** The Granny Smith lots are packed on 21 April, the day of the inspection (11:30). The certificate says "inspected at the packhouse before loading". Check whether the sample covered cartons packed after 11:30.
- **Hafefo's number range.** Hafefo uses one range for transactions, orders, declarations and receipts (26-0214, 26-0215, 26-0250, 26-0256); its remittance 26-0127 and payment order 26-0027 are separate. D24 says "per kind of document". Check whether ProfileExecutionIDs and orders share one range.
- **Real specification names.** The reefer .md names real specifications and bodies: the IPPC (reefer/04.md, "the IPPC's model certificate"), "the UNECE standards FFV-50/FFV-51" (reefer/06.md) and "Incoterms 2020" (CIP, every flow). These are decided parallels (O235, O239), but check them against the "no real specification" rule for world pages.
- **Shared .md boilerplate (workshop layer):** "OASIS example UBL-RemittanceAdvice-2.0-Example" in reefer/12.md; "(UBL 2.5, 2.2.2 Manifest Values)" in reefer/08.md.

---

## Across the five flows

- **Published-text leaks:**
  - finding IDs in ore/02.md "(F5)", rail/02.md and rail/03.md "(03#F14)", energy/01.md "(timelines#F8)";
  - rule IDs "UBL rule IND6" in ore/01.md and rail/01.md, and "(IND6)" at the head of utilities/06.md.
- **Lower-cased names in published text:** "trade accord" in energy/09.md and the utilities/12 XML; "sm-vi-sa-2026" in ore/07.md.
- **Boilerplate (wood report, same lines):** "as in the OASIS example …" in ore/08, utilities/04, 07, 14 and reefer/12; "(UBL 2.5, 2.2.2 Manifest Values)" in ore/06, 07, rail/10, 11, energy/02, 03, 06, 07, utilities/06, 11 and reefer/08.
- **Wiki texts of these flows' parties** (25 read) contain no decision numbers, person names, paths or change words. The only stale point is the 18-xu "border terminal" (rail 5).
