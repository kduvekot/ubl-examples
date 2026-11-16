"""Cause metadata: merges of rule keys, stage, kind, decision, source place and the text of each cause."""

MERGE = {
    'STOCK': 'MASTERCOPY', 'PREFIX2': 'PREFIX', 'BENCHWEIGHT': 'BENCHPHYS', 'KNOCKDOWN': 'BENCHPHYS',
    'INCOPLACE': 'PLACES', 'UTILESTIMATE': 'UTILAMOUNTS', 'UTILEXCISE': 'UTILAMOUNTS', 'TEPPERIOD': 'TEPTERMS',
    'CUSTOMSISSUER': 'CUSTOMSDECL', 'PREVDECL': 'CUSTOMSDECL', 'CUSTOMSOFFICE': 'CUSTOMSDECL', 'CUSTOMSGOODS': 'CUSTOMSDECL',
    'FARMADDR': 'FARM', 'FARMREG': 'FARM', 'CATTERRITORY': 'CATALOGUE', 'FORWARDER': 'ROLEDUP',
    'ZEROTAX': 'TAXTOTALS', 'TAXABLEALLOW': 'TAXTOTALS', 'WOODUNIT': 'WOOD', 'WOODISOL': 'WOOD',
    'PACKAGINGISOL': 'PACKAGING',
}

KINDS = ['encoding', 'master data', 'world rule', 'cross-flow story', 'generator mechanism', 'flow story', 'check missing']

# stage 6 order: flows by number of examples, smallest first
FLOW_ORDER = ['waste', 'carnet', 'mast', 'ore', 'energy', 'packaging', 'air', 'plastics', 'wood', 'rail', 'utilities',
              'contest', 'road', 'furniture', 'cotton', 'retail', 'sea', 'tender']

# key: (stage, kind, title, decision, source, wrong, after, fix, deps)
# decision: 'none' | 'taken: <ref>' | 'D<n>' (filled from DECISIONS below) ; notes may contain conflicts.
C = {}


def c(key, stage, kind, title, decision, source, wrong, after, fix, deps='none', note=''):
    C[key] = dict(stage=stage, kind=kind, title=title, decision=decision, source=source, wrong=wrong, after=after,
                  fix=fix, deps=deps, note=note)


# ------------------------------------------------------------------ stage 1: no decision, no story change
c('REGION', 1, 'master data', "Urvanian province written into `Region`",
  'taken: merge decisions, row "Province … in `Region`"',
  '`world/parties.json` `identity.address.Region` of the 14 Urvanian parties (e.g. line 37) and `world/countries.json` `region` (line 96); `tools/build_examples.py` `address()` (field order at line 472)',
  'The province ("Province of Ferrano") of every Urvanian address is in `Region`, which UBL defines as a region "of a country" in the sense of an informal area; a province is a country subdivision (`CountrySubentity`). The value is master data and is copied into every full party description. The same element holds the cotton farm\'s "North coast" origin area in cotton/02 and 07.',
  'No address of an Urvanian party carries the province in `Region`; it is in `CountrySubentity` (with a code if the world has one).',
  'Move the field in parties.json (and the Urvanian address format in countries.json) from `Region` to `CountrySubentity`; the cotton origin area goes to the element the farm address already uses (`District`). A build check that `Region` is not used for a country subdivision would guard it.')
c('GATE', 1, 'master data', "Lumeway's \"Gate 3\" in its postal address",
  'taken: merge decisions, row "`AdditionalStreetName` = "Gate 3""',
  '`world/parties.json` Lumeway Distribution (6-xb) `identity.address.AdditionalStreetName` = "Gate 3" (line 898)',
  'Lumeway\'s postal address carries a vehicle gate as additional street name, so every full description of Lumeway (76 files, 5 flows) gives a gate where the post should go. A gate belongs in a delivery or pick-up location.',
  'Lumeway\'s postal address has no gate; where a document needs the gate, it is in a delivery location (with the GLN the flow already uses for the siding or goods-in).',
  'Drop the line from parties.json; add the gate to the delivery locations that need it (road/01 names gates and docks inconsistently, ROADISOL).')
c('PUBBODY', 1, 'encoding', 'Public bodies described as companies in a commercial register',
  'taken: merge decisions, row "Public bodies … as companies"',
  '`tools/build_examples.py` `legal_entity()`: `CompanyLiquidationStatusCode` "ACTIVE" for every non-person (line 297) and `CorporateRegistrationTypeCode` "COMMERCIAL" for every register (line 315); `world/parties.json` `kind: "public"`',
  'Customs services, the public works department, the chambers, the review board, the Trade Accord Council and the maritime administration get a commercial-register entry with a liquidation status, because `legal_entity()` writes both for every party that is not a person. The world list has no register type for public bodies.',
  'No public body carries `CorporateRegistrationTypeCode` COMMERCIAL or `CompanyLiquidationStatusCode`; companies keep them.',
  'In `legal_entity()`, skip the commercial-register scheme and the liquidation status for parties of kind "public" (and give them their legal basis instead, if a document needs one). Small related slips: the Port of Selanu as a separately registered head office (air/09#F3), the farm\'s yearly registration (see FARM).')
c('EXEMPTWORD', 1, 'master data', "The department's party tax exemption reason is worded as a transaction",
  'taken: merge decisions, row "Party tax exemption reason worded as a transaction" (in the parties review\'s Known table)',
  '`world/parties.json` Lumeport Public Works Department `tax_exemption_kind` = "Sale to a public body" (line 1163); the text comes from `world/countries.json` (line 249) via `tools/examples_kit.py` `tax_category()` (line 105)',
  'The department\'s `PartyTaxScheme/ExemptionReason` says "Sale to a public body", which describes a transaction, not the party\'s status, in every document that describes the department (55 in contest, furniture, tender and utilities, as the parties review counts).',
  'The party-level exemption reason describes why the party is exempt ("Public body exempt from sales tax"), and the transaction wording stays in the tax categories of lines.',
  'Give the exemption list a party-status wording, or a separate party text in parties.json.')
c('CONTACT', 1, 'master data', 'One contact template per kind of party, whatever the role',
  'taken: merge decisions, row "Contacts whose name, job title and department contradict …"',
  '`world/parties.json` `identity.contacts` (name, `job_title`, `department`, `hours`), written by `tools/build_examples.py` `party()` (lines 199–202) into every role',
  'Every company desk is a "Customer service officer" in "Sales", carriers\' desks "Operations planner", public bodies "Public service officer"; the same desk appears whether the party sells, buys, pays or receives goods (contacts of Valdara\'s "Order desk" on ore, gas and slat purchases). Name, job title and department often contradict each other.',
  'Each contact fits the party\'s role in the document (buying, accounts, goods-in, customs), and name, job title and department agree.',
  'Give parties.json contacts per function (sales, purchasing, accounts, goods-in, customs) and let the role pick the contact (in `place_parties()` / `party()`), or drop the contact where the document does not need one.',
  note='Contact hours that exclude the time of an event are under WEEKEND.')
c('MASTERCOPY', 1, 'encoding', "Party master data copied into documents that do nothing with it",
  'taken: merge decisions, rows "Party master data copied …" and "`CorporateStockAmount` holds share capital"',
  '`tools/build_examples.py` `place_parties()` (line 1117) writes `party(pid)` in full for every role of `world/documents.json`; `party()` (line 91) and `legal_entity()` (line 276) always add customs-trader IDs, tax schemes, share capital, listing, logo, website, service provider, permits and accounts',
  'A party is described with all its master data wherever it appears: customs-trader numbers in domestic orders and tender documents, share capital and stock listing in despatch advices, tax registrations in documents without tax, Rinova\'s waste permit in every plastics document, bank accounts in orders that move no money. The per-example reviews rate it Low, one finding per example.',
  'Each document carries of a party only what that document uses (identification, name and the data its definition or the transaction needs); the issuer\'s own share capital on its own invoice stays.',
  'Give each role a profile (short, trade, legal, tax, customs, payment) and let `place_parties()` choose it per document type; build check: no customs-trader ID outside customs and cross-border documents, no share capital outside the issuer\'s own invoice.',
  note='The findings marked "Needs decision: yes" (mostly contest and tender: the authority\'s tax scheme in procurement documents) follow the same rule and are confirmed in bulk (D47).')
c('EMISSION', 1, 'master data', 'Bench emission: 96 kg with factor 0.82 per 1 EA',
  'taken: merge decisions, row "Bench emission triple"',
  '`world/items.json` bench `emission` (factor "0.82", line 219, base 1 EA); written by `tools/build_examples.py` `item()` (line 1089)',
  'Every full description of the bench (40 files, 6 flows) states 96 kg CO2e with `ValueFactorNumeric` 0.82 and `ValueBaseMeasure` 1 EA, and 0.82 × 1 is not 96. The figure is a product footprint from the manufacturer\'s LCA, not a calculation from an activity.',
  'Either no factor and base, or a factor and base whose product is the stated value.',
  'Drop factor and base from items.json (preferred in all 40 findings); a build check that value = factor × base where both are given. tender/35#F2 (interest factor) is in this cause because it is the same element misuse on a reminder line.')
c('NOSTATUS', 1, 'encoding', '"NoStatus" as document or line status',
  'taken: merge decisions, row "`NoStatus` as status code"',
  '`tools/examples_kit.py` `despatch_advice()` (lines 407, 421), `receipt_advice()` (line 436), `tep_request()` (line 680), and scenario documents that copy them',
  'Document and line status codes say "NoStatus" in despatch advices, requests and receipts of ten flows: a filler that states nothing (UBL IND5/IND6).',
  'No `DocumentStatusCode` or `LineStatusCode` with a value that only says there is no status.',
  'Remove the elements from the kit builders; a build check rejecting the code "NoStatus".')
c('REFTYPE', 1, 'encoding', 'References that give only an ID',
  'taken: merge decisions, row "References with only an ID and no document type"',
  '`tools/examples_scenarios.py` `ref()` (line 2303) and `full_reference()` (line 4838); inline `DocumentReference` blocks in the kit (e.g. `examples_kit.py` line 443) and scenarios',
  'Additional and line document references carry only an `ID`, so the receiver cannot tell what kind of document is meant (waybills, orders, data sheets, minutes, contracts), in 13 flows.',
  'Every reference to a document that is not typed by its element names its kind (`DocumentTypeCode` or `DocumentType`), and, where it is an example of the flow, resolves to it.',
  'Let the reference helper always add the type; build check: every `AdditionalDocumentReference`/`DocumentReference` has a type.')
c('FXRATE', 1, 'encoding', 'Currencies and exchange rates with nothing to convert, or the wrong currency',
  'taken: merge decisions, row "Exchange rates with nothing to convert …"',
  '`tools/examples_kit.py` `price_block()` (line 329, `PricingExchangeRate`), `rate()` (line 817), `currency_line()` (line 278); `tools/examples_scenarios.py` `PRICING_RATE` (lines 2418, 2453) and the forward contract in the tender call-off',
  'Pricing, payment, tax and alternative currencies are written where nothing is converted (identity rates, rates in waybills and forwarding instructions), or name a currency the amounts are not in: the pricing currency is lume while every price is in coral (cotton/04, 05) or ferra while the price is in lume (tender/26, 32, 33).',
  'Every currency code and exchange rate converts an amount the document states in that currency; no rate from a currency to itself.',
  'Drop the elements where nothing is converted (preferred in every finding); build check: a `PricingCurrencyCode` equals the currency of the prices, a rate\'s source ≠ target.',
  note='Possibly not a problem for cotton/04#F1 and 05#F1: `note/src/03-world.md` says "seed cotton is priced from the trade accord\'s lint reference price, published in lume", so a lume pricing currency may be intended; then the conversion must be shown, not dropped.')
