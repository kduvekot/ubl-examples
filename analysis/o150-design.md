# O150: thermal modification as contract processing (design study, read-only)

Date: 2026-11-20. Nothing in the repository was changed. Sources read: `CLAUDE.md`; `analysis/worklist-decisions.md` (O149, O150, O180, O197, O225, O226, O231, D18, D27, D43, the story lines on customs and money, the calendar); `world/examples/wood/*` (XML and .md); `world/documents.json` (flow `wood`); `world/parties.json`; `world/countries.json` (XU tax); `world/codelists/lists.json` (XU/XB exemption reasons, customs declaration subtypes, nature of transaction, life cycle stage); `world/bench/report.md`; `analysis/coverage-register.md` (all 558 rows under "Missing"); `analysis/place-list.md`; and a world model I built in the scratchpad with `tools/world_model.py`, to find a free square. The UBL definitions are quoted from `.ubl/mod/UBL-Entities-2.5.gc`.

Anything marked **(from memory)** is general knowledge that I did not check against a source in this session.

---

## 0. Summary

- **Elements the flow could honestly win: 18 recommended**, plus 2 more if the owner takes the variant of the split delivery, so 20. Another 6 circularity elements fit, but they are not specific to this flow (section 1.3).
- **Why the sawmill outsources: capacity in its season.** The sawmill's single modification kiln is booked with its own decking and cladding through the southern building season (October to March). For those months it buys kiln slots from a plant near Ferrano under a season agreement. For the rest of the year it modifies the ash itself, so O149 stays true as the rule.
- **Customs and VAT in two lines:**
  - The Accord is a free trade area with import VAT at Urvania's border. Inward processing is used to suspend that VAT, not duty: the blanks are owned by a Bayvarran company with no Urvanian VAT number. Valdara releases the finished slats for free circulation and pays import VAT on what it pays for them.
  - The plant's service is supplied to a business established in Bayvarra. It is outside Urvania's VAT (`SVCABROAD`, the real parallel being Article 44 of the EU VAT Directive), and Bayvarra taxes only retail sales.
- **Documents:** 8 new ones in a new flow `modification`, plus an optional remittance advice. In the wood flow, 5 change and 1 goes (section 2e).

---

## 1. Coverage scan

I checked every one of the 558 rows under "Missing" for a case in this flow. Below are the rows that pass, with their definition and case, then the ones that pass only weakly, then the ones I rejected and why. `ImportCustomsDeclaration/ValidityPeriod` is left out as asked. The flow would honestly have it: the period by which the inward processing must be discharged.

### 1.1 Recommended (18)

