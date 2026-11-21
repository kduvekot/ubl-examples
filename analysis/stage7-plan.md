# Stage 7: build checks, a plan for the owner (2026-11-21)

Read-only survey of the repository at `8ed26ced3`. Nothing was built or changed. The estimates of what each check
would find come from read-only probes over `world/examples/*/*.xml` and `.md` (scripts in
`/tmp/claude-0/-home-user-ubl-examples/dec3f5a6-c191-5ca3-b0d0-bc52deffd7b2/scratchpad/probes/`). The probes ran
after the read-through fix batch (commit 2a048333e and the merges after it), so most read-through mismatches are
already fixed. Many checks below would therefore find nothing today: they guard the fix.

Sources: `analysis/worklist.md` "Stage 7: Build checks" and "Work the decisions add"; `analysis/worklist-decisions.md`
rows O31, O60, O62, O64, O66, O70, O78, O79, O250 (marked "Stage 7 (owner, 2026-11-20)"), and O156, O259, O262,
O265, O266, O269; the four reports in `analysis/readthroughs/`.

## 0. Where the checks run today, and one general point

- `tools/build_site.sh` runs `tools/check_world.py` (which runs terrain, place list, fx, `world_model.py`,
  `world_docs.py`, `world_parties.py`, `world_items.py`, `build_codelists.py --check`, `coverage_register.py`), then
  `tools/build_examples.py --check`, XSD and phase-2 validation, and at the end `tools/check_published.py` on the
  built site.
- `build_examples.main()` runs these checks per document: `check_issue_order`, `check_reference_targets`,
  `check_specifications`, the C18 transport-event check and the C16 `NoStatus` check (both inline in `main`),
  `check_addresses`, `check_payment_means`, `check_dangerous_goods`, `check_classifications`, `check_formats`,
  `check_time_offsets`, `check_schemes` (with `check_codana`), `check_tax_exemption_lists`, `check_instance_rules`,
  `check_payment_terms` and `check_due_dates`. Per flow it runs `check_reference_uuids`, `check_air_uld_ids`,
  `check_party_profiles`, `check_calendar`, `check_unit_ids`, `check_packages` and `check_utility_statements`.
  Over all flows it runs `air_load_problems`, `check_party_knowledge` and `check_numbering`.
- **Fixers are not the same as checks.** Several stage 7 items are covered today by functions that *repair* the
  content during the build. Most of them only raise an error in some cases:
  - `tax_arithmetic` (C24) rewrites a wrong TaxableAmount and raises an error only when the rate is not 0.
  - `currency_cleanup` (C11) drops idle currencies and rates without a word.
  - `shipment_weights` (C15) recomputes the weights.
  - `national_tariffs` (C29) removes the national tariff where it does not belong.

  A fixer hides the generator error behind it. One case: the read-through found a subtotal of 0.00 under a reason
  that says "the lines of this category plus the document's charges" (utilities/06, tender/26). That is fixed now.
  This is question Q1 below.

## Part A: checks that exist in part, or are cheap

### A1. Every time has an offset (O78)
1. **Guards:** D27 and O78 (C53, C72): every `cbc:*Time` carries its offset from UTC.
2. **What exists:** `check_time_offsets()` in `tools/build_examples.py` (l. 3566). `examples_kit.time_offsets()`
   fills in the offsets. **Built 2026-11-20.**
3. **Missing:** a check that an offset is *right*, meaning it is the offset of the place where the event happens:
   −01:00 on the mainland, +00:00 on Lisavu, +05:30 or +02:00 abroad. Today only the format is checked.
4. **How it would work:** for each time, find the place the same way `time_offsets()` does (UN/LOCODE, GLN,
   address country, else the issuer). Compare with `world/countries.json` `timezone` (`abroad_countries` for
   parties abroad).
5. **Today:** probably 0. The read-through of six flows found "the offsets that are given are right everywhere".
6. **Effort and risk:** S. Low risk. An event with no place falls back to the issuer, which is the rule already used.
7. **Owner decision:** none.

### A2. A document is issued within its issuer's desk hours (O269, stage 7 part)
1. **Guards:** O269 and the read-through finds tender/24, 37, modification/03, 04, reefer/09, 11 and others.
2. **What exists:** nothing. `check_calendar()` checks only the day, not the hour.
3. **Missing:** the whole check.
4. **How it would work:**
   - Parse `identity.contact.hours` in `world/parties.json`. There are 13 forms, all regular, such as
     "Weekdays 08:00–17:00", "Monday to Saturday 05:00–14:00" and "Every day, around the clock". A desk may have
     hours of its own (`desks.<k>.hours`, 3 of them today).
   - Compare `IssueTime` in the issuer's local time with the hours of the desk that the document's contact names,
     else the contact hours.
   - Report the file, the time and the hours.
5. **Today (probe `desk.py`):** 14 of 299 documents with an IssueTime fall outside the issuer's contact hours:
   - road/02 (17:42), retail/01 (08:42), retail/08 (08:15), retail/20 (17:05), air/01 (07:50), air/07 (19:50),
     air/08 (20:05), air/10 (17:03), plastics/08 (17:57), furniture/04 (08:23), furniture/07 (17:49),
     furniture/19 (07:30), mast/05 (17:34), medicines/02 (08:40 +05:30, the Indian maker).
   - mast/05's issuer has an "emergency" desk with its own hours.