c('SHIPORDER', 1, 'encoding', '`ShippingOrderID` holding the consignment or shipment ID',
  'taken: merge decisions, row "`ShippingOrderID` holding the consignment or shipment ID"',
  '`tools/examples_kit.py` `waybill()` (line 759: `flow.numbers.get("consignment", number)`); `tools/examples_scenarios.py` lines 1639, 4249, 4279',
  '`ShippingOrderID` is "the shipping order or forwarding instructions" number, but the kit fills it with the consignment ID, so the same shipment has two or three different "shipping orders" across a flow (air, sea).',
  'Every `ShippingOrderID` is the number of the forwarding instructions or booking that exists in the flow, the same in all documents of the shipment, or the element is absent.',
  'Use the forwarding instructions\' number where the flow has one, else drop the element; build check: a ShippingOrderID resolves to a ForwardingInstructions of the flow.')
c('GROSSWT', 1, 'encoding', 'Shipment gross weight without the transport equipment',
  'taken: merge decisions, row "Shipment `GrossWeightMeasure` without the transport equipment"',
  '`tools/examples_kit.py` `gross_weight()` (line 469), used by `despatch_advice()` (line 415) and `waybill()` (line 789)',
  '`Shipment/GrossWeightMeasure` includes the transport equipment by its definition, but the kit writes the goods\' gross weight, also where the same document gives the container\'s tare (sea/10: the shipment weighs less than its own container).',
  'The shipment gross weight includes the equipment where the document knows it (container, wagons), or is absent; the goods\' gross weight is on the goods item or consignment.',
  'Compute goods + tare where equipment is known, else move the value to the goods item; build check: shipment gross ≥ sum of equipment tare + goods.')
c('ORIGINALS', 1, 'encoding', '"Three originals" against the distribution list',
  'taken: merge decisions, row "Waybill note "three originals" against the distribution list"',
  '`tools/examples_kit.py` `waybill()` note (line 762) and `DocumentDistribution` (lines 772–779); `tools/examples_scenarios.py` line 1640, `bl_distribution()` (line 4418)',
  'The waybill says "Three originals: consignor, consignee, carrier." while its distribution lists one original and an electronic copy (eight flows).',
  'The note and the distribution list agree on the number of originals and who gets them.',
  'Generate the note from the distribution (or the distribution from the convention); build check comparing the two.')
c('TAXTOTALS', 1, 'encoding', 'Tax totals and taxable amounts that ignore the document\'s own charges, or state an empty zero',
  'taken: merge decisions, row "Taxable amount that ignores the document\'s own allowance or charge"',
  '`tools/examples_kit.py` `tax_total()` (line 243) and `monetary_total()` (line 259); `tools/examples_scenarios.py` `with_allowance()` (line 921)',
  'The taxable amount leaves out the document-level allowance or charge of the same category (furniture/10, retail/08, cotton/04, 05, wood/03; air/01 the whole order instead of the change), and several documents carry a zero tax total without a category, scheme or reason (energy/08, sea/25, tender/15, tender/35, wood/02, cotton/04).',
  'Taxable amount = line extension ± document-level allowances and charges of that category; a tax total only where a tax is stated, with category and reason when it is zero.',
  'Feed allowances and charges into `tax_total()`; drop empty tax totals. Build check: the tax arithmetic per subtotal.')
c('PRIVACY', 1, 'encoding', 'A line marked both confidential and internal', 'none',
  '`tools/examples_scenarios.py` lines 5227 and 5285 (`SecurityClassificationCode` INTERNAL next to a `PrivacyCode`)',
  'Lines carry `PrivacyCode` "Confidential" and `SecurityClassificationCode` "Internal" at once, two different levels (furniture/01, wood/01).',
  'At most one classification per line, consistent with the other.',
  'Drop one of the two in the scenario code.')
c('PENALTYMONTH', 1, 'encoding', 'Bayvarra\'s surcharge "per month" encoded as one month only', 'none',
  '`tools/examples_kit.py` `payment_terms()`: `PenaltyPeriod/DurationMeasure` 1 MON and `PenaltyAmount` for one month (lines 167–171)',
  'All 18 XB-STD terms state "1.5 % surcharge per month late" with a penalty period of one month; four reviews flagged it (conditions#F9 gives the extent).',
  'All 18 places encode the surcharge the same way, and the encoding says "per month" (no end of the period, or a note that the amount is per month).',
  'Drop the duration (preferred by conditions#F9) in `payment_terms()`; one change fixes all 18.')
c('ROLEDUP', 1, 'encoding', 'Party roles that repeat another role or do not fit their definition',
  'none',
  '`world/documents.json` `parties` maps (e.g. CustomerParty next to ReceiverParty, notifier = importer), placed by `tools/build_examples.py` `place_parties()` (line 1117); originator/beneficiary blocks in `tools/examples_scenarios.py` (lines 5275, 5293, 6487)',
  'Roles are filled with the party that already holds another role in the same document: `CustomerParty` equal to the receiver in utility statements (whose definition is "the buyer, if different from the receiver"), the importer as its own notifier, the contracting party in eight further roles of the tender notices, originator and beneficiary on every line; and the rail carrier and the mast forwarder as `FreightForwarderParty`, which UBL defines as a consolidator.',
  'A role appears only where it adds a party or information the document needs; party roles fit their UBL definition.',
  'Remove the redundant roles from documents.json; build check: no role whose definition says "if different" equals the role it is compared with.',
  note='The findings marked "yes" (forwarder role, consignor notified of its own goods) are confirmed in bulk (D47).')
c('LOCNAME', 1, 'encoding', 'Locations named after companies or their office addresses',
  'none',
  '`tools/examples_kit.py` `leg_places()` (line 624) and `address_of()` (line 631) build transport locations from the parties\' postal addresses; issue and status locations in `event()` (line 1273) and the scenarios',
  'From/to locations, issue, status and notification locations are a company\'s name and business address instead of the place (quay, siding, airport, warehouse), so the barge "starts" at the carrier\'s office and the ore train runs between head offices.',
  'Transport and event locations name the place where the thing happens, with its identifier (UN/LOCODE, GLN) where the world has one.',
  'Derive locations from map.json places (or the parties\' sites/GLNs) instead of postal addresses.')
c('PLACES', 1, 'encoding', 'Places and offices given only by name or text, without the identifier they have elsewhere',
  'none',
  '`tools/examples_kit.py` `place()` (line 1177) and `order()` delivery terms (line 300); `tools/examples_scenarios.py` `exit_office()` (line 4557)',
  'Delivery places of Incoterms, airports, customs offices and ports of registry are given by name only, although the flow identifies them elsewhere by UN/LOCODE or GLN.',
  'A place that the world identifies carries its identifier wherever it is given.',
  'Use `place()` with the identifier for delivery terms, offices and ports.')
c('EVENTS', 1, 'encoding', 'Transport events without type or place, or as generic events where a dedicated one exists',
  'none',
  '`tools/examples_kit.py` `event()` (line 1273) and its callers in the scenarios',
  'Events are given with a date and time but no type and no location, or as "additional" free-text events where the stage has a dedicated event (loading, acceptance, arrival), in six flows.',
  'Every event says what happened (dedicated element or type code) and where.',
  'Make `location` and `type_code` required in `event()` and use the dedicated stage events.')
c('TRANSPORTCONTENT', 1, 'encoding', 'Transport requests, instructions, waybills and manifests that do not say what, from where, to where or when',
  'none',
  '`tools/examples_kit.py` `tep_request()` (line 673), `tep()` (line 700), `waybill()` (line 747); forwarding instructions in `tools/examples_scenarios.py` (`sea_consignment_fi()` line 1522, `air_consignment()` line 1892)',
  'The generic transport builders give a weight and a note but no goods item, packages, places of taking over and delivery, or dates: forwarding instructions that do not say what to carry, a shipped-on-board bill without goods or vessel, a cargo manifest that does not list the cargo.',
  'Every transport request, plan, instruction, waybill and manifest states the cargo (goods items, packages), the places and the requested or actual dates its definition calls for.',
  'Give the builders the consignment data the flow already holds (handling units, legs, events).')
c('DESPDATES', 1, 'encoding', 'Despatch advices that do not say when the goods leave or arrive', 'none',
  '`tools/examples_kit.py` `despatch_advice()` (line 401)',
  'The kit\'s despatch advice has no despatch date or time, no estimated delivery and no transport reference, in nine flows.',
  'Every despatch advice states the despatch (actual or planned) and the expected delivery, and how the goods are identified.',
  'Add `Shipment/Delivery/Despatch` dates and the estimated delivery period in `despatch_advice()`.')
c('ORDERDATES', 1, 'encoding', 'Orders without a requested delivery date', 'none',
  '`tools/examples_kit.py` `order()` (line 285)',
  'Orders and order changes state no requested delivery or collection date, also where urgency is the reason (air/01).',
  'Every order states when the goods are wanted (or, for ex-works, when they are collected).',
  'Add `Delivery/RequestedDeliveryPeriod` in `order()` from the flow\'s dates.')
c('INVLINK', 1, 'encoding', 'Invoices not linked to the delivery they bill', 'none',
  '`tools/examples_kit.py` `invoice()` (line 473)',
  'Invoices give no delivery date or place and no despatch or receipt reference, also where an export exemption rests on the delivery (packaging/02, rail/11, wood/08).',
  'Every invoice for goods identifies the delivery (despatch advice reference or delivery date and place); an export exemption names its evidence.',
  'Add `DespatchDocumentReference` and `Delivery` in `invoice()`.')
c('REMIT', 1, 'encoding', 'Remittance advices: the invoice twice on a line, two payment-order references, header parties repeated', 'none',
  '`tools/examples_kit.py` `remittance()` (line 546)',
  'The remittance builder references the paid invoice twice on the same line, gives two different values for the payer\'s payment order, repeats the header\'s accounting parties on the line and sets a generic payment purpose, in eight flows.',
  'One reference per paid document per line, one payment-order reference, line-level parties only where they differ.',
  'Fix `remittance()` once.')
c('COSTCENTRE', 1, 'master data', "The buyer's cost centre does not fit what is bought", 'none',
  '`tools/examples_kit.py` `cost_centre()` (line 215) with `world/parties.json` `cost_centre` (one per party, e.g. line 149)',
  'Each party has one cost centre, used for whatever it buys: Valdara books electricity, waste services and freight as "Raw materials and parts", the store books shirts to its garden department, outbound freight is "Stock purchases".',
  'The accounting cost of a line fits what the line buys, from the buyer\'s own chart.',
  'Give parties.json a small chart of cost centres per kind of purchase and let `cost_centre()` choose by item kind.')