| # | Element | UBL 2.5 definition | The case in this flow | Strength |
|---|---|---|---|---|
| 1 | `Order/SalesOrderID` | "An identifier for the Order, assigned by the seller." | The plant gives each kiln slot of its season schedule a job number when the season agreement's slots are allotted. The sawmill's processing order (modification/01) quotes the job number of the slot it fills. The seller assigned the number before the order existed. | strong |
| 2 | `OrderChange/SalesOrderID` | "An identifier for the Order Change, assigned by the seller." | The call-off (modification/07) changes the processing order: it adds the delivery to Valdara. It quotes the plant's job number. Caveat: the definition says "for the Order Change"; in practice it is the seller's order number. | good, with the caveat |
| 3 | `LineItem/SubLineItem` | "The subsidiary line items that constitute the main line item, such as in a bill of materials." | The processing order's line is the output, 96 bundles of modified slats. Its sub-line item is the input the customer supplies free of charge, 4,800 ash blanks of 1,830 × 101 × 51 mm. A toll-processing order names the customer's material in exactly this way. | strong |
| 4 | `Despatch/ReleaseID` | "An identifier for the release of the despatch used as security control or cargo control (pick-up)." | The goods are the sawmill's, held in the plant's store. The sawmill issues a pick-up release number, and the plant hands the 96 bundles only to the Trasvia driver who quotes it. The plant's despatch advice (wood/06) records the release the goods left under. | strong |
| 5 | `Consignment/ConsignorAssignedID` | "An identifier for this consignment, assigned by the consignor." | In the transport request wood/04 the sawmill is the transport user and the plant the consignor. The consignment's ID is the sawmill's booking; the plant's own despatch number is a second ID, given by a different party. This element exists for exactly that split. | strong |
| 6 | `InventoryReportLine/AvailabilityDate` | "The date from which the goods will be available. If not present, the goods are available now." | The plant's stock report to the sawmill (modification/06, Friday 30 January): charge 1, 48 bundles, is in store and available now (no date). Charge 2, 48 bundles, is still being planed and is available from Wednesday 4 February. | strong |
| 7 | `Shipment/DeclaredCustomsValueAmount` | "The total declared value for customs purposes of those goods in this shipment that are subject to the same customs procedure and have the same tariff/statistical heading, country information, and duty regime." | The release declaration (wood/07) covers the goods of two inward-processing entries, one per truck of blanks. That makes two goods items under the same heading (4407.95, ash), the same procedure and the same origin. The shipment states their total. This is the definition's grouping, and it is what the register's loss lacked: sea/11 summed two headings. | strong |
| 8 | `Shipment/DeclaredStatisticsValueAmount` | "The value, declared for statistical purposes, of those goods in this shipment that have the same statistical heading." | Under the world's rule for inward processing (section 2c), the customs value is that of the blanks placed under the procedure. The statistics record the processed slats: the blanks plus the processing. That gives two different values, each by its definition. | strong (it needs the valuation rule of 2c) |
| 9 | `GoodsItem/ValueAmount` | "The amount on which a duty, tax, or fee will be assessed." | Import VAT on each released goods item is assessed on the price of the processed slats, not on the customs value of the blanks. The goods item states that base. The register already has a Lisavu candidate for this row in the sea flow; both cases are honest. | strong |
| 10 | `Item/LifecycleStageCode` | "A code indicating the product's lifecycle stage (e.g., sourcing, manufacturing, distribution, usage, end-of-life)" | The item on the plant's invoice (modification/08) is the thermal modification service, `MANUFACTURING` in the world's list `LifecycleStage` (EN 15804 A3). The sawmill needs the plant's stage data for the slat's footprint, which feeds the bench's footprint (O25, O225). | good |
| 11 | `Item/LifecycleStageDescription` | "A text describing the specific environmental impact associated with this product's lifecycle stage." | For example: "Thermal modification at 212 °C in steam: about 0.35 MWh of heat a cubic metre of wood from the plant's boiler fired with its own offcuts, and 0.06 MWh of electricity; the kiln's fumes are burned in its afterburner; no chemicals." The figures are illustrative **(from memory)** and must match the factors in `world/bench/parameters.json`. | good |
| 12 | `Consignment/OfficeOfEntryLocation` | "The customs office or offices indicated in the authorisation as empowered to accept declarations entering goods for the arrangements." | In the inward-processing entry (modification/05): the plant's authorisation names the Urvanian offices that may accept entries for its procedure, the border office at Valico Euridice and the inland office for Ferrano. It is an authorisation term, not the office the declaration goes to. Risk: a reviewer may call it a repeat of the receiving office. To avoid that, list both authorised offices. | borderline, but by its definition |
| 13 | `Party/ServiceProviderParty` | "A party providing a service to this party." | In the sawmill's quotation (wood/02), under `SellerSupplierParty/Party`. The slat is type-tested (UR-SF-0450) and sampled yearly, and its modification is a special process. A buyer's approval of a supplier covers whoever performs such a process, so the sawmill names its processor. A change of processor needs Valdara's consent. | moderate |
| 14 | `ServiceProviderParty/Party` | "The Party who provides this service." | The plant, with its name, register ID and address. | moderate |
| 15 | `ServiceProviderParty/ServiceTypeCode` | "The type of service provided, expressed as a code." | A code such as `PROCESSING` (contract processing). There is no list yet, so a regional one is needed in `lists.json`. | moderate (costs a list) |
| 16 | `ServiceProviderParty/ServiceType` | "The type of service provided, expressed as text." | "Thermal modification at 212 °C, planing to 1,800 × 95 × 45 mm, end-grain sealing, storage and despatch". This is more than the code says. | moderate |
| 17 | `ServiceProviderParty/SellerContact` | "The contact for the Service Provider." | The plant's despatch desk: Valdara's goods-in deals with it on delivery days. | moderate |
| 18 | `OrderChange/DeliveryTerms` | "A set of delivery terms associated with this document." | The call-off sets how the plant hands over the sawmill's goods: loaded at the plant's dock onto the carrier the sawmill names, at the sawmill's risk from loading. The processing order (modification/01) said only "hold in store until called off". | moderate |

### 1.2 Conditional (2): only with the split-delivery variant (owner question Q9)

| # | Element | Definition | Case |
|---|---|---|---|
| 19 | `DespatchLine/OutstandingQuantity` | "The quantity outstanding (which will follow in a later despatch)." | The plant's final inspection rejects 4 bundles with end splits. Modified ash is brittle: its splitting strength falls by 30–40 % (bench report, section 4.4). The despatch of 26 February carries 92 bundles; 4 follow from slats re-cut in the next charge. |
| 20 | `DespatchLine/OutstandingReason` | "The reason for the outstanding quantity." | "4 bundles held back: end splits found in final inspection; replacements follow on 5 March." |

Cost of the variant: one more despatch advice and transport for the 4 bundles, and the invoice and import must split. `DespatchLine/BackorderQuantity` would repeat the outstanding quantity and is not proposed.

### 1.3 Honest, but not specific to this flow (6, not counted)