6. **Effort and risk:** S for the check. The 14 fixes go to the scenarios, or to the desks' hours. False alarms come
   from documents that a system sends on its own (a despatch advice when the truck leaves at 20:05, air/08), or a
   desk with longer hours than the front office (dispatch, goods-in).
7. **Owner decision:** Q2. Do the hours bind every document, or only those a person issues? May a desk (despatch,
   goods-in) have hours of its own, as the "emergency" desk does?

### A3. One flight duration from the map everywhere (O269 with O250)
1. **Guards:** O269 and the air read-through finding A3 (truck and flight times).
2. **What exists:**
   - `FLIGHT_BLOCK_EAST = 2.75` in `tools/examples_scenarios.py` l. 2769, with a SystemExit when
     `world_map.air_km()` no longer fits it (l. 2770).
   - air, mast and medicines use it (l. 2772, 8583, 8854).
   - The "+1" hour time difference is written into these lines by hand.
3. **Missing:**
   - The map route's wiki facts in `world/map.json` route `air` ("Distance: about 1,080 km", "Timetable: 2 h 45
     east, 3 h 00 west", the lead "about 2½ hours") are literals. Nothing ties them to `air_km()` or to the constant.
   - The westbound block time (3 h 00) has no constant: carnet flies back.
   - The time difference should come from the two countries' `timezone`.
4. **How it would work:**
   - One `FLIGHT_BLOCK = {"east": 2.75, "west": 3.0}` in world data, for example the route's own entry in `map.json`.
   - The route's facts are generated from it, or asserted against it (see B2).
   - A check reads every air ShipmentStage with a planned or actual departure and arrival, and asserts that arrival
     minus departure equals the block time, or is shorter for an actual landing.
5. **Today (probe `flights.py`):** 3 waybills (air/04, mast/03, medicines/11) are all 2:45. air/09 actual 10:30
   against a planned 10:45 is an early landing (fine). The map facts agree: `air_km()` = 1,076 km against
   "about 1,080 km". So 0 hits.
6. **Effort and risk:** S. Low risk.
7. **Owner decision:** none. Only whether the westbound 3 h 00 should exist as data.

### A4. Published-text rules (O265, two layers)
1. **Guards:** O265, O256, SR-07, and the read-through finds (finding IDs, rule IDs, real standards).
2. **What exists:** `tools/check_published.py`. It scans the built HTML except `note/`, `codelists/`, `examples/`
   and two history pages, and the world's own code lists. It fails on:
   - D-, O- and MO-numbers, finding IDs and IND-numbers;
   - paths;
   - EN 16931, Peppol and XRechnung;
   - "EN nnnn" except EN 15804;
   - RecyClass, the European List of Waste, VATEX and "EU", with an exemption for the Dutch party `51-nl` and its
     documents.

   It only warns on change words ("no longer", "was moved", "proposed addition").
3. **Missing:**
   - **Explanations by the model or the project.** "(UBL 2.5, 2.2.2 Manifest Values)" is on 41 example pages, and
     "as in the OASIS example …" on 11. The read-throughs flag both as two-layer breaches. A rule cannot be added
     until the owner says whether they count (Q3).
   - **Lower-cased world names.** "trade accord's network" is in sea/03-DigitalAgreement (XML and .md).
   - Change words are only a warning.
4. **How it would work:**
   - Add the pattern list of Q3 to `FAIL`.
   - Add a case check for a short list of world proper names (Trade Accord, Lumeport Exchange, party names) written
     in lower case.
   - Possibly promote `WARN` to `FAIL` once its hits are 0.
5. **Today:**
   - `FAIL` and the European rules, run over the example .md text (probe `pub.py`, code spans removed): 0 hits.
   - Manifest Values: 41 files. "as in the OASIS example": 11 files. Lower-cased "trade accord": 1.
6. **Effort and risk:** S. Low risk. A proper-name list needs care with ordinary words ("accord").
7. **Owner decision:** Q3, whether reasons that cite UBL's own principles or the OASIS samples are allowed in world
   text. Q4 (EN 13556) is under A12.

### A5. Tax currency and tax exchange rate only where VAT is charged (O262)
1. **Guards:** O262.
2. **What exists:**
   - The scenario code for the tender order only (comment at `tools/examples_scenarios.py` l. 12009).
   - `untaxed_sales()` strips them from Lisavan sellers' documents.
   - There is no general check.
3. **Missing:** a check that `TaxCurrencyCode` and `TaxExchangeRate` appear only on Invoice, CreditNote,
   SelfBilledInvoice, SelfBilledCreditNote, DebitNote and a PurchaseReceipt that charges tax, and only where VAT is
   actually charged.
4. **How it would work:** per document, the document type is in the allowed set, and some `TaxTotal/TaxAmount` is
   not 0.
5. **Today (probe `taxcur.py`):** 5 documents carry them.
   - wood/08 (S 20 %) and packaging/09 (receipt, 6.5 %, a TaxExchangeRate only; PurchaseReceipt has no
     TaxCurrencyCode in UBL 2.5) are fine.
   - **tender/32-Invoice, tender/33-CreditNote and tender/39-Invoice** carry XUF as the tax currency with a second
     TaxTotal of 0, on a 0 % export (G/EXP) or a service outside the scope (O/SVCABROAD).
   - So 3 hits if "charged" means a tax amount above 0, and 0 if it means the document type.
6. **Effort and risk:** S. Low risk.
7. **Owner decision:** Q5. Does O262's "on which VAT is actually charged" exclude an invoice whose tax is 0 % or
   outside the scope (tender/32, 33, 39)? Or does the second TaxTotal in ferra stay because Urvania asks for its
   VAT, even at 0, to be stated in its own currency?

