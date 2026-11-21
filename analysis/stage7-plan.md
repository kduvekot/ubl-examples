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
- **Built (2026-11-21), Q1:** the four fixers in `tools/build_examples.py` are checks that stop the build and
  repair nothing. `tax_arithmetic()`: a subtotal's taxable amount is its lines plus the document's charges less its
  allowances; a document-level allowance or charge in a one-category document states its category. Found 5 documents:
  retail/08 (the order's promotion allowance: no category, the subtotal before it), furniture/10 (the repeat-order
  discount not in the subtotal), furniture/15 (the disposal charge not in it), wood/02 and wood/03 (the pallet charge
  without its category); fixed in `examples_scenarios.py` (`with_allowance()` for every document with a tax total,
  the furniture orders and the wood quotation and order). `currency_cleanup()`: no currency equal to the document's,
  no pricing currency the prices are not in and no pricing rate without one, no alternative payment currency without
  an amount in it, no idle rate in transport documents, statements and remittances. Found 41 values: the payment
  currency of every cross-border kit invoice (`examples_kit.invoice()`), road/15's payment rate, sea/26's alternative
  currency, cotton/04 and 05's pricing, payment and alternative currencies (`cotton_currencies()`, removed), cotton/08's
  requested invoice currency, packaging/09's pricing rate, and the free rates of the forwarding instructions, bills of
  lading, the air waybill, the factor's statement and the sea remittance; all dropped at the source. `national_tariffs()`:
  a national tariff code only in a document of its own country. Found 54 goods items: `item()` now gives the
  subheading only where `document_country()` of the document being built (`CURRENT_DOC`) is the maker's. `shipment_weights()`:
  a shipment states its gross weight only with its transport equipment, the goods plus the tares or the equipment's
  gross weights; else the goods' weight is on the consignment or the goods items. Found 59 documents: the kit's
  despatch advice, waybill and export declaration put the goods' weight on the consignment, the import declaration on
  its goods items (`import_consignment()` where a scenario names a consignment), and `examples_kit.shipment_gross()`
  states the shipment's weight with the equipment (road/08, rail/06, rail/08, sea/10, sea/14, sea/15, lpg/03,
  reefer/07). Published values unchanged (only reasons reworded).
