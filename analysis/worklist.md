# Worklist: the review findings by root cause

**State.** This file groups the 3,348 review findings into 128 root causes and orders the work of fixing them. It was made on 2026-11-15, before the owner's decisions, and was brought up to date with decisions D1 to D27 of `analysis/worklist-decisions.md` on 2026-11-16, working from commit 4afbded. Decided: D1 to D5 and D7 to D27 (26 decisions, 28 causes); D6 (signatures) is deferred to a stage of its own. Every cause section now says what was decided, what a decision changed or touched, and whether the cause is ready to fix now or what it waits for; 1,906 findings are ready. Next: the flow decisions D28 to D45 and the bulk confirmation D46, with the owner, one at a time, each starting with its open points and its goods balance. Where this file and the decisions file differ, the decisions file is the authority. **Do not regenerate this file with `analysis/review-scripts/worklist/make_docs.py`:** it would overwrite these hand edits and the hand-edited decisions file.

Made on 2026-11-15 at commit f07f6e1 (branch `claude/stoic-noether-5pboei`). Read: the 250 merged per-example reviews (`world/examples/<flow>/*.llm-review.<run>.merged.md`, 15 thorough runs from `20261112T1415Z-thorough` to `20261114T1433Z-thorough`) and the six topic files of the consistency review `20261114T2143Z-consistency` (index `analysis/consistency-review.20261114T2143Z-consistency.md`), with `analysis/review-merge-decisions.md`, `analysis/codelist-decisions.md`, `note/src/03-world.md` and the generators for the source places.

**3348 findings** in 256 review files (18 flows plus the consistency review): **293 High, 908 Medium, 2147 Low**; 921 are marked "Needs decision: yes". They are assigned to **128 causes**; 1960 findings wait on one of **46 owner decisions** (`analysis/worklist-decisions.md`). These are the numbers as the file was made; the state after the decisions is in the Summary.

How the assignment was made: `list_findings.py` turns every finding into one row of a table (title, severity, decision, the element names and values of its XPath lines). An ordered list of rules (patterns over title, elements and flow; first match wins) assigns a cause; about 150 findings that the rules put in the wrong place were corrected by hand after reading their titles, and the 32 consistency findings were assigned by reading. Each cause was then checked against the titles of all its findings, the options of every High finding and the full text of samples; the source place was found with grep in `tools/` and `world/`. Every finding has exactly one cause (`analysis/worklist-assignments.csv`).

Reproduce the findings table:

    python3 -I .claude/skills/ubl-example-review/scripts/list_findings.py    # writes .review/worklist/{findings,outside,refuted}.csv

## How to read this