c('SUPPLYTYPE', 1, 'encoding', 'Electricity, gas, water and levies classified as services', 'none',
  '`tools/examples_kit.py` `tax_category()` (lines 115–128: GOODS only for items of kind "goods")',
  '`SupplyTypeCode` is "SERVICES" for electricity, gas and drinking water (utilities, energy) and for a levy that is no supply, while gas is goods elsewhere in the same flow.',
  'Energy and water are goods (or the code is absent); a levy collected for a third party carries no supply type.',
  'Classify the utility items as goods in items.json and skip the code for levies.')
c('CATALOGUE', 1, 'encoding', 'Catalogue encoding: territory of the seller, "Active" status, CatalogueIndicator, discounts and dependent prices', 'none',
  '`tools/examples_kit.py` `catalogue_terms()` (line 1001; territory = seller\'s country at line 1015); `tools/build_examples.py` `item()` `CatalogueIndicator` (line 871)',
  'Every catalogue puts the seller\'s country into the price\'s territory, so an export price carries "Export outside Bayvarra" for the territory Bayvarra (conditions#F1: one price list, two tax treatments); the price list status is "Active" where the element names original/copy/revision; `CatalogueIndicator` is set in the catalogue itself; the "full container" discount and the dependent side-frame price do not follow from their conditions.',
  'Territory = the market the price is offered for, with that market\'s tax; one price list ID, one territory, one treatment; status codes from the element\'s meaning; no indicator in the catalogue itself.',
  'Fix `catalogue_terms()` (option a of conditions#F1: territory = buyer\'s market).')
c('REFKIND', 1, 'encoding', 'Documents referenced as a kind they are not', 'none',
  'source not located in one place: the reference elements chosen in the scenario code (cotton `self_billed()` in `tools/examples_kit.py` line 1115, furniture in `tools/examples_scenarios.py` lines 3268–3396, sea debit note `sea_with_debit()` line 5904)',
  'A delivery note is referenced as a despatch advice, a weighbridge ticket as a receipt advice, a quotation as a contract, a work report and a budget commitment as billing documents, a bill of lading as a delivery note.',
  'Each reference uses the element for the kind of document referenced, or a typed `AdditionalDocumentReference`.',
  'Correct the reference elements per flow.')
c('PAYNOTE', 1, 'encoding', 'Payment notes that call every document an invoice', 'none',
  '`tools/build_examples.py` `account()` (line 611: `PaymentNote`)',
  'The payment note of credit notes, debit notes and the deposit asks the payer to quote "invoice …".',
  'The payment note names the document type it is on.',
  'Pass the document type into `account()`.')
c('WAYBILLTYPE', 1, 'encoding', 'Transport document type fixed per mode, not per convention and scope', 'none',
  '`tools/examples_kit.py` `WAYBILL_KIND` (line 741: one kind per mode) used by `waybill()`; damage notes "on the consignment note" in despatch advices',
  'A domestic road carriage gets a CMR, a domestic rail carriage a CIM note, the rail flow\'s waybill is a CMR, and despatch advices in air and sea shipments ask for damage to be noted "on the consignment note".',
  'The waybill type follows the convention that applies to the leg (international or domestic, mode), and texts name the document the flow uses.',
  'Choose the kind by mode and border crossing (codelist-decisions: WaybillTypeCode by legal regime); fix the despatch-advice note.')
c('HANDLINGUNIT', 1, 'encoding', 'Pallets listed as packages contained in themselves', 'none',
  '`tools/examples_kit.py` `handling_units()` (line 1366) and `pallets()` (line 1294)',
  'Each pallet lists itself as the one package it contains, and the package quantity is used as a number of packages (road/08, retail/12).',
  'A handling unit contains the packages actually on it; quantities count what they say.',
  'Fix `handling_units()`.')
c('LINEID', 1, 'encoding', 'Line IDs reused for another line', 'none',
  '`tools/examples_kit.py` despatch and receipt lines (lines 423, 450–451: line i refers to order line i); the air order change in `tools/examples_scenarios.py` `air()` (line 1940)',
  'The air order change adds frames under line ID 1, the bench line of the order it changes; responses and despatch advices follow; a substitute line and a handling-unit receipt line reuse ID 1 (retail).',
  'A new line has a new ID, carried through the follow-up documents; references point to the line they mean.',
  'Give the added line ID 3 (air) and fix the index-based references in the kit.')
c('TEMPCODE', 1, 'encoding', 'Temperature code given next to a measured value', 'none',
  '`tools/examples_scenarios.py` lines 5392 and 5879 (`MeasureCode` with a value)',
  'A temperature carries both a measured value and a code that only qualifies it (mast/02, plastics/09).',
  'A temperature is either a value with its attribute or a code, as the element defines.',
  'Drop `MeasureCode` where the value is given.')
c('JOURNEY', 1, 'encoding', '`JourneyID` holding a voyage or month instead of the service schedule', 'none',
  '`tools/examples_kit.py` `means()` (line 1206); `tools/examples_scenarios.py` line 8698 (pipeline "KG-P1-2603")',
  '`JourneyID` (the regular service schedule) holds the barge\'s voyage number and the pipeline\'s month.',
  'JourneyID only where a scheduled service exists; a voyage number in the element for it.',
  'Correct the two values.')
c('TEPTERMS', 1, 'encoding', 'Framework transport-plan clauses and periods mis-encoded', 'none',
  '`tools/examples_kit.py` `tep_terms()` (lines 646–661) and `tep_request()`/`tep()` periods (lines 673–738)',
  'The shared framework clauses put a late-delivery penalty into `PenaltySurchargePercent` (a late-payment element), a post-event duration into a pre-arrival notice, a stationary-service location without a stationary service, a commission to an absent broker, and "Waiting time 40 per hour" without a currency; the service period starts after the pickup it contains (rail/02, 03) or the pre-arrival period lies before the transport (ore/03); the wood transport window ends before the promised delivery window.',
  'The clauses use elements whose definitions fit; every amount has a currency; the service period contains the pickup and delivery.',
  'Fix `tep_terms()` once (it is shared by ore, rail and plastics) and derive the periods from the legs.',
  note='The waiting-time currency is "Cannot be told" 8 in the conditions file; the fixing session picks XUF or XBL with a plausible rate.')
c('TEPSERVICE', 1, 'encoding', 'One transport service code per mode', 'none',
  '`tools/examples_kit.py` `MODE_SERVICE_CODE` (line 619: road FTL, rail RAILCONT …)',
  'The service code depends only on the mode, so the ore in bulk wagons gets a container-train service, the rail flow\'s road pickup becomes "Full truck load" as main service of a container train, and the plastics barge carries "bulk" for bagged cargo.',
  'The main service fits the cargo and the means (wagon load for ore, container train with a pre-carriage stage for the road leg, bagged cargo for jumbo bags).',
  'Choose the service from the leg and the cargo type, not the mode alone.')
c('CUSTOMSDECL', 1, 'encoding', 'Customs declaration builders: goods items, offices, previous declaration and issuer', 'none',
  '`tools/examples_kit.py` `goods_items()` (line 844), `export_declaration()` (line 864), `import_declaration()` (line 881); `tools/examples_scenarios.py` `export_extras()` (line 4567), `import_extras()` (line 4590), `exit_office()` (line 4557), `rail_offices()` (line 590)',
  'Declarations give the goods quantity as a weight without packages, no transport at the border, no link to the invoice the value rests on, and validity periods; the exit office of the exporting country appears in imports; `PreviousCustomsDeclaration` holds another country\'s declaration; the waybill names customs as issuer of the exporter\'s declaration.',
  'Each declaration declares packages, transport at the border and the invoice; offices are the declaring country\'s; a previous declaration is a declaration of the same procedure chain in that country; the issuer of a declaration is its declarant.',
  'Fix the shared customs builders; build check: the office in a declaration belongs to the declaring country.',
  note='The previous-declaration finding of sea/11 is also part of the goods chain (STOCKCHAIN, D3).')
c('ADVALOREM', 1, 'encoding', 'Ad valorem indicator and declared carriage value without a valuation', 'none',
  '`tools/examples_kit.py` `waybill()` (line 765); `tools/examples_scenarios.py` lines 1638, 1654',
  '`AdValoremIndicator` and declared carriage values appear where no ad valorem charge or duty exists, and with opposite values for the same air shipment.',
  'The indicator and the value appear only together with the charge they concern, the same in every document of a shipment.',
  'Drop them (preferred in air/03, 04).')
c('ORDERREFS', 1, 'encoding', 'Order references in the wrong element', 'none',
  'source not located in one place: the air order change (`tools/examples_scenarios.py` `air()`, line 1940) and the tender call-off enrichments (after line 7151)',
  '`SalesOrderID` holds the seller\'s number of the original order in a buyer\'s change, a release number sits in `ReleaseID` (delivery-access release), a project name in `CustomerReference`.',
  'Each order reference element holds what its definition says.',
  'Correct the values.')
c('DERIVEDID', 1, 'generator mechanism', 'Identifiers built from flow names, file numbers and other identifiers',
  'none',
  '`tools/examples_kit.py` `tep()` signature `…-SIG-{flow.base}` (line 715), `waybill()` signature (line 784), `unit_id()` (line 1346: SSCC serial from the castings\' serial); flow-name signature IDs in `tools/examples_scenarios.py` (search "SIG-EX")',
  'Signature IDs contain the flow name or the example\'s file number, pallet SSCCs start with the serial of the first casting, the same remittance ID `VI-RM-26-0316` is used by three payers (see NUMBERING), a journey/week number is one off.',
  'No identifier contains a flow name or file number; identifiers of different things are not derived from each other unless the world\'s rule says so.',
  'Per scheme an independent running number in the issuer\'s series (identifiers#F4 option a).')
c('ITEMPROP', 1, 'master data', 'Item properties of the slat: validity periods, repeated length, full specification', 'none',
  '`world/items.json` hardwood slat properties; `tools/build_examples.py` `item_property()` (line 638)',
  'The slat\'s property "Planed on four sides" has a 12-month validity, its length is repeated in `SellersItemIdentification/MeasurementDimension`, and the full commercial specification (test methods) stands in customs declarations and invoices (wood, 7 files).',
  'Properties carry validity only where they expire; dimensions once, in the item; customs declarations carry what customs needs.',
  'Clean the slat\'s data in items.json.',
  note='The copying part depends on D10x (what item data travels).')
c('TARIFF', 1, 'encoding', "Urvania's national tariff subheading in other countries' documents",
  'taken: `analysis/codelist-decisions.md` Q24 ("tariffs, rates and exemptions stay national") and `note/src/03-world.md` ("in Urvania, the national tariff code")',
  '`world/items.json` `national_tariff` of bench and frame (e.g. line 253), written by `tools/examples_kit.py` `customs_item()` (line 828) into every customs declaration and item',
  'The 8-digit Urvanian subheading travels with the bench and the frame into Bayvarran and Lisavan declarations (road/10, tender/31, sea/11, sea/19, rail/06) and into Bayvarran commercial documents.',
  'A national subheading appears only in documents of the country whose tariff it is.',
  'Write `national_tariff` only when the declaring country (or the seller, for commercial documents) is Urvania (conditions#F10 option a).',
  note='The findings marked "yes" are settled by Q24; confirmed in bulk (D47).')