`CircularityProfile/EndOfLifeTreatment`, `CircularityProfile/RecyclabilityPercent`, `EndOfLifeTreatment/ImpactCode`, `/ProcessingTypeCode`, `/TreatmentLocation`, `/TreatmentPathwayCode`.

The modified slat has a real end-of-life story. It contains no biocide, so it counts as untreated waste wood and goes to energy recovery or particleboard rather than to hazardous-waste treatment **(from memory: the German waste wood ordinance's classes A I/A II against A IV for preservative-treated wood)**. But that is a property of the slat item. The wood flow (or Valdara's bench data) can state it with or without the plant, and the register already gives these rows to packaging or medicines. If they are to be won with the slat, the place is the slat item in `world/items.json`, whoever modifies it.

### 1.4 Weak: not recommended

| Element | Definition | Why not |
|---|---|---|
| `OrderResponse/Contract` | "A contract associated with the Order being responded to." | The processing order would naturally cite the season agreement itself (`Order/Contract`, which is already covered). Stating it again in the response repeats it. It is honest only if the order leaves the contract out, which is less natural. |
| `InvoiceLine/SubInvoiceLine` | "An invoice line subsidiary to this invoice line." | The job, with modification, planing, sealing and storage as sub-lines, could equally be four plain lines. It is defensible, but the reason is thin. |
| `WorkReport/BillingReference` | "A reference to a related billing document." | It would need a kiln-charge work report issued after a billing document, for example a slot reservation fee billed in advance. That is invented complexity. |
| `Delivery/ReleaseID` | "An identifier used for approval of access to delivery locations (e.g., port terminals)." | The O150 note read it as a call-off. By its definition it is a gate-access approval. Neither the plant's yard nor Valdara's goods-in has controlled access that the world states. |
| `CustomerParty/AdditionalAccountID` | "An identifier for the customer's account, assigned by a third party." | Valdara's account number at the sawmill, printed on the plant's despatch advice: the case is too thin. |
| `RemittanceAdvice/PayerReference` | "An internal reference to the payer's order for payment." | Honest in the sawmill's remittance to the plant, but just as honest in any remittance. It is not this flow's case. |

### 1.5 Rejected

- `OrderReference/CustomerReference`: "Text used for tagging purchasing card transactions"; there is no purchasing card.
- `Order/OriginatorCustomerParty`: the sawmill produces ahead; Valdara does not originate the processing order.
- `GoodsItem/MeasurementDimension`: the volume in m³ belongs in `GoodsItem/CustomsTariffQuantity` (the supplementary unit of 4407), so it would repeat.
- `ImportCustomsDeclaration/CustomsExitOfficeLocation`: there is no exit.
- `TransitCustomsDeclaration/*`: no transit is needed. The blanks are entered at the border.
- `Shipment/DeclaredStatisticsValueAmount` in the Bayvarran export: it would equal the customs value.
- The currency elements (`Order/RequestedInvoiceCurrencyCode`, `Invoice/PricingCurrencyCode` and their rates): the plant prices and invoices in ferra, its own currency, and a conversion inside the Accord is the bank's business (O226 principle, O231 parities). Asking for lume would be invented.
- `PartyLegalEntity/ShareholderParty` and its children: only if the owner wants the plant to be a joint venture of the sawmill. Even then no trade document states shareholders.
- `Duty/TaxCategory`: `Duty` is the telecom charging rate.
- `ItemProperty/UsabilityPeriod`: no property of the modified slat lapses.
- `Invoice/DeliveryNoteDocumentReference` and `Delivery/DeliveryNoteDocumentReference`: the plant sends a despatch advice, not a delivery note.
- Everything else in the register: no case in this flow (tender, maritime, self-billing, debit notes, telecom and so on).

**Count:** 18 recommended (strong or moderate), 2 conditional, 6 not specific, 6 weak.

**Against the O150 note's own candidates:**
- 7 recommended: rows 1, 2, 4, 7, 8, 10, 11. `Despatch/ReleaseID` (row 4) passes as a pick-up release, not as a call-off.
- `OrderResponse/Contract` is weak.
- `Delivery/ReleaseID` and `OrderReference/CustomerReference` are rejected.

**New from the scan, not in the note (11):** rows 3, 5, 6, 9, 12 to 18.

---

## 2. Design proposal

### 2a. Why the sawmill outsources: capacity in the season (recommended)

| Reason | For | Against |
|---|---|---|
| **Capacity in the season (recommended)** | Thermal modification is a batch process: a charge takes several days **(from memory: about 3–6 days for hardwood, including cooling and conditioning)**. In the southern summer (October to March) the sawmill's one kiln is booked with its own decking and cladding, which earn more. A season agreement for kiln slots at a plant near Ferrano is ordinary capacity buying. The plant is also 19 km from Valdara: the wood crosses the border once, as blanks, and the finished slats travel only a short way. It supports a recurring arrangement: the contract, the job numbers, the stock held for the owner, the call-off. | It changes O149's "the sawmill modifies the ash itself" from "always" to "outside its season". |
| Kiln out of action | A clear one-off. | No season agreement, no job numbers allotted in advance, no stock for call-off, so rows 1, 2, 6 and 18 lose their reason. A breakdown also has to be told and dated. |
| A specialist with better quality or certification | It explains a permanent outsourcing. | It contradicts O149's settled story and the type test made on the sawmill's own slats. The bench report's section 4.4 would have to be rewritten entirely. |
| Cost | | The sawmill already owns a kiln. A cheaper specialist for a quarter's supply of a product the sawmill can make is not believable. |