- A **cause** is the place in the source (a builder, a default, a world-data value, a scenario) that produces findings. Fixing it resolves all its findings at once; a fixing session takes one cause (or one stage) at a time.
- **Kind**: encoding (a shared builder writes the wrong element or value), master data (world/*.json), world rule (a rule the owner must set), cross-flow story, generator mechanism (times, numbers, references derived by method), flow story (one flow's scenario). No cause is only a missing build check; the checks are listed in stage 7.
- **Decision**: "none" (the reviews and the merge decisions agree on the fix), "taken: …" (an earlier decision settles it), or "owner: D<n>" (see `analysis/worklist-decisions.md`). Findings marked "yes" inside a cause without an owner decision are confirmed in bulk under D46. Since the decisions of 2026-11-15/16 a cause header says "decided (D<n>, date)" or "deferred (D6, 2026-11-16)", and the summary table "decided: D<n>" or "deferred: D6".
- **Decided, Touched by, Not settled, State**: "Decided" gives the outcome of the cause's own decision, and which findings it dismisses; "Touched by" names a decision or open point that changes a cause it does not name; "Not settled by D<n>" marks what a decision leaves open for the cause; "State" says whether the cause is ready to fix now (no open decision, no open point that blocks it, no conflict), ready in part (with the findings that wait), or what it waits for. The column "Now" of the summary table gives the same in short ("owner, not settled": a point the decisions leave open that has no D- or O-number yet).
- **Files** counts review files, one per example (plus the consistency topic files). Severity counts are per finding.
- "Possibly not a problem" and "Conflict" notes mark findings that contradict the world story or an earlier decision. They stay assigned; the owner decides.
- Example citations name the example file and the absolute XPath in one pair of backticks, followed by the quoted value; all of them are checked with `check_xpaths.py` and `check_values.py`.

## Summary

After decisions D1 to D27: **28 causes (942 findings) are decided** (26 decisions: D1 to D5 and D7 to D27); **1 cause (38 findings) is deferred** (D6, the signatures stage); **48 causes (877 findings) still need the owner** (the flow decisions D28 to D45); 51 causes (1,491 findings) never needed an owner decision, and 103 of their findings are marked "yes" for the bulk confirmation D46, which is still open. **Ready to fix now: 1,906 findings**: 48 whole causes with 1,440 findings, and 466 findings of 19 causes that are ready in part. How the counts are made: see "How the counts are made" at the end of the Order of work.

| Kind of cause | Causes | Findings | High | Decided (D1 to D27): causes / findings | Deferred (D6) | Needing the owner (D28 to D45) | No owner decision | Ready now: findings (whole causes) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| encoding | 36 | 840 | 54 | 0 | 0 | 0 | 36 / 840 | 576 (30) |
| master data | 16 | 853 | 51 | 9 / 307 | 0 | 0 | 7 / 546 | 780 (9) |
| world rule | 15 | 647 | 27 | 14 / 609 | 1 / 38 | 0 | 0 | 451 (3) |
| cross-flow story | 3 | 17 | 5 | 2 / 11 | 0 | 0 | 1 / 6 | 15 (2) |
| generator mechanism | 6 | 108 | 52 | 3 / 15 | 0 | 1 / 27 | 2 / 66 | 57 (0) |
| flow story | 52 | 883 | 104 | 0 | 0 | 47 / 850 | 5 / 33 | 27 (4) |
| **Total** | **128** | **3,348** | **293** | **28 / 942** | **1 / 38** | **48 / 877** | **51 / 1,491** | **1,906 (48)** |

| Cause | Title | Kind | Findings | Files | Flows | H/M/L | Decision | Source (short) | Now |
|---|---|---|---:|---:|---:|---|---|---|---|
| C01 | Party master data copied into documents that do nothing with it | encoding | 245 | 213 | 17 | 0/0/245 | taken: merge decisions, rows "Party master data copied …" and "`CorporateStockAmount` holds share capital" | tools/build_examples.py, place_parties() | waits: owner, not settled |
| C02 | One contact template per kind of party, whatever the role | master data | 226 | 213 | 18 | 1/0/225 | taken: merge decisions, row "Contacts whose name, job title and department contradict …" | world/parties.json, tools/build_examples.py | ready |
| C03 | Urvanian province written into `Region` | master data | 111 | 111 | 15 | 0/104/7 | taken: merge decisions, row "Province … in `Region`" | world/parties.json, world/countries.json | ready |
| C04 | Public bodies described as companies in a commercial register | encoding | 88 | 83 | 13 | 0/77/11 | taken: merge decisions, row "Public bodies … as companies" | tools/build_examples.py, legal_entity() | ready |
| C05 | Lumeway's "Gate 3" in its postal address | master data | 76 | 76 | 5 | 0/76/0 | taken: merge decisions, row "`AdditionalStreetName` = "Gate 3"" | world/parties.json | ready |
| C06 | References that give only an ID | encoding | 59 | 59 | 13 | 0/0/59 | taken: merge decisions, row "References with only an ID and no document type" | tools/examples_scenarios.py, ref() | ready |
| C07 | The department's party tax exemption reason is worded as a transaction | master data | 52 | 52 | 2 | 0/0/52 | taken: merge decisions, row "Party tax exemption reason worded as a transaction" (in the parties review's Known table) | world/parties.json, world/countries.json | ready |
| C08 | Party roles that repeat another role or do not fit their definition | encoding | 41 | 39 | 12 | 0/7/34 | none | world/documents.json, tools/build_examples.py | ready |
| C09 | Bench emission: 96 kg with factor 0.82 per 1 EA | master data | 40 | 40 | 6 | 40/0/0 | taken: merge decisions, row "Bench emission triple" | world/items.json, tools/build_examples.py | waits: D28 1, O25 39 |
| C10 | Locations named after companies or their office addresses | encoding | 36 | 29 | 11 | 1/4/31 | none | tools/examples_kit.py, leg_places() | ready |
| C11 | Currencies and exchange rates with nothing to convert, or the wrong currency | encoding | 34 | 25 | 7 | 7/7/20 | taken: merge decisions, row "Exchange rates with nothing to convert …" | tools/examples_kit.py, price_block() | ready 22 of 34; D28 10, D30 2 |
| C12 | Customs declaration builders: goods items, offices, previous declaration and issuer | encoding | 32 | 17 | 9 | 5/7/20 | none | tools/examples_kit.py, goods_items() | ready 31 of 32; D42 1 |
| C13 | Identifiers built from flow names, file numbers and other identifiers | generator mechanism | 28 | 28 | 7 | 0/0/28 | none | tools/examples_kit.py, tep() | ready 2 of 28; signatures stage 26 |
| C14 | The buyer's cost centre does not fit what is bought | master data | 24 | 24 | 11 | 1/2/21 | none | tools/examples_kit.py, cost_centre() | ready 22 of 24; D28 1, D32 1 |
| C15 | Shipment gross weight without the transport equipment | encoding | 24 | 24 | 6 | 5/15/4 | taken: merge decisions, row "Shipment `GrossWeightMeasure` without the transport equipment" | tools/examples_kit.py, gross_weight() | ready |
| C16 | "NoStatus" as document or line status | encoding | 24 | 24 | 10 | 0/0/24 | taken: merge decisions, row "`NoStatus` as status code" | tools/examples_kit.py, despatch_advice() | ready |
| C17 | Remittance advices: the invoice twice on a line, two payment-order references, header parties repeated | encoding | 21 | 10 | 8 | 0/0/21 | none | tools/examples_kit.py, remittance() | ready |
| C18 | Transport events without type or place, or as generic events where a dedicated one exists | encoding | 19 | 17 | 6 | 0/9/10 | none | tools/examples_kit.py, event() | ready |
| C19 | Framework transport-plan clauses and periods mis-encoded | encoding | 19 | 8 | 6 | 4/7/8 | none | tools/examples_kit.py, tep_terms() | ready |
| C20 | `ShippingOrderID` holding the consignment or shipment ID | encoding | 18 | 18 | 9 | 7/10/1 | taken: merge decisions, row "`ShippingOrderID` holding the consignment or shipment ID" | tools/examples_kit.py, waybill() | ready |
| C21 | Transport requests, instructions, waybills and manifests that do not say what, from where, to where or when | encoding | 18 | 18 | 9 | 0/17/1 | none | tools/examples_kit.py, tep_request() | ready |
| C22 | Item properties of the slat: validity periods, repeated length, full specification | master data | 17 | 7 | 1 | 0/0/17 | none | world/items.json, tools/build_examples.py | ready 14 of 17; O20 3 |
| C23 | Places and offices given only by name or text, without the identifier they have elsewhere | encoding | 16 | 16 | 8 | 0/0/16 | none | tools/examples_kit.py, place() | ready |
| C24 | Tax totals and taxable amounts that ignore the document's own charges, or state an empty zero | encoding | 14 | 13 | 8 | 5/1/8 | taken: merge decisions, row "Taxable amount that ignores the document's own allowance or charge" | tools/examples_kit.py, tax_total() | ready |
| C25 | Catalogue encoding: territory of the seller, "Active" status, CatalogueIndicator, discounts and dependent prices | encoding | 12 | 5 | 3 | 3/5/4 | none | tools/examples_kit.py, catalogue_terms() | ready |
| C26 | Documents referenced as a kind they are not | encoding | 11 | 9 | 3 | 0/7/4 | none | self_billed(), tools/examples_kit.py | ready 8 of 11; D30 1, D32 2 |
| C27 | Despatch advices that do not say when the goods leave or arrive | encoding | 10 | 10 | 9 | 0/8/2 | none | tools/examples_kit.py, despatch_advice() | ready |
| C28 | Orders without a requested delivery date | encoding | 10 | 10 | 7 | 0/0/10 | none | tools/examples_kit.py, order() | ready |
| C29 | Urvania's national tariff subheading in other countries' documents | encoding | 10 | 10 | 5 | 0/2/8 | taken: `analysis/codelist-decisions.md` Q24 ("tariffs, rates and exemptions stay national") and `note/src/03-world.md` ("in Urvania, the national tariff code") | world/items.json, tools/examples_kit.py | ready |
| C30 | Transport document type fixed per mode, not per convention and scope | encoding | 10 | 10 | 7 | 1/4/5 | none | tools/examples_kit.py, waybill() | ready 9 of 10; D37 1 |
| C31 | Electricity, gas, water and levies classified as services | encoding | 9 | 6 | 3 | 0/5/4 | none | tools/examples_kit.py, tax_category() | ready |
| C32 | Invoices not linked to the delivery they bill | encoding | 8 | 8 | 5 | 0/0/8 | none | tools/examples_kit.py, invoice() | ready |
| C33 | "Three originals" against the distribution list | encoding | 8 | 8 | 8 | 3/0/5 | taken: merge decisions, row "Waybill note "three originals" against the distribution list" | tools/examples_kit.py, waybill() | ready |
| C34 | Line IDs reused for another line | encoding | 7 | 7 | 2 | 4/0/3 | none | tools/examples_kit.py, tools/examples_scenarios.py | ready |
| C35 | One transport service code per mode | encoding | 7 | 7 | 3 | 7/0/0 | none | tools/examples_kit.py | ready |
| C36 | Ad valorem indicator and declared carriage value without a valuation | encoding | 5 | 5 | 3 | 2/0/3 | none | tools/examples_kit.py, waybill() | ready |
| C37 | Order references in the wrong element | encoding | 5 | 4 | 3 | 0/3/2 | none | tools/examples_scenarios.py, air() | ready |
| C38 | Bayvarra's surcharge "per month" encoded as one month only | encoding | 5 | 5 | 2 | 0/0/5 | none | tools/examples_kit.py, payment_terms() | ready |
| C39 | Payment notes that call every document an invoice | encoding | 4 | 4 | 2 | 0/0/4 | none | tools/build_examples.py, account() | ready 2 of 4; D30 1, D32 1 |
| C40 | Pallets listed as packages contained in themselves | encoding | 3 | 2 | 2 | 0/3/0 | none | tools/examples_kit.py, handling_units() | ready |
| C41 | `JourneyID` holding a voyage or month instead of the service schedule | encoding | 3 | 3 | 2 | 0/0/3 | none | tools/examples_kit.py, means() | ready |
| C42 | A line marked both confidential and internal | encoding | 2 | 2 | 2 | 0/0/2 | none | tools/examples_scenarios.py | ready |
| C43 | Temperature code given next to a measured value | encoding | 2 | 2 | 2 | 0/2/0 | none | tools/examples_scenarios.py | ready |
| C44 | `VI-C180-2026` replaces a frame in one catalogue and a bench in a tender | encoding | 1 | 1 | 0 | 0/0/1 | none | tools/examples_scenarios.py | ready |
| C45 | `Language/LocaleCode` = `en` | world rule | 213 | 213 | 15 | 0/213/0 | decided: D1 | tools/build_examples.py, party() | ready |
| C46 | English renderings tagged with the issuer's country, Italian names tagged as English, legal form untagged | world rule | 179 | 123 | 15 | 0/0/179 | decided: D2 | tools/build_examples.py, language_tag() | ready |
| C47 | `FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING for a cradle-to-gate footprint | world rule | 74 | 40 | 7 | 0/74/0 | decided: D10 | world/items.json, world/codelists/lists.json | waits: O25 |
| C48 | Catalogue and product-passport data copied into business documents | world rule | 41 | 38 | 8 | 0/0/41 | decided: D11 | tools/build_examples.py, item() | waits: O20 |
| C49 | Signature aggregates with only an ID and a signatory | world rule | 38 | 38 | 4 | 0/1/37 | deferred: D6 | tools/examples_kit.py, tep() | waits: signatures stage |
| C50 | Tax category O for goods, 0 % on O, and Lisavu's tax scheme without ID | world rule | 29 | 13 | 4 | 0/6/23 | decided: D15 | tools/examples_kit.py, tax_rule() | ready 29 of 29 (D30 and D31 decided) |
| C51 | Contract payment terms never applied by the invoices under the contract | world rule | 12 | 10 | 4 | 10/0/2 | decided: D22 | tools/examples_kit.py, payment_terms() | ready 9 of 12; D28 3 |
| C52 | Customs value on a different basis in each flow | world rule | 12 | 12 | 6 | 1/6/5 | decided: D16 | tools/examples_kit.py, goods_items() | waits: O46 |
| C53 | Documents dated at the weekend against a Monday-to-Friday week | world rule | 12 | 12 | 6 | 1/2/9 | decided: D27 | tools/examples_scenarios.py, world/parties.json | ready 9 of 12; D28 3 |
| C54 | Bayvarran withholding tax and tax representative only in the tender, and Urvania's "service to a business abroad" for a public body | world rule | 10 | 5 | 1 | 0/2/8 | decided: D17 | tools/examples_scenarios.py, withholding() | ready 7 of 10; D28 3 |
| C55 | Standard terms IDs that do not mean the same number of days everywhere | world rule | 8 | 8 | 4 | 8/0/0 | decided: D23 | tools/examples_kit.py, payment_terms() | ready 7 of 8; D30 1 |
| C56 | The map scale: all coordinates inside 35 km, against distances and times of hours and days | world rule | 8 | 7 | 2 | 4/0/4 | decided: D19 | world/countries.json, tools/build_examples.py | waits: D44 4, O82 4 |
| C57 | Duties, import taxes and Trade Accord preference stated nowhere | world rule | 6 | 5 | 4 | 1/2/3 | decided: D18 | tools/examples_scenarios.py, import_extras() | ready 4 of 6; D40 2 |
| C58 | One sea voyage with four passage times | world rule | 4 | 3 | 1 | 2/1/1 | decided: D19 | tools/examples_scenarios.py, sea() | waits: O91 (rule settled in D30) |
| C59 | Lisavu's capital: "Port Wrenfield" in English addresses, "Selanu" in every other English text | world rule | 1 | 1 | 0 | 0/1/0 | decided: D3 | world/countries.json, tools/build_examples.py | ready |
| C60 | Default founding date 1996-01-01 and size classes that do not fit the parties | master data | 181 | 169 | 15 | 4/0/177 | decided: D4 | world/parties.json, tools/codelists.py | ready 165 of 181; D28 8, owner, not settled 1, O17 7 |
| C61 | World item numbers that are valid GTIN-12s; Valdara's items under Lumeway's GS1 prefix | master data | 76 | 54 | 9 | 0/0/76 | decided: D5 | world/items.json, world/parties.json | ready 74 of 76; owner, not settled 2 |
| C62 | The maker's brand on the store's own-line garden set | master data | 12 | 12 | 1 | 0/0/12 | decided: D7 | world/items.json, tools/build_examples.py | ready |
| C63 | Lisavu Cotton Farm: address lines that repeat the structured address, and a yearly expiring registration | master data | 11 | 6 | 2 | 0/0/11 | decided: D4 | world/parties.json, tools/build_examples.py | ready |
| C64 | Industry classes that leave out what the party does | master data | 9 | 9 | 2 | 0/0/9 | decided: D8 | world/parties.json | ready |
| C65 | Bale weight of about 227 kg as `PackSizeNumeric` | master data | 7 | 7 | 1 | 0/0/7 | decided: D12 | world/items.json | ready |
| C66 | Debit notes with accounting supplier and customer reversed | master data | 5 | 5 | 3 | 5/0/0 | decided: D9 | world/documents.json | ready (D28, D30, D32 decided) |
| C67 | Side frame classified HS 7325.99 instead of a part of a seat | master data | 5 | 5 | 2 | 0/4/1 | decided: D13 | world/items.json | waits: O27 |
| C68 | Valdara's distributor price equals its public contract price; Lumeway's revised frame price is below cost | master data | 1 | 1 | 0 | 0/0/1 | decided: D14 | world/items.json | ready |
| C69 | The bench as shipped: pallets that do not fit, and a bench lighter than its parts | cross-flow story | 7 | 6 | 3 | 1/3/3 | decided: D20 | world/items.json, tools/examples_kit.py | ready |
| C70 | One melt, one coating batch and one manufacture time for every casting and lot | cross-flow story | 6 | 4 | 2 | 3/0/3 | none | world/items.json, tools/examples_kit.py | ready 4 of 6; D39 2 |
| C71 | Goods "from the distributor's stock" made days before they leave, and no document moves them | cross-flow story | 4 | 4 | 1 | 1/1/2 | decided: D21 | tools/examples_kit.py, instances() | ready |
| C72 | Documents that report or cite what happens after their own issue time | generator mechanism | 38 | 32 | 9 | 30/1/7 | none | tools/build_examples.py, tools/examples_scenarios.py | ready 35 of 38; D30 1, D34 1, D39 1 |
| C73 | References to documents under IDs no document has, or to documents the flow does not contain | generator mechanism | 27 | 25 | 8 | 20/3/4 | owner: D38 | tools/examples_scenarios.py, air() | ready (D38 decided) |
| C74 | Document numbers: one counter per flow shared by all issuers | generator mechanism | 10 | 8 | 3 | 2/1/7 | decided: D24 | tools/examples_kit.py, Flow.number() | waits: after stage 6 (D24) |
| C75 | Issuer prefixes: `BF` for two parties, second prefixes for signatures | generator mechanism | 4 | 3 | 1 | 0/1/3 | decided: D25 | tools/examples_kit.py, initials() | waits: after stage 6 (D24) 2, signatures stage 2 |
| C76 | `ProfileExecutionID` is the flow name in all 250 documents | generator mechanism | 1 | 1 | 0 | 0/1/0 | decided: D26 | tools/build_examples.py | waits: after stage 6 (D24) |
| C77 | Waste flow: a transboundary notification for a movement inside one town; no weighbridge statement | flow story | 19 | 3 | 1 | 1/6/12 | owner: D42 | tools/examples_scenarios.py, waste() | ready (D42 decided) |
| C78 | Carnet flow: counterfoils, time limits and the duty claim | flow story | 20 | 4 | 1 | 2/4/14 | owner: D40 | tools/examples_scenarios.py, carnet() | ready (D40 decided) |
| C79 | Mast flow: dangerous-goods data of the battery, detector and stripper consignment | flow story | 36 | 5 | 1 | 2/13/21 | owner: D36 | world/items.json, tools/build_examples.py | ready (D36 decided) |
| C80 | Mast flow: the air waybill and the ULDs | flow story | 6 | 3 | 1 | 0/1/5 | owner: D36 | tools/examples_scenarios.py, mast() | ready (D36 decided) |
| C81 | Ore flow: monthly call-off, plan "as requested", bonus and moisture | flow story | 7 | 5 | 1 | 1/0/6 | owner: D45 | tools/examples_scenarios.py, ore() | ready (D45 decided) |
| C82 | Energy flow: 2400 MWh exported to Montebrio, sold to Ferrano Energy, imported by nobody | flow story | 9 | 3 | 1 | 4/4/1 | owner: D44 | tools/examples_scenarios.py | ready (D44 decided) |
| C83 | Energy flow: isolated slips | flow story | 8 | 5 | 1 | 1/2/5 | none | tools/examples_scenarios.py, utility_statement() | ready |
| C84 | Packaging flow: isolated slips | flow story | 5 | 4 | 1 | 0/0/5 | none | tools/examples_scenarios.py, packaging() | ready |
| C85 | Air flow: the missed-flight story and the CPT order change | flow story | 13 | 8 | 1 | 2/0/11 | owner: D39 | tools/examples_scenarios.py, air() | ready (D39 decided) |
| C86 | Air flow: packing, consolidation and charges of the castings | flow story | 10 | 3 | 1 | 3/2/5 | owner: D39 | tools/examples_scenarios.py, air_consignment() | ready (D39 decided) |
| C87 | Plastics flow: barge waybill and goods data | flow story | 15 | 4 | 1 | 2/4/9 | owner: D41 | tools/examples_scenarios.py, plastics() | ready (D41 decided) |
| C88 | Plastics flow: recycled-content certificate issued by a chamber of commerce | flow story | 5 | 5 | 1 | 0/0/5 | owner: D41 | world/parties.json, world/items.json | ready (D41 decided) |
| C89 | Wood flow: slat units and isolated slips | flow story | 10 | 5 | 1 | 1/0/9 | owner: D43 | tools/examples_scenarios.py, wood() | ready (D43 decided) |
| C90 | Rail flow: container train documents | flow story | 33 | 8 | 1 | 3/6/24 | owner: D37 | tools/examples_scenarios.py, rail() | ready (D37 decided) |
| C91 | Utility statement builder: average amount, supplier consumption, subscriber data | flow story | 30 | 6 | 2 | 3/9/18 | owner: D31 | tools/examples_scenarios.py, utility_statement() | ready (D31 decided) |
| C92 | Utilities: the telecom statement and invoice | flow story | 15 | 3 | 1 | 4/5/6 | owner: D31 | tools/examples_scenarios.py, telecom_consumption() | ready (D31 decided) |
| C93 | Utilities: the household's water on account, the mandate and the levy | flow story | 13 | 5 | 1 | 2/3/8 | owner: D31 | tools/examples_scenarios.py, utilities() | ready (D31 decided) |
| C94 | Utilities: excise and estimate-correction amounts | flow story | 7 | 3 | 1 | 6/1/0 | none | tools/examples_scenarios.py, energy_tax() | ready |
| C95 | Utilities: isolated slips | flow story | 7 | 6 | 1 | 1/2/4 | owner: D31 | tools/examples_scenarios.py, utilities() | ready (D31 decided) |
| C96 | Qualification requests and responses (ESPD-like) in contest and tender | flow story | 32 | 8 | 2 | 1/11/20 | owner: D29 | tools/examples_scenarios.py, qualification_limits() | ready (D29 decided) |
| C97 | Procurement notices (contest and tender): notice types, defaults, languages, links | flow story | 31 | 14 | 2 | 0/6/25 | owner: D29 | tools/examples_scenarios.py, notice_head() | ready (D29 decided) |
| C98 | Contest: the design team, references, prizes and versions | flow story | 24 | 13 | 1 | 1/4/19 | owner: D29 | tools/examples_scenarios.py, contest_version() | ready (D29 decided) |
| C99 | Contest: the estimated contract amount of 54,000 lume | flow story | 8 | 8 | 1 | 0/0/8 | owner: D29 | tools/examples_scenarios.py, contest_project() | ready (D29 decided) |
| C100 | Road flow: isolated slips of the truck shipment | flow story | 25 | 10 | 1 | 1/6/18 | owner: D35 | tools/examples_scenarios.py, road() | ready (D35 decided) |
| C101 | Road flow: application and certificate of origin | flow story | 14 | 3 | 1 | 4/4/6 | owner: D35 | tools/examples_scenarios.py, road() | ready (D35 decided) |
| C102 | Road flow: the substituted 2026 casting | flow story | 8 | 7 | 1 | 0/1/7 | owner: D35 | tools/examples_scenarios.py, road() | ready (D35 decided) |
| C103 | Furniture flow: quotation, orders, invoice, return and credit | flow story | 27 | 9 | 1 | 0/1/26 | owner: D32 | tools/examples_scenarios.py, furniture() | ready (D32 decided) |
| C104 | Furniture flow: the replenishment and sales-reporting documents | flow story | 21 | 5 | 1 | 0/10/11 | owner: D32 | tools/examples_scenarios.py, furniture() | ready (D32 decided) |
| C105 | Furniture flow: the department's desks and installation | flow story | 10 | 3 | 1 | 0/0/10 | owner: D32 | tools/examples_scenarios.py, furniture() | ready (D32 decided) |
| C106 | Cotton flow: self-billing between ginnery and farm, and the mill's forecasts | flow story | 26 | 6 | 1 | 1/4/21 | owner: D33 | tools/examples_kit.py, self_billed() | ready (D33 decided) |
| C107 | Cotton flow: classing and phytosanitary certificates | flow story | 15 | 7 | 1 | 5/1/9 | owner: D33 | tools/examples_scenarios.py, cotton() | ready (D33 decided) |
| C108 | Cotton flow: the sea export (bill of lading, VGM, pre-arrival report) | flow story | 13 | 8 | 1 | 2/3/8 | owner: D33 | tools/examples_scenarios.py, cotton() | ready (D33 decided) |
| C109 | Cotton flow: classing results carried as the applicant's remarks | flow story | 7 | 7 | 1 | 0/0/7 | none | tools/examples_scenarios.py, cotton() | ready |
| C110 | Retail flow: catalogue request, catalogue, updates and deletion | flow story | 15 | 5 | 1 | 3/4/8 | owner: D34 | tools/examples_scenarios.py, catalogue_update_head() | ready (D34 decided) |
| C111 | Retail flow: promotion, forecast, inventory and the shop sale | flow story | 13 | 4 | 1 | 2/2/9 | owner: D34 | tools/examples_scenarios.py, retail() | ready (D34 decided) |
| C112 | Retail flow: isolated slips | flow story | 12 | 5 | 1 | 1/2/9 | owner: D34 | tools/examples_scenarios.py, retail() | ready (D34 decided) |
| C113 | Retail flow: the delivery to the store (carrier references, arrival day) | flow story | 12 | 6 | 1 | 3/2/7 | owner: D34 | tools/examples_scenarios.py, retail() | ready (D34 decided) |
| C114 | Sea flow: bill of lading and ship reports | flow story | 21 | 5 | 1 | 3/7/11 | owner: D30 | tools/examples_scenarios.py, sea_consignment() | ready (D30 decided) |
| C115 | Sea flow: isolated slips | flow story | 20 | 11 | 1 | 2/3/15 | owner: D30 | tools/examples_scenarios.py, sea() | ready (D30 decided) |
| C116 | Sea flow: factoring, statement, payment and the island's debit note | flow story | 16 | 6 | 1 | 5/4/7 | owner: D30 | tools/examples_scenarios.py, sea_with_debit() | ready (D30 decided) |
| C117 | Sea flow: business card, digital agreement and capabilities | flow story | 15 | 3 | 1 | 0/4/11 | owner: D30 | tools/examples_scenarios.py, digital_service() | ready (D30 decided) |
| C118 | Sea flow: the CIF sale, freight and insurance | flow story | 14 | 10 | 1 | 3/3/8 | owner: D30 | tools/examples_scenarios.py, sea_invoice_terms() | ready (D30 decided) |
| C119 | Tender: tendering terms copied into notices, call, award and contract | flow story | 86 | 13 | 1 | 4/40/42 | owner: D28 | tools/examples_scenarios.py, tendering_terms() | ready (D28 decided) |
| C120 | Tender: contract, catalogue and call-off (releases, despatch, credit, reminder) | flow story | 30 | 11 | 1 | 2/6/22 | owner: D28 | tools/examples_scenarios.py, tender() | ready (D28 decided) |
| C121 | Tender: the procurement project and its lots | flow story | 26 | 11 | 1 | 3/0/23 | owner: D28 | tools/examples_scenarios.py, procurement_project() | ready (D28 decided) |
| C122 | Tender: the tenders, receipt and withdrawal | flow story | 15 | 4 | 1 | 2/0/13 | owner: D28 | tools/examples_scenarios.py, tender_lines() | ready (D28 decided) |
| C123 | Tender: the installation billed but never ordered | flow story | 14 | 7 | 1 | 7/4/3 | owner: D28 | tools/examples_scenarios.py, tender() | ready (D28 decided) |
| C124 | Tender: expressions of interest, status, register extract and Valdara's qualification | flow story | 13 | 3 | 1 | 0/5/8 | owner: D28 | tools/examples_scenarios.py | ready (D28 decided) |
| C125 | Tender: procedure periods against the notices' issue dates | flow story | 10 | 9 | 1 | 5/0/5 | owner: D28 | tools/examples_scenarios.py, out_day() | ready (D28 decided) |
| C126 | Tender: the guarantee certificate | flow story | 9 | 4 | 1 | 0/3/6 | owner: D28 | tools/examples_scenarios.py | ready (D28 decided) |
| C127 | Tender: award, notifications and appeal | flow story | 7 | 3 | 1 | 1/0/6 | owner: D28 | tools/examples_scenarios.py, tender_result() | ready (D28 decided) |
| C128 | Tender: moss green ordered, grey identified | flow story | 6 | 6 | 1 | 5/1/0 | none | tools/examples_scenarios.py, tender() | ready (D28 decided) |

## Order of work

The stages stay as they were made; each now lists its causes as they stand after D1 to D27. "Ready" means no open decision, no open point that blocks it and no conflict; a cause that is ready in part names, in its State line, the findings that wait and what for. The lists "Ready to fix now", "Waits for a flow decision" and "Waits for an open point" follow the stages; every finding is in exactly one of them or in the signatures stage, the numbering after stage 6, or the points the decisions leave open.

### Stage 1: Fixes that need no decision and no story change

Encoding in shared builders and simple master-data corrections that the merge decisions or the reviews settle. They touch many files and remove most of the noise, so later stages are reviewed against a cleaner set.

Causes (44, 1414 findings): C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C44.

- Ready to fix now (34 causes, 969 findings): C02, C03, C04, C05, C06, C07, C08, C10, C15, C16, C17, C18, C19, C20, C21, C23, C24, C25, C27, C28, C29, C31, C32, C33, C34, C35, C36, C37, C38, C40, C41, C42, C43, C44.
- Ready in part (8 causes; 110 of their 160 findings ready): C11 (22 of 34; 10 for D28, 2 for D30); C12 (31 of 32; 1 for D42); C13 (2 of 28; 26 for the signatures stage); C14 (22 of 24; 1 for D32, 1 for D28); C22 (14 of 17; 3 for O20); C26 (8 of 11; 2 for D32, 1 for D30); C30 (9 of 10; 1 for D37); C39 (2 of 4; 1 for D32, 1 for D30).
- Waits (2 causes, 285 findings): C01 (245 for the owner, not settled); C09 (39 for O25, 1 for D28).

No longer ready, against the first version of this file: C01 (party master data: D11 asks for the profile per document type as a table for the owner, and D1 puts a regional `LocaleCode` into every party description that has a `Language`, so whether `Language` stays in each profile is open) and C09 (the bench emission: D10 puts its arithmetic right in one change with the split of the footprint, C47, which waits for O25). Parts of C11, C12, C13, C14, C22, C26, C30 and C39 wait, as listed above: mostly findings on the three buyer-issued debit notes (D9, O6), on the tender's currencies (O50), on signature identifiers (D6) and on item data (O20).

Order inside the stage: C40 is done with C69 (stage 4); the previous declaration of sea/11 (C12) takes its value from the ledger of C71; dropping a contact altogether (C02) follows C01.

Stage 1 now has 1,079 of its 1414 findings ready to fix.

### Stage 2: World rules decided in D1 to D27, then their implementation

Geography, calendar, payment terms, customs, tax and language rules. All are decided except C49 (D6, deferred to the signatures stage); the earlier decisions and world-story sentences they contradicted are revised (`analysis/codelist-decisions.md`, "Revisions of 2026-11-16"; `note/src/03-world.md`).

Causes (15, 647 findings): C45, C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56, C57, C58, C59. Decided: C45 (D1), C46 (D2), C47 (D10), C48 (D11), C50 (D15), C51 (D22), C52 (D16), C53 (D27), C54 (D17), C55 (D23), C56 (D19), C57 (D18), C58 (D19), C59 (D3); deferred: C49 (D6).

- Ready to fix now (3 causes, 393 findings): C45, C46, C59.
- Ready in part (6 causes; 58 of their 77 findings ready): C50 (22 of 29; 6 for D31, 1 for D30); C51 (9 of 12; 3 for D28); C53 (9 of 12; 3 for D28); C54 (7 of 10; 3 for D28); C55 (7 of 8; 1 for D30); C57 (4 of 6; 2 for D40).
- Waits (6 causes, 177 findings): C47 (74 for O25); C48 (41 for O20); C49 (38 for the signatures stage); C52 (12 for O46); C56 (4 for O82, 4 for D44); C58 (4 for D30).

Implement in this order: the language rules (C45, C46: they touch most files, and need the world locale list, O19), then payment (C51, C55) and tax (C50, C54), customs (C57; C52 after O46), the calendar (C53, with O78), and the geography last (C56 after O82, then C58 with the sea flow). The item rules C47 and C48 start with their proposals for the owner (O25, O20); C09 goes with C47.

### Stage 3: Master data

Party and item data in world/*.json; all decided (D4, D5, D7, D8, D9, D12, D13, D14).

Causes (9, 307 findings): C60, C61, C62, C63, C64, C65, C66, C67, C68.

- Ready to fix now (5 causes, 40 findings): C62, C63, C64, C65, C68.
- Ready in part (2 causes; 239 of their 257 findings ready): C60 (165 of 181; 8 for D28, 7 for O17, 1 for the owner, not settled); C61 (74 of 76; 2 for the owner, not settled).
- Waits (2 causes, 10 findings): C66 (3 for D28, 1 for D30, 1 for D32); C67 (5 for O27).

Order: the founding table with D14's corrections (C60, O21, O30), identification (C61, O22, O23), the store's label (C62), then the smaller ones. C66 (the debit notes) is re-homed with the furniture, sea and tender flows (O6).

### Stage 4: Cross-flow story: the goods chain

Which lots reach Lumeway and how the bench ships (D20, D21); this changes product data in several flows at once.

Causes (3, 17 findings): C69, C70, C71.

- Ready to fix now (2 causes, 11 findings): C69, C71.
- Ready in part (1 cause; 4 of its 6 findings ready): C70 (4 of 6; 2 for D39).

Order: the bench as three parcels (C69 with C40, O61), then the production record and stock ledgers (C71, O64), then melts and serials from the production record (C70). The air frames' cross-dock (O63) goes with the air flow (D39).

### Stage 5: Generator mechanisms: time, numbering, references

Issue times, document numbers, codes and references are derived by method; fix the method once.

Causes (5, 80 findings): C72, C73, C74, C75, C76.

- Ready in part (2 causes; 55 of their 65 findings ready): C72 (35 of 38; 1 for D39, 1 for D34, 1 for D30); C73 (20 of 27; 6 for D38, 1 for D34).
- Waits (3 causes, 15 findings): C74 (10 for after stage 6); C75 (2 for after stage 6, 2 for the signatures stage); C76 (1 for after stage 6).

Issue times first (C72), then references (C73). Numbering, company codes and execution identifiers (C74, C75, C76) are decided but implemented after stage 6: D24 says numbers follow the final issue times (documents that cite later ones, the sea voyage, the tender dates) and are one of the last things implemented, and the collaborations of O77 depend on which documents each flow keeps. C75's two signature prefixes wait for the signatures stage.

### Stage 6: Flow stories, smallest flows first

Each flow's remaining findings, per flow in the order waste, carnet, mast, ore, energy, packaging, air, plastics, wood, rail, utilities, contest, road, furniture, cotton, retail, sea, tender. Each flow decision starts with its open points and its goods balance (O66). Findings of other causes that wait for a flow's decision are listed with the flow.

Causes (52, 883 findings): C77, C78, C79, C80, C81, C82, C83, C84, C85, C86, C87, C88, C89, C90, C91, C92, C93, C94, C95, C96, C97, C98, C99, C100, C101, C102, C103, C104, C105, C106, C107, C108, C109, C110, C111, C112, C113, C114, C115, C116, C117, C118, C119, C120, C121, C122, C123, C124, C125, C126, C127, C128.

- waste: C77 (19 findings, D42); plus C12 (1) from other causes that wait for D42
- carnet: C78 (20 findings, D40); plus C57 (2) from other causes that wait for D40
- mast: C79, C80 (42 findings, D36)
- ore: C81 (7 findings, D45)
- energy: C82 (9 findings, D44); C83 (8 findings, ready now); plus C56 (4) from other causes that wait for D44
- packaging: C84 (5 findings, ready now)
- air: C85, C86 (23 findings, D39); plus C70 (2), C72 (1) from other causes that wait for D39
- plastics: C87, C88 (20 findings, D41)
- wood: C89 (10 findings, D43)
- rail: C90 (33 findings, D37); plus C30 (1) from other causes that wait for D37
- utilities: C91, C92, C93, C95 (65 findings, D31); C94 (7 findings, ready now); plus C50 (6) from other causes that wait for D31
- contest: C96, C97, C98, C99 (95 findings, D29)
- road: C100, C101, C102 (47 findings, D35)
- furniture: C103, C104, C105 (58 findings, D32); plus C14 (1), C26 (2), C39 (1), C66 (1) from other causes that wait for D32
- cotton: C106, C107, C108 (54 findings, D33); C109 (7 findings, ready now)
- retail: C110, C111, C112, C113 (52 findings, D34); plus C72 (1), C73 (1) from other causes that wait for D34
- sea: C114, C115, C116, C117, C118 (86 findings, D30); plus C11 (2), C26 (1), C39 (1), C50 (1), C55 (1), C58 (4), C66 (1), C72 (1) from other causes that wait for D30
- tender: C119, C120, C121, C122, C123, C124, C125, C126, C127, C128 (216 findings, D28); plus C09 (1), C11 (10), C14 (1), C51 (3), C53 (3), C54 (3), C60 (8), C66 (3) from other causes that wait for D28

### Stage 7: Build checks

No cause is only a missing check. The checks below guard causes of the earlier stages so that the errors do not come back; the decisions add several (see "Work the decisions add").

- Issue time after every actual event and every referenced document of the same flow: guards C72, C73.
- Due date − issue date = the period of the cited terms ID, and an invoice under a contract or plan carries its terms (D22, D23, O70): guards C55, C51.
- Tax arithmetic per subtotal, including document-level allowances and charges: guards C24, C94.
- Emission value = factor × base where both are given: guards C09.
- No `NoStatus`, no identity exchange rate, no pricing currency other than the price's: guards C16, C11.
- Every document reference typed; every reference to an example resolves (flow_index "-> ?"): guards C06, C73.
- `ShippingOrderID` resolves to forwarding instructions of the flow: guards C20.
- Shipment gross weight ≥ goods + equipment tare: guards C15.
- Waybill note and distribution list agree on the originals: guards C33.
- Customs offices of a declaration belong to the declaring country; national tariff only in its country: guards C12, C29.
- No customs-trader ID outside customs and cross-border documents; no share capital outside the issuer's own invoice: guards C01.
- A document is dated on a working day of its issuer (kind of party, country and state holidays), and times that cross the zone boundary carry an offset (D27, O79): guards C53.
- Document numbers rise per issuer and kind with the issue timestamp; one code per company; documents that share a `ProfileExecutionID` share the parties and refer to each other (D24, D25, D26, O77): guards C74, C75, C76.
- Coordinates against stated distances and durations at 14 km a square (D19, O60): guards C56, C58.
- New with the decisions: item physics (O62, guards C69), the goods chain (O65, guards C70, C71, C12), margins and turnover per person (O30, guards C68, C60), the HS reasoning list (O31, guards C67), Codana prefixes and no identifier repeating another (O32, O22, guards C61, C13).

### Stage 8: Signatures, a late stage of its own (D6)

Deferred by the owner on 2026-11-16: real signatures with a key pair and a certificate for each signing party, after the story fixes. Until then no Signature aggregate is removed or added. The stage holds C49 (38 findings), the signature part of C13 (26) and C75's two signature prefixes: 66 findings. What is decided then is open point O18; the write-up point on `Signature/ValidationDate` is O40.

### Ready to fix now

1,906 findings are ready to fix now.

- Whole causes (48 causes, 1,440 findings): C02, C03, C04, C05, C06, C07, C08, C10, C15, C16, C17, C18, C19, C20, C21, C23, C24, C25, C27, C28, C29, C31, C32, C33, C34, C35, C36, C37, C38, C40, C41, C42, C43, C44, C45, C46, C59, C62, C63, C64, C65, C68, C69, C71, C83, C84, C94, C109.
- Ready in part (19 causes; 466 of their 565 findings): C11, C12, C13, C14, C22, C26, C30, C39, C50, C51, C53, C54, C55, C57, C60, C61, C70, C72, C73. Each cause's State line names the findings that wait.
- Of the 1,906 ready findings, 74 are marked "yes" and are to be confirmed in bulk under D46, which is still open (see below).

### Waits for a flow decision

| Decision | Findings | Causes (findings that wait for it) |
|---|---:|---|
| D28 | 248 | C09 (1), C11 (10), C14 (1), C51 (3), C53 (3), C54 (3), C60 (8), C66 (3), C119 (86), C120 (30), C121 (26), C122 (15), C123 (14), C124 (13), C125 (10), C126 (9), C127 (7), C128 (6) |
| D29 | 95 | C96 (32), C97 (31), C98 (24), C99 (8) |
| D30 | 98 | C11 (2), C26 (1), C39 (1), C50 (1), C55 (1), C58 (4), C66 (1), C72 (1), C114 (21), C115 (20), C116 (16), C117 (15), C118 (14) |
| D31 | 71 | C50 (6), C91 (30), C92 (15), C93 (13), C95 (7) |
| D32 | 63 | C14 (1), C26 (2), C39 (1), C66 (1), C103 (27), C104 (21), C105 (10) |
| D33 | 54 | C106 (26), C107 (15), C108 (13) |
| D34 | 54 | C72 (1), C73 (1), C110 (15), C111 (13), C112 (12), C113 (12) |
| D35 | 47 | C100 (25), C101 (14), C102 (8) |
| D36 | 42 | C79 (36), C80 (6) |
| D37 | 34 | C30 (1), C90 (33) |
| D38 | 6 | C73 (6) |
| D39 | 26 | C70 (2), C72 (1), C85 (13), C86 (10) |
| D40 | 22 | C57 (2), C78 (20) |
| D41 | 20 | C87 (15), C88 (5) |
| D42 | 20 | C12 (1), C77 (19) |
| D43 | 10 | C89 (10) |
| D44 | 13 | C56 (4), C82 (9) |
| D45 | 7 | C81 (7) |
| **D28 to D45** | **930** | |

D46 (the bulk confirmation, still open) covers 103 findings marked "yes" in 26 causes without an owner decision: C01, C02, C03, C04, C06, C08, C11, C12, C13, C14, C15, C17, C19, C23, C24, C26, C29, C30, C31, C33, C36, C41, C70, C72, C84, C94. It confirms that they are fixed with their cause; 74 of them lie in the ready parts counted above, the other 29 in parts that wait for something else (C01 15; C11 5 and C13 5 for D28 and the signatures stage; C12 1 for D42; C30 1 for D37; C72 2 for D39 and D34).

### Waits for an open point

| Open point | Findings | Causes |
|---|---:|---|
| O17 | 7 | C60 (7) |
| O20 | 44 | C22 (3), C48 (41) |
| O25 | 113 | C09 (39), C47 (74) |
| O27 | 5 | C67 (5) |
| O46 | 12 | C52 (12) |
| O82 | 4 | C56 (4) |
| **Together** | **185** | |

O17 is taken up with C04 in stage 1; O20 and O25 are proposals for the owner; O27 and O46 are readings of an official text before the change; O82 is an owner choice about the map before the scale is implemented.

### Other waits

- Not settled by the decisions, with no D- or O-number yet (248 findings): C01 (245), C60 (1), C61 (2). The cause sections say what is open.
- Numbering after stage 6 (13 findings): C74 (10), C75 (2), C76 (1).
- Signatures stage (66 findings): C13 (26), C49 (38), C75 (2).

### How the counts are made

Findings per cause, per decision and per "yes" come from `analysis/worklist-assignments.csv` (3,348 rows, one per finding, 128 causes; the count per cause equals the column Findings of the summary table). A split inside a cause comes from the titles of its findings in `.review/worklist/findings.csv` (written by `list_findings.py`), read against the decisions and the open points; each split names its findings in the cause's State line. Every finding is counted once: 1,906 ready + 930 flow decisions + 185 open points + 248 not settled + 13 after stage 6 + 66 signatures stage = 3,348.

Dependencies across stages: C56 waits for O82 and blocks C58, which goes with the sea flow (O53, D30); the map rendering on the site uses the same tiles; C09 with C47 (D10, O25); C22's specification findings with C48 (O20); C40 with C69 (D20); C70 after C71 (D21); C12 (sea/11 previous declaration) with C71; C85 with C72 (order of cancellation and replacement); C118 with C52 (D16, O46); C123 with C51 (D22, O69) and C54 (D17); C74, C75 and C76 after stage 6 (D24); the findings on the three buyer-issued debit notes with D28, D30 and D32 (O6).

## Work the decisions add

The decisions created work that no review finding asked for: the holidays and time zones in the documents, numbering styles and company codes, the bench as three parcels, item physics, the goods ledger and its check, the price chain, the handling limit, the map scale and the world's new position, founding dates, and the build checks that guard them. The rows below are the open points of the groups "To work out when a decision is implemented" and "For the build checks" of the register in `analysis/worklist-decisions.md` ("Open points"), which has the full text; O57 of the first group is settled (D27) and not listed.

| Open point | Work | From | Stage | Causes |
|---|---|---|---|---|
| O19 | The world locale list (three codes and what marks each variety); whether a party whose first language is Urvanian or Lisavan states its English locale; the note paragraph | D1 | 2 | C45 |
| O20 | The profile per document type of what a document says about an item, as a table for the owner | D11 | 2 | C48, C22 (and C01 for parties) |
| O21 | Each party's day and month of founding; the textile mill's size | D4 | 3 | C60 |
| O22 | Codana numbers in order of registration; telephone numbers without relation to an identifier; the check that no identifier of a party repeats another | D5 | 3 (check: 7) | C61, C13 |
| O23 | Identifiers for the items that carry world item numbers today; GTINs for the Elderwick bench and chair from Brightmarket's prefix; Lumeway named as the issuer of its GTIN | D5, D7 | 3 | C61, C62 |
| O24 | Site codes for Urvanian places and returnable items on the Codana side, only where a document needs one | D5 | 3 | C10, C23 |
| O25 | The two figures of the bench's footprint and the same split for other items; the bench's steel and wood consumption | D10, D20 | 2 | C47, C09 |
| O26 | Cotton: bale count, per-bale weights and totals agree | D12 | 3 | C65, C108 |
| O46 | Read the WTO Valuation Agreement (Articles 1 and 8); bring each delivery term to each country's basis | D16 | 2 | C52, C118 |
| O47 | The withholding scheme's name; the tax representative's registration; the new text of `SVCABROAD` | D17 | 2 | C54 |
| O49 | The import declaration's elements for the preference claim, the proof of origin and the tax due; the Accord's preference criteria; Urvania's import VAT; the carnet's amount | D18 | 2 | C57, C12, C78 |
| O55 | The world's position: chart and claims checks, the origin and degrees per square in `world/countries.json`, no coordinate on real land | D19 | 2 | C56 |
| O56 | The island's map (cliffs west, port, airport and town east, the route round a cape) and the inset on the site's map | D19 | 2 | C56 |
| O58 | The freighter's range against the ATR 72-600F data the world holds | D19 | 6 (air) | C86 |
| O61 | The bench as three parcels in the 49 documents: package levels, parcel counts, handling instructions, shipping marks, pallet size and weight | D20 | 4 | C69, C40, C15, C21 |
| O64 | The production record at Valdara and the stock ledgers of Lumeway, Brightmarket and Velumi as world data | D21 | 4 | C71, C70, C12 |
| O73 | The Accord's code and text for the utility term of 21 days; the utility invoices and their follow-ups; cotton/16 and mast/05 due dates | D23 | 2 | C55, C17 |
| O75 | Numbering: yearly volumes, exact formats, company codes in `world/parties.json`, the airline prefix and the air waybill check digit, the special cases | D24, D25 | 5 (after 6) | C74, C75 |
| O77 | The collaborations of each flow and their `ProfileExecutionID`; the build check | D26 | 5 (after 6) | C76 |
| O78 | The calendar in the documents: weekend and holiday documents, contact hours, time zone offsets, due dates on holidays, payments between countries | D27 | 2 | C53, C02, C18, C27, C72 |
| O81 | When the examples follow the decisions: remove the caveat from `note/src/03-world.md` and `CLAUDE.md`; bring world/*.json into line with the story lines | the summary of 2026-11-16 | last | all |
| O84 | Other note sources to change (`05-validation.md`, `04-rationale.md`, `02-principles.md`, the four new references) and the row "SET stays for real sets" of `analysis/codelist-decisions.md` | the note's update of 2026-11-16 (D5, D24, D7) | 2 | C61, C74, C62 |
| O27 | Read the legal notes to Section XV and Note 1(d) to Chapter 94 before the side frame becomes 9401.99 | D13 | 3 | C67 |
| O28 | The world's price type list says for each type whether it includes tax | D14 | 3 | C68, C25 |
| O29 | Confirm that Urvania works the other way round for place names | D3 | 2 | C59 |
| O60 | Check: stated distances equal the routes on the map; times fit distance and speed | D19 | 7 | C56, C58 |
| O62 | Check: item physics, one sheet per physical item (weights from dimensions and density, parts to whole, parcels to pallets to holds, the handling limit) | D20 | 7 | C69 |
| O65 | Check: the goods chain (stock never below zero, nothing leaves before it arrived or is made after it ships, previous declarations cover their lots) | D21 | 7 | C71, C70, C12 |
| O66 | The other goods chains, each balanced with its flow decision (ore, slats, timber, cotton, granulate, waste, gas, the Elderwick pieces) | D21 | 6 and 7 | C77, C81, C82, C87, C89, C103, C106, C110 |
| O70 | Check: payment terms (contract terms first, one period per terms ID, interest from the due date) | D22, D23 | 7 | C51, C55 |
| O79 | Check: the calendar (working days per kind of party and holidays, due dates on bank working days, offsets) | D27 | 7 | C53 |
| O30 | Check: nobody resells below cost plus stated freight; margins and turnover per person in their bands | D14 | 7 | C68, C60 |
| O31 | Check: a list of the world's items with the reasoning for each HS heading, verified once by a person | D13 | 7 | C67 |
| O32 | Check: the prefix of every Codana identifier is the company number of its issuer | D5 | 7 | C61 |

The rewrites of `note/src/03-world.md` and `analysis/codelist-decisions.md` that the decisions ask for (D1, D2, D3, D5, D10, D11, D13, D16 to D18, D22, D26) are not open points; they were made in commits fc87335 and 4afbded on 2026-11-16, and O81 and O84 hold what is left.

Counted and pointed to only (see the register): 23 open points to decide with a later decision (O5 to O18, O48, O50, O53, O54, O63, O69, O72, O82, O83; O1 to O4 and O45 of that group are settled); 8 for the encyclopaedia and the backstory (O33 to O36, O52, O59, O74, O80); 2 to check outside the repository (O37, O38; O68 is settled); 2 for the write-up to the OASIS UBL TC (O39, O40); 7 later enhancements (O41 to O44, O51, O67, O76). Of the first group, O17 and O82 hold up findings of this file (see "Waits for an open point") and O18 is the signatures stage. When this file was updated the register had 83 rows numbered from O1 to O84 (O71 is not used); O85 to O87 were added from this update's own report: O85 (Codana's status, with O17), O86 (the party profile that C01 waited for; settled 2026-11-16, so C01's 245 findings move from "not settled" to ready once the table of O88 is agreed, and O88 to O90 follow from it) and O87 (wording in decisions to settle with their flows).

## Causes

### C01 · Party master data copied into documents that do nothing with it
- Kind: encoding · Findings: 245 (High 0, Medium 0, Low 245) in 213 files, 17 flows · Needs decision: taken: merge decisions, rows "Party master data copied …" and "`CorporateStockAmount` holds share capital" (15 findings marked "yes" go to D46)
- What is wrong: A party is described with all its master data wherever it appears: customs-trader numbers in domestic orders and tender documents, share capital and stock listing in despatch advices, tax registrations in documents without tax, Rinova's waste permit in every plastics document, bank accounts in orders that move no money. The per-example reviews rate it Low, one finding per example. Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002` (contest/01#F4); `ore/01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch` (ore/01#F3).
- Where it comes from: `tools/build_examples.py` `place_parties()` (line 1117) writes `party(pid)` in full for every role of `world/documents.json`; `party()` (line 91) and `legal_entity()` (line 276) always add customs-trader IDs, tax schemes, share capital, listing, logo, website, service provider, permits and accounts
- What must be true afterwards: Each document carries of a party only what that document uses (identification, name and the data its definition or the transaction needs); the issuer's own share capital on its own invoice stays.
- Fix direction: Give each role a profile (short, trade, legal, tax, customs, payment) per document type, laid before the owner as a table like the item profile of D11 (O20), and let `place_parties()` choose it; build check: no customs-trader ID outside customs and cross-border documents, no share capital outside the issuer's own invoice.
- Depends on / blocks: none
- Note: The findings marked "Needs decision: yes" (mostly contest and tender: the authority's tax scheme in procurement documents) follow the same rule and are confirmed in bulk (D46).
- Touched by: D11 (the same rule for items: a later document repeats a fact only if its own transaction uses it; D11 names this cause as one of the two the "is this needed here?" check produced, and says that the profile per document type is made at implementation as a table for the owner), D1 (every party description that has a `Language` now carries `LocaleCode` `en-XU`, `en-XB` or `en-XL`), D18 (the customs trader number stays, built from the business register number, so the build check on customs-trader IDs stands), D4 and D5 (the founding date, size class and Codana number that a profile keeps change in stage 3).
- Not settled by D1 and D11: whether `Language`, with its new `LocaleCode`, stays in every party description or only where the document uses it; whether the party profile goes to the owner as a table before it is applied, as D11 asks for items (O20 names items only).
- State: decided 2026-11-16 (O86, see the story line "What a document says about a party"): each party is the authority on its own data, every document stands on its own, the answer completes the picture. Ready to fix once the party table of O88 has been shown to the owner; the direction above changes in one respect: a follow-on document is not cut down to name and number, the sender still describes itself in full for that kind of document.
- Fixed (2026-11-17, stage 1, after the owner approved the party table O88): every party is written with the profile of its part in the document: the sender about itself, the receiver as the sender knows it, a third party as the receiver needs it, per kind of document (`DOC_CLASS`, `PROFILE`, `THIRD`, `party_profile()` in `tools/build_examples.py`; the table and its seven special rules in `analysis/party-profile.md`). Share capital only on an Urvanian SUA's own invoice-kind documents (O147). Build checks: customs trader numbers, share capital, and O90 (never contradicting what a party says about itself). The examples go from 79,130 to 58,106 elements; coverage 4996 → 4993 (O145).
- Findings: air (1): 10#F12; carnet (2): 01#F10, 04#F6; contest (29): 01#F3, 01#F4, 02#F4, 02#F5, 03#F4 …; cotton (15): 01#F3, 02#F4, 03#F8, 04#F15, 05#F17 …; energy (7): 01#F6, 03#F4, 05#F10, 06#F4, 07#F7 …; furniture (17): 01#F6, 02#F6, 03#F6, 04#F5, 05#F5 …; ore (8): 01#F3, 02#F8, 03#F13, 04#F5, 05#F9 …; packaging (10): 01#F3, 01#F7, 02#F6, 03#F3, 04#F4 …; plastics (21): 01#F5, 01#F8, 02#F5, 02#F7, 03#F9 …; rail (8): 01#F7, 02#F10, 03#F12, 06#F23, 08#F27 …; retail (23): 01#F6, 02#F10, 02#F18, 03#F7, 04#F10 …; road (17): 01#F8, 02#F8, 03#F10, 04#F11, 05#F10 …; sea (27): 01#F7, 02#F13, 02#F17, 04#F8, 07#F6 …; tender (32): 01#F16, 02#F19, 03#F19, 04#F8, 05#F6 …; utilities (12): 01#F10, 02#F9, 03#F12, 04#F6, 05#F6 …; waste (6): 01#F8, 01#F11, 02#F12, 02#F15, 03#F8 …; wood (10): 01#F5, 02#F9, 03#F5, 04#F11, 04#F13 …. Full list in `analysis/worklist-assignments.csv`.

### C02 · One contact template per kind of party, whatever the role
- Kind: master data · Findings: 226 (High 1, Medium 0, Low 225) in 213 files, 18 flows · Needs decision: taken: merge decisions, row "Contacts whose name, job title and department contradict …" (1 finding marked "yes" goes to D46)
- What is wrong: Every company desk is a "Customer service officer" in "Sales", carriers' desks "Operations planner", public bodies "Public service officer"; the same desk appears whether the party sells, buys, pays or receives goods (contacts of Valdara's "Order desk" on ore, gas and slat purchases). Name, job title and department often contradict each other. Example: `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office` (furniture/01#F5); `contest/03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry` (contest/03#F9).
- Where it comes from: `world/parties.json` `identity.contacts` (name, `job_title`, `department`, `hours`), written by `tools/build_examples.py` `party()` (lines 199–202) into every role
- What must be true afterwards: Each contact fits the party's role in the document (buying, accounts, goods-in, customs), and name, job title and department agree.
- Fix direction: Give parties.json contacts per function (sales, purchasing, accounts, goods-in, customs) and let the role pick the contact (in `place_parties()` / `party()`), or drop the contact where the document does not need one.
- Depends on / blocks: none
- Note: Contact hours that exclude the time of an event are under C53.
- Touched by: D27 (working days per kind of party: offices and factories Monday to Friday, shops Monday to Saturday, ports, carriers, terminals, border customs and the operations of utilities every day; their contacts say so; O78), D11 (D11 names this cause next to C01: where a contact is dropped because the document does not need one, that follows the C01 profile).
- State: ready to fix now for contacts per function and their hours; dropping a contact altogether follows C01.
- Fixed in part (2026-11-17, stage 1 step 1a): every party's main contact now has a name, job title and department that agree, and a party has desks by function in `world/parties.json` (`identity.desks`); the role it plays picks the desk (`desk_for()` in `tools/build_examples.py`: seller → sales, buyer → purchasing, accounting supplier → accounts receivable, accounting customer → accounts payable, delivery party and consignee → goods-in, despatch party and consignor → dispatch, exporter, importer and declarant → customs, transport user → transport planning, tenderers → bids; customs services by export, import and transit, chambers by certificates and carnets); a world check guards the desk data. Still open: dropping a contact altogether (with C01, after O88); contact hours per kind of party (D27, O78, stage 2).
- Findings: air (11): 01#F12, 02#F10, 03#F16, 04#F19, 05#F10 …; carnet (2): 01#F13, 03#F10; contest (12): 03#F9, 04#F9, 05#F9, 06#F10, 07#F7 …; cotton (20): 01#F5, 02#F6, 03#F7, 04#F17, 05#F19 …; energy (8): 01#F7, 02#F4, 03#F3, 04#F10, 05#F7 …; furniture (15): 01#F5, 02#F5, 03#F5, 04#F4, 05#F4 …; mast (7): 01#F9, 02#F10, 03#F11, 03#F12, 04#F8 …; ore (8): 01#F2, 02#F7, 03#F12, 04#F4, 05#F8 …; packaging (10): 01#F4, 02#F4, 03#F5, 04#F6, 05#F4 …; plastics (11): 01#F4, 02#F4, 03#F8, 04#F11, 05#F7 …; rail (9): 01#F8, 02#F11, 03#F13, 06#F20, 06#F21 …; retail (22): 01#F5, 02#F11, 03#F8, 04#F11, 05#F9 …; road (17): 01#F7, 02#F7, 03#F6, 04#F9, 05#F9 …; sea (32): 01#F10, 02#F15, 02#F19, 03#F11, 04#F9 …; tender (18): 02#F30, 03#F30, 03#F31, 13#F17, 14#F14 …; utilities (10): 01#F11, 02#F10, 03#F13, 04#F7, 05#F7 …; waste (3): 01#F9, 02#F13, 03#F7; wood (11): 01#F6, 02#F10, 03#F6, 04#F7, 05#F6 …. Full list in `analysis/worklist-assignments.csv`.

### C03 · Urvanian province written into `Region`
- Kind: master data · Findings: 111 (High 0, Medium 104, Low 7) in 111 files, 15 flows · Needs decision: taken: merge decisions, row "Province … in `Region`" (4 findings marked "yes" go to D46)
- What is wrong: The province ("Province of Ferrano") of every Urvanian address is in `Region`, which UBL defines as a region "of a country" in the sense of an informal area; a province is a country subdivision (`CountrySubentity`). The value is master data and is copied into every full party description. The same element holds the cotton farm's "North coast" origin area in cotton/02 and 07. Example: `tender/03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano` (tender/03#F7); `contest/15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano` (contest/15#F5).
- Where it comes from: `world/parties.json` `identity.address.Region` of the 14 Urvanian parties (e.g. line 37) and `world/countries.json` `region` (line 96); `tools/build_examples.py` `address()` (field order at line 472)
- What must be true afterwards: No address of an Urvanian party carries the province in `Region`; it is in `CountrySubentity` (with a code if the world has one).
- Fix direction: Move the field in parties.json (and the Urvanian address format in countries.json) from `Region` to `CountrySubentity`; the cotton origin area goes to the element the farm address already uses (`District`). A build check that `Region` is not used for a country subdivision would guard it.
- Depends on / blocks: none
- Touched by: none of D1 to D27 (D2 changes the language tag of the same address's English renderings, not its fields).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1a): the Urvanian province is in `CountrySubentity` (`world/parties.json`, Urvania's address format and `province` in `world/countries.json`); the cotton's origin area is a `District` (`origin_district` in `world/items.json`); the world check rejects `Region` in a party's address. `Address/Region` lost its only example: O140.
- Findings: carnet (4): 01#F4, 02#F2, 03#F3, 04#F2; contest (2): 15#F5, 16#F4; cotton (7): 02#F10, 07#F10, 08#F15, 10#F11, 11#F12 …; energy (9): 01#F3, 02#F3, 03#F2, 04#F6, 05#F2 …; ore (8): 01#F1, 02#F3, 03#F7, 04#F2, 05#F5 …; packaging (2): 01#F1, 02#F2; plastics (11): 01#F2, 02#F1, 03#F2, 04#F3, 05#F1 …; rail (11): 01#F4, 02#F4, 03#F5, 04#F1, 05#F3 …; retail (1): 02#F6; road (17): 01#F4, 02#F1, 03#F3, 04#F3, 05#F3 …; sea (1): 02#F8; tender (22): 03#F7, 12#F3, 13#F5, 14#F5, 15#F2 …; utilities (4): 01#F7, 02#F6, 03#F9, 04#F1; waste (3): 01#F3, 02#F6, 03#F3; wood (9): 01#F2, 02#F3, 03#F1, 04#F3, 05#F2 …. Full list in `analysis/worklist-assignments.csv`.

### C04 · Public bodies described as companies in a commercial register
- Kind: encoding · Findings: 88 (High 0, Medium 77, Low 11) in 83 files, 13 flows · Needs decision: taken: merge decisions, row "Public bodies … as companies" (16 findings marked "yes" go to D46)
- What is wrong: Customs services, the public works department, the chambers, the review board, the Trade Accord Council and the maritime administration get a commercial-register entry with a liquidation status, because `legal_entity()` writes both for every party that is not a person. The world list has no register type for public bodies. Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL` (contest/01#F2); `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE` (tender/01#F6).
- Where it comes from: `tools/build_examples.py` `legal_entity()`: `CompanyLiquidationStatusCode` "ACTIVE" for every non-person (line 297) and `CorporateRegistrationTypeCode` "COMMERCIAL" for every register (line 315); `world/parties.json` `kind: "public"`
- What must be true afterwards: No public body carries `CorporateRegistrationTypeCode` COMMERCIAL or `CompanyLiquidationStatusCode`; companies keep them.
- Fix direction: In `legal_entity()`, skip the commercial-register scheme and the liquidation status for parties of kind "public" (and give them their legal basis instead, if a document needs one). Small related slips: the Port of Selanu as a separately registered head office (air/09#F3: Selanu Airport Cargo is a branch of the port company, D25); the farm keeps its yearly registration (D4, see C63).
- Depends on / blocks: none
- Touched by: O17 (from D4: whether the two ports and Selanu Telecom are companies with a register entry or public bodies; the register says it is taken up with this cause in stage 1), D4 (the cotton farm's registration keeps its yearly expiry as a rule of Lisavu's farm register), D25 (Selanu Airport Cargo is a branch of the port company and numbers in the port's series), D5 (Codana is "a public body, set up by the state").
- Not settled by D4 and D5: Codana is a public body in D5, but the founding table of D4 gives it a founding year, a headcount, a turnover and the size SMALL like a company; which register type the farm's entry names (sea/29#F12 objects to the commercial register) is not said by D4.
- State: ready to fix now; O17 is put to the owner when the cause is worked. No finding of this cause depends on it.
- Fixed in part (2026-11-17, stage 1 step 1b): public bodies (customs services, chambers, the Trade Accord Council, the review board, the public works department, the information service, the maritime administration and Codana, which D46 makes a public body and whose company figures go) carry no commercial register scheme, no `CompanyLiquidationStatusCode`, no size class and no `CompanyID`; the ports of Lumeport and Selanu are state-owned companies (`kind` company), as Selanu Telecom already was; the cotton farm names Lisavu's farm register with type `FARM`; Selanu Airport Cargo no longer names the port as its head office (air/09#F3). Still open: the identifier of a public body and the farm register's numbers (O142). `PartyLegalEntity/HeadOfficeParty` lost its only example: O143.
- Findings: air (1): 09#F3; carnet (8): 01#F6, 01#F11, 02#F3, 02#F6, 03#F4 …; contest (16): 01#F2, 02#F2, 03#F3, 04#F2, 05#F2 …; cotton (3): 10#F14, 11#F2, 15#F2; energy (2): 04#F7, 05#F4; furniture (3): 15#F1, 16#F2, 17#F2; plastics (2): 05#F4, 09#F1; rail (1): 06#F4; road (4): 05#F8, 06#F14, 07#F15, 10#F4; sea (8): 03#F4, 04#F2, 11#F11, 15#F6, 16#F5 …; tender (36): 01#F6, 02#F7, 03#F8, 04#F3, 05#F3 …; waste (2): 01#F10, 02#F14; wood (2): 05#F4, 07#F3. Full list in `analysis/worklist-assignments.csv`.

### C05 · Lumeway's "Gate 3" in its postal address
- Kind: master data · Findings: 76 (High 0, Medium 76, Low 0) in 76 files, 5 flows · Needs decision: taken: merge decisions, row "`AdditionalStreetName` = "Gate 3""
- What is wrong: Lumeway's postal address carries a vehicle gate as additional street name, so every full description of Lumeway (76 files, 5 flows) gives a gate where the post should go. A gate belongs in a delivery or pick-up location. Example: `retail/01-CatalogueRequest.xml:/CatalogueRequest/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (retail/01#F4); `sea/01-BusinessCard.xml:/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (sea/01#F2).
- Where it comes from: `world/parties.json` Lumeway Distribution (6-xb) `identity.address.AdditionalStreetName` = "Gate 3" (line 898)
- What must be true afterwards: Lumeway's postal address has no gate; where a document needs the gate, it is in a delivery location (with the GLN the flow already uses for the siding or goods-in).
- Fix direction: Drop the line from parties.json; add the gate to the delivery locations that need it (road/01 names gates and docks inconsistently, C100).
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1a): no gate in Lumeway's postal address; the road order delivers to Lumeway's goods-in location (GLN 9520610900039, "Goods-in, dock 4 of the distribution centre, entered by gate 3 of Marrowdale Business Park"), the alternative location is dock 6 of the same goods-in, and the waybill's delivery instructions name gate 3 and dock 4. `Address/AdditionalStreetName` lost its only example: O141.
- Findings: air (8): 01#F4, 02#F3, 03#F8, 04#F9, 06#F5 …; rail (6): 01#F3, 02#F6, 03#F9, 06#F11, 08#F14 …; retail (20): 01#F4, 02#F4, 03#F5, 04#F4, 05#F4 …; road (17): 01#F3, 02#F3, 03#F2, 04#F5, 05#F7 …; sea (25): 01#F2, 02#F4, 03#F5, 04#F3, 05#F4 …. Full list in `analysis/worklist-assignments.csv`.

### C06 · References that give only an ID
- Kind: encoding · Findings: 59 (High 0, Medium 0, Low 59) in 59 files, 13 flows · Needs decision: taken: merge decisions, row "References with only an ID and no document type" (2 findings marked "yes" go to D46)
- What is wrong: Additional and line document references carry only an `ID`, so the receiver cannot tell what kind of document is meant (waybills, orders, data sheets, minutes, contracts), in 13 flows. Example: `sea/01-BusinessCard.xml:/BusinessCard/cac:AdditionalDocumentReference/cbc:ID` = `LD-REG-XB` (sea/01#F11); `tender/22-AwardedNotification.xml:/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID` = `PWD-EVAL-REPORT-26` (tender/22#F12).
- Where it comes from: `tools/examples_scenarios.py` `ref()` (line 2303) and `full_reference()` (line 4838); inline `DocumentReference` blocks in the kit (e.g. `examples_kit.py` line 443) and scenarios
- What must be true afterwards: Every reference to a document that is not typed by its element names its kind (`DocumentTypeCode` or `DocumentType`), and, where it is an example of the flow, resolves to it.
- Fix direction: Let the reference helper always add the type; build check: every `AdditionalDocumentReference`/`DocumentReference` has a type.
- Depends on / blocks: none
- Touched by: D24 and D25 (the numbers that references carry change in stage 5; the type a reference names does not), D38 (still open: which cited documents are added to the flows).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1c): every reference in a generic or role-only element (`AdditionalDocumentReference`, `DocumentReference`, supporting, evidence, originator, parent, previous, original, required, provided, requested, shipment) carries `DocumentTypeCode` or `DocumentType`: the UBL document type of the example it points to (from an index of all examples), or the kind of a document outside the examples from the new table `cited` in `world/documents.json` (UN/EDIFACT 1001 where an exact code exists, else in words; decision Q29). The build fails on an untyped reference. References inside signatures wait for the signatures stage. The two status reports no longer cite a consignment number as a document. Resolving a reference to the right example is C73 (stage 5). Coverage: O145.
- Findings: air: 02#F5, 07#F8; carnet: 01#F21, 02#F8, 03#F11, 04#F12; cotton: 03#F4, 05#F11; ore: 02#F9, 03#F14, 05#F10; plastics: 05#F15, 06#F18, 07#F6, 09#F11; rail: 06#F16, 10#F7; retail: 01#F8; road: 02#F9, 05#F16, 06#F21, 07#F22, 09#F13, 14#F6, 16#F10; sea: 01#F11, 03#F17, 09#F9, 10#F11, 11#F17, 12#F8, 14#F17, 15#F11, 16#F23, 18#F5, 19#F12, 21#F10, 25#F12; tender: 01#F15, 15#F13, 17#F18, 19#F17, 20#F12, 21#F26, 22#F12, 23#F11, 24#F11, 27#F12, 29#F13, 30#F16, 33#F17, 36#F7; utilities: 04#F4, 07#F5, 08#F15, 14#F4; waste: 01#F15, 02#F9; wood: 05#F16

### C07 · The department's party tax exemption reason is worded as a transaction
- Kind: master data · Findings: 52 (High 0, Medium 0, Low 52) in 52 files, 2 flows · Needs decision: taken: merge decisions, row "Party tax exemption reason worded as a transaction" (in the parties review's Known table)
- What is wrong: The department's `PartyTaxScheme/ExemptionReason` says "Sale to a public body", which describes a transaction, not the party's status, in every document that describes the department (55 in contest, furniture, tender and utilities, as the parties review counts). Example: `tender/06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC` (tender/06#F11); `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC` (contest/01#F5).
- Where it comes from: `world/parties.json` Lumeport Public Works Department `tax_exemption_kind` = "Sale to a public body" (line 1163); the text comes from `world/countries.json` (line 249) via `tools/examples_kit.py` `tax_category()` (line 105)
- What must be true afterwards: The party-level exemption reason describes why the party is exempt ("Public body exempt from sales tax"), and the transaction wording stays in the tax categories of lines.
- Fix direction: Give the exemption list a party-status wording, or a separate party text in parties.json.
- Depends on / blocks: none
- Touched by: D17 (a Bayvarran seller invoices the department with the Bayvarran exemption for public bodies `PUBLIC`; the party-level wording is still to be fixed).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1a): code `PUBLIC` of Bayvarra's exemption list is named "Public body" (the party's status; its definition already said so), and the department's text is "Public body: buys free of the state sales tax"; the lines of a sale keep the code, which now reads as the buyer's status there too.
- Findings: contest: 01#F5, 02#F6, 03#F6, 04#F6, 05#F6, 06#F8, 07#F11, 08#F7, 09#F6, 10#F6, 11#F12, 12#F8, 13#F6, 14#F7, 15#F11, 16#F10; tender: 01#F17, 02#F20, 03#F20, 04#F9, 05#F8, 06#F11, 07#F9, 08#F4, 09#F7, 10#F8, 11#F6, 12#F9, 13#F18, 14#F15, 15#F9, 16#F8, 17#F9, 18#F7, 19#F9, 20#F9, 21#F22, 22#F9, 23#F9, 24#F15, 25#F15, 26#F16, 27#F13, 28#F8, 29#F20, 30#F15, 31#F9, 32#F23, 33#F23, 34#F15, 35#F14, 36#F11

### C08 · Party roles that repeat another role or do not fit their definition
- Kind: encoding · Findings: 41 (High 0, Medium 7, Low 34) in 39 files, 12 flows · Needs decision: none (6 findings marked "yes" go to D46)
- What is wrong: Roles are filled with the party that already holds another role in the same document: `CustomerParty` equal to the receiver in utility statements (whose definition is "the buyer, if different from the receiver"), the importer as its own notifier, the contracting party in eight further roles of the tender notices, originator and beneficiary on every line; and the rail carrier and the mast forwarder as `FreightForwarderParty`, which UBL defines as a consolidator. Example: `tender/15-Tender.xml:/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department` (tender/15#F10); `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores` (furniture/01#F3).
- Where it comes from: `world/documents.json` `parties` maps (e.g. CustomerParty next to ReceiverParty, notifier = importer), placed by `tools/build_examples.py` `place_parties()` (line 1117); originator/beneficiary blocks in `tools/examples_scenarios.py` (lines 5275, 5293, 6487)
- What must be true afterwards: A role appears only where it adds a party or information the document needs; party roles fit their UBL definition.
- Fix direction: Remove the redundant roles from documents.json; build check: no role whose definition says "if different" equals the role it is compared with.
- Depends on / blocks: none
- Note: The findings marked "yes" (forwarder role, consignor notified of its own goods) are confirmed in bulk (D46).
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1g): a party role that only names a party the document already gives in a role that covers it is left out (`redundant_roles()` in `tools/build_examples.py`): originator and beneficiary equal to the buyer, contracting party or accounting customer, at the header and on lines; the customer equal to the receiver in the utility statements; the importer as its own notifier; the sender as source issuer; the contracted carrier as performing carrier (with its assigned ID) and the consignment's carrier as freight forwarder; the contracting party repeated in the tendering roles (a role with a contact of its own stays); a line's contract parties, manufacturer or performing party equal to the header's or the line's above; a distribution copy to the addressee (the receiver, or the forwarder of forwarding instructions). The order's originator and beneficiary are dropped from the fulfilment cancellation, the factor's statement and the remittance advice. The city's levy on the water credit note names the city as `CollectedForParty`, as the invoice does. The six findings for D46 (cotton/03#F10, 04#F4, mast/02#F11, #F15, mast/03#F16, #F17) go with the flow stories of stage 6.
- Findings: air: 03#F12, 07#F14; cotton: 03#F10, 04#F4, 09#F14; energy: 01#F2; furniture: 01#F3, 02#F7, 11#F5, 12#F4, 16#F9; mast: 02#F11, 02#F15, 03#F16, 03#F17; plastics: 09#F12; rail: 05#F9, 06#F3, 08#F23; retail: 02#F12, 03#F10, 04#F13; sea: 05#F15, 25#F8, 27#F6; tender: 01#F18, 02#F21, 03#F21, 09#F9, 15#F10, 17#F10, 19#F10, 21#F23, 31#F12, 33#F19; utilities: 01#F4, 05#F2, 08#F3, 09#F10, 12#F5; wood: 07#F9

### C09 · Bench emission: 96 kg with factor 0.82 per 1 EA
- Kind: master data · Findings: 40 (High 40, Medium 0, Low 0) in 40 files, 6 flows · Needs decision: taken: merge decisions, row "Bench emission triple"
- What is wrong: Every full description of the bench (40 files, 6 flows) states 96 kg CO2e with `ValueFactorNumeric` 0.82 and `ValueBaseMeasure` 1 EA, and 0.82 × 1 is not 96. The figure is a product footprint from the manufacturer's LCA, not a calculation from an activity. Example: `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96` (rail/01#F1); `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96` (road/01#F1).
- Where it comes from: `world/items.json` bench `emission` (factor "0.82", line 219, base 1 EA); written by `tools/build_examples.py` `item()` (line 1089)
- What must be true afterwards: Either no factor and base, or a factor and base whose product is the stated value.
- Fix direction: Drop factor and base from items.json (preferred in all 40 findings), in the same change as the split of the footprint by lifecycle stage (C47, D10); a build check that value = factor × base where both are given. tender/35#F2 (interest factor) is in this cause because it is the same element misuse on a reminder line.
- Depends on / blocks: with C47 (D10)
- Touched by: D10 (the bench's footprint becomes two emissions, `SOURCING` and `MANUFACTURING`, that add up to the total, and D10 says the factor arithmetic is put right at the same time), D11 (the footprint is a fact of the item type: it stays in the catalogue and the product information and leaves the documents whose transaction does not use it, so fewer than 40 files will carry it).
- State: waits: 39 findings for O25 (the two figures of the footprint, proposed from typical shares, for the owner to confirm), with C47; tender/35#F2 (the interest factor on the reminder) for D28 (O69: from which day interest runs).
- Findings: carnet: 01#F3; rail: 01#F1, 06#F2, 11#F1; retail: 02#F1, 04#F2, 05#F2, 07#F1, 08#F1, 12#F1, 17#F1, 18#F1, 19#F1, 21#F1; road: 01#F1, 04#F2, 05#F2, 06#F2, 07#F2, 10#F2, 11#F1, 13#F1, 15#F1; sea: 02#F2, 05#F2, 10#F2, 11#F2, 19#F1, 20#F1, 21#F1, 22#F4, 29#F1; tender: 25#F2, 26#F2, 29#F2, 30#F2, 31#F2, 32#F7, 33#F4, 35#F2

### C10 · Locations named after companies or their office addresses
- Kind: encoding · Findings: 36 (High 1, Medium 4, Low 31) in 29 files, 11 flows · Needs decision: none
- What is wrong: From/to locations, issue, status and notification locations are a company's name and business address instead of the place (quay, siding, airport, warehouse), so the barge "starts" at the carrier's office and the ore train runs between head offices. Example: `ore/05-Waybill.xml:/Waybill/cac:IssueLocation/cbc:Name` = `Serravona Mining` (ore/05#F7); `plastics/03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Rivermouth Packaging` (plastics/03#F10).
- Where it comes from: `tools/examples_kit.py` `leg_places()` (line 624) and `address_of()` (line 631) build transport locations from the parties' postal addresses; issue and status locations in `event()` (line 1273) and the scenarios
- What must be true afterwards: Transport and event locations name the place where the thing happens, with its identifier (UN/LOCODE, GLN) where the world has one.
- Fix direction: Derive locations from map.json places (or the parties' sites/GLNs) instead of postal addresses.
- Depends on / blocks: none
- Touched by: D19 (positions follow the map at 14 km a square; O82 may redraw towns, ports and airports), D21 (the urgent air frames pass through Lumeway's dispatch area, a place of its own), D5 (site codes for Urvanian places only where a document uses one, O24).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): each transport leg in `world/documents.json` names the place at both ends (`from_place`, `to_place`: the warehouse, siding, quay, goods-in, port or airport, with its GLN or UN/LOCODE-form code where the world has one), and the transport locations, the waybill's place of issue and the plans' notification place are built from them (`kit.leg_location()`), not from the company's name and office address; a status report's location is the place of the event it reports. The barge leg stays on Fiumella's tile until the map is redrawn with Rinova on the river (O92), its place named Rinova's quay as D41 says.
- Findings: air: 04#F15, 05#F5, 09#F10; mast: 03#F10; ore: 02#F6, 03#F8, 03#F10, 05#F7; plastics: 03#F1, 03#F10, 04#F14, 04#F18, 06#F15, 06#F17; rail: 02#F14, 03#F6, 03#F16, 04#F8, 05#F10, 07#F9, 08#F9, 08#F20; retail: 06#F12, 08#F11, 11#F4, 13#F8, 21#F11; road: 03#F8, 08#F10, 08#F20, 09#F6; sea: 29#F8; tender: 02#F31, 03#F32; utilities: 02#F11; wood: 04#F12

### C11 · Currencies and exchange rates with nothing to convert, or the wrong currency
- Kind: encoding · Findings: 34 (High 7, Medium 7, Low 20) in 25 files, 7 flows · Needs decision: taken: merge decisions, row "Exchange rates with nothing to convert …" (7 findings marked "yes" go to D46)
- What is wrong: Pricing, payment, tax and alternative currencies are written where nothing is converted (identity rates, rates in waybills and forwarding instructions), or name a currency the amounts are not in: the pricing currency is lume while every price is in coral (cotton/04, 05) or ferra while the price is in lume (tender/26, 32, 33). Example: `energy/06-Invoice.xml:/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.` (energy/06#F1); `cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:TaxCurrencyCode` = `XLC` (cotton/04#F7).
- Where it comes from: `tools/examples_kit.py` `price_block()` (line 329, `PricingExchangeRate`), `rate()` (line 817), `currency_line()` (line 278); `tools/examples_scenarios.py` `PRICING_RATE` (lines 2418, 2453) and the forward contract in the tender call-off
- What must be true afterwards: Every currency code and exchange rate converts an amount the document states in that currency; no rate from a currency to itself.
- Fix direction: Drop the elements where nothing is converted (preferred in every finding); build check: a `PricingCurrencyCode` equals the currency of the prices, a rate's source ≠ target.
- Depends on / blocks: none
- Note: Possibly not a problem for cotton/04#F1 and 05#F1: `note/src/03-world.md` says "seed cotton is priced from the trade accord's lint reference price, published in lume", so a lume pricing currency may be intended; then the conversion must be shown, not dropped.
- Touched by: "Story lines: Money" (open point O2, settled: through 2026 every exchange rate is the parity; a spot conversion at the parity is not chosen; the forward contract of the tender flow becomes Valdara's hedge across the review of 1 January 2027, and how the documents carry it is O50, with D28), D9 (sea/28 is not a debit note and is re-homed with the sea flow, O6). The Note on cotton/04 and 05 stands: the lint reference price is published in lume ("Story lines", 1974).
- State: ready in part: 22 findings ready; the 10 tender findings on the pricing currency, the pricing rate and the forward contract (tender/26#F1, 26#F6, 26#F13, 27#F8, 28#F7, 32#F6, 32#F9, 32#F14, 33#F3, 33#F14) wait for D28 (O50); sea/28#F4 and 28#F10 wait for D30 (O6).
- Fixed (2026-11-17, stage 1 step 1e): one rule in the build (`currency_cleanup()` in `tools/build_examples.py`): no currency code equal to the document currency (with its exchange rate), no rate from a currency to itself, no pricing currency the prices are not in, no alternative payment currency without an alternative amount, no free-standing exchange rate in a transport document, statement, remittance advice, status response or utility statement when no amount is in the other currency. The gas invoices state the contract price in ferra without a conversion from lume (energy/06, 07); no forward contract in a tender document (D28, O50); cotton's lume reference price is the story's (D33, O116), not a pricing currency for coral prices. Still to come with the tender flow (D28): the tender documents' pricing in ferra, which D28 moves to lume. Coverage: O145 (42 elements).
- Findings: air: 03#F11, 04#F12; cotton: 04#F1, 04#F7, 04#F8, 05#F1, 05#F8, 08#F3, 09#F13, 13#F8; energy: 06#F1, 07#F2; road: 15#F2; sea: 09#F8, 12#F7, 14#F16, 24#F3, 25#F2, 26#F8, 27#F3, 28#F4, 28#F10; tender: 26#F1, 26#F6, 26#F13, 27#F8, 28#F7, 32#F6, 32#F9, 32#F14, 33#F3, 33#F14, 35#F8; utilities: 12#F16

### C12 · Customs declaration builders: goods items, offices, previous declaration and issuer
- Kind: encoding · Findings: 32 (High 5, Medium 7, Low 20) in 17 files, 9 flows · Needs decision: none (12 findings marked "yes" go to D46)
- What is wrong: Declarations give the goods quantity as a weight without packages, no transport at the border, no link to the invoice the value rests on, and validity periods; the exit office of the exporting country appears in imports; `PreviousCustomsDeclaration` holds another country's declaration; the waybill names customs as issuer of the exporter's declaration. Example: `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side` (tender/30#F14); `rail/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331` (rail/08#F4).
- Where it comes from: `tools/examples_kit.py` `goods_items()` (line 844), `export_declaration()` (line 864), `import_declaration()` (line 881); `tools/examples_scenarios.py` `export_extras()` (line 4567), `import_extras()` (line 4590), `exit_office()` (line 4557), `rail_offices()` (line 590)
- What must be true afterwards: Each declaration declares packages, transport at the border and the invoice; offices are the declaring country's; a previous declaration is a declaration of the same procedure chain in that country; the issuer of a declaration is its declarant.
- Fix direction: Fix the shared customs builders; build check: the office in a declaration belongs to the declaring country.
- Depends on / blocks: none
- Note: The previous-declaration finding of sea/11 is also part of the goods chain (C71, D21).
- Touched by: D16 (each declaration values the goods on the basis of the country it is lodged in, and refers to the invoice the value rests on), D18 (every import declaration claims the preference with its criterion and proof of origin; the note "Duties paid by the importer's account at customs." goes; the elements are O49), D20 (the packages are the bench's three parcels on pallets, O61), D21 (the previous declaration of the sea export sea/11 is the import under which the goods entered Bayvarra: the rail delivery's declaration for the benches, the March road import for the frames), D27 (times with offsets).
- Not settled by D21: the rail flow has a transit declaration (rail/06) and no import declaration into Bayvarra, so the "rail delivery's declaration" that sea/11 is to cite for the benches is not an example today.
- State: ready in part: 31 findings ready (the value of sea/11's previous declaration with C71 in stage 4); waste/02#F4 (a domestic movement reported to the customs administration's border office) waits for D42.
- Fixed in part (2026-11-17, stage 1 step 1f): an import cites another country's export declaration as a typed additional reference, not as its previous declaration, and carries no release validity and no exit office of the exporting country; the rail transit drops the offices that did not fit their definitions and cites the export declaration at departure as a document outside the examples; every declaration refers to the commercial invoice its value rests on where that invoice is issued by then (`declaration_invoices()`), and states the mode of transport at the border (`border_transport()`); the waybills name Valdara, the declarant, as issuer of its declarations, and the road waybill says the seller declares the export (D46); the sea export states its values per goods item only. The sea export's previous declaration is Bayvarra's own import of the goods (D21): it stays and takes its value from the ledger in stage 4. Still to come: packages per goods item with the three-parcel bench (D20, stage 4); the customs offices' places and identifiers with the place list (O91); waste/02#F4 with D42. Coverage: O145.
- Findings: cotton: 15#F8, 15#F10; energy: 04#F11, 05#F11; plastics: 05#F2, 05#F9, 09#F5, 09#F8, 09#F9, 09#F13; rail: 06#F5, 06#F6, 06#F12, 08#F4; road: 05#F1, 08#F4, 08#F5, 10#F12; sea: 11#F1, 11#F3, 11#F4, 11#F16, 19#F10, 19#F11; tender: 30#F12, 30#F14, 31#F14, 31#F15; waste: 02#F4; wood: 05#F11, 07#F11, 07#F12

### C13 · Identifiers built from flow names, file numbers and other identifiers
- Kind: generator mechanism · Findings: 28 (High 0, Medium 0, Low 28) in 28 files, 7 flows · Needs decision: none (5 findings marked "yes" go to D46)
- What is wrong: Signature IDs contain the flow name or the example's file number, pallet SSCCs start with the serial of the first casting, the same remittance ID `VI-RM-26-0316` is used by three payers (see C74), a journey/week number is one off. Example: `cotton/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `SCG-SIG-EX-cotton` (cotton/11#F14); `road/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-road` (road/05#F17).
- Where it comes from: `tools/examples_kit.py` `tep()` signature `…-SIG-{flow.base}` (line 715), `waybill()` signature (line 784), `unit_id()` (line 1346: SSCC serial from the castings' serial); flow-name signature IDs in `tools/examples_scenarios.py` (search "SIG-EX")
- What must be true afterwards: No identifier contains a flow name or file number; identifiers of different things are not derived from each other unless the world's rule says so.
- Fix direction: Per scheme an independent running number in the issuer's series (identifiers#F4 option a); signature identifiers only in the signatures stage, then with the company's one code (D6, D25).
- Depends on / blocks: none
- Touched by: D6 (deferred: no signature is removed or added before the signatures stage, and the signature identifiers of this cause wait for it), D25 (signature identifiers then take the company's one code), D24 (the remittance ID shared by three payers goes with C74), D5 (no identifier of a party repeats the digits of another; Codana licence plates carry the issuing company's number, O22, O32).
- State: ready in part: 2 findings ready (energy/05#F13, and identifiers#F4 for the pallet SSCC and the other derived identifiers); the 26 findings on signature IDs wait for the signatures stage.
- Fixed (2026-11-17, stage 1 step 1g): pallet SSCCs and Codana licence plates take their serial from a running series of the packer (`unit_serial()` in `tools/examples_kit.py`), no longer from the flow's number or the castings' serials; the carnet consignment is `VI-CS-26-0241` in Valdara's series; the forwarder's transport plan in the retail status request is `BF-TEP-26-0262`, no longer the distributor's request number. energy/05#F13 was done by C41 in step 1d. The other derived values of identifiers#F4 go with C61 (new Codana company numbers in order of registration, so the ISO 6523 values no longer cut the register numbers, and telephone numbers without relation to an identifier, O22) and the bank accounts with the master data of stage 3; the issuer prefixes with C75.
- Findings: cotton: 09#F15, 11#F14, 13#F14, 15#F17; energy: 05#F13; plastics: 04#F13, 05#F16, 06#F24, 09#F16; road: 05#F17, 06#F10, 07#F12, 09#F12, 10#F18, 16#F5; sea: 09#F16, 11#F25, 12#F15, 13#F12, 14#F25; tender: 15#F20, 17#F19, 19#F18, 30#F17, 31#F17; wood: 05#F17, 07#F16; consistency: identifiers#F4

### C14 · The buyer's cost centre does not fit what is bought
- Kind: master data · Findings: 24 (High 1, Medium 2, Low 21) in 24 files, 11 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: Each party has one cost centre, used for whatever it buys: Valdara books electricity, waste services and freight as "Raw materials and parts", the store books shirts to its garden department, outbound freight is "Stock purchases". Example: `packaging/03-Order.xml:/Order/cbc:AccountingCostCode` = `2200` (packaging/03#F2); `utilities/05-UtilityStatement.xml:/UtilityStatement/cbc:AccountingCostCode` = `6120` (utilities/05#F11).
- Where it comes from: `tools/examples_kit.py` `cost_centre()` (line 215) with `world/parties.json` `cost_centre` (one per party, e.g. line 149)
- What must be true afterwards: The accounting cost of a line fits what the line buys, from the buyer's own chart.
- Fix direction: Give parties.json a small chart of cost centres per kind of purchase and let `cost_centre()` choose by item kind.
- Depends on / blocks: none
- Touched by: D9 (furniture/14 is re-homed with the furniture flow, O6).
- State: ready in part: 22 findings ready; furniture/14#F2 waits for D32 (O6); tender/33#F18 (the programme code against the procurement documents, the subject of C121) waits for D28.
- Fixed in part (2026-11-17, stage 1 step 1e): every buyer has a chart of cost centres by kind of purchase (`cost_centres` in `world/parties.json`: goods, packaging, freight and forwarding, energy and water, telephone and data, services, and per item where a department buys it, such as the store's clothing department for shirts and the department's planning-office fit-out for desks and installation); each item names its kind of purchase (`purchase` in `world/items.json`); the order, invoice, credit note and utility statement take the cost centre of what they buy (`kit.cost_centre(..., iid=...)`). The issuers' own ledger codes go from the farm's delivery note and the water company's reminder. Still to come: furniture/14#F2 goes with the removed debit note (D32); tender/33#F18 (the programme code) with the tender flow (D28). Coverage: O145.
- Findings: air: 10#F4; cotton: 03#F2; furniture: 14#F2, 15#F4, 16#F5, 17#F5; packaging: 03#F2, 04#F2, 05#F2, 07#F2; rail: 10#F4; retail: 16#F3; road: 14#F5; sea: 18#F4; tender: 33#F18; utilities: 01#F8, 02#F8, 03#F4, 05#F11, 06#F8, 10#F1, 12#F10, 13#F3; waste: 03#F4

### C15 · Shipment gross weight without the transport equipment
- Kind: encoding · Findings: 24 (High 5, Medium 15, Low 4) in 24 files, 6 flows · Needs decision: taken: merge decisions, row "Shipment `GrossWeightMeasure` without the transport equipment" (4 findings marked "yes" go to D46)
- What is wrong: `Shipment/GrossWeightMeasure` includes the transport equipment by its definition, but the kit writes the goods' gross weight, also where the same document gives the container's tare (sea/10: the shipment weighs less than its own container). Example: `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29` (cotton/09#F5); `sea/10-PackingList.xml:/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4` (sea/10#F1).
- Where it comes from: `tools/examples_kit.py` `gross_weight()` (line 469), used by `despatch_advice()` (line 415) and `waybill()` (line 789)
- What must be true afterwards: The shipment gross weight includes the equipment where the document knows it (container, wagons), or is absent; the goods' gross weight is on the goods item or consignment.
- Fix direction: Compute goods + tare where equipment is known, else move the value to the goods item; build check: shipment gross ≥ sum of equipment tare + goods.
- Depends on / blocks: none
- Touched by: D20 (the bench weighs 44.4 kg gross, and the pallets' own weight, about half a tonne for 25 pallets, is added to consignment and container weights; O61).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): one rule in the build (`shipment_weights()` in `tools/build_examples.py`): where a document states its transport equipment, the shipment's gross weight is the goods plus the tares (the sea container: 4,106.4 + 3,750 = 7,856.4 kg) or the equipment's gross weights (the two rail boxes: 2 × 7,884 = 15,768 kg), and the goods' weight is the consignment's, whose definition excludes the equipment; where it does not, the goods' weight is on the consignment or the goods item only. The waste flow's weighbridge weight is the loaded truck and goes with D42. The bench's weights change with D20 in stage 4.
- Findings: cotton: 03#F11, 09#F5, 11#F1, 13#F4, 15#F1; mast: 02#F4, 03#F4, 04#F2; ore: 04#F1, 05#F3; rail: 06#F1, 08#F2; sea: 06#F2, 09#F4, 10#F1, 11#F6, 12#F3, 14#F2, 15#F2, 19#F5, 20#F4; wood: 05#F7, 06#F11, 07#F10

### C16 · "NoStatus" as document or line status
- Kind: encoding · Findings: 24 (High 0, Medium 0, Low 24) in 24 files, 10 flows · Needs decision: taken: merge decisions, row "`NoStatus` as status code"
- What is wrong: Document and line status codes say "NoStatus" in despatch advices, requests and receipts of ten flows: a filler that states nothing (UBL IND5/IND6). Example: `plastics/03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus` (plastics/03#F5); `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cbc:DocumentStatusCode` = `NoStatus` (sea/16#F9).
- Where it comes from: `tools/examples_kit.py` `despatch_advice()` (lines 407, 421), `receipt_advice()` (line 436), `tep_request()` (line 680), and scenario documents that copy them
- What must be true afterwards: No `DocumentStatusCode` or `LineStatusCode` with a value that only says there is no status.
- Fix direction: Remove the elements from the kit builders; a build check rejecting the code "NoStatus".
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1c): no `NoStatus` in any builder; the build rejects the value. Coverage: O145.
- Findings: air: 03#F18, 06#F7, 08#F9; cotton: 03#F1, 04#F24, 09#F6; mast: 04#F5; plastics: 03#F5, 08#F7; rail: 02#F8; retail: 11#F8, 12#F17, 17#F7; road: 03#F4, 04#F8; sea: 06#F13, 09#F15, 12#F14, 16#F9, 20#F8, 21#F6; tender: 29#F11; wood: 04#F5, 06#F4

### C17 · Remittance advices: the invoice twice on a line, two payment-order references, header parties repeated
- Kind: encoding · Findings: 21 (High 0, Medium 0, Low 21) in 10 files, 8 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: The remittance builder references the paid invoice twice on the same line, gives two different values for the payer's payment order, repeats the header's accounting parties on the line and sets a generic payment purpose, in eight flows. Example: `plastics/11-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PayerReference` = `RP-0882` (plastics/11#F3); `utilities/04-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0313` (utilities/04#F5).
- Where it comes from: `tools/examples_kit.py` `remittance()` (line 546)
- What must be true afterwards: One reference per paid document per line, one payment-order reference, line-level parties only where they differ.
- Fix direction: Fix `remittance()` once.
- Depends on / blocks: none
- Touched by: D23 (the utility invoices these remittances pay become due 21 days after the bill under one Accord code, O73), D24 (the remittance number shared by three payers goes with C74).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): the remittance builder references each paid invoice once per line (its billing reference), gives the payment order once (no second `PayerReference`), leaves out the line's parties that repeat the header's, and names the purpose of the payment (`purpose`: `ELEC`, `WTER` and `PHON` for the utility bills, `SUPP` otherwise); the store's credit note settled by set-off carries no payment purpose; the furniture order refers to its quotation line once. Coverage: O145.
- Findings: cotton: 18#F2, 18#F3, 18#F4; furniture: 08#F11; ore: 08#F2, 08#F3, 08#F4; plastics: 11#F3, 11#F4; retail: 19#F11; road: 17#F9, 17#F10; utilities: 04#F3, 04#F5, 04#F8, 07#F4, 07#F6, 14#F9, 14#F10; wood: 09#F7, 09#F8

### C18 · Transport events without type or place, or as generic events where a dedicated one exists
- Kind: encoding · Findings: 19 (High 0, Medium 9, Low 10) in 17 files, 6 flows · Needs decision: none
- What is wrong: Events are given with a date and time but no type and no location, or as "additional" free-text events where the stage has a dedicated event (loading, acceptance, arrival), in six flows. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13` (air/03#F6); `rail/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00` (rail/02#F7).
- Where it comes from: `tools/examples_kit.py` `event()` (line 1273) and its callers in the scenarios
- What must be true afterwards: Every event says what happened (dedicated element or type code) and where.
- Fix direction: Make `location` and `type_code` required in `event()` and use the dedicated stage events.
- Depends on / blocks: none
- Touched by: D27 (a time carries its offset from UTC, at least where a document crosses the zone boundary, O78).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): every transport event names its place (the leg's warehouse, hub, border station, quay, port, airport or the receiver's goods-in, with a UN/LOCODE-form code or a GLN where the world has one), and an event in the generic `TransportEvent` carries a type code; `transportation_status()` requires one. The world's event-type list gains `ACCEPTANCE`, `LOADING`, `DISCHARGE`, `ENROUTE` and `STORAGE` (O146). The build rejects an event without a place, or a generic one without a type. Places get their identifiers from the place list (O91).
- Findings: air: 03#F6, 05#F3, 09#F4; plastics: 04#F22, 06#F20; rail: 02#F7, 03#F19, 07#F3, 07#F6, 08#F11, 09#F3; retail: 15#F5; road: 08#F27; sea: 08#F8, 13#F5, 14#F18, 16#F19, 17#F4, 17#F5

### C19 · Framework transport-plan clauses and periods mis-encoded
- Kind: encoding · Findings: 19 (High 4, Medium 7, Low 8) in 8 files, 6 flows · Needs decision: none (4 findings marked "yes" go to D46)
- What is wrong: The shared framework clauses put a late-delivery penalty into `PenaltySurchargePercent` (a late-payment element), a post-event duration into a pre-arrival notice, a stationary-service location without a stationary service, a commission to an absent broker, and "Waiting time 40 per hour" without a currency; the service period starts after the pickup it contains (rail/02, 03) or the pre-arrival period lies before the transport (ore/03); the wood transport window ends before the promised delivery window. Example: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:StartDate` = `2026-03-04` (ore/03#F2); `rail/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14` (rail/02#F2).
- Where it comes from: `tools/examples_kit.py` `tep_terms()` (lines 646–661) and `tep_request()`/`tep()` periods (lines 673–738)
- What must be true afterwards: The clauses use elements whose definitions fit; every amount has a currency; the service period contains the pickup and delivery.
- Fix direction: Fix `tep_terms()` once (it is shared by ore, rail and plastics) and derive the periods from the legs.
- Depends on / blocks: none
- Note: The waiting-time currency is "Cannot be told" 8 in the conditions file; the fixing session picks XUF or XBL with a plausible rate.
- Touched by: D22 (the carriers' invoices follow the plans' "30 days net from the consignment note"; the clause stays), D9 (demurrage and waiting time are the candidates for the world's real debit note, O7: keep those clauses and give them a currency), D19 (periods follow the legs' durations at 14 km a square, O60).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): the shared framework terms (`kit.tep_terms()`) state the late-delivery penalty as the carrier's liability in the note, without `PenaltySurchargePercent` (a late-payment element); the pre-arrival notice without a post-event duration; the waiting-time charge in the carrier's currency at a plausible rate (40 lume an hour at the parities, 4,000 ferra for the Urvanian carriers); no broker's commission (the barge is booked directly); no `AtLocation` filler; the ore plan's notice period on the day of the train; the rail request and plan start with the pickup; the wood flow's requested and promised delivery window 26 February to 6 March, around the transport; the utility reminder's 0 % surcharge goes and the reminder says the surcharge is waived. The plastics plan's freight charge (plastics/04#F16) and the goods in the transport requests (plastics/03#F3, retail/11#F1) go with C21. Coverage: O145.
- Findings: ore: 03#F2, 03#F5, 03#F9, 03#F11; plastics: 03#F3, 04#F4, 04#F5, 04#F15, 04#F16, 04#F17, 04#F19; rail: 02#F2, 03#F2, 03#F7, 03#F17, 03#F18; retail: 11#F1; utilities: 10#F9; wood: 04#F1

### C20 · `ShippingOrderID` holding the consignment or shipment ID
- Kind: encoding · Findings: 18 (High 7, Medium 10, Low 1) in 18 files, 9 flows · Needs decision: taken: merge decisions, row "`ShippingOrderID` holding the consignment or shipment ID"
- What is wrong: `ShippingOrderID` is "the shipping order or forwarding instructions" number, but the kit fills it with the consignment ID, so the same shipment has two or three different "shipping orders" across a flow (air, sea). Example: `air/04-Waybill.xml:/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324` (air/04#F1); `rail/07-TransportationStatus.xml:/TransportationStatus/cbc:ShippingOrderID` = `VI-CS-26-0327` (rail/07#F2).
- Where it comes from: `tools/examples_kit.py` `waybill()` (line 759: `flow.numbers.get("consignment", number)`); `tools/examples_scenarios.py` lines 1639, 4249, 4279
- What must be true afterwards: Every `ShippingOrderID` is the number of the forwarding instructions or booking that exists in the flow, the same in all documents of the shipment, or the element is absent.
- Fix direction: Use the forwarding instructions' number where the flow has one, else drop the element; build check: a ShippingOrderID resolves to a ForwardingInstructions of the flow.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): `ShippingOrderID` is the number of the forwarding instructions the shipment is booked under (to the carrier where there are two: `kit.shipping_order()`), the same in the waybill, the bill of lading and the status messages of a flow; absent where the flow has no forwarding instructions, and in the forwarding instructions themselves. Coverage: O145.
- Findings: air: 03#F10, 04#F1, 05#F2, 09#F1; cotton: 09#F2; mast: 03#F1; ore: 05#F1; plastics: 06#F4; rail: 07#F2, 08#F7; retail: 13#F4, 14#F3; road: 08#F6, 09#F2; sea: 09#F3, 12#F1, 13#F2, 17#F1

### C21 · Transport requests, instructions, waybills and manifests that do not say what, from where, to where or when
- Kind: encoding · Findings: 18 (High 0, Medium 17, Low 1) in 18 files, 9 flows · Needs decision: none
- What is wrong: The generic transport builders give a weight and a note but no goods item, packages, places of taking over and delivery, or dates: forwarding instructions that do not say what to carry, a shipped-on-board bill without goods or vessel, a cargo manifest that does not list the cargo. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323` (air/03#F4); `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201` (cotton/09#F4).
- Where it comes from: `tools/examples_kit.py` `tep_request()` (line 673), `tep()` (line 700), `waybill()` (line 747); forwarding instructions in `tools/examples_scenarios.py` (`sea_consignment_fi()` line 1522, `air_consignment()` line 1892)
- What must be true afterwards: Every transport request, plan, instruction, waybill and manifest states the cargo (goods items, packages), the places and the requested or actual dates its definition calls for.
- Fix direction: Give the builders the consignment data the flow already holds (handling units, legs, events).
- Depends on / blocks: none
- Touched by: D20 (the cargo to state is the bench in three parcels on pallets, O61).
- State: ready to fix now.
- Fixed in part (2026-11-17, stage 1 step 1d): every waybill, forwarding instruction and bill of lading says what it carries: a goods item per line of the deal (description, quantity, gross weight, Harmonized System subheading; `kit.transport_goods()`), added by the build where the scenario gives none; every transport plan and request carries a summary of the goods on its consignment (UBL has no goods item under a consignment). Still to come: the handling units with their parcels, with D20 in stage 4 (sea/10#F3, retail/11#F1, wood/04#F4, the plastics bags); the places, stages, equipment requests and dates of the cotton, sea, air and mast transport documents (cotton/09#F4, 13#F2, 14#F1, sea/07#F4, 12#F2, 15#F3, air/03#F4, mast/02#F3), with their flows in stage 6, whose decisions move those dates (D30, D33, D36, D39); the freight charge in the plastics plan (plastics/04#F16) with D41.
- Findings: air: 03#F4, 04#F5; contest: 08#F4; cotton: 09#F4, 13#F2, 14#F1; mast: 02#F3; ore: 02#F2, 03#F6, 05#F2; plastics: 04#F6; retail: 13#F3; sea: 07#F4, 09#F2, 10#F3, 12#F2, 15#F3; wood: 04#F4

### C22 · Item properties of the slat: validity periods, repeated length, full specification
- Kind: master data · Findings: 17 (High 0, Medium 0, Low 17) in 7 files, 1 flow · Needs decision: none
- What is wrong: The slat's property "Planed on four sides" has a 12-month validity, its length is repeated in `SellersItemIdentification/MeasurementDimension`, and the full commercial specification (test methods) stands in customs declarations and invoices (wood, 7 files). Example: `wood/01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800` (wood/01#F8).
- Where it comes from: `world/items.json` hardwood slat properties; `tools/build_examples.py` `item_property()` (line 638)
- What must be true afterwards: Properties carry validity only where they expire; dimensions once, in the item; customs declarations carry what customs needs.
- Fix direction: Clean the slat's data in items.json (validity only where a property expires, the length once); the full specification in the customs declarations and the invoice goes with the profile per document type of D11 (C48).
- Depends on / blocks: none
- Touched by: D11 (decided: a customs declaration carries the description, commodity code, origin and weights; an invoice the identification, the name and what tax needs; the full specification stays in the documents of the item type), D12 (the bundle of 50 slats, `PackSizeNumeric` 50, stays as the world's pack of one item).
- State: ready in part: 14 findings ready (validity and repeated length); wood/05#F13, 07#F14 and 08#F12 (the specification in customs declarations and the invoice) wait for O20, with C48.
- Fixed (2026-11-17, stage 1 step 1g): the slat's surface property no longer carries a twelve-month usability period, and its seller's item number no longer repeats the length as a measurement dimension; the length is in the item's dimensions only (`world/items.json`, slat-1800).
- Findings: wood: 01#F8, 01#F9, 02#F14, 02#F15, 03#F11, 03#F12, 05#F12, 05#F13, 05#F14, 06#F13, 06#F14, 07#F13, 07#F14, 07#F15, 08#F11, 08#F12, 08#F13

### C23 · Places and offices given only by name or text, without the identifier they have elsewhere
- Kind: encoding · Findings: 16 (High 0, Medium 0, Low 16) in 16 files, 8 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: Delivery places of Incoterms, airports, customs offices and ports of registry are given by name only, although the flow identifies them elsewhere by UN/LOCODE or GLN. Example: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport` (sea/14#F19); `air/01-OrderChange.xml:/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal` (air/01#F8).
- Where it comes from: `tools/examples_kit.py` `place()` (line 1177) and `order()` delivery terms (line 300); `tools/examples_scenarios.py` `exit_office()` (line 4557)
- What must be true afterwards: A place that the world identifies carries its identifier wherever it is given.
- Fix direction: Use `place()` with the identifier for delivery terms, offices and ports.
- Depends on / blocks: none
- Touched by: D5 (site codes for Urvanian places only where a document uses one, O24), D19 (place positions at 14 km a square).
- State: ready to fix now.
- Fixed in part (2026-11-17, stage 1 step 1d): the build gives every location named like a place the world identifies (the UN/LOCODE-form towns, ports and airports, the legs' named places, every GS1 party's own locations, and a short list of the names the documents use for them) its identifier, also where the place is given only in `Description` (`identify_places()` in `tools/build_examples.py`). The customs offices have no identifier anywhere in the world yet: they get one with the place list (O91).
- Findings: air: 01#F8; cotton: 08#F10, 11#F7; ore: 01#F5; rail: 01#F13, 06#F13; retail: 14#F7, 22#F6; road: 05#F14; sea: 05#F11, 11#F15, 13#F9, 14#F19, 15#F12, 16#F22; wood: 03#F9

### C24 · Tax totals and taxable amounts that ignore the document's own charges, or state an empty zero
- Kind: encoding · Findings: 14 (High 5, Medium 1, Low 8) in 13 files, 8 flows · Needs decision: taken: merge decisions, row "Taxable amount that ignores the document's own allowance or charge" (1 finding marked "yes" goes to D46)
- What is wrong: The taxable amount leaves out the document-level allowance or charge of the same category (furniture/10, retail/08, cotton/04, 05, wood/03; air/01 the whole order instead of the change), and several documents carry a zero tax total without a category, scheme or reason (energy/08, sea/25, tender/15, tender/35, wood/02, cotton/04). Example: `tender/15-Tender.xml:/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00` (tender/15#F14); `air/01-OrderChange.xml:/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `51200.00` (air/01#F2).
- Where it comes from: `tools/examples_kit.py` `tax_total()` (line 243) and `monetary_total()` (line 259); `tools/examples_scenarios.py` `with_allowance()` (line 921)
- What must be true afterwards: Taxable amount = line extension ± document-level allowances and charges of that category; a tax total only where a tax is stated, with category and reason when it is zero.
- Fix direction: Feed allowances and charges into `tax_total()`; drop empty tax totals (for a Lisavan sale the whole tax section, D15). Build check: the tax arithmetic per subtotal.
- Depends on / blocks: none
- Touched by: D15 (a Lisavan sale carries no tax section, so the zero tax totals of the Lisavan self-billed documents cotton/04 and 05 go, and with them the taxable amounts these findings question; the presumptive tax stays in its `WithholdingTaxTotal`).
- State: ready to fix now.
- Fixed in part (2026-11-17, stage 1 step 1e): one rule in the build (`tax_arithmetic()` in `tools/build_examples.py`): a subtotal's taxable amount is the lines of its category plus the document's charges less its allowances, a line or an allowance without a category in a document with one category takes that category, a levy collected for someone else is no part of the supply, and the build fails where a rate above zero would make the tax change; the order change air/01 states the amount of the change (512.00) in its totals; empty zero totals: the gas producer's reminder states the surcharge outside the scope with its reason (energy/08), the factor's statement and Valdara's reminder state no tax total (sea/25, tender/35, with its tax point date), the sawmill's quotation states its export subtotal (wood/02). Still to come: the zero tax totals of the three tenders (tender/15, 17, 19), with the wording of what the notices say about tax (O97, D28). Coverage: O145.
- Findings: air: 01#F2; cotton: 04#F2, 04#F23, 05#F3; energy: 08#F7; furniture: 10#F1; retail: 08#F2; sea: 25#F7; tender: 15#F14, 17#F14, 19#F14, 35#F9; wood: 02#F11, 03#F3

### C25 · Catalogue encoding: territory of the seller, "Active" status, CatalogueIndicator, discounts and dependent prices
- Kind: encoding · Findings: 12 (High 3, Medium 5, Low 4) in 5 files, 3 flows · Needs decision: none
- What is wrong: Every catalogue puts the seller's country into the price's territory, so an export price carries "Export outside Bayvarra" for the territory Bayvarra (conditions#F1: one price list, two tax treatments); the price list status is "Active" where the element names original/copy/revision; `CatalogueIndicator` is set in the catalogue itself; the "full container" discount and the dependent side-frame price do not follow from their conditions. Example: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB` (sea/02#F1); `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU` (tender/25#F1).
- Where it comes from: `tools/examples_kit.py` `catalogue_terms()` (line 1001; territory = seller's country at line 1015); `tools/build_examples.py` `item()` `CatalogueIndicator` (line 871)
- What must be true afterwards: Territory = the market the price is offered for, with the tax treatment the seller applies to sales into that market (D17: a seller states its own country's tax, so an export out of the seller's country keeps its export exemption); one price list ID, one territory, one treatment; status codes from the element's meaning; no indicator in the catalogue itself.
- Fix direction: Fix `catalogue_terms()` (option a of conditions#F1: territory = buyer's market).
- Depends on / blocks: none
- Touched by: D17 (a seller states its own country's tax), D14 (Valdara has a list price, 499.00 on its list `VI-PL-2026`, and a distributor price; the price type list says for each type whether it includes tax, O28), D20 (a "full container" is a kind of booking, not a statement that the hold is full).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): a catalogue price's territory is the buyer's market (the island for Velumi, Bayvarra for the store and the public works department), so it agrees with the export or domestic tax category the line carries; the price list's status is `ORIGINAL` (UBL names original, copy, revision or cancellation; `ORIGINAL` and `REVISION` added to the world's record-status list); `CatalogueIndicator` goes from the catalogues and marks the items of the orders placed from a catalogue (sea/05, retail/08); the full-container discount is a quantity range of its own from 144 benches (a 40-foot container of 36 pallets of four, D20), so the sea order's 96 do not qualify (D30); the maximum order is two full containers, 288; the frame's price is no longer a share of the bench's (D34 lowers one and not the other), so `DependentPriceReference` goes. Coverage: O145.
- Findings: retail: 02#F15, 02#F23, 03#F11; sea: 02#F1, 02#F5, 02#F6, 02#F7, 02#F21; tender: 25#F1, 25#F7, 25#F8; consistency: conditions#F1

### C26 · Documents referenced as a kind they are not
- Kind: encoding · Findings: 11 (High 0, Medium 7, Low 4) in 9 files, 3 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: A delivery note is referenced as a despatch advice, a weighbridge ticket as a receipt advice, a quotation as a contract, a work report and a budget commitment as billing documents, a bill of lading as a delivery note. Example: `cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193` (cotton/04#F3); `furniture/11-OrderCancellation.xml:/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568` (furniture/11#F1).
- Where it comes from: source not located in one place: the reference elements chosen in the scenario code (cotton `self_billed()` in `tools/examples_kit.py` line 1115, furniture in `tools/examples_scenarios.py` lines 3268–3396, sea debit note `sea_with_debit()` line 5904)
- What must be true afterwards: Each reference uses the element for the kind of document referenced, or a typed `AdditionalDocumentReference`.
- Fix direction: Correct the reference elements per flow.
- Depends on / blocks: none
- Touched by: D9 (furniture/14 and sea/28 are not debit notes and are re-homed with their flows, O6).
- State: ready in part: 8 findings ready; furniture/11#F1 and 14#F3 (the quotation used as a contract, which C103 also names) wait for D32; sea/28#F7 waits for D30 (O6).
- Fixed in part (2026-11-17, stage 1 step 1c): cotton/04 and 05 do not cite the delivery note as a despatch advice; the weighbridge ticket is a typed additional reference in 04 and goes from 05; the department's budget commitment is an additional reference, given in the order (15) and quoted on the work report (16) and the invoice (17); the work report is no longer a line billing reference (17); the digital agreement is no longer the contract of the sea order response (06), the credit note (26), the air order change (01) or the cancellation (07) (D30). furniture/11#F1 and 14#F3 wait for D32, sea/28 goes with D30. Coverage: O145.
- Findings: cotton: 04#F3, 04#F11, 05#F4, 05#F12; furniture: 11#F1, 14#F3, 16#F1, 17#F1; sea: 06#F7, 26#F5, 28#F7

### C27 · Despatch advices that do not say when the goods leave or arrive
- Kind: encoding · Findings: 10 (High 0, Medium 8, Low 2) in 10 files, 9 flows · Needs decision: none
- What is wrong: The kit's despatch advice has no despatch date or time, no estimated delivery and no transport reference, in nine flows. Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323` (air/06#F6); `packaging/06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cbc:ID` = `LTM-SH-26-0527` (packaging/06#F2).
- Where it comes from: `tools/examples_kit.py` `despatch_advice()` (line 401)
- What must be true afterwards: Every despatch advice states the despatch (actual or planned) and the expected delivery, and how the goods are identified.
- Fix direction: Add `Shipment/Delivery/Despatch` dates and the estimated delivery period in `despatch_advice()`.
- Depends on / blocks: none
- Touched by: D27 (dates on the issuer's working days, times with offsets, O78).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): every despatch advice states its actual despatch date and an estimated delivery period (`kit.despatch_delivery()`), from the transit of the flow's main mode or the leg's own `transit_days` in `world/documents.json` (the ore train and the sawmill's truck arrive the same day, D45, D43); flows that state their own delivery keep it. The durations follow the place list (O91) in stage 2; air/06's waybill and handling unit with the air flow (D39).
- Findings: air: 06#F6, 08#F7; mast: 04#F7; ore: 04#F3; packaging: 06#F2; plastics: 08#F1; retail: 12#F3; sea: 20#F5; tender: 29#F4; wood: 06#F3

### C28 · Orders without a requested delivery date
- Kind: encoding · Findings: 10 (High 0, Medium 0, Low 10) in 10 files, 7 flows · Needs decision: none
- What is wrong: Orders and order changes state no requested delivery or collection date, also where urgency is the reason (air/01). Example: `air/01-OrderChange.xml:/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:ID` = `CPT` (air/01#F9); `furniture/10-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport` (furniture/10#F6).
- Where it comes from: `tools/examples_kit.py` `order()` (line 285)
- What must be true afterwards: Every order states when the goods are wanted (or, for ex-works, when they are collected).
- Fix direction: Add `Delivery/RequestedDeliveryPeriod` in `order()` from the flow's dates.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): every order and order change states when the goods are wanted: where the scenario states nothing, the build gives the requested delivery period from the flow's table (`REQUESTED_DELIVERY` in `tools/examples_scenarios.py`, days from the flow's start, so that a flow that moves in stage 6 keeps it), and fails on an order without one; free-carrier orders state their collection instead. The rule covers all twenty orders, not only the ten the findings name.
- Findings: air: 01#F9; furniture: 10#F6; packaging: 01#F6, 03#F6, 05#F6; plastics: 01#F9; rail: 01#F12; retail: 08#F10; wood: 03#F8, 10#F4

### C29 · Urvania's national tariff subheading in other countries' documents
- Kind: encoding · Findings: 10 (High 0, Medium 2, Low 8) in 10 files, 5 flows · Needs decision: taken: `analysis/codelist-decisions.md` Q24 ("tariffs, rates and exemptions stay national") and `note/src/03-world.md` ("in Urvania, the national tariff code") (4 findings marked "yes" go to D46)
- What is wrong: The 8-digit Urvanian subheading travels with the bench and the frame into Bayvarran and Lisavan declarations (road/10, tender/31, sea/11, sea/19, rail/06) and into Bayvarran commercial documents. Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990` (air/06#F13); `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910` (sea/19#F7).
- Where it comes from: `world/items.json` `national_tariff` of bench and frame (e.g. line 253), written by `tools/examples_kit.py` `customs_item()` (line 828) into every customs declaration and item
- What must be true afterwards: A national subheading appears only in documents of the country whose tariff it is.
- Fix direction: Write `national_tariff` only when the declaring country (or the seller, for commercial documents) is Urvania (conditions#F10 option a).
- Depends on / blocks: none
- Note: The findings marked "yes" are settled by Q24; confirmed in bulk (D46).
- Touched by: D13 (the frame's own subheading and Urvania's tariff line change to those of 9401.99; the rule of this cause is unchanged), D18 (tariffs stay national; Accord goods are free of duty on proof of origin).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1f): a national tariff subheading appears only in documents of the country whose tariff it is: the declaring country's declarations and the seller's commercial documents (`national_tariffs()` in `tools/build_examples.py`, decision Q24).
- Findings: air: 01#F10, 06#F13, 08#F15; retail: 02#F22, 04#F16; road: 10#F10; sea: 19#F7, 26#F11; tender: 31#F7; consistency: conditions#F10

### C30 · Transport document type fixed per mode, not per convention and scope
- Kind: encoding · Findings: 10 (High 1, Medium 4, Low 5) in 10 files, 7 flows · Needs decision: none (3 findings marked "yes" go to D46)
- What is wrong: A domestic road carriage gets a CMR, a domestic rail carriage a CIM note, the rail flow's waybill is a CMR, and despatch advices in air and sea shipments ask for damage to be noted "on the consignment note". Example: `road/11-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:Delivery/cac:DeliveryNoteDocumentReference/cbc:ID` = `TH-WB-26-0159` (road/11#F2); `air/06-DespatchAdvice.xml:/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.` (air/06#F8).
- Where it comes from: `tools/examples_kit.py` `WAYBILL_KIND` (line 741: one kind per mode) used by `waybill()`; damage notes "on the consignment note" in despatch advices
- What must be true afterwards: The waybill type follows the convention that applies to the leg (international or domestic, mode), and texts name the document the flow uses.
- Fix direction: Choose the kind by mode and border crossing (codelist-decisions: WaybillTypeCode by legal regime); fix the despatch-advice note.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready in part: 9 findings ready; rail/08#F1 (a road consignment note for an international rail carriage) waits for D37 (which consignment note the rail leg has).
- Fixed (2026-11-17, stage 1 step 1d): the waybill type follows the convention of the carrier's main leg and its scope (`kit.waybill_kind()`): CMR, CIM, CMNI and the air waybill between two countries, and the new world codes `NATROAD` and `NATRAIL` within one (the store's truck in Bayvarra and the ore train in Urvania, D46); the rail flow's waybill is a CIM note (D37); the receipt advices cite the road waybill as a typed transport document, not as a delivery note; a despatch advice asks for damage to be reported in the receipt advice where the flow has one, else on its transport document by name; the air forwarding instructions no longer ask for a bill of lading. Coverage: O145.
- Findings: air: 03#F5, 06#F8, 08#F10; mast: 04#F6; ore: 05#F4; rail: 08#F1; retail: 13#F7; road: 11#F2, 13#F5; sea: 20#F9

### C31 · Electricity, gas, water and levies classified as services
- Kind: encoding · Findings: 9 (High 0, Medium 5, Low 4) in 6 files, 3 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: `SupplyTypeCode` is "SERVICES" for electricity, gas and drinking water (utilities, energy) and for a levy that is no supply, while gas is goods elsewhere in the same flow. Example: `utilities/06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES` (utilities/06#F2); `energy/03-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES` (energy/03#F1).
- Where it comes from: `tools/examples_kit.py` `tax_category()` (lines 115–128: GOODS only for items of kind "goods")
- What must be true afterwards: Energy and water are goods (or the code is absent); a levy collected for a third party carries no supply type.
- Fix direction: Classify the utility items as goods in items.json and skip the code for levies.
- Depends on / blocks: none
- Touched by: D15 (the levy's tax category `O` with `LEVY` goes to D31, O16; dropping the supply type on the levy does not depend on it).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): electricity, wholesale electricity, gas and drinking water are supplies of goods (`supply` in `world/items.json`, `kit.supply_kind()`), whatever their tax treatment, which keeps following `kind`; network use and telephony stay services; the city's sewage levy, collected for someone else, carries no supply type.
- Findings: energy: 03#F1; furniture: 09#F8; utilities: 02#F4, 06#F2, 06#F6, 09#F5, 09#F11, 11#F2, 11#F9

### C32 · Invoices not linked to the delivery they bill
- Kind: encoding · Findings: 8 (High 0, Medium 0, Low 8) in 8 files, 5 flows · Needs decision: none
- What is wrong: Invoices give no delivery date or place and no despatch or receipt reference, also where an export exemption rests on the delivery (packaging/02, rail/11, wood/08). Example: `air/10-Invoice.xml:/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324` (air/10#F9); `cotton/16-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198` (cotton/16#F6).
- Where it comes from: `tools/examples_kit.py` `invoice()` (line 473)
- What must be true afterwards: Every invoice for goods identifies the delivery (despatch advice reference or delivery date and place); an export exemption names its evidence.
- Fix direction: Add `DespatchDocumentReference` and `Delivery` in `invoice()`.
- Depends on / blocks: none
- Touched by: D9 ("Story lines: Billing documents": Valdara invoices on despatch, so its invoices refer to the despatch).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): an invoice for goods refers to the despatch advice of its own sale and states the delivery: the place from the leg to the buyer, the day the goods arrived, or, for an invoice issued on despatch, the day they left (`kit.invoice_delivery()`; a despatch advice records its despatch and expected delivery day, D9); scenario-specific deliveries for the forwarder's air freight (air/10, the day flown), the ginnery's FOB sale (cotton/16, on board at Selanu, with the bill of lading), the sawmill's ex-works timber (wood/11, collected at the yard) and Valdara's rail export (rail/11, at the siding, with the transit declaration and the consignment note as the export evidence). The road leg takes two days (D35), so the road invoice of 24 March states its despatch.
- Findings: air: 10#F9; cotton: 16#F6; packaging: 02#F8, 04#F3, 07#F3; rail: 11#F7; wood: 08#F9, 11#F4

### C33 · "Three originals" against the distribution list
- Kind: encoding · Findings: 8 (High 3, Medium 0, Low 5) in 8 files, 8 flows · Needs decision: taken: merge decisions, row "Waybill note "three originals" against the distribution list" (2 findings marked "yes" go to D46)
- What is wrong: The waybill says "Three originals: consignor, consignee, carrier." while its distribution lists one original and an electronic copy (eight flows). Example: `plastics/06-Waybill.xml:/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.` (plastics/06#F3); `rail/08-Waybill.xml:/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.` (rail/08#F6).
- Where it comes from: `tools/examples_kit.py` `waybill()` note (line 762) and `DocumentDistribution` (lines 772–779); `tools/examples_scenarios.py` line 1640, `bl_distribution()` (line 4418)
- What must be true afterwards: The note and the distribution list agree on the number of originals and who gets them.
- Fix direction: Generate the note from the distribution (or the distribution from the convention); build check comparing the two.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): the waybill's distribution lists the consignor's original (handed over, the new world code `ORIGINALHANDED`), the consignee's original with the goods and the electronic copy; the note names the three originals as the distribution lists them, the carrier keeping its own. sea/14#F11: the holder of the bill of lading is Bayforth, which receives the originals (option b, which avoids losing `BillOfLadingHolderParty`; the merge preferred dropping it).
- Findings: air: 04#F16; mast: 03#F8; ore: 05#F6; plastics: 06#F3; rail: 08#F6; retail: 13#F1; road: 08#F19; sea: 14#F11

### C34 · Line IDs reused for another line
- Kind: encoding · Findings: 7 (High 4, Medium 0, Low 3) in 7 files, 2 flows · Needs decision: none
- What is wrong: The air order change adds frames under line ID 1, the bench line of the order it changes; responses and despatch advices follow; a substitute line and a handling-unit receipt line reuse ID 1 (retail). Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1` (air/06#F2); `retail/08-Order.xml:/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cbc:ID` = `1` (retail/08#F9).
- Where it comes from: `tools/examples_kit.py` despatch and receipt lines (lines 423, 450–451: line i refers to order line i); the air order change in `tools/examples_scenarios.py` `air()` (line 1940)
- What must be true afterwards: A new line has a new ID, carried through the follow-up documents; references point to the line they mean.
- Fix direction: Give the added line ID 3 (air) and fix the index-based references in the kit.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): a deal line may name the order line it is (`line` in the flow's deal); the kit uses it for the order line's ID and every later reference to it (order response, despatch and receipt lines, invoice lines). The air frames are line 3 of the sea order as changed, from the order change to both despatch advices; the retail substitute is line `1.1`, the per-pallet despatch lines `1-1` to `1-6`, the damaged pallet's receipt line `1-3`.
- Findings: air: 01#F1, 02#F1, 06#F2, 08#F3; retail: 08#F9, 12#F9, 17#F13

### C35 · One transport service code per mode
- Kind: encoding · Findings: 7 (High 7, Medium 0, Low 0) in 7 files, 3 flows · Needs decision: none
- What is wrong: The service code depends only on the mode, so the ore in bulk wagons gets a container-train service, the rail flow's road pickup becomes "Full truck load" as main service of a container train, and the plastics barge carries "bulk" for bagged cargo. Example: `ore/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT` (ore/02#F1); `plastics/07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Bulk cargo down the river to the coast of Bayvarra, per tonne.` (plastics/07#F2).
- Where it comes from: `tools/examples_kit.py` `MODE_SERVICE_CODE` (line 619: road FTL, rail RAILCONT …)
- What must be true afterwards: The main service fits the cargo and the means (wagon load for ore, container train with a pre-carriage stage for the road leg, bagged cargo for jumbo bags).
- Fix direction: Choose the service from the leg and the cargo type, not the mode alone.
- Depends on / blocks: none
- Touched by: none of D1 to D27; the rail findings meet D37 (open: CIM for the rail leg with a road pre-carriage stage), which leaves the service code to this cause.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): the main transport service is chosen by the carrier's main leg and its cargo (`kit.main_service()`): a leg names its service in `world/documents.json` where the mode does not tell it (the ore train `RAILWAGON`); the rail flow's main service is the container train, not its road pre-carriage; the barge freight is bagged cargo (`world/items.json`).
- Findings: ore: 02#F1, 03#F1, 06#F2; plastics: 07#F2; rail: 02#F1, 03#F1, 09#F2

### C36 · Ad valorem indicator and declared carriage value without a valuation
- Kind: encoding · Findings: 5 (High 2, Medium 0, Low 3) in 5 files, 3 flows · Needs decision: none (3 findings marked "yes" go to D46)
- What is wrong: `AdValoremIndicator` and declared carriage values appear where no ad valorem charge or duty exists, and with opposite values for the same air shipment. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `false` (air/03#F3); `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `true` (cotton/09#F7).
- Where it comes from: `tools/examples_kit.py` `waybill()` (line 765); `tools/examples_scenarios.py` lines 1638, 1654
- What must be true afterwards: The indicator and the value appear only together with the charge they concern, the same in every document of a shipment.
- Fix direction: Drop them (preferred in air/03, 04).
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): no `AdValoremIndicator` in any transport document (UBL defines it by ad valorem duties; no shipment pays duty, D18); cotton declares no carriage value (nothing was charged for it, and the Bank of Selanu's role goes with D33). The air frames and the granulate keep their declared value; the valuation charge the findings ask for comes with their flows (D39, D41). Coverage: O145.
- Findings: air: 03#F3, 04#F3; cotton: 09#F7, 13#F6; plastics: 06#F12

### C37 · Order references in the wrong element
- Kind: encoding · Findings: 5 (High 0, Medium 3, Low 2) in 4 files, 3 flows · Needs decision: none
- What is wrong: `SalesOrderID` holds the seller's number of the original order in a buyer's change, a release number sits in `ReleaseID` (delivery-access release), a project name in `CustomerReference`. Example: `air/07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:CustomerReference` = `Harbour parks Selanu` (air/07#F4); `tender/26-Order.xml:/Order/cbc:SalesOrderID` = `VI-SO-26-0058` (tender/26#F4).
- Where it comes from: source not located in one place: the air order change (`tools/examples_scenarios.py` `air()`, line 1940) and the tender call-off enrichments (after line 7151)
- What must be true afterwards: Each order reference element holds what its definition says.
- Fix direction: Correct the values.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1c): the seller's order number in `OrderReference/SalesOrderID` of the air order change; no `CustomerReference` in the cancellation's order reference; the tender's sales order number in the seller's response (28), not the buyer's order; the release number of the call-off as a note, not `Delivery/ReleaseID`; the untraceable export release `ReleaseID` of road/04 dropped (option b), to come back as the export declaration's number in stage 5. Coverage: O145.
- Findings: air: 01#F7, 07#F4; road: 04#F12; tender: 26#F4, 26#F5

### C38 · Bayvarra's surcharge "per month" encoded as one month only
- Kind: encoding · Findings: 5 (High 0, Medium 0, Low 5) in 5 files, 2 flows · Needs decision: none
- What is wrong: All 18 XB-STD terms state "1.5 % surcharge per month late" with a penalty period of one month; four reviews flagged it (conditions#F9 gives the extent). Example: `packaging/02-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1` (packaging/02#F7); `utilities/06-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1` (utilities/06#F7).
- Where it comes from: `tools/examples_kit.py` `payment_terms()`: `PenaltyPeriod/DurationMeasure` 1 MON and `PenaltyAmount` for one month (lines 167–171)
- What must be true afterwards: All 18 places encode the surcharge the same way, and the encoding says "per month" (no end of the period, or a note that the amount is per month).
- Fix direction: Drop the duration (preferred by conditions#F9) in `payment_terms()`; one change fixes all 18.
- Depends on / blocks: none
- Touched by: D22 (Bayvarra's standard terms are the second layer: a surcharge per month late on 30 days net).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1e): Bayvarra's surcharge per month late is a penalty period from the day after the due date with no end and no one-month duration, and the penalty amount is the surcharge for each month late (`kit.payment_terms()`; all invoices under `XB-STD` at once).
- Findings: packaging: 02#F7, 04#F7, 07#F7; utilities: 06#F7; consistency: conditions#F9

### C39 · Payment notes that call every document an invoice
- Kind: encoding · Findings: 4 (High 0, Medium 0, Low 4) in 4 files, 2 flows · Needs decision: none
- What is wrong: The payment note of credit notes, debit notes and the deposit asks the payer to quote "invoice …". Example: `furniture/13-CreditNote.xml:/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-CN-26-0579` (furniture/13#F4); `sea/06-OrderResponse.xml:/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice LD-SO-26-0123` (sea/06#F11).
- Where it comes from: `tools/build_examples.py` `account()` (line 611: `PaymentNote`)
- What must be true afterwards: The payment note names the document type it is on.
- Fix direction: Pass the document type into `account()`.
- Depends on / blocks: none
- Touched by: D9 (furniture/14 and sea/28 are re-homed, O6).
- State: ready in part: 2 findings ready (furniture/13#F4, sea/06#F11); furniture/14#F6 waits for D32 and sea/28#F11 for D30 (O6).
- Fixed (2026-11-17, stage 1 step 1c): the payment note names the document it is on (invoice, credit note, debit note, self-billed invoice, deposit on sales order, statement); the build passes the document type to `payment_means()`.
- Findings: furniture: 13#F4, 14#F6; sea: 06#F11, 28#F11

### C40 · Pallets listed as packages contained in themselves
- Kind: encoding · Findings: 3 (High 0, Medium 3, Low 0) in 2 files, 2 flows · Needs decision: none
- What is wrong: Each pallet lists itself as the one package it contains, and the package quantity is used as a number of packages (road/08, retail/12). Example: `retail/12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `PX` (retail/12#F2); `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `KXU104411490000015` (road/08#F15).
- Where it comes from: `tools/examples_kit.py` `handling_units()` (line 1366) and `pallets()` (line 1294)
- What must be true afterwards: A handling unit contains the packages actually on it; quantities count what they say.
- Fix direction: Fix `handling_units()` together with the three-parcel bench of D20 (C69): a bench pallet contains four slat bundles and eight frame cartons.
- Depends on / blocks: with C69 (D20)
- Touched by: D20 (the packages on a pallet are the bench's parcels, which gives `ContainedPackage` its real case; O61).
- State: ready to fix now, together with C69.
- Findings: retail: 12#F2; road: 08#F15, 08#F16

### C41 · `JourneyID` holding a voyage or month instead of the service schedule
- Kind: encoding · Findings: 3 (High 0, Medium 0, Low 3) in 3 files, 2 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: `JourneyID` (the regular service schedule) holds the barge's voyage number and the pipeline's month. Example: `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031` (plastics/04#F21); `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603` (energy/04#F12).
- Where it comes from: `tools/examples_kit.py` `means()` (line 1206); `tools/examples_scenarios.py` line 8698 (pipeline "KG-P1-2603")
- What must be true afterwards: JourneyID only where a scheduled service exists; a voyage number in the element for it.
- Fix direction: Correct the two values.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1d): `JourneyID` only for a scheduled service (the container train in the hub's timetable, the airline's flights, the shipping line's voyages); not for the truck's one-off job (D35), the barge's booked voyage (its number stays in the carrier-assigned ID) or the pipeline's month.
- Findings: energy: 04#F12; plastics: 04#F21, 06#F19

### C42 · A line marked both confidential and internal
- Kind: encoding · Findings: 2 (High 0, Medium 0, Low 2) in 2 files, 2 flows · Needs decision: none
- What is wrong: Lines carry `PrivacyCode` "Confidential" and `SecurityClassificationCode` "Internal" at once, two different levels (furniture/01, wood/01). Example: `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL` (furniture/01#F10); `wood/01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL` (wood/01#F7).
- Where it comes from: `tools/examples_scenarios.py` lines 5227 and 5285 (`SecurityClassificationCode` INTERNAL next to a `PrivacyCode`)
- What must be true afterwards: At most one classification per line, consistent with the other.
- Fix direction: Drop one of the two in the scenario code.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1g): `SecurityClassificationCode` removed from the RFQ lines of the wood and furniture flows (`tools/examples_scenarios.py`).
- Findings: furniture: 01#F10; wood: 01#F7

### C43 · Temperature code given next to a measured value
- Kind: encoding · Findings: 2 (High 0, Medium 2, Low 0) in 2 files, 2 flows · Needs decision: none
- What is wrong: A temperature carries both a measured value and a code that only qualifies it (mast/02, plastics/09). Example: `mast/02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Temperature/cbc:MeasureCode` = `TARGET` (mast/02#F7); `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:Measure` = `5` (plastics/09#F4).
- Where it comes from: `tools/examples_scenarios.py` lines 5392 and 5879 (`MeasureCode` with a value)
- What must be true afterwards: A temperature is either a value with its attribute or a code, as the element defines.
- Fix direction: Drop `MeasureCode` where the value is given.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1g): `MeasureCode` is left out wherever a temperature value is given (`tools/examples_scenarios.py`).
- Findings: mast: 02#F7; plastics: 09#F4

### C44 · `VI-C180-2026` replaces a frame in one catalogue and a bench in a tender
- Kind: encoding · Findings: 1 (High 0, Medium 0, Low 1) in 1 file, 0 flows · Needs decision: none
- What is wrong: The same unresolvable identifier replaces the side frame in retail/02 and the whole bench in tender/15. Example: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026` (items#F4).
- Where it comes from: source not located: the replacement item in the retail catalogue and the tender line (`tools/examples_scenarios.py`)
- What must be true afterwards: A replacement identifier means one item, identified somewhere, of the same kind as the item it replaces.
- Fix direction: Drop it from the tender line; identify the 2026 casting by `VI-C180` + extended ID (items#F4 option a).
- Depends on / blocks: none
- Touched by: D5 (the company's own number `VI-C180` stays the seller's identification; the globally unique form is the Codana prefix plus that number).
- State: ready to fix now.
- Fixed (2026-11-17, stage 1 step 1g): the retail catalogue's frame line names only the item it replaces (`VI-C180`, the side frame of the 2025 casting) as `ReplacedRelatedItem`; the `ReplacementRelatedItem` of the catalogue and of the tender line are gone (`tools/examples_scenarios.py`).
- Findings: consistency: items#F4

### C45 · `Language/LocaleCode` = `en`
- Kind: world rule · Findings: 213 (High 0, Medium 213, Low 0) in 213 files, 15 flows · Needs decision: decided (D1, 2026-11-15)
- Decided: `LocaleCode` carries the regional English of the party's country, `en-XU`, `en-XB` or `en-XL`, from a world locale list (option b). `Language/ID` stays plain `en`. Decision 6b of `analysis/codelist-decisions.md` is revised for `LocaleCode` only. The element stays: the earlier direction to drop it is not followed.
- What is wrong: 213 files carry `LocaleCode` `en` with listID ISO 639: a language, not a locale (Medium in every review). Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en` (contest/01#F1); `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en` (energy/04#F3).
- Where it comes from: `tools/build_examples.py` `party()` (lines 136–141: `LocaleCode` from `identity.language`); `tools/examples_scenarios.py` lines 3930, 4850, 6435, 6939
- What must be true afterwards: Every `LocaleCode` holds the locale of its party's English (`en-XU`, `en-XB` or `en-XL`) from the world locale list; `Language/ID` stays `en`.
- Fix direction: Add the world locale list (three codes, each with what marks the variety, O19) and let `party()` write the party's country as the region of `LocaleCode`. With O19, settle whether a party whose first language is Urvanian or Lisavan also states its English locale.
- Depends on / blocks: none
- Note: The conflict with decision 6b is settled: 6b is revised for `LocaleCode` (`analysis/codelist-decisions.md`, "Revisions of 2026-11-16").
- Not settled by D1 and D11: whether every party description keeps `Language` (see C01).
- State: ready to fix now (213 findings, resolved by the new value).
- Fixed (2026-11-17, stage 2): `LocaleCode` holds the party's English, `en-XU`, `en-XB` or `en-XL`, from the new regional list `Locale` (O19); Urvanian and Lisavan stay plain `qau` and `qal` without a locale. Documents between the countries are in English, so an Urvanian or Lisavan party states English with its own locale there (`party(lang=)`, `international()` in `tools/build_examples.py`); the other `LocaleCode` values of the catalogue request, the digital agreement's reference, the call for tenders and the expression of interest are `en-XB`.
- Findings: air (10): 01#F3, 02#F2, 03#F7, 04#F8, 05#F4 …; contest (16): 01#F1, 02#F1, 03#F2, 04#F1, 05#F1 …; cotton (13): 02#F3, 07#F2, 08#F1, 09#F3, 10#F5 …; energy (6): 04#F3, 05#F3, 06#F2, 07#F3, 08#F2 …; furniture (17): 01#F1, 02#F1, 03#F2, 04#F3, 05#F3 …; mast (5): 01#F2, 02#F2, 03#F3, 04#F1, 05#F2; packaging (9): 01#F2, 02#F1, 03#F1, 04#F1, 05#F1 …; plastics (10): 01#F1, 02#F2, 03#F4, 04#F7, 05#F3 …; rail (6): 01#F2, 02#F5, 03#F8, 06#F10, 08#F13 …; retail (22): 01#F2, 02#F3, 03#F4, 04#F3, 05#F3 …; road (17): 01#F2, 02#F2, 03#F1, 04#F4, 05#F6 …; sea (28): 01#F1, 02#F3, 03#F3, 04#F1, 05#F3 …; tender (36): 01#F5, 02#F6, 03#F6, 04#F2, 05#F2 …; utilities (7): 05#F4, 06#F3, 07#F2, 08#F2, 09#F2 …; wood (11): 01#F1, 02#F2, 03#F2, 04#F2, 05#F1 …. Full list in `analysis/worklist-assignments.csv`.

### C46 · English renderings tagged with the issuer's country, Italian names tagged as English, legal form untagged
- Kind: world rule · Findings: 179 (High 0, Medium 0, Low 179) in 123 files, 15 flows · Needs decision: decided (D2, 2026-11-15)
- Decided: The tag names the English of whoever wrote the text (option b). A party's master data (address, legal form and the like) carries that party's region in every document; free text written for the document carries the issuer's. The Italian names stay English, as the visible trait of Urvanian English. The legal form is tagged like the other renderings. Decision 6b and the sentence of `note/src/03-world.md` are revised.
- Dismissed and resolved (counted by title from `.review/worklist/findings.csv`): 51 findings object only to Italian names tagged as English and are dismissed, because D2 keeps the Italian names as English; 19 object to that and to the region or the legal form, and their Italian part is dismissed; the other 109 are about the issuer's region on a party's renderings or an untagged legal form and are resolved by the rule. Four of the 109 (cotton/02#F7, 07#F6, 08#F7, tender/26#F19) also name item texts, whose tag D2 leaves open (O5).
- What is wrong: The same party's English address is `en-XB` in Bayvarran documents and `en-XU`/`en-XL` in its own (277 of 277 tagged rows follow the issuer); the Italian street names of Urvania are tagged English; the legal form is untagged in one rendering. Example: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato` (carnet/01#F9); `plastics/01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo` (plastics/01#F6).
- Where it comes from: `tools/build_examples.py` `language_tag()` (line 1215: the sender's country as region), `city_names()` (line 420), legal form in `legal_entity()` (lines 284–289)
- What must be true afterwards: A party's address, names and legal form carry that party's region (`en-XU`, `en-XB` or `en-XL`) in every document, the Italian names of Urvania included; free text carries the issuer's region; the legal form is tagged in every rendering.
- Fix direction: In `language_tag()` and `city_names()`, take the region from the party whose master data is written, not from the sender; keep the sender's region for free text; tag the legal form in `legal_entity()`. Item texts keep today's tag until O5 is settled.
- Depends on / blocks: none
- Note: The conflict with decision 6b and `note/src/03-world.md` is settled: both are revised by D2.
- State: ready to fix now.
- Fixed (2026-11-17, stage 2): a party's English master data carries that party's region in every document: the English street and town names of Urvanian and Lisavan addresses (`address()`, `city_names()`) and the legal form, now tagged in every rendering and given in both languages of the party's country (`legal_entity()` and the code-name rendering in `fill()`); free text keeps the issuer's region. Item texts wait for O5.
- Findings: air (14): 02#F7, 02#F8, 03#F13, 03#F14, 05#F7 …; carnet (8): 01#F9, 01#F15, 02#F5, 02#F7, 03#F5 …; contest (2): 15#F14, 16#F14; cotton (14): 02#F7, 02#F8, 07#F6, 07#F7, 08#F7 …; energy (4): 04#F13, 06#F6, 07#F9, 08#F6; mast (4): 02#F14, 03#F14, 04#F11, 05#F7; packaging (2): 02#F5, 09#F4; plastics (12): 01#F6, 01#F7, 02#F6, 03#F6, 04#F9 …; rail (13): 01#F9, 01#F10, 01#F11, 02#F9, 03#F10 …; retail (1): 02#F19; road (25): 01#F14, 01#F15, 02#F10, 03#F11, 03#F12 …; sea (25): 01#F8, 02#F12, 02#F18, 03#F9, 04#F6 …; tender (32): 03#F42, 03#F43, 12#F10, 12#F11, 13#F15 …; utilities (4): 01#F16, 02#F12, 03#F16, 04#F10; wood (19): 01#F4, 02#F6, 02#F7, 02#F8, 03#F4 …. Full list in `analysis/worklist-assignments.csv`.

### C47 · `FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING for a cradle-to-gate footprint
- Kind: world rule · Findings: 74 (High 0, Medium 74, Low 0) in 40 files, 7 flows · Needs decision: decided (D10, 2026-11-16)
- Decided: `FullnessIndicationCode` comes off the product footprint and stays only where a load is described (a full container, `FCL`); the world's `EmissionBoundaryCode` list goes; Q21 is revised for this element (option a). The bench's footprint becomes two emissions that add up to the total: one for `SOURCING` (raw material supply and its transport, EN 15804 A1 and A2) and one for `MANUFACTURING` (A3), each with a stage description that says what it covers.
- What is wrong: The bench's footprint carries a system boundary in an element about full transport equipment, and the stage A3 for a figure from the mine to the gate (74 findings in 40 files). Example: `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE` (road/01#F6); `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE` (tender/25#F10).
- Where it comes from: `world/items.json` bench footprint `stage` "MANUFACTURING" and `fullness` "CRADLETOGATE" (lines 207–211); lists in `world/codelists/lists.json` (lines 6492, 6519)
- What must be true afterwards: No product footprint carries `FullnessIndicationCode`; the bench's footprint is two emissions, `SOURCING` and `MANUFACTURING`, each with a description of what it covers, which add up to the stated total; factor and base multiply out or are absent (C09).
- Fix direction: Remove `fullness` from the bench footprint in items.json and the `EmissionBoundaryCode` list from lists.json; split the emission into the two stages with the figures of O25; the same split for the other items that carry a footprint (O25); in one change with C09.
- Depends on / blocks: with C09
- Note: The conflict with Q21 is settled: Q21 is revised (D10). The missing element for a footprint's system boundary goes to the OASIS write-up (O39).
- State: waits for O25 (the two figures, proposed from typical shares for steel and timber, for the owner to confirm, and whether the total stays 96 kg).
- Findings: carnet (1): 01#F7; rail (6): 01#F5, 01#F6, 06#F7, 06#F8, 11#F2 …; retail (20): 02#F7, 02#F8, 04#F6, 04#F7, 05#F5 …; road (18): 01#F5, 01#F6, 04#F6, 04#F7, 05#F4 …; sea (18): 02#F9, 02#F10, 05#F5, 05#F6, 10#F4 …; tender (10): 25#F9, 25#F10, 26#F7, 26#F8, 29#F5 …; waste (1): 03#F2. Full list in `analysis/worklist-assignments.csv`.

### C48 · Catalogue and product-passport data copied into business documents
- Kind: world rule · Findings: 41 (High 0, Medium 0, Low 41) in 38 files, 8 flows · Needs decision: decided (D11, 2026-11-16)
- Decided: A fact is stated first in the document of the moment it becomes known, and a later document repeats it only if its own transaction uses it; otherwise it identifies the item, the lot or the earlier document (option a, as a rule about when a fact becomes known; "Story lines: What a document says about an item"). The sentence "The maker's facts travel with the item wherever it appears" in `note/src/03-world.md` is replaced.
- What is wrong: The full bench description (properties, emissions, warranty, dimensions, keywords) stands in orders, despatch advices, invoices, customs declarations and till receipts. Example: `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture` (tender/30#F13); `wood/10-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `440799` (wood/10#F5).
- Where it comes from: `tools/build_examples.py` `item()` (line 844) always writes the maker's full item data (brand, properties, certificates, footprint, circularity); customs-relevant item data in `customs_item()` (`tools/examples_kit.py` line 828)
- What must be true afterwards: Each document type carries the item facts of its profile: catalogue, item information and product passport everything about the type and its variants; order and order response the identification, name, variant chosen and anything made to order; despatch and receipt advice the identification, name, lot or serial numbers, handling and dangerous-goods data; invoice and credit note the identification, name and what tax needs; customs declaration the description, commodity code, origin and weights; shopper's receipt the name, brand and warranty.
- Fix direction: Give `item()` a profile per document type, worked out as a table for the owner (O20), and let `customs_item()` write what customs needs.
- Depends on / blocks: none
- Note: The conflict with the world story is settled: the sentence of `note/src/03-world.md` is replaced by D11.
- State: waits for O20 (the profile per document type, as a table for the owner).
- Fixed (2026-11-17, stage 2, after the owner approved the item table O20): every item carries the blocks of its kind of document (`ITEM_KIND`, `ITEM_PROFILE`, `item_profiles()` in `tools/build_examples.py`; the table in `analysis/item-profile.md`): catalogue and offer everything about the type, order the identification with the variant, despatch the lots and dangerous goods, invoice the identification and tax (and the cotton's classing certificate, a lot fact), shopper's receipt the brand and warranty, customs the description, commodity code and origin; what a scenario adds for its transaction stays. 9,179 item elements become 3,508; coverage 4982 → 4971 (O145). The story sentence of `note/src/03-world.md` is rewritten.
- Findings: carnet: 01#F19; packaging: 09#F7; rail: 01#F14, 06#F24, 11#F8; retail: 05#F11, 07#F11, 08#F13, 12#F13, 17#F17, 18#F16, 19#F10, 19#F14, 21#F15; road: 01#F13, 04#F14, 05#F13, 06#F18, 06#F20, 07#F19, 07#F20, 10#F16, 11#F11, 13#F16, 15#F11; sea: 05#F16, 10#F9, 11#F12, 19#F17, 20#F13, 21#F13, 22#F15, 29#F5; tender: 26#F17, 29#F16, 30#F13, 31#F16, 32#F24, 33#F24; wood: 10#F5, 11#F6

### C49 · Signature aggregates with only an ID and a signatory
- Kind: world rule · Findings: 38 (High 0, Medium 1, Low 37) in 38 files, 4 flows · Needs decision: deferred (D6, 2026-11-16)
- Decided: deferred. Signatures become a stage of their own after the story fixes, with real signatures: each signing party gets a key pair and a certificate, and the build signs and verifies. Which documents are signed is decided in that stage (O18). Until then the Signature aggregates stay as they are: none is removed and none is added.
- What is wrong: 137 of 147 Signature aggregates carry only an ID and a signatory party, no method, time or attached signature. Example: `retail/08-Order.xml:/Order/cac:Signature/cbc:ID` = `BM-SIG-26-0424` (retail/08#F17); `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Signature/cbc:ID` = `TWL-SIG-CTR` (sea/16#F24).
- Where it comes from: `tools/examples_kit.py` `tep()` (line 715) and `waybill()` (line 784); `tools/examples_scenarios.py` `full_signature()` (line 4822) and inline signatures (e.g. lines 1006, 1797, 1878)
- What must be true afterwards: Decided in the signatures stage: a Signature exists where the stage's rule says a document is signed, and says what was signed, how and when.
- Fix direction: In the signatures stage (O18): the rule for what is signed, whether Urvania requires signed invoices, the trust model, where the signature is carried, test keys and reproducible signing. Nothing changes before.
- Depends on / blocks: none
- State: waits for the signatures stage.
- Findings: air: 02#F11, 03#F17, 04#F20, 05#F11, 07#F9, 09#F9; retail: 01#F9, 02#F9, 03#F6, 04#F9, 05#F7, 06#F8, 07#F7, 08#F17, 09#F6, 10#F7, 13#F12, 14#F11, 17#F9, 20#F5, 21#F8; sea: 01#F6, 03#F2, 04#F5, 07#F5, 08#F9, 10#F19, 15#F17, 16#F24, 17#F10, 19#F21, 20#F17, 21#F16; utilities: 04#F9, 07#F10, 08#F9, 10#F4, 14#F5

### C50 · Tax category O for goods, 0 % on O, and Lisavu's tax scheme without ID
- Kind: world rule · Findings: 29 (High 0, Medium 6, Low 23) in 13 files, 4 flows · Needs decision: decided (D15, 2026-11-16)
- Decided: option c), and no rate on category `O` anywhere. A Lisavan sale carries no tax section: no `TaxTotal`, no tax category on the line, no tax scheme; its totals state that no tax is due. The island's own taxes keep their section: the presumptive tax withheld on farm produce, and the duty and import consumption tax of the import declarations (D18). `O` stays where it means what it says ("Services outside scope of tax", as for Urvania's services abroad), without a percent.
- What is wrong: Lisavan sales of goods use category O "Services outside scope of tax"; O is given with a 0 % rate and, for levies, with an exemption reason; the Lisavan scheme has a name and no ID. Example: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O` (cotton/01#F2); `utilities/06-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY` (utilities/06#F5).
- Where it comes from: `tools/examples_kit.py` `tax_rule()` (line 72) and `tax_category()` (lines 115–135; scheme name "No general sales tax" without ID, line 133)
- What must be true afterwards: No Lisavan sale has a tax section, and its amounts without tax, with tax and to pay are equal; no `Percent` on category `O`; the scheme "No general sales tax" is gone; the levy's category follows D31.
- Fix direction: In `tax_rule()` and `tax_category()`, write no tax section and no line tax category for a Lisavan seller (the presumptive tax keeps its `WithholdingTaxTotal`) and no percent on `O`. `TaxScheme/TaxTypeCode` keeps its coverage through the withholding scheme `INCOME` of D17 (O45, settled).
- Depends on / blocks: none
- State: ready in part: 22 findings ready; the six levy findings (utilities/06#F4, 06#F5, 09#F8, 09#F9, 11#F6, 11#F7) wait for D31 (O16: D15 leaves the levy to D31 and D17, and D17 does not settle it); sea/28#F15 waits for D30 (O6).
- Fixed (2026-11-17, stage 2, 22 findings): a Lisavan seller's document has no tax section: no `TaxTotal`, no tax category on lines, items or charges, no tax scheme, no tax point date; its totals with and without tax are the same and say why (`untaxed_sales()` in `tools/build_examples.py`); the presumptive tax keeps its `WithholdingTaxTotal`, the customs declarations their duties. Category `O` carries no `Percent` anywhere (`tax_category()` in `tools/examples_kit.py`). The scheme "No general sales tax" is gone, except in sea/28, which waits for D30 (O6); the six levy findings wait for D31 (O16).
- Findings: cotton: 01#F2, 01#F8, 01#F9, 04#F6, 04#F21, 04#F22, 05#F7, 05#F22, 05#F23, 08#F2, 08#F11, 08#F12, 08#F13, 16#F2, 16#F4, 16#F5; road: 14#F12; sea: 28#F15, 29#F2, 29#F13; utilities: 06#F4, 06#F5, 09#F8, 09#F9, 11#F6, 11#F7, 12#F17, 13#F7, 13#F8

### C51 · Contract payment terms never applied by the invoices under the contract
- Kind: world rule · Findings: 12 (High 10, Medium 0, Low 2) in 10 files, 4 flows · Needs decision: decided (D22, 2026-11-16)
- Decided: option a), the contract wins, in three layers: what the parties agreed in a contract or framework agreement; where they agreed nothing, the seller's standard terms (`XU-STD`, `XB-STD`, `XL-STD`); where neither says anything about late payment, the statutory interest of the seller's country. A cross-border sale follows the seller's country unless the contract chooses otherwise. The sentence of `note/src/03-world.md` is rewritten to the three layers.
- What is wrong: The framework transport plans (ore, rail, plastics) say "30 days net from the consignment note" and the tender contract "30 days after each accepted release", but every invoice under them applies XU-STD (30 days from the invoice, 2 % discount, 8 % interest); the reminder and remittance follow. Example: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` (ore/03#F4); `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` (plastics/04#F2).
- Where it comes from: `tools/examples_kit.py` `payment_terms()` (line 150) always applies the seller's country terms; the contracts' own terms in `tep_terms()` (line 646) and the tender `tendering_terms()` (`tools/examples_scenarios.py` line 6283)
- What must be true afterwards: The carriers' invoices under the ore, rail and plastics plans are due 30 days from the consignment note, with no settlement discount and no interest clause of the standard terms; the tender invoice is due 30 days after the accepted release, and late interest is Urvania's statutory 8 % a year from that date; tender/27 quotes the contract; the reminder and the remittance advice follow; standard terms only where no contract terms exist.
- Fix direction: Let `payment_terms()` take the terms of the contract or plan a document belongs to, and the seller's standard terms only where there are none; build check O70.
- Depends on / blocks: none
- Note: The conflict with the world story is settled: the sentence of `note/src/03-world.md` is rewritten (D22).
- State: ready in part: 9 findings ready (ore, rail, plastics and conditions#F3); tender/27#F1, 32#F5 and 35#F1 wait for D28 (O69: the release needs an acceptance with a date before "30 days after each accepted release" gives a due date).
- Fixed (2026-11-17, stage 2, 9 findings): the carriers' invoices under the ore, rail and plastics plans apply the plan's term, "30 days net from the consignment note" (`PLAN_PAYMENT`, `terms_of()` in `tools/examples_kit.py`), with no settlement discount and Urvania's statutory interest for late payment: due 2026-04-09 (ore/06), 2026-05-14 (rail/10) and 2026-05-19 (plastics/07); the farm's advance (cotton/01) is due on issue in all its dates, as the season agreement says. Build check O70. tender/27, 32 and 35 wait for D28 (O69).
- Findings: ore: 03#F4, 06#F1; plastics: 04#F2, 07#F1, 07#F4; rail: 03#F4, 10#F1, 10#F3; tender: 27#F1, 32#F5, 35#F1; consistency: conditions#F3

### C52 · Customs value on a different basis in each flow
- Kind: world rule · Findings: 12 (High 1, Medium 6, Low 5) in 12 files, 6 flows · Needs decision: decided (D16, 2026-11-16)
- Decided: option c), each country values imports on its own basis: Urvania the price paid with freight and insurance to its border (a CIF-type value); Bayvarra the price paid as the goods left the exporting country, without freight and insurance (an FOB-type value); Lisavu the price paid with freight and insurance to the island. In all three, charges that are part of the price paid belong to the value, and a customs value declared on a transport document agrees with the declaration. One rule for all three, which conditions#F5 preferred, is not followed.
- What is wrong: Bayvarra alone values imports on four bases (freight to destination added in plastics, FCA/FOB without freight in road and cotton, a delivered price in tender); document-level charges (colour, pallets) are never in the value; the sea bill of lading declares a CIF value the import declaration does not use. Example: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00` (sea/14#F3); `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000` (tender/30#F4).
- Where it comes from: `tools/examples_kit.py` `goods_items()` (line 844, value = the goods lines of the invoice); `tools/examples_scenarios.py` `cif_value()` (line 1154) and `goods_items()` (line 87)
- What must be true afterwards: Every declaration follows the valuation basis of the country it is lodged in, with the charges that are part of the price paid. By D16: road/10 and cotton/15 stand; plastics/09 drops the river freight; tender/31 deducts the carriage from its delivered price and adds the colour charge; wood/07 adds the pallet charge; energy/05 stays; sea/19 states the landed value, which then agrees with the 53,778.00 lume of the bill of lading; the transit declaration rail/06 follows the country that asks for it.
- Fix direction: Give `goods_items()` the valuation basis of the declaring country (from countries.json) and add the charges that are part of the price; work out with O46 how each delivery term is brought to each basis and which elements carry the value without freight and the freight.
- Depends on / blocks: none
- State: waits for O46 (D16: the WTO Valuation Agreement, Articles 1 and 8, is to be read before implementation).
- Fixed in part (2026-11-17, stage 2, after O46): each declaration values the goods on its country's basis (`VALUATION`, `customs_values()` in `tools/build_examples.py`): wood/05 and 07 include the pallets (34,800.00 lume, 3,480,000 ferra), tender/30 and 31 the colour (2,016,000 ferra, 20,160.00 lume), plastics/05 and 09 leave out the river freight (9,804,600 ferra, 98,046.00 lume), sea/19 adds freight and insurance to the island (21,511.200 coral, the bill of lading's value); the phytosanitary certificate cotton/10 no longer carries a customs value or the classing certificate. road/10, cotton/15 and energy/05 stand. tender/31's deduction of the carriage after the border and rail/06 wait for the distances of the place list (O91).
- Findings: cotton: 10#F9, 15#F4; plastics: 05#F10, 09#F6; rail: 06#F17; sea: 14#F3, 19#F6; tender: 30#F4, 31#F6; wood: 05#F3, 07#F4; consistency: conditions#F5

### C53 · Documents dated at the weekend against a Monday-to-Friday week
- Kind: world rule · Findings: 12 (High 1, Medium 2, Low 9) in 12 files, 6 flows · Needs decision: decided (D27, 2026-11-16)
- Decided: option a), with working days per kind of party (offices and factories Monday to Friday; shops Monday to Saturday; ports, carriers, terminals, border customs and the operations of utilities every day), public holidays per country and state ("Story lines: The calendar", current base), the same week in all three countries, two time zones without summer time (the mainland UTC−01:00, the island UTC+00:00) and times written with their offset. A document is dated on a day its issuer works, unless it says why not.
- What is wrong: By the count of conditions#F7, 48 documents (19 %) are issued on a Saturday or Sunday by offices whose contacts say "Weekdays 08:00–17:00"; contact hours also exclude the times goods are at the border or a ship arrives. Example: `retail/21-PurchaseReceipt.xml:/PurchaseReceipt/cbc:Note` = `Home delivery booked for Saturday.` (retail/21#F2); `tender/09-ProcurementStatus.xml:/ProcurementStatus/cbc:IssueDate` = `2026-02-21` (conditions#F7).
- Where it comes from: the flows' start dates and day offsets in `tools/examples_scenarios.py` (`kit.Flow(…)` lines 25–8894 and the day argument of each document); contact hours in `world/parties.json` (`hours`, e.g. line 28)
- What must be true afterwards: Every document is dated on a working day of its issuer (its kind of party, its country's and state's holidays) or says why not; contacts state the hours of their kind of party; times of documents that cross the zone boundary carry an offset; island addresses carry the offset 0.
- Fix direction: Add the holidays and the time zones to countries.json and the working days per kind of party to parties.json; move or reassign the 48 weekend documents and the few on holidays, each with its flow (O78); build check O79.
- Depends on / blocks: none
- State: ready in part: 9 findings ready; tender/05#F5, 09#F4 and 10#F4 wait for D28 (the tender's dates move with its procedure periods, C125).
- Fixed in part (2026-11-17, stage 2): the calendar is in the world data (holidays per country, state and town; legal times and offsets; a working week per party) and the build checks it (O79, `check_calendar()`); contacts of ports, terminals, carriers, border customs and utilities say every day, those of shops Monday to Saturday (cotton/14#F5, rail/07#F7, road/05#F15, road/10#F14, sea/15#F9); road/07 is issued on Monday morning (road/07#F11); retail/21's delivery is on the Saturday its note names (retail/21#F2); retail/07's note matches its dates (retail/07#F2); issue times carry the issuer's offset. The other weekend and holiday documents of conditions#F7 move with their flows, listed in `CALENDAR_WAITS` (O78).
- Findings: cotton: 14#F5; rail: 07#F7; retail: 07#F2, 21#F2; road: 05#F15, 07#F11, 10#F14; sea: 15#F9; tender: 05#F5, 09#F4, 10#F4; consistency: conditions#F7

### C54 · Bayvarran withholding tax and tax representative only in the tender, and Urvania's "service to a business abroad" for a public body
- Kind: world rule · Findings: 10 (High 0, Medium 2, Low 8) in 5 files, 1 flow · Needs decision: decided (D17, 2026-11-16)
- Decided: option a), in three parts. (1) Bayvarra's withholding of 10 % stays, for public bodies only, and becomes readable from the document: the scheme's name says that it applies to payments by public bodies, the scheme carries the tax type `INCOME`, and the tax representative carries its registration with the tax office. (2) A seller states its own country's tax, a rule for all 250 documents. (3) Urvania's `SVCABROAD` is widened to "a service supplied outside Urvania" (to a customer established abroad, or on land abroad). conditions#F4's preferred option (drop the withholding) is not followed; conditions#F8 is resolved by the wider definition.
- What is wrong: The tender notices state Bayvarran exemption PUBLIC; the winner's invoices apply Urvanian VAT (EXP, SVCABROAD) plus a Bayvarran 10 % withholding on the installation collected through a tax representative, which no other non-resident supplier into Bayvarra has; SVCABROAD ("to a business") is used for the public works department. Example: `tender/35-Reminder.xml:/Reminder/cac:PrepaidPayment/cbc:ID` = `XB-WHT-26-04-1187` (tender/35#F4); `tender/02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC` (conditions#F4).
- Where it comes from: `tools/examples_scenarios.py` `withholding()` (line 2333) and the tender invoices; `tools/examples_kit.py` `tax_rule()` (line 72)
- What must be true afterwards: The department withholds under a named scheme with `TaxTypeCode` `INCOME` on Valdara's installation; the tax representative carries its registration; nothing is withheld on a penalty; `SVCABROAD` means a service supplied outside Urvania; the notices' wording on the Bayvarran exemption does not contradict a foreign bidder's own country's tax (with D28, O13).
- Fix direction: Fix `withholding()` and the tender invoices and reminder; widen `SVCABROAD` in lists.json in English and Urvanian; work out the scheme's name and the representative's registration (O47).
- Depends on / blocks: none
- Note: The story rule of `note/src/03-world.md` stands, as D17 decides.
- State: ready in part: 7 findings ready; tender/34#F7, 34#F8 and 34#F10 wait for D28 (tender/34 is re-homed, O6; D17: nothing is withheld on a penalty).
- Fixed (2026-11-17, stage 2, 7 findings): the withholding scheme is named for what it is, payments by public bodies to non-resident businesses, with `TaxTypeCode` `INCOME` (`withholding_scheme()` in `tools/examples_scenarios.py`); the tax representative carries its registration with the Bayvarran tax office (`tax_representative()`) on the invoice and the credit note, and is gone from the reminder; the credit note's withholding has its subtotal; the reminder no longer lists the withholding as a prepaid payment but says in its note that the balance is net of it; `SVCABROAD` means a service supplied outside Urvania (O47). tender/34 waits for D28.
- Findings: tender: 32#F15, 33#F15, 33#F16, 34#F7, 34#F8, 34#F10, 35#F4, 35#F10; consistency: conditions#F4, conditions#F8

### C55 · Standard terms IDs that do not mean the same number of days everywhere
- Kind: world rule · Findings: 8 (High 8, Medium 0, Low 0) in 8 files, 4 flows · Needs decision: decided (D23, 2026-11-16)
- Decided: option a), with the utility term as a rule of the Accord: utility bills are due 21 days after the bill under one Accord code for all three countries (a name such as `TA-UTIL`, to be fixed); no utility bill cites `XU-STD`, `XB-STD` or `XL-STD`, and no document redefines one of them. The three invoices between Bayvarra and the island follow the seller's standard terms (D22): cotton/16 becomes due in 45 days, mast/05 in 30; sea/22 is settled with the sea flow (O72).
- What is wrong: XU-STD/XB-STD say 30 days and XL-STD 45 days, but the utilities are due in 21 days under all three IDs, and the Bayvarra–Lisavu invoices use the buyer's period under the seller's text. Example: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27` (cotton/01#F1); `mast/05-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-06-04` (mast/05#F1).
- Where it comes from: `tools/examples_kit.py` `payment_terms()` (line 150: due date = issue day + `due_days` passed by each caller); `world/countries.json` `payment` per country; the 21-day utilities calls in `tools/examples_scenarios.py` `utilities()` (line 2998)
- What must be true afterwards: One terms ID, one text, one period wherever it is used; the utility bills carry the Accord's utility code with 21 days; cotton/16 is due 45 days and mast/05 30 days after issue; every due date follows from the terms the document cites.
- Fix direction: Derive `due_days` from the terms, not from the caller; add the Accord's utility code and text (O73); build check O70.
- Depends on / blocks: none
- State: ready in part: 7 findings ready; sea/22#F1 waits for D30 (O72).
- Fixed (2026-11-17, stage 2, 7 findings): every due date follows from the terms the invoice cites (`terms_of()`); the utility bills carry the Accord's `TA-UTIL`, 21 days net from the bill (O73); cotton/16 is due 2026-04-16 (45 days, the ginnery's terms) and mast/05 2026-07-04 (30 days); the electricity remittance no longer takes a discount the utility term does not give. Build check O70 (`check_payment_terms()`). sea/22 keeps its date until O72 (`DUE_DATE_WAITS`).
- Findings: cotton: 01#F1, 16#F1; mast: 05#F1; sea: 22#F1; utilities: 02#F2, 06#F1, 13#F1; consistency: conditions#F2

### C56 · The map scale: all coordinates inside 35 km, against distances and times of hours and days
- Kind: world rule · Findings: 8 (High 4, Medium 0, Low 4) in 7 files, 2 flows · Needs decision: decided (D19, 2026-11-16)
- Decided: neither a) nor b) as written. One map square is 14 km; the mainland is about 560 km from west to east and 390 km from north to south; road and rail distances are taken from the route's length on the map; the island lies about 1,000 km east of Lumeport, in an inset on the map, with its port, airport and town on the lee (east) coast. Position, current base: the mainland at 28.1° to 31.9° South, 17.7° to 12.3° West; the island at 33.0° South, 2.65° West.
- What is wrong: Coordinates are computed from map tiles at 0.01° per tile, so Lumeport and Selanu are 6 km (3.2 nm) apart and the whole world fits in 21 × 32 km, while the documents state two days at sea, a three-hour flight, 186 km by road and a ballast exchange 120 nm off Selanu. Example: `energy/06-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.` (energy/06#F5); `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2` (sea/08#F3).
- Where it comes from: `world/countries.json` `geography.degrees_per_tile` = 0.01 (line 619) and `origin`; `tools/build_examples.py` `coordinate()` (line 510); `world/map.json` tiles
- What must be true afterwards: Coordinates follow 14 km a square from the new origin; every stated distance equals the route's length on the map, and every duration fits the distance and the mode's speed (the sea crossing to Selanu about 42 hours at 13.5 knots, the flight about two hours).
- Fix direction: O82 was settled on 2026-11-16 (the drawing is a diagram; geography from a place list): agree the place list with the owner (O91), redraw what the diagram shows wrongly (O92), then set the origin and the degrees per square in countries.json (O55), draw the island and its inset (O56), and derive distances and durations from the map; build check O60.
- Depends on / blocks: blocks C58; the map rendering on the site uses the same tiles
- Touched by: O82 (found 2026-11-16: at 14 km a square a town's port, airport and companies lie 85 to 140 km apart; the map is redrawn or given two scales "before the scale is implemented").
- State: waits: sea/08#F3, 16#F2, 16#F3 and timelines#F1 for the place list (O91; O82 itself was settled on 2026-11-16); the energy findings on the "four kilometres" to the gas field (energy/04#F8, 05#F8, 06#F5, 07#F8) for D44 (O54).
- Findings: energy: 04#F8, 05#F8, 06#F5, 07#F8; sea: 08#F3, 16#F2, 16#F3; consistency: timelines#F1

### C57 · Duties, import taxes and Trade Accord preference stated nowhere
- Kind: world rule · Findings: 6 (High 1, Medium 2, Low 3) in 5 files, 4 flows · Needs decision: decided (D18, 2026-11-16)
- Decided: option a), worked out per country. Goods of Accord origin are free of duty on proof: every import declaration claims the preference, names the criterion and refers to its proof of origin; goods from outside the Accord pay each country's own tariff; the note "Duties paid by the importer's account at customs." goes from all six declarations. Due at import: in Urvania value added tax of 20 % on the value with freight and insurance to the border; in Bayvarra nothing; in Lisavu the import consumption tax of 10 % on the landed value. D18 also settles O1 and O3.
- What is wrong: Every import says duties were paid without a duty, rate or amount; preference is claimed once (plastics), certified but not claimed in road, ignored elsewhere; the carnet reminder claims 1,300 coral of duties and consumption tax on goods worth 399.20 XLC. Example: `carnet/03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000` (carnet/03#F1); `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P` (conditions#F6).
- Where it comes from: `tools/examples_scenarios.py` `import_extras()` (note "Duties paid by the importer's account at customs.", line 4597); preference only in the plastics import (line 868)
- What must be true afterwards: Each import declaration claims the preference (criterion and proof of origin) and states the tax due at import by its country's rule; none says that duties were paid.
- Fix direction: In `import_extras()`, drop the note and add the preference claim and the import tax per country, in the elements worked out with O49.
- Depends on / blocks: none
- Note: The story and Q24 stand; D18 settles the open question of conditions#F6.
- State: ready in part: 4 findings ready; carnet/03#F1 and 03#F2 wait for D40 (the carnet's timeline; by D18 the tax at stake on the two benches is about 40 coral).
- Fixed (2026-11-17, stage 2, 4 findings): every import declaration claims the Accord's preference per goods item, with the criterion of the goods' origin (`origin_criterion` in `world/items.json`), and refers to its proof: the certificate of origin in road, else the commercial invoice, which now carries the exporter's statement on origin (`origin_statement()` in `tools/examples_kit.py`, `origin_notes()`); it states what is due at import by its country's rule, in the note and as the goods item's tax category: Urvania 20 % VAT on the customs value, Bayvarra nothing, Lisavu 10 % import consumption tax on the landed value (`import_preference()` in `tools/build_examples.py`). The note "Duties paid by the importer's account at customs." is gone. energy/05's proof waits for its dates (O78); carnet/03 waits for D40.
- Findings: carnet: 03#F1, 03#F2; plastics: 09#F7; road: 10#F11; tender: 31#F13; consistency: conditions#F6

### C58 · One sea voyage with four passage times
- Kind: world rule · Findings: 4 (High 2, Medium 1, Low 1) in 3 files, 1 flow · Needs decision: decided (D19, 2026-11-16)
- Decided: covered by D19: the sea crossing to Selanu is about 570 nautical miles, 42 hours at the ship's 13.5 knots.
- What is wrong: Voyage `TH-26-19E` takes two days (service), 64 h (manifest estimate, issued after the actual departure), 84 h (actual) and is 40 nm off Selanu at 13.5 kn on 16 May although it arrives on 18 May. Example: `sea/15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15` (sea/15#F1); `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2` (timelines#F5).
- Where it comes from: `tools/examples_scenarios.py` sea flow (`sea()` line 1527; manifest, status and pre-arrival report dates and times)
- What must be true afterwards: One passage time (38 to 43 hours) in the service description, the manifest, the pre-arrival report and the status messages; the arrival moves earlier (O53).
- Fix direction: Settle the voyage's times with the sea flow (O53, D30), after C56; then derive estimate, position and arrival.
- Depends on / blocks: after C56 (D19, O82) and with D30
- State: waits for D30 (O53).
- Findings: sea: 15#F1, 16#F1, 16#F17; consistency: timelines#F5

### C59 · Lisavu's capital: "Port Wrenfield" in English addresses, "Selanu" in every other English text
- Kind: world rule · Findings: 1 (High 0, Medium 1, Low 0) in 1 file, 0 flows · Needs decision: decided (D3, 2026-11-15)
- Decided: the story stays, with a stated rule (a refinement of option b). Addresses give both names, Lisavan first: Port Wrenfield is the official English name in Lisavu's address register. In running English text everyone writes "Selanu"; party names keep "Selanu". No example changes, except that one document shows both names together outside an address; the rule goes into `note/src/03-world.md`.
- What is wrong: The 12 Lisavan parties' English addresses say Port Wrenfield; about 140 party names, place names and texts say Selanu. Example: `sea/05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[1]` = `Selanu` (parties#F1).
- Where it comes from: `world/countries.json` `english_place_names` ("Selanu": "Port Wrenfield", lines 1711–1713); `tools/build_examples.py` `city_names()` (line 432); party and place names in `world/parties.json`
- What must be true afterwards: Addresses keep both names; one document names Port Wrenfield as Selanu's English name outside an address.
- Fix direction: Add the sentence to one document (D3's option b proposed the business card); confirm that Urvania works the other way round (O29).
- Depends on / blocks: none
- Note: The story is kept (D3); parties#F1 option (a) is not followed.
- State: ready to fix now.
- Fixed (2026-11-17, stage 2): the distributor's business card (sea/01) names Selanu and, in brackets, Port Wrenfield as its name in the island's address register; the rule is in `note/src/03-world.md` (Languages).
- Findings: consistency: parties#F1

### C60 · Default founding date 1996-01-01 and size classes that do not fit the parties
- Kind: master data · Findings: 181 (High 4, Medium 0, Low 177) in 169 files, 15 flows · Needs decision: decided (D4, 2026-11-15)
- Decided: option a), with the founding table under "Story lines" as the current base: each of the 25 parties gets its own founding date, headcount and turnover, tied to the history of the Trade Accord, and the size class follows from the figures. Valdara Industries stays LARGE (3,083 persons, listed on the Ferrano Stock Exchange); the 180 employees and 41 years of tender/13 are put right in the tender flow. Marrowdale Sawmill and Brackenmere Furniture take their founding years from their own tenders, and the sawmill its headcount of 85. D14 corrects the figures of five companies (Lumeway 78 persons, Valdara a turnover of 520 million, Brackenmere 45 persons, Tevaro 2.4 million, Nalevi 2.6 million).
- Resolved elsewhere: the 8 findings on Valdara's size and years (conditions#F12, tender/03#F41, 12#F12, 13#F9, 13#F16, 14#F13, 15#F7, 16#F5) are resolved in the tender flow (O13, D28), not by changing the size.
- What is wrong: 25 unrelated companies were registered on 1 January 1996 and are all SMALL, including both national ports, the state water company, the telecom operator and the rail operator; the sawmill states 85 employees but is SMALL; Valdara is LARGE with 180 persons; operating years contradict the registration (tender/04, 07, 13). Example: `contest/09-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (contest/09#F14); `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (retail/02#F20).
- Where it comes from: `world/parties.json` `identity.legal.founded` = "1996-01-01" for 25 parties (e.g. line 209) with low `headcount`/`turnover`; the size follows from them in `tools/codelists.py` `entity_size()` (line 266)
- What must be true afterwards: Every party's founding date, headcount, turnover and size class are those of the founding table with D14's corrections, and the turnover per person falls in the band for its kind (O30).
- Fix direction: Write the founding table into parties.json, with each party's day and month and the textile mill's size (O21); the size follows by the existing rule; build check O30.
- Depends on / blocks: none
- Not settled by D4 and D5: retail/02#F17 (Codana as a small private limited company): D5 calls Codana a public body, the founding table gives it company figures.
- State: ready in part: 165 findings ready on the current base; 8 wait for D28 (O13); 7 on the ports and the telecom operator (cotton/14#F6, sea/13#F8, mast/01#F11, utilities/12#F11, 13#F4, 14#F7, parties#F2) wait for O17; 1 (retail/02#F17) is not settled.
- Findings: air (10): 01#F11, 02#F9, 03#F15, 04#F18, 05#F9 …; contest (12): 04#F8, 05#F8, 06#F9, 07#F6, 09#F14 …; cotton (19): 01#F4, 02#F5, 03#F9, 04#F16, 05#F18 …; furniture (17): 01#F4, 02#F4, 03#F4, 04#F6, 05#F6 …; mast (6): 01#F11, 01#F12, 02#F12, 03#F13, 04#F9 …; packaging (8): 01#F5, 02#F3, 03#F4, 04#F5, 05#F5 …; plastics (11): 01#F3, 02#F3, 03#F7, 04#F10, 05#F6 …; rail (9): 02#F12, 03#F11, 04#F5, 05#F7, 06#F25 …; retail (10): 02#F17, 02#F20, 11#F7, 12#F16, 13#F11 …; road (10): 01#F9, 03#F7, 04#F10, 05#F11, 08#F21 …; sea (14): 01#F9, 02#F14, 03#F10, 04#F7, 05#F9 …; tender (28): 03#F41, 04#F1, 04#F6, 04#F7, 05#F1 …; utilities (11): 03#F14, 05#F8, 06#F11, 07#F9, 08#F10 …; waste (3): 01#F13, 02#F16, 03#F10; wood (11): 01#F3, 02#F5, 03#F7, 04#F6, 05#F5 …; consistency (2): conditions#F12, parties#F2. Full list in `analysis/worklist-assignments.csv`.

### C61 · World item numbers that are valid GTIN-12s; Valdara's items under Lumeway's GS1 prefix
- Kind: master data · Findings: 76 (High 0, Medium 0, Low 76) in 54 files, 9 flows · Needs decision: decided (D5, 2026-11-15)
- Decided: two systems stay (option a), with the ISO side designed as ISO/IEC 15459 works ("Story lines: Identification, the GS1 way and the Codana way"). The world item numbers (`771…`, `772…`, scheme `urn:ubl-examples:world:item`) go; an item on the Codana side is identified by the company's Codana prefix plus its own part number (`KXU10427B180`), with no check character; Lumeway's GTIN stays as the distributor's own number and names Lumeway, not Codana, as its issuer; no GS1 organisation is a party. ID-Q4 is replaced for item numbers.
- Dismissed and resolved (counted by title): 53 findings on world item numbers that pass as GTIN-12 are resolved by the new form; 21 that object to two "standard" identities of one item (items#F2 and the 20 on Valdara's GTINs in Lumeway's prefix) are dismissed, because the two systems are the story and a distributor giving an imported item its own GTIN is real practice. D5 speaks of "the 76 findings on world item numbers"; by their titles the 76 are these 53 and 21 and the two below.
- What is wrong: The world item numbers have the form and check digit of GTIN-12s in a real US/Canada range; the distributor gives the manufacturer's branded bench and frame GTINs under its own prefix, so one item has two standard identities (items#F2). Example: `packaging/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103` (packaging/01#F8); `retail/04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008` (retail/04#F14).
- Where it comes from: `world/items.json` `standard_id` (e.g. "771020000027", line 44) and the GS1 items of the GS1-convention parties in `world/parties.json` `identification`
- What must be true afterwards: No world item number remains; Codana-side items carry `KXU`, the company number and the company's own reference (at most 20 characters); GS1-side items carry a GTIN from the prefix of the company that numbers them, which is named as issuer; no identifier repeats the digits of another (O22, O32).
- Fix direction: Replace `standard_id` in items.json as O23 lists it; new Codana numbers in order of registration and telephone numbers without relation to an identifier (O22); build checks O22 and O32.
- Depends on / blocks: none
- Note: The conflicts are settled: ID-Q4 is replaced for item numbers and the identification paragraph of `note/src/03-world.md` is rewritten (D5).
- Not settled by D5 and D7: packaging/08#F5 and 09#F8 (the shirt's GTIN under Brightmarket's prefix, not the brand owner's): D5 dismisses the distributor's own GTIN, D7 says that under GS1 rules the brand owner numbers the item; the shirt is the textile mill's item, resold by the store.
- State: ready in part: 74 findings ready; 2 not settled.
- Findings: carnet (1): 01#F20; ore (3): 01#F6, 04#F6, 07#F3; packaging (11): 01#F8, 02#F9, 03#F7, 04#F8, 05#F8 …; plastics (5): 01#F10, 05#F11, 08#F9, 09#F19, 10#F8; rail (3): 01#F15, 06#F26, 11#F12; retail (20): 02#F16, 02#F21, 04#F14, 04#F15, 05#F12 …; road (9): 01#F12, 04#F13, 05#F12, 06#F19, 07#F21 …; sea (20): 02#F16, 02#F20, 05#F17, 05#F18, 10#F17 …; tender (3): 25#F21, 26#F21, 29#F22; consistency (1): items#F2. Full list in `analysis/worklist-assignments.csv`.

### C62 · The maker's brand on the store's own-line garden set
- Kind: master data · Findings: 12 (High 0, Medium 0, Low 12) in 12 files, 1 flow · Needs decision: decided (D7, 2026-11-16)
- Decided: option a), the store's own label under an invented name: the Elderwick Marrow bench and the Elderwick Marrow chair, brand Elderwick (owned by Brightmarket Stores), model Marrow, made by Brackenmere Furniture as the manufacturer party. Bench and chair are separate items, each with its own GTIN from Brightmarket's prefix; the set (one bench and two chairs) is an offer without a GTIN, so the GTIN `9523710000012` goes. Brackenmere's own products keep its brand and GTINs.
- What is wrong: The store sells the set under its own line, but every document gives Brackenmere's brand (furniture, 12 files). Example: `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cbc:Note` = `For the store's own garden line.` (furniture/01#F11).
- Where it comes from: `world/items.json` garden bench set (BF-GS-01) brand, as written by `tools/build_examples.py` `item()`
- What must be true afterwards: Every document of the furniture flow and the shopper's receipt in the retail flow names the brand Elderwick, with Brackenmere as manufacturer; bench and chair are items of their own; the set is an offer, not an item.
- Fix direction: Change the brand and the manufacturer in items.json; give bench and chair their GTINs from Brightmarket's prefix (O23); how the documents carry the offer, the prices and the quantities in SET go with the furniture flow (O9, D32).
- Depends on / blocks: none
- State: ready to fix now for the brand (all 12 findings); the split into bench and chair waits for D32 (O9).
- Findings: furniture: 01#F11, 02#F2, 03#F7, 04#F8, 05#F9, 06#F9, 07#F12, 08#F9, 09#F4, 10#F7, 12#F5, 13#F6

### C63 · Lisavu Cotton Farm: address lines that repeat the structured address, and a yearly expiring registration
- Kind: master data · Findings: 11 (High 0, Medium 0, Low 11) in 6 files, 2 flows · Needs decision: decided (D4, 2026-11-15)
- Decided: the farm's registration keeps its yearly expiry, as a rule of Lisavu's farm register: a grower's registration is renewed each season; the story says so.
- Dismissed: the 5 expiry findings (cotton/01#F7, 03#F6, 04#F26, 05#F27, 06#F7). The 6 address-line findings need no decision.
- What is wrong: The farm's `AddressLine`s repeat the structured address and mix two languages in one line; its commercial-register entry has an expiry date. Example: `cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road` (cotton/04#F25); `sea/29-PurchaseReceipt.xml:/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road` (sea/29#F7).
- Where it comes from: `world/parties.json` Lisavu Cotton Farm (`identity.address` lines, `legal.registration_expires`); `tools/build_examples.py` `legal_entity()` (line 292: "The island renews a farm's registration every year")
- What must be true afterwards: Address lines only where the structured address cannot carry the information; the farm's registration keeps its expiry.
- Fix direction: Fix the address lines in parties.json; keep the expiry and its text.
- Depends on / blocks: none
- State: ready to fix now.
- Findings: cotton: 01#F6, 01#F7, 03#F5, 03#F6, 04#F25, 04#F26, 05#F26, 05#F27, 06#F4, 06#F7; sea: 29#F7

### C64 · Industry classes that leave out what the party does
- Kind: master data · Findings: 9 (High 0, Medium 0, Low 9) in 9 files, 2 flows · Needs decision: decided (D8, 2026-11-16)
- Decided: Selanu Telecom changes to ISIC 6120 (wireless telecommunications); Ferrano Energy and Ferrano Grid keep 3510, because the class names a party's principal activity.
- Resolved and dismissed: the 5 mast findings are resolved; the 4 energy findings (energy/01#F8, 02#F5, 03#F5, 07#F6) are dismissed.
- What is wrong: The mast operator is classified as wired telecommunications; Ferrano Energy's and Ferrano Grid's class covers electricity only, in a gas statement. Example: `mast/01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110` (mast/01#F10); `energy/01-UtilityStatement.xml:/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510` (energy/01#F8).
- Where it comes from: `world/parties.json` `identity.industry` (Selanu Telecom 6110, line 2581; Ferrano Energy and Ferrano Grid 3510)
- What must be true afterwards: Each party's ISIC class is its principal activity; Selanu Telecom is 6120.
- Fix direction: Change Selanu Telecom's `identity.industry` to 6120 in parties.json.
- Depends on / blocks: none
- State: ready to fix now.
- Findings: energy: 01#F8, 02#F5, 03#F5, 07#F6; mast: 01#F10, 02#F13, 03#F15, 04#F10, 05#F13

### C65 · Bale weight of about 227 kg as `PackSizeNumeric`
- Kind: master data · Findings: 7 (High 0, Medium 0, Low 7) in 7 files, 1 flow · Needs decision: decided (D12, 2026-11-16)
- Decided: option a). The pack elements come off the cotton item; the nominal bale weight stays in the item's description; the number of bales is the shipment's package count, with the packaging type "bale"; each bale's real weight is in the weight statement. `PackSizeNumeric` stays covered by the sawmill's bundle of 50 slats.
- What is wrong: `PackQuantity` 1 / `PackSizeNumeric` 227 give the nominal bale weight as a pack size in seven cotton documents. Example: `cotton/10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackQuantity` = `1` (cotton/10#F7).
- Where it comes from: `world/items.json` cotton lint (lines 938–947: `per_package` 227, size "227")
- What must be true afterwards: No pack size on the cotton; the bales are the packages; bale count, per-bale weights and totals agree (27 bales, 6,129 kg, 6,190.29 kg gross; O26).
- Fix direction: Remove the pack size of the cotton lint in items.json and give the shipment the bale count; check O26.
- Depends on / blocks: none
- State: ready to fix now.
- Findings: cotton: 02#F9, 07#F9, 08#F14, 10#F7, 11#F4, 15#F5, 16#F7

### C66 · Debit notes with accounting supplier and customer reversed
- Kind: master data · Findings: 5 (High 5, Medium 0, Low 0) in 5 files, 3 flows · Needs decision: decided (D9, 2026-11-16)
- Decided: neither a) nor b) as written. In this world a debit note is the supplier's addition to an invoice it issued, the counterpart of the credit note. None of the three is one: furniture/14 (the store bills the maker for return transport), sea/28 (the importer passes on a customs inspection cost) and tender/34 (the public buyer claims a contract penalty) are re-homed with their flows (D32, D30, D28): a service the buyer performed becomes an invoice from the buyer, a cost passed on an invoice or a supplier's credit note, a penalty a supplier's credit note or a deduction in the remittance advice. The earlier recommendation to swap the roles is withdrawn.
- What is wrong: In all three debit notes the document number and language tag name the real issuer, but the accounting supplier is the party that is charged; the tender reminder and remittance then enter the debit as a credit. Example: `furniture/14-DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture` (furniture/14#F1); `sea/28-DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution` (sea/28#F1).
- Where it comes from: `world/documents.json` the three DebitNote entries (furniture, sea, tender): `parties` `AccountingSupplierParty` = the party debited
- What must be true afterwards: No buyer issues a debit note; each of the three claims is the document its story needs, with the parties in their UBL roles; tender/35 and 36 follow the re-homed penalty.
- Fix direction: Re-home each of the three with its flow decision (O6); do not swap the roles in documents.json. The world's real debit note comes only from a natural case (O7: demurrage first, waiting time second; not forced).
- Depends on / blocks: none
- State: waits: furniture/14#F1 for D32, sea/28#F1 for D30, tender/34#F1, 35#F3 and 36#F1 for D28 (O6).
- Findings: furniture: 14#F1; sea: 28#F1; tender: 34#F1, 35#F3, 36#F1

### C67 · Side frame classified HS 7325.99 instead of a part of a seat
- Kind: master data · Findings: 5 (High 0, Medium 4, Low 1) in 5 files, 2 flows · Needs decision: decided (D13, 2026-11-16)
- Decided: option a). The spare side frame is a part of a seat, HS 2022 subheading 9401.99, with its CPC class and Urvania's national tariff line adjusted to it (22 documents carry `732599` and `73259990` today). Decision P5 is revised.
- What is wrong: The spare side frame is classified as a general cast article; the reviews say a part of a seat (9401.99). Example: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599` (sea/02#F11); `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599` (retail/02#F24).
- Where it comes from: `world/items.json` side frame `hs` "732599" (line 241), `national_tariff` "73259990" (line 253)
- What must be true afterwards: The frame carries 9401.99, the matching CPC class and Urvania's matching tariff line in every document that carries it.
- Fix direction: After O27, change `hs`, `cpc` and `national_tariff` of the frame in items.json; add the list of the world's items with the reasoning for each HS heading (O31).
- Depends on / blocks: none
- Note: The conflict with P5 is settled: P5 is revised (D13).
- State: waits for O27 (the legal notes to Section XV and Note 1(d) to Chapter 94 are read against the official text before the change).
- Findings: retail: 02#F24; sea: 02#F11, 05#F7, 10#F6, 11#F5

### C68 · Valdara's distributor price equals its public contract price; Lumeway's revised frame price is below cost
- Kind: master data · Findings: 1 (High 0, Medium 0, Low 1) in 1 file, 0 flows · Needs decision: decided (D14, 2026-11-16)
- Decided: option a). Valdara has a list price (499.00, its list `VI-PL-2026`, paid by a direct customer and called the contract price in the tender catalogue) and a distributor price for Lumeway, its distributor since 1996. The price table under "Story lines: Prices along the chain" is the current base: only Valdara's two prices to Lumeway change (bench 499.00 to 399.00, side frame 59.80 to 47.50); the road and rail flows recalculate (road invoice 4,862,160 to 3,887,400 ferra, rail 9,580,800 to 7,660,800 ferra); the tender, retail and sea flows keep their prices. Three rules of thumb are checked by the build.
- What is wrong: Valdara sells to its distributor at the price it tenders to the public buyer in the distributor's own city; the revised frame price is below the purchase price. Example: `road/15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `49900` (conditions#F11).
- Where it comes from: `world/items.json` prices of the bench and frame per seller (Valdara 49900 XUF; Lumeway price list `LD-PL-2026`, revision 58 XBL)
- What must be true afterwards: Prices follow the table; nobody resells below what they paid plus the stated freight; gross margins and turnover per person fall in their bands (O30).
- Fix direction: Change Valdara's two prices to Lumeway in items.json; recalculate the road and rail orders, customs values and payments; the price type list says whether a type includes tax (O28); build check O30. Velumi's shop price (O48) goes with D30, the reason for Lumeway's frame price of 20 May (O15) with D34.
- Depends on / blocks: none
- State: ready to fix now.
- Findings: consistency: conditions#F11

### C69 · The bench as shipped: pallets that do not fit, and a bench lighter than its parts
- Kind: cross-flow story · Findings: 7 (High 1, Medium 3, Low 3) in 6 files, 3 flows · Needs decision: decided (D20, 2026-11-16)
- Decided: option a), the bench ships knocked down, as three parcels: two frame cartons (10.2 kg, and 11.2 kg with the bolt set) and a strapped bundle of five slats (23.0 kg); bench net 43.5 kg, gross 44.4 kg. A pallet of four benches is about 1,850 × 650 × 750 mm and 200 kg; 24 such pallets and the castings pallet fit a 13.6 m trailer, a 40-foot container and a 45-foot rail container, in two layers. New rule: the handling limit of ISO 11228-1 (25 kg for one person; two people together about two thirds of their combined capacity). "One full truck" and "one 40-foot container" stay as kinds of booking.
- What is wrong: Four assembled benches (1800 × 620 × 780 mm) do not fit the 1850 × 650 × 1650 mm pallet, 24 such pallets fit neither the trailer nor a 40-foot container; and the bench weighs less than its five slats and two side frames as other flows ship them. Example: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:Quantity` = `24` (sea/05#F1); `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MeasurementDimension/cbc:Measure` = `13.6` (road/08#F12).
- Where it comes from: `world/items.json` bench dimensions and `gross_kg` 41.5 (line 55); `tools/examples_kit.py` `pallets()` (line 1294) and `handling_units()` (line 1366)
- What must be true afterwards: In the 49 documents that carry the bench, its gross weight is 44.4 kg and the totals built from it follow; pallets have the stated size and contain the parcels; parcel counts stand beside pallet counts (300 parcels on 25 pallets); the pallets' own weight is in consignment and container weights; whatever a person lifts is within the limit, or the documents say how it is moved.
- Fix direction: Give items.json the bench's parts and parcels; fix `pallets()` and `handling_units()` (with C40); package levels, parcel counts, handling instructions and shipping marks (O61); the item physics check (O62).
- Depends on / blocks: none
- State: ready to fix now.
- Findings: rail: 06#F15, 08#F16; road: 08#F12, 08#F17; sea: 05#F1; consistency: equipment#F1, items#F3

### C70 · One melt, one coating batch and one manufacture time for every casting and lot
- Kind: cross-flow story · Findings: 6 (High 3, Medium 0, Low 3) in 4 files, 2 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: All castings carry melt `M-26-0412` although made on 20 March, 10 and 11 May; serials run against manufacture dates; one coating batch for four bench lots; the replacement despatch advice gives the same castings a manufacture date a day later. Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-03190` (air/06#F14); `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cac:AdditionalItemProperty/cbc:Value` = `M-26-0412` (timelines#F2).
- Where it comes from: `world/items.json` coating batch "ZN-26-114" (line 225) and melt "M-26-0412" (line 260); `tools/examples_kit.py` `instances()` (line 355: manufacture time 06:40, serials)
- What must be true afterwards: One melt number per casting day and one coating batch per lot, serials rising with the manufacture date, the same casting with the same data in every document (D21).
- Fix direction: Derive melt, batch and serial from the production record at Valdara (O64), after C71 (timelines#F2 option a).
- Depends on / blocks: after C71 (D21), which may change the lots
- Touched by: D21 (settles O4: serials rise with the manufacture date, each casting day has its own melt number and each lot its own coating batch; the 12 frames shipped by sea are the 12 that came by road, with their March serials; the eight air frames are cast to an urgent order and cross-docked).
- State: ready in part, with C71: 4 findings ready; air/06#F3 and air/08#F4 (the air frames' manufacture date) wait for D39 (O63 takes up their one manufacture date).
- Findings: air: 06#F3, 06#F14, 08#F4, 08#F16; road: 04#F16; consistency: timelines#F2

### C71 · Goods "from the distributor's stock" made days before they leave, and no document moves them
- Kind: cross-flow story · Findings: 4 (High 1, Medium 1, Low 2) in 4 files, 1 flow · Needs decision: decided (D21, 2026-11-16)
- Decided: option a) for the goods that came from stock, and a cross-dock for the urgent air frames. Brightmarket's 24 benches come from the March road lot `VI-LOT-260320`; the island's 96 from the April rail delivery, which gets lot numbers; the 12 frames by sea are the 12 that came by road; the sea export's previous declaration is the import under which those goods entered Bayvarra. The eight air frames are cast for Velumi's order of 11 May and pass through Lumeway's dispatch area without entering its stock. The goods chain becomes world data with a check.
- What is wrong: The retail, sea and air lots are made in Urvania two or three days before Lumeway despatches them from Marrowdale "from stock"; only the road (March) and rail (April) deliveries move goods to Lumeway; the sea export cites the March road import as its previous declaration for goods made in May. Example: `sea/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `LD-IM-26-0161` (items#F1); `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.` (sea/20#F16).
- Where it comes from: the lots and manufacture dates of the sea, air and retail goods: `tools/examples_kit.py` `instances()` (line 355) with the despatch days of `sea()`, `air()` and `retail()` in `tools/examples_scenarios.py`
- What must be true afterwards: Every lot and serial that leaves Lumeway arrived in a documented delivery; Lumeway's benches run 96 in on 25 March, 192 in on 15 April, 24 out on 29 April, 96 out on 13 May, 168 left; stock never goes below zero, nothing leaves before it arrived and nothing is made after it ships (O65).
- Fix direction: Add the production record at Valdara and the stock ledgers of Lumeway, Brightmarket and Velumi to the world data (O64); give the rail delivery its lots; take the lots and the previous declarations from the ledger; build check O65; the air frames with D39 (O63).
- Depends on / blocks: with C70; C12 (sea/11 previous declaration)
- Not settled by D21: the rail flow has no import declaration into Bayvarra (see C12).
- State: ready to fix now (stage 4); the air frames' part of timelines#F4 goes with O63 (D39).
- Findings: sea: 20#F16, 29#F11; consistency: items#F1, timelines#F4

### C72 · Documents that report or cite what happens after their own issue time
- Kind: generator mechanism · Findings: 38 (High 30, Medium 1, Low 7) in 32 files, 9 flows · Needs decision: none (5 findings marked "yes" go to D46)
- What is wrong: Issue times are spread pseudo-randomly between 08:00 and 18:00, so waybills report pickups in the afternoon of their morning issue, status reports cite waybills issued later, a cancellation follows its replacement, and revisions are dated after the issue (ten flows; 30 High). Example: `energy/01-UtilityStatement.xml:/UtilityStatement/cbc:IssueDate` = `2026-04-02` (energy/01#F5); `utilities/08-UtilityStatement.xml:/UtilityStatement/cbc:IssueTime` = `15:10:00` (utilities/08#F8).
- Where it comes from: `tools/build_examples.py` main loop: `IssueTime` from a hash of flow and number when the scenario gives none (lines 1704–1707); the days and times set per document in `tools/examples_scenarios.py`
- What must be true afterwards: No document reports as actual, or cites, anything dated after its issue time; transport documents are issued at the moment their type implies.
- Fix direction: Derive issue times from the events and references of the flow (issue after the latest event or document cited), with the scenario overriding; build check: no actual event or referenced document after the issue timestamp (`check_consistency.py` group 10 already lists them).
- Depends on / blocks: none
- Note: Includes timelines#F6 (export declarations after the goods left) and #F8.
- Touched by: D27 (times carry their offset; a document is dated on a working day of its issuer), D24 (numbers follow the final issue times, so this cause comes before C74), D9 (sea/28 is re-homed, O6).
- State: ready in part: 35 findings ready; air/09#F2 (the missed flight) waits for D39, retail/12#F4 (the delivery day) for D34, sea/28#F3 for D30 (O6).
- Findings: air: 04#F4, 05#F1, 07#F1, 08#F1, 09#F2, 10#F5; energy: 01#F5; plastics: 06#F1; rail: 05#F1, 08#F3, 08#F5; retail: 03#F1, 04#F1, 04#F8, 06#F1, 09#F1, 10#F1, 12#F4, 16#F5; road: 04#F1, 08#F1, 08#F3, 09#F1, 10#F1, 14#F1, 16#F1; sea: 03#F1, 13#F1, 22#F2, 28#F3; tender: 17#F2, 18#F1, 19#F1, 19#F2; utilities: 08#F8; consistency: timelines#F3, timelines#F6, timelines#F8

### C73 · References to documents under IDs no document has, or to documents the flow does not contain
- Kind: generator mechanism · Findings: 27 (High 20, Medium 3, Low 4) in 25 files, 8 flows · Needs decision: owner: D38
- What is wrong: References carry IDs no example carries: an air order that does not exist, the call for tenders under a file number in eight tender documents, replaced notices for first notices, a consignment ID as document reference; others point to documents the flow does not model (waste weight statement, furniture delivery note, retail transport plan). Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0319` (air/03#F1); `tender/15-Tender.xml:/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT` (tender/15#F1).
- Where it comes from: reference values in the scenario code: the air order `VT-PO-26-0319` (`tools/examples_scenarios.py` `air()`, line 1940), the tender call for tenders `PWD-2026-PARKS-CFT` and replaced notices (tender enrichments, lines 6476–6560), the waste weight statement (`waste()`, line 2512)
- What must be true afterwards: Every reference to an example resolves to it; a reference to a document outside the examples says what it is.
- Fix direction: Wrong IDs: correct them (no decision). Missing documents: decide per flow whether to add them (D38). Build check: `flow_index.py`'s "-> ?" references reported by the build.
- Depends on / blocks: none
- Touched by: D38 (open) itself says that the correctable wrong IDs need no decision; D24 (the corrected references take the new numbers in stage 5).
- State: D38 decided 2026-11-16; ready: the 20 wrong IDs are corrected, four documents are added (waste/04, furniture/19, retail/23, tender/40), the ore references stay typed references to documents outside the examples.
- Findings: air: 03#F1, 06#F1, 08#F2; furniture: 09#F1; ore: 02#F10, 03#F15; rail: 07#F1, 09#F4; retail: 01#F1, 06#F2, 14#F1, 18#F12; sea: 13#F3; tender: 01#F3, 02#F3, 02#F4, 03#F3, 03#F4, 06#F1, 13#F13, 15#F1, 17#F1, 18#F2, 19#F4, 24#F2, 28#F1; waste: 02#F1

### C74 · Document numbers: one counter per flow shared by all issuers
- Kind: generator mechanism · Findings: 10 (High 2, Medium 1, Low 7) in 8 files, 3 flows · Needs decision: decided (D24, 2026-11-16)
- Decided: option a), with numbers that reflect the size of the business. Each issuer numbers its own documents, per kind of document, rising with the time of issue across all flows; a document's number follows from its date and the issuer's estimated yearly volume, so the examples show a sample of each sequence with gaps. Every reference, every creditor reference built from an invoice number and every signature identifier follows; three payers no longer share a remittance number. The styles differ by country and kind of company ("Story lines: Who numbers how"): Urvanian invoices and credit notes numbered within the year (`2026/0920`), numeric ranges for large companies, code, kind and year for mid-sized companies, year and number for small ones, file references for public bodies.
- What is wrong: Every flow uses one block of consecutive numbers shared by all its issuers, so no issuer numbers its own documents in order (Lumeway's invoice of 30 April is 0236, of 14 May 0147); the same remittance number is used by three payers in utilities; the department's numbers run against its issue times. Example: `road/06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1` (road/06#F22); `utilities/07-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316` (utilities/07#F1).
- Where it comes from: `tools/examples_kit.py` `Flow.number()` (lines 52–57: `{initials}-{type}-26-{base + count}`, `base` from a CRC of the flow name)
- What must be true afterwards: Per issuer and kind of document, numbers rise with the issue timestamp across flows, in the issuer's style; no number is shared by two issuers.
- Fix direction: One counter per issuer and kind in `Flow.number()`, built in global issue order, with the volumes and formats of O75.
- Depends on / blocks: after C72 and the flow decisions (D24: numbers follow time, after the documents that cite later ones, the sea voyage and the tender dates are final; one of the last things implemented)
- State: waits: implemented after stage 6 (D24).
- Findings: road: 06#F22, 07#F23; tender: 06#F9, 22#F6; utilities: 01#F15, 07#F1, 07#F3, 14#F1, 14#F3; consistency: identifiers#F2

### C75 · Issuer prefixes: `BF` for two parties, second prefixes for signatures
- Kind: generator mechanism · Findings: 4 (High 0, Medium 1, Low 3) in 3 files, 1 flow · Needs decision: decided (D25, 2026-11-16)
- Decided: option a), designed with D24: each company has one short code of its own, chosen and held in the world data, not derived from its initials; it appears only where the company's numbering style has a prefix, and then for everything the company numbers; one code per kind of thing within a company. The codes of "Story lines: Who numbers how" are the current base (Lumeway `LMW`, Bayforth `BYF`, Marrowdale Sawmill `MDS` and the others). Signature identifiers take the company's code when the signatures stage comes.
- What is wrong: Bayforth Forwarding and Brackenmere Furniture both get `BF` (invoices, items, signatures, RF references); seven parties sign under a second prefix; one prefix-plus-infix stands for two kinds of document. Example: `tender/04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI` (tender/04#F10); `cotton/17-Invoice.xml:/Invoice/cbc:ID` = `BF-INV-26-0211` (identifiers#F1).
- Where it comes from: `tools/examples_kit.py` `initials()` (line 36); hard-coded signature prefixes in the scenarios (e.g. "BM-SIG", "PWD-SIG", "HS-SIG")
- What must be true afterwards: Every code belongs to one company and is unique in the world; a company uses one code; one code means one kind of thing; creditor references follow the new invoice numbers with recalculated check digits.
- Fix direction: Enter the codes in parties.json (O75) and drop `initials()`; rebuild the creditor references from the invoice numbers.
- Depends on / blocks: with C74
- State: waits: identifiers#F1 and #F5 with C74 (after stage 6); tender/04#F10 and 10#F5 (signature prefixes) for the signatures stage.
- Findings: tender: 04#F10, 10#F5; consistency: identifiers#F1, identifiers#F5

### C76 · `ProfileExecutionID` is the flow name in all 250 documents
- Kind: generator mechanism · Findings: 1 (High 0, Medium 1, Low 0) in 1 file, 0 flows · Needs decision: decided (D26, 2026-11-16)
- Decided: option a), one identifier per collaboration: `ProfileExecutionID` identifies one run of a process between the same parties, assigned by the party that starts it in its own numbering style and repeated by every later document of that transaction; a document that belongs to no collaboration carries none. The earlier decision and the sentence of `note/src/03-world.md` are revised.
- What is wrong: One execution ID per flow joins unrelated collaborations and documents of different profiles. Example: `packaging/01-Order.xml:/Order/cbc:ProfileExecutionID` = `PACKAGING-2026-01` (identifiers#F3).
- Where it comes from: `tools/build_examples.py` main loop (lines 1701–1703: `{FLOW}-2026-01`)
- What must be true afterwards: Each `ProfileExecutionID` identifies one collaboration and is repeated by every document of it; documents sharing one share the parties and refer to each other.
- Fix direction: List the collaborations of each flow (O77) and write the identifier from that list in the main loop; build check of O77.
- Depends on / blocks: with C74, after the flow decisions (which documents each flow keeps)
- Note: The conflict with the earlier decision is settled: `analysis/codelist-decisions.md` and `note/src/03-world.md` are revised (D26).
- State: waits: implemented after stage 6, with C74.
- Findings: consistency: identifiers#F3

### C77 · Waste flow: a transboundary notification for a movement inside one town; no weighbridge statement
- Kind: flow story · Findings: 19 (High 1, Medium 6, Low 12) in 3 files, 1 flow · Needs decision: owner: D42
- What is wrong: The notification and movement are addressed to the customs administration's border office for a movement inside Ferrano; Rinova is named a disposal facility in a recovery notification; 38–40 t of bagged PE in one road load; the planned shipment reuses the first movement's IDs; the weight statement the movement and the invoice rest on does not exist; the invoice bills gross tonnes. Example: `waste/01-WasteNotification.xml:/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage` (waste/01#F12).
- Where it comes from: `tools/examples_scenarios.py` `waste()` (line 2512) and `waste_shipment()` (line 2502)
- What must be true afterwards: The flow tells one plausible domestic (or transboundary) story with the competent authority, a recovery facility, plausible loads and a traceable billed net weight.
- Fix direction: Decide D42 (domestic vs transboundary, weight statement added).
- Depends on / blocks: none
- Touched by: D38 (the weight statement is one of the documents D38 proposes to add), D11 (the net weight is stated first in the weight statement), O66 (the flow decision starts with its goods balance: production waste to the recycler); C12's waste/02#F4 goes with this cause.
- State: D42 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D42).
- Findings: waste: 01#F1, 01#F2, 01#F4, 01#F5, 01#F6, 01#F7, 01#F12, 01#F14, 02#F2, 02#F3, 02#F5, 02#F7, 02#F8, 02#F10, 02#F11, 02#F17, 03#F1, 03#F5, 03#F6

### C78 · Carnet flow: counterfoils, time limits and the duty claim
- Kind: flow story · Findings: 20 (High 2, Medium 4, Low 14) in 4 files, 1 flow · Needs decision: owner: D40
- What is wrong: The carnet as issued shows all four counterfoils stamped; transit through Bayvarra has no transit counterfoils; proof is requested before the re-exportation time limit; the proof does not identify the carnet; contact and office names vary. Example: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cbc:IssueDate` = `2026-05-25` (carnet/01#F1).
- Where it comes from: `tools/examples_scenarios.py` `carnet()` (lines 2485 and 3761)
- What must be true afterwards: The carnet's counterfoils, dates and claims follow one timeline.
- Fix direction: Decide D40 (the timeline of the fair and the re-export; the duty claim goes with D18).
- Depends on / blocks: none
- Touched by: D18 (at 10 % the import consumption tax at stake on the two benches is about 40 coral; the claim of 1,300 coral is more than three times their value; C57's carnet/03#F1 and #F2 go with this cause), D20 (the benches travel as parcels).
- State: D40 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D40).
- Findings: carnet: 01#F1, 01#F2, 01#F5, 01#F8, 01#F12, 01#F14, 01#F16, 01#F17, 01#F18, 01#F22, 01#F23, 02#F1, 02#F4, 03#F8, 03#F9, 04#F1, 04#F4, 04#F9, 04#F10, 04#F11

### C79 · Mast flow: dangerous-goods data of the battery, detector and stripper consignment
- Kind: flow story · Findings: 36 (High 2, Medium 13, Low 21) in 5 files, 1 flow · Needs decision: owner: D36
- What is wrong: Placard notation 7 for an excepted package; the fissile aggregate for a non-fissile americium source; the activity of one detector for ten; placard endorsements that repeat the class or the label model; orange plates for air; crates over the PI 965 IA limit; road transport data in orders and invoices. Example: `mast/01-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7` (mast/01#F1).
- Where it comes from: `world/items.json` dangerous-goods data of SE-BAT-48100, SE-SMK-10, SE-CS-05; `tools/build_examples.py` `hazardous_item()` (line 772); `tools/examples_scenarios.py` `mast_consignment()` (line 5736)
- What must be true afterwards: The DG data follow the air rules the world states, per package, and appear only in transport documents.
- Fix direction: Decide D36 for the yes-findings (crate weights, CAO, endorsements); the rest are encoding fixes in items.json and `mast_consignment()`.
- Depends on / blocks: none
- Touched by: D20 (the handling limit: a crate a person lifts stays within 25 kg, or the documents say how it is moved), D8 (Selanu Telecom is ISIC 6120), O11 (the ionisation smoke detector set, from D7).
- State: D36 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D36); the coverage it costs is won back by O124 and O126.
- Findings: mast: 01#F1, 01#F3, 01#F4, 01#F5, 01#F6, 01#F7, 02#F1, 02#F5, 02#F6, 02#F8, 02#F9, 02#F18, 02#F19, 02#F20, 02#F21, 02#F22, 02#F23, 03#F2, 03#F6, 03#F7, 03#F19, 03#F20, 03#F21, 04#F3, 04#F4, 04#F13, 04#F14, 04#F15, 04#F16, 05#F3, 05#F4, 05#F5, 05#F9, 05#F10, 05#F11, 05#F12

### C80 · Mast flow: the air waybill and the ULDs
- Kind: flow story · Findings: 6 (High 0, Medium 1, Low 5) in 3 files, 1 flow · Needs decision: owner: D36
- What is wrong: The air waybill has no airports or flight date and two numbers; the consignor's instructions carry the carrier's ULD numbers and positions; reefer and food settings without reason; the CPT place is "mast site". Example: `mast/02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AirFlowPercent` = `40` (mast/02#F17).
- Where it comes from: `tools/examples_scenarios.py` `mast()` (line 5862) and `mast_consignment()` (line 5736)
- What must be true afterwards: The waybill identifies the flight; instructions carry what the consignor knows.
- Fix direction: With D36.
- Depends on / blocks: none
- Touched by: D19 and D27 (the flight is about two hours; the island's times are UTC+00:00).
- State: D36 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D36); the coverage it costs is won back by O124 and O126.
- Findings: mast: 01#F8, 02#F16, 02#F17, 03#F5, 03#F9, 03#F18

### C81 · Ore flow: monthly call-off, plan "as requested", bonus and moisture
- Kind: flow story · Findings: 7 (High 1, Medium 0, Low 6) in 5 files, 1 flow · Needs decision: owner: D45
- What is wrong: The monthly call-off is typed as a plain order; the plan is confirmed "as requested" but differs; weekly vs monthly quantities; bonus and penalty neither applied nor excluded; moisture deduction without basis. Example: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cbc:DocumentStatusCode` = `Confirmed` (ore/03#F3).
- Where it comes from: `tools/examples_scenarios.py` `ore()` (line 37)
- What must be true afterwards: The ore call-off, plan and invoice tell one agreement.
- Fix direction: Decide D45 (the train's arrival, bonus or penalty).
- Depends on / blocks: none
- Touched by: D22 (the carrier's invoices follow the framework's "30 days net from the consignment note", C51), D9 (waiting time is the second candidate for the world's real debit note, O7; the bonus is not one), D19 (the ore train runs about 154 km), O66 (ore to steel to castings).
- State: D45 decided 2026-11-17; ready to implement as decided (see `analysis/worklist-decisions.md`, D45).
- Findings: ore: 01#F4, 02#F4, 02#F5, 03#F3, 06#F4, 06#F5, 07#F2

### C82 · Energy flow: 2400 MWh exported to Montebrio, sold to Ferrano Energy, imported by nobody
- Kind: flow story · Findings: 9 (High 4, Medium 4, Low 1) in 3 files, 1 flow · Needs decision: owner: D44
- What is wrong: The export declaration consigns 39200 MWh to Montebrio Power; 2400 MWh are invoiced to Ferrano Energy and have no import declaration; the import declares 36800 MWh under the same shipment ID; gas declared as dry bulk; no period or crossing point. Example: `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK` (energy/04#F4).
- Where it comes from: `tools/examples_scenarios.py` energy declarations (`ENERGY` flow, line 8672 ff.)
- What must be true afterwards: Each buyer's gas is exported and imported under declarations that match its invoice.
- Fix direction: Decide D44 (split by buyer; Ferrano Energy's import).
- Depends on / blocks: none
- Touched by: D19 (O54: the "four kilometres" to the gas field are derived from the map; C56's energy findings go with this flow), D16 (energy/05 stays as it is), O83 (whether the energy protocol's separation of networks from supply applies to Bayvarra and the island).
- State: D44 decided 2026-11-17; ready to implement as decided (see `analysis/worklist-decisions.md`, D44); the coordinates with O55.
- Findings: energy: 04#F1, 04#F2, 04#F4, 04#F5, 05#F1, 05#F5, 05#F6, 05#F12, 07#F1

### C83 · Energy flow: isolated slips
- Kind: flow story · Findings: 8 (High 1, Medium 2, Low 5) in 5 files, 1 flow · Needs decision: none
- What is wrong: Statement payable 0 for a billed consumption; network-use lines that cannot be told apart; the reminder in lume for a ferra debt; the surcharge line without its invoice and period; the plant's InformationURI is the home page. Example: `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example` (energy/04#F9).
- Where it comes from: `tools/examples_scenarios.py` energy flow (line 8672 ff.) and `utility_statement()` (line 2708)
- What must be true afterwards: Each slip corrected in place.
- Fix direction: Fix in the energy scenario.
- Depends on / blocks: none
- Touched by: D22 (energy/08: a cross-border sale follows the seller's country, as the reminder already does).
- State: ready to fix now.
- Findings: energy: 01#F1, 02#F1, 02#F2, 04#F9, 05#F9, 08#F1, 08#F8, 08#F9

### C84 · Packaging flow: isolated slips
- Kind: flow story · Findings: 5 (High 0, Medium 0, Low 5) in 4 files, 1 flow · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: Goods-in point without its GLN; a note referring to a consignment note the document does not identify; no package count; a promotion discount missing on a till receipt; a tax statement in an item description. Example: `packaging/05-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport` (packaging/05#F7).
- Where it comes from: `tools/examples_scenarios.py` `packaging()` (line 3396)
- What must be true afterwards: Each slip corrected.
- Fix direction: Fix in the packaging scenario.
- Depends on / blocks: none
- Touched by: D11 (packaging/08#F4: a tax statement is no fact of the item).
- State: ready to fix now.
- Findings: packaging: 05#F7, 06#F3, 06#F8, 08#F4, 09#F6

### C85 · Air flow: the missed-flight story and the CPT order change
- Kind: flow story · Findings: 13 (High 2, Medium 0, Low 11) in 8 files, 1 flow · Needs decision: owner: D39
- What is wrong: "Goes on the next day's flight" but the cargo arrives the same day; the cancelled despatch advice contains nothing the missed flight changed; the replacement says nothing it replaces; CPT next to "the rest stays CIF"; the buyer names the carrier. Example: `air/07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.` (air/07#F2).
- Where it comes from: `tools/examples_scenarios.py` `air()` (lines 1940 and 3612)
- What must be true afterwards: One consistent story of which flight was missed and when the goods flew.
- Fix direction: Decide D39 (preferred by air/07#F2: an evening flight on 13 May was missed).
- Depends on / blocks: C72 (order of cancellation and replacement)
- Touched by: D27 (a flight leaving Lumeport at 07:00 lands in Selanu at 10:00 island time after two hours), D21 (O63: the eight air frames are an urgent order cross-docked at Lumeport, with one manufacture date, the road leg from Ferrano and the customs treatment across Bayvarra; C70's and C72's air findings go with this cause).
- State: D39 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D39).
- Findings: air: 01#F5, 01#F6, 02#F4, 02#F6, 04#F10, 04#F11, 05#F6, 07#F2, 07#F3, 07#F7, 08#F8, 09#F6, 10#F14

### C86 · Air flow: packing, consolidation and charges of the castings
- Kind: flow story · Findings: 10 (High 3, Medium 2, Low 5) in 3 files, 1 flow · Needs decision: owner: D39
- What is wrong: The box cannot hold the eight frames; gross minus net leaves 5.6 kg for skid, box and bags; "not consolidated" with a house waybill; a warehouse as substitute carrier; two waybill numbers; freight invoiced on gross instead of chargeable weight. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cbc:Quantity` = `8` (air/03#F2).
- Where it comes from: `tools/examples_scenarios.py` `air_consignment()` (line 1892)
- What must be true afterwards: Packing, consolidation and charges agree across the air documents.
- Fix direction: With D39 (consolidation story); the arithmetic fixes need none.
- Depends on / blocks: none
- Touched by: D20 (a spare side frame is one frame carton of 10.2 kg), D21 (O63), D19 (O58: the freighter's range).
- State: D39 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D39).
- Findings: air: 03#F2, 03#F9, 04#F2, 04#F6, 04#F7, 04#F13, 04#F14, 04#F17, 10#F1, 10#F6

### C87 · Plastics flow: barge waybill and goods data
- Kind: flow story · Findings: 15 (High 2, Medium 4, Low 9) in 4 files, 1 flow · Needs decision: owner: D41
- What is wrong: The barge's CO2e is a hundredth of what its diesel produces; the freight rate as base amount; net volume of solid PE; returnable quantity counts bags; one package for 120 bags; lot IDs differ between waybill and despatch advice; standard VAT on international carriage. Example: `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Fiumella Barges` (plastics/04#F1).
- Where it comes from: `tools/examples_scenarios.py` `plastics()` (line 824), `barge_goods()` (line 751), `barge_consignment()` (line 801)
- What must be true afterwards: The barge documents describe the bags and the voyage consistently.
- Fix direction: Encoding fixes; plastics/07#F5 (VAT on carriage of exports) goes to D41.
- Depends on / blocks: none
- Touched by: D16 (plastics/09 drops the river freight from the customs value), D18 (the preference claim), O66 (granulate to film to packed goods).
- State: D41 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D41).
- Findings: plastics: 04#F1, 04#F8, 06#F2, 06#F7, 06#F8, 06#F9, 06#F10, 06#F11, 06#F13, 06#F14, 06#F16, 07#F5, 08#F4, 08#F5, 08#F6

### C88 · Plastics flow: recycled-content certificate issued by a chamber of commerce
- Kind: flow story · Findings: 5 (High 0, Medium 0, Low 5) in 5 files, 1 flow · Needs decision: owner: D41
- What is wrong: Five documents give a chamber of commerce as issuer of a recycled-content certificate. Example: `plastics/08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce` (plastics/08#F8).
- Where it comes from: `world/parties.json` / `world/items.json` certificate of the PE granulate (issuer the Ferrano chamber); `tools/build_examples.py` certificates (line 987)
- What must be true afterwards: The certificate's issuer is a body that can certify recycled content.
- Fix direction: Decide D41.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: D41 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D41).
- Findings: plastics: 01#F11, 05#F12, 08#F8, 09#F18, 10#F7

### C89 · Wood flow: slat units and isolated slips
- Kind: flow story · Findings: 10 (High 1, Medium 0, Low 9) in 5 files, 1 flow · Needs decision: owner: D43
- What is wrong: "Quoted per thousand slats" against a price per slat; `OrderableUnitFactorRate` 50 while quantities are single slats; two sets of terms without saying which governs; pallets charged but in no goods description; resale exemption without certificate. Example: `wood/02-Quotation.xml:/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.` (wood/02#F1).
- Where it comes from: `tools/examples_scenarios.py` `wood()` (line 3176), `quotation()` (line 3164)
- What must be true afterwards: One unit for quoting, ordering and invoicing; charges match the goods described.
- Fix direction: Decide D43 (the orderable unit).
- Depends on / blocks: none
- Touched by: D12 (the bundle of 50 slats is the world's pack of one item; the order for 4,800 slats is 96 bundles), O10 (the two levels of the slat bundle), O66 (4,800 slats make 960 benches against about 330 benches shipped), D16 (wood/07 adds the pallet charge to the customs value).
- State: D43 decided 2026-11-17; ready to implement as decided (see `analysis/worklist-decisions.md`, D43).
- Findings: wood: 02#F1, 02#F4, 02#F12, 02#F13, 02#F16, 03#F10, 06#F12, 08#F10, 08#F14, 11#F5

### C90 · Rail flow: container train documents
- Kind: flow story · Findings: 33 (High 3, Medium 6, Low 24) in 8 files, 1 flow · Needs decision: owner: D37
- What is wrong: Terminal operator as network manager; the hub as destination instead of the siding; passenger quantity 0; demurrage under a vessel definition; the second container without wagon, places and events; one framework contract under two identifiers; the container "being stored" while on the train. Example: `rail/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0` (rail/03#F20).
- Where it comes from: `tools/examples_scenarios.py` `rail()` (lines 659 and 3522), `rail_container()` (line 487), `rail_stage()` (line 565), `rail_consignment()` (line 605)
- What must be true afterwards: Both containers described alike; roles and places as the rail leg has them.
- Fix direction: Encoding fixes; the yes-findings (roles of the hub, CMR vs CIM, Container Convention) go to D37.
- Depends on / blocks: none
- Touched by: D9 (demurrage after five days' free time is the first candidate for the world's real debit note, O7), D21 (the April rail delivery gets lot numbers and supplies the island's 96 benches), D22 (the carrier's invoices follow the framework), D20 (96 knocked-down benches per container), D14 (the rail invoice is recalculated); C30's rail/08#F1 goes with this cause.
- State: D37 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D37); the train times wait for the place list (O54, O91).
- Findings: rail: 02#F3, 02#F13, 03#F3, 03#F14, 03#F15, 03#F20, 03#F21, 04#F2, 04#F3, 04#F6, 04#F7, 05#F2, 05#F4, 05#F5, 05#F8, 06#F14, 06#F18, 06#F22, 07#F4, 07#F8, 08#F8, 08#F10, 08#F15, 08#F17, 08#F18, 08#F19, 08#F21, 08#F22, 08#F24, 08#F25, 09#F1, 09#F6, 09#F7

### C91 · Utility statement builder: average amount, supplier consumption, subscriber data
- Kind: flow story · Findings: 30 (High 3, Medium 9, Low 18) in 6 files, 2 flows · Needs decision: owner: D31
- What is wrong: AverageAmount holds the month's amount; SupplierConsumption for a single supplier; SubscriberID holds the contract number; the item's subscriber type is a utility type; district-heating elements for electricity and water; empty descriptions. Example: `utilities/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120` (utilities/01#F12); `energy/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `61200` (energy/01#F4).
- Where it comes from: `tools/examples_scenarios.py` `utility_statement()` (line 2708), `consumption_line()` (line 2665), `telecom_consumption()` (line 2891)
- What must be true afterwards: The statement elements are used by their definitions in all six statements (also energy/01).
- Fix direction: Fix `utility_statement()`; D31 for the yes-findings (subscriber data, consumer level).
- Depends on / blocks: none
- Touched by: D23 (utility bills are due 21 days after the bill under one Accord code, O73), D15 (O16).
- State: D31 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D31).
- Findings: energy: 01#F4; utilities: 01#F3, 01#F5, 01#F9, 01#F12, 01#F13, 01#F14, 03#F3, 03#F7, 03#F8, 03#F10, 03#F11, 03#F15, 05#F1, 05#F3, 05#F9, 05#F10, 05#F12, 05#F13, 08#F4, 08#F5, 08#F7, 08#F12, 08#F14, 08#F16, 08#F17, 12#F9, 12#F14, 12#F20, 12#F21

### C92 · Utilities: the telecom statement and invoice
- Kind: flow story · Findings: 15 (High 4, Medium 5, Low 6) in 3 files, 1 flow · Needs decision: owner: D31
- What is wrong: 35 GB stated twice (roaming and pool); a masked number shown in full; allowances ignored in line totals; one month invoiced as "6 months"; quantities that mix minutes, gigabytes and views. Example: `utilities/12-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:InvoicedQuantity` = `6` (utilities/12#F19).
- Where it comes from: `tools/examples_scenarios.py` `telecom_consumption()` (line 2891)
- What must be true afterwards: The telecom statement adds up and uses its elements by definition.
- Fix direction: Fix in `telecom_consumption()`; D31 for the yes-findings.
- Depends on / blocks: none
- Note: Possibly not a problem for utilities/13#F2 and 14#F2 (blockchain identifier): `note/src/03-world.md` says "Coral net, the island's clearing, settles tokenised deposits on the Bank of Selanu's ledger".
- Touched by: D12 and D15 (O16: "Mobile data beyond the subscription, per gigabyte" with a pack of 5 gigabytes and a pack size of 7; the island's telephone bill carries no tax section), D23 (O73).
- State: D31 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D31).
- Findings: utilities: 12#F1, 12#F2, 12#F3, 12#F4, 12#F6, 12#F7, 12#F8, 12#F15, 12#F18, 12#F19, 12#F22, 13#F2, 13#F9, 13#F10, 14#F2

### C93 · Utilities: the household's water on account, the mandate and the levy
- Kind: flow story · Findings: 13 (High 2, Medium 3, Low 8) in 5 files, 1 flow · Needs decision: owner: D31
- What is wrong: The statement says the household pays on account monthly; invoice 09 bills and collects the full amount; the mandate is limited to 12 instructions; payable amounts leave out the sewage levy; the reminder and credit note lack references. Example: `utilities/08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.` (utilities/08#F1).
- Where it comes from: `tools/examples_scenarios.py` `utilities()` (line 2998), `levy()` (line 2538)
- What must be true afterwards: One billing scheme for the household from statement to credit note.
- Fix direction: Decide D31 (preferred by utilities/08#F1: drop the on-account scheme).
- Depends on / blocks: none
- Touched by: D15 (O16: the levy coded `O` with `LEVY`; C50's six levy findings go with D31), D23 (O73).
- State: D31 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D31).
- Findings: utilities: 05#F5, 08#F1, 08#F6, 09#F1, 09#F3, 09#F4, 09#F7, 10#F7, 10#F8, 10#F10, 11#F3, 11#F5, 11#F8

### C94 · Utilities: excise and estimate-correction amounts
- Kind: flow story · Findings: 7 (High 6, Medium 1, Low 0) in 3 files, 1 flow · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: The energy tax report carries the excise of the whole invoice in each statement; totals leave out the excise; per-unit amounts do not produce the excise; the estimate correction double-counts and its unit amount × quantity is not the amount. Example: `utilities/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840` (utilities/01#F1).
- Where it comes from: `tools/examples_scenarios.py` `energy_tax()` (line 2576) and the estimate correction in `utility_statement()` (line 2708)
- What must be true afterwards: The statements of one invoice add up to the invoice; excise arithmetic holds.
- Fix direction: Fix the arithmetic (preferred options of utilities/01#F1, F2, 02#F1); build check for the tier arithmetic.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: ready to fix now.
- Findings: utilities: 01#F1, 01#F2, 02#F1, 02#F3, 03#F1, 03#F2, 03#F5

### C95 · Utilities: isolated slips
- Kind: flow story · Findings: 7 (High 1, Medium 2, Low 4) in 6 files, 1 flow · Needs decision: owner: D31
- What is wrong: Castrano named as subscriber of Valdara's subscription; OriginatorParty for the warehouse occupant; a one-time charge type for a monthly item; a tax point date on a reminder without tax. Example: `utilities/03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics` (utilities/03#F6).
- Where it comes from: `tools/examples_scenarios.py` `utilities()` (line 2998)
- What must be true afterwards: Each slip corrected.
- Fix direction: Fix in the scenario; utilities/03#F6 (who subscribes) goes to D31.
- Depends on / blocks: none
- Touched by: D23 (O73).
- State: D31 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D31).
- Findings: utilities: 01#F6, 02#F5, 02#F7, 03#F6, 04#F2, 08#F13, 10#F3

### C96 · Qualification requests and responses (ESPD-like) in contest and tender
- Kind: flow story · Findings: 32 (High 1, Medium 11, Low 20) in 8 files, 2 flows · Needs decision: owner: D29
- What is wrong: The buyer's request sets the fulfilment indicator; no exclusion grounds; responses that do not refer to the request; evidence not linked; the same text as description and value; groups whose other member is not encoded; expected values that are thresholds; "all criteria answered" with one answer. Example: `contest/06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF` (contest/06#F3); `tender/07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:Note` = `All criteria answered.` (tender/07#F1).
- Where it comes from: `tools/examples_scenarios.py` `qualification_limits()` (line 6709) and the QualificationApplicationRequest/Response enrichments (lines 6592–6839)
- What must be true afterwards: Requests ask, responses answer, linked to each other and to evidence.
- Fix direction: Fix the shared qualification builders; yes-findings with D29.
- Depends on / blocks: none
- Touched by: D4 (the headcounts, founding years and sizes that qualification responses state follow the founding table).
- State: D29 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D29).
- Findings: contest: 05#F3, 05#F10, 06#F3, 06#F4, 06#F5, 06#F12, 06#F13, 06#F14, 07#F5, 10#F1, 10#F8, 11#F1, 11#F4, 11#F6, 11#F7, 11#F8, 11#F9, 12#F5; tender: 06#F4, 06#F5, 06#F6, 06#F7, 06#F8, 06#F13, 06#F14, 06#F15, 06#F16, 07#F1, 07#F4, 07#F5, 07#F6, 07#F7

### C97 · Procurement notices (contest and tender): notice types, defaults, languages, links
- Kind: flow story · Findings: 31 (High 0, Medium 6, Low 25) in 14 files, 2 flows · Needs decision: owner: D29
- What is wrong: Design-contest notices use the standard-procedure notice types CN and CAN; the requested legal form applies to the follow-up contract; the reference criterion's DurationPeriod is the look-back window; CandidateReductionConstraintIndicator says the candidates are reduced; PublishAwardIndicator without its situation; Urvanian declared as a notice language without Urvanian text; calls that do not link the contract notice. Example: `contest/03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD` (contest/03#F7); `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:NoticeLanguageCode` = `en` (tender/01#F14).
- Where it comes from: `tools/examples_scenarios.py` `notice_head()` (line 6476), `tendering_process()` (line 6220), contest helpers (lines 8894–8943)
- What must be true afterwards: Notice coding follows the procedure type (design contest vs open procedure).
- Fix direction: Encoding fixes in the shared notice builders; the yes-findings with D29.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: D29 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D29).
- Findings: contest: 03#F1, 03#F7, 03#F8, 03#F10, 04#F10, 04#F11, 04#F12, 04#F13, 05#F11, 08#F1, 08#F8, 08#F9, 08#F11, 09#F7, 09#F9, 09#F10, 09#F13, 10#F9, 15#F3, 15#F13, 16#F2, 16#F13; tender: 01#F14, 02#F18, 02#F27, 03#F27, 03#F44, 12#F7, 21#F5, 21#F18, 24#F3

### C98 · Contest: the design team, references, prizes and versions
- Kind: flow story · Findings: 24 (High 1, Medium 4, Low 19) in 13 files, 1 flow · Needs decision: owner: D29
- What is wrong: The first prize of 6,000 contradicts the 8,000 of the notice; the winning team is reduced to its lead; one completed task where two references are required; requests addressed to one participant before selection; version 2 documents do not say what they change. Example: `contest/15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:Description` = `First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.` (contest/15#F2).
- Where it comes from: `tools/examples_scenarios.py` `contest_version()` (line 8901), `contest_prizes()` (line 8910), `contest_awarding()` (line 8943)
- What must be true afterwards: The contest tells one story of the team, the criteria and the prize correction.
- Fix direction: Decide D29.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: D29 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D29).
- Findings: contest: 02#F3, 04#F3, 04#F7, 05#F7, 05#F12, 06#F11, 07#F1, 07#F4, 07#F8, 09#F8, 09#F12, 10#F7, 11#F5, 12#F1, 12#F6, 13#F3, 13#F4, 14#F3, 14#F4, 14#F5, 15#F1, 15#F2, 16#F1, 16#F11

### C99 · Contest: the estimated contract amount of 54,000 lume
- Kind: flow story · Findings: 8 (High 0, Medium 0, Low 8) in 8 files, 1 flow · Needs decision: owner: D29
- What is wrong: What the estimate covers is not stated, and it stays the same after the first prize rose. Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00` (contest/01#F6).
- Where it comes from: `tools/examples_scenarios.py` `contest_project()` (line 8924)
- What must be true afterwards: The estimate says what it covers and follows the prize change, or is absent.
- Fix direction: Decide with D29.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: D29 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D29).
- Findings: contest: 01#F6, 02#F7, 03#F11, 04#F14, 08#F12, 09#F11, 15#F12, 16#F12

### C100 · Road flow: isolated slips of the truck shipment
- Kind: flow story · Findings: 25 (High 1, Medium 6, Low 18) in 10 files, 1 flow · Needs decision: owner: D35
- What is wrong: Gross volume smaller than its handling units; journey ID for a one-off trip; required and latest delivery times disagree; notes that narrate the example; trailer seal only in a remark; package level "inner"; a recount with one package more. Example: `road/08-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossVolumeMeasure` = `41.5` (road/08#F2).
- Where it comes from: `tools/examples_scenarios.py` `road()` (line 195), `road_stage()` (line 109), `road_consignment()` (line 139)
- What must be true afterwards: Each slip corrected.
- Fix direction: Encoding fixes; the yes ones with D35.
- Depends on / blocks: none
- Touched by: D19 (O54: the road distances 186 km and 38 km are derived from the map; Ferrano to Marrowdale is about 182 km), D20 (the load becomes 24 pallets of knocked-down benches and the castings pallet), D9 (O8: the extra box of side frames is settled with D35), D14 (the road invoice is recalculated).
- State: D35 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D35); the distance waits for the place list (O54, O91).
- Findings: road: 01#F10, 01#F11, 02#F4, 02#F5, 03#F5, 03#F9, 08#F2, 08#F11, 08#F13, 08#F14, 08#F18, 08#F24, 08#F25, 08#F26, 08#F28, 08#F29, 08#F30, 09#F10, 09#F11, 12#F1, 13#F8, 13#F15, 14#F11, 16#F11, 17#F8

### C101 · Road flow: application and certificate of origin
- Kind: flow story · Findings: 14 (High 4, Medium 4, Low 6) in 3 files, 1 flow · Needs decision: owner: D35
- What is wrong: Application and certificate share ID and version; a second endorsement before the first; the buyer's order number as job number; an embassy endorsement by the Trade Accord Council; endorsers' signatory contacts against their definition. Example: `road/06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office` (road/06#F16).
- Where it comes from: `tools/examples_scenarios.py` road certificate of origin documents (`road()` line 195; enrichment `road()` line 3676)
- What must be true afterwards: Application and certificate are two documents with their own IDs, endorsements in order.
- Fix direction: Decide D35 for the endorsement roles; the rest are encoding fixes.
- Depends on / blocks: none
- Touched by: D18 (the import declaration claims the preference and refers to the certificate as proof of origin), D27 (the certificate dated on a working day of its issuer).
- State: D35 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D35); the distance waits for the place list (O54, O91).
- Findings: road: 06#F1, 06#F3, 06#F7, 06#F15, 06#F16, 06#F17, 07#F1, 07#F6, 07#F9, 07#F10, 07#F16, 07#F17, 07#F18, 10#F3

### C102 · Road flow: the substituted 2026 casting
- Kind: flow story · Findings: 8 (High 0, Medium 1, Low 7) in 7 files, 1 flow · Needs decision: owner: D35
- What is wrong: The order response replaces the old casting by the 2026 casting, but despatch, certificates, receipt and invoice do not identify it (extended ID `2026`); the proposed substitute is the old casting; an extra frame is accepted but never billed. Example: `road/07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180` (road/07#F25).
- Where it comes from: `tools/examples_scenarios.py` `road()` (line 195): the substitute line of the order response and the follow-up lines
- What must be true afterwards: The 2026 casting is identified the same way from the response to the invoice.
- Fix direction: Carry the extended ID through; road/13#F9 (the extra frame) with D35.
- Depends on / blocks: none
- Touched by: D9 (O8), D5 (the 2026 casting is identified by `VI-C180` with an extended ID, C44).
- State: D35 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D35); the distance waits for the place list (O54, O91).
- Findings: road: 02#F6, 04#F15, 07#F25, 10#F21, 11#F12, 13#F9, 13#F18, 15#F13

### C103 · Furniture flow: quotation, orders, invoice, return and credit
- Kind: flow story · Findings: 27 (High 0, Medium 1, Low 26) in 9 files, 1 flow · Needs decision: owner: D32
- What is wrong: Optional cushions only in a note; the initial order twice the target inventory; a repeat order while stock suffices; sub-line prices without quantities; a restocking deduction on a return the maker asked for; the quotation used as a contract. Example: `furniture/12-InstructionForReturns.xml:/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-04-29` (furniture/12#F1).
- Where it comes from: `tools/examples_scenarios.py` `furniture()` (lines 3268 and 3685), `set_parts()` (line 3224)
- What must be true afterwards: Order, stock and return figures follow the replenishment profile and the story.
- Fix direction: Decide D32.
- Depends on / blocks: none
- Touched by: D7 (Elderwick; bench and chair are separate items and the set is an offer, O9; the care kit's content, O10), D9 (furniture/14 is re-homed, O6; C14's, C26's and C39's furniture/14 findings and the quotation used as a contract in furniture/11 go with this cause).
- State: D32 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D32: the Marrow line is a dining set).
- Findings: furniture: 01#F2, 01#F7, 01#F8, 01#F9, 02#F3, 02#F8, 08#F5, 08#F6, 08#F7, 08#F8, 08#F10, 09#F3, 09#F7, 09#F9, 10#F3, 10#F4, 10#F5, 10#F10, 10#F11, 11#F3, 11#F4, 12#F1, 12#F3, 13#F2, 13#F3, 13#F5, 14#F5

### C104 · Furniture flow: the replenishment and sales-reporting documents
- Kind: flow story · Findings: 21 (High 0, Medium 10, Low 11) in 5 files, 1 flow · Needs decision: owner: D32
- What is wrong: Request lines that ask for activity, forecast and metric at once; a replenishment owner that describes a division of work; exception status codes for shipments used for sales; one four-week figure where weekly ones were requested; the weather as an activity property. Example: `furniture/03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode` = `SALES` (furniture/03#F1).
- Where it comes from: `tools/examples_scenarios.py` `furniture()` (lines 3268 and 3685), `collab()` (line 3263)
- What must be true afterwards: Each collaboration document uses its elements by definition, one kind of criterion per line.
- Fix direction: Decide D32 for the yes-findings; encoding fixes otherwise.
- Depends on / blocks: none
- Touched by: D7 (O9: the quantities in SET in the exception criteria).
- State: D32 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D32: the Marrow line is a dining set).
- Findings: furniture: 03#F1, 03#F3, 04#F1, 04#F2, 04#F7, 04#F9, 05#F1, 05#F2, 05#F7, 05#F8, 06#F5, 06#F6, 06#F7, 06#F8, 07#F1, 07#F2, 07#F3, 07#F4, 07#F5, 07#F10, 07#F11

### C105 · Furniture flow: the department's desks and installation
- Kind: flow story · Findings: 10 (High 0, Medium 0, Low 10) in 3 files, 1 flow · Needs decision: owner: D32
- What is wrong: A packaging-disposal charge the order does not contain; a zero tax total without category; the place of work named only; an hourly price without base quantity. Example: `furniture/15-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax` (furniture/15#F5).
- Where it comes from: `tools/examples_scenarios.py` `furniture()` documents 15–17
- What must be true afterwards: Invoice and work report bill what was ordered.
- Fix direction: Decide with D32.
- Depends on / blocks: none
- Touched by: D17 (a Bayvarran seller invoices the department with `PUBLIC`).
- State: D32 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D32: the Marrow line is a dining set).
- Findings: furniture: 15#F3, 15#F5, 16#F4, 16#F6, 16#F8, 16#F10, 16#F12, 17#F4, 17#F6, 17#F7

### C106 · Cotton flow: self-billing between ginnery and farm, and the mill's forecasts
- Kind: flow story · Findings: 26 (High 1, Medium 4, Low 21) in 6 files, 1 flow · Needs decision: owner: D33
- What is wrong: A customs broker as tax representative of a domestic purchase; invoice periods before the delivery; references that say nothing; a charge whose text calls it an allowance; the farm as payee of a credit that flows to the ginnery; "twenty per cent more" is 25 %. Example: `cotton/03-DeliveryNote.xml:/DeliveryNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26` (cotton/03#F3).
- Where it comes from: `tools/examples_kit.py` `self_billed()` (line 1115); `tools/examples_scenarios.py` `cotton()` (line 2082)
- What must be true afterwards: The self-billed documents and forecasts tell one season agreement.
- Fix direction: Decide D33 for the yes-findings.
- Depends on / blocks: none
- Touched by: D15 (a Lisavan sale has no tax section; the presumptive tax stays), D23 (cotton/16 is due in 45 days), O66 (seed cotton to lint).
- State: D33 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D33: the flow moves into the harvest).
- Findings: cotton: 02#F2, 03#F3, 04#F5, 04#F9, 04#F10, 04#F12, 04#F13, 04#F14, 04#F18, 04#F19, 04#F20, 05#F5, 05#F6, 05#F9, 05#F10, 05#F13, 05#F14, 05#F15, 05#F16, 05#F20, 05#F24, 05#F25, 06#F5, 06#F6, 07#F1, 07#F8

### C107 · Cotton flow: classing and phytosanitary certificates
- Kind: flow story · Findings: 15 (High 5, Medium 1, Low 9) in 7 files, 1 flow · Needs decision: owner: D33
- What is wrong: A forecast carries a classing certificate signed 18 days later; a downgrade cites a certificate that says Middling and is signed later; "10 bales sampled out of 80" for 27 bales; a version 1 with a previous version from last season; a phytosanitary certificate issued by a chamber of commerce. Example: `cotton/02-Forecast.xml:/Forecast/cbc:IssueDate` = `2026-02-02` (cotton/02#F1).
- Where it comes from: `tools/examples_scenarios.py` `cotton()` (line 2082), certificate documents 10 and their references
- What must be true afterwards: Certificates exist before they are cited and describe the shipment.
- Fix direction: Decide D33 (who issues the phytosanitary certificate).
- Depends on / blocks: none
- Touched by: D11 (the classing grade and moisture are lot facts, stated first in the certificate).
- State: D33 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D33: the flow moves into the harvest).
- Findings: cotton: 02#F1, 05#F2, 05#F21, 07#F11, 10#F1, 10#F2, 10#F3, 10#F4, 10#F6, 10#F8, 10#F15, 10#F17, 11#F6, 14#F3, 15#F7

### C108 · Cotton flow: the sea export (bill of lading, VGM, pre-arrival report)
- Kind: flow story · Findings: 13 (High 2, Medium 3, Low 8) in 8 files, 1 flow · Needs decision: owner: D33
- What is wrong: The original bill goes to a bank while the instructions ask for the forwarder; the bank as mortgage holder without any financing; "freight collect" while the forwarder invoices freight; the VGM without method or date; the pre-arrival report not tied to the shipment. Example: `cotton/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129` (cotton/11#F5).
- Where it comes from: `tools/examples_scenarios.py` `cotton()` (line 2082), `bl_distribution()` (line 4418)
- What must be true afterwards: The sea documents follow the instructions and one payment arrangement.
- Fix direction: Decide D33 (documentary collection or not).
- Depends on / blocks: none
- Touched by: D12 (O26: 27 bales, 6,129 kg, 6,190.29 kg gross), C15.
- State: D33 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D33: the flow moves into the harvest).
- Findings: cotton: 08#F9, 09#F1, 11#F5, 12#F1, 12#F2, 12#F4, 13#F1, 13#F3, 13#F7, 14#F4, 15#F6, 17#F2, 17#F5

### C109 · Cotton flow: classing results carried as the applicant's remarks
- Kind: flow story · Findings: 7 (High 0, Medium 0, Low 7) in 7 files, 1 flow · Needs decision: none
- What is wrong: The classing results stand in the applicant's `Remarks` in seven documents. Example: `cotton/10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.` (cotton/10#F10).
- Where it comes from: `tools/examples_scenarios.py` cotton certificate (`cotton()` line 2082)
- What must be true afterwards: The results are in the certificate's own elements.
- Fix direction: Move them (encoding).
- Depends on / blocks: none
- Touched by: D11 (classing results are lot facts, stated first in the certificate's own elements).
- State: ready to fix now.
- Findings: cotton: 02#F11, 07#F12, 08#F16, 10#F10, 11#F11, 15#F11, 16#F9

### C110 · Retail flow: catalogue request, catalogue, updates and deletion
- Kind: flow story · Findings: 15 (High 3, Medium 4, Low 8) in 5 files, 1 flow · Needs decision: owner: D34
- What is wrong: A request for an update of a catalogue that exists nowhere; a "new" catalogue that supersedes a version; references to the catalogue with wrong issue and revision times; the update line pointing to the bench for the frame; "Unchanged." as trading terms. Example: `retail/03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.` (retail/03#F9).
- Where it comes from: `tools/examples_scenarios.py` retail catalogue enrichments (lines 3847–3990), `catalogue_update_head()` (line 3951)
- What must be true afterwards: The catalogue versions and their references agree.
- Fix direction: Decide D34 (new catalogue vs update).
- Depends on / blocks: none
- Touched by: D14 (O15: the reason for Lumeway's side-frame price of 20 May), D5 (GTINs); C73's retail/01#F1 goes with this cause.
- State: D34 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D34: the reopening of the department); the travel time waits for the place list (O54, O91).
- Findings: retail: 01#F3, 01#F7, 01#F10, 02#F2, 02#F5, 02#F13, 02#F14, 03#F2, 03#F3, 03#F9, 03#F12, 04#F5, 04#F12, 20#F1, 20#F4

### C111 · Retail flow: promotion, forecast, inventory and the shop sale
- Kind: flow story · Findings: 13 (High 2, Medium 2, Low 9) in 4 files, 1 flow · Needs decision: owner: D34
- What is wrong: The forecast's promotion reference resolves nowhere; a store-opening event nothing supports; the promotion price valid for another period than the promotion; planned sales at the regular price; sale IDs encode 18 May for a purchase on 15 May. Example: `retail/05-Forecast.xml:/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `BM-RE-26` (retail/05#F1).
- Where it comes from: `tools/examples_scenarios.py` `retail()` (lines 953 and 3628), `promo_allowance()` (line 909)
- What must be true afterwards: The promotion has one period and one price chain from event to receipt.
- Fix direction: Decide D34 for the yes-findings.
- Depends on / blocks: none
- Touched by: D14 (shop price 749.00, promotion 674.10, the sales tax added at the till), D27 (shops work Monday to Saturday).
- State: D34 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D34: the reopening of the department); the travel time waits for the place list (O54, O91).
- Findings: retail: 05#F1, 05#F10, 06#F5, 06#F6, 06#F7, 06#F11, 06#F13, 06#F14, 07#F10, 07#F14, 21#F3, 21#F7, 21#F12

### C112 · Retail flow: isolated slips
- Kind: flow story · Findings: 12 (High 1, Medium 2, Low 9) in 5 files, 1 flow · Needs decision: owner: D34
- What is wrong: Purchase-card data capability described as the e-document channel; the invoice bills 24 benches against a receipt of 23; a tax point date without event; the factor as payee of a credit owed to the buyer. Example: `retail/18-Invoice.xml:/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5` (retail/18#F2).
- Where it comes from: `tools/examples_scenarios.py` `retail()` (lines 953, 3628)
- What must be true afterwards: Each slip corrected.
- Fix direction: With D34.
- Depends on / blocks: none
- Note: Possibly not a problem for retail/22#F7 (full card number and CVV in the webshop order): `note/src/03-world.md` says "A webshop order is different: the card is not at hand, so the order carries the full number, the card's dates and its security code".
- Touched by: none of D1 to D27.
- State: D34 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D34: the reopening of the department); the travel time waits for the place list (O54, O91).
- Findings: retail: 08#F5, 08#F8, 08#F12, 10#F4, 18#F2, 18#F10, 18#F11, 18#F13, 19#F2, 22#F2, 22#F5, 22#F7

### C113 · Retail flow: the delivery to the store (carrier references, arrival day)
- Kind: flow story · Findings: 12 (High 3, Medium 2, Low 7) in 6 files, 1 flow · Needs decision: owner: D34
- What is wrong: Three different carrier references for one shipment; the shipping-document reference points to the request; "on its way, expected 29 April 14:00" but received 30 April 10:40; "late" for a slot no document agreed. Example: `retail/13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217` (retail/13#F2).
- Where it comes from: `tools/examples_scenarios.py` `retail()` documents 11–17
- What must be true afterwards: One carrier reference and one delivery day across the transport documents.
- Fix direction: Decide D34 (the delivery day; merge decision Medium/yes).
- Depends on / blocks: none
- Touched by: D27 (working days and times with offsets), D19 (O54: the 38 km to the store); C72's retail/12#F4 goes with this cause.
- State: D34 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D34: the reopening of the department); the travel time waits for the place list (O54, O91).
- Findings: retail: 12#F10, 12#F11, 13#F2, 14#F2, 14#F6, 15#F1, 15#F4, 16#F4, 17#F4, 17#F8, 17#F12, 17#F14

### C114 · Sea flow: bill of lading and ship reports
- Kind: flow story · Findings: 21 (High 3, Medium 7, Low 11) in 5 files, 1 flow · Needs decision: owner: D30
- What is wrong: One SSCC for the frames pallet and a box; the bill's total invoice amount is the goods value; the final delivery party is the buyer, not its 3PL; the road chassis still attached on board; crew lists of 3 of 14; a WHO affected area; the port company issuing sanitation certificates. Example: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254` (sea/14#F1).
- Where it comes from: `tools/examples_scenarios.py` `sea_consignment()` (line 1222), `sea_equipment()` (line 1171), `bl_extras()` (line 4403)
- What must be true afterwards: The bill and the ship reports describe the shipment and the ship consistently.
- Fix direction: Decide D30 for the yes-findings.
- Depends on / blocks: none
- Touched by: D19 (O53: one passage time of 38 to 43 hours; the arrival moves earlier), D27 (the island is on UTC+00:00), D20 (pallets of parcels), D21 (the island's 96 benches come from the April rail delivery).
- State: D30 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D30); the voyage's figures wait for the place list (O91, O53).
- Findings: sea: 13#F7, 14#F1, 14#F4, 14#F5, 14#F6, 14#F7, 14#F8, 15#F7, 15#F8, 16#F6, 16#F7, 16#F8, 16#F13, 16#F14, 16#F15, 16#F16, 16#F18, 16#F20, 16#F21, 17#F2, 17#F9

### C115 · Sea flow: isolated slips
- Kind: flow story · Findings: 20 (High 2, Medium 3, Low 15) in 11 files, 1 flow · Needs decision: owner: D30
- What is wrong: A booking deadline already past when the service is offered; weekly sailing day Friday against a Thursday sailing; a service classified with a goods code; the rejected frame not identified; the full-container discount not applied; the on-carriage leg 19–21 May dated nowhere (timelines#F7). Example: `sea/07-TransportServiceDescriptionRequest.xml:/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT` (sea/07#F3); `sea/06-OrderResponse.xml:/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-05-18` (timelines#F7).
- Where it comes from: `tools/examples_scenarios.py` `sea()` (lines 1527 and 3551)
- What must be true afterwards: Each slip corrected.
- Fix direction: With D30.
- Depends on / blocks: none
- Touched by: D19 (O53), D9 (O7: demurrage could explain the container between its release on 19 May and the receipt on 21 May).
- State: D30 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D30); the voyage's figures wait for the place list (O91, O53).
- Findings: sea: 05#F14, 06#F5, 06#F6, 06#F12, 07#F3, 08#F1, 08#F2, 08#F6, 08#F7, 08#F12, 08#F13, 10#F10, 11#F14, 12#F6, 18#F8, 19#F14, 21#F7, 21#F8, 21#F9; consistency: timelines#F7

### C116 · Sea flow: factoring, statement, payment and the island's debit note
- Kind: flow story · Findings: 16 (High 5, Medium 4, Low 7) in 6 files, 1 flow · Needs decision: owner: D30
- What is wrong: The status response reports a payment made a month later; paid amounts differ from the remittance advice; the factor as accounting supplier of the invoice line; the storage charge three times in the debit note; the deposit as an invoice period. Example: `sea/24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30` (sea/24#F1).
- Where it comes from: `tools/examples_scenarios.py` `sea_with_debit()` (line 5904) and the sea finance documents 22–28
- What must be true afterwards: Factoring, statement and payments agree.
- Fix direction: Encoding fixes; yes-findings with D30.
- Depends on / blocks: none
- Touched by: D9 (sea/28 is not a debit note: the importer's customs inspection cost is re-homed, O6; C11's, C26's, C39's, C50's and C72's sea/28 findings go with this cause), D23 (O72: sea/22's deposit and balance).
- State: D30 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D30); the voyage's figures wait for the place list (O91, O53).
- Findings: sea: 22#F7, 22#F13, 22#F14, 24#F1, 24#F2, 25#F3, 25#F6, 26#F4, 26#F6, 26#F7, 27#F1, 27#F2, 28#F2, 28#F5, 28#F6, 28#F12

### C117 · Sea flow: business card, digital agreement and capabilities
- Kind: flow story · Findings: 15 (High 0, Medium 4, Low 11) in 3 files, 1 flow · Needs decision: owner: D30
- What is wrong: Audit evidence issued by the audited company; tendering-only evidence elements in a business card; a bilateral agreement signed by one participant; Lumeway's own EDI terms "signed" by the Trade Accord Council; billing processes that do not match the flow. Example: `sea/01-BusinessCard.xml:/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:EvidenceTypeCode` = `AUDIT` (sea/01#F3).
- Where it comes from: `tools/examples_scenarios.py` `digital_service()` (line 4890), `service_customization()` (line 4881), sea documents 01–04
- What must be true afterwards: The agreement documents describe what the parties actually exchange.
- Fix direction: Decide D30 for the yes-findings.
- Depends on / blocks: none
- Touched by: D6 (the digital agreement's signature waits for the signatures stage).
- State: D30 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D30); the voyage's figures wait for the place list (O91, O53).
- Findings: sea: 01#F3, 01#F4, 01#F5, 01#F12, 03#F6, 03#F7, 03#F8, 03#F12, 03#F13, 03#F14, 03#F15, 03#F16, 03#F18, 04#F4, 04#F10

### C118 · Sea flow: the CIF sale, freight and insurance
- Kind: flow story · Findings: 14 (High 3, Medium 3, Low 8) in 10 files, 1 flow · Needs decision: owner: D30
- What is wrong: Freight and insurance are charged on top of a price agreed CIF; the confirmed total differs from the invoice; the insurer as insurance party; one insurance split over two policies; pre-carriage freight that nobody bills; the statement repeats the invoice's freight. Example: `sea/06-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00` (sea/06#F1).
- Where it comes from: `tools/examples_scenarios.py` `sea_invoice_terms()` (line 1357), `cif_value()` (line 1154), `sea_order_response()` (line 1456)
- What must be true afterwards: Under CIF the price includes freight and insurance, consistently in order, invoice, statement and declarations.
- Fix direction: Decide D30 (preferred by sea/22#F3: drop the two charges).
- Depends on / blocks: C52 (D16)
- Touched by: D16 (Lisavu values landed: sea/19 states the landed value, which agrees with the 53,778.00 of the bill of lading), D18 (the import consumption tax of 10 % on the landed value; O48: Velumi's shop price).
- State: D30 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D30); the voyage's figures wait for the place list (O91, O53).
- Findings: sea: 05#F12, 05#F13, 06#F1, 09#F1, 09#F7, 11#F13, 14#F12, 14#F13, 14#F14, 18#F3, 19#F20, 22#F3, 25#F1, 26#F3

### C119 · Tender: tendering terms copied into notices, call, award and contract
- Kind: flow story · Findings: 86 (High 4, Medium 40, Low 42) in 13 files, 1 flow · Needs decision: owner: D28
- What is wrong: The shared terms repeat the same errors in five documents: a security-clearance date with "not required", a guarantee of 2400.00 that is 2 % of nothing, a turnover criterion "at least" coded "greater than", a "precise" subcontract share of 30 % next to 3.5 %, paper copies as a concession fee, variants unconstrained with a maximum of one, an auction and a framework agreement nobody holds, design-contest indicators in a supply procedure. Example: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21` (tender/01#F1).
- Where it comes from: `tools/examples_scenarios.py` `tendering_terms()` (line 6283), `auction_terms()` (line 6189), `tendering_process()` (line 6220), used by tender/01, 02, 03, 21, 22, 23 and 24
- What must be true afterwards: The procedure's terms are stated once, correctly, and the later documents repeat them unchanged.
- Fix direction: Fix `tendering_terms()` once (most options need no decision); D28 for the yes-findings (auction, framework values, budget).
- Depends on / blocks: none
- Touched by: D17 (O13: the notices' wording on the Bayvarran exemption), D27 (deadlines counted in the working days of the party that set them).
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender (86): 01#F1, 01#F7, 01#F8, 01#F9, 01#F10 …. Full list in `analysis/worklist-assignments.csv`.

### C120 · Tender: contract, catalogue and call-off (releases, despatch, credit, reminder)
- Kind: flow story · Findings: 30 (High 2, Medium 6, Low 22) in 11 files, 1 flow · Needs decision: owner: D28
- What is wrong: The contract identifies neither the accepted tender nor the prices; catalogue validity shifted against the contract; 200 benches "outstanding" that were never ordered; no serial numbers although the contract requires them; two statements of how the credit is settled; interest paid that the contract does not make due. Example: `tender/26-Order.xml:/Order/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS` (tender/26#F14).
- Where it comes from: `tools/examples_scenarios.py` `tender()` (lines 2360, 3459) and `tender_with_credit()` (line 6029)
- What must be true afterwards: The call-off documents execute the contract as signed.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Touched by: D22 (the invoice falls due 30 days after the accepted release, O69; Urvania's statutory 8 % for late payment), O12 (moss green, from D11), O50 (the forward contract becomes Valdara's hedge); C11's tender findings go with this cause.
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 24#F4, 25#F3, 25#F12, 25#F16, 25#F17, 25#F19, 25#F20, 25#F22, 26#F12, 26#F14, 27#F3, 27#F9, 27#F10, 27#F11, 28#F6, 29#F3, 29#F10, 29#F12, 32#F17, 32#F18, 33#F1, 33#F7, 33#F12, 33#F13, 34#F3, 34#F11, 35#F12, 36#F2, 36#F6, 36#F9

### C121 · Tender: the procurement project and its lots
- Kind: flow story · Findings: 26 (High 3, Medium 0, Low 23) in 11 files, 1 flow · Needs decision: owner: D28
- What is wrong: Lot 2 is works in the prior information notice and services elsewhere; lot 2 is described with the bench data; the buyer's estimates equal the winning tender to the cent; the project and programme have different names and codes. Example: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00` (tender/01#F27).
- Where it comes from: `tools/examples_scenarios.py` `procurement_project()` (line 6110), `procurement_lots()` (line 6462), `contract_name()` (line 6872)
- What must be true afterwards: One description of project and lots, and an estimate made before the tenders.
- Fix direction: Decide D28 (the estimate).
- Depends on / blocks: none
- Touched by: D14 (the tender keeps its prices: Valdara's bid 499 plus 18 for installation; O14: Lumeway's position on the direct bid and the estimate equal to the bid); C14's tender/33#F18 goes with this cause.
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 01#F4, 01#F27, 01#F28, 01#F29, 01#F30, 02#F5, 02#F32, 02#F33, 02#F34, 02#F38, 02#F39, 03#F5, 03#F33, 03#F34, 03#F35, 03#F39, 03#F40, 08#F6, 09#F10, 15#F15, 21#F14, 21#F17, 24#F14, 26#F15, 29#F14, 32#F19

### C122 · Tender: the tenders, receipt and withdrawal
- Kind: flow story · Findings: 15 (High 2, Medium 0, Low 13) in 4 files, 1 flow · Needs decision: owner: D28
- What is wrong: Warranty five years on the line and six in the criterion response; the tenderer's own costs as fees of the project; no unit prices although the procedure evaluates them; identical ordering terms in competing tenders. Example: `tender/15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:Quantity` = `240` (tender/15#F16).
- Where it comes from: `tools/examples_scenarios.py` `tender_lines()` (line 6557) and documents 15–19
- What must be true afterwards: Each tender states one offer, evaluated as tendered.
- Fix direction: Decide D28 for the yes-findings.
- Depends on / blocks: none
- Touched by: D4 (O13: the figures the tenders state).
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 15#F11, 15#F16, 15#F17, 16#F6, 17#F3, 17#F11, 17#F13, 17#F15, 17#F16, 17#F17, 19#F3, 19#F11, 19#F13, 19#F15, 19#F16

### C123 · Tender: the installation billed but never ordered
- Kind: flow story · Findings: 14 (High 7, Medium 4, Low 3) in 7 files, 1 flow · Needs decision: owner: D28
- What is wrong: The release order has one line (the benches); the invoice bills forty installations, invoiced before they can be done, taxed as a service to a business; the penalty is for late installation of a service billed as supplied; "by the manufacturer's installers" although a subcontractor installs. Example: `tender/32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.` (tender/32#F8).
- Where it comes from: `tools/examples_scenarios.py` `tender()` release order (lines 2360, 3459) and invoice
- What must be true afterwards: The installation is ordered, performed, accepted and then billed, by the party the award names.
- Fix direction: Decide D28 (preferred: order line for the installation, separate later invoice).
- Depends on / blocks: C51 (D22), C54 (D17)
- Touched by: D17 (`SVCABROAD` widened covers Valdara's installation on land abroad; the department withholds 10 %), D22 (O69), D9 (tender/34's penalty is re-homed as a supplier's credit note or a deduction in the remittance advice, O6), D20 (installation has real content: a crew of two assembles and anchors the benches).
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 25#F11, 25#F18, 26#F3, 27#F2, 28#F2, 32#F1, 32#F2, 32#F4, 32#F8, 32#F16, 33#F5, 33#F6, 34#F2, 34#F9

### C124 · Tender: expressions of interest, status, register extract and Valdara's qualification
- Kind: flow story · Findings: 13 (High 0, Medium 5, Low 8) in 3 files, 1 flow · Needs decision: owner: D28
- What is wrong: Two competing tenderers presented as one group; OperationType holds the line of business; capability figures that differ between the register extract and Valdara's qualification; one reference supply where three are required. Example: `tender/12-BusinessInformation.xml:/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupTypeCode` = `SAMEACTIVITY` (tender/12#F4).
- Where it comes from: `tools/examples_scenarios.py` tender documents 04–13 (enrichments after line 6508)
- What must be true afterwards: The qualification figures are one set, stated the same everywhere.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Touched by: D4 (the tender states Valdara's real figures, or says that the 180 are the staff of its street-furniture division; O13; C60's 8 Valdara findings go with this cause).
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 09#F5, 12#F4, 12#F5, 12#F6, 12#F13, 12#F14, 12#F15, 13#F1, 13#F3, 13#F4, 13#F10, 13#F11, 13#F12

### C125 · Tender: procedure periods against the notices' issue dates
- Kind: flow story · Findings: 10 (High 5, Medium 0, Low 5) in 9 files, 1 flow · Needs decision: owner: D28
- What is wrong: Requested publication and procedure periods lie before the notices' issue dates; interest and registrations after the reception period; the appeal period is the award's before the award existed; the contract signed on the last appeal day. Example: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT` (tender/01#F2).
- Where it comes from: `tools/examples_scenarios.py` `out_day()` (line 6491) and the notice/award dates in `tender()` (lines 2360, 3459)
- What must be true afterwards: Every period lies after the document that announces it and fits the procedure.
- Fix direction: Decide D28 (move the notices to late January, or the periods).
- Depends on / blocks: none
- Touched by: D27 (procedure dates on working days of the contracting body; C53's three tender findings go with this cause).
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 01#F2, 02#F1, 03#F1, 04#F4, 05#F4, 20#F1, 21#F2, 21#F12, 22#F5, 24#F13

### C126 · Tender: the guarantee certificate
- Kind: flow story · Findings: 9 (High 0, Medium 3, Low 6) in 4 files, 1 flow · Needs decision: owner: D28
- What is wrong: A bank guarantee described as immobilised shares of the tenderer itself; the tenderer as issuer of the bank's certificate; value and market value three days apart; tenders that do not refer to their guarantee. Example: `tender/17-Tender.xml:/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.` (tender/17#F12).
- Where it comes from: `tools/examples_scenarios.py` tender document 14 (guarantee)
- What must be true afterwards: One kind of guarantee, issued by the bank, referenced by the tender.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 14#F1, 14#F2, 14#F3, 14#F7, 14#F8, 14#F9, 15#F12, 17#F12, 19#F12

### C127 · Tender: award, notifications and appeal
- Kind: flow story · Findings: 7 (High 1, Medium 0, Low 6) in 3 files, 1 flow · Needs decision: owner: D28
- What is wrong: The opening still "scheduled" in the award notice; the review board as information party, receiver and mediator without contact; the winner's subcontract price told to the loser. Example: `tender/20-TendererQualificationResponse.xml:/TendererQualificationResponse/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra` (tender/20#F7).
- Where it comes from: `tools/examples_scenarios.py` `tender_result()` (line 6894), `appeal_terms()` (line 6884)
- What must be true afterwards: The award documents report a completed opening and a reachable appeal body.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Touched by: none of D1 to D27.
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 20#F6, 20#F7, 20#F8, 21#F1, 23#F3, 23#F4, 23#F5

### C128 · Tender: moss green ordered, grey identified
- Kind: flow story · Findings: 6 (High 5, Medium 1, Low 0) in 6 files, 1 flow · Needs decision: none
- What is wrong: The order change asks for moss green and the lot is made green, but despatch, declarations, invoice and credit note identify the grey variant while charging the special colour. Example: `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY` (tender/30#F1).
- Where it comes from: `tools/examples_scenarios.py` tender order change and despatch (`tender()` lines 2360, 3459); colour codes in `world/codelists/lists.json`
- What must be true afterwards: From the order change on, every document identifies the variant the change orders, as D28 settles it (O12), and the surcharge is charged only for a special colour.
- Fix direction: Carry the variant D28 chooses (O12) through every document from the order change on: a standard variant named by its identifier, with no surcharge, or a special colour specified in the order change, with the surcharge.
- Depends on / blocks: none
- Touched by: D11 (O12: moss green is either a standard variant that the order change names, so that no surcharge is due, or a special colour that the order change specifies, so that the surcharge is right; taken up with D28).
- State: D28 decided 2026-11-16; ready to implement as decided (see `analysis/worklist-decisions.md`, D28).
- Findings: tender: 27#F4, 29#F1, 30#F1, 31#F1, 32#F3, 33#F2