c('REPLACEITEM', 1, 'encoding', '`VI-C180-2026` replaces a frame in one catalogue and a bench in a tender', 'none',
  'source not located: the replacement item in the retail catalogue and the tender line (`tools/examples_scenarios.py`)',
  'The same unresolvable identifier replaces the side frame in retail/02 and the whole bench in tender/15.',
  'A replacement identifier means one item, identified somewhere, of the same kind as the item it replaces.',
  'Drop it from the tender line; identify the 2026 casting by `VI-C180` + extended ID (items#F4 option a).')

# ------------------------------------------------------------------ stage 2: world rules (owner decisions)
c('MAPSCALE', 2, 'world rule', 'The map scale: all coordinates inside 35 km, against distances and times of hours and days', 'D1',
  '`world/countries.json` `geography.degrees_per_tile` = 0.01 (line 619) and `origin`; `tools/build_examples.py` `coordinate()` (line 510); `world/map.json` tiles',
  'Coordinates are computed from map tiles at 0.01° per tile, so Lumeport and Selanu are 6 km (3.2 nm) apart and the whole world fits in 21 × 32 km, while the documents state two days at sea, a three-hour flight, 186 km by road and a ballast exchange 120 nm off Selanu.',
  'Coordinates, stated distances (km, nm) and durations agree within plausible speeds per mode.',
  'Decide the scale (D1); preferred by timelines#F1: scale the coordinates (one constant), because distances and durations are spread over many documents.',
  deps='blocks SEAVOYAGE; the map rendering on the site uses the same tiles')
c('SEAVOYAGE', 2, 'world rule', 'One sea voyage with four passage times', 'D1',
  '`tools/examples_scenarios.py` sea flow (`sea()` line 1527; manifest, status and pre-arrival report dates and times)',
  'Voyage `TH-26-19E` takes two days (service), 64 h (manifest estimate, issued after the actual departure), 84 h (actual) and is 40 nm off Selanu at 13.5 kn on 16 May although it arrives on 18 May.',
  'Service duration, estimate, reporting position and actual times describe one passage, or a stated event explains the difference.',
  'Settle with D1, then derive estimate, position and arrival.', deps='after MAPSCALE (D1)')
c('WEEKEND', 2, 'world rule', 'Documents dated at the weekend against a Monday-to-Friday week', 'D4',
  'the flows\' start dates and day offsets in `tools/examples_scenarios.py` (`kit.Flow(…)` lines 25–8894 and the day argument of each document); contact hours in `world/parties.json` (`hours`, e.g. line 28)',
  'By the count of conditions#F7, 48 documents (19 %) are issued on a Saturday or Sunday by offices whose contacts say "Weekdays 08:00–17:00"; contact hours also exclude the times goods are at the border or a ship arrives.',
  'Documents of people or offices with weekday hours fall on weekdays, or the world states that systems issue at any time.',
  'Decide D4; then a build check on the weekday of issue dates per issuer kind.')
c('DUEDATE', 2, 'world rule', 'Standard terms IDs that do not mean the same number of days everywhere', 'D5',
  '`tools/examples_kit.py` `payment_terms()` (line 150: due date = issue day + `due_days` passed by each caller); `world/countries.json` `payment` per country; the 21-day utilities calls in `tools/examples_scenarios.py` `utilities()` (line 2998)',
  'XU-STD/XB-STD say 30 days and XL-STD 45 days, but the utilities are due in 21 days under all three IDs, and the Bayvarra–Lisavu invoices use the buyer\'s period under the seller\'s text.',
  'One terms ID, one text, one period; every due date follows from the terms the document cites.',
  'Decide D5 (preferred by conditions#F2: own terms ID for utilities, correct the three cross-border dates); derive `due_days` from the terms, not from the caller; build check due date − issue date = terms period.')
c('CONTRACTTERMS', 2, 'world rule', 'Contract payment terms never applied by the invoices under the contract', 'D6',
  '`tools/examples_kit.py` `payment_terms()` (line 150) always applies the seller\'s country terms; the contracts\' own terms in `tep_terms()` (line 646) and the tender `tendering_terms()` (`tools/examples_scenarios.py` line 6283)',
  'The framework transport plans (ore, rail, plastics) say "30 days net from the consignment note" and the tender contract "30 days after each accepted release", but every invoice under them applies XU-STD (30 days from the invoice, 2 % discount, 8 % interest); the reminder and remittance follow.',
  'An invoice under a contract applies the contract\'s terms; standard terms only where no contract terms exist.',
  'Decide D6. conditions#F3 prefers (a) invoices follow the contract.',
  note='Conflict with the world story: `note/src/03-world.md` says "Each country also has its own payment practice, which every invoice of a seller there follows." The generator does exactly that; the reviews (and conditions#F3, "Needs decision: no") want the contract to win.')
c('CUSTOMSVALUE', 2, 'world rule', 'Customs value on a different basis in each flow', 'D7',
  '`tools/examples_kit.py` `goods_items()` (line 844, value = the goods lines of the invoice); `tools/examples_scenarios.py` `cif_value()` (line 1154) and `goods_items()` (line 87)',
  'Bayvarra alone values imports on four bases (freight to destination added in plastics, FCA/FOB without freight in road and cotton, a delivered price in tender); document-level charges (colour, pallets) are never in the value; the sea bill of lading declares a CIF value the import declaration does not use.',
  'Each country\'s customs values follow one stated basis, applied in every declaration; charges that are part of the price are treated the same way everywhere.',
  'Decide D7 (preferred by conditions#F5: CIF-type value at the importing border for all three countries).')
c('DUTIES', 2, 'world rule', 'Duties, import taxes and Trade Accord preference stated nowhere', 'D8',
  '`tools/examples_scenarios.py` `import_extras()` (note "Duties paid by the importer\'s account at customs.", line 4597); preference only in the plastics import (line 868)',
  'Every import says duties were paid without a duty, rate or amount; preference is claimed once (plastics), certified but not claimed in road, ignored elsewhere; the carnet reminder claims 1,300 coral of duties and consumption tax on goods worth 399.20 XLC.',
  'Import declarations state, per country, whether duty and import tax are due on Accord-origin goods (amount, or a preference claim with criterion and proof).',
  'Decide D8.',
  note='`note/src/03-world.md` already says: "Lisavu (XL) has no general sales tax. Customs collects a customs duty and an import consumption tax when goods enter the island." and codelist-decisions Q24 "tariffs, rates and exemptions stay national". So the Lisavan import tax of carnet/03 agrees with the story; conditions#F6 lists it as an open question.')
c('TAXO', 2, 'world rule', "Tax category O for goods, 0 % on O, and Lisavu's tax scheme without ID", 'D11',
  '`tools/examples_kit.py` `tax_rule()` (line 72) and `tax_category()` (lines 115–135; scheme name "No general sales tax" without ID, line 133)',
  'Lisavan sales of goods use category O "Services outside scope of tax"; O is given with a 0 % rate and, for levies, with an exemption reason; the Lisavan scheme has a name and no ID.',
  'Goods outside any sales tax use a category that fits goods (or the world states that O covers them); no percent on O; a scheme with an identifier or none.',
  'Decide D11 (merge decisions: "Tax category O … used for goods", Medium, yes).')
c('TENDERTAX', 2, 'world rule', "Bayvarran withholding tax and tax representative only in the tender, and Urvania's \"service to a business abroad\" for a public body", 'D10',
  '`tools/examples_scenarios.py` `withholding()` (line 2333) and the tender invoices; `tools/examples_kit.py` `tax_rule()` (line 72)',
  'The tender notices state Bayvarran exemption PUBLIC; the winner\'s invoices apply Urvanian VAT (EXP, SVCABROAD) plus a Bayvarran 10 % withholding on the installation collected through a tax representative, which no other non-resident supplier into Bayvarra has; SVCABROAD ("to a business") is used for the public works department.',
  'One visible rule for Bayvarran taxes on non-residents\' supplies, applied the same way in tender and road; the notices describe the treatment the invoices use.',
  'Decide D10.',
  note='`note/src/03-world.md` states the rule: "A public body in Bayvarra withholds 10 % of the price of a service from a business not established there and pays it to the state; such a supplier names a tax representative in Bayvarra." That supports conditions#F4 option (a) and contradicts its preferred option (c) "drop the withholding"; road/14 (a company customer) is consistent with the story.')
c('LANGTAG', 2, 'world rule', "English renderings tagged with the issuer's country, Italian names tagged as English, legal form untagged", 'D5x',
  '`tools/build_examples.py` `language_tag()` (line 1215: the sender\'s country as region), `city_names()` (line 420), legal form in `legal_entity()` (lines 284–289)',
  'The same party\'s English address is `en-XB` in Bayvarran documents and `en-XU`/`en-XL` in its own (277 of 277 tagged rows follow the issuer); the Italian street names of Urvania are tagged English; the legal form is untagged in one rendering.',
  'One stated rule for the language tag of English renderings (and the legal form), applied everywhere.',
  'Decide D5x.',
  note='Conflict with an earlier decision: `analysis/codelist-decisions.md` 6b: "(a) Every sender tags its English texts with its own region: `languageID` `en-XU`, `en-XB` or `en-XL`." and `note/src/03-world.md`: "the inherited Italian names count as English". The documents follow both; the findings ask for a different rule.')
c('LOCALE', 2, 'world rule', '`Language/LocaleCode` = `en`', 'D4x',
  '`tools/build_examples.py` `party()` (lines 136–141: `LocaleCode` from `identity.language`); `tools/examples_scenarios.py` lines 3930, 4850, 6435, 6939',
  '213 files carry `LocaleCode` `en` with listID ISO 639: a language, not a locale (Medium in every review).',
  'LocaleCode holds a locale or is absent.',
  'Decide D4x; merge decisions prefer dropping it.',
  note='Conflict with an earlier decision: `analysis/codelist-decisions.md` 6b: "Coded elements (LocaleCode, Language/ID, DefaultLanguageCode) stay plain `en`, because ISO 639 has no region." The merge decisions (Medium, no) contradict it.')
c('SELANUNAME', 2, 'world rule', "Lisavu's capital: \"Port Wrenfield\" in English addresses, \"Selanu\" in every other English text", 'D6x',
  '`world/countries.json` `english_place_names` ("Selanu": "Port Wrenfield", lines 1711–1713); `tools/build_examples.py` `city_names()` (line 432); party and place names in `world/parties.json`',
  'The 12 Lisavan parties\' English addresses say Port Wrenfield; about 140 party names, place names and texts say Selanu.',
  'In English the town has one name, or the documents say once that Port Wrenfield is Selanu\'s English name.',
  'Decide D6x.',
  note='`note/src/03-world.md`: "Selanu is also *Port Wrenfield*"; "An address gives both, Lisavan first." The addresses follow the story; parties#F1 option (a) (Selanu in English addresses) would change the story.')