- **Built (2026-11-21), O274 (owner):** an amount collected for a third party (CollectionInvoiceLine) is outside the
  lines' sum and the tax and is added to the amount payable only. The utilities bills 06, 09, 11 (the city's sewage
  levy) now do so (`collected_apart()` in `examples_scenarios.py`): LineExtensionAmount, TaxExclusiveAmount and
  TaxInclusiveAmount without the levy, no tax subtotal of category O for it (the levy's line keeps category O), the
  payable amount unchanged. `check_totals()` accepts only this rule.

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
8. **Built (2026-11-21):** `check_time_places()` in `tools/build_examples.py`, per document: every time's offset is that of the place its aggregate or the one above names (UN/LOCODE, GLN, address country, read from the XML with `xml_place_country()`); a delivery that names no place is where it is received (DeliveryParty, else the document's delivery customer or buyer); a cited document's IssueTime has the offset of that document's own issue time; else the issuer's. Found 5: four were right but undocumented in the XML (delivery periods of air/02, 06, 08 in island time; air/07's cited order) and are now resolved by the delivery and citation rules; sea/16's requested arrival at the Selanu fairway buoy named no country, so its OccurrenceLocation now carries the country XL (scenario).

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
8. **Built (2026-11-21):** `check_desk_hours()` in `tools/build_examples.py`, per flow over the XML: the IssueTime lies
   within the hours of the issuer's desk the document's contact names (matched by its e-mail address; a desk keeps
   hours of its own, `identity.desks.<k>.hours`, else the contact's), else the main contact's (`party_desks()`,
   `desk_hours()`). Messages a system sends on its own are exempt by type, with the reason, in `SYSTEM_SENT`
   (DespatchAdvice, TransportationStatus, TransportProgressStatus, GoodsItemItinerary): this covers air/07 and air/08,
   furniture/19 and plastics/08 of the probe. Found 10 (the other 4 of the 14 were despatch advices or already moved):
   road/02, retail/01, 08, 20, air/01, 10, furniture/04, 07, mast/05, medicines/02. Fixed at the source: a time the
   scenario does not give is put within the issuer's hours (`issuer_hours()`; outside them the generated time moves
   by minutes to just after the opening or before the closing); retail/08 (the store's order, 09:15, once the buying
   office has opened) and air/01 (Velumi's order change, 09:10) in the scenarios; the catalogue retail/02 is issued at
   10:00, after the store's request (`CATALOGUE_REVISIONS`). No desk needed hours of its own: every hit was a person's
   document at the front office.

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
8. **Built (2026-11-21):** the timetable is world data: `world/map.json` route `air`, key `flight` (block times east 2.75 h and west 3.0 h, taxiing, climb and descent, cruising speed); `world_map.flight()` derives the still-air time from `air_km()` and stops the build when a block time no longer keeps its margin, `world_map.clock_ahead()` the island's clock difference from the countries' timezones, `world_map.duration()` the "2 h 45" form. `examples_scenarios.py` reads `FLIGHT_BLOCK_EAST`, `FLIGHT_CLOCKS` and the reason text from them (air, mast, medicines). The Encyclopedia's figures are placeholders filled by `build_wiki.flight_values()`: `{flight_km}`, `{flight_east}`, `{flight_west}`, `{flight_still_air}` in the air route's facts, lead and section and in Kelaro Air Cargo's "Operations" (the route's infobox facts are now filled too). The check is `check_flight_times()` in `tools/build_examples.py`: every air ShipmentStage's planned or estimated departure and arrival are exactly the block time of their direction apart, an actual flight no longer. Found 0. The westbound 3 h 00 existed only as wiki text; it is now data beside the eastbound one (no document flies west).

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
8. **Built (2026-11-21):** the two sources are reworded in `examples_kit.py`: the payable amount (`monetary_total()`,
   41 pages) is "stated in full so that it books the amount without working it out", the remittance's debit line
   (`remittance()`, 11 pages) says that a remittance lists each invoice paid on its debit side and a discount taken
   on its credit side. `tools/check_published.py` fails on "Manifest Values", "UBL 2.5, 2.2.2" and "OASIS example"
   (FAIL) and on the Trade Accord in lower case (`PROPER_NAMES`: "trade accord", "Trade accord", "trade Accord"),
   in the pages and in the world's own code lists. Fixed: sea/03's "trade accord's network" (scenario).

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
8. **Built (2026-11-21):** `check_tax_currency()` in `tools/build_examples.py`, per document: a TaxCurrencyCode or
   TaxExchangeRate only on an Invoice, CreditNote, SelfBilledInvoice, SelfBilledCreditNote, DebitNote or
   PurchaseReceipt (`TAX_CURRENCY_DOCS`) with a tax amount above 0. Found the 3: `ferra_tax()` in
   `examples_scenarios.py` adds the tax currency, its rate and the tax total in ferra only where tax is charged, so
   tender/32, 33 and 39 carry none. CreditNote/TaxCurrencyCode and CreditNote/TaxExchangeRate are registered in
   `analysis/coverage-register.md` (coverage 4623 → 4621); wood/08 keeps the invoice's.

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
8. **Built (2026-11-21):** every leg in `world/documents.json` names the sales whose goods it carries (`"carries"`: the order and the invoice, for the store's return leg the credit note; empty for the carnet's and the waste's legs, which carry no sale). `tax_problems()` in `tools/world_movement.py` (run by `check_world.py`), per order, invoice or note of a seller in the Accord, over its VAT and sales-tax categories (not withholding or excise): an export code only where a leg that carries it (or the order or invoice it refers to) goes from the seller's country to another, its delivery terms name a place abroad (UN/LOCODE or the world's GLN) or it cites an export declaration of the flow; TRANSIT only where the legs bring the goods in from abroad and on abroad; a supply taxed in another country (the sawmill's slats taxed in Urvania) only where its legs stay inside that country; a domestic code on goods a leg takes abroad is an export. 66 categories, found 0 (packaging, mast and medicines have their border legs, now linked to their sales); mutation-tested (a leg removed, a transit leg made domestic, a domestic resale sent abroad: each caught).

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
8. **Built (2026-11-21):** `origin_problems()` in `tools/build_examples.py`, over all flows' XML at the end of a full
   run: an invoice carries the statement ("preferential origin under the Trade Accord" in a note) exactly when seller
   and buyer (their addresses) are in two Accord countries, its goods are of one Accord origin (`items.json`, through
   the item's name) and a leg of the flow ends in the buyer's country coming from another, and the flow has no
   certificate of origin; no other kind of document carries it; an import declaration with a PreferenceCriterionCode
   cites an invoice with the statement or a certificate of origin, the exporter's pro forma invoice where nothing is
   sold, or the entry it releases (a PreviousCustomsDeclaration whose claim holds). A reseller may make it (Lumeway,
   air/11, sea/22). Found 2: modification/05 (the blanks sent for processing, no sale) and wood/07 (their release);
   the pro forma invoice's reference in modification/05 now says it carries the sawmill's statement on origin as their
   exporter, and wood/07 rests on that entry. The 11 invoices of the probe hold.

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
8. **Built (2026-11-21):** `world/items.json` `production_records`: the records of the sawmill (blank lots
   MDS-BL26-0109 and -0116, the second load's lot outside the documents; slat lots MDS-L26-0119 and -0126 with the
   plant's kiln charges TWM-K1-26-03/04 and the blank lot each was made from), the wood modification plant (its
   charges, recorded with the owner's lots), Rinova (RR-PE-0417), the ginnery (SCG-L26-017, 27 bales, 6,129 kg), the
   cooperative (HRW-L26-0401 to 0451 with their growers), the vaccine maker (the three NLB lots with expiry dates) and
   the isotope maker (serial HVI-TCG20-26-0137); each with its patterns. Valdara's stays in `goods_chain`. The
   generator still writes these numbers as literals (`examples_scenarios.py`, `MOD_CHARGES`, `MED_LOTS`, `rf_lots`,
   `PE_LOT`); the check holds them to the records. Check: `tools/world_goods.py` `lot_problems()` (run by
   `check_world.py`): every LotNumberID, SerialID and ProductTraceID, and every number in a maker's form in any text,
   is in the record, on the same item (via SellersItemIdentification, a resold item as its maker's), with the same
   ManufactureDate and ExpiryDate; no recorded number in another form (the same digits and letters under the
   maker's prefix); a line ships no more than its lots made; a line with serials has one a unit (or one a rejected
   unit); over all flows a lot leaves its maker in no more than it made; no document quotes a lot before it was
   made; a lot made from another is made after it and takes no more than it made. **Found:** nothing in the
   documents once the records were set (the probe's 18 lots and 21 serials all match); the text scan first flagged
   the weight statement number SCG-PR-26-L017, which is a document of its own, not the lot in another form (the
   rule now compares letters as well as digits).

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
8. **Built (2026-11-21), the payments part:** `check_payment_dates()` in `tools/build_examples.py`, per document: a bank payment (credit transfer, direct debit, or a prepayment with no means stated) is paid (PaidDate, PaymentDate) on a business day of both the payer's and the payee's country and received (ReceivedDate) on one of the payee's; a payment at the till (cash, cheque, cards: `AT_THE_TILL`) on a day the payee works. Found 2: sea/22 and sea/25, the deposit paid on Friday 8 May and received on Saturday 9 May; it is now received on Monday 11 May (`kit.due_day`, scenario), and sea/22's reason that it was paid "the day after the order was accepted" now agrees with sea/25 and the order response (the same day). Deliveries and receipts wait for Q9.
9. **Built (2026-11-21), deliveries and receipts (Q9):** `check_delivery_days()` in `tools/build_examples.py`, per
   document: every ActualDeliveryDate, a receipt advice's ReceivedDate and every completed ActualDeliveryTransportEvent
   or ReceiptTransportEvent falls on a working day (`working_day()`, the party's working week and holidays) of the
   party that receives the goods: the DeliveryParty or ConsigneeParty its aggregate or one above names, else the
   document's delivery, consignee or buyer role (`RECEIVING_ROLES`), for a receipt advice its issuer. A carrier's
   movements on the way are free. Found 0 (23 delivery dates, the receipt advices and the delivery events hold).

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
8. **Built (2026-11-21):** `check_plan_terms()` in `tools/build_examples.py`, per flow: an invoice or debit note of a carrier to the user of its TransportExecutionPlan carries the plan's payment terms. Found 1: retail/16, Bayforth's freight invoice under the plan retail/23, billed on its standard terms; it now uses the plan's term (`terms="plan"`, 30 days from the consignment note, due 29 May). `check_reminder_interest()`, per document: a reminder line charging for a period starts the day after the cited invoice's due date, and its amount is the surcharge per month begun (PenaltySurchargePercent) or the simple annual interest per day (the reminder's PenaltyInterestRate) on the principal line. Found 0 (energy/08, utilities/10 hold).

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

- **Built (2026-11-21):** `check_totals()` in `tools/build_examples.py`, per document, over the XML, repairing nothing: each tax subtotal's tax is its taxable amount at its rate, each TaxTotal and WithholdingTaxTotal the sum of its subtotals, and a bill's LegalMonetaryTotal adds up (lines, allowances, charges, tax, prepaid, withholding, rounding). Found 0 once amounts collected for a third party are counted: utilities (06, 09, 11) counts its CollectionInvoiceLine in the lines' sum, the cotton gin's self-billing (cotton/04, 05) adds it to the payable amount only; the check accepts both and the difference is reported to the owner.
- **Built (2026-11-21):** `check_emissions()` in `tools/build_examples.py`: a document's EnvironmentalEmission with a factor and a base is their product to the precision of the value (lpg/03: 0.268 × 1,700 kWh = 456 kg). Found 0.
- **Built (2026-11-21):** `check_shipping_orders()` in `tools/build_examples.py`: every ShippingOrderID is the ID of an example ForwardingInstructions (`doc_types()`). Found 0.
- **Built (2026-11-21):** `check_originals()` in `tools/build_examples.py`: ORIGINALHANDED goes to the ConsignorParty, ORIGINALWITHGOODS to the ConsigneeParty, and a note "N originals" counts those plus the carrier's own. Found 0.
- **Not built (2026-11-21):** the customs offices (C12, C23) have no ID or country to check. The C11 and C15 assertions are built with Q1 (section 0: `currency_cleanup()`, `shipment_weights()`).

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
9. **Built (2026-11-21), Q4:** the Accord's `Wood` list in `world/codelists/lists.json` has the timber trade's codes
   QCXE (European oak, Quercus robur and Quercus petraea) and FXEX (European ash, Fraxinus excelsior) in place of OAK
   and ASH, without the standard's name; the four Marrow items' variant attribute in `world/items.json` uses them
   (the makers' own item-number suffixes, ExtendedID OAK and ASH, are their numbering, not the list, and stay).
8. **Built (2026-11-21), the provenance part:** `provenance_problems()` in `tools/build_codelists.py`, run by `--check` (so by `check_world.py`): every file under `world/codelists/sources/` has its SHA-256 in `PROVENANCE.md` or `PROVENANCE-second-round.md` and still has it. The two missing hashes (IATA Table 9.3.A, the ATR fact sheet) are added below their rows in `PROVENANCE.md`. Found 0 after that. EN 13556 waits for Q4.

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

- **Built (2026-11-21):** `check_reason_premises()` with `PREMISES` in `tools/build_examples.py`, per document over every reason: "quoted in its order" needs an OrderReference; "Issued on despatch" / "Issued on delivery" need the issue date to be a stated ActualDespatchDate / ActualDeliveryDate where the document states one. Found 3 (ore/06, road/14, cotton/17). Fixed at the source: `examples_kit.invoice()` says "quoted in its order" only where the invoice cites an order and the buyer ordered from this seller in the flow, else "contract or booking".
- **Built (2026-11-21):** `consignment_weight_problems()` in `tools/build_examples.py`, over all flows at the end of a full run: one gross weight per Consignment or Shipment ID among the planning documents (`PLANNING_DOCUMENTS`) and one among the others. Found 0.
- **Built (2026-11-21):** the 11 road vehicles have an empty weight by part in `world/parties.json` (`tare_kg`; the vans and the box truck also `max_gross_kg`). `fleet_weight_problems()` in `tools/world_parties.py` (run by `check_world.py`) requires `tare_kg` for every road vehicle, a payload left under the Accord's 40 t or the vehicle's own maximum, and a road vehicle for every carrier of a road leg; `check_road_weights()` in `tools/build_examples.py` checks that a document's shipment or consignment on a vehicle named by its plate stays within that limit with the vehicle's tare. Found 0.
- **Not built (2026-11-21):** the contact desk against the issuer's role needs a role → desk table first; the reason whose number differs from the value has no generic check.

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
8. **Built (2026-11-21):** `world/map.json` top-level `speeds` (per mode and vehicle, km/h with a reason: road `truck` 65, `delivery_truck` 60, `container_chassis` 55; rail `container_train` 50, `ore_train` 40; river `barge` 11; sea `feeder` 13.5 kn = 25.0 km/h; air `freighter` 500, the air route's `flight` keeping taxiing, climb and descent) and `allowances` (hours with a reason: `shunt` 0.25, `driver_break` 0.75, `border_path_rail` 5, `morning_placement` 19.5, `second_run` 2, `stacking` 0.17, `daylight_pilotage` 12; `night_mooring` as sails/moors times). The real set is the documents' own (it changes no document); the 3D map's figures (truck 65, train 80, barge 12, ship 30, aircraft 750) are to follow it, read by the map session from these keys. `world_map.speed(mode, vehicle)` and `world_map.allowance(name)` serve the generators (the ore, road, rail, plastics, air, sea, reefer and lpg constants are gone; `flight()` takes the freighter's cruise from the table) and the place list's timing column. The seven per-flow asserts are removed. A leg names its speed class and allowances in `world/documents.json` (`"timing"`: `speed`, `allowances` as a list or per kind of time). `time_problems()` and `route_problems()` in `tools/world_movement.py`: every departure–arrival pair of a shipment stage (same kind, in one stage or once per flow across its documents) against the leg's km at its speed plus its allowances, ±15 % or 30 minutes; each despatch advice's estimate against `door_to_door_days` or the main leg's `transit_days`, and that many days hold the leg; the routes' Length, Distance and Passage facts against `route_km`, `sea_km`, `air_km` and `sea_hours`. 11 pairs, 9 estimates, 4 facts: found 0 once the legs named their allowances (rail: the border path and the morning placement, the haulage's second run; sea: the wait for daylight pilotage). (d), the km in hand-written texts, stays with B2.
9. **Built with it (2026-11-21), O278:** the ore train's 30 ore wagons (the documents' "30 wagons of about 60 tonnes") with 62 t payload each, the container wagons 66 t, Fiumella IV a deadweight of 2,100 t, the timber truck S-1 and the farm tractor F-1 their maximum gross weights; the rail haulage leg states its two runs (`runs`, and rail/08's pre-carriage Instructions), so the `KNOWN` entry in `tools/world_goods.py` is gone; the nine road legs of the forwarder and the furniture maker name their vehicle (`"vehicle"`). The load check now checks wagons, ore, deadweight and those legs: 0 problems, 0 notes. **Also built:** the care kit (Q14) is HS 3405.20 with CPC 35333 and its reasoning (Bayvarra keeps no national tariff list, so no national line); "despatch" for UBL concepts in the generators and the world data, and `tools/check_published.py` fails on "dispatch advice/date/note/office/area …", "dispatched to" and "date of dispatch" (O277 (3)).

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
8. **Built (2026-11-21):** `world/items.json` `chains`: cotton (seed cotton to lint, 33 to 40 %, FAO's
   technical conversion factors and the ICAC Cotton Data Book 2021), ore (62 % Fe, 35 % scrap in the melt, foundry
   yield 45 to 80 %, from the casting-yield paper: at most 0.76 kg of castings a kg of ore), slats (one slat a blank,
   with the second load's blank lot from the sawmill's record), film (granulate to film and bags, at most its
   mass), gas (a balance) and the bench (its ledgers in `goods_chain`). Sources with SHA-256 in
   `world/codelists/sources/PROVENANCE-second-round.md` (cited, not copied). Check: `tools/world_goods.py`
   `chain_problems()`: out ≤ in × the highest rate (a balance: equal) from the built documents' line quantities,
   every document counted dated within the chain's period, a rate in steps the product of its steps;
   `chain_figures()` lists the rates with `--notes`. **Found:** the probe's 27 % for cotton counted the season
   advance (cotton/01, a prepayment of 4,500 kg) as seed cotton; the seed cotton delivered is the 18,000 kg of
   cotton/03, so the out-turn is 34.0 %, inside the range: no change to the documents. Ore 0.4 % (benches are a few
   tonnes of a month's iron), film 0.6 %, slats 4,800 of 4,800, gas 39,200 MWh in balance. Story (for
   `world/parties.json`, another session): Valdara as a broad iron works, and the ginnery keeping part of its lint
   for the home market.

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
8. **Built (2026-11-21):** `world/items.json` `materials` (oak 720, ash 670, thermally modified ash 585, ductile
   iron 7,100, polyethylene 920, the stripper, each with a range and its source: the Wood Handbook FPL-GTR-282, the
   Ductile Iron Society's figures, 21 CFR 177.1520 and ASTM D883's terms, the IPCC's calorific value for gas) and a
   `physics` sheet on all 34 items with a weight (after `gross_kg`): by envelope (dimensions, material, solid
   fraction: the side frame 5 %, the Marrow bench 13.1 %, the chair 7.6 %, the desk 7 %), by sheet (the garment bag:
   two layers of 12 µm), by volume, mass or energy, by contents or the items of a pack, by parts; and who lifts the
   package (one, two, machine, with an aid where above the limit). Check: `tools/world_goods.py`
   `physics_problems()`: the implied density within the material's range, a unit by mass, volume or energy as its
   unit says, contents and packs sum to the whole, a part's weight is its item's, oak and ash variants weigh as their
   densities (±2 %), each lifted package within ISO 11228-1 (25 kg one, 33 kg two) or with its aid;
   `load_problems()`: each vehicle the documents name (plate, vessel, train) against the fleet in
   `world/parties.json` (tares plus load within 40 t or its maximum gross weight, a tank within its maximum load,
   pallets within a curtain-sider's floor of 13.6 × 2.45 m, one container on a chassis, a train's containers one to a
   wagon, a ship's TEU), and a road leg whose vehicle no document names with its carrier's only road vehicle against
   the flow's largest despatch. **Fixed:** the Marrow bench and chair in oak are 7 % heavier than in ash (22.6/25.6
   and 11.3/12.3 kg net/gross), the timber 720 kg (oak) and 670 kg (ash) a cubic metre: furniture/12 (295.85 kg,
   its reason now from the data) and furniture/19 (985.4 kg) follow. **Found, not fixed (generator):** rail/08
   puts both containers on the one container chassis of the rail carrier with no second run stated (listed as a
   known note). **Capacities missing in `world/parties.json`:** payload of the container and ore wagons (the ore
   train lists 4 ore wagons for 1,788.4 t), the barge's deadweight (only gross and net tonnage), the timber truck's
   and the farm tractor's load limits; the forwarder's and the furniture maker's road legs have several vehicles and
   no document names one. The 40 t rule has no hits (reefer/07 is the closest, 39,528 kg).

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
8. **Built (2026-11-21), awaiting the owner's sitting:** the WCO's HS 2022 legal texts (GIR, section and chapter
   notes of the chapters used and weighed) in `world/codelists/sources/hs2022-notes/` (provenance in
   `PROVENANCE-second-round.md`); `hs_reason` {gir, heading, subheading, notes, text} and `hs_verified: null` on the
   34 maker items in `world/items.json` (not published); `world_items.hs_problems()`: reasoning present, code in
   H6.json, heading and subheading match the code, a stamp still matching code and hash, else the build stops;
   while unverified, one note only. `python3 tools/hs_review.py [-o .review/hs-review.md]` prints the table,
   `--stamp <id> ...` (or `--stamp --all`) records the verification. Doubts for the sitting: the care kit (3210
   against 3405.20 or 3208), seed cotton (52.01 rests on the heading's wording; the Explanatory Note is not a
   source), the slats as parts (identifiability rests on the Explanatory Notes); no code changed.

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
- **Q2 (desk hours, O269): decided (owner, 2026-11-21): A,** the stated hours bind every document; a party may give a desk its own hours (dispatch, goods-in, emergency); messages a system sends on its own (despatch advice on departure, status messages) are exempt and marked so; the check reads each document's contact and that desk's hours; the 14 hits fixed at the source.
  - Do the stated hours bind every document, or only those a person issues? A despatch advice sent by the system
    when the truck leaves at 20:05 is one case.
  - May desks have hours of their own?
- **Q3 (two layers): decided (owner, 2026-11-21): A, both go ("the UBL examples have no meaning in this world"):** the 41 "(UBL 2.5, 2.2.2 Manifest Values)" reasons state the fact in world terms without the section; the 11 "as in the OASIS example" references are dropped or replaced by the world's own reason; the published-text check gets both patterns. are reasons that explain a value by UBL's own principles ("UBL 2.5, 2.2.2 Manifest Values",
  41 pages) or by the OASIS samples ("as in the OASIS example", 11 pages) allowed in published world text?
- **Q4 (EN 13556, O156): decided (owner, 2026-11-21): A, the Accord's own `Wood` list stays, "but you can reuse the same codes":** its codes become QCXE (European oak) and FXEX (European ash), the four-letter codes of the trade's wood nomenclature, without naming the standard in world text; O156 closed.
  - Is a secondary source enough, given that the standard itself is paid?
  - Would its name be allowed in world text under O265, or only its codes?
- **Q5 (O262): decided (owner, 2026-11-21): A,** zero tax is not "charged": tender/32, 33, 39 drop the tax currency and rate; the check allows them only where a tax amount is above 0; CreditNote/TaxCurrencyCode and CreditNote/TaxExchangeRate get register rows. does "VAT actually charged" exclude invoices at 0 % or outside the scope (tender/32, 33, 39 carry
  XUF and a TaxTotal of 0)?
- **Q6 (tax treatment): decided (owner, 2026-11-21): A, plus the link:** every leg in `documents.json` names the documents whose goods it carries (the order or the invoice), so the check follows each sale's own leg; delivery terms with a place abroad or a cited export declaration remain accepted evidence. (The flows packaging, mast and medicines do have their border legs; the probe's problem was the missing link between leg and sale.) is an export proved by a leg of the flow only, or also by delivery terms with a place
  abroad, where the flow has no leg?
- **Q7 (origin statement): answered (owner, 2026-11-20, with the air batch):** a reseller may make the statement where its sale crosses an Accord border (Lumeway on air/11 and sea/22, as the exporter in the Accord's sense); built. may a reseller make the statement (sea/22, air/11)? Is it right on air/11 at all,
  where the goods move under Valdara's transit declaration?
- **Q8 (O64 scope): decided (owner, 2026-11-21): A,** production records for every maker that numbers lots or serials (Tostara, the sawmill, Rinova, the textile mill, Quillmoor, the generator's maker …), as Valdara's, in `world/items.json`; the lot/serial check and the goods-chain check cover them. should the other makers' lots and serials become production records in world data, like
  Valdara's?
- **Q9 (calendar): decided (owner, 2026-11-21): A, checked:** deliveries and receipts fall on a day the receiving party works, by its working week; carriers' movements in between are free. must deliveries and receipts also fall on the receiving party's working days?
- **Q10 (O60): decided (owner, 2026-11-21): A, with B for the 3D map:** one table of real speeds and allowances per mode and vehicle type in the world data, read by the generators, one check over all flows (±15 % or 30 minutes, whichever is larger; the route texts too) and the 3D map; the seven per-flow asserts go. The 3D map keeps its compression as one visible rule, map speed = factor × √(real speed ÷ truck speed) (MO015), applied to the shared real speeds. Today the documents and the map disagree (truck 55/65, train 50/80, ship 25/30 km/h, aircraft block 390/750 cruise): one set of real speeds, chosen when the table is built. should speeds and allowances (border stop, shunt, night mooring) move into world data, and with
  what tolerance?
- **Q11 (O250): decided (owner, 2026-11-21):** (a) placeholders (`{fact:…}`) for the published world data and encyclopedia texts, assertions for the method note; (b) the internal story lines in the decisions file are not checked; (c) start with the read-throughs' facts (about 10–20 per flow) and grow the register whenever a text adds a number.
  - placeholders or assertions;
  - which texts are in scope (published world data, wiki, `03-world.md`, story lines);
  - who picks each flow's key facts.
- **Q12 (O66): decided (owner, 2026-11-21):** (a) a yield plausibility check for every chain (output ≤ input × the maximum yield, a stated range with a public source), ledgers only where totals matter (the bench chain); (b) Valdara is a broad iron works (other castings such as manhole covers, gratings, machine parts are its main business; benches one line), the ore train stays, the story and Valdara's encyclopedia text get the sentence; (c) the cotton's 27 % out-turn in the documents is accepted: the ginnery keeps part of the lint for the home market; the check uses 33–40 % as the maximum; (d) conversion rates from public sources (e.g. FAO for ginning, foundry yields for iron to castings, timber yields for ash).
  - conversion rates and their sources;
  - ledger or plausibility check per chain;
  - what Valdara makes from about 1,100 t of iron a month;
  - whether the cotton's 27 % out-turn in the documents is acceptable.
- **Q13 (O62): decided (owner, 2026-11-21):** (a) one density per material with a range and a public source (the US Forest Products Laboratory's Wood Handbook for the woods: oak about 720, ash about 670, thermally modified ash about 550–620 kg/m³; ductile iron 7,100; polyethylene 920–960), the check dimensions × density × solid fraction = weight within a tolerance; (b) oak and ash variants differ in weight (oak about 7 % denser), the documents' weights follow; (c) hold capacities from the fleet data (pallets per trailer, TEU per ship, wagons per train) and a load check per leg.
  - densities and ranges per material;
  - should oak and ash variants differ in weight;
  - which hold capacities count.
- **Q14, the stamp (owner, 2026-11-21: "get it locked in", confirmed "stamp it"):** all 34 HS reasonings verified by the owner and stamped on 2026-11-21 (`tools/hs_review.py --stamp --all`), the care kit as 3405.20; a changed code or reasoning now stops the build until re-verified.
- **Q14, the care kit (owner, 2026-11-21): A, HS 3405.20** (polishes and creams for the maintenance of wooden furniture): the kit is a care product, its oil refreshes a finish; the item data, its CPC and national line, its reasoning and the furniture documents that carry it change with the next batch.
- **Q14 (O31): decided (owner, 2026-11-21): all three, behind the scenes ("facts matter, and HS is open for interpretation; this grounds the world's interpretations; no need to show them publicly"):** (a) the WCO's free HS 2022 section and chapter notes fetched into `world/codelists/sources/` with their SHA-256; (b) a reasoning per item (rule, heading, notes cited) in the item data, unprinted, and one internal table the owner verifies in one sitting, each item stamped (date, code, hash of the reasoning); (c) a changed code or reasoning breaks the stamp and the build stops until re-verified. Nothing of it is published.
  - one sitting to verify 34 reasonings;
  - may reasoning rest on own knowledge of the HS notes;
  - does a change of an HS code re-open the verification.