### A6. Tax codes for goods in transit and for domestic sales abroad (O266, O259)
1. **Guards:** O266 (TRANSIT for the air frames), O259 (the slat sale as an Urvanian domestic supply) and C50.
2. **What exists:**
   - The rule engine `examples_kit.tax_rule()` (l. 269) with `TAXED_IN` (l. 262).
   - `check_tax_exemption_lists()` in `build_examples.py` (l. 641) checks that the list fits the seller's country.
   - `world_parties.py` checks `tax_abroad` (format, check digit, uniqueness).
   - These check the *list*, not whether the code fits the movement of the goods. `tax_rule` decides from the
     parties' countries only, and the TRANSIT case comes from the scenario.
3. **Missing:** an independent check of the treatment against the goods' movement:
   - an export code (XU EXP, XB EXP) only where the goods leave the seller's country: a leg of the flow crosses its
     border, or the delivery place lies abroad;
   - TRANSIT where the goods only pass through the seller's country under a transit declaration;
   - a sale of goods in free circulation in another country is S of that country, under the seller's `tax_abroad`
     number, with no origin statement (see A7).
4. **How it would work:**
   - Read the flow's `legs` (from, to, mode), the delivery location and its country, and the flow's customs
     documents.
   - Derive "leaves the seller's country", "only transits" or "stays".
   - Compare with each TaxCategory and exemption code of the invoice-kind documents and orders.
5. **Today (probe `exempt.py`):**
   - 84 categories, all with codes from the right list.
   - The air case is now G/TRANSIT on air/01 and air/11, and the wood case is S without a code.
   - Expected hits: 0. Possible false alarms: the invoices whose export leg is not in the flow, such as
     packaging/02 (FCA, the buyer's carrier collects), mast/05 and medicines/14 (by air, with no export declaration
     among the examples).
6. **Effort and risk:** M. Medium false-alarm risk until "the goods leave" is defined for flows with no leg.
7. **Owner decision:** Q6. Is an export proved by a leg of the flow, or is the delivery terms' place abroad enough?

### A7. The origin statement only when the goods cross an Accord border to the buyer
1. **Guards:** D18, O49, the wood read-through (3) and the air read-through (A5).
2. **What exists:**
   - The generator rule `examples_kit.origin_statement()` (l. 1470): different countries, not `TAXED_IN`, no
     certificate of origin in the flow, one Accord origin of the goods.
   - `build_examples.origin_notes()` writes the statement into the Note. No check reads the XML afterwards.
3. **Missing:** a check over the XML:
   - an invoice carries the statement exactly when it sells Accord-origin goods to a buyer in another Accord
     country and the goods cross that border;
   - never on a domestic sale;
   - never next to a certificate of origin;
   - the import declaration that claims the preference cites that invoice or the certificate.
4. **How it would work:** detect the statement text in `cbc:Note`. Combine it with the A6 movement test and the
   flow's documents. The citation part uses `AdditionalDocumentReference` of the import declarations.
5. **Today (probe `origin.py`):**
   - The statement is on rail/11, sea/22, air/11, tender/32, plastics/10, cotton/16, packaging/02, mast/05,
     energy/06, 07 and reefer/08.
   - It is not on road/15 (certificate of origin), wood/08 (domestic), medicines/02, 07 (made abroad, outside the
     Accord) or medicines/14 (abroad origin).
   - All of this is consistent with the rule: 0 hits.
   - Still open from the read-through: air/11 and sea/22 are issued by Lumeway, a reseller. For air/11 the goods
     leave Urvania under Valdara's transit declaration, so Lumeway is not the exporter there (A5).
6. **Effort and risk:** S for the presence rule, M with the citation part. Low risk.
7. **Owner decision:** Q7. May a reseller (Lumeway) make the statement on its own invoice? In air/11, where the goods
   move under the maker's transit declaration, is the statement right at all?

### A8. A lot or serial number, once assigned, appears unchanged everywhere (O64)
1. **Guards:** O64 (decided 2026-11-20: "once a serial number or lot number is assigned, it should never be
   changed"), C70, C71 and the rail read-through (4).
2. **What exists:**
   - `world_items.chain_problems()` (l. 322): the production record and the ledgers. Serials do not overlap, rise
     with the casting day, one melt per day, one coating per lot, stock never below zero, nothing leaves before it
     arrives.
   - `check_unit_ids()` in `build_examples.py` (l. 3152): logistic units, **within one flow only**.
   - `previous_declarations()` in the scenarios: the previous customs declaration comes from the ledger.
3. **Missing:** the document side, across flows:
   - every `LotNumberID`, `SerialID` or other serial of an item that has a production record is in that record,
     on the same item, in the same form;
   - the same lot never appears in another form (another prefix, a Codana form, another digit count);
   - a lot quoted in two flows (road/04 → retail/12, sea/20) belongs to the same item.
4. **How it would work:**
   - Gather the structured lot and serial elements with their item (SellersItemIdentification) over all built
     roots (`BUILT`).
   - Compare them with `world/items.json` `goods_chain`. For makers without a record, check that one value maps to
     one item everywhere.
5. **Today (probes `lots.py`, `lottok.py`):**
   - 18 distinct lots and 21 serials in structured elements.
   - All VI lots and serials are in the production record (VI-LOT-260320/327/409/410; VI-SF-01298, 01490–01501,
     01611, 01690, 03190–03197).
   - The other makers' lots (HRW-L26-…, MDS-L26-0119/0126, MDS-BL26-0109, NLB-…, RR-PE-0417, SCG-L26-017) appear
     consistently, in at most two documents each.
   - Expected hits: 0. The rail delivery itself still carries no lot (read-through rail 4, O271).
6. **Effort and risk:** S–M. Low risk if only structured elements are read. A text scan gives false alarms: the
   NLB item numbers share the lot prefix "NLB-".
7. **Owner decision:** Q8. Should the other makers' lots and serials (the plant, the sawmill, the recycler, the
   ginnery, the orchards, the pharma maker) also become production records in world data, like Valdara's? This
   decides how far O64 reaches, and it is the data O66 needs too.