c('SIGNATURE', 2, 'world rule', 'Signature aggregates with only an ID and a signatory', 'D11x',
  '`tools/examples_kit.py` `tep()` (line 715) and `waybill()` (line 784); `tools/examples_scenarios.py` `full_signature()` (line 4822) and inline signatures (e.g. lines 1006, 1797, 1878)',
  '137 of 147 Signature aggregates carry only an ID and a signatory party, no method, time or attached signature.',
  'A Signature says what was signed, how and when, or is absent.',
  'Decide D11x (merge decisions: Low, yes).')
c('FULLNESS', 2, 'world rule', '`FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING for a cradle-to-gate footprint', 'D9',
  '`world/items.json` bench footprint `stage` "MANUFACTURING" and `fullness` "CRADLETOGATE" (lines 207–211); lists in `world/codelists/lists.json` (lines 6492, 6519)',
  'The bench\'s footprint carries a system boundary in an element about full transport equipment, and the stage A3 for a figure from the mine to the gate (74 findings in 40 files).',
  'Elements are used by their UBL definitions.',
  'Decide D9.',
  note='Conflict with an earlier decision: `analysis/codelist-decisions.md` Q21: "FullnessIndicationCode gets a consistent separate list (CRADLETOGATE …)". The merge decisions (Medium, no: drop) contradict it.')
c('ITEMCOPY', 2, 'world rule', 'Catalogue and product-passport data copied into business documents', 'D10x',
  '`tools/build_examples.py` `item()` (line 844) always writes the maker\'s full item data (brand, properties, certificates, footprint, circularity); customs-relevant item data in `customs_item()` (`tools/examples_kit.py` line 828)',
  'The full bench description (properties, emissions, warranty, dimensions, keywords) stands in orders, despatch advices, invoices, customs declarations and till receipts.',
  'Each document carries the item data its transaction uses.',
  'Decide D10x.',
  note='Conflict with the world story: `note/src/03-world.md`: "The maker\'s facts travel with the item wherever it appears: brand and model, properties with their test method and accepted range, certificates, the carbon footprint and the circularity profile." The merge decisions (Low, no) treat it as a fault.')

# ------------------------------------------------------------------ stage 3: master data
c('REGDATE', 3, 'master data', 'Default founding date 1996-01-01 and size classes that do not fit the parties', 'D7x',
  '`world/parties.json` `identity.legal.founded` = "1996-01-01" for 25 parties (e.g. line 209) with low `headcount`/`turnover`; the size follows from them in `tools/codelists.py` `entity_size()` (line 266)',
  '25 unrelated companies were registered on 1 January 1996 and are all SMALL, including both national ports, the state water company, the telecom operator and the rail operator; the sawmill states 85 employees but is SMALL; Valdara is LARGE with 180 persons; operating years contradict the registration (tender/04, 07, 13).',
  'Every party\'s founding date and size class are its own and consistent with the figures the documents state.',
  'Decide D7x (per party a date, headcount and turnover), then the size follows by the existing rule.')
c('GTIN', 3, 'master data', 'World item numbers that are valid GTIN-12s; Valdara\'s items under Lumeway\'s GS1 prefix', 'D8x',
  '`world/items.json` `standard_id` (e.g. "771020000027", line 44) and the GS1 items of the GS1-convention parties in `world/parties.json` `identification`',
  'The world item numbers have the form and check digit of GTIN-12s in a real US/Canada range; the distributor gives the manufacturer\'s branded bench and frame GTINs under its own prefix, so one item has two standard identities (items#F2).',
  'One standard identification per item that all sellers use, or a stated rule; fictional numbers not mistakable for real GTINs.',
  'Decide D8x.',
  note='Conflicts: `note/src/03-world.md`: "where the maker has no GTIN, the GS1 distributor gives the item one of its own, as GS1 allows a wholesaler or importer to do, and the maker\'s Codana number travels with it"; `analysis/codelist-decisions.md` ID-Q4: "item numbers with a non-company GS1 prefix (world scheme, check digit kept)". Both choices are deliberate.')
c('FURNBRAND', 3, 'master data', "The maker's brand on the store's own-line garden set", 'D12',
  '`world/items.json` garden bench set (BF-GS-01) brand, as written by `tools/build_examples.py` `item()`',
  'The store sells the set under its own line, but every document gives Brackenmere\'s brand (furniture, 12 files).',
  'The brand is the brand under which the item is sold, or the story says the store sells the maker\'s brand.',
  'Decide D12.')
c('ISIC', 3, 'master data', "Industry classes that leave out what the party does", 'D13',
  '`world/parties.json` `identity.industry` (Selanu Telecom 6110, line 2581; Ferrano Energy and Ferrano Grid 3510)',
  'The mast operator is classified as wired telecommunications; Ferrano Energy\'s and Ferrano Grid\'s class covers electricity only, in a gas statement.',
  'Each party\'s ISIC class fits what it does in the documents.',
  'Decide D13 (which class per party), then change parties.json.')
c('FARM', 3, 'master data', "Lisavu Cotton Farm: address lines that repeat the structured address, and a yearly expiring registration", 'D7x',
  '`world/parties.json` Lisavu Cotton Farm (`identity.address` lines, `legal.registration_expires`); `tools/build_examples.py` `legal_entity()` (line 292: "The island renews a farm\'s registration every year")',
  'The farm\'s `AddressLine`s repeat the structured address and mix two languages in one line; its commercial-register entry has an expiry date.',
  'Address lines only where the structured address cannot carry the information; the registration has an expiry only if the world\'s register expires.',
  'Address part: no decision (fix the lines). Expiry: part of D7x.')
c('BALE', 3, 'master data', 'Bale weight of about 227 kg as `PackSizeNumeric`', 'D14',
  '`world/items.json` cotton lint (lines 938–947: `per_package` 227, size "227")',
  '`PackQuantity` 1 / `PackSizeNumeric` 227 give the nominal bale weight as a pack size in seven cotton documents.',
  'Pack size counts units in a pack; the bale weight is a weight.',
  'Decide D14 (what the pack is), then fix items.json.')
c('HSFRAME', 3, 'master data', 'Side frame classified HS 7325.99 instead of a part of a seat', 'D15',
  '`world/items.json` side frame `hs` "732599" (line 241), `national_tariff` "73259990" (line 253)',
  'The spare side frame is classified as a general cast article; the reviews say a part of a seat (9401.99).',
  'The frame\'s heading follows the Harmonized System\'s notes for parts of seats.',
  'Decide D15.',
  note='Conflict with an earlier decision: `analysis/codelist-decisions.md` P5 confirmed "7325.99 → 42999 "Metal goods n.e.c." (bench casting)". The merge decisions (Medium, no: 9401.99) contradict it.')
c('PRICECHAIN', 3, 'master data', "Valdara's distributor price equals its public contract price; Lumeway's revised frame price is below cost", 'D16',
  '`world/items.json` prices of the bench and frame per seller (Valdara 49900 XUF; Lumeway price list `LD-PL-2026`, revision 58 XBL)',
  'Valdara sells to its distributor at the price it tenders to the public buyer in the distributor\'s own city; the revised frame price is below the purchase price.',
  'The price chain is plausible or the documents give the reason.',
  'Decide D16.')
c('DEBITROLES', 3, 'master data', 'Debit notes with accounting supplier and customer reversed', 'D17',
  '`world/documents.json` the three DebitNote entries (furniture, sea, tender): `parties` `AccountingSupplierParty` = the party debited',
  'In all three debit notes the document number and language tag name the real issuer, but the accounting supplier is the party that is charged; the tender reminder and remittance then enter the debit as a credit.',
  'The issuer of a debit note (the creditor) is its accounting supplier.',
  'Swap the two roles in documents.json; the merge decisions mark it "yes" ("probably one pattern in the generator"), so it is put to the owner as D17.')

# ------------------------------------------------------------------ stage 4: cross-flow story (goods chain)
c('STOCKCHAIN', 4, 'cross-flow story', "Goods \"from the distributor's stock\" made days before they leave, and no document moves them", 'D3',
  'the lots and manufacture dates of the sea, air and retail goods: `tools/examples_kit.py` `instances()` (line 355) with the despatch days of `sea()`, `air()` and `retail()` in `tools/examples_scenarios.py`',
  'The retail, sea and air lots are made in Urvania two or three days before Lumeway despatches them from Marrowdale "from stock"; only the road (March) and rail (April) deliveries move goods to Lumeway; the sea export cites the March road import as its previous declaration for goods made in May.',
  'Every lot Lumeway despatches was made before a documented delivery to Lumeway, or the documents say how it arrived.',
  'Decide D3 (preferred by timelines#F4: give the later goods lots of the existing deliveries).',
  deps='with MELT; CUSTOMSDECL (sea/11 previous declaration)')
c('MELT', 4, 'cross-flow story', 'One melt, one coating batch and one manufacture time for every casting and lot', 'none',
  '`world/items.json` coating batch "ZN-26-114" (line 225) and melt "M-26-0412" (line 260); `tools/examples_kit.py` `instances()` (line 355: manufacture time 06:40, serials)',
  'All castings carry melt `M-26-0412` although made on 20 March, 10 and 11 May; serials run against manufacture dates; one coating batch for four bench lots; the replacement despatch advice gives the same castings a manufacture date a day later.',
  'One melt and coating batch per production event, serials ascending with the date, the same casting with the same data in every document.',
  'Derive melt, batch and serial from the lot\'s production day (timelines#F2 option a).',
  deps='after STOCKCHAIN (D3), which may change the lots')
c('BENCHPHYS', 4, 'cross-flow story', 'The bench as shipped: pallets that do not fit, and a bench lighter than its parts', 'D2',
  '`world/items.json` bench dimensions and `gross_kg` 41.5 (line 55); `tools/examples_kit.py` `pallets()` (line 1294) and `handling_units()` (line 1366)',
  'Four assembled benches (1800 × 620 × 780 mm) do not fit the 1850 × 650 × 1650 mm pallet, 24 such pallets fit neither the trailer nor a 40-foot container; and the bench weighs less than its five slats and two side frames as other flows ship them.',
  'Pallet size, stacking and counts fit each hold; the bench\'s gross weight is at least the weight of its parts.',
  'Decide D2 (preferred: knocked down, flat-pack pallet size; heavier bench).')

# ------------------------------------------------------------------ stage 5: generator mechanisms
c('ISSUETIME', 5, 'generator mechanism', 'Documents that report or cite what happens after their own issue time', 'none',
  '`tools/build_examples.py` main loop: `IssueTime` from a hash of flow and number when the scenario gives none (lines 1704–1707); the days and times set per document in `tools/examples_scenarios.py`',
  'Issue times are spread pseudo-randomly between 08:00 and 18:00, so waybills report pickups in the afternoon of their morning issue, status reports cite waybills issued later, a cancellation follows its replacement, and revisions are dated after the issue (ten flows; 30 High).',
  'No document reports as actual, or cites, anything dated after its issue time; transport documents are issued at the moment their type implies.',
  'Derive issue times from the events and references of the flow (issue after the latest event or document cited), with the scenario overriding; build check: no actual event or referenced document after the issue timestamp (`check_consistency.py` group 10 already lists them).',
  note='Includes timelines#F6 (export declarations after the goods left) and #F8.')