**What it means for D43 and O149:**
- **O149:** add "outside its summer season". Following O197, the bench report's sentence "There is no separate modification plant" gets a note pointing to O150's decision.
- **D43's goods balance:** the February delivery is the season case. The blanks went to the plant in January, and the 96 bundles leave the plant on 26 February. The May delivery falls outside the season and is the sawmill's own, so it is unchanged and not in the examples.
- **The truck figures:** the 21.0 t truck of modified slats (bench report) becomes Trasvia's leg from the plant to Valdara. The blanks go in two trucks, about 14.2 t of wood each.

### 2b. The party and its place

- **Name: Tostara Wood Modification**, legal form SRU (`Tostara Wood Modification SRU`). "Tostara" comes from Italian *tostare*, to roast. It follows the world's Urvanian pattern of an invented Italian-sounding word plus an English trade noun (Valdara Industries, Castrano Logistics, Rinova Recovery).
  - **Web check (2026-11-20):** searches for "Tostara" with wood, srl, azienda and company found no company of that name. The nearest hits are TOSTAR SRL, an Argentine coffee roaster, and the Taupo Totara Timber Company, a former New Zealand timber firm.
  - Rejected: "Bruniva" (also clean, but less telling); anything with "ThermoWood" or "Thermo" (ThermoWood is the registered mark of the Finnish producers' association **(from memory)**, and the bench report already avoids its trade names).
- **What it does (world text):** thermally modifies wood in two steam kilns for Urvanian timber merchants (beech from the western hills around Faggiorna, ash, poplar), and under contract for foreign sawmills in its customers' busy months. It holds an inward-processing authorisation for those foreign goods.
- **Place: square 84/113**, next to Conciaro (83/113), at about 302 m.
  - In the world model the square is free: farmland, with no party, house, road, rail or water on it.
  - It touches the main road to the border at 83/114 and 84/114, so the trucks from Marrowdale pass its gate.
  - Its address would be `Via delle Concerie, Conciaro` (the street name is not used anywhere in the world data), postal code 4190.
  - The reason for the place is already in the world: Conciaro is where Ferrano's tanneries were put, "downwind of the town". A modification kiln smells of smoke and acetic acid.
  - The road to Valdara (79/114) is about 5 squares, roughly 19 km on the map. That is a domestic leg for Trasvia, whose depot at 80/116 is close by.
  - Still to check: the 80 m terrace rule for a built square, and the place list (`tools/world_model.py` and `place_list.py --check`).
  - Free alternatives: 84/115 (same road, south side) and 81/114 (beside Valdara, but too close to tell a separate story).
- **Party number:** the next free number when it is built. 51 belongs to the Dutch isotope maker, and the reefer flow (O137) will take numbers too, so it is not pinned here.

### 2c. The customs procedure

**What the world's rules say.** The Accord is a free trade area, not a customs union (`codelist-decisions.md` Q24 and the story line on customs). Accord goods are duty-free on proof of origin. Urvania charges import VAT of 20 % at the border, which a business deducts (D18). So duty is no reason for inward processing; **import VAT is**:
- **Without a procedure:** the sawmill would import the blanks into free circulation and pay 20 % import VAT. A Bayvarran company can deduct that only with an Urvanian VAT registration. Its sale to Valdara would then be a domestic Urvanian supply by a foreign seller, with Urvanian VAT on it.
- **With inward processing:** the import VAT is suspended. The plant holds the authorisation; it is established in Urvania, as the holder must be in the EU **(from memory)**. The VAT falls once, on release, on the importer Valdara, who deducts it.
- **The real parallel:** the EU's inward processing suspends import VAT as well as duty, and companies use it for that alone, for example in trade with Switzerland and Norway **(from memory)**. This is realistic and gives the flow its point.

**Not recommended:**
- The sawmill registering for VAT in Urvania: realistic, but a foreign registration and Urvanian VAT on the sale, with no element won.
- The plant buying the blanks and selling the slats: that is no longer contract processing, and the sawmill's responsibility for the type-tested slat is gone.

**The procedure, step by step:**
1. **Export from Bayvarra** (modification/04, by the sawmill): a permanent export, because the goods do not come back. Nature of transaction `PROCESSING` (already in the list: "for or after processing under contract, UN/EU 4 and 5"). The consignee is the plant. The sawmill's statement on Bayvarran preferential origin goes with the goods.
2. **Entry into inward processing in Urvania** (modification/05, by the plant as holder and declarant; consignor the sawmill; the owner named in a note):
   - type `IMPORT`, a new subtype `INWARDPROC` in `CustomsDeclarationSubType`;
   - the authorisation as an additional document reference;
   - `Consignment/OfficeOfEntryLocation` (row 12);
   - the preference claim (D18) and the VAT suspended, stated;
   - the discharge period as `ValidityPeriod` (honest, but not counted);
   - customs value: there is no sale, so it is a computed value, the sawmill's cost of the blanks plus its profit, plus freight to the border (D16, Urvanian valuation).
3. **Release for free circulation** (wood/07, by Valdara as importer, as under DAP today):
   - the date moves to Thursday 26 February, before the goods leave the plant;
   - two goods items, one per entry, each with its `PreviousCustomsDeclaration` (the first is modification/05; the second truck's entry is cited but not in the examples);
   - the shipment's declared customs value and statistics value (rows 7 and 8), and each goods item's VAT base (row 9);
   - the plant, as holder, could instead lodge it as Valdara's direct representative. I recommend Valdara lodges it, as today.

**The valuation rule this needs** (a new world rule, the price of rows 8 and 9): when processed products leave inward processing into free circulation, Urvania assesses duty on the goods as they were placed under the procedure (their tariff line, customs value and origin), and VAT on the value of the processed products.
- This was the default of the EU's old Community Customs Code (Article 121) for inward processing under suspension. The Union Customs Code keeps it as an option on request (Article 86(3)) **(both from memory)**. With Accord goods the duty is nil, but the customs value is still declared.
- **Statistics** record the processed products at the value of the goods placed plus the processing **(from memory: how EU trade statistics treat goods after processing)**.
- The rule refines D18's sentence "VAT of 20 % on the value with freight and insurance to the border" for this procedure. It belongs in `countries.json` (XU customs) and in the story line.

### 2d. VAT and sales tax

1. **The plant's service to the sawmill** (modification/08): work on movable goods for a business customer established in Bayvarra. Urvania does not tax a service supplied to a customer established abroad (D17), so the invoice states category E with `SVCABROAD` (an existing code: "A service supplied outside Urvania, to a customer established abroad"). The EU parallel is Article 44 of Directive 2006/112/EC: since 2010, business-to-business work on movable goods is supplied where the customer is established, and Article 54 keeps work on movable goods at the place of performance only for private customers **(from memory)**. In Bayvarra the service is not taxed: its state sales tax falls only on the final retail sale, and D17's withholding applies only to public bodies.
2. **The sawmill's sale to Valdara** (wood/08): the goods are sold while still under inward processing in Urvania. The world rule (story text only, no code in any document): a supply of goods under a customs procedure carries no Urvanian VAT; the VAT falls on release, as import VAT on the importer. The EU parallel is the Member States' option in Articles 156 and 160 of the VAT Directive **(from memory, to be verified before it is written as fact)**. The sawmill states its own country's tax, as the story line requires. Bayvarran `EXP` ("Goods or services sent to a buyer outside Bayvarra") still fits: the wood left Bayvarra for this sale. The tax section of wood/08 is unchanged.
3. **Valdara** pays import VAT on release (row 9's base) and deducts it in its return, as today.

### 2e. The documents

A new flow, `modification`, numbered from 01 (D28). The wood flow's changed documents keep their numbers; wood/05 goes, and its number is not reused.

| No. | Document | From → to | Date (2026) | Purpose and what it carries |
|---|---|---|---|---|
| modification/01 | Order | sawmill → plant | Mon 12 Jan | Processing order for job `TW-J-26-0112` (`SalesOrderID`, row 1) under the season agreement 2025/26 (`Contract`). Output line: 96 bundles of modified slats `MS-SL-1800-50`, with `SubLineItem` 4,800 free-issue blanks (row 3). Operations: modification at 212 °C, planing, end sealing, bundling, storage until called off. The blanks are delivered by the sawmill's truck on 13 and 20 January. |
| modification/02 | OrderResponse | plant → sawmill | Tue 13 Jan | Accepted. The two charges: 14 to 19 January and 21 to 26 January. |
| modification/03 | DespatchAdvice | sawmill → plant | Tue 13 Jan | Truck 1: 2,400 blanks on 12 heat-treated pallets, the sawmill's timber truck S-1, the lot of the blanks. |
| modification/04 | ExportCustomsDeclaration | sawmill → Bayvarra customs | Tue 13 Jan | Permanent export, nature `PROCESSING`, consignee the plant, origin statement. |
| modification/05 | ImportCustomsDeclaration | plant → Urvanian customs | Tue 13 Jan | Entry into inward processing (`INWARDPROC`): the authorisation, `OfficeOfEntryLocation` (row 12), the preference claim, VAT suspended, the computed customs value, the discharge period. |
| modification/06 | InventoryReport | plant → sawmill | Fri 30 Jan | The sawmill's goods in the plant's store: charge 1, 48 bundles, available now; charge 2, 48 bundles, `AvailabilityDate` Wed 4 Feb (row 6). No blanks left unprocessed. |
| modification/07 | OrderChange | sawmill → plant | Tue 24 Feb | Call-off of all 96 bundles for Valdara, collected by Trasvia on Thu 26 Feb under pick-up release `MS-REL-26-0640`. Carries `SalesOrderID` (row 2) and `DeliveryTerms`: handover at the dock, risk passes on loading (row 18). |
| modification/08 | Invoice | plant → sawmill | Thu 26 Feb | Modification of 45.25 m³ in two charges; planing, end sealing and bundling of 96 bundles; storage. In ferra, Urvanian terms (30 days net, 2 % within 10). `SVCABROAD`. The service item carries `LifecycleStageCode` and `LifecycleStageDescription` (rows 10 and 11). |
| (modification/09) | RemittanceAdvice | sawmill → plant | Tue 10 Mar | Optional. Paid with the 2 % discount: the tenth day, Sunday 8 March, and Monday 9 March (Urvania's Independence Day) are not business days in the payee's country (O180). In ferra from the sawmill's lume account; the bank converts (O226 principle). |
| wood/02 (changed) | Quotation | sawmill → Valdara | Thu 19 Feb | Thermally modified ash only (O149: one wood). Names the processor under `SellerSupplierParty/Party/ServiceProviderParty` (rows 13 to 17). The price follows Q7. |
| wood/04 (changed) | TransportExecutionPlanRequest | sawmill → Trasvia | Mon 23 Feb | A domestic Urvanian leg, about 19 km, from the plant to Valdara. Consignor the plant, with its own despatch number `TW-DN-26-0219` (`ConsignorAssignedID`, row 5). No border. |
| wood/05 | ExportCustomsDeclaration | — | — | **Removed**: the export took place in January, as blanks (modification/04). The number is not reused (D28). |
| wood/06 (changed) | DespatchAdvice | **plant** → Valdara, for the sawmill | Thu 26 Feb | The plant is despatch supplier and the sawmill seller. `Shipment/Delivery/Despatch/ReleaseID` (row 4). The lots per charge give traceability. In the variant, 92 bundles with `OutstandingQuantity` 4 and its reason (rows 19 and 20). |
| wood/07 (changed) | ImportCustomsDeclaration | Valdara → Urvanian customs | Thu 26 Feb (was 27 Feb) | Release from inward processing: two goods items with their previous declarations; `Shipment/DeclaredCustomsValueAmount` and `DeclaredStatisticsValueAmount` (rows 7 and 8); `GoodsItem/ValueAmount` (row 9). The note gives the VAT basis. Nature `PURCHASE` (Valdara buys the slats). |
| wood/08 (changed) | Invoice | sawmill → Valdara | Thu 26 Feb | As now, with the amounts of Q7. Refers to the plant's despatch advice. `EXP` stays. |

wood/01, 03, 09, 10 and 11 are unchanged, except that wood/09's amount follows the price (Q7).

### 2f. Timeline

All dates are working days of the issuer (D27). Border customs and Trasvia work every day. No document falls on a holiday: none is issued by a Bayvarran party on Settlers' Day (16 February), and none by an Urvanian party on Children's Day (6 January) or Independence Day (9 March).

| Date | What happens |
|---|---|
| Mon 12 Jan | Processing order (modification/01) |
| Tue 13 Jan | Response; truck 1 (despatch advice, export, inward-processing entry) |
| Wed 14 Jan to Mon 19 Jan | Charge 1 |
| Tue 20 Jan | Truck 2. Its documents are not in the examples; the release cites its entry. |
| Wed 21 Jan to Mon 26 Jan | Charge 2. Planing of charge 1 from 20 January. |
| Fri 30 Jan | Stock report: charge 2 available from Wed 4 Feb |
| Mon 16 Feb to Mon 23 Feb | The wood flow's request for quotation (16 Feb), quotation (19 Feb), order and transport request (23 Feb), as now |
| Tue 24 Feb | Call-off (modification/07) |
| Thu 26 Feb | Release declaration; collection at the plant; delivery to Valdara the same day (19 km); sawmill's invoice; plant's invoice. This is inside the delivery window of 26 February to 6 March already agreed. |
| Tue 10 Mar | Sawmill pays the plant with discount (optional remittance) |
| Mon 30 Mar | Net due date of the plant's invoice: the 30th day, Sat 28 Mar, moves to the next business day (O180) |

The bench lots from March to May (`goods_chain` in `world/items.json`) are unaffected: the slats arrive at Valdara on the same day as before.

### 2g. Quantities and prices

All figures are a proposal unless taken from the bench report.

- **Blanks:** 4,800 of 1,830 × 101 × 51 mm (bench report: "untreated ash blanks, assumed"). That is 0.009427 m³ each, 45.25 m³ in all; 5.9 kg each at about 625 kg/m³ kiln-dried (29.5 kg per bench of 5, bench report), so 28.3 t in all. Two trucks of 2,400 blanks (22.6 m³, about 14.2 t of wood plus 12 pallets each). The vehicles must be checked against the sawmill's truck S-1, as the vehicles follow from the legs.
- **Output:** 4,800 slats of 1,800 × 95 × 45 mm, 4.24 kg each (bench report), 96 bundles of 50, about 20.4 t, on the same 24 heat-treated pallets. That is the bench report's 21.0 t truck load, now for Trasvia (tractor and curtain-side trailer T-07).
- **Kiln-dried rather than green:** O150 says "green ash". I recommend kiln-dried blanks. The sawmill's ordinary drying kilns are not its bottleneck, and hardwood is usually dried before thermal modification to limit checking **(from memory)**. It also keeps the bench report's 29.5 kg, and green wood (about 850 kg/m³, from memory) would weigh about 38 t, still two trucks.
- **The plant's fee:** 1,296,000 ferra = 12,960 lume, 135 lume a bundle. Proposed split:
  - modification: 22,000 ferra a m³ of input × 45.25 = 995,500;
  - planing, end sealing and bundling: 2,900 ferra a bundle × 96 = 278,400;
  - storage, 4 weeks: 22,100.

  The order of magnitude, about 200 lume a m³ for toll modification, is **from memory**.
- **Customs value of the blanks** (computed value plus freight to the border): about 240 lume for 50 blanks (about 510 lume, roughly 425 EUR, a m³ **(from memory, about right for kiln-dried sawn ash)**) × 96 = 2,304,000 ferra, plus 2 × 60,000 freight. **Declared customs value 2,424,000 ferra**, 1,212,000 per goods item.
- **Statistics value:** 2,424,000 + 1,296,000 = **3,720,000 ferra**.
- **The price problem (Q7).** At today's 360 lume a bundle the sawmill's invoice comes to 34,800 lume = 3,480,000 ferra. That is *below* the cost of blanks plus fee (about 37,200 lume with freight), and below the statistics value. Every value of this design reads wrongly at that price.
  - The problem exists without O150 too: 360 lume was the price of oak 38 mm. Thermally modified ash 45 mm (O149, O119, still to be rewritten in the wood flow) is about 18 % more wood plus the modification.
  - Proposal: **480 lume a bundle** (9.60 a slat, about 1,250 lume or 1,040 EUR a m³ of finished slats; the market check is **from memory**). Invoice 46,080 + 240 pallets = **46,320 lume = 4,632,000 ferra**.
  - The VAT base on release is 4,632,000 less the 30,000 for carriage from the plant to Valdara = 4,602,000; import VAT 920,400 ferra.
  - Valdara's slats cost 12 lume more a bench (48 instead of 36). Valdara absorbs it: the bench prices of D14 stay.

---

## 3. Costs, risks and questions for the owner

### 3.1 What changes in existing flows and data

- **The wood flow:** wood/02, 04, 06, 07 and 08 change, wood/05 is removed, wood/09 changes only with the price. These documents must be rewritten for thermally modified ash anyway (O149, O119; the XML still says oak 38 mm and HS 4407.99, while ash is 4407.95), so the two changes are best made in one step.
- **`world/documents.json`:**
  - the wood flow's text: no oak, no "from May ash";
  - the legs: 36-xb → 5-xu is replaced by 36-xb → plant (blanks, the sawmill's truck, across the border) and plant → 5-xu (Trasvia, domestic);
  - a new flow `modification` with its documents and their reasons.
- **`world/parties.json`:** the new party, with identity, register, customs trader number (D18: built from the register number), contacts and fleet if it has one. The sawmill's "what" text gets its own kiln and the season contract.
- **`world/items.json`:** the blank `MS-BL-1830` (the sawmill's number), the plant's service item with its life cycle stage, and the slat item already being rewritten. The goods chain gets the delivery's origin.
- **`world/codelists/lists.json`:** `CustomsDeclarationSubType` gets `INWARDPROC`; a regional list of service types for row 15 (or row 15 is dropped and the text alone kept). XU exemption reasons: none; `SVCABROAD` exists.
- **`world/countries.json` and `note/src/03-world.md`:** Urvania's inward processing (holder established in Urvania, VAT suspended, the valuation rule of 2c, supplies while under the procedure); the plant and Conciaro's industry; the sawmill's season.
- **`world/bench/report.md` and `parameters.json`:**
  - section 4.4: "There is no separate modification plant" gets a note following O197;
  - "only the end grain is sealed at the sawmill" becomes "before delivery" (in the season the plant seals them), with the same change in the datasheet text;
  - the modification energy factor of the footprint must agree with the plant's life cycle description (O25, O225).
- **The decisions file:** O150 decided; O149 and D43 notes per O197; O119 and the price (Q7) recorded.
- **`analysis/coverage-register.md`:** the rows won move to "Won back". `OrderResponse/Contract` and `Delivery/ReleaseID` drop the "O150, if adopted" mark. The place list is regenerated, and the world-model and place checks run.
- **Build:** new scenario code in `tools/examples_scenarios.py` (wood and modification), and probably builder support for `SubLineItem`, `ServiceProviderParty`, `InventoryReportLine/AvailabilityDate` and the inward-processing declaration.

### 3.2 Risks

- **The valuation rule** (2c) is the most complex customs story in the world. If it is not adopted, rows 8 and 9 go: the customs value would then equal the statistics value and the VAT base, and stating them would repeat.
- **`OfficeOfEntryLocation`** (row 12) may be reviewed as a repeat of the receiving office.
- **`OrderChange/SalesOrderID`** (row 2): the definition says "for the Order Change".
- **The service-provider group** (rows 13 to 17) in a quotation is unusual, though the supplier-approval reason is real.
- **The VAT rule for supplies under a customs procedure** (2d, point 2) is from memory and must be verified before it is published as fact.
- **The three-flow consistency checks** (legs on the map's routes, vehicles from legs, due dates on business days, numbering per issuer under D24) all need new entries.

### 3.3 Questions for the owner

| Q | Question | Options | Recommendation |
|---|---|---|---|
| Q1 | Adopt O150? | a) as designed; b) only the plant's documents, without the customs part (loses rows 7 to 9 and 12); c) not at all | **a)**: 18 elements for 8 new documents and one rewrite the wood flow needs anyway |
| Q2 | The sawmill's reason to outsource | a) capacity in the season; b) kiln out of action; c) a specialist; d) cost | **a)**: see 2a |
| Q3 | Which delivery | a) the February delivery of the examples; b) a separate later delivery (May, outside the season, needs a reason b) and a new order and quotation from Valdara) | **a)** |
| Q4 | Where the documents go | a) a new flow `modification`; b) appended to the wood flow as wood/12 onwards | **a)**: two contracts, two flows; the wood flow stays the sale |
| Q5 | Customs | a) inward processing for the VAT suspension, valuation on the goods placed; b) inward processing, with customs value on the processed products (loses rows 8 and 9); c) a plain import and an Urvanian VAT registration for the sawmill | **a)** |
| Q6 | The sale while the goods are under inward processing | a) a story rule (no Urvanian VAT; import VAT on release); b) also an XU exemption code, shown where an Urvanian seller makes such a sale | **a)**: no Urvanian seller makes one in the examples |
| Q7 | The price of the bundle of modified ash, 45 mm | a) 480 lume (Valdara absorbs it, bench prices unchanged); b) keep 360 and make the blanks and the fee cheaper (about 170 and 110 lume a bundle: tight, but it can be made to add up); c) another figure | **a)**; decide together with O119 |
| Q8 | Blanks green or kiln-dried | a) kiln-dried; b) green, as O150 said | **a)** |
| Q9 | The split delivery (4 bundles with end splits) | a) no; b) yes: +2 elements, +1 despatch advice and transport, a split invoice and release | **a)**, unless coverage needs the two |
| Q10 | The processor named in the quotation (rows 13 to 17) | a) yes, with the supplier-approval reason; b) no (−5) | **a)** |
| Q11 | Name and place | a) Tostara Wood Modification SRU, Via delle Concerie, Conciaro, square 84/113; b) another name or square (84/115 is free too) | **a)** |
| Q12 | Who seals the end grain | a) the plant, in the season (datasheet: "before delivery"); b) the sawmill, after the slats are returned (an extra round trip, not believable) | **a)** |
| Q13 | Is the plant independent or a joint venture of the sawmill | a) independent; b) a joint venture (would explain the arrangement, but no document needs it) | **a)** |
| Q14 | `OrderResponse/Contract` | a) leave it out (the order cites the contract); b) cite the contract only in the response | **a)**: avoid the repetition |

### 3.4 New open points this would raise (to number when recorded)

- The world rule for inward processing (valuation, statistics, supplies under the procedure), to be verified against the EU texts before it goes into the world text.
- The modification energy figures: one set for the sawmill's own kiln and the plant's, or two.
- The second truck's documents: cited but not in the examples, as the wood flow already does for other deliveries.

---

Sources for the name check: [TOSTAR SRL (nosis)](https://trade.nosis.com/en/TOSTAR-SRL/30711985669/1/p), [Taupo Totara Timber Company (Wikipedia)](https://en.wikipedia.org/wiki/Taupo_Totara_Timber_Company), [B Timber (Facebook)](https://www.facebook.com/btimber.it/). No search found "Tostara" or "Bruniva" as a company name.