### A9. The calendar (O79, the rest)
1. **Guards:** D27, O79, O180 and C53.
2. **What exists:**
   - `check_calendar()` in `build_examples.py` (l. 3542): the issue day is a working day of the issuer, with
     `CALENDAR_WAITS` (empty now).
   - `check_due_dates()` (l. 3524): a due date is a business day of the payee's country.
   - `working_day()` and `business_day()`.
3. **Missing:**
   - "unless it says why not": there is no way to mark a justified exception other than `CALENDAR_WAITS`;
   - "payments between countries on a day both banking systems are open";
   - the event dates of goods movements, for example a delivery on a day the receiving warehouse works.
4. **How it would work:**
   - An optional `calendar_exception` (reason) on the document in `world/documents.json`.
   - For credit transfers (PaymentMeansCode 30, 31, 58, 59, and remittances), `PaymentDate`/`PaidDate` is a
     business day in both the payer's and the payee's country.
   - `ActualDeliveryDate` is a working day of the delivery party.
5. **Today (probe `pay.py`):** 0 cross-border transfers on a closed day. The only two hits are card receipts at a
   till on a Saturday (packaging/09, sea/29), and they are not bank transfers, so they are false alarms unless
   card and cash are excluded. Delivery days were not probed.
6. **Effort and risk:** S. False alarms only if the payment means is not filtered.
7. **Owner decision:** none for payments. Q9: should deliveries and receipts also fall on the receiver's working
   days?

### A10. Payment terms (O70, the rest)
1. **Guards:** D22, D23, O70, C51 and C55.
2. **What exists:** `check_payment_terms()` in `build_examples.py` (l. 3449): one terms ID has one text and one
   period, the due dates of a document agree, and the due date follows from the issue date, moved to a business
   day. `DUE_DATE_WAITS` is empty. `examples_kit.terms_of()` picks the terms.
3. **Missing:**
   - "an invoice under a contract or plan carries those terms", as a check;
   - "a reminder's interest runs from the due date of the terms that apply", and its amount (rate × days or
     months × principal).
4. **How it would work:**
   - Contract: an invoice that cites a contract or plan whose world terms are known has a `PaymentTerms` with that
     ID.
   - Reminder: each interest period's `StartDate` is the day after the cited invoice's due date, and the amount
     follows from the rate (`PenaltySurchargePercent` or `InterestRatePercent`) and the period.
5. **Today:**
   - Probe `pay.py`: 0 invoices cite a contract or plan without PaymentTerms.
   - There are 3 reminders (energy/08, tender/35, utilities/10). Their periods start the day after the due date in
     the texts read (energy/08 from 6 May for a due date of 5 May; tender/35 from 14 May for 13 May). Expected 0.
6. **Effort and risk:** S. Low risk.
7. **Owner decision:** none.

### A11. The rest of the stage 7 list in `analysis/worklist.md`: what is built, what is open
| Stage 7 item (guards) | Exists | Missing | Probe today |
|---|---|---|---|
| Issue time after every reported event and cited document (C72, C73) | `check_issue_order`, `derived_issue_time`, `CITED_LATER` in `main` | – | – (built) |
| Due date − issue date = terms period; contract terms (C55, C51) | `check_payment_terms` | the contract and reminder parts, see A10 | 0 |
| Tax arithmetic per subtotal with allowances and charges (C24, C94) | `tax_arithmetic` (fixer; raises only when the tax would change), `check_utility_statements` | an assertion that does not repair; tax = base × rate; total = Σ subtotals; monetary totals (with withholding) | 80 subtotals: 0; totals: 0 (cotton/04, 05 and tender/39 hold once WithholdingTaxTotalAmount is counted) |
| Emission = factor × base (C09) | `world_items.emission_problems` (items only) | the same on the document's `EnvironmentalEmission` (lpg/03 gives a factor 0.268) | not measured |
| No `NoStatus`, no identity rate, pricing currency (C16, C11) | `NoStatus` inline in `main`; `currency_cleanup` (fixer) | an assertion for C11 instead of a silent drop | – |
| Every reference typed and resolved (C06, C73) | `type_references`, `check_reference_targets`, `UNTYPED`/`UNRESOLVED` in `__main__` | – | built |
| `ShippingOrderID` resolves to forwarding instructions (C20) | none | the check | 10 of 10 resolve (probe `batch.py`) |
| Shipment gross ≥ goods + equipment tare (C15) | `shipment_weights` (fixer) | an assertion | – |
| Waybill note and distribution agree on the originals (C33) | `examples_kit` l. 1368–1409 makes both from one source | a check: ORIGINALHANDED goes to the consignor and ORIGINALWITHGOODS to the consignee, and the note's count matches | 14 documents: 0 (rail/08, medicines/11 and lpg/03 are fixed) |
| Customs offices of the declaring country; national tariff only at home (C12, C29) | `national_tariffs` (fixer), `border_transport`, `declaration_invoices` | offices: the `Office*Location` elements carry no ID or country, so only names could be checked (C23) | CustomsParty is the procedure's country everywhere (wood/07: Urvanian customs for the Bayvarran importer) |
| No customs-trader ID outside customs documents; share capital only on the issuer's invoice (C01) | `check_party_profiles`, `check_party_knowledge` | – | built |
| Working day, offsets (C53) | see A1, A9 | see A1, A9 | – |
| Numbering, collaborations (C74–C76) | `check_numbering` | – | built 2026-11-20 |
| Coordinates against distances and durations (C56, C58) | see B1 | see B1 | – |
| Item physics (O62), goods chain (O65), margins (O30), HS (O31), Codana prefixes and repeats (O32, O22) | O65: `chain_problems`; O30: `resale_problems`, `figure_problems`; O32: `check_codana`; O22: `world_parties.repeat_problems`; O62: `physics_problems` (bench only) | O62 → B4, O66 → B3, O31 → B5 | – |