c('REFID', 5, 'generator mechanism', 'References to documents under IDs no document has, or to documents the flow does not contain', 'D29',
  'reference values in the scenario code: the air order `VT-PO-26-0319` (`tools/examples_scenarios.py` `air()`, line 1940), the tender call for tenders `PWD-2026-PARKS-CFT` and replaced notices (tender enrichments, lines 6476–6560), the waste weight statement (`waste()`, line 2512)',
  'References carry IDs no example carries: an air order that does not exist, the call for tenders under a file number in eight tender documents, replaced notices for first notices, a consignment ID as document reference; others point to documents the flow does not model (waste weight statement, furniture delivery note, retail transport plan).',
  'Every reference to an example resolves to it; a reference to a document outside the examples says what it is.',
  'Wrong IDs: correct them (no decision). Missing documents: decide per flow whether to add them (D29). Build check: `flow_index.py`\'s "-> ?" references reported by the build.')
c('NUMBERING', 5, 'generator mechanism', 'Document numbers: one counter per flow shared by all issuers', 'D18',
  '`tools/examples_kit.py` `Flow.number()` (lines 52–57: `{initials}-{type}-26-{base + count}`, `base` from a CRC of the flow name)',
  'Every flow uses one block of consecutive numbers shared by all its issuers, so no issuer numbers its own documents in order (Lumeway\'s invoice of 30 April is 0236, of 14 May 0147); the same remittance number is used by three payers in utilities; the department\'s numbers run against its issue times.',
  'Per issuer (and type, if wanted) numbers rise with the issue timestamp across flows.',
  'Decide D18, then one counter per issuer in `Flow.number()` built in global issue order.')
c('PREFIX', 5, 'generator mechanism', 'Issuer prefixes: `BF` for two parties, second prefixes for signatures', 'D19',
  '`tools/examples_kit.py` `initials()` (line 36); hard-coded signature prefixes in the scenarios (e.g. "BM-SIG", "PWD-SIG", "HS-SIG")',
  'Bayforth Forwarding and Brackenmere Furniture both get `BF` (invoices, items, signatures, RF references); seven parties sign under a second prefix; one prefix-plus-infix stands for two kinds of document.',
  'Every prefix belongs to one party; each party uses one prefix; one infix means one kind.',
  'Decide D19 (e.g. a fixed prefix per party in parties.json).')
c('PROFILEEXEC', 5, 'generator mechanism', '`ProfileExecutionID` is the flow name in all 250 documents', 'D20',
  '`tools/build_examples.py` main loop (lines 1701–1703: `{FLOW}-2026-01`)',
  'One execution ID per flow joins unrelated collaborations and documents of different profiles.',
  'Each ProfileExecutionID identifies one execution of the document\'s profile, or is absent.',
  'Decide D20.',
  note='Conflict with an earlier decision: `analysis/codelist-decisions.md`: "ProfileExecutionID: stays one per flow instance." and `note/src/03-world.md`: "`ProfileExecutionID` still names the run of the process".')

# ------------------------------------------------------------------ stage 6: flow stories (smallest flows first)
def flow(key, fl, title, dec, source, wrong, after, fix, note='', deps='none'):
    c(key, 6, 'flow story', title, dec, source, wrong, after, fix, deps=deps, note=note)
    C[key]['flow'] = fl


flow('WASTESTORY', 'waste', 'Waste flow: a transboundary notification for a movement inside one town; no weighbridge statement', 'D30',
     '`tools/examples_scenarios.py` `waste()` (line 2512) and `waste_shipment()` (line 2502)',
     'The notification and movement are addressed to the customs administration\'s border office for a movement inside Ferrano; Rinova is named a disposal facility in a recovery notification; 38–40 t of bagged PE in one road load; the planned shipment reuses the first movement\'s IDs; the weight statement the movement and the invoice rest on does not exist; the invoice bills gross tonnes.',
     'The flow tells one plausible domestic (or transboundary) story with the competent authority, a recovery facility, plausible loads and a traceable billed net weight.',
     'Decide D30 (domestic vs transboundary, weight statement added).')
flow('CARNET', 'carnet', 'Carnet flow: counterfoils, time limits and the duty claim', 'D31',
     '`tools/examples_scenarios.py` `carnet()` (lines 2485 and 3761)',
     'The carnet as issued shows all four counterfoils stamped; transit through Bayvarra has no transit counterfoils; proof is requested before the re-exportation time limit; the proof does not identify the carnet; contact and office names vary.',
     'The carnet\'s counterfoils, dates and claims follow one timeline.',
     'Decide D31 (the timeline of the fair and the re-export; the duty claim goes with D8).')
flow('MASTDG', 'mast', 'Mast flow: dangerous-goods data of the battery, detector and stripper consignment', 'D32',
     '`world/items.json` dangerous-goods data of SE-BAT-48100, SE-SMK-10, SE-CS-05; `tools/build_examples.py` `hazardous_item()` (line 772); `tools/examples_scenarios.py` `mast_consignment()` (line 5736)',
     'Placard notation 7 for an excepted package; the fissile aggregate for a non-fissile americium source; the activity of one detector for ten; placard endorsements that repeat the class or the label model; orange plates for air; crates over the PI 965 IA limit; road transport data in orders and invoices.',
     'The DG data follow the air rules the world states, per package, and appear only in transport documents.',
     'Decide D32 for the yes-findings (crate weights, CAO, endorsements); the rest are encoding fixes in items.json and `mast_consignment()`.')
flow('MASTAIR', 'mast', 'Mast flow: the air waybill and the ULDs', 'D32',
     '`tools/examples_scenarios.py` `mast()` (line 5862) and `mast_consignment()` (line 5736)',
     'The air waybill has no airports or flight date and two numbers; the consignor\'s instructions carry the carrier\'s ULD numbers and positions; reefer and food settings without reason; the CPT place is "mast site".',
     'The waybill identifies the flight; instructions carry what the consignor knows.',
     'With D32.')
flow('ORESTORY', 'ore', 'Ore flow: monthly call-off, plan "as requested", bonus and moisture', 'D33',
     '`tools/examples_scenarios.py` `ore()` (line 37)',
     'The monthly call-off is typed as a plain order; the plan is confirmed "as requested" but differs; weekly vs monthly quantities; bonus and penalty neither applied nor excluded; moisture deduction without basis.',
     'The ore call-off, plan and invoice tell one agreement.',
     'Decide D33 (the train\'s arrival, bonus or penalty).')
flow('ENERGYPIPE', 'energy', 'Energy flow: 2400 MWh exported to Montebrio, sold to Ferrano Energy, imported by nobody', 'D34',
     '`tools/examples_scenarios.py` energy declarations (`ENERGY` flow, line 8672 ff.)',
     'The export declaration consigns 39200 MWh to Montebrio Power; 2400 MWh are invoiced to Ferrano Energy and have no import declaration; the import declares 36800 MWh under the same shipment ID; gas declared as dry bulk; no period or crossing point.',
     'Each buyer\'s gas is exported and imported under declarations that match its invoice.',
     'Decide D34 (split by buyer; Ferrano Energy\'s import).')
flow('ENERGYISOL', 'energy', 'Energy flow: isolated slips', 'none',
     '`tools/examples_scenarios.py` energy flow (line 8672 ff.) and `utility_statement()` (line 2708)',
     'Statement payable 0 for a billed consumption; network-use lines that cannot be told apart; the reminder in lume for a ferra debt; the surcharge line without its invoice and period; the plant\'s InformationURI is the home page.',
     'Each slip corrected in place.', 'Fix in the energy scenario.')
flow('PACKAGING', 'packaging', 'Packaging flow: isolated slips', 'none',
     '`tools/examples_scenarios.py` `packaging()` (line 3396)',
     'Goods-in point without its GLN; a note referring to a consignment note the document does not identify; no package count; a promotion discount missing on a till receipt; a tax statement in an item description.',
     'Each slip corrected.', 'Fix in the packaging scenario.')
flow('AIRSTORY', 'air', 'Air flow: the missed-flight story and the CPT order change', 'D35',
     '`tools/examples_scenarios.py` `air()` (lines 1940 and 3612)',
     '"Goes on the next day\'s flight" but the cargo arrives the same day; the cancelled despatch advice contains nothing the missed flight changed; the replacement says nothing it replaces; CPT next to "the rest stays CIF"; the buyer names the carrier.',
     'One consistent story of which flight was missed and when the goods flew.',
     'Decide D35 (preferred by air/07#F2: an evening flight on 13 May was missed).',
     deps='ISSUETIME (order of cancellation and replacement)')
flow('AIRPACK', 'air', 'Air flow: packing, consolidation and charges of the castings', 'D35',
     '`tools/examples_scenarios.py` `air_consignment()` (line 1892)',
     'The box cannot hold the eight frames; gross minus net leaves 5.6 kg for skid, box and bags; "not consolidated" with a house waybill; a warehouse as substitute carrier; two waybill numbers; freight invoiced on gross instead of chargeable weight.',
     'Packing, consolidation and charges agree across the air documents.',
     'With D35 (consolidation story); the arithmetic fixes need none.')
flow('PLASTICSCERT', 'plastics', 'Plastics flow: recycled-content certificate issued by a chamber of commerce', 'D36',
     '`world/parties.json` / `world/items.json` certificate of the PE granulate (issuer the Ferrano chamber); `tools/build_examples.py` certificates (line 987)',
     'Five documents give a chamber of commerce as issuer of a recycled-content certificate.',
     'The certificate\'s issuer is a body that can certify recycled content.',
     'Decide D36.')
flow('PLASTICSISOL', 'plastics', 'Plastics flow: barge waybill and goods data', 'D36',
     '`tools/examples_scenarios.py` `plastics()` (line 824), `barge_goods()` (line 751), `barge_consignment()` (line 801)',
     'The barge\'s CO2e is a hundredth of what its diesel produces; the freight rate as base amount; net volume of solid PE; returnable quantity counts bags; one package for 120 bags; lot IDs differ between waybill and despatch advice; standard VAT on international carriage.',
     'The barge documents describe the bags and the voyage consistently.',
     'Encoding fixes; plastics/07#F5 (VAT on carriage of exports) goes to D36.')
flow('WOOD', 'wood', 'Wood flow: slat units and isolated slips', 'D37',
     '`tools/examples_scenarios.py` `wood()` (line 3176), `quotation()` (line 3164)',
     '"Quoted per thousand slats" against a price per slat; `OrderableUnitFactorRate` 50 while quantities are single slats; two sets of terms without saying which governs; pallets charged but in no goods description; resale exemption without certificate.',
     'One unit for quoting, ordering and invoicing; charges match the goods described.',
     'Decide D37 (the orderable unit).')
flow('RAILISOL', 'rail', 'Rail flow: container train documents', 'D38',
     '`tools/examples_scenarios.py` `rail()` (lines 659 and 3522), `rail_container()` (line 487), `rail_stage()` (line 565), `rail_consignment()` (line 605)',
     'Terminal operator as network manager; the hub as destination instead of the siding; passenger quantity 0; demurrage under a vessel definition; the second container without wagon, places and events; one framework contract under two identifiers; the container "being stored" while on the train.',
     'Both containers described alike; roles and places as the rail leg has them.',
     'Encoding fixes; the yes-findings (roles of the hub, CMR vs CIM, Container Convention) go to D38.')