### A12. Code-list sources, and EN 13556 (O156)
1. **Guards:** "external lists only from verified sources" (rules), and O156.
2. **What exists:**
   - `build_codelists.real_code_problems()`: world codes are not real ISO 4217, ICD or MIC codes.
   - `iso20022_problems()`: definitions word for word.
   - SHA-256 checks only for the two UBL originals (`LISTS`, l. 46).
   - Nothing checks the files in `world/codelists/sources/` against `PROVENANCE*.md`.
3. **Missing:**
   - a provenance check: every source file has its SHA-256 in `PROVENANCE.md` or `PROVENANCE-second-round.md`,
     and the file still has that hash;
   - for EN 13556, a source first.
4. **How it would work:** parse the 64-hex hashes per row of the two PROVENANCE files, and hash every file under
   `sources/`.
5. **Today:**
   - 76 source files, 74 with a listed hash.
   - **2 without one:** `iata-dgr/2026_Table_9.3.A_table-only.pdf` (6a842c49…) and `atr/ATR_Fiche72-600F-3.pdf`
     (b1c03f2b…). Their rows (PROVENANCE.md l. 87–88) give the URL but no hash.
   - EN 13556: no source in the repository. The standard is a paid CEN publication. The `Wood` list is regional,
     with 2 codes (OAK, ASH).
6. **Effort and risk:** S. No false alarms.
7. **Owner decision:** Q4.
   - A verified source for EN 13556 is a paid standard, or a secondary list that quotes it: is a secondary source
     enough?
   - `check_published.py` allows only EN 15804 among "EN nnnn". Does EN 13556 count as a norm the world accepts
     (O265), or would its codes appear without the standard's name?

### A13. Patterns from the read-throughs
| Pattern (read-through) | Check | Probe today | Effort/risk |
|---|---|---|---|
| A reason that states a premise which does not hold: "quoted in its order" without an order (waste/03, plastics/07, air/10, …); "Issued on despatch" or "on delivery" against the dates (plastics/10, packaging/07, mast/05) | a short list of shared reasons, each with a predicate that the build tests on the document (OrderReference present; IssueDate = ActualDespatchDate/ActualDeliveryDate; "the next working day after X" = `working_day` + 1) | **3 hits:** ore/06, road/14 and cotton/17 (freight invoices; the "order" is a transport plan or a booking, and the text is from `examples_kit` l. 1004). IssueDate "on despatch"/"on delivery": 0 hits (packaging/04 has no delivery date to compare) | S per predicate; low risk; it covers only listed phrases |
| A reason whose number differs from the value (air/04: "97.6 kg" against 105) | none generic; the rule "a reason that states a value computes it" belongs in the generators | not measurable cheaply | – |
| Originals to the wrong party (rail/08, medicines/11, lpg/03) | see A11 (C33) | 0 | S |
| The same consignment with different gross weights (medicines/09 against 06, 11) | per Consignment/Shipment ID, gross weights agree among documents of the same stage (planned with planned, actual with actual) | 0. ore/02, 03 (plan 1,800 t) against 04, 05 (weighed 1,788.4 t) is a legitimate difference and must not be flagged | S; medium risk without the stage split |
| Contact desk not fitting the role (lpg/03 "Pipeline control", waste/01 "Order desk") | each document's contact desk is one of the desks the issuer's role uses (a role → desk table) | not measured | M; needs a table |
| Vehicles without tare, so the Accord's 40 t road rule is not checked (wood read-through) | every road vehicle in a fleet has `tare_kg`; every road leg's load ≤ 40,000 kg − tare | 17 fleet entries lack `tare_kg`. Road ones: 8-xu V-12, 14-xu FRC-T1, 26-xb V-1, 10-xb B-03/B-05/B-08, 9-xl N-1, 36-xb S-1, 38-xl F-1, 49-xb Q-7, 50-xl H-2. The 40 t rule is applied in two scenarios only (`examples_scenarios.py` l. 3728, 5192) | S check + data for 11 vehicles |
| Text that says "N km" differently from the map | see B1 | 42 statements in example pages, all consistent | – |

## Part B: the larger checks