flow('UTILSTMT', 'utilities', 'Utility statement builder: average amount, supplier consumption, subscriber data', 'D39',
     '`tools/examples_scenarios.py` `utility_statement()` (line 2708), `consumption_line()` (line 2665), `telecom_consumption()` (line 2891)',
     'AverageAmount holds the month\'s amount; SupplierConsumption for a single supplier; SubscriberID holds the contract number; the item\'s subscriber type is a utility type; district-heating elements for electricity and water; empty descriptions.',
     'The statement elements are used by their definitions in all six statements (also energy/01).',
     'Fix `utility_statement()`; D39 for the yes-findings (subscriber data, consumer level).')
flow('UTILAMOUNTS', 'utilities', 'Utilities: excise and estimate-correction amounts', 'none',
     '`tools/examples_scenarios.py` `energy_tax()` (line 2576) and the estimate correction in `utility_statement()` (line 2708)',
     'The energy tax report carries the excise of the whole invoice in each statement; totals leave out the excise; per-unit amounts do not produce the excise; the estimate correction double-counts and its unit amount × quantity is not the amount.',
     'The statements of one invoice add up to the invoice; excise arithmetic holds.',
     'Fix the arithmetic (preferred options of utilities/01#F1, F2, 02#F1); build check for the tier arithmetic.')
flow('UTILWATER', 'utilities', 'Utilities: the household\'s water on account, the mandate and the levy', 'D39',
     '`tools/examples_scenarios.py` `utilities()` (line 2998), `levy()` (line 2538)',
     'The statement says the household pays on account monthly; invoice 09 bills and collects the full amount; the mandate is limited to 12 instructions; payable amounts leave out the sewage levy; the reminder and credit note lack references.',
     'One billing scheme for the household from statement to credit note.',
     'Decide D39 (preferred by utilities/08#F1: drop the on-account scheme).')
flow('UTILTELECOM', 'utilities', 'Utilities: the telecom statement and invoice', 'D39',
     '`tools/examples_scenarios.py` `telecom_consumption()` (line 2891)',
     '35 GB stated twice (roaming and pool); a masked number shown in full; allowances ignored in line totals; one month invoiced as "6 months"; quantities that mix minutes, gigabytes and views.',
     'The telecom statement adds up and uses its elements by definition.',
     'Fix in `telecom_consumption()`; D39 for the yes-findings.',
     note='Possibly not a problem for utilities/13#F2 and 14#F2 (blockchain identifier): `note/src/03-world.md` says "Coral net, the island\'s clearing, settles tokenised deposits on the Bank of Selanu\'s ledger".')
flow('UTILISOL', 'utilities', 'Utilities: isolated slips', 'D39',
     '`tools/examples_scenarios.py` `utilities()` (line 2998)',
     'Castrano named as subscriber of Valdara\'s subscription; OriginatorParty for the warehouse occupant; a one-time charge type for a monthly item; a tax point date on a reminder without tax.',
     'Each slip corrected.', 'Fix in the scenario; utilities/03#F6 (who subscribes) goes to D39.')
flow('PROCNOTICE', 'contest', 'Procurement notices (contest and tender): notice types, defaults, languages, links', 'D40',
     '`tools/examples_scenarios.py` `notice_head()` (line 6476), `tendering_process()` (line 6220), contest helpers (lines 8894–8943)',
     'Design-contest notices use the standard-procedure notice types CN and CAN; the requested legal form applies to the follow-up contract; the reference criterion\'s DurationPeriod is the look-back window; CandidateReductionConstraintIndicator says the candidates are reduced; PublishAwardIndicator without its situation; Urvanian declared as a notice language without Urvanian text; calls that do not link the contract notice.',
     'Notice coding follows the procedure type (design contest vs open procedure).',
     'Encoding fixes in the shared notice builders; the yes-findings with D40.')
flow('PROCQUAL', 'contest', 'Qualification requests and responses (ESPD-like) in contest and tender', 'D40',
     '`tools/examples_scenarios.py` `qualification_limits()` (line 6709) and the QualificationApplicationRequest/Response enrichments (lines 6592–6839)',
     'The buyer\'s request sets the fulfilment indicator; no exclusion grounds; responses that do not refer to the request; evidence not linked; the same text as description and value; groups whose other member is not encoded; expected values that are thresholds; "all criteria answered" with one answer.',
     'Requests ask, responses answer, linked to each other and to evidence.',
     'Fix the shared qualification builders; yes-findings with D40.')
flow('CONTESTAMT', 'contest', 'Contest: the estimated contract amount of 54,000 lume', 'D40',
     '`tools/examples_scenarios.py` `contest_project()` (line 8924)',
     'What the estimate covers is not stated, and it stays the same after the first prize rose.',
     'The estimate says what it covers and follows the prize change, or is absent.',
     'Decide with D40.')
flow('CONTESTSTORY', 'contest', 'Contest: the design team, references, prizes and versions', 'D40',
     '`tools/examples_scenarios.py` `contest_version()` (line 8901), `contest_prizes()` (line 8910), `contest_awarding()` (line 8943)',
     'The first prize of 6,000 contradicts the 8,000 of the notice; the winning team is reduced to its lead; one completed task where two references are required; requests addressed to one participant before selection; version 2 documents do not say what they change.',
     'The contest tells one story of the team, the criteria and the prize correction.',
     'Decide D40.')
flow('ROADSUBST', 'road', 'Road flow: the substituted 2026 casting', 'D41',
     '`tools/examples_scenarios.py` `road()` (line 195): the substitute line of the order response and the follow-up lines',
     'The order response replaces the old casting by the 2026 casting, but despatch, certificates, receipt and invoice do not identify it (extended ID `2026`); the proposed substitute is the old casting; an extra frame is accepted but never billed.',
     'The 2026 casting is identified the same way from the response to the invoice.',
     'Carry the extended ID through; road/13#F9 (the extra frame) with D41.')
flow('ROADCOO', 'road', 'Road flow: application and certificate of origin', 'D41',
     '`tools/examples_scenarios.py` road certificate of origin documents (`road()` line 195; enrichment `road()` line 3676)',
     'Application and certificate share ID and version; a second endorsement before the first; the buyer\'s order number as job number; an embassy endorsement by the Trade Accord Council; endorsers\' signatory contacts against their definition.',
     'Application and certificate are two documents with their own IDs, endorsements in order.',
     'Decide D41 for the endorsement roles; the rest are encoding fixes.')
flow('ROADISOL', 'road', 'Road flow: isolated slips of the truck shipment', 'D41',
     '`tools/examples_scenarios.py` `road()` (line 195), `road_stage()` (line 109), `road_consignment()` (line 139)',
     'Gross volume smaller than its handling units; journey ID for a one-off trip; required and latest delivery times disagree; notes that narrate the example; trailer seal only in a remark; package level "inner"; a recount with one package more.',
     'Each slip corrected.', 'Encoding fixes; the yes ones with D41.')
flow('FURNSCM', 'furniture', 'Furniture flow: the replenishment and sales-reporting documents', 'D42',
     '`tools/examples_scenarios.py` `furniture()` (lines 3268 and 3685), `collab()` (line 3263)',
     'Request lines that ask for activity, forecast and metric at once; a replenishment owner that describes a division of work; exception status codes for shipments used for sales; one four-week figure where weekly ones were requested; the weather as an activity property.',
     'Each collaboration document uses its elements by definition, one kind of criterion per line.',
     'Decide D42 for the yes-findings; encoding fixes otherwise.')
flow('FURNORDER', 'furniture', 'Furniture flow: quotation, orders, invoice, return and credit', 'D42',
     '`tools/examples_scenarios.py` `furniture()` (lines 3268 and 3685), `set_parts()` (line 3224)',
     'Optional cushions only in a note; the initial order twice the target inventory; a repeat order while stock suffices; sub-line prices without quantities; a restocking deduction on a return the maker asked for; the quotation used as a contract.',
     'Order, stock and return figures follow the replenishment profile and the story.',
     'Decide D42.')
flow('FURNPUBLIC', 'furniture', 'Furniture flow: the department\'s desks and installation', 'D42',
     '`tools/examples_scenarios.py` `furniture()` documents 15–17',
     'A packaging-disposal charge the order does not contain; a zero tax total without category; the place of work named only; an hourly price without base quantity.',
     'Invoice and work report bill what was ordered.', 'Decide with D42.')
flow('COTTONSELFBILL', 'cotton', 'Cotton flow: self-billing between ginnery and farm, and the mill\'s forecasts', 'D43',
     '`tools/examples_kit.py` `self_billed()` (line 1115); `tools/examples_scenarios.py` `cotton()` (line 2082)',
     'A customs broker as tax representative of a domestic purchase; invoice periods before the delivery; references that say nothing; a charge whose text calls it an allowance; the farm as payee of a credit that flows to the ginnery; "twenty per cent more" is 25 %.',
     'The self-billed documents and forecasts tell one season agreement.',
     'Decide D43 for the yes-findings.')
flow('COTTONCLASS', 'cotton', 'Cotton flow: classing and phytosanitary certificates', 'D43',
     '`tools/examples_scenarios.py` `cotton()` (line 2082), certificate documents 10 and their references',
     'A forecast carries a classing certificate signed 18 days later; a downgrade cites a certificate that says Middling and is signed later; "10 bales sampled out of 80" for 27 bales; a version 1 with a previous version from last season; a phytosanitary certificate issued by a chamber of commerce.',
     'Certificates exist before they are cited and describe the shipment.',
     'Decide D43 (who issues the phytosanitary certificate).')
flow('CLASSING', 'cotton', 'Cotton flow: classing results carried as the applicant\'s remarks', 'none',
     '`tools/examples_scenarios.py` cotton certificate (`cotton()` line 2082)',
     'The classing results stand in the applicant\'s `Remarks` in seven documents.',
     'The results are in the certificate\'s own elements.', 'Move them (encoding).')
flow('COTTONSEA', 'cotton', 'Cotton flow: the sea export (bill of lading, VGM, pre-arrival report)', 'D43',
     '`tools/examples_scenarios.py` `cotton()` (line 2082), `bl_distribution()` (line 4418)',
     'The original bill goes to a bank while the instructions ask for the forwarder; the bank as mortgage holder without any financing; "freight collect" while the forwarder invoices freight; the VGM without method or date; the pre-arrival report not tied to the shipment.',
     'The sea documents follow the instructions and one payment arrangement.',
     'Decide D43 (documentary collection or not).')
flow('RETAILCAT', 'retail', 'Retail flow: catalogue request, catalogue, updates and deletion', 'D44',
     '`tools/examples_scenarios.py` retail catalogue enrichments (lines 3847–3990), `catalogue_update_head()` (line 3951)',
     'A request for an update of a catalogue that exists nowhere; a "new" catalogue that supersedes a version; references to the catalogue with wrong issue and revision times; the update line pointing to the bench for the frame; "Unchanged." as trading terms.',
     'The catalogue versions and their references agree.',
     'Decide D44 (new catalogue vs update).')