### B1. Distances and durations against the map (O60)
1. **Guards:** D19, O60, O152, C56 and C58.
2. **What exists:**
   - The generators take distances from `tools/world_map.py`: `leg_km`, `border_km`, `route_km`, `sea_km`, `air_km`.
   - Speeds are constants in the scenarios: ORE_TRAIN_KMH 40, TRAIN_KMH 50, TRUCK_KMH 55, KNOTS 13.5 in
     `world_map`, the lpg truck about 65 km/h, the barge's daylight sailing.
   - Seven per-flow assertions stop the build when the map no longer fits: ore l. 54, rail l. 744, plastics
     l. 1305, sea l. 1827, air l. 2770, reefer l. 13820, and the rail tractor l. 765.
   - `place_list.py` prints leg lengths and `transit_days`.
3. **Missing:** one check over all flows instead of per-flow asserts:
   - (a) every actual or planned departure–arrival pair in the XML fits its leg's km at the mode's speed band;
   - (b) `transit_days` in `world/documents.json` agrees with the XML dates (the reefer had 5 against 2; it is 2 now);
   - (c) the routes' wiki facts in `map.json` (Length, Distance, Timetable) equal `route_km` / `sea_km` / `air_km`;
   - (d) km stated in hand-written texts (parties' and routes' wikis, `documents.json` texts) equal the computed
     value (this overlaps B2).
4. **How it would work:**
   - A speeds table per mode and vehicle in world data (the constants moved out of the scenarios).
   - For (a), pair the Departure and Arrival events of each ShipmentStage, find the leg by the flow and the places,
     compute the hours, and compare with km / speed plus the allowances the story gives (shunt, border stop,
     daylight-only sailing).
5. **Today:**
   - Probe `km.py`: of 42 "N km" statements in example pages, 19 equal a leg or the sea or air length. The other 23
     are speeds, litres per 100 km, the grid's "blocks of 14 km", "rounded to 10 km", and border distances (63 km,
     65 km, 105 km) that come from `border_km`. So 0 real mismatches.
   - Probe `routes.py`: ore 166 against 165.7, sea 1,200 against 1,196, air 1,080 against 1,076, gas 207 against
     206.6. All agree.
   - The ore read-through's "166 against 159" is the line (route) against the leg: both are right, but the texts
     do not say which is which.
   - Expected hits for (a): 0 to a few, because the times come from the same constants.
6. **Effort and risk:** M. False alarms where a stage includes waiting (border stop, overnight at the yard, barge
   moored at night) unless the allowances are data.
7. **Owner decision:** Q10. Should speeds and allowances move from code constants into world data (one table that
   the check and the generators share)? What tolerance applies?

### B2. Each flow's key facts as build assertions (O250, SR-09)
1. **Guards:**
   - SR-09: hand-written sentences copy facts in four places (`examples_scenarios.py` reasons, `world/documents.json`
     texts, the story lines in the decisions file, `note/src/03-world.md`), and nothing compares them.
   - The read-throughs found the stale copies.
2. **What exists:** the seven per-flow asserts of B1 (ORE_ARRIVES and the others), and reasons that are computed from
   the world data.
3. **Missing:** a register of the facts each flow's story states (distances, dates, quantities, amounts, durations),
   each with a computed value, and a check that every text stating it agrees.