flow('RETAILPROMO', 'retail', 'Retail flow: promotion, forecast, inventory and the shop sale', 'D44',
     '`tools/examples_scenarios.py` `retail()` (lines 953 and 3628), `promo_allowance()` (line 909)',
     'The forecast\'s promotion reference resolves nowhere; a store-opening event nothing supports; the promotion price valid for another period than the promotion; planned sales at the regular price; sale IDs encode 18 May for a purchase on 15 May.',
     'The promotion has one period and one price chain from event to receipt.',
     'Decide D44 for the yes-findings.')
flow('RETAILTRANSPORT', 'retail', 'Retail flow: the delivery to the store (carrier references, arrival day)', 'D44',
     '`tools/examples_scenarios.py` `retail()` documents 11–17',
     'Three different carrier references for one shipment; the shipping-document reference points to the request; "on its way, expected 29 April 14:00" but received 30 April 10:40; "late" for a slot no document agreed.',
     'One carrier reference and one delivery day across the transport documents.',
     'Decide D44 (the delivery day; merge decision Medium/yes).')
flow('RETAILISOL', 'retail', 'Retail flow: isolated slips', 'D44',
     '`tools/examples_scenarios.py` `retail()` (lines 953, 3628)',
     'Purchase-card data capability described as the e-document channel; the invoice bills 24 benches against a receipt of 23; a tax point date without event; the factor as payee of a credit owed to the buyer.',
     'Each slip corrected.', 'With D44.',
     note='Possibly not a problem for retail/22#F7 (full card number and CVV in the webshop order): `note/src/03-world.md` says "A webshop order is different: the card is not at hand, so the order carries the full number, the card\'s dates and its security code".')
flow('SEACIF', 'sea', 'Sea flow: the CIF sale, freight and insurance', 'D45',
     '`tools/examples_scenarios.py` `sea_invoice_terms()` (line 1357), `cif_value()` (line 1154), `sea_order_response()` (line 1456)',
     'Freight and insurance are charged on top of a price agreed CIF; the confirmed total differs from the invoice; the insurer as insurance party; one insurance split over two policies; pre-carriage freight that nobody bills; the statement repeats the invoice\'s freight.',
     'Under CIF the price includes freight and insurance, consistently in order, invoice, statement and declarations.',
     'Decide D45 (preferred by sea/22#F3: drop the two charges).',
     deps='CUSTOMSVALUE (D7)')
flow('SEAAGREE', 'sea', 'Sea flow: business card, digital agreement and capabilities', 'D45',
     '`tools/examples_scenarios.py` `digital_service()` (line 4890), `service_customization()` (line 4881), sea documents 01–04',
     'Audit evidence issued by the audited company; tendering-only evidence elements in a business card; a bilateral agreement signed by one participant; Lumeway\'s own EDI terms "signed" by the Trade Accord Council; billing processes that do not match the flow.',
     'The agreement documents describe what the parties actually exchange.', 'Decide D45 for the yes-findings.')
flow('SEASHIP', 'sea', 'Sea flow: bill of lading and ship reports', 'D45',
     '`tools/examples_scenarios.py` `sea_consignment()` (line 1222), `sea_equipment()` (line 1171), `bl_extras()` (line 4403)',
     'One SSCC for the frames pallet and a box; the bill\'s total invoice amount is the goods value; the final delivery party is the buyer, not its 3PL; the road chassis still attached on board; crew lists of 3 of 14; a WHO affected area; the port company issuing sanitation certificates.',
     'The bill and the ship reports describe the shipment and the ship consistently.', 'Decide D45 for the yes-findings.')
flow('SEAFINANCE', 'sea', 'Sea flow: factoring, statement, payment and the island\'s debit note', 'D45',
     '`tools/examples_scenarios.py` `sea_with_debit()` (line 5904) and the sea finance documents 22–28',
     'The status response reports a payment made a month later; paid amounts differ from the remittance advice; the factor as accounting supplier of the invoice line; the storage charge three times in the debit note; the deposit as an invoice period.',
     'Factoring, statement and payments agree.', 'Encoding fixes; yes-findings with D45.')
flow('SEAISOL', 'sea', 'Sea flow: isolated slips', 'D45',
     '`tools/examples_scenarios.py` `sea()` (lines 1527 and 3551)',
     'A booking deadline already past when the service is offered; weekly sailing day Friday against a Thursday sailing; a service classified with a goods code; the rejected frame not identified; the full-container discount not applied; the on-carriage leg 19–21 May dated nowhere (timelines#F7).',
     'Each slip corrected.', 'With D45.')
flow('TENDERTERMS', 'tender', 'Tender: tendering terms copied into notices, call, award and contract', 'D46',
     '`tools/examples_scenarios.py` `tendering_terms()` (line 6283), `auction_terms()` (line 6189), `tendering_process()` (line 6220), used by tender/01, 02, 03, 21, 22, 23 and 24',
     'The shared terms repeat the same errors in five documents: a security-clearance date with "not required", a guarantee of 2400.00 that is 2 % of nothing, a turnover criterion "at least" coded "greater than", a "precise" subcontract share of 30 % next to 3.5 %, paper copies as a concession fee, variants unconstrained with a maximum of one, an auction and a framework agreement nobody holds, design-contest indicators in a supply procedure.',
     'The procedure\'s terms are stated once, correctly, and the later documents repeat them unchanged.',
     'Fix `tendering_terms()` once (most options need no decision); D46 for the yes-findings (auction, framework values, budget).')
flow('TENDERPROJECT', 'tender', 'Tender: the procurement project and its lots', 'D46',
     '`tools/examples_scenarios.py` `procurement_project()` (line 6110), `procurement_lots()` (line 6462), `contract_name()` (line 6872)',
     'Lot 2 is works in the prior information notice and services elsewhere; lot 2 is described with the bench data; the buyer\'s estimates equal the winning tender to the cent; the project and programme have different names and codes.',
     'One description of project and lots, and an estimate made before the tenders.',
     'Decide D46 (the estimate).')
flow('TENDERDATES', 'tender', 'Tender: procedure periods against the notices\' issue dates', 'D46',
     '`tools/examples_scenarios.py` `out_day()` (line 6491) and the notice/award dates in `tender()` (lines 2360, 3459)',
     'Requested publication and procedure periods lie before the notices\' issue dates; interest and registrations after the reception period; the appeal period is the award\'s before the award existed; the contract signed on the last appeal day.',
     'Every period lies after the document that announces it and fits the procedure.',
     'Decide D46 (move the notices to late January, or the periods).')
flow('TENDERQUALIF', 'tender', 'Tender: expressions of interest, status, register extract and Valdara\'s qualification', 'D46',
     '`tools/examples_scenarios.py` tender documents 04–13 (enrichments after line 6508)',
     'Two competing tenderers presented as one group; OperationType holds the line of business; capability figures that differ between the register extract and Valdara\'s qualification; one reference supply where three are required.',
     'The qualification figures are one set, stated the same everywhere.', 'Decide D46.')
flow('TENDERGUAR', 'tender', 'Tender: the guarantee certificate', 'D46',
     '`tools/examples_scenarios.py` tender document 14 (guarantee)',
     'A bank guarantee described as immobilised shares of the tenderer itself; the tenderer as issuer of the bank\'s certificate; value and market value three days apart; tenders that do not refer to their guarantee.',
     'One kind of guarantee, issued by the bank, referenced by the tender.', 'Decide D46.')
flow('TENDERBIDS', 'tender', 'Tender: the tenders, receipt and withdrawal', 'D46',
     '`tools/examples_scenarios.py` `tender_lines()` (line 6557) and documents 15–19',
     'Warranty five years on the line and six in the criterion response; the tenderer\'s own costs as fees of the project; no unit prices although the procedure evaluates them; identical ordering terms in competing tenders.',
     'Each tender states one offer, evaluated as tendered.', 'Decide D46 for the yes-findings.')
flow('TENDERAWARD', 'tender', 'Tender: award, notifications and appeal', 'D46',
     '`tools/examples_scenarios.py` `tender_result()` (line 6894), `appeal_terms()` (line 6884)',
     'The opening still "scheduled" in the award notice; the review board as information party, receiver and mediator without contact; the winner\'s subcontract price told to the loser.',
     'The award documents report a completed opening and a reachable appeal body.', 'Decide D46.')
flow('TENDERCALLOFF', 'tender', 'Tender: contract, catalogue and call-off (releases, despatch, credit, reminder)', 'D46',
     '`tools/examples_scenarios.py` `tender()` (lines 2360, 3459) and `tender_with_credit()` (line 6029)',
     'The contract identifies neither the accepted tender nor the prices; catalogue validity shifted against the contract; 200 benches "outstanding" that were never ordered; no serial numbers although the contract requires them; two statements of how the credit is settled; interest paid that the contract does not make due.',
     'The call-off documents execute the contract as signed.', 'Decide D46.')
flow('TENDERINSTALL', 'tender', 'Tender: the installation billed but never ordered', 'D46',
     '`tools/examples_scenarios.py` `tender()` release order (lines 2360, 3459) and invoice',
     'The release order has one line (the benches); the invoice bills forty installations, invoiced before they can be done, taxed as a service to a business; the penalty is for late installation of a service billed as supplied; "by the manufacturer\'s installers" although a subcontractor installs.',
     'The installation is ordered, performed, accepted and then billed, by the party the award names.',
     'Decide D46 (preferred: order line for the installation, separate later invoice).',
     deps='CONTRACTTERMS (D6), TENDERTAX (D10)')
flow('TENDERCOLOUR', 'tender', 'Tender: moss green ordered, grey identified', 'none',
     '`tools/examples_scenarios.py` tender order change and despatch (`tender()` lines 2360, 3459); colour codes in `world/codelists/lists.json`',
     'The order change asks for moss green and the lot is made green, but despatch, declarations, invoice and credit note identify the grey variant while charging the special colour.',
     'From the change on, every document identifies the green variant.',
     'Carry the green variant (ExtendedID, colour property) through; add the colour code to the world list if missing.')

STAGES = {
    1: ('Fixes that need no decision and no story change',
        'Encoding in shared builders and simple master-data corrections that the merge decisions or the reviews settle. They touch many files and remove most of the noise, so later stages are reviewed against a cleaner set.'),
    2: ('Owner decisions on world rules, then their implementation',
        'Geography, calendar, payment terms, customs, tax and language rules. Each needs D-numbers answered first; several contradict an earlier decision or the world story and must be settled before any example changes.'),
    3: ('Master data',
        'Party and item data in world/*.json that need an owner choice (dates, sizes, identifiers, classes, brands).'),
    4: ('Cross-flow story: the goods chain',
        'Which lots reach Lumeway and how the bench ships; this changes product data in several flows at once.'),
    5: ('Generator mechanisms: time, numbering, references',
        'Issue times, document numbers, prefixes and references are derived by method; fix the method once, after the stories that change dates and documents are settled.'),
    6: ('Flow stories, smallest flows first',
        'Each flow\'s remaining findings, per flow in the order waste, carnet, mast, ore, energy, packaging, air, plastics, wood, rail, utilities, contest, road, furniture, cotton, retail, sea, tender.'),
    7: ('Build checks',
        'No cause is only a missing check. The checks below guard causes of the earlier stages so that the errors do not come back.'),
}