4. **How it would work, two options:**
   - **(a) Placeholders:** hand texts write `{fact:ore.km}` and the build fills it in. No copy can go stale. The
     method note keeps literals and is checked by (b).
   - **(b) Assertions:** texts keep their literals. A register (Python, or `world/facts.json`) lists the
     computation, the files, the JSON paths or text anchors, and the expected rendering ("about 159 km").
     The build stops when a text no longer holds the value, or when a computed value changes.

   Either way, the facts come from the data (`wmap`, the flow's deal, `documents.json`), not from a second literal.
5. **Today, numbers with a unit in hand texts (probe, rough):**
   - `documents.json` 54, `map.json` 33, `parties.json` 68, `countries.json` 33, `items.json` 74 (about 260);
   - `note/src/03-world.md` 142;
   - plus the literal reasons in `examples_scenarios.py` (13,800 lines).

   Not every one is a flow fact. A first register of about 10–20 facts per flow (about 250–400 in all) is a
   realistic first scope. The known stale cases are fixed. A first run would probably find a handful of
   wording mismatches of the line-against-leg kind.
6. **Effort and risk:** L. Option (a) is more work up front and has no false alarms afterwards. Option (b) is
   quicker to start and brittle with wording ("about", rounding, words against digits).
7. **Owner decision:** Q11.
   - (a) or (b), or (a) for world data and (b) for the method note?
   - Which texts are in scope: published ones only (world data, wiki), or also `03-world.md` and the decisions'
     story lines (internal)?
   - Which facts are "key": the owner picks per flow, or the read-through list is the start?

### B3. The other goods chains with their yields (O66)
1. **Guards:** D21, O66, and C77, C81, C82, C87, C89, C103, C106, C110.
2. **What exists:** `chain_problems()` for the bench chain only (`items.json` `goods_chain`: the production record of
   Valdara and the ledgers of 6-xb, 26-xb and 1-xl). `check_packages()` does the cotton bales piece by piece.
   No yield or conversion data exists in world data (searched: no "yield" or "conversion" key).
3. **Missing:**
   - for each chain, a period (start, end), the inputs and outputs in the documents, a conversion rate with a
     real-world range (O66 asks for it to be stated like the density in O62), and a check that out ≤ in × the
     maximum yield, where a ledger is not needed;
   - ledgers where totals matter.
4. **How it would work:** a `chains` block in `items.json` (or per flow in `documents.json`) with the input item,
   the output item, the rate range with its source, the period and which documents count. The check sums
   quantities from the built documents (DeliveredQuantity, InvoicedQuantity) and compares them.
5. **Today (probe `qty.py`), first readings:**
   - **Cotton:** 4,500 + 18,000 kg seed cotton (cotton/01, 04) against 6,129 kg lint exported (cotton/16) is 27 %.
     Ginning out-turn is about a third (O66), typically 33–40 %. So 6,129 kg is below what 22.5 t gives. That is
     plausible only if the ginnery keeps or sells part of the lint, or the out-turn is low; no excess.
   - **Ore:** 1,788.4 t at 62 % Fe is about 1,109 t of iron in one monthly train, against castings for a few
     hundred benches (22.2 kg of frames each, a few tonnes). Valdara must make much more than benches. The story
     needs to say so, or the ore volume is a finding.
   - **Ash blanks → slats:** 2,400 blanks on the first load (modification/03, "the first load") against
     96 × 50 = 4,800 slats. That is consistent if the second load stays outside the documents (it does).
   - **Granulate → film:** 120 t of granulate against 480 kg of film sold to Valdara. That is consistent, because
     the film maker has other customers.
   - **Gas:** found in balance (D44).
6. **Effort and risk:** L (data for 7 chains). Low false-alarm risk once the periods are explicit; high without them.
7. **Owner decision:** Q12.
   - The conversion rates and their sources, per chain.
   - Which chains need a ledger and which only a yield plausibility check.
   - The ore: what else Valdara makes from about 1,100 t of iron a month, or whether the train is smaller.
   - The cotton: is a 27 % out-turn in the documents acceptable, or should the documents show more seed cotton or
     less lint?

### B4. Item physics for all items (O62)
1. **Guards:** D20, O62, C69, C40 and C15.
2. **What exists:**
   - `world_items.physics_problems()` (l. 455): parts sum to the net weight, parcels to the gross weight, the
     handling limit (25 kg for one person, 33 kg for two), and a spare part ships in the whole item's parcel. This
     is done for the 2 items with `parts`/`parcels` (bench-serra, -g) and 2 cartons.
   - The pallet data for 8 items (`pallet`: mm, tare, per, stack).
   - `air_load_problems()`: payload, volume, LD3 positions, ULD maxima, the door, dangerous goods.
   - `check_packages()`: the cotton bales.
3. **Missing for the O62 list** (the bench chair and care kit, the desk, the slat and bundle, the side frame, the
   bale, the film, the granulate, the mast equipment, the ore):
   - dimensions × stated density = weight, within a tolerance;
   - parts to whole for the other assembled items;
   - parcels or packages to pallets, and pallets to holds for road, rail and sea (only air is checked);
   - the handling limit for every parcel a person lifts;
   - the 40 t road rule with vehicle tares (A13).
4. **How it would work:** one `physics` sheet per item in `items.json`:
   - dimensions, material, density with its range and source, solid fraction where the envelope is not solid;
   - parts, packaging tare, pallet pattern.

   The check extends `physics_problems` and adds a hold check per leg. The hold check takes its capacities from
   the fleet in `world/parties.json`: the trailer's 33 pallets, the TEU of the ships, the wagons.
5. **Today (probe on `items.json`), densities the data imply:**
   - slat 1800 × 95 × 45 mm at 4.24 kg is 551 kg/m³;
   - ash blank 1830 × 101 × 51 at 5.89 kg is 625 kg/m³ (thermally modified ash is lighter: plausible);
   - timber 700 kg/m³ for oak and ash alike;
   - the bench's parts are 2 × 11.1 + 5 × 4.24 + 0.77 = 44.17 against 44.1 (within the 0.1 tolerance).

   Points to look at:
   - the Marrow bench and chair weigh the same in oak and in ash (21.0 and 10.5 kg). Oak is somewhat denser than
     ash;
   - the Marrow items and the desk have no full dimensions in `dimensions_mm`;
   - the side frame's envelope (730 × 620 × 70 mm, 11.1 kg) gives about 5 % solid ductile iron, which is plausible
     for an open frame but should be stated.

   Expected first-run hits: a few, mainly missing data rather than contradictions.
6. **Effort and risk:** L (data for about 12 items, then the hold check). Low risk once ranges are stated.
7. **Owner decision:** Q13.
   - Densities and their ranges per material (oak, ash, thermally modified ash, ductile iron, PE).
   - Whether oak and ash variants must differ in weight.
   - Which hold capacities count per vehicle (pallet places, volume, payload).

### B5. The HS reasoning list, verified once by a person (O31)
1. **Guards:** D13, O31, C67 and O27.
2. **What exists:**
   - `world_items.check()`: the HS code is six digits, the national tariff extends it, and the CPC fits the HS
     through the official correspondence (`cpc_hs_problem`).
   - `check_classifications()` in `build_examples.py`: the documents' CPC against the HS.
   - The HS 2022 nomenclature is in `world/codelists/sources/hs2022/H6.json` (UN Comtrade: codes and texts, no
     legal or explanatory notes). Nothing records *why* a heading applies.
3. **Missing:**
   - per maker item, the reasoning: the GIR applied, the heading and subheading texts, the section and chapter
     notes relied on;
   - a verification stamp by the owner: date, HS code, and a hash of the reasoning;
   - a build check that every goods item has reasoning, that its code is in H6.json, and that the code and the
     reasoning have not changed since they were verified.
4. **How it would work:** `items.json` `hs_reason` (text) and `hs_verified` ({"by": "owner", "date", "hs", "hash"}).
   A generated table (an internal report, not published) lists the 34 items for the one review.
5. **Today:**
   - 34 maker items carry an HS code (14 resales inherit theirs). All 34 codes exist in HS 2022 (probe). None has
     reasoning. The check would report 34 missing until the list is written and verified.
   - Items that need the closest reading:
     - bench-casting 9401.99, the side frame as a part (O27: Section XV notes, Note 1(d) to Chapter 94);
     - slat-1800 and its bundle 9401.91, parts of seats, of wood (against 4409/4421);
     - seed-cotton 5201: seed cotton and ginned lint share the subheading in the data;
     - tc-generator 2844.43: the Tc-99m generator (against 2844.44 and 3006.30);
     - marrow-care-kit 3210 (a care oil or wax might be 3405 or 1518);
     - marrow-seat-pad 9404.90.
6. **Effort and risk:** M (writing 34 reasonings, the stamp and the check). No false alarms.
7. **Owner decision:** Q14.
   - One sitting to verify the list.
   - Whether reasoning may rest on own knowledge of the HS notes, or only on a verified source (the WCO's legal
     notes are not in the repository).
   - Whether a change of an item's HS code must re-open the verification.

## Proposed sequence

1. **Cheap guards (one batch, about a day):**
   - A1 offsets right;
   - A3 flight block time as data;
   - A5 tax currency (after Q5);
   - A7 origin statement (presence part);
   - A8 lots and serials across flows;
   - A9 payments between countries;
   - A10 contract terms and reminder interest;
   - A11's `ShippingOrderID` and originals checks, and the totals arithmetic;
   - A12 provenance hashes (adds the 2 missing hashes).
2. **Checks with hits to fix:**
   - A2 desk hours (14 hits, after Q2);
   - A4 published text (Manifest Values and OASIS sample reasons, 52 pages, after Q3; "trade accord" 1);
   - A13 premise reasons ("quoted in its order", 3 hits);
   - A13 vehicle tares (11 road vehicles, then the 40 t rule over all road legs).
3. **Fixers into assertions (after Q1):** `tax_arithmetic`, `currency_cleanup`, `shipment_weights`,
   `national_tariffs` report instead of repairing, or report when they repair.
4. **A6 tax treatment against movement** (after Q6).
5. **B1 distances and durations:** speeds and allowances into world data (after Q10), then the one check over all
   legs.
6. **B2 key facts** (after Q11), building on B1's computed values.
7. **B4 item physics:** the data sheets first (after Q13), then the hold check.
8. **B3 goods chains:** per flow with its balance, after Q12 and Q8 (production records).
9. **B5 HS reasoning:** write the 34 reasonings, the owner verifies once (Q14), then turn on the check.

Each step follows the standing rule: check, full build, deploy to `main`. A check that removes an element's last
example adds its coverage-register row in the same commit.

## Questions for the owner

- **Q1 (fixers): decided (owner, 2026-11-21): A, turn them into checks that stop the build; fix the generators at the source.** should the build functions that silently repair content (`tax_arithmetic`, `currency_cleanup`,
  `shipment_weights`, `national_tariffs`) stop the build instead, so that the generator is fixed at the source?
- **Q2 (desk hours, O269):**
  - Do the stated hours bind every document, or only those a person issues? A despatch advice sent by the system
    when the truck leaves at 20:05 is one case.
  - May desks have hours of their own?
- **Q3 (two layers):** are reasons that explain a value by UBL's own principles ("UBL 2.5, 2.2.2 Manifest Values",
  41 pages) or by the OASIS samples ("as in the OASIS example", 11 pages) allowed in published world text?
- **Q4 (EN 13556, O156):**
  - Is a secondary source enough, given that the standard itself is paid?
  - Would its name be allowed in world text under O265, or only its codes?
- **Q5 (O262):** does "VAT actually charged" exclude invoices at 0 % or outside the scope (tender/32, 33, 39 carry
  XUF and a TaxTotal of 0)?
- **Q6 (tax treatment):** is an export proved by a leg of the flow only, or also by delivery terms with a place
  abroad, where the flow has no leg?
- **Q7 (origin statement):** may a reseller make the statement (sea/22, air/11)? Is it right on air/11 at all,
  where the goods move under Valdara's transit declaration?
- **Q8 (O64 scope):** should the other makers' lots and serials become production records in world data, like
  Valdara's?
- **Q9 (calendar):** must deliveries and receipts also fall on the receiving party's working days?
- **Q10 (O60):** should speeds and allowances (border stop, shunt, night mooring) move into world data, and with
  what tolerance?
- **Q11 (O250):**
  - placeholders or assertions;
  - which texts are in scope (published world data, wiki, `03-world.md`, story lines);
  - who picks each flow's key facts.
- **Q12 (O66):**
  - conversion rates and their sources;
  - ledger or plausibility check per chain;
  - what Valdara makes from about 1,100 t of iron a month;
  - whether the cotton's 27 % out-turn in the documents is acceptable.
- **Q13 (O62):**
  - densities and ranges per material;
  - should oak and ash variants differ in weight;
  - which hold capacities count.
- **Q14 (O31):**
  - one sitting to verify 34 reasonings;
  - may reasoning rest on own knowledge of the HS notes;
  - does a change of an HS code re-open the verification.
