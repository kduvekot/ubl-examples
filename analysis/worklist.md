# Worklist: the review findings by root cause

Made on 2026-11-15 at commit f07f6e1 (branch `claude/stoic-noether-5pboei`). Read: the 250 merged per-example reviews (`world/examples/<flow>/*.llm-review.<run>.merged.md`, 15 thorough runs from `20261112T1415Z-thorough` to `20261114T1433Z-thorough`) and the six topic files of the consistency review `20261114T2143Z-consistency` (index `analysis/consistency-review.20261114T2143Z-consistency.md`), with `analysis/review-merge-decisions.md`, `analysis/codelist-decisions.md`, `note/src/03-world.md` and the generators for the source places.

**3348 findings** in 256 review files (18 flows plus the consistency review): **293 High, 908 Medium, 2147 Low**; 921 are marked "Needs decision: yes". They are assigned to **128 causes**; 1960 findings wait on one of **46 owner decisions** (`analysis/worklist-decisions.md`).

How the assignment was made: `list_findings.py` turns every finding into one row of a table (title, severity, decision, the element names and values of its XPath lines). An ordered list of rules (patterns over title, elements and flow; first match wins) assigns a cause; about 150 findings that the rules put in the wrong place were corrected by hand after reading their titles, and the 32 consistency findings were assigned by reading. Each cause was then checked against the titles of all its findings, the options of every High finding and the full text of samples; the source place was found with grep in `tools/` and `world/`. Every finding has exactly one cause (`analysis/worklist-assignments.csv`).

Reproduce the findings table:

    python3 -I .claude/skills/ubl-example-review/scripts/list_findings.py    # writes .review/worklist/{findings,outside,refuted}.csv

## How to read this

- A **cause** is the place in the source (a builder, a default, a world-data value, a scenario) that produces findings. Fixing it resolves all its findings at once; a fixing session takes one cause (or one stage) at a time.
- **Kind**: encoding (a shared builder writes the wrong element or value), master data (world/*.json), world rule (a rule the owner must set), cross-flow story, generator mechanism (times, numbers, references derived by method), flow story (one flow's scenario). No cause is only a missing build check; the checks are listed in stage 7.
- **Decision**: "none" (the reviews and the merge decisions agree on the fix), "taken: …" (an earlier decision settles it), or "owner: D<n>" (see `analysis/worklist-decisions.md`). Findings marked "yes" inside a cause without an owner decision are confirmed in bulk under D46.
- **Files** counts review files, one per example (plus the consistency topic files). Severity counts are per finding.
- "Possibly not a problem" and "Conflict" notes mark findings that contradict the world story or an earlier decision. They stay assigned; the owner decides.
- Example citations name the example file and the absolute XPath in one pair of backticks, followed by the quoted value; all of them are checked with `check_xpaths.py` and `check_values.py`.

## Summary

| Kind of cause | Causes | Findings | High | Waiting on an owner decision |
|---|---:|---:|---:|---:|
| encoding | 36 | 840 | 54 | 84 |
| master data | 16 | 853 | 51 | 313 |
| world rule | 15 | 647 | 27 | 647 |
| cross-flow story | 3 | 17 | 5 | 12 |
| generator mechanism | 6 | 108 | 52 | 52 |
| flow story | 52 | 883 | 104 | 852 |
| check missing | 0 | 0 | 0 | 0 |
| **Total** | **128** | **3348** | **293** | **1960** |

| Cause | Title | Kind | Findings | Files | Flows | H/M/L | Decision | Source (short) |
|---|---|---|---:|---:|---:|---|---|---|
| C01 | Party master data copied into documents that do nothing with it | encoding | 245 | 213 | 17 | 0/0/245 | taken: merge decisions, rows "Party master data copied …" and "`CorporateStockAmount` holds share capital" | tools/build_examples.py, place_parties() |
| C02 | One contact template per kind of party, whatever the role | master data | 226 | 213 | 18 | 1/0/225 | taken: merge decisions, row "Contacts whose name, job title and department contradict …" | world/parties.json, tools/build_examples.py |
| C03 | Urvanian province written into `Region` | master data | 111 | 111 | 15 | 0/104/7 | taken: merge decisions, row "Province … in `Region`" | world/parties.json, world/countries.json |
| C04 | Public bodies described as companies in a commercial register | encoding | 88 | 83 | 13 | 0/77/11 | taken: merge decisions, row "Public bodies … as companies" | tools/build_examples.py, legal_entity() |
| C05 | Lumeway's "Gate 3" in its postal address | master data | 76 | 76 | 5 | 0/76/0 | taken: merge decisions, row "`AdditionalStreetName` = "Gate 3"" | world/parties.json |
| C06 | References that give only an ID | encoding | 59 | 59 | 13 | 0/0/59 | taken: merge decisions, row "References with only an ID and no document type" | tools/examples_scenarios.py, ref() |
| C07 | The department's party tax exemption reason is worded as a transaction | master data | 52 | 52 | 2 | 0/0/52 | taken: merge decisions, row "Party tax exemption reason worded as a transaction" (in the parties review's Known table) | world/parties.json, world/countries.json |
| C08 | Party roles that repeat another role or do not fit their definition | encoding | 41 | 39 | 12 | 0/7/34 | none | world/documents.json, tools/build_examples.py |
| C09 | Bench emission: 96 kg with factor 0.82 per 1 EA | master data | 40 | 40 | 6 | 40/0/0 | taken: merge decisions, row "Bench emission triple" | world/items.json, tools/build_examples.py |
| C10 | Locations named after companies or their office addresses | encoding | 36 | 29 | 11 | 1/4/31 | none | tools/examples_kit.py, leg_places() |
| C11 | Currencies and exchange rates with nothing to convert, or the wrong currency | encoding | 34 | 25 | 7 | 7/7/20 | taken: merge decisions, row "Exchange rates with nothing to convert …" | tools/examples_kit.py, price_block() |
| C12 | Customs declaration builders: goods items, offices, previous declaration and issuer | encoding | 32 | 17 | 9 | 5/7/20 | none | tools/examples_kit.py, goods_items() |
| C13 | Identifiers built from flow names, file numbers and other identifiers | generator mechanism | 28 | 28 | 7 | 0/0/28 | none | tools/examples_kit.py, tep() |
| C14 | The buyer's cost centre does not fit what is bought | master data | 24 | 24 | 11 | 1/2/21 | none | tools/examples_kit.py, cost_centre() |
| C15 | Shipment gross weight without the transport equipment | encoding | 24 | 24 | 6 | 5/15/4 | taken: merge decisions, row "Shipment `GrossWeightMeasure` without the transport equipment" | tools/examples_kit.py, gross_weight() |
| C16 | "NoStatus" as document or line status | encoding | 24 | 24 | 10 | 0/0/24 | taken: merge decisions, row "`NoStatus` as status code" | tools/examples_kit.py, despatch_advice() |
| C17 | Remittance advices: the invoice twice on a line, two payment-order references, header parties repeated | encoding | 21 | 10 | 8 | 0/0/21 | none | tools/examples_kit.py, remittance() |
| C18 | Transport events without type or place, or as generic events where a dedicated one exists | encoding | 19 | 17 | 6 | 0/9/10 | none | tools/examples_kit.py, event() |
| C19 | Framework transport-plan clauses and periods mis-encoded | encoding | 19 | 8 | 6 | 4/7/8 | none | tools/examples_kit.py, tep_terms() |
| C20 | `ShippingOrderID` holding the consignment or shipment ID | encoding | 18 | 18 | 9 | 7/10/1 | taken: merge decisions, row "`ShippingOrderID` holding the consignment or shipment ID" | tools/examples_kit.py, waybill() |
| C21 | Transport requests, instructions, waybills and manifests that do not say what, from where, to where or when | encoding | 18 | 18 | 9 | 0/17/1 | none | tools/examples_kit.py, tep_request() |
| C22 | Item properties of the slat: validity periods, repeated length, full specification | master data | 17 | 7 | 1 | 0/0/17 | none | world/items.json, tools/build_examples.py |
| C23 | Places and offices given only by name or text, without the identifier they have elsewhere | encoding | 16 | 16 | 8 | 0/0/16 | none | tools/examples_kit.py, place() |
| C24 | Tax totals and taxable amounts that ignore the document's own charges, or state an empty zero | encoding | 14 | 13 | 8 | 5/1/8 | taken: merge decisions, row "Taxable amount that ignores the document's own allowance or charge" | tools/examples_kit.py, tax_total() |
| C25 | Catalogue encoding: territory of the seller, "Active" status, CatalogueIndicator, discounts and dependent prices | encoding | 12 | 5 | 3 | 3/5/4 | none | tools/examples_kit.py, catalogue_terms() |
| C26 | Documents referenced as a kind they are not | encoding | 11 | 9 | 3 | 0/7/4 | none | self_billed(), tools/examples_kit.py |
| C27 | Despatch advices that do not say when the goods leave or arrive | encoding | 10 | 10 | 9 | 0/8/2 | none | tools/examples_kit.py, despatch_advice() |
| C28 | Orders without a requested delivery date | encoding | 10 | 10 | 7 | 0/0/10 | none | tools/examples_kit.py, order() |
| C29 | Urvania's national tariff subheading in other countries' documents | encoding | 10 | 10 | 5 | 0/2/8 | taken: `analysis/codelist-decisions.md` Q24 ("tariffs, rates and exemptions stay national") and `note/src/03-world.md` ("in Urvania, the national tariff code") | world/items.json, tools/examples_kit.py |
| C30 | Transport document type fixed per mode, not per convention and scope | encoding | 10 | 10 | 7 | 1/4/5 | none | tools/examples_kit.py, waybill() |
| C31 | Electricity, gas, water and levies classified as services | encoding | 9 | 6 | 3 | 0/5/4 | none | tools/examples_kit.py, tax_category() |
| C32 | Invoices not linked to the delivery they bill | encoding | 8 | 8 | 5 | 0/0/8 | none | tools/examples_kit.py, invoice() |
| C33 | "Three originals" against the distribution list | encoding | 8 | 8 | 8 | 3/0/5 | taken: merge decisions, row "Waybill note "three originals" against the distribution list" | tools/examples_kit.py, waybill() |
| C34 | Line IDs reused for another line | encoding | 7 | 7 | 2 | 4/0/3 | none | tools/examples_kit.py, tools/examples_scenarios.py |
| C35 | One transport service code per mode | encoding | 7 | 7 | 3 | 7/0/0 | none | tools/examples_kit.py |
| C36 | Ad valorem indicator and declared carriage value without a valuation | encoding | 5 | 5 | 3 | 2/0/3 | none | tools/examples_kit.py, waybill() |
| C37 | Order references in the wrong element | encoding | 5 | 4 | 3 | 0/3/2 | none | tools/examples_scenarios.py, air() |
| C38 | Bayvarra's surcharge "per month" encoded as one month only | encoding | 5 | 5 | 2 | 0/0/5 | none | tools/examples_kit.py, payment_terms() |
| C39 | Payment notes that call every document an invoice | encoding | 4 | 4 | 2 | 0/0/4 | none | tools/build_examples.py, account() |
| C40 | Pallets listed as packages contained in themselves | encoding | 3 | 2 | 2 | 0/3/0 | none | tools/examples_kit.py, handling_units() |
| C41 | `JourneyID` holding a voyage or month instead of the service schedule | encoding | 3 | 3 | 2 | 0/0/3 | none | tools/examples_kit.py, means() |
| C42 | A line marked both confidential and internal | encoding | 2 | 2 | 2 | 0/0/2 | none | tools/examples_scenarios.py |
| C43 | Temperature code given next to a measured value | encoding | 2 | 2 | 2 | 0/2/0 | none | tools/examples_scenarios.py |
| C44 | `VI-C180-2026` replaces a frame in one catalogue and a bench in a tender | encoding | 1 | 1 | 0 | 0/0/1 | none | tools/examples_scenarios.py |
| C45 | `Language/LocaleCode` = `en` | world rule | 213 | 213 | 15 | 0/213/0 | owner: D1 | tools/build_examples.py, party() |
| C46 | English renderings tagged with the issuer's country, Italian names tagged as English, legal form untagged | world rule | 179 | 123 | 15 | 0/0/179 | owner: D2 | tools/build_examples.py, language_tag() |
| C47 | `FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING for a cradle-to-gate footprint | world rule | 74 | 40 | 7 | 0/74/0 | owner: D10 | world/items.json, world/codelists/lists.json |
| C48 | Catalogue and product-passport data copied into business documents | world rule | 41 | 38 | 8 | 0/0/41 | owner: D11 | tools/build_examples.py, item() |
| C49 | Signature aggregates with only an ID and a signatory | world rule | 38 | 38 | 4 | 0/1/37 | owner: D6 | tools/examples_kit.py, tep() |
| C50 | Tax category O for goods, 0 % on O, and Lisavu's tax scheme without ID | world rule | 29 | 13 | 4 | 0/6/23 | owner: D15 | tools/examples_kit.py, tax_rule() |
| C51 | Contract payment terms never applied by the invoices under the contract | world rule | 12 | 10 | 4 | 10/0/2 | owner: D22 | tools/examples_kit.py, payment_terms() |
| C52 | Customs value on a different basis in each flow | world rule | 12 | 12 | 6 | 1/6/5 | owner: D16 | tools/examples_kit.py, goods_items() |
| C53 | Documents dated at the weekend against a Monday-to-Friday week | world rule | 12 | 12 | 6 | 1/2/9 | owner: D27 | tools/examples_scenarios.py, world/parties.json |
| C54 | Bayvarran withholding tax and tax representative only in the tender, and Urvania's "service to a business abroad" for a public body | world rule | 10 | 5 | 1 | 0/2/8 | owner: D17 | tools/examples_scenarios.py, withholding() |
| C55 | Standard terms IDs that do not mean the same number of days everywhere | world rule | 8 | 8 | 4 | 8/0/0 | owner: D23 | tools/examples_kit.py, payment_terms() |
| C56 | The map scale: all coordinates inside 35 km, against distances and times of hours and days | world rule | 8 | 7 | 2 | 4/0/4 | owner: D19 | world/countries.json, tools/build_examples.py |
| C57 | Duties, import taxes and Trade Accord preference stated nowhere | world rule | 6 | 5 | 4 | 1/2/3 | owner: D18 | tools/examples_scenarios.py, import_extras() |
| C58 | One sea voyage with four passage times | world rule | 4 | 3 | 1 | 2/1/1 | owner: D19 | tools/examples_scenarios.py, sea() |
| C59 | Lisavu's capital: "Port Wrenfield" in English addresses, "Selanu" in every other English text | world rule | 1 | 1 | 0 | 0/1/0 | owner: D3 | world/countries.json, tools/build_examples.py |
| C60 | Default founding date 1996-01-01 and size classes that do not fit the parties | master data | 181 | 169 | 15 | 4/0/177 | owner: D4 | world/parties.json, tools/codelists.py |
| C61 | World item numbers that are valid GTIN-12s; Valdara's items under Lumeway's GS1 prefix | master data | 76 | 54 | 9 | 0/0/76 | owner: D5 | world/items.json, world/parties.json |
| C62 | The maker's brand on the store's own-line garden set | master data | 12 | 12 | 1 | 0/0/12 | owner: D7 | world/items.json, tools/build_examples.py |
| C63 | Lisavu Cotton Farm: address lines that repeat the structured address, and a yearly expiring registration | master data | 11 | 6 | 2 | 0/0/11 | owner: D4 | world/parties.json, tools/build_examples.py |
| C64 | Industry classes that leave out what the party does | master data | 9 | 9 | 2 | 0/0/9 | owner: D8 | world/parties.json |
| C65 | Bale weight of about 227 kg as `PackSizeNumeric` | master data | 7 | 7 | 1 | 0/0/7 | owner: D12 | world/items.json |
| C66 | Debit notes with accounting supplier and customer reversed | master data | 5 | 5 | 3 | 5/0/0 | owner: D9 | world/documents.json |
| C67 | Side frame classified HS 7325.99 instead of a part of a seat | master data | 5 | 5 | 2 | 0/4/1 | owner: D13 | world/items.json |
| C68 | Valdara's distributor price equals its public contract price; Lumeway's revised frame price is below cost | master data | 1 | 1 | 0 | 0/0/1 | owner: D14 | world/items.json |
| C69 | The bench as shipped: pallets that do not fit, and a bench lighter than its parts | cross-flow story | 7 | 6 | 3 | 1/3/3 | owner: D20 | world/items.json, tools/examples_kit.py |
| C70 | One melt, one coating batch and one manufacture time for every casting and lot | cross-flow story | 6 | 4 | 2 | 3/0/3 | none | world/items.json, tools/examples_kit.py |
| C71 | Goods "from the distributor's stock" made days before they leave, and no document moves them | cross-flow story | 4 | 4 | 1 | 1/1/2 | owner: D21 | tools/examples_kit.py, instances() |
| C72 | Documents that report or cite what happens after their own issue time | generator mechanism | 38 | 32 | 9 | 30/1/7 | none | tools/build_examples.py, tools/examples_scenarios.py |
| C73 | References to documents under IDs no document has, or to documents the flow does not contain | generator mechanism | 27 | 25 | 8 | 20/3/4 | owner: D38 | tools/examples_scenarios.py, air() |
| C74 | Document numbers: one counter per flow shared by all issuers | generator mechanism | 10 | 8 | 3 | 2/1/7 | owner: D24 | tools/examples_kit.py, Flow.number() |
| C75 | Issuer prefixes: `BF` for two parties, second prefixes for signatures | generator mechanism | 4 | 3 | 1 | 0/1/3 | owner: D25 | tools/examples_kit.py, initials() |
| C76 | `ProfileExecutionID` is the flow name in all 250 documents | generator mechanism | 1 | 1 | 0 | 0/1/0 | owner: D26 | tools/build_examples.py |
| C77 | Waste flow: a transboundary notification for a movement inside one town; no weighbridge statement | flow story | 19 | 3 | 1 | 1/6/12 | owner: D42 | tools/examples_scenarios.py, waste() |
| C78 | Carnet flow: counterfoils, time limits and the duty claim | flow story | 20 | 4 | 1 | 2/4/14 | owner: D40 | tools/examples_scenarios.py, carnet() |
| C79 | Mast flow: dangerous-goods data of the battery, detector and stripper consignment | flow story | 36 | 5 | 1 | 2/13/21 | owner: D36 | world/items.json, tools/build_examples.py |
| C80 | Mast flow: the air waybill and the ULDs | flow story | 6 | 3 | 1 | 0/1/5 | owner: D36 | tools/examples_scenarios.py, mast() |
| C81 | Ore flow: monthly call-off, plan "as requested", bonus and moisture | flow story | 7 | 5 | 1 | 1/0/6 | owner: D45 | tools/examples_scenarios.py, ore() |
| C82 | Energy flow: 2400 MWh exported to Montebrio, sold to Ferrano Energy, imported by nobody | flow story | 9 | 3 | 1 | 4/4/1 | owner: D44 | tools/examples_scenarios.py |
| C83 | Energy flow: isolated slips | flow story | 8 | 5 | 1 | 1/2/5 | none | tools/examples_scenarios.py, utility_statement() |
| C84 | Packaging flow: isolated slips | flow story | 5 | 4 | 1 | 0/0/5 | none | tools/examples_scenarios.py, packaging() |
| C85 | Air flow: the missed-flight story and the CPT order change | flow story | 13 | 8 | 1 | 2/0/11 | owner: D39 | tools/examples_scenarios.py, air() |
| C86 | Air flow: packing, consolidation and charges of the castings | flow story | 10 | 3 | 1 | 3/2/5 | owner: D39 | tools/examples_scenarios.py, air_consignment() |
| C87 | Plastics flow: barge waybill and goods data | flow story | 15 | 4 | 1 | 2/4/9 | owner: D41 | tools/examples_scenarios.py, plastics() |
| C88 | Plastics flow: recycled-content certificate issued by a chamber of commerce | flow story | 5 | 5 | 1 | 0/0/5 | owner: D41 | world/parties.json, world/items.json |
| C89 | Wood flow: slat units and isolated slips | flow story | 10 | 5 | 1 | 1/0/9 | owner: D43 | tools/examples_scenarios.py, wood() |
| C90 | Rail flow: container train documents | flow story | 33 | 8 | 1 | 3/6/24 | owner: D37 | tools/examples_scenarios.py, rail() |
| C91 | Utility statement builder: average amount, supplier consumption, subscriber data | flow story | 30 | 6 | 2 | 3/9/18 | owner: D31 | tools/examples_scenarios.py, utility_statement() |
| C92 | Utilities: the telecom statement and invoice | flow story | 15 | 3 | 1 | 4/5/6 | owner: D31 | tools/examples_scenarios.py, telecom_consumption() |
| C93 | Utilities: the household's water on account, the mandate and the levy | flow story | 13 | 5 | 1 | 2/3/8 | owner: D31 | tools/examples_scenarios.py, utilities() |
| C94 | Utilities: excise and estimate-correction amounts | flow story | 7 | 3 | 1 | 6/1/0 | none | tools/examples_scenarios.py, energy_tax() |
| C95 | Utilities: isolated slips | flow story | 7 | 6 | 1 | 1/2/4 | owner: D31 | tools/examples_scenarios.py, utilities() |
| C96 | Qualification requests and responses (ESPD-like) in contest and tender | flow story | 32 | 8 | 2 | 1/11/20 | owner: D29 | tools/examples_scenarios.py, qualification_limits() |
| C97 | Procurement notices (contest and tender): notice types, defaults, languages, links | flow story | 31 | 14 | 2 | 0/6/25 | owner: D29 | tools/examples_scenarios.py, notice_head() |
| C98 | Contest: the design team, references, prizes and versions | flow story | 24 | 13 | 1 | 1/4/19 | owner: D29 | tools/examples_scenarios.py, contest_version() |
| C99 | Contest: the estimated contract amount of 54,000 lume | flow story | 8 | 8 | 1 | 0/0/8 | owner: D29 | tools/examples_scenarios.py, contest_project() |
| C100 | Road flow: isolated slips of the truck shipment | flow story | 25 | 10 | 1 | 1/6/18 | owner: D35 | tools/examples_scenarios.py, road() |
| C101 | Road flow: application and certificate of origin | flow story | 14 | 3 | 1 | 4/4/6 | owner: D35 | tools/examples_scenarios.py, road() |
| C102 | Road flow: the substituted 2026 casting | flow story | 8 | 7 | 1 | 0/1/7 | owner: D35 | tools/examples_scenarios.py, road() |
| C103 | Furniture flow: quotation, orders, invoice, return and credit | flow story | 27 | 9 | 1 | 0/1/26 | owner: D32 | tools/examples_scenarios.py, furniture() |
| C104 | Furniture flow: the replenishment and sales-reporting documents | flow story | 21 | 5 | 1 | 0/10/11 | owner: D32 | tools/examples_scenarios.py, furniture() |
| C105 | Furniture flow: the department's desks and installation | flow story | 10 | 3 | 1 | 0/0/10 | owner: D32 | tools/examples_scenarios.py, furniture() |
| C106 | Cotton flow: self-billing between ginnery and farm, and the mill's forecasts | flow story | 26 | 6 | 1 | 1/4/21 | owner: D33 | tools/examples_kit.py, self_billed() |
| C107 | Cotton flow: classing and phytosanitary certificates | flow story | 15 | 7 | 1 | 5/1/9 | owner: D33 | tools/examples_scenarios.py, cotton() |
| C108 | Cotton flow: the sea export (bill of lading, VGM, pre-arrival report) | flow story | 13 | 8 | 1 | 2/3/8 | owner: D33 | tools/examples_scenarios.py, cotton() |
| C109 | Cotton flow: classing results carried as the applicant's remarks | flow story | 7 | 7 | 1 | 0/0/7 | none | tools/examples_scenarios.py, cotton() |
| C110 | Retail flow: catalogue request, catalogue, updates and deletion | flow story | 15 | 5 | 1 | 3/4/8 | owner: D34 | tools/examples_scenarios.py, catalogue_update_head() |
| C111 | Retail flow: promotion, forecast, inventory and the shop sale | flow story | 13 | 4 | 1 | 2/2/9 | owner: D34 | tools/examples_scenarios.py, retail() |
| C112 | Retail flow: isolated slips | flow story | 12 | 5 | 1 | 1/2/9 | owner: D34 | tools/examples_scenarios.py, retail() |
| C113 | Retail flow: the delivery to the store (carrier references, arrival day) | flow story | 12 | 6 | 1 | 3/2/7 | owner: D34 | tools/examples_scenarios.py, retail() |
| C114 | Sea flow: bill of lading and ship reports | flow story | 21 | 5 | 1 | 3/7/11 | owner: D30 | tools/examples_scenarios.py, sea_consignment() |
| C115 | Sea flow: isolated slips | flow story | 20 | 11 | 1 | 2/3/15 | owner: D30 | tools/examples_scenarios.py, sea() |
| C116 | Sea flow: factoring, statement, payment and the island's debit note | flow story | 16 | 6 | 1 | 5/4/7 | owner: D30 | tools/examples_scenarios.py, sea_with_debit() |
| C117 | Sea flow: business card, digital agreement and capabilities | flow story | 15 | 3 | 1 | 0/4/11 | owner: D30 | tools/examples_scenarios.py, digital_service() |
| C118 | Sea flow: the CIF sale, freight and insurance | flow story | 14 | 10 | 1 | 3/3/8 | owner: D30 | tools/examples_scenarios.py, sea_invoice_terms() |
| C119 | Tender: tendering terms copied into notices, call, award and contract | flow story | 86 | 13 | 1 | 4/40/42 | owner: D28 | tools/examples_scenarios.py, tendering_terms() |
| C120 | Tender: contract, catalogue and call-off (releases, despatch, credit, reminder) | flow story | 30 | 11 | 1 | 2/6/22 | owner: D28 | tools/examples_scenarios.py, tender() |
| C121 | Tender: the procurement project and its lots | flow story | 26 | 11 | 1 | 3/0/23 | owner: D28 | tools/examples_scenarios.py, procurement_project() |
| C122 | Tender: the tenders, receipt and withdrawal | flow story | 15 | 4 | 1 | 2/0/13 | owner: D28 | tools/examples_scenarios.py, tender_lines() |
| C123 | Tender: the installation billed but never ordered | flow story | 14 | 7 | 1 | 7/4/3 | owner: D28 | tools/examples_scenarios.py, tender() |
| C124 | Tender: expressions of interest, status, register extract and Valdara's qualification | flow story | 13 | 3 | 1 | 0/5/8 | owner: D28 | tools/examples_scenarios.py |
| C125 | Tender: procedure periods against the notices' issue dates | flow story | 10 | 9 | 1 | 5/0/5 | owner: D28 | tools/examples_scenarios.py, out_day() |
| C126 | Tender: the guarantee certificate | flow story | 9 | 4 | 1 | 0/3/6 | owner: D28 | tools/examples_scenarios.py |
| C127 | Tender: award, notifications and appeal | flow story | 7 | 3 | 1 | 1/0/6 | owner: D28 | tools/examples_scenarios.py, tender_result() |
| C128 | Tender: moss green ordered, grey identified | flow story | 6 | 6 | 1 | 5/1/0 | none | tools/examples_scenarios.py, tender() |

## Order of work

### Stage 1: Fixes that need no decision and no story change

Encoding in shared builders and simple master-data corrections that the merge decisions or the reviews settle. They touch many files and remove most of the noise, so later stages are reviewed against a cleaner set.

Causes (44, 1414 findings): C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C44.

Safe to fix immediately (no decision, no dependency, no conflict): C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C23, C24, C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C44.

Fix after the named decision or cause: C22 (The copying part depends on D11 (what item data travels).…).

Stage 1 covers 1414 of 3348 findings (42 %).

### Stage 2: Owner decisions on world rules, then their implementation

Geography, calendar, payment terms, customs, tax and language rules. Each needs D-numbers answered first; several contradict an earlier decision or the world story and must be settled before any example changes.

Causes (15, 647 findings): C45, C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56, C57, C58, C59.

Decide first, then implement in this order: the language rules (they touch most files), the payment, customs and tax rules, the calendar, and the geography (which the sea voyage depends on). Item and catalogue data whose decision conflicts with an earlier one (FullnessIndicationCode, item data in documents) are here because the conflict must be settled before stage 1's item fixes are finished.

### Stage 3: Master data

Party and item data in world/*.json that need an owner choice (dates, sizes, identifiers, classes, brands).

Causes (9, 307 findings): C60, C61, C62, C63, C64, C65, C66, C67, C68.

### Stage 4: Cross-flow story: the goods chain

Which lots reach Lumeway and how the bench ships; this changes product data in several flows at once.

Causes (3, 17 findings): C69, C70, C71.

The goods chain comes before the generator mechanisms because it changes lots, dates and possibly documents; the melt and serial fix follows the chosen lots.

### Stage 5: Generator mechanisms: time, numbering, references

Issue times, document numbers, prefixes and references are derived by method; fix the method once, after the stories that change dates and documents are settled.

Causes (5, 80 findings): C72, C73, C74, C75, C76.

Issue times first (they decide document order), then numbering, prefixes and the execution ID (which depend on the final order), then references (which use the final numbers).

### Stage 6: Flow stories, smallest flows first

Each flow's remaining findings, per flow in the order waste, carnet, mast, ore, energy, packaging, air, plastics, wood, rail, utilities, contest, road, furniture, cotton, retail, sea, tender.

Causes (52, 883 findings): C77, C78, C79, C80, C81, C82, C83, C84, C85, C86, C87, C88, C89, C90, C91, C92, C93, C94, C95, C96, C97, C98, C99, C100, C101, C102, C103, C104, C105, C106, C107, C108, C109, C110, C111, C112, C113, C114, C115, C116, C117, C118, C119, C120, C121, C122, C123, C124, C125, C126, C127, C128.

- waste: C77 (19 findings)
- carnet: C78 (20 findings)
- mast: C79, C80 (42 findings)
- ore: C81 (7 findings)
- energy: C82, C83 (17 findings)
- packaging: C84 (5 findings)
- air: C85, C86 (23 findings)
- plastics: C87, C88 (20 findings)
- wood: C89 (10 findings)
- rail: C90 (33 findings)
- utilities: C91, C92, C93, C94, C95 (72 findings)
- contest: C96, C97, C98, C99 (95 findings)
- road: C100, C101, C102 (47 findings)
- furniture: C103, C104, C105 (58 findings)
- cotton: C106, C107, C108, C109 (61 findings)
- retail: C110, C111, C112, C113 (52 findings)
- sea: C114, C115, C116, C117, C118 (86 findings)
- tender: C119, C120, C121, C122, C123, C124, C125, C126, C127, C128 (216 findings)

### Stage 7: Build checks

No cause is only a missing check. The checks below guard causes of the earlier stages so that the errors do not come back.

- Issue time after every actual event and every referenced document of the same flow: guards C72, C73.
- Due date − issue date = the period of the cited terms ID: guards C55, C51.
- Tax arithmetic per subtotal, including document-level allowances and charges: guards C24, C94.
- Emission value = factor × base where both are given: guards C09.
- No `NoStatus`, no identity exchange rate, no pricing currency other than the price's: guards C16, C11.
- Every document reference typed; every reference to an example resolves (flow_index "-> ?"): guards C06, C73.
- `ShippingOrderID` resolves to forwarding instructions of the flow: guards C20.
- Shipment gross weight ≥ goods + equipment tare: guards C15.
- Waybill note and distribution list agree on the originals: guards C33.
- Customs offices of a declaration belong to the declaring country; national tariff only in its country: guards C12, C29.
- No customs-trader ID outside customs and cross-border documents; no share capital outside the issuer's own invoice: guards C01.
- Issue weekday per issuer kind (after the calendar decision): guards C53.
- Document numbers rise per issuer with the issue timestamp; one prefix per party: guards C74, C75.
- Coordinates against stated distances and durations (after the map decision): guards C56, C58.

Dependencies across stages: C56 — blocks C58; the map rendering on the site uses the same tiles; C58 — after C56 (D19); C70 — after C71 (D21), which may change the lots; C71 — with C70; C12 (sea/11 previous declaration); C85 — C72 (order of cancellation and replacement); C118 — C52 (D16); C123 — C51 (D22), C54 (D17).

## Causes

### C01 · Party master data copied into documents that do nothing with it
- Kind: encoding · Findings: 245 (High 0, Medium 0, Low 245) in 213 files, 17 flows · Needs decision: taken: merge decisions, rows "Party master data copied …" and "`CorporateStockAmount` holds share capital" (15 findings marked "yes" go to D46)
- What is wrong: A party is described with all its master data wherever it appears: customs-trader numbers in domestic orders and tender documents, share capital and stock listing in despatch advices, tax registrations in documents without tax, Rinova's waste permit in every plastics document, bank accounts in orders that move no money. The per-example reviews rate it Low, one finding per example. Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002` (contest/01#F4); `ore/01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch` (ore/01#F3).
- Where it comes from: `tools/build_examples.py` `place_parties()` (line 1117) writes `party(pid)` in full for every role of `world/documents.json`; `party()` (line 91) and `legal_entity()` (line 276) always add customs-trader IDs, tax schemes, share capital, listing, logo, website, service provider, permits and accounts
- What must be true afterwards: Each document carries of a party only what that document uses (identification, name and the data its definition or the transaction needs); the issuer's own share capital on its own invoice stays.
- Fix direction: Give each role a profile (short, trade, legal, tax, customs, payment) and let `place_parties()` choose it per document type; build check: no customs-trader ID outside customs and cross-border documents, no share capital outside the issuer's own invoice.
- Depends on / blocks: none
- Note: The findings marked "Needs decision: yes" (mostly contest and tender: the authority's tax scheme in procurement documents) follow the same rule and are confirmed in bulk (D46).
- Findings: air (1): 10#F12; carnet (2): 01#F10, 04#F6; contest (29): 01#F3, 01#F4, 02#F4, 02#F5, 03#F4 …; cotton (15): 01#F3, 02#F4, 03#F8, 04#F15, 05#F17 …; energy (7): 01#F6, 03#F4, 05#F10, 06#F4, 07#F7 …; furniture (17): 01#F6, 02#F6, 03#F6, 04#F5, 05#F5 …; ore (8): 01#F3, 02#F8, 03#F13, 04#F5, 05#F9 …; packaging (10): 01#F3, 01#F7, 02#F6, 03#F3, 04#F4 …; plastics (21): 01#F5, 01#F8, 02#F5, 02#F7, 03#F9 …; rail (8): 01#F7, 02#F10, 03#F12, 06#F23, 08#F27 …; retail (23): 01#F6, 02#F10, 02#F18, 03#F7, 04#F10 …; road (17): 01#F8, 02#F8, 03#F10, 04#F11, 05#F10 …; sea (27): 01#F7, 02#F13, 02#F17, 04#F8, 07#F6 …; tender (32): 01#F16, 02#F19, 03#F19, 04#F8, 05#F6 …; utilities (12): 01#F10, 02#F9, 03#F12, 04#F6, 05#F6 …; waste (6): 01#F8, 01#F11, 02#F12, 02#F15, 03#F8 …; wood (10): 01#F5, 02#F9, 03#F5, 04#F11, 04#F13 …. Full list in `analysis/worklist-assignments.csv`.

### C02 · One contact template per kind of party, whatever the role
- Kind: master data · Findings: 226 (High 1, Medium 0, Low 225) in 213 files, 18 flows · Needs decision: taken: merge decisions, row "Contacts whose name, job title and department contradict …" (1 finding marked "yes" goes to D46)
- What is wrong: Every company desk is a "Customer service officer" in "Sales", carriers' desks "Operations planner", public bodies "Public service officer"; the same desk appears whether the party sells, buys, pays or receives goods (contacts of Valdara's "Order desk" on ore, gas and slat purchases). Name, job title and department often contradict each other. Example: `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office` (furniture/01#F5); `contest/03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry` (contest/03#F9).
- Where it comes from: `world/parties.json` `identity.contacts` (name, `job_title`, `department`, `hours`), written by `tools/build_examples.py` `party()` (lines 199–202) into every role
- What must be true afterwards: Each contact fits the party's role in the document (buying, accounts, goods-in, customs), and name, job title and department agree.
- Fix direction: Give parties.json contacts per function (sales, purchasing, accounts, goods-in, customs) and let the role pick the contact (in `place_parties()` / `party()`), or drop the contact where the document does not need one.
- Depends on / blocks: none
- Note: Contact hours that exclude the time of an event are under C53.
- Findings: air (11): 01#F12, 02#F10, 03#F16, 04#F19, 05#F10 …; carnet (2): 01#F13, 03#F10; contest (12): 03#F9, 04#F9, 05#F9, 06#F10, 07#F7 …; cotton (20): 01#F5, 02#F6, 03#F7, 04#F17, 05#F19 …; energy (8): 01#F7, 02#F4, 03#F3, 04#F10, 05#F7 …; furniture (15): 01#F5, 02#F5, 03#F5, 04#F4, 05#F4 …; mast (7): 01#F9, 02#F10, 03#F11, 03#F12, 04#F8 …; ore (8): 01#F2, 02#F7, 03#F12, 04#F4, 05#F8 …; packaging (10): 01#F4, 02#F4, 03#F5, 04#F6, 05#F4 …; plastics (11): 01#F4, 02#F4, 03#F8, 04#F11, 05#F7 …; rail (9): 01#F8, 02#F11, 03#F13, 06#F20, 06#F21 …; retail (22): 01#F5, 02#F11, 03#F8, 04#F11, 05#F9 …; road (17): 01#F7, 02#F7, 03#F6, 04#F9, 05#F9 …; sea (32): 01#F10, 02#F15, 02#F19, 03#F11, 04#F9 …; tender (18): 02#F30, 03#F30, 03#F31, 13#F17, 14#F14 …; utilities (10): 01#F11, 02#F10, 03#F13, 04#F7, 05#F7 …; waste (3): 01#F9, 02#F13, 03#F7; wood (11): 01#F6, 02#F10, 03#F6, 04#F7, 05#F6 …. Full list in `analysis/worklist-assignments.csv`.

### C03 · Urvanian province written into `Region`
- Kind: master data · Findings: 111 (High 0, Medium 104, Low 7) in 111 files, 15 flows · Needs decision: taken: merge decisions, row "Province … in `Region`" (4 findings marked "yes" go to D46)
- What is wrong: The province ("Province of Ferrano") of every Urvanian address is in `Region`, which UBL defines as a region "of a country" in the sense of an informal area; a province is a country subdivision (`CountrySubentity`). The value is master data and is copied into every full party description. The same element holds the cotton farm's "North coast" origin area in cotton/02 and 07. Example: `tender/03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano` (tender/03#F7); `contest/15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano` (contest/15#F5).
- Where it comes from: `world/parties.json` `identity.address.Region` of the 14 Urvanian parties (e.g. line 37) and `world/countries.json` `region` (line 96); `tools/build_examples.py` `address()` (field order at line 472)
- What must be true afterwards: No address of an Urvanian party carries the province in `Region`; it is in `CountrySubentity` (with a code if the world has one).
- Fix direction: Move the field in parties.json (and the Urvanian address format in countries.json) from `Region` to `CountrySubentity`; the cotton origin area goes to the element the farm address already uses (`District`). A build check that `Region` is not used for a country subdivision would guard it.
- Depends on / blocks: none
- Findings: carnet (4): 01#F4, 02#F2, 03#F3, 04#F2; contest (2): 15#F5, 16#F4; cotton (7): 02#F10, 07#F10, 08#F15, 10#F11, 11#F12 …; energy (9): 01#F3, 02#F3, 03#F2, 04#F6, 05#F2 …; ore (8): 01#F1, 02#F3, 03#F7, 04#F2, 05#F5 …; packaging (2): 01#F1, 02#F2; plastics (11): 01#F2, 02#F1, 03#F2, 04#F3, 05#F1 …; rail (11): 01#F4, 02#F4, 03#F5, 04#F1, 05#F3 …; retail (1): 02#F6; road (17): 01#F4, 02#F1, 03#F3, 04#F3, 05#F3 …; sea (1): 02#F8; tender (22): 03#F7, 12#F3, 13#F5, 14#F5, 15#F2 …; utilities (4): 01#F7, 02#F6, 03#F9, 04#F1; waste (3): 01#F3, 02#F6, 03#F3; wood (9): 01#F2, 02#F3, 03#F1, 04#F3, 05#F2 …. Full list in `analysis/worklist-assignments.csv`.

### C04 · Public bodies described as companies in a commercial register
- Kind: encoding · Findings: 88 (High 0, Medium 77, Low 11) in 83 files, 13 flows · Needs decision: taken: merge decisions, row "Public bodies … as companies" (16 findings marked "yes" go to D46)
- What is wrong: Customs services, the public works department, the chambers, the review board, the Trade Accord Council and the maritime administration get a commercial-register entry with a liquidation status, because `legal_entity()` writes both for every party that is not a person. The world list has no register type for public bodies. Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL` (contest/01#F2); `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE` (tender/01#F6).
- Where it comes from: `tools/build_examples.py` `legal_entity()`: `CompanyLiquidationStatusCode` "ACTIVE" for every non-person (line 297) and `CorporateRegistrationTypeCode` "COMMERCIAL" for every register (line 315); `world/parties.json` `kind: "public"`
- What must be true afterwards: No public body carries `CorporateRegistrationTypeCode` COMMERCIAL or `CompanyLiquidationStatusCode`; companies keep them.
- Fix direction: In `legal_entity()`, skip the commercial-register scheme and the liquidation status for parties of kind "public" (and give them their legal basis instead, if a document needs one). Small related slips: the Port of Selanu as a separately registered head office (air/09#F3), the farm's yearly registration (see C63).
- Depends on / blocks: none
- Findings: air (1): 09#F3; carnet (8): 01#F6, 01#F11, 02#F3, 02#F6, 03#F4 …; contest (16): 01#F2, 02#F2, 03#F3, 04#F2, 05#F2 …; cotton (3): 10#F14, 11#F2, 15#F2; energy (2): 04#F7, 05#F4; furniture (3): 15#F1, 16#F2, 17#F2; plastics (2): 05#F4, 09#F1; rail (1): 06#F4; road (4): 05#F8, 06#F14, 07#F15, 10#F4; sea (8): 03#F4, 04#F2, 11#F11, 15#F6, 16#F5 …; tender (36): 01#F6, 02#F7, 03#F8, 04#F3, 05#F3 …; waste (2): 01#F10, 02#F14; wood (2): 05#F4, 07#F3. Full list in `analysis/worklist-assignments.csv`.

### C05 · Lumeway's "Gate 3" in its postal address
- Kind: master data · Findings: 76 (High 0, Medium 76, Low 0) in 76 files, 5 flows · Needs decision: taken: merge decisions, row "`AdditionalStreetName` = "Gate 3""
- What is wrong: Lumeway's postal address carries a vehicle gate as additional street name, so every full description of Lumeway (76 files, 5 flows) gives a gate where the post should go. A gate belongs in a delivery or pick-up location. Example: `retail/01-CatalogueRequest.xml:/CatalogueRequest/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (retail/01#F4); `sea/01-BusinessCard.xml:/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (sea/01#F2).
- Where it comes from: `world/parties.json` Lumeway Distribution (6-xb) `identity.address.AdditionalStreetName` = "Gate 3" (line 898)
- What must be true afterwards: Lumeway's postal address has no gate; where a document needs the gate, it is in a delivery location (with the GLN the flow already uses for the siding or goods-in).
- Fix direction: Drop the line from parties.json; add the gate to the delivery locations that need it (road/01 names gates and docks inconsistently, C100).
- Depends on / blocks: none
- Findings: air (8): 01#F4, 02#F3, 03#F8, 04#F9, 06#F5 …; rail (6): 01#F3, 02#F6, 03#F9, 06#F11, 08#F14 …; retail (20): 01#F4, 02#F4, 03#F5, 04#F4, 05#F4 …; road (17): 01#F3, 02#F3, 03#F2, 04#F5, 05#F7 …; sea (25): 01#F2, 02#F4, 03#F5, 04#F3, 05#F4 …. Full list in `analysis/worklist-assignments.csv`.

### C06 · References that give only an ID
- Kind: encoding · Findings: 59 (High 0, Medium 0, Low 59) in 59 files, 13 flows · Needs decision: taken: merge decisions, row "References with only an ID and no document type" (2 findings marked "yes" go to D46)
- What is wrong: Additional and line document references carry only an `ID`, so the receiver cannot tell what kind of document is meant (waybills, orders, data sheets, minutes, contracts), in 13 flows. Example: `sea/01-BusinessCard.xml:/BusinessCard/cac:AdditionalDocumentReference/cbc:ID` = `LD-REG-XB` (sea/01#F11); `tender/22-AwardedNotification.xml:/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID` = `PWD-EVAL-REPORT-26` (tender/22#F12).
- Where it comes from: `tools/examples_scenarios.py` `ref()` (line 2303) and `full_reference()` (line 4838); inline `DocumentReference` blocks in the kit (e.g. `examples_kit.py` line 443) and scenarios
- What must be true afterwards: Every reference to a document that is not typed by its element names its kind (`DocumentTypeCode` or `DocumentType`), and, where it is an example of the flow, resolves to it.
- Fix direction: Let the reference helper always add the type; build check: every `AdditionalDocumentReference`/`DocumentReference` has a type.
- Depends on / blocks: none
- Findings: air: 02#F5, 07#F8; carnet: 01#F21, 02#F8, 03#F11, 04#F12; cotton: 03#F4, 05#F11; ore: 02#F9, 03#F14, 05#F10; plastics: 05#F15, 06#F18, 07#F6, 09#F11; rail: 06#F16, 10#F7; retail: 01#F8; road: 02#F9, 05#F16, 06#F21, 07#F22, 09#F13, 14#F6, 16#F10; sea: 01#F11, 03#F17, 09#F9, 10#F11, 11#F17, 12#F8, 14#F17, 15#F11, 16#F23, 18#F5, 19#F12, 21#F10, 25#F12; tender: 01#F15, 15#F13, 17#F18, 19#F17, 20#F12, 21#F26, 22#F12, 23#F11, 24#F11, 27#F12, 29#F13, 30#F16, 33#F17, 36#F7; utilities: 04#F4, 07#F5, 08#F15, 14#F4; waste: 01#F15, 02#F9; wood: 05#F16

### C07 · The department's party tax exemption reason is worded as a transaction
- Kind: master data · Findings: 52 (High 0, Medium 0, Low 52) in 52 files, 2 flows · Needs decision: taken: merge decisions, row "Party tax exemption reason worded as a transaction" (in the parties review's Known table)
- What is wrong: The department's `PartyTaxScheme/ExemptionReason` says "Sale to a public body", which describes a transaction, not the party's status, in every document that describes the department (55 in contest, furniture, tender and utilities, as the parties review counts). Example: `tender/06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC` (tender/06#F11); `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC` (contest/01#F5).
- Where it comes from: `world/parties.json` Lumeport Public Works Department `tax_exemption_kind` = "Sale to a public body" (line 1163); the text comes from `world/countries.json` (line 249) via `tools/examples_kit.py` `tax_category()` (line 105)
- What must be true afterwards: The party-level exemption reason describes why the party is exempt ("Public body exempt from sales tax"), and the transaction wording stays in the tax categories of lines.
- Fix direction: Give the exemption list a party-status wording, or a separate party text in parties.json.
- Depends on / blocks: none
- Findings: contest: 01#F5, 02#F6, 03#F6, 04#F6, 05#F6, 06#F8, 07#F11, 08#F7, 09#F6, 10#F6, 11#F12, 12#F8, 13#F6, 14#F7, 15#F11, 16#F10; tender: 01#F17, 02#F20, 03#F20, 04#F9, 05#F8, 06#F11, 07#F9, 08#F4, 09#F7, 10#F8, 11#F6, 12#F9, 13#F18, 14#F15, 15#F9, 16#F8, 17#F9, 18#F7, 19#F9, 20#F9, 21#F22, 22#F9, 23#F9, 24#F15, 25#F15, 26#F16, 27#F13, 28#F8, 29#F20, 30#F15, 31#F9, 32#F23, 33#F23, 34#F15, 35#F14, 36#F11

### C08 · Party roles that repeat another role or do not fit their definition
- Kind: encoding · Findings: 41 (High 0, Medium 7, Low 34) in 39 files, 12 flows · Needs decision: none (6 findings marked "yes" go to D46)
- What is wrong: Roles are filled with the party that already holds another role in the same document: `CustomerParty` equal to the receiver in utility statements (whose definition is "the buyer, if different from the receiver"), the importer as its own notifier, the contracting party in eight further roles of the tender notices, originator and beneficiary on every line; and the rail carrier and the mast forwarder as `FreightForwarderParty`, which UBL defines as a consolidator. Example: `tender/15-Tender.xml:/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department` (tender/15#F10); `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores` (furniture/01#F3).
- Where it comes from: `world/documents.json` `parties` maps (e.g. CustomerParty next to ReceiverParty, notifier = importer), placed by `tools/build_examples.py` `place_parties()` (line 1117); originator/beneficiary blocks in `tools/examples_scenarios.py` (lines 5275, 5293, 6487)
- What must be true afterwards: A role appears only where it adds a party or information the document needs; party roles fit their UBL definition.
- Fix direction: Remove the redundant roles from documents.json; build check: no role whose definition says "if different" equals the role it is compared with.
- Depends on / blocks: none
- Note: The findings marked "yes" (forwarder role, consignor notified of its own goods) are confirmed in bulk (D46).
- Findings: air: 03#F12, 07#F14; cotton: 03#F10, 04#F4, 09#F14; energy: 01#F2; furniture: 01#F3, 02#F7, 11#F5, 12#F4, 16#F9; mast: 02#F11, 02#F15, 03#F16, 03#F17; plastics: 09#F12; rail: 05#F9, 06#F3, 08#F23; retail: 02#F12, 03#F10, 04#F13; sea: 05#F15, 25#F8, 27#F6; tender: 01#F18, 02#F21, 03#F21, 09#F9, 15#F10, 17#F10, 19#F10, 21#F23, 31#F12, 33#F19; utilities: 01#F4, 05#F2, 08#F3, 09#F10, 12#F5; wood: 07#F9

### C09 · Bench emission: 96 kg with factor 0.82 per 1 EA
- Kind: master data · Findings: 40 (High 40, Medium 0, Low 0) in 40 files, 6 flows · Needs decision: taken: merge decisions, row "Bench emission triple"
- What is wrong: Every full description of the bench (40 files, 6 flows) states 96 kg CO2e with `ValueFactorNumeric` 0.82 and `ValueBaseMeasure` 1 EA, and 0.82 × 1 is not 96. The figure is a product footprint from the manufacturer's LCA, not a calculation from an activity. Example: `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96` (rail/01#F1); `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96` (road/01#F1).
- Where it comes from: `world/items.json` bench `emission` (factor "0.82", line 219, base 1 EA); written by `tools/build_examples.py` `item()` (line 1089)
- What must be true afterwards: Either no factor and base, or a factor and base whose product is the stated value.
- Fix direction: Drop factor and base from items.json (preferred in all 40 findings); a build check that value = factor × base where both are given. tender/35#F2 (interest factor) is in this cause because it is the same element misuse on a reminder line.
- Depends on / blocks: none
- Findings: carnet: 01#F3; rail: 01#F1, 06#F2, 11#F1; retail: 02#F1, 04#F2, 05#F2, 07#F1, 08#F1, 12#F1, 17#F1, 18#F1, 19#F1, 21#F1; road: 01#F1, 04#F2, 05#F2, 06#F2, 07#F2, 10#F2, 11#F1, 13#F1, 15#F1; sea: 02#F2, 05#F2, 10#F2, 11#F2, 19#F1, 20#F1, 21#F1, 22#F4, 29#F1; tender: 25#F2, 26#F2, 29#F2, 30#F2, 31#F2, 32#F7, 33#F4, 35#F2

### C10 · Locations named after companies or their office addresses
- Kind: encoding · Findings: 36 (High 1, Medium 4, Low 31) in 29 files, 11 flows · Needs decision: none
- What is wrong: From/to locations, issue, status and notification locations are a company's name and business address instead of the place (quay, siding, airport, warehouse), so the barge "starts" at the carrier's office and the ore train runs between head offices. Example: `ore/05-Waybill.xml:/Waybill/cac:IssueLocation/cbc:Name` = `Serravona Mining` (ore/05#F7); `plastics/03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Rivermouth Packaging` (plastics/03#F10).
- Where it comes from: `tools/examples_kit.py` `leg_places()` (line 624) and `address_of()` (line 631) build transport locations from the parties' postal addresses; issue and status locations in `event()` (line 1273) and the scenarios
- What must be true afterwards: Transport and event locations name the place where the thing happens, with its identifier (UN/LOCODE, GLN) where the world has one.
- Fix direction: Derive locations from map.json places (or the parties' sites/GLNs) instead of postal addresses.
- Depends on / blocks: none
- Findings: air: 04#F15, 05#F5, 09#F10; mast: 03#F10; ore: 02#F6, 03#F8, 03#F10, 05#F7; plastics: 03#F1, 03#F10, 04#F14, 04#F18, 06#F15, 06#F17; rail: 02#F14, 03#F6, 03#F16, 04#F8, 05#F10, 07#F9, 08#F9, 08#F20; retail: 06#F12, 08#F11, 11#F4, 13#F8, 21#F11; road: 03#F8, 08#F10, 08#F20, 09#F6; sea: 29#F8; tender: 02#F31, 03#F32; utilities: 02#F11; wood: 04#F12

### C11 · Currencies and exchange rates with nothing to convert, or the wrong currency
- Kind: encoding · Findings: 34 (High 7, Medium 7, Low 20) in 25 files, 7 flows · Needs decision: taken: merge decisions, row "Exchange rates with nothing to convert …" (7 findings marked "yes" go to D46)
- What is wrong: Pricing, payment, tax and alternative currencies are written where nothing is converted (identity rates, rates in waybills and forwarding instructions), or name a currency the amounts are not in: the pricing currency is lume while every price is in coral (cotton/04, 05) or ferra while the price is in lume (tender/26, 32, 33). Example: `energy/06-Invoice.xml:/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.` (energy/06#F1); `cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:TaxCurrencyCode` = `XLC` (cotton/04#F7).
- Where it comes from: `tools/examples_kit.py` `price_block()` (line 329, `PricingExchangeRate`), `rate()` (line 817), `currency_line()` (line 278); `tools/examples_scenarios.py` `PRICING_RATE` (lines 2418, 2453) and the forward contract in the tender call-off
- What must be true afterwards: Every currency code and exchange rate converts an amount the document states in that currency; no rate from a currency to itself.
- Fix direction: Drop the elements where nothing is converted (preferred in every finding); build check: a `PricingCurrencyCode` equals the currency of the prices, a rate's source ≠ target.
- Depends on / blocks: none
- Note: Possibly not a problem for cotton/04#F1 and 05#F1: `note/src/03-world.md` says "seed cotton is priced from the trade accord's lint reference price, published in lume", so a lume pricing currency may be intended; then the conversion must be shown, not dropped.
- Findings: air: 03#F11, 04#F12; cotton: 04#F1, 04#F7, 04#F8, 05#F1, 05#F8, 08#F3, 09#F13, 13#F8; energy: 06#F1, 07#F2; road: 15#F2; sea: 09#F8, 12#F7, 14#F16, 24#F3, 25#F2, 26#F8, 27#F3, 28#F4, 28#F10; tender: 26#F1, 26#F6, 26#F13, 27#F8, 28#F7, 32#F6, 32#F9, 32#F14, 33#F3, 33#F14, 35#F8; utilities: 12#F16

### C12 · Customs declaration builders: goods items, offices, previous declaration and issuer
- Kind: encoding · Findings: 32 (High 5, Medium 7, Low 20) in 17 files, 9 flows · Needs decision: none (12 findings marked "yes" go to D46)
- What is wrong: Declarations give the goods quantity as a weight without packages, no transport at the border, no link to the invoice the value rests on, and validity periods; the exit office of the exporting country appears in imports; `PreviousCustomsDeclaration` holds another country's declaration; the waybill names customs as issuer of the exporter's declaration. Example: `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side` (tender/30#F14); `rail/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331` (rail/08#F4).
- Where it comes from: `tools/examples_kit.py` `goods_items()` (line 844), `export_declaration()` (line 864), `import_declaration()` (line 881); `tools/examples_scenarios.py` `export_extras()` (line 4567), `import_extras()` (line 4590), `exit_office()` (line 4557), `rail_offices()` (line 590)
- What must be true afterwards: Each declaration declares packages, transport at the border and the invoice; offices are the declaring country's; a previous declaration is a declaration of the same procedure chain in that country; the issuer of a declaration is its declarant.
- Fix direction: Fix the shared customs builders; build check: the office in a declaration belongs to the declaring country.
- Depends on / blocks: none
- Note: The previous-declaration finding of sea/11 is also part of the goods chain (C71, D21).
- Findings: cotton: 15#F8, 15#F10; energy: 04#F11, 05#F11; plastics: 05#F2, 05#F9, 09#F5, 09#F8, 09#F9, 09#F13; rail: 06#F5, 06#F6, 06#F12, 08#F4; road: 05#F1, 08#F4, 08#F5, 10#F12; sea: 11#F1, 11#F3, 11#F4, 11#F16, 19#F10, 19#F11; tender: 30#F12, 30#F14, 31#F14, 31#F15; waste: 02#F4; wood: 05#F11, 07#F11, 07#F12

### C13 · Identifiers built from flow names, file numbers and other identifiers
- Kind: generator mechanism · Findings: 28 (High 0, Medium 0, Low 28) in 28 files, 7 flows · Needs decision: none (5 findings marked "yes" go to D46)
- What is wrong: Signature IDs contain the flow name or the example's file number, pallet SSCCs start with the serial of the first casting, the same remittance ID `VI-RM-26-0316` is used by three payers (see C74), a journey/week number is one off. Example: `cotton/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `SCG-SIG-EX-cotton` (cotton/11#F14); `road/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-road` (road/05#F17).
- Where it comes from: `tools/examples_kit.py` `tep()` signature `…-SIG-{flow.base}` (line 715), `waybill()` signature (line 784), `unit_id()` (line 1346: SSCC serial from the castings' serial); flow-name signature IDs in `tools/examples_scenarios.py` (search "SIG-EX")
- What must be true afterwards: No identifier contains a flow name or file number; identifiers of different things are not derived from each other unless the world's rule says so.
- Fix direction: Per scheme an independent running number in the issuer's series (identifiers#F4 option a).
- Depends on / blocks: none
- Findings: cotton: 09#F15, 11#F14, 13#F14, 15#F17; energy: 05#F13; plastics: 04#F13, 05#F16, 06#F24, 09#F16; road: 05#F17, 06#F10, 07#F12, 09#F12, 10#F18, 16#F5; sea: 09#F16, 11#F25, 12#F15, 13#F12, 14#F25; tender: 15#F20, 17#F19, 19#F18, 30#F17, 31#F17; wood: 05#F17, 07#F16; consistency: identifiers#F4

### C14 · The buyer's cost centre does not fit what is bought
- Kind: master data · Findings: 24 (High 1, Medium 2, Low 21) in 24 files, 11 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: Each party has one cost centre, used for whatever it buys: Valdara books electricity, waste services and freight as "Raw materials and parts", the store books shirts to its garden department, outbound freight is "Stock purchases". Example: `packaging/03-Order.xml:/Order/cbc:AccountingCostCode` = `2200` (packaging/03#F2); `utilities/05-UtilityStatement.xml:/UtilityStatement/cbc:AccountingCostCode` = `6120` (utilities/05#F11).
- Where it comes from: `tools/examples_kit.py` `cost_centre()` (line 215) with `world/parties.json` `cost_centre` (one per party, e.g. line 149)
- What must be true afterwards: The accounting cost of a line fits what the line buys, from the buyer's own chart.
- Fix direction: Give parties.json a small chart of cost centres per kind of purchase and let `cost_centre()` choose by item kind.
- Depends on / blocks: none
- Findings: air: 10#F4; cotton: 03#F2; furniture: 14#F2, 15#F4, 16#F5, 17#F5; packaging: 03#F2, 04#F2, 05#F2, 07#F2; rail: 10#F4; retail: 16#F3; road: 14#F5; sea: 18#F4; tender: 33#F18; utilities: 01#F8, 02#F8, 03#F4, 05#F11, 06#F8, 10#F1, 12#F10, 13#F3; waste: 03#F4

### C15 · Shipment gross weight without the transport equipment
- Kind: encoding · Findings: 24 (High 5, Medium 15, Low 4) in 24 files, 6 flows · Needs decision: taken: merge decisions, row "Shipment `GrossWeightMeasure` without the transport equipment" (4 findings marked "yes" go to D46)
- What is wrong: `Shipment/GrossWeightMeasure` includes the transport equipment by its definition, but the kit writes the goods' gross weight, also where the same document gives the container's tare (sea/10: the shipment weighs less than its own container). Example: `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29` (cotton/09#F5); `sea/10-PackingList.xml:/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4` (sea/10#F1).
- Where it comes from: `tools/examples_kit.py` `gross_weight()` (line 469), used by `despatch_advice()` (line 415) and `waybill()` (line 789)
- What must be true afterwards: The shipment gross weight includes the equipment where the document knows it (container, wagons), or is absent; the goods' gross weight is on the goods item or consignment.
- Fix direction: Compute goods + tare where equipment is known, else move the value to the goods item; build check: shipment gross ≥ sum of equipment tare + goods.
- Depends on / blocks: none
- Findings: cotton: 03#F11, 09#F5, 11#F1, 13#F4, 15#F1; mast: 02#F4, 03#F4, 04#F2; ore: 04#F1, 05#F3; rail: 06#F1, 08#F2; sea: 06#F2, 09#F4, 10#F1, 11#F6, 12#F3, 14#F2, 15#F2, 19#F5, 20#F4; wood: 05#F7, 06#F11, 07#F10

### C16 · "NoStatus" as document or line status
- Kind: encoding · Findings: 24 (High 0, Medium 0, Low 24) in 24 files, 10 flows · Needs decision: taken: merge decisions, row "`NoStatus` as status code"
- What is wrong: Document and line status codes say "NoStatus" in despatch advices, requests and receipts of ten flows: a filler that states nothing (UBL IND5/IND6). Example: `plastics/03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus` (plastics/03#F5); `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cbc:DocumentStatusCode` = `NoStatus` (sea/16#F9).
- Where it comes from: `tools/examples_kit.py` `despatch_advice()` (lines 407, 421), `receipt_advice()` (line 436), `tep_request()` (line 680), and scenario documents that copy them
- What must be true afterwards: No `DocumentStatusCode` or `LineStatusCode` with a value that only says there is no status.
- Fix direction: Remove the elements from the kit builders; a build check rejecting the code "NoStatus".
- Depends on / blocks: none
- Findings: air: 03#F18, 06#F7, 08#F9; cotton: 03#F1, 04#F24, 09#F6; mast: 04#F5; plastics: 03#F5, 08#F7; rail: 02#F8; retail: 11#F8, 12#F17, 17#F7; road: 03#F4, 04#F8; sea: 06#F13, 09#F15, 12#F14, 16#F9, 20#F8, 21#F6; tender: 29#F11; wood: 04#F5, 06#F4

### C17 · Remittance advices: the invoice twice on a line, two payment-order references, header parties repeated
- Kind: encoding · Findings: 21 (High 0, Medium 0, Low 21) in 10 files, 8 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: The remittance builder references the paid invoice twice on the same line, gives two different values for the payer's payment order, repeats the header's accounting parties on the line and sets a generic payment purpose, in eight flows. Example: `plastics/11-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PayerReference` = `RP-0882` (plastics/11#F3); `utilities/04-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0313` (utilities/04#F5).
- Where it comes from: `tools/examples_kit.py` `remittance()` (line 546)
- What must be true afterwards: One reference per paid document per line, one payment-order reference, line-level parties only where they differ.
- Fix direction: Fix `remittance()` once.
- Depends on / blocks: none
- Findings: cotton: 18#F2, 18#F3, 18#F4; furniture: 08#F11; ore: 08#F2, 08#F3, 08#F4; plastics: 11#F3, 11#F4; retail: 19#F11; road: 17#F9, 17#F10; utilities: 04#F3, 04#F5, 04#F8, 07#F4, 07#F6, 14#F9, 14#F10; wood: 09#F7, 09#F8

### C18 · Transport events without type or place, or as generic events where a dedicated one exists
- Kind: encoding · Findings: 19 (High 0, Medium 9, Low 10) in 17 files, 6 flows · Needs decision: none
- What is wrong: Events are given with a date and time but no type and no location, or as "additional" free-text events where the stage has a dedicated event (loading, acceptance, arrival), in six flows. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13` (air/03#F6); `rail/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00` (rail/02#F7).
- Where it comes from: `tools/examples_kit.py` `event()` (line 1273) and its callers in the scenarios
- What must be true afterwards: Every event says what happened (dedicated element or type code) and where.
- Fix direction: Make `location` and `type_code` required in `event()` and use the dedicated stage events.
- Depends on / blocks: none
- Findings: air: 03#F6, 05#F3, 09#F4; plastics: 04#F22, 06#F20; rail: 02#F7, 03#F19, 07#F3, 07#F6, 08#F11, 09#F3; retail: 15#F5; road: 08#F27; sea: 08#F8, 13#F5, 14#F18, 16#F19, 17#F4, 17#F5

### C19 · Framework transport-plan clauses and periods mis-encoded
- Kind: encoding · Findings: 19 (High 4, Medium 7, Low 8) in 8 files, 6 flows · Needs decision: none (4 findings marked "yes" go to D46)
- What is wrong: The shared framework clauses put a late-delivery penalty into `PenaltySurchargePercent` (a late-payment element), a post-event duration into a pre-arrival notice, a stationary-service location without a stationary service, a commission to an absent broker, and "Waiting time 40 per hour" without a currency; the service period starts after the pickup it contains (rail/02, 03) or the pre-arrival period lies before the transport (ore/03); the wood transport window ends before the promised delivery window. Example: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:StartDate` = `2026-03-04` (ore/03#F2); `rail/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14` (rail/02#F2).
- Where it comes from: `tools/examples_kit.py` `tep_terms()` (lines 646–661) and `tep_request()`/`tep()` periods (lines 673–738)
- What must be true afterwards: The clauses use elements whose definitions fit; every amount has a currency; the service period contains the pickup and delivery.
- Fix direction: Fix `tep_terms()` once (it is shared by ore, rail and plastics) and derive the periods from the legs.
- Depends on / blocks: none
- Note: The waiting-time currency is "Cannot be told" 8 in the conditions file; the fixing session picks XUF or XBL with a plausible rate.
- Findings: ore: 03#F2, 03#F5, 03#F9, 03#F11; plastics: 03#F3, 04#F4, 04#F5, 04#F15, 04#F16, 04#F17, 04#F19; rail: 02#F2, 03#F2, 03#F7, 03#F17, 03#F18; retail: 11#F1; utilities: 10#F9; wood: 04#F1

### C20 · `ShippingOrderID` holding the consignment or shipment ID
- Kind: encoding · Findings: 18 (High 7, Medium 10, Low 1) in 18 files, 9 flows · Needs decision: taken: merge decisions, row "`ShippingOrderID` holding the consignment or shipment ID"
- What is wrong: `ShippingOrderID` is "the shipping order or forwarding instructions" number, but the kit fills it with the consignment ID, so the same shipment has two or three different "shipping orders" across a flow (air, sea). Example: `air/04-Waybill.xml:/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324` (air/04#F1); `rail/07-TransportationStatus.xml:/TransportationStatus/cbc:ShippingOrderID` = `VI-CS-26-0327` (rail/07#F2).
- Where it comes from: `tools/examples_kit.py` `waybill()` (line 759: `flow.numbers.get("consignment", number)`); `tools/examples_scenarios.py` lines 1639, 4249, 4279
- What must be true afterwards: Every `ShippingOrderID` is the number of the forwarding instructions or booking that exists in the flow, the same in all documents of the shipment, or the element is absent.
- Fix direction: Use the forwarding instructions' number where the flow has one, else drop the element; build check: a ShippingOrderID resolves to a ForwardingInstructions of the flow.
- Depends on / blocks: none
- Findings: air: 03#F10, 04#F1, 05#F2, 09#F1; cotton: 09#F2; mast: 03#F1; ore: 05#F1; plastics: 06#F4; rail: 07#F2, 08#F7; retail: 13#F4, 14#F3; road: 08#F6, 09#F2; sea: 09#F3, 12#F1, 13#F2, 17#F1

### C21 · Transport requests, instructions, waybills and manifests that do not say what, from where, to where or when
- Kind: encoding · Findings: 18 (High 0, Medium 17, Low 1) in 18 files, 9 flows · Needs decision: none
- What is wrong: The generic transport builders give a weight and a note but no goods item, packages, places of taking over and delivery, or dates: forwarding instructions that do not say what to carry, a shipped-on-board bill without goods or vessel, a cargo manifest that does not list the cargo. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323` (air/03#F4); `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201` (cotton/09#F4).
- Where it comes from: `tools/examples_kit.py` `tep_request()` (line 673), `tep()` (line 700), `waybill()` (line 747); forwarding instructions in `tools/examples_scenarios.py` (`sea_consignment_fi()` line 1522, `air_consignment()` line 1892)
- What must be true afterwards: Every transport request, plan, instruction, waybill and manifest states the cargo (goods items, packages), the places and the requested or actual dates its definition calls for.
- Fix direction: Give the builders the consignment data the flow already holds (handling units, legs, events).
- Depends on / blocks: none
- Findings: air: 03#F4, 04#F5; contest: 08#F4; cotton: 09#F4, 13#F2, 14#F1; mast: 02#F3; ore: 02#F2, 03#F6, 05#F2; plastics: 04#F6; retail: 13#F3; sea: 07#F4, 09#F2, 10#F3, 12#F2, 15#F3; wood: 04#F4

### C22 · Item properties of the slat: validity periods, repeated length, full specification
- Kind: master data · Findings: 17 (High 0, Medium 0, Low 17) in 7 files, 1 flow · Needs decision: none
- What is wrong: The slat's property "Planed on four sides" has a 12-month validity, its length is repeated in `SellersItemIdentification/MeasurementDimension`, and the full commercial specification (test methods) stands in customs declarations and invoices (wood, 7 files). Example: `wood/01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800` (wood/01#F8).
- Where it comes from: `world/items.json` hardwood slat properties; `tools/build_examples.py` `item_property()` (line 638)
- What must be true afterwards: Properties carry validity only where they expire; dimensions once, in the item; customs declarations carry what customs needs.
- Fix direction: Clean the slat's data in items.json.
- Depends on / blocks: none
- Note: The copying part depends on D11 (what item data travels).
- Findings: wood: 01#F8, 01#F9, 02#F14, 02#F15, 03#F11, 03#F12, 05#F12, 05#F13, 05#F14, 06#F13, 06#F14, 07#F13, 07#F14, 07#F15, 08#F11, 08#F12, 08#F13

### C23 · Places and offices given only by name or text, without the identifier they have elsewhere
- Kind: encoding · Findings: 16 (High 0, Medium 0, Low 16) in 16 files, 8 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: Delivery places of Incoterms, airports, customs offices and ports of registry are given by name only, although the flow identifies them elsewhere by UN/LOCODE or GLN. Example: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport` (sea/14#F19); `air/01-OrderChange.xml:/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal` (air/01#F8).
- Where it comes from: `tools/examples_kit.py` `place()` (line 1177) and `order()` delivery terms (line 300); `tools/examples_scenarios.py` `exit_office()` (line 4557)
- What must be true afterwards: A place that the world identifies carries its identifier wherever it is given.
- Fix direction: Use `place()` with the identifier for delivery terms, offices and ports.
- Depends on / blocks: none
- Findings: air: 01#F8; cotton: 08#F10, 11#F7; ore: 01#F5; rail: 01#F13, 06#F13; retail: 14#F7, 22#F6; road: 05#F14; sea: 05#F11, 11#F15, 13#F9, 14#F19, 15#F12, 16#F22; wood: 03#F9

### C24 · Tax totals and taxable amounts that ignore the document's own charges, or state an empty zero
- Kind: encoding · Findings: 14 (High 5, Medium 1, Low 8) in 13 files, 8 flows · Needs decision: taken: merge decisions, row "Taxable amount that ignores the document's own allowance or charge" (1 finding marked "yes" goes to D46)
- What is wrong: The taxable amount leaves out the document-level allowance or charge of the same category (furniture/10, retail/08, cotton/04, 05, wood/03; air/01 the whole order instead of the change), and several documents carry a zero tax total without a category, scheme or reason (energy/08, sea/25, tender/15, tender/35, wood/02, cotton/04). Example: `tender/15-Tender.xml:/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00` (tender/15#F14); `air/01-OrderChange.xml:/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `51200.00` (air/01#F2).
- Where it comes from: `tools/examples_kit.py` `tax_total()` (line 243) and `monetary_total()` (line 259); `tools/examples_scenarios.py` `with_allowance()` (line 921)
- What must be true afterwards: Taxable amount = line extension ± document-level allowances and charges of that category; a tax total only where a tax is stated, with category and reason when it is zero.
- Fix direction: Feed allowances and charges into `tax_total()`; drop empty tax totals. Build check: the tax arithmetic per subtotal.
- Depends on / blocks: none
- Findings: air: 01#F2; cotton: 04#F2, 04#F23, 05#F3; energy: 08#F7; furniture: 10#F1; retail: 08#F2; sea: 25#F7; tender: 15#F14, 17#F14, 19#F14, 35#F9; wood: 02#F11, 03#F3

### C25 · Catalogue encoding: territory of the seller, "Active" status, CatalogueIndicator, discounts and dependent prices
- Kind: encoding · Findings: 12 (High 3, Medium 5, Low 4) in 5 files, 3 flows · Needs decision: none
- What is wrong: Every catalogue puts the seller's country into the price's territory, so an export price carries "Export outside Bayvarra" for the territory Bayvarra (conditions#F1: one price list, two tax treatments); the price list status is "Active" where the element names original/copy/revision; `CatalogueIndicator` is set in the catalogue itself; the "full container" discount and the dependent side-frame price do not follow from their conditions. Example: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB` (sea/02#F1); `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU` (tender/25#F1).
- Where it comes from: `tools/examples_kit.py` `catalogue_terms()` (line 1001; territory = seller's country at line 1015); `tools/build_examples.py` `item()` `CatalogueIndicator` (line 871)
- What must be true afterwards: Territory = the market the price is offered for, with that market's tax; one price list ID, one territory, one treatment; status codes from the element's meaning; no indicator in the catalogue itself.
- Fix direction: Fix `catalogue_terms()` (option a of conditions#F1: territory = buyer's market).
- Depends on / blocks: none
- Findings: retail: 02#F15, 02#F23, 03#F11; sea: 02#F1, 02#F5, 02#F6, 02#F7, 02#F21; tender: 25#F1, 25#F7, 25#F8; consistency: conditions#F1

### C26 · Documents referenced as a kind they are not
- Kind: encoding · Findings: 11 (High 0, Medium 7, Low 4) in 9 files, 3 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: A delivery note is referenced as a despatch advice, a weighbridge ticket as a receipt advice, a quotation as a contract, a work report and a budget commitment as billing documents, a bill of lading as a delivery note. Example: `cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193` (cotton/04#F3); `furniture/11-OrderCancellation.xml:/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568` (furniture/11#F1).
- Where it comes from: source not located in one place: the reference elements chosen in the scenario code (cotton `self_billed()` in `tools/examples_kit.py` line 1115, furniture in `tools/examples_scenarios.py` lines 3268–3396, sea debit note `sea_with_debit()` line 5904)
- What must be true afterwards: Each reference uses the element for the kind of document referenced, or a typed `AdditionalDocumentReference`.
- Fix direction: Correct the reference elements per flow.
- Depends on / blocks: none
- Findings: cotton: 04#F3, 04#F11, 05#F4, 05#F12; furniture: 11#F1, 14#F3, 16#F1, 17#F1; sea: 06#F7, 26#F5, 28#F7

### C27 · Despatch advices that do not say when the goods leave or arrive
- Kind: encoding · Findings: 10 (High 0, Medium 8, Low 2) in 10 files, 9 flows · Needs decision: none
- What is wrong: The kit's despatch advice has no despatch date or time, no estimated delivery and no transport reference, in nine flows. Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323` (air/06#F6); `packaging/06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cbc:ID` = `LTM-SH-26-0527` (packaging/06#F2).
- Where it comes from: `tools/examples_kit.py` `despatch_advice()` (line 401)
- What must be true afterwards: Every despatch advice states the despatch (actual or planned) and the expected delivery, and how the goods are identified.
- Fix direction: Add `Shipment/Delivery/Despatch` dates and the estimated delivery period in `despatch_advice()`.
- Depends on / blocks: none
- Findings: air: 06#F6, 08#F7; mast: 04#F7; ore: 04#F3; packaging: 06#F2; plastics: 08#F1; retail: 12#F3; sea: 20#F5; tender: 29#F4; wood: 06#F3

### C28 · Orders without a requested delivery date
- Kind: encoding · Findings: 10 (High 0, Medium 0, Low 10) in 10 files, 7 flows · Needs decision: none
- What is wrong: Orders and order changes state no requested delivery or collection date, also where urgency is the reason (air/01). Example: `air/01-OrderChange.xml:/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:ID` = `CPT` (air/01#F9); `furniture/10-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport` (furniture/10#F6).
- Where it comes from: `tools/examples_kit.py` `order()` (line 285)
- What must be true afterwards: Every order states when the goods are wanted (or, for ex-works, when they are collected).
- Fix direction: Add `Delivery/RequestedDeliveryPeriod` in `order()` from the flow's dates.
- Depends on / blocks: none
- Findings: air: 01#F9; furniture: 10#F6; packaging: 01#F6, 03#F6, 05#F6; plastics: 01#F9; rail: 01#F12; retail: 08#F10; wood: 03#F8, 10#F4

### C29 · Urvania's national tariff subheading in other countries' documents
- Kind: encoding · Findings: 10 (High 0, Medium 2, Low 8) in 10 files, 5 flows · Needs decision: taken: `analysis/codelist-decisions.md` Q24 ("tariffs, rates and exemptions stay national") and `note/src/03-world.md` ("in Urvania, the national tariff code") (4 findings marked "yes" go to D46)
- What is wrong: The 8-digit Urvanian subheading travels with the bench and the frame into Bayvarran and Lisavan declarations (road/10, tender/31, sea/11, sea/19, rail/06) and into Bayvarran commercial documents. Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990` (air/06#F13); `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910` (sea/19#F7).
- Where it comes from: `world/items.json` `national_tariff` of bench and frame (e.g. line 253), written by `tools/examples_kit.py` `customs_item()` (line 828) into every customs declaration and item
- What must be true afterwards: A national subheading appears only in documents of the country whose tariff it is.
- Fix direction: Write `national_tariff` only when the declaring country (or the seller, for commercial documents) is Urvania (conditions#F10 option a).
- Depends on / blocks: none
- Note: The findings marked "yes" are settled by Q24; confirmed in bulk (D46).
- Findings: air: 01#F10, 06#F13, 08#F15; retail: 02#F22, 04#F16; road: 10#F10; sea: 19#F7, 26#F11; tender: 31#F7; consistency: conditions#F10

### C30 · Transport document type fixed per mode, not per convention and scope
- Kind: encoding · Findings: 10 (High 1, Medium 4, Low 5) in 10 files, 7 flows · Needs decision: none (3 findings marked "yes" go to D46)
- What is wrong: A domestic road carriage gets a CMR, a domestic rail carriage a CIM note, the rail flow's waybill is a CMR, and despatch advices in air and sea shipments ask for damage to be noted "on the consignment note". Example: `road/11-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:Delivery/cac:DeliveryNoteDocumentReference/cbc:ID` = `TH-WB-26-0159` (road/11#F2); `air/06-DespatchAdvice.xml:/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.` (air/06#F8).
- Where it comes from: `tools/examples_kit.py` `WAYBILL_KIND` (line 741: one kind per mode) used by `waybill()`; damage notes "on the consignment note" in despatch advices
- What must be true afterwards: The waybill type follows the convention that applies to the leg (international or domestic, mode), and texts name the document the flow uses.
- Fix direction: Choose the kind by mode and border crossing (codelist-decisions: WaybillTypeCode by legal regime); fix the despatch-advice note.
- Depends on / blocks: none
- Findings: air: 03#F5, 06#F8, 08#F10; mast: 04#F6; ore: 05#F4; rail: 08#F1; retail: 13#F7; road: 11#F2, 13#F5; sea: 20#F9

### C31 · Electricity, gas, water and levies classified as services
- Kind: encoding · Findings: 9 (High 0, Medium 5, Low 4) in 6 files, 3 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: `SupplyTypeCode` is "SERVICES" for electricity, gas and drinking water (utilities, energy) and for a levy that is no supply, while gas is goods elsewhere in the same flow. Example: `utilities/06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES` (utilities/06#F2); `energy/03-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES` (energy/03#F1).
- Where it comes from: `tools/examples_kit.py` `tax_category()` (lines 115–128: GOODS only for items of kind "goods")
- What must be true afterwards: Energy and water are goods (or the code is absent); a levy collected for a third party carries no supply type.
- Fix direction: Classify the utility items as goods in items.json and skip the code for levies.
- Depends on / blocks: none
- Findings: energy: 03#F1; furniture: 09#F8; utilities: 02#F4, 06#F2, 06#F6, 09#F5, 09#F11, 11#F2, 11#F9

### C32 · Invoices not linked to the delivery they bill
- Kind: encoding · Findings: 8 (High 0, Medium 0, Low 8) in 8 files, 5 flows · Needs decision: none
- What is wrong: Invoices give no delivery date or place and no despatch or receipt reference, also where an export exemption rests on the delivery (packaging/02, rail/11, wood/08). Example: `air/10-Invoice.xml:/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324` (air/10#F9); `cotton/16-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198` (cotton/16#F6).
- Where it comes from: `tools/examples_kit.py` `invoice()` (line 473)
- What must be true afterwards: Every invoice for goods identifies the delivery (despatch advice reference or delivery date and place); an export exemption names its evidence.
- Fix direction: Add `DespatchDocumentReference` and `Delivery` in `invoice()`.
- Depends on / blocks: none
- Findings: air: 10#F9; cotton: 16#F6; packaging: 02#F8, 04#F3, 07#F3; rail: 11#F7; wood: 08#F9, 11#F4

### C33 · "Three originals" against the distribution list
- Kind: encoding · Findings: 8 (High 3, Medium 0, Low 5) in 8 files, 8 flows · Needs decision: taken: merge decisions, row "Waybill note "three originals" against the distribution list" (2 findings marked "yes" go to D46)
- What is wrong: The waybill says "Three originals: consignor, consignee, carrier." while its distribution lists one original and an electronic copy (eight flows). Example: `plastics/06-Waybill.xml:/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.` (plastics/06#F3); `rail/08-Waybill.xml:/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.` (rail/08#F6).
- Where it comes from: `tools/examples_kit.py` `waybill()` note (line 762) and `DocumentDistribution` (lines 772–779); `tools/examples_scenarios.py` line 1640, `bl_distribution()` (line 4418)
- What must be true afterwards: The note and the distribution list agree on the number of originals and who gets them.
- Fix direction: Generate the note from the distribution (or the distribution from the convention); build check comparing the two.
- Depends on / blocks: none
- Findings: air: 04#F16; mast: 03#F8; ore: 05#F6; plastics: 06#F3; rail: 08#F6; retail: 13#F1; road: 08#F19; sea: 14#F11

### C34 · Line IDs reused for another line
- Kind: encoding · Findings: 7 (High 4, Medium 0, Low 3) in 7 files, 2 flows · Needs decision: none
- What is wrong: The air order change adds frames under line ID 1, the bench line of the order it changes; responses and despatch advices follow; a substitute line and a handling-unit receipt line reuse ID 1 (retail). Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1` (air/06#F2); `retail/08-Order.xml:/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cbc:ID` = `1` (retail/08#F9).
- Where it comes from: `tools/examples_kit.py` despatch and receipt lines (lines 423, 450–451: line i refers to order line i); the air order change in `tools/examples_scenarios.py` `air()` (line 1940)
- What must be true afterwards: A new line has a new ID, carried through the follow-up documents; references point to the line they mean.
- Fix direction: Give the added line ID 3 (air) and fix the index-based references in the kit.
- Depends on / blocks: none
- Findings: air: 01#F1, 02#F1, 06#F2, 08#F3; retail: 08#F9, 12#F9, 17#F13

### C35 · One transport service code per mode
- Kind: encoding · Findings: 7 (High 7, Medium 0, Low 0) in 7 files, 3 flows · Needs decision: none
- What is wrong: The service code depends only on the mode, so the ore in bulk wagons gets a container-train service, the rail flow's road pickup becomes "Full truck load" as main service of a container train, and the plastics barge carries "bulk" for bagged cargo. Example: `ore/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT` (ore/02#F1); `plastics/07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Bulk cargo down the river to the coast of Bayvarra, per tonne.` (plastics/07#F2).
- Where it comes from: `tools/examples_kit.py` `MODE_SERVICE_CODE` (line 619: road FTL, rail RAILCONT …)
- What must be true afterwards: The main service fits the cargo and the means (wagon load for ore, container train with a pre-carriage stage for the road leg, bagged cargo for jumbo bags).
- Fix direction: Choose the service from the leg and the cargo type, not the mode alone.
- Depends on / blocks: none
- Findings: ore: 02#F1, 03#F1, 06#F2; plastics: 07#F2; rail: 02#F1, 03#F1, 09#F2

### C36 · Ad valorem indicator and declared carriage value without a valuation
- Kind: encoding · Findings: 5 (High 2, Medium 0, Low 3) in 5 files, 3 flows · Needs decision: none (3 findings marked "yes" go to D46)
- What is wrong: `AdValoremIndicator` and declared carriage values appear where no ad valorem charge or duty exists, and with opposite values for the same air shipment. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `false` (air/03#F3); `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `true` (cotton/09#F7).
- Where it comes from: `tools/examples_kit.py` `waybill()` (line 765); `tools/examples_scenarios.py` lines 1638, 1654
- What must be true afterwards: The indicator and the value appear only together with the charge they concern, the same in every document of a shipment.
- Fix direction: Drop them (preferred in air/03, 04).
- Depends on / blocks: none
- Findings: air: 03#F3, 04#F3; cotton: 09#F7, 13#F6; plastics: 06#F12

### C37 · Order references in the wrong element
- Kind: encoding · Findings: 5 (High 0, Medium 3, Low 2) in 4 files, 3 flows · Needs decision: none
- What is wrong: `SalesOrderID` holds the seller's number of the original order in a buyer's change, a release number sits in `ReleaseID` (delivery-access release), a project name in `CustomerReference`. Example: `air/07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:CustomerReference` = `Harbour parks Selanu` (air/07#F4); `tender/26-Order.xml:/Order/cbc:SalesOrderID` = `VI-SO-26-0058` (tender/26#F4).
- Where it comes from: source not located in one place: the air order change (`tools/examples_scenarios.py` `air()`, line 1940) and the tender call-off enrichments (after line 7151)
- What must be true afterwards: Each order reference element holds what its definition says.
- Fix direction: Correct the values.
- Depends on / blocks: none
- Findings: air: 01#F7, 07#F4; road: 04#F12; tender: 26#F4, 26#F5

### C38 · Bayvarra's surcharge "per month" encoded as one month only
- Kind: encoding · Findings: 5 (High 0, Medium 0, Low 5) in 5 files, 2 flows · Needs decision: none
- What is wrong: All 18 XB-STD terms state "1.5 % surcharge per month late" with a penalty period of one month; four reviews flagged it (conditions#F9 gives the extent). Example: `packaging/02-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1` (packaging/02#F7); `utilities/06-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1` (utilities/06#F7).
- Where it comes from: `tools/examples_kit.py` `payment_terms()`: `PenaltyPeriod/DurationMeasure` 1 MON and `PenaltyAmount` for one month (lines 167–171)
- What must be true afterwards: All 18 places encode the surcharge the same way, and the encoding says "per month" (no end of the period, or a note that the amount is per month).
- Fix direction: Drop the duration (preferred by conditions#F9) in `payment_terms()`; one change fixes all 18.
- Depends on / blocks: none
- Findings: packaging: 02#F7, 04#F7, 07#F7; utilities: 06#F7; consistency: conditions#F9

### C39 · Payment notes that call every document an invoice
- Kind: encoding · Findings: 4 (High 0, Medium 0, Low 4) in 4 files, 2 flows · Needs decision: none
- What is wrong: The payment note of credit notes, debit notes and the deposit asks the payer to quote "invoice …". Example: `furniture/13-CreditNote.xml:/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-CN-26-0579` (furniture/13#F4); `sea/06-OrderResponse.xml:/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice LD-SO-26-0123` (sea/06#F11).
- Where it comes from: `tools/build_examples.py` `account()` (line 611: `PaymentNote`)
- What must be true afterwards: The payment note names the document type it is on.
- Fix direction: Pass the document type into `account()`.
- Depends on / blocks: none
- Findings: furniture: 13#F4, 14#F6; sea: 06#F11, 28#F11

### C40 · Pallets listed as packages contained in themselves
- Kind: encoding · Findings: 3 (High 0, Medium 3, Low 0) in 2 files, 2 flows · Needs decision: none
- What is wrong: Each pallet lists itself as the one package it contains, and the package quantity is used as a number of packages (road/08, retail/12). Example: `retail/12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `PX` (retail/12#F2); `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `KXU104411490000015` (road/08#F15).
- Where it comes from: `tools/examples_kit.py` `handling_units()` (line 1366) and `pallets()` (line 1294)
- What must be true afterwards: A handling unit contains the packages actually on it; quantities count what they say.
- Fix direction: Fix `handling_units()`.
- Depends on / blocks: none
- Findings: retail: 12#F2; road: 08#F15, 08#F16

### C41 · `JourneyID` holding a voyage or month instead of the service schedule
- Kind: encoding · Findings: 3 (High 0, Medium 0, Low 3) in 3 files, 2 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: `JourneyID` (the regular service schedule) holds the barge's voyage number and the pipeline's month. Example: `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031` (plastics/04#F21); `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603` (energy/04#F12).
- Where it comes from: `tools/examples_kit.py` `means()` (line 1206); `tools/examples_scenarios.py` line 8698 (pipeline "KG-P1-2603")
- What must be true afterwards: JourneyID only where a scheduled service exists; a voyage number in the element for it.
- Fix direction: Correct the two values.
- Depends on / blocks: none
- Findings: energy: 04#F12; plastics: 04#F21, 06#F19

### C42 · A line marked both confidential and internal
- Kind: encoding · Findings: 2 (High 0, Medium 0, Low 2) in 2 files, 2 flows · Needs decision: none
- What is wrong: Lines carry `PrivacyCode` "Confidential" and `SecurityClassificationCode` "Internal" at once, two different levels (furniture/01, wood/01). Example: `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL` (furniture/01#F10); `wood/01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL` (wood/01#F7).
- Where it comes from: `tools/examples_scenarios.py` lines 5227 and 5285 (`SecurityClassificationCode` INTERNAL next to a `PrivacyCode`)
- What must be true afterwards: At most one classification per line, consistent with the other.
- Fix direction: Drop one of the two in the scenario code.
- Depends on / blocks: none
- Findings: furniture: 01#F10; wood: 01#F7

### C43 · Temperature code given next to a measured value
- Kind: encoding · Findings: 2 (High 0, Medium 2, Low 0) in 2 files, 2 flows · Needs decision: none
- What is wrong: A temperature carries both a measured value and a code that only qualifies it (mast/02, plastics/09). Example: `mast/02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Temperature/cbc:MeasureCode` = `TARGET` (mast/02#F7); `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:Measure` = `5` (plastics/09#F4).
- Where it comes from: `tools/examples_scenarios.py` lines 5392 and 5879 (`MeasureCode` with a value)
- What must be true afterwards: A temperature is either a value with its attribute or a code, as the element defines.
- Fix direction: Drop `MeasureCode` where the value is given.
- Depends on / blocks: none
- Findings: mast: 02#F7; plastics: 09#F4

### C44 · `VI-C180-2026` replaces a frame in one catalogue and a bench in a tender
- Kind: encoding · Findings: 1 (High 0, Medium 0, Low 1) in 1 file, 0 flows · Needs decision: none
- What is wrong: The same unresolvable identifier replaces the side frame in retail/02 and the whole bench in tender/15. Example: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026` (items#F4).
- Where it comes from: source not located: the replacement item in the retail catalogue and the tender line (`tools/examples_scenarios.py`)
- What must be true afterwards: A replacement identifier means one item, identified somewhere, of the same kind as the item it replaces.
- Fix direction: Drop it from the tender line; identify the 2026 casting by `VI-C180` + extended ID (items#F4 option a).
- Depends on / blocks: none
- Findings: consistency: items#F4

### C45 · `Language/LocaleCode` = `en`
- Kind: world rule · Findings: 213 (High 0, Medium 213, Low 0) in 213 files, 15 flows · Needs decision: owner: D1
- What is wrong: 213 files carry `LocaleCode` `en` with listID ISO 639: a language, not a locale (Medium in every review). Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en` (contest/01#F1); `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en` (energy/04#F3).
- Where it comes from: `tools/build_examples.py` `party()` (lines 136–141: `LocaleCode` from `identity.language`); `tools/examples_scenarios.py` lines 3930, 4850, 6435, 6939
- What must be true afterwards: LocaleCode holds a locale or is absent.
- Fix direction: Decide D1; merge decisions prefer dropping it.
- Depends on / blocks: none
- Note: Conflict with an earlier decision: `analysis/codelist-decisions.md` 6b: "Coded elements (LocaleCode, Language/ID, DefaultLanguageCode) stay plain `en`, because ISO 639 has no region." The merge decisions (Medium, no) contradict it.
- Findings: air (10): 01#F3, 02#F2, 03#F7, 04#F8, 05#F4 …; contest (16): 01#F1, 02#F1, 03#F2, 04#F1, 05#F1 …; cotton (13): 02#F3, 07#F2, 08#F1, 09#F3, 10#F5 …; energy (6): 04#F3, 05#F3, 06#F2, 07#F3, 08#F2 …; furniture (17): 01#F1, 02#F1, 03#F2, 04#F3, 05#F3 …; mast (5): 01#F2, 02#F2, 03#F3, 04#F1, 05#F2; packaging (9): 01#F2, 02#F1, 03#F1, 04#F1, 05#F1 …; plastics (10): 01#F1, 02#F2, 03#F4, 04#F7, 05#F3 …; rail (6): 01#F2, 02#F5, 03#F8, 06#F10, 08#F13 …; retail (22): 01#F2, 02#F3, 03#F4, 04#F3, 05#F3 …; road (17): 01#F2, 02#F2, 03#F1, 04#F4, 05#F6 …; sea (28): 01#F1, 02#F3, 03#F3, 04#F1, 05#F3 …; tender (36): 01#F5, 02#F6, 03#F6, 04#F2, 05#F2 …; utilities (7): 05#F4, 06#F3, 07#F2, 08#F2, 09#F2 …; wood (11): 01#F1, 02#F2, 03#F2, 04#F2, 05#F1 …. Full list in `analysis/worklist-assignments.csv`.

### C46 · English renderings tagged with the issuer's country, Italian names tagged as English, legal form untagged
- Kind: world rule · Findings: 179 (High 0, Medium 0, Low 179) in 123 files, 15 flows · Needs decision: owner: D2
- What is wrong: The same party's English address is `en-XB` in Bayvarran documents and `en-XU`/`en-XL` in its own (277 of 277 tagged rows follow the issuer); the Italian street names of Urvania are tagged English; the legal form is untagged in one rendering. Example: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato` (carnet/01#F9); `plastics/01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo` (plastics/01#F6).
- Where it comes from: `tools/build_examples.py` `language_tag()` (line 1215: the sender's country as region), `city_names()` (line 420), legal form in `legal_entity()` (lines 284–289)
- What must be true afterwards: One stated rule for the language tag of English renderings (and the legal form), applied everywhere.
- Fix direction: Decide D2.
- Depends on / blocks: none
- Note: Conflict with an earlier decision: `analysis/codelist-decisions.md` 6b: "(a) Every sender tags its English texts with its own region: `languageID` `en-XU`, `en-XB` or `en-XL`." and `note/src/03-world.md`: "the inherited Italian names count as English". The documents follow both; the findings ask for a different rule.
- Findings: air (14): 02#F7, 02#F8, 03#F13, 03#F14, 05#F7 …; carnet (8): 01#F9, 01#F15, 02#F5, 02#F7, 03#F5 …; contest (2): 15#F14, 16#F14; cotton (14): 02#F7, 02#F8, 07#F6, 07#F7, 08#F7 …; energy (4): 04#F13, 06#F6, 07#F9, 08#F6; mast (4): 02#F14, 03#F14, 04#F11, 05#F7; packaging (2): 02#F5, 09#F4; plastics (12): 01#F6, 01#F7, 02#F6, 03#F6, 04#F9 …; rail (13): 01#F9, 01#F10, 01#F11, 02#F9, 03#F10 …; retail (1): 02#F19; road (25): 01#F14, 01#F15, 02#F10, 03#F11, 03#F12 …; sea (25): 01#F8, 02#F12, 02#F18, 03#F9, 04#F6 …; tender (32): 03#F42, 03#F43, 12#F10, 12#F11, 13#F15 …; utilities (4): 01#F16, 02#F12, 03#F16, 04#F10; wood (19): 01#F4, 02#F6, 02#F7, 02#F8, 03#F4 …. Full list in `analysis/worklist-assignments.csv`.

### C47 · `FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING for a cradle-to-gate footprint
- Kind: world rule · Findings: 74 (High 0, Medium 74, Low 0) in 40 files, 7 flows · Needs decision: owner: D10
- What is wrong: The bench's footprint carries a system boundary in an element about full transport equipment, and the stage A3 for a figure from the mine to the gate (74 findings in 40 files). Example: `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE` (road/01#F6); `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE` (tender/25#F10).
- Where it comes from: `world/items.json` bench footprint `stage` "MANUFACTURING" and `fullness` "CRADLETOGATE" (lines 207–211); lists in `world/codelists/lists.json` (lines 6492, 6519)
- What must be true afterwards: Elements are used by their UBL definitions.
- Fix direction: Decide D10.
- Depends on / blocks: none
- Note: Conflict with an earlier decision: `analysis/codelist-decisions.md` Q21: "FullnessIndicationCode gets a consistent separate list (CRADLETOGATE …)". The merge decisions (Medium, no: drop) contradict it.
- Findings: carnet (1): 01#F7; rail (6): 01#F5, 01#F6, 06#F7, 06#F8, 11#F2 …; retail (20): 02#F7, 02#F8, 04#F6, 04#F7, 05#F5 …; road (18): 01#F5, 01#F6, 04#F6, 04#F7, 05#F4 …; sea (18): 02#F9, 02#F10, 05#F5, 05#F6, 10#F4 …; tender (10): 25#F9, 25#F10, 26#F7, 26#F8, 29#F5 …; waste (1): 03#F2. Full list in `analysis/worklist-assignments.csv`.

### C48 · Catalogue and product-passport data copied into business documents
- Kind: world rule · Findings: 41 (High 0, Medium 0, Low 41) in 38 files, 8 flows · Needs decision: owner: D11
- What is wrong: The full bench description (properties, emissions, warranty, dimensions, keywords) stands in orders, despatch advices, invoices, customs declarations and till receipts. Example: `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture` (tender/30#F13); `wood/10-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `440799` (wood/10#F5).
- Where it comes from: `tools/build_examples.py` `item()` (line 844) always writes the maker's full item data (brand, properties, certificates, footprint, circularity); customs-relevant item data in `customs_item()` (`tools/examples_kit.py` line 828)
- What must be true afterwards: Each document carries the item data its transaction uses.
- Fix direction: Decide D11.
- Depends on / blocks: none
- Note: Conflict with the world story: `note/src/03-world.md`: "The maker's facts travel with the item wherever it appears: brand and model, properties with their test method and accepted range, certificates, the carbon footprint and the circularity profile." The merge decisions (Low, no) treat it as a fault.
- Findings: carnet: 01#F19; packaging: 09#F7; rail: 01#F14, 06#F24, 11#F8; retail: 05#F11, 07#F11, 08#F13, 12#F13, 17#F17, 18#F16, 19#F10, 19#F14, 21#F15; road: 01#F13, 04#F14, 05#F13, 06#F18, 06#F20, 07#F19, 07#F20, 10#F16, 11#F11, 13#F16, 15#F11; sea: 05#F16, 10#F9, 11#F12, 19#F17, 20#F13, 21#F13, 22#F15, 29#F5; tender: 26#F17, 29#F16, 30#F13, 31#F16, 32#F24, 33#F24; wood: 10#F5, 11#F6

### C49 · Signature aggregates with only an ID and a signatory
- Kind: world rule · Findings: 38 (High 0, Medium 1, Low 37) in 38 files, 4 flows · Needs decision: owner: D6
- What is wrong: 137 of 147 Signature aggregates carry only an ID and a signatory party, no method, time or attached signature. Example: `retail/08-Order.xml:/Order/cac:Signature/cbc:ID` = `BM-SIG-26-0424` (retail/08#F17); `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Signature/cbc:ID` = `TWL-SIG-CTR` (sea/16#F24).
- Where it comes from: `tools/examples_kit.py` `tep()` (line 715) and `waybill()` (line 784); `tools/examples_scenarios.py` `full_signature()` (line 4822) and inline signatures (e.g. lines 1006, 1797, 1878)
- What must be true afterwards: A Signature says what was signed, how and when, or is absent.
- Fix direction: Decide D6 (merge decisions: Low, yes).
- Depends on / blocks: none
- Findings: air: 02#F11, 03#F17, 04#F20, 05#F11, 07#F9, 09#F9; retail: 01#F9, 02#F9, 03#F6, 04#F9, 05#F7, 06#F8, 07#F7, 08#F17, 09#F6, 10#F7, 13#F12, 14#F11, 17#F9, 20#F5, 21#F8; sea: 01#F6, 03#F2, 04#F5, 07#F5, 08#F9, 10#F19, 15#F17, 16#F24, 17#F10, 19#F21, 20#F17, 21#F16; utilities: 04#F9, 07#F10, 08#F9, 10#F4, 14#F5

### C50 · Tax category O for goods, 0 % on O, and Lisavu's tax scheme without ID
- Kind: world rule · Findings: 29 (High 0, Medium 6, Low 23) in 13 files, 4 flows · Needs decision: owner: D15
- What is wrong: Lisavan sales of goods use category O "Services outside scope of tax"; O is given with a 0 % rate and, for levies, with an exemption reason; the Lisavan scheme has a name and no ID. Example: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O` (cotton/01#F2); `utilities/06-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY` (utilities/06#F5).
- Where it comes from: `tools/examples_kit.py` `tax_rule()` (line 72) and `tax_category()` (lines 115–135; scheme name "No general sales tax" without ID, line 133)
- What must be true afterwards: Goods outside any sales tax use a category that fits goods (or the world states that O covers them); no percent on O; a scheme with an identifier or none.
- Fix direction: Decide D15 (merge decisions: "Tax category O … used for goods", Medium, yes).
- Depends on / blocks: none
- Findings: cotton: 01#F2, 01#F8, 01#F9, 04#F6, 04#F21, 04#F22, 05#F7, 05#F22, 05#F23, 08#F2, 08#F11, 08#F12, 08#F13, 16#F2, 16#F4, 16#F5; road: 14#F12; sea: 28#F15, 29#F2, 29#F13; utilities: 06#F4, 06#F5, 09#F8, 09#F9, 11#F6, 11#F7, 12#F17, 13#F7, 13#F8

### C51 · Contract payment terms never applied by the invoices under the contract
- Kind: world rule · Findings: 12 (High 10, Medium 0, Low 2) in 10 files, 4 flows · Needs decision: owner: D22
- What is wrong: The framework transport plans (ore, rail, plastics) say "30 days net from the consignment note" and the tender contract "30 days after each accepted release", but every invoice under them applies XU-STD (30 days from the invoice, 2 % discount, 8 % interest); the reminder and remittance follow. Example: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` (ore/03#F4); `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` (plastics/04#F2).
- Where it comes from: `tools/examples_kit.py` `payment_terms()` (line 150) always applies the seller's country terms; the contracts' own terms in `tep_terms()` (line 646) and the tender `tendering_terms()` (`tools/examples_scenarios.py` line 6283)
- What must be true afterwards: An invoice under a contract applies the contract's terms; standard terms only where no contract terms exist.
- Fix direction: Decide D22. conditions#F3 prefers (a) invoices follow the contract.
- Depends on / blocks: none
- Note: Conflict with the world story: `note/src/03-world.md` says "Each country also has its own payment practice, which every invoice of a seller there follows." The generator does exactly that; the reviews (and conditions#F3, "Needs decision: no") want the contract to win.
- Findings: ore: 03#F4, 06#F1; plastics: 04#F2, 07#F1, 07#F4; rail: 03#F4, 10#F1, 10#F3; tender: 27#F1, 32#F5, 35#F1; consistency: conditions#F3

### C52 · Customs value on a different basis in each flow
- Kind: world rule · Findings: 12 (High 1, Medium 6, Low 5) in 12 files, 6 flows · Needs decision: owner: D16
- What is wrong: Bayvarra alone values imports on four bases (freight to destination added in plastics, FCA/FOB without freight in road and cotton, a delivered price in tender); document-level charges (colour, pallets) are never in the value; the sea bill of lading declares a CIF value the import declaration does not use. Example: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00` (sea/14#F3); `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000` (tender/30#F4).
- Where it comes from: `tools/examples_kit.py` `goods_items()` (line 844, value = the goods lines of the invoice); `tools/examples_scenarios.py` `cif_value()` (line 1154) and `goods_items()` (line 87)
- What must be true afterwards: Each country's customs values follow one stated basis, applied in every declaration; charges that are part of the price are treated the same way everywhere.
- Fix direction: Decide D16 (preferred by conditions#F5: CIF-type value at the importing border for all three countries).
- Depends on / blocks: none
- Findings: cotton: 10#F9, 15#F4; plastics: 05#F10, 09#F6; rail: 06#F17; sea: 14#F3, 19#F6; tender: 30#F4, 31#F6; wood: 05#F3, 07#F4; consistency: conditions#F5

### C53 · Documents dated at the weekend against a Monday-to-Friday week
- Kind: world rule · Findings: 12 (High 1, Medium 2, Low 9) in 12 files, 6 flows · Needs decision: owner: D27
- What is wrong: By the count of conditions#F7, 48 documents (19 %) are issued on a Saturday or Sunday by offices whose contacts say "Weekdays 08:00–17:00"; contact hours also exclude the times goods are at the border or a ship arrives. Example: `retail/21-PurchaseReceipt.xml:/PurchaseReceipt/cbc:Note` = `Home delivery booked for Saturday.` (retail/21#F2); `tender/09-ProcurementStatus.xml:/ProcurementStatus/cbc:IssueDate` = `2026-02-21` (conditions#F7).
- Where it comes from: the flows' start dates and day offsets in `tools/examples_scenarios.py` (`kit.Flow(…)` lines 25–8894 and the day argument of each document); contact hours in `world/parties.json` (`hours`, e.g. line 28)
- What must be true afterwards: Documents of people or offices with weekday hours fall on weekdays, or the world states that systems issue at any time.
- Fix direction: Decide D27; then a build check on the weekday of issue dates per issuer kind.
- Depends on / blocks: none
- Findings: cotton: 14#F5; rail: 07#F7; retail: 07#F2, 21#F2; road: 05#F15, 07#F11, 10#F14; sea: 15#F9; tender: 05#F5, 09#F4, 10#F4; consistency: conditions#F7

### C54 · Bayvarran withholding tax and tax representative only in the tender, and Urvania's "service to a business abroad" for a public body
- Kind: world rule · Findings: 10 (High 0, Medium 2, Low 8) in 5 files, 1 flow · Needs decision: owner: D17
- What is wrong: The tender notices state Bayvarran exemption PUBLIC; the winner's invoices apply Urvanian VAT (EXP, SVCABROAD) plus a Bayvarran 10 % withholding on the installation collected through a tax representative, which no other non-resident supplier into Bayvarra has; SVCABROAD ("to a business") is used for the public works department. Example: `tender/35-Reminder.xml:/Reminder/cac:PrepaidPayment/cbc:ID` = `XB-WHT-26-04-1187` (tender/35#F4); `tender/02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC` (conditions#F4).
- Where it comes from: `tools/examples_scenarios.py` `withholding()` (line 2333) and the tender invoices; `tools/examples_kit.py` `tax_rule()` (line 72)
- What must be true afterwards: One visible rule for Bayvarran taxes on non-residents' supplies, applied the same way in tender and road; the notices describe the treatment the invoices use.
- Fix direction: Decide D17.
- Depends on / blocks: none
- Note: `note/src/03-world.md` states the rule: "A public body in Bayvarra withholds 10 % of the price of a service from a business not established there and pays it to the state; such a supplier names a tax representative in Bayvarra." That supports conditions#F4 option (a) and contradicts its preferred option (c) "drop the withholding"; road/14 (a company customer) is consistent with the story.
- Findings: tender: 32#F15, 33#F15, 33#F16, 34#F7, 34#F8, 34#F10, 35#F4, 35#F10; consistency: conditions#F4, conditions#F8

### C55 · Standard terms IDs that do not mean the same number of days everywhere
- Kind: world rule · Findings: 8 (High 8, Medium 0, Low 0) in 8 files, 4 flows · Needs decision: owner: D23
- What is wrong: XU-STD/XB-STD say 30 days and XL-STD 45 days, but the utilities are due in 21 days under all three IDs, and the Bayvarra–Lisavu invoices use the buyer's period under the seller's text. Example: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27` (cotton/01#F1); `mast/05-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-06-04` (mast/05#F1).
- Where it comes from: `tools/examples_kit.py` `payment_terms()` (line 150: due date = issue day + `due_days` passed by each caller); `world/countries.json` `payment` per country; the 21-day utilities calls in `tools/examples_scenarios.py` `utilities()` (line 2998)
- What must be true afterwards: One terms ID, one text, one period; every due date follows from the terms the document cites.
- Fix direction: Decide D23 (preferred by conditions#F2: own terms ID for utilities, correct the three cross-border dates); derive `due_days` from the terms, not from the caller; build check due date − issue date = terms period.
- Depends on / blocks: none
- Findings: cotton: 01#F1, 16#F1; mast: 05#F1; sea: 22#F1; utilities: 02#F2, 06#F1, 13#F1; consistency: conditions#F2

### C56 · The map scale: all coordinates inside 35 km, against distances and times of hours and days
- Kind: world rule · Findings: 8 (High 4, Medium 0, Low 4) in 7 files, 2 flows · Needs decision: owner: D19
- What is wrong: Coordinates are computed from map tiles at 0.01° per tile, so Lumeport and Selanu are 6 km (3.2 nm) apart and the whole world fits in 21 × 32 km, while the documents state two days at sea, a three-hour flight, 186 km by road and a ballast exchange 120 nm off Selanu. Example: `energy/06-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.` (energy/06#F5); `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2` (sea/08#F3).
- Where it comes from: `world/countries.json` `geography.degrees_per_tile` = 0.01 (line 619) and `origin`; `tools/build_examples.py` `coordinate()` (line 510); `world/map.json` tiles
- What must be true afterwards: Coordinates, stated distances (km, nm) and durations agree within plausible speeds per mode.
- Fix direction: Decide the scale (D19); preferred by timelines#F1: scale the coordinates (one constant), because distances and durations are spread over many documents.
- Depends on / blocks: blocks C58; the map rendering on the site uses the same tiles
- Findings: energy: 04#F8, 05#F8, 06#F5, 07#F8; sea: 08#F3, 16#F2, 16#F3; consistency: timelines#F1

### C57 · Duties, import taxes and Trade Accord preference stated nowhere
- Kind: world rule · Findings: 6 (High 1, Medium 2, Low 3) in 5 files, 4 flows · Needs decision: owner: D18
- What is wrong: Every import says duties were paid without a duty, rate or amount; preference is claimed once (plastics), certified but not claimed in road, ignored elsewhere; the carnet reminder claims 1,300 coral of duties and consumption tax on goods worth 399.20 XLC. Example: `carnet/03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000` (carnet/03#F1); `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P` (conditions#F6).
- Where it comes from: `tools/examples_scenarios.py` `import_extras()` (note "Duties paid by the importer's account at customs.", line 4597); preference only in the plastics import (line 868)
- What must be true afterwards: Import declarations state, per country, whether duty and import tax are due on Accord-origin goods (amount, or a preference claim with criterion and proof).
- Fix direction: Decide D18.
- Depends on / blocks: none
- Note: `note/src/03-world.md` already says: "Lisavu (XL) has no general sales tax. Customs collects a customs duty and an import consumption tax when goods enter the island." and codelist-decisions Q24 "tariffs, rates and exemptions stay national". So the Lisavan import tax of carnet/03 agrees with the story; conditions#F6 lists it as an open question.
- Findings: carnet: 03#F1, 03#F2; plastics: 09#F7; road: 10#F11; tender: 31#F13; consistency: conditions#F6

### C58 · One sea voyage with four passage times
- Kind: world rule · Findings: 4 (High 2, Medium 1, Low 1) in 3 files, 1 flow · Needs decision: owner: D19
- What is wrong: Voyage `TH-26-19E` takes two days (service), 64 h (manifest estimate, issued after the actual departure), 84 h (actual) and is 40 nm off Selanu at 13.5 kn on 16 May although it arrives on 18 May. Example: `sea/15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15` (sea/15#F1); `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2` (timelines#F5).
- Where it comes from: `tools/examples_scenarios.py` sea flow (`sea()` line 1527; manifest, status and pre-arrival report dates and times)
- What must be true afterwards: Service duration, estimate, reporting position and actual times describe one passage, or a stated event explains the difference.
- Fix direction: Settle with D19, then derive estimate, position and arrival.
- Depends on / blocks: after C56 (D19)
- Findings: sea: 15#F1, 16#F1, 16#F17; consistency: timelines#F5

### C59 · Lisavu's capital: "Port Wrenfield" in English addresses, "Selanu" in every other English text
- Kind: world rule · Findings: 1 (High 0, Medium 1, Low 0) in 1 file, 0 flows · Needs decision: owner: D3
- What is wrong: The 12 Lisavan parties' English addresses say Port Wrenfield; about 140 party names, place names and texts say Selanu. Example: `sea/05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[1]` = `Selanu` (parties#F1).
- Where it comes from: `world/countries.json` `english_place_names` ("Selanu": "Port Wrenfield", lines 1711–1713); `tools/build_examples.py` `city_names()` (line 432); party and place names in `world/parties.json`
- What must be true afterwards: In English the town has one name, or the documents say once that Port Wrenfield is Selanu's English name.
- Fix direction: Decide D3.
- Depends on / blocks: none
- Note: `note/src/03-world.md`: "Selanu is also *Port Wrenfield*"; "An address gives both, Lisavan first." The addresses follow the story; parties#F1 option (a) (Selanu in English addresses) would change the story.
- Findings: consistency: parties#F1

### C60 · Default founding date 1996-01-01 and size classes that do not fit the parties
- Kind: master data · Findings: 181 (High 4, Medium 0, Low 177) in 169 files, 15 flows · Needs decision: owner: D4
- What is wrong: 25 unrelated companies were registered on 1 January 1996 and are all SMALL, including both national ports, the state water company, the telecom operator and the rail operator; the sawmill states 85 employees but is SMALL; Valdara is LARGE with 180 persons; operating years contradict the registration (tender/04, 07, 13). Example: `contest/09-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (contest/09#F14); `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (retail/02#F20).
- Where it comes from: `world/parties.json` `identity.legal.founded` = "1996-01-01" for 25 parties (e.g. line 209) with low `headcount`/`turnover`; the size follows from them in `tools/codelists.py` `entity_size()` (line 266)
- What must be true afterwards: Every party's founding date and size class are its own and consistent with the figures the documents state.
- Fix direction: Decide D4 (per party a date, headcount and turnover), then the size follows by the existing rule.
- Depends on / blocks: none
- Findings: air (10): 01#F11, 02#F9, 03#F15, 04#F18, 05#F9 …; contest (12): 04#F8, 05#F8, 06#F9, 07#F6, 09#F14 …; cotton (19): 01#F4, 02#F5, 03#F9, 04#F16, 05#F18 …; furniture (17): 01#F4, 02#F4, 03#F4, 04#F6, 05#F6 …; mast (6): 01#F11, 01#F12, 02#F12, 03#F13, 04#F9 …; packaging (8): 01#F5, 02#F3, 03#F4, 04#F5, 05#F5 …; plastics (11): 01#F3, 02#F3, 03#F7, 04#F10, 05#F6 …; rail (9): 02#F12, 03#F11, 04#F5, 05#F7, 06#F25 …; retail (10): 02#F17, 02#F20, 11#F7, 12#F16, 13#F11 …; road (10): 01#F9, 03#F7, 04#F10, 05#F11, 08#F21 …; sea (14): 01#F9, 02#F14, 03#F10, 04#F7, 05#F9 …; tender (28): 03#F41, 04#F1, 04#F6, 04#F7, 05#F1 …; utilities (11): 03#F14, 05#F8, 06#F11, 07#F9, 08#F10 …; waste (3): 01#F13, 02#F16, 03#F10; wood (11): 01#F3, 02#F5, 03#F7, 04#F6, 05#F5 …; consistency (2): conditions#F12, parties#F2. Full list in `analysis/worklist-assignments.csv`.

### C61 · World item numbers that are valid GTIN-12s; Valdara's items under Lumeway's GS1 prefix
- Kind: master data · Findings: 76 (High 0, Medium 0, Low 76) in 54 files, 9 flows · Needs decision: owner: D5
- What is wrong: The world item numbers have the form and check digit of GTIN-12s in a real US/Canada range; the distributor gives the manufacturer's branded bench and frame GTINs under its own prefix, so one item has two standard identities (items#F2). Example: `packaging/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103` (packaging/01#F8); `retail/04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008` (retail/04#F14).
- Where it comes from: `world/items.json` `standard_id` (e.g. "771020000027", line 44) and the GS1 items of the GS1-convention parties in `world/parties.json` `identification`
- What must be true afterwards: One standard identification per item that all sellers use, or a stated rule; fictional numbers not mistakable for real GTINs.
- Fix direction: Decide D5.
- Depends on / blocks: none
- Note: Conflicts: `note/src/03-world.md`: "where the maker has no GTIN, the GS1 distributor gives the item one of its own, as GS1 allows a wholesaler or importer to do, and the maker's Codana number travels with it"; `analysis/codelist-decisions.md` ID-Q4: "item numbers with a non-company GS1 prefix (world scheme, check digit kept)". Both choices are deliberate.
- Findings: carnet (1): 01#F20; ore (3): 01#F6, 04#F6, 07#F3; packaging (11): 01#F8, 02#F9, 03#F7, 04#F8, 05#F8 …; plastics (5): 01#F10, 05#F11, 08#F9, 09#F19, 10#F8; rail (3): 01#F15, 06#F26, 11#F12; retail (20): 02#F16, 02#F21, 04#F14, 04#F15, 05#F12 …; road (9): 01#F12, 04#F13, 05#F12, 06#F19, 07#F21 …; sea (20): 02#F16, 02#F20, 05#F17, 05#F18, 10#F17 …; tender (3): 25#F21, 26#F21, 29#F22; consistency (1): items#F2. Full list in `analysis/worklist-assignments.csv`.

### C62 · The maker's brand on the store's own-line garden set
- Kind: master data · Findings: 12 (High 0, Medium 0, Low 12) in 12 files, 1 flow · Needs decision: owner: D7
- What is wrong: The store sells the set under its own line, but every document gives Brackenmere's brand (furniture, 12 files). Example: `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cbc:Note` = `For the store's own garden line.` (furniture/01#F11).
- Where it comes from: `world/items.json` garden bench set (BF-GS-01) brand, as written by `tools/build_examples.py` `item()`
- What must be true afterwards: The brand is the brand under which the item is sold, or the story says the store sells the maker's brand.
- Fix direction: Decide D7.
- Depends on / blocks: none
- Findings: furniture: 01#F11, 02#F2, 03#F7, 04#F8, 05#F9, 06#F9, 07#F12, 08#F9, 09#F4, 10#F7, 12#F5, 13#F6

### C63 · Lisavu Cotton Farm: address lines that repeat the structured address, and a yearly expiring registration
- Kind: master data · Findings: 11 (High 0, Medium 0, Low 11) in 6 files, 2 flows · Needs decision: owner: D4
- What is wrong: The farm's `AddressLine`s repeat the structured address and mix two languages in one line; its commercial-register entry has an expiry date. Example: `cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road` (cotton/04#F25); `sea/29-PurchaseReceipt.xml:/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road` (sea/29#F7).
- Where it comes from: `world/parties.json` Lisavu Cotton Farm (`identity.address` lines, `legal.registration_expires`); `tools/build_examples.py` `legal_entity()` (line 292: "The island renews a farm's registration every year")
- What must be true afterwards: Address lines only where the structured address cannot carry the information; the registration has an expiry only if the world's register expires.
- Fix direction: Address part: no decision (fix the lines). Expiry: part of D4.
- Depends on / blocks: none
- Findings: cotton: 01#F6, 01#F7, 03#F5, 03#F6, 04#F25, 04#F26, 05#F26, 05#F27, 06#F4, 06#F7; sea: 29#F7

### C64 · Industry classes that leave out what the party does
- Kind: master data · Findings: 9 (High 0, Medium 0, Low 9) in 9 files, 2 flows · Needs decision: owner: D8
- What is wrong: The mast operator is classified as wired telecommunications; Ferrano Energy's and Ferrano Grid's class covers electricity only, in a gas statement. Example: `mast/01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110` (mast/01#F10); `energy/01-UtilityStatement.xml:/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510` (energy/01#F8).
- Where it comes from: `world/parties.json` `identity.industry` (Selanu Telecom 6110, line 2581; Ferrano Energy and Ferrano Grid 3510)
- What must be true afterwards: Each party's ISIC class fits what it does in the documents.
- Fix direction: Decide D8 (which class per party), then change parties.json.
- Depends on / blocks: none
- Findings: energy: 01#F8, 02#F5, 03#F5, 07#F6; mast: 01#F10, 02#F13, 03#F15, 04#F10, 05#F13

### C65 · Bale weight of about 227 kg as `PackSizeNumeric`
- Kind: master data · Findings: 7 (High 0, Medium 0, Low 7) in 7 files, 1 flow · Needs decision: owner: D12
- What is wrong: `PackQuantity` 1 / `PackSizeNumeric` 227 give the nominal bale weight as a pack size in seven cotton documents. Example: `cotton/10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackQuantity` = `1` (cotton/10#F7).
- Where it comes from: `world/items.json` cotton lint (lines 938–947: `per_package` 227, size "227")
- What must be true afterwards: Pack size counts units in a pack; the bale weight is a weight.
- Fix direction: Decide D12 (what the pack is), then fix items.json.
- Depends on / blocks: none
- Findings: cotton: 02#F9, 07#F9, 08#F14, 10#F7, 11#F4, 15#F5, 16#F7

### C66 · Debit notes with accounting supplier and customer reversed
- Kind: master data · Findings: 5 (High 5, Medium 0, Low 0) in 5 files, 3 flows · Needs decision: owner: D9
- What is wrong: In all three debit notes the document number and language tag name the real issuer, but the accounting supplier is the party that is charged; the tender reminder and remittance then enter the debit as a credit. Example: `furniture/14-DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture` (furniture/14#F1); `sea/28-DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution` (sea/28#F1).
- Where it comes from: `world/documents.json` the three DebitNote entries (furniture, sea, tender): `parties` `AccountingSupplierParty` = the party debited
- What must be true afterwards: The issuer of a debit note (the creditor) is its accounting supplier.
- Fix direction: Swap the two roles in documents.json; the merge decisions mark it "yes" ("probably one pattern in the generator"), so it is put to the owner as D9.
- Depends on / blocks: none
- Findings: furniture: 14#F1; sea: 28#F1; tender: 34#F1, 35#F3, 36#F1

### C67 · Side frame classified HS 7325.99 instead of a part of a seat
- Kind: master data · Findings: 5 (High 0, Medium 4, Low 1) in 5 files, 2 flows · Needs decision: owner: D13
- What is wrong: The spare side frame is classified as a general cast article; the reviews say a part of a seat (9401.99). Example: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599` (sea/02#F11); `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599` (retail/02#F24).
- Where it comes from: `world/items.json` side frame `hs` "732599" (line 241), `national_tariff` "73259990" (line 253)
- What must be true afterwards: The frame's heading follows the Harmonized System's notes for parts of seats.
- Fix direction: Decide D13.
- Depends on / blocks: none
- Note: Conflict with an earlier decision: `analysis/codelist-decisions.md` P5 confirmed "7325.99 → 42999 "Metal goods n.e.c." (bench casting)". The merge decisions (Medium, no: 9401.99) contradict it.
- Findings: retail: 02#F24; sea: 02#F11, 05#F7, 10#F6, 11#F5

### C68 · Valdara's distributor price equals its public contract price; Lumeway's revised frame price is below cost
- Kind: master data · Findings: 1 (High 0, Medium 0, Low 1) in 1 file, 0 flows · Needs decision: owner: D14
- What is wrong: Valdara sells to its distributor at the price it tenders to the public buyer in the distributor's own city; the revised frame price is below the purchase price. Example: `road/15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `49900` (conditions#F11).
- Where it comes from: `world/items.json` prices of the bench and frame per seller (Valdara 49900 XUF; Lumeway price list `LD-PL-2026`, revision 58 XBL)
- What must be true afterwards: The price chain is plausible or the documents give the reason.
- Fix direction: Decide D14.
- Depends on / blocks: none
- Findings: consistency: conditions#F11

### C69 · The bench as shipped: pallets that do not fit, and a bench lighter than its parts
- Kind: cross-flow story · Findings: 7 (High 1, Medium 3, Low 3) in 6 files, 3 flows · Needs decision: owner: D20
- What is wrong: Four assembled benches (1800 × 620 × 780 mm) do not fit the 1850 × 650 × 1650 mm pallet, 24 such pallets fit neither the trailer nor a 40-foot container; and the bench weighs less than its five slats and two side frames as other flows ship them. Example: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:Quantity` = `24` (sea/05#F1); `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MeasurementDimension/cbc:Measure` = `13.6` (road/08#F12).
- Where it comes from: `world/items.json` bench dimensions and `gross_kg` 41.5 (line 55); `tools/examples_kit.py` `pallets()` (line 1294) and `handling_units()` (line 1366)
- What must be true afterwards: Pallet size, stacking and counts fit each hold; the bench's gross weight is at least the weight of its parts.
- Fix direction: Decide D20 (preferred: knocked down, flat-pack pallet size; heavier bench).
- Depends on / blocks: none
- Findings: rail: 06#F15, 08#F16; road: 08#F12, 08#F17; sea: 05#F1; consistency: equipment#F1, items#F3

### C70 · One melt, one coating batch and one manufacture time for every casting and lot
- Kind: cross-flow story · Findings: 6 (High 3, Medium 0, Low 3) in 4 files, 2 flows · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: All castings carry melt `M-26-0412` although made on 20 March, 10 and 11 May; serials run against manufacture dates; one coating batch for four bench lots; the replacement despatch advice gives the same castings a manufacture date a day later. Example: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-03190` (air/06#F14); `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cac:AdditionalItemProperty/cbc:Value` = `M-26-0412` (timelines#F2).
- Where it comes from: `world/items.json` coating batch "ZN-26-114" (line 225) and melt "M-26-0412" (line 260); `tools/examples_kit.py` `instances()` (line 355: manufacture time 06:40, serials)
- What must be true afterwards: One melt and coating batch per production event, serials ascending with the date, the same casting with the same data in every document.
- Fix direction: Derive melt, batch and serial from the lot's production day (timelines#F2 option a).
- Depends on / blocks: after C71 (D21), which may change the lots
- Findings: air: 06#F3, 06#F14, 08#F4, 08#F16; road: 04#F16; consistency: timelines#F2

### C71 · Goods "from the distributor's stock" made days before they leave, and no document moves them
- Kind: cross-flow story · Findings: 4 (High 1, Medium 1, Low 2) in 4 files, 1 flow · Needs decision: owner: D21
- What is wrong: The retail, sea and air lots are made in Urvania two or three days before Lumeway despatches them from Marrowdale "from stock"; only the road (March) and rail (April) deliveries move goods to Lumeway; the sea export cites the March road import as its previous declaration for goods made in May. Example: `sea/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `LD-IM-26-0161` (items#F1); `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.` (sea/20#F16).
- Where it comes from: the lots and manufacture dates of the sea, air and retail goods: `tools/examples_kit.py` `instances()` (line 355) with the despatch days of `sea()`, `air()` and `retail()` in `tools/examples_scenarios.py`
- What must be true afterwards: Every lot Lumeway despatches was made before a documented delivery to Lumeway, or the documents say how it arrived.
- Fix direction: Decide D21 (preferred by timelines#F4: give the later goods lots of the existing deliveries).
- Depends on / blocks: with C70; C12 (sea/11 previous declaration)
- Findings: sea: 20#F16, 29#F11; consistency: items#F1, timelines#F4

### C72 · Documents that report or cite what happens after their own issue time
- Kind: generator mechanism · Findings: 38 (High 30, Medium 1, Low 7) in 32 files, 9 flows · Needs decision: none (5 findings marked "yes" go to D46)
- What is wrong: Issue times are spread pseudo-randomly between 08:00 and 18:00, so waybills report pickups in the afternoon of their morning issue, status reports cite waybills issued later, a cancellation follows its replacement, and revisions are dated after the issue (ten flows; 30 High). Example: `energy/01-UtilityStatement.xml:/UtilityStatement/cbc:IssueDate` = `2026-04-02` (energy/01#F5); `utilities/08-UtilityStatement.xml:/UtilityStatement/cbc:IssueTime` = `15:10:00` (utilities/08#F8).
- Where it comes from: `tools/build_examples.py` main loop: `IssueTime` from a hash of flow and number when the scenario gives none (lines 1704–1707); the days and times set per document in `tools/examples_scenarios.py`
- What must be true afterwards: No document reports as actual, or cites, anything dated after its issue time; transport documents are issued at the moment their type implies.
- Fix direction: Derive issue times from the events and references of the flow (issue after the latest event or document cited), with the scenario overriding; build check: no actual event or referenced document after the issue timestamp (`check_consistency.py` group 10 already lists them).
- Depends on / blocks: none
- Note: Includes timelines#F6 (export declarations after the goods left) and #F8.
- Findings: air: 04#F4, 05#F1, 07#F1, 08#F1, 09#F2, 10#F5; energy: 01#F5; plastics: 06#F1; rail: 05#F1, 08#F3, 08#F5; retail: 03#F1, 04#F1, 04#F8, 06#F1, 09#F1, 10#F1, 12#F4, 16#F5; road: 04#F1, 08#F1, 08#F3, 09#F1, 10#F1, 14#F1, 16#F1; sea: 03#F1, 13#F1, 22#F2, 28#F3; tender: 17#F2, 18#F1, 19#F1, 19#F2; utilities: 08#F8; consistency: timelines#F3, timelines#F6, timelines#F8

### C73 · References to documents under IDs no document has, or to documents the flow does not contain
- Kind: generator mechanism · Findings: 27 (High 20, Medium 3, Low 4) in 25 files, 8 flows · Needs decision: owner: D38
- What is wrong: References carry IDs no example carries: an air order that does not exist, the call for tenders under a file number in eight tender documents, replaced notices for first notices, a consignment ID as document reference; others point to documents the flow does not model (waste weight statement, furniture delivery note, retail transport plan). Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0319` (air/03#F1); `tender/15-Tender.xml:/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT` (tender/15#F1).
- Where it comes from: reference values in the scenario code: the air order `VT-PO-26-0319` (`tools/examples_scenarios.py` `air()`, line 1940), the tender call for tenders `PWD-2026-PARKS-CFT` and replaced notices (tender enrichments, lines 6476–6560), the waste weight statement (`waste()`, line 2512)
- What must be true afterwards: Every reference to an example resolves to it; a reference to a document outside the examples says what it is.
- Fix direction: Wrong IDs: correct them (no decision). Missing documents: decide per flow whether to add them (D38). Build check: `flow_index.py`'s "-> ?" references reported by the build.
- Depends on / blocks: none
- Findings: air: 03#F1, 06#F1, 08#F2; furniture: 09#F1; ore: 02#F10, 03#F15; rail: 07#F1, 09#F4; retail: 01#F1, 06#F2, 14#F1, 18#F12; sea: 13#F3; tender: 01#F3, 02#F3, 02#F4, 03#F3, 03#F4, 06#F1, 13#F13, 15#F1, 17#F1, 18#F2, 19#F4, 24#F2, 28#F1; waste: 02#F1

### C74 · Document numbers: one counter per flow shared by all issuers
- Kind: generator mechanism · Findings: 10 (High 2, Medium 1, Low 7) in 8 files, 3 flows · Needs decision: owner: D24
- What is wrong: Every flow uses one block of consecutive numbers shared by all its issuers, so no issuer numbers its own documents in order (Lumeway's invoice of 30 April is 0236, of 14 May 0147); the same remittance number is used by three payers in utilities; the department's numbers run against its issue times. Example: `road/06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1` (road/06#F22); `utilities/07-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316` (utilities/07#F1).
- Where it comes from: `tools/examples_kit.py` `Flow.number()` (lines 52–57: `{initials}-{type}-26-{base + count}`, `base` from a CRC of the flow name)
- What must be true afterwards: Per issuer (and type, if wanted) numbers rise with the issue timestamp across flows.
- Fix direction: Decide D24, then one counter per issuer in `Flow.number()` built in global issue order.
- Depends on / blocks: none
- Findings: road: 06#F22, 07#F23; tender: 06#F9, 22#F6; utilities: 01#F15, 07#F1, 07#F3, 14#F1, 14#F3; consistency: identifiers#F2

### C75 · Issuer prefixes: `BF` for two parties, second prefixes for signatures
- Kind: generator mechanism · Findings: 4 (High 0, Medium 1, Low 3) in 3 files, 1 flow · Needs decision: owner: D25
- What is wrong: Bayforth Forwarding and Brackenmere Furniture both get `BF` (invoices, items, signatures, RF references); seven parties sign under a second prefix; one prefix-plus-infix stands for two kinds of document. Example: `tender/04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI` (tender/04#F10); `cotton/17-Invoice.xml:/Invoice/cbc:ID` = `BF-INV-26-0211` (identifiers#F1).
- Where it comes from: `tools/examples_kit.py` `initials()` (line 36); hard-coded signature prefixes in the scenarios (e.g. "BM-SIG", "PWD-SIG", "HS-SIG")
- What must be true afterwards: Every prefix belongs to one party; each party uses one prefix; one infix means one kind.
- Fix direction: Decide D25 (e.g. a fixed prefix per party in parties.json).
- Depends on / blocks: none
- Findings: tender: 04#F10, 10#F5; consistency: identifiers#F1, identifiers#F5

### C76 · `ProfileExecutionID` is the flow name in all 250 documents
- Kind: generator mechanism · Findings: 1 (High 0, Medium 1, Low 0) in 1 file, 0 flows · Needs decision: owner: D26
- What is wrong: One execution ID per flow joins unrelated collaborations and documents of different profiles. Example: `packaging/01-Order.xml:/Order/cbc:ProfileExecutionID` = `PACKAGING-2026-01` (identifiers#F3).
- Where it comes from: `tools/build_examples.py` main loop (lines 1701–1703: `{FLOW}-2026-01`)
- What must be true afterwards: Each ProfileExecutionID identifies one execution of the document's profile, or is absent.
- Fix direction: Decide D26.
- Depends on / blocks: none
- Note: Conflict with an earlier decision: `analysis/codelist-decisions.md`: "ProfileExecutionID: stays one per flow instance." and `note/src/03-world.md`: "`ProfileExecutionID` still names the run of the process".
- Findings: consistency: identifiers#F3

### C77 · Waste flow: a transboundary notification for a movement inside one town; no weighbridge statement
- Kind: flow story · Findings: 19 (High 1, Medium 6, Low 12) in 3 files, 1 flow · Needs decision: owner: D42
- What is wrong: The notification and movement are addressed to the customs administration's border office for a movement inside Ferrano; Rinova is named a disposal facility in a recovery notification; 38–40 t of bagged PE in one road load; the planned shipment reuses the first movement's IDs; the weight statement the movement and the invoice rest on does not exist; the invoice bills gross tonnes. Example: `waste/01-WasteNotification.xml:/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage` (waste/01#F12).
- Where it comes from: `tools/examples_scenarios.py` `waste()` (line 2512) and `waste_shipment()` (line 2502)
- What must be true afterwards: The flow tells one plausible domestic (or transboundary) story with the competent authority, a recovery facility, plausible loads and a traceable billed net weight.
- Fix direction: Decide D42 (domestic vs transboundary, weight statement added).
- Depends on / blocks: none
- Findings: waste: 01#F1, 01#F2, 01#F4, 01#F5, 01#F6, 01#F7, 01#F12, 01#F14, 02#F2, 02#F3, 02#F5, 02#F7, 02#F8, 02#F10, 02#F11, 02#F17, 03#F1, 03#F5, 03#F6

### C78 · Carnet flow: counterfoils, time limits and the duty claim
- Kind: flow story · Findings: 20 (High 2, Medium 4, Low 14) in 4 files, 1 flow · Needs decision: owner: D40
- What is wrong: The carnet as issued shows all four counterfoils stamped; transit through Bayvarra has no transit counterfoils; proof is requested before the re-exportation time limit; the proof does not identify the carnet; contact and office names vary. Example: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cbc:IssueDate` = `2026-05-25` (carnet/01#F1).
- Where it comes from: `tools/examples_scenarios.py` `carnet()` (lines 2485 and 3761)
- What must be true afterwards: The carnet's counterfoils, dates and claims follow one timeline.
- Fix direction: Decide D40 (the timeline of the fair and the re-export; the duty claim goes with D18).
- Depends on / blocks: none
- Findings: carnet: 01#F1, 01#F2, 01#F5, 01#F8, 01#F12, 01#F14, 01#F16, 01#F17, 01#F18, 01#F22, 01#F23, 02#F1, 02#F4, 03#F8, 03#F9, 04#F1, 04#F4, 04#F9, 04#F10, 04#F11

### C79 · Mast flow: dangerous-goods data of the battery, detector and stripper consignment
- Kind: flow story · Findings: 36 (High 2, Medium 13, Low 21) in 5 files, 1 flow · Needs decision: owner: D36
- What is wrong: Placard notation 7 for an excepted package; the fissile aggregate for a non-fissile americium source; the activity of one detector for ten; placard endorsements that repeat the class or the label model; orange plates for air; crates over the PI 965 IA limit; road transport data in orders and invoices. Example: `mast/01-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7` (mast/01#F1).
- Where it comes from: `world/items.json` dangerous-goods data of SE-BAT-48100, SE-SMK-10, SE-CS-05; `tools/build_examples.py` `hazardous_item()` (line 772); `tools/examples_scenarios.py` `mast_consignment()` (line 5736)
- What must be true afterwards: The DG data follow the air rules the world states, per package, and appear only in transport documents.
- Fix direction: Decide D36 for the yes-findings (crate weights, CAO, endorsements); the rest are encoding fixes in items.json and `mast_consignment()`.
- Depends on / blocks: none
- Findings: mast: 01#F1, 01#F3, 01#F4, 01#F5, 01#F6, 01#F7, 02#F1, 02#F5, 02#F6, 02#F8, 02#F9, 02#F18, 02#F19, 02#F20, 02#F21, 02#F22, 02#F23, 03#F2, 03#F6, 03#F7, 03#F19, 03#F20, 03#F21, 04#F3, 04#F4, 04#F13, 04#F14, 04#F15, 04#F16, 05#F3, 05#F4, 05#F5, 05#F9, 05#F10, 05#F11, 05#F12

### C80 · Mast flow: the air waybill and the ULDs
- Kind: flow story · Findings: 6 (High 0, Medium 1, Low 5) in 3 files, 1 flow · Needs decision: owner: D36
- What is wrong: The air waybill has no airports or flight date and two numbers; the consignor's instructions carry the carrier's ULD numbers and positions; reefer and food settings without reason; the CPT place is "mast site". Example: `mast/02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AirFlowPercent` = `40` (mast/02#F17).
- Where it comes from: `tools/examples_scenarios.py` `mast()` (line 5862) and `mast_consignment()` (line 5736)
- What must be true afterwards: The waybill identifies the flight; instructions carry what the consignor knows.
- Fix direction: With D36.
- Depends on / blocks: none
- Findings: mast: 01#F8, 02#F16, 02#F17, 03#F5, 03#F9, 03#F18

### C81 · Ore flow: monthly call-off, plan "as requested", bonus and moisture
- Kind: flow story · Findings: 7 (High 1, Medium 0, Low 6) in 5 files, 1 flow · Needs decision: owner: D45
- What is wrong: The monthly call-off is typed as a plain order; the plan is confirmed "as requested" but differs; weekly vs monthly quantities; bonus and penalty neither applied nor excluded; moisture deduction without basis. Example: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cbc:DocumentStatusCode` = `Confirmed` (ore/03#F3).
- Where it comes from: `tools/examples_scenarios.py` `ore()` (line 37)
- What must be true afterwards: The ore call-off, plan and invoice tell one agreement.
- Fix direction: Decide D45 (the train's arrival, bonus or penalty).
- Depends on / blocks: none
- Findings: ore: 01#F4, 02#F4, 02#F5, 03#F3, 06#F4, 06#F5, 07#F2

### C82 · Energy flow: 2400 MWh exported to Montebrio, sold to Ferrano Energy, imported by nobody
- Kind: flow story · Findings: 9 (High 4, Medium 4, Low 1) in 3 files, 1 flow · Needs decision: owner: D44
- What is wrong: The export declaration consigns 39200 MWh to Montebrio Power; 2400 MWh are invoiced to Ferrano Energy and have no import declaration; the import declares 36800 MWh under the same shipment ID; gas declared as dry bulk; no period or crossing point. Example: `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK` (energy/04#F4).
- Where it comes from: `tools/examples_scenarios.py` energy declarations (`ENERGY` flow, line 8672 ff.)
- What must be true afterwards: Each buyer's gas is exported and imported under declarations that match its invoice.
- Fix direction: Decide D44 (split by buyer; Ferrano Energy's import).
- Depends on / blocks: none
- Findings: energy: 04#F1, 04#F2, 04#F4, 04#F5, 05#F1, 05#F5, 05#F6, 05#F12, 07#F1

### C83 · Energy flow: isolated slips
- Kind: flow story · Findings: 8 (High 1, Medium 2, Low 5) in 5 files, 1 flow · Needs decision: none
- What is wrong: Statement payable 0 for a billed consumption; network-use lines that cannot be told apart; the reminder in lume for a ferra debt; the surcharge line without its invoice and period; the plant's InformationURI is the home page. Example: `energy/04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example` (energy/04#F9).
- Where it comes from: `tools/examples_scenarios.py` energy flow (line 8672 ff.) and `utility_statement()` (line 2708)
- What must be true afterwards: Each slip corrected in place.
- Fix direction: Fix in the energy scenario.
- Depends on / blocks: none
- Findings: energy: 01#F1, 02#F1, 02#F2, 04#F9, 05#F9, 08#F1, 08#F8, 08#F9

### C84 · Packaging flow: isolated slips
- Kind: flow story · Findings: 5 (High 0, Medium 0, Low 5) in 4 files, 1 flow · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: Goods-in point without its GLN; a note referring to a consignment note the document does not identify; no package count; a promotion discount missing on a till receipt; a tax statement in an item description. Example: `packaging/05-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport` (packaging/05#F7).
- Where it comes from: `tools/examples_scenarios.py` `packaging()` (line 3396)
- What must be true afterwards: Each slip corrected.
- Fix direction: Fix in the packaging scenario.
- Depends on / blocks: none
- Findings: packaging: 05#F7, 06#F3, 06#F8, 08#F4, 09#F6

### C85 · Air flow: the missed-flight story and the CPT order change
- Kind: flow story · Findings: 13 (High 2, Medium 0, Low 11) in 8 files, 1 flow · Needs decision: owner: D39
- What is wrong: "Goes on the next day's flight" but the cargo arrives the same day; the cancelled despatch advice contains nothing the missed flight changed; the replacement says nothing it replaces; CPT next to "the rest stays CIF"; the buyer names the carrier. Example: `air/07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.` (air/07#F2).
- Where it comes from: `tools/examples_scenarios.py` `air()` (lines 1940 and 3612)
- What must be true afterwards: One consistent story of which flight was missed and when the goods flew.
- Fix direction: Decide D39 (preferred by air/07#F2: an evening flight on 13 May was missed).
- Depends on / blocks: C72 (order of cancellation and replacement)
- Findings: air: 01#F5, 01#F6, 02#F4, 02#F6, 04#F10, 04#F11, 05#F6, 07#F2, 07#F3, 07#F7, 08#F8, 09#F6, 10#F14

### C86 · Air flow: packing, consolidation and charges of the castings
- Kind: flow story · Findings: 10 (High 3, Medium 2, Low 5) in 3 files, 1 flow · Needs decision: owner: D39
- What is wrong: The box cannot hold the eight frames; gross minus net leaves 5.6 kg for skid, box and bags; "not consolidated" with a house waybill; a warehouse as substitute carrier; two waybill numbers; freight invoiced on gross instead of chargeable weight. Example: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cbc:Quantity` = `8` (air/03#F2).
- Where it comes from: `tools/examples_scenarios.py` `air_consignment()` (line 1892)
- What must be true afterwards: Packing, consolidation and charges agree across the air documents.
- Fix direction: With D39 (consolidation story); the arithmetic fixes need none.
- Depends on / blocks: none
- Findings: air: 03#F2, 03#F9, 04#F2, 04#F6, 04#F7, 04#F13, 04#F14, 04#F17, 10#F1, 10#F6

### C87 · Plastics flow: barge waybill and goods data
- Kind: flow story · Findings: 15 (High 2, Medium 4, Low 9) in 4 files, 1 flow · Needs decision: owner: D41
- What is wrong: The barge's CO2e is a hundredth of what its diesel produces; the freight rate as base amount; net volume of solid PE; returnable quantity counts bags; one package for 120 bags; lot IDs differ between waybill and despatch advice; standard VAT on international carriage. Example: `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Fiumella Barges` (plastics/04#F1).
- Where it comes from: `tools/examples_scenarios.py` `plastics()` (line 824), `barge_goods()` (line 751), `barge_consignment()` (line 801)
- What must be true afterwards: The barge documents describe the bags and the voyage consistently.
- Fix direction: Encoding fixes; plastics/07#F5 (VAT on carriage of exports) goes to D41.
- Depends on / blocks: none
- Findings: plastics: 04#F1, 04#F8, 06#F2, 06#F7, 06#F8, 06#F9, 06#F10, 06#F11, 06#F13, 06#F14, 06#F16, 07#F5, 08#F4, 08#F5, 08#F6

### C88 · Plastics flow: recycled-content certificate issued by a chamber of commerce
- Kind: flow story · Findings: 5 (High 0, Medium 0, Low 5) in 5 files, 1 flow · Needs decision: owner: D41
- What is wrong: Five documents give a chamber of commerce as issuer of a recycled-content certificate. Example: `plastics/08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce` (plastics/08#F8).
- Where it comes from: `world/parties.json` / `world/items.json` certificate of the PE granulate (issuer the Ferrano chamber); `tools/build_examples.py` certificates (line 987)
- What must be true afterwards: The certificate's issuer is a body that can certify recycled content.
- Fix direction: Decide D41.
- Depends on / blocks: none
- Findings: plastics: 01#F11, 05#F12, 08#F8, 09#F18, 10#F7

### C89 · Wood flow: slat units and isolated slips
- Kind: flow story · Findings: 10 (High 1, Medium 0, Low 9) in 5 files, 1 flow · Needs decision: owner: D43
- What is wrong: "Quoted per thousand slats" against a price per slat; `OrderableUnitFactorRate` 50 while quantities are single slats; two sets of terms without saying which governs; pallets charged but in no goods description; resale exemption without certificate. Example: `wood/02-Quotation.xml:/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.` (wood/02#F1).
- Where it comes from: `tools/examples_scenarios.py` `wood()` (line 3176), `quotation()` (line 3164)
- What must be true afterwards: One unit for quoting, ordering and invoicing; charges match the goods described.
- Fix direction: Decide D43 (the orderable unit).
- Depends on / blocks: none
- Findings: wood: 02#F1, 02#F4, 02#F12, 02#F13, 02#F16, 03#F10, 06#F12, 08#F10, 08#F14, 11#F5

### C90 · Rail flow: container train documents
- Kind: flow story · Findings: 33 (High 3, Medium 6, Low 24) in 8 files, 1 flow · Needs decision: owner: D37
- What is wrong: Terminal operator as network manager; the hub as destination instead of the siding; passenger quantity 0; demurrage under a vessel definition; the second container without wagon, places and events; one framework contract under two identifiers; the container "being stored" while on the train. Example: `rail/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0` (rail/03#F20).
- Where it comes from: `tools/examples_scenarios.py` `rail()` (lines 659 and 3522), `rail_container()` (line 487), `rail_stage()` (line 565), `rail_consignment()` (line 605)
- What must be true afterwards: Both containers described alike; roles and places as the rail leg has them.
- Fix direction: Encoding fixes; the yes-findings (roles of the hub, CMR vs CIM, Container Convention) go to D37.
- Depends on / blocks: none
- Findings: rail: 02#F3, 02#F13, 03#F3, 03#F14, 03#F15, 03#F20, 03#F21, 04#F2, 04#F3, 04#F6, 04#F7, 05#F2, 05#F4, 05#F5, 05#F8, 06#F14, 06#F18, 06#F22, 07#F4, 07#F8, 08#F8, 08#F10, 08#F15, 08#F17, 08#F18, 08#F19, 08#F21, 08#F22, 08#F24, 08#F25, 09#F1, 09#F6, 09#F7

### C91 · Utility statement builder: average amount, supplier consumption, subscriber data
- Kind: flow story · Findings: 30 (High 3, Medium 9, Low 18) in 6 files, 2 flows · Needs decision: owner: D31
- What is wrong: AverageAmount holds the month's amount; SupplierConsumption for a single supplier; SubscriberID holds the contract number; the item's subscriber type is a utility type; district-heating elements for electricity and water; empty descriptions. Example: `utilities/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120` (utilities/01#F12); `energy/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `61200` (energy/01#F4).
- Where it comes from: `tools/examples_scenarios.py` `utility_statement()` (line 2708), `consumption_line()` (line 2665), `telecom_consumption()` (line 2891)
- What must be true afterwards: The statement elements are used by their definitions in all six statements (also energy/01).
- Fix direction: Fix `utility_statement()`; D31 for the yes-findings (subscriber data, consumer level).
- Depends on / blocks: none
- Findings: energy: 01#F4; utilities: 01#F3, 01#F5, 01#F9, 01#F12, 01#F13, 01#F14, 03#F3, 03#F7, 03#F8, 03#F10, 03#F11, 03#F15, 05#F1, 05#F3, 05#F9, 05#F10, 05#F12, 05#F13, 08#F4, 08#F5, 08#F7, 08#F12, 08#F14, 08#F16, 08#F17, 12#F9, 12#F14, 12#F20, 12#F21

### C92 · Utilities: the telecom statement and invoice
- Kind: flow story · Findings: 15 (High 4, Medium 5, Low 6) in 3 files, 1 flow · Needs decision: owner: D31
- What is wrong: 35 GB stated twice (roaming and pool); a masked number shown in full; allowances ignored in line totals; one month invoiced as "6 months"; quantities that mix minutes, gigabytes and views. Example: `utilities/12-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:InvoicedQuantity` = `6` (utilities/12#F19).
- Where it comes from: `tools/examples_scenarios.py` `telecom_consumption()` (line 2891)
- What must be true afterwards: The telecom statement adds up and uses its elements by definition.
- Fix direction: Fix in `telecom_consumption()`; D31 for the yes-findings.
- Depends on / blocks: none
- Note: Possibly not a problem for utilities/13#F2 and 14#F2 (blockchain identifier): `note/src/03-world.md` says "Coral net, the island's clearing, settles tokenised deposits on the Bank of Selanu's ledger".
- Findings: utilities: 12#F1, 12#F2, 12#F3, 12#F4, 12#F6, 12#F7, 12#F8, 12#F15, 12#F18, 12#F19, 12#F22, 13#F2, 13#F9, 13#F10, 14#F2

### C93 · Utilities: the household's water on account, the mandate and the levy
- Kind: flow story · Findings: 13 (High 2, Medium 3, Low 8) in 5 files, 1 flow · Needs decision: owner: D31
- What is wrong: The statement says the household pays on account monthly; invoice 09 bills and collects the full amount; the mandate is limited to 12 instructions; payable amounts leave out the sewage levy; the reminder and credit note lack references. Example: `utilities/08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.` (utilities/08#F1).
- Where it comes from: `tools/examples_scenarios.py` `utilities()` (line 2998), `levy()` (line 2538)
- What must be true afterwards: One billing scheme for the household from statement to credit note.
- Fix direction: Decide D31 (preferred by utilities/08#F1: drop the on-account scheme).
- Depends on / blocks: none
- Findings: utilities: 05#F5, 08#F1, 08#F6, 09#F1, 09#F3, 09#F4, 09#F7, 10#F7, 10#F8, 10#F10, 11#F3, 11#F5, 11#F8

### C94 · Utilities: excise and estimate-correction amounts
- Kind: flow story · Findings: 7 (High 6, Medium 1, Low 0) in 3 files, 1 flow · Needs decision: none (1 finding marked "yes" goes to D46)
- What is wrong: The energy tax report carries the excise of the whole invoice in each statement; totals leave out the excise; per-unit amounts do not produce the excise; the estimate correction double-counts and its unit amount × quantity is not the amount. Example: `utilities/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840` (utilities/01#F1).
- Where it comes from: `tools/examples_scenarios.py` `energy_tax()` (line 2576) and the estimate correction in `utility_statement()` (line 2708)
- What must be true afterwards: The statements of one invoice add up to the invoice; excise arithmetic holds.
- Fix direction: Fix the arithmetic (preferred options of utilities/01#F1, F2, 02#F1); build check for the tier arithmetic.
- Depends on / blocks: none
- Findings: utilities: 01#F1, 01#F2, 02#F1, 02#F3, 03#F1, 03#F2, 03#F5

### C95 · Utilities: isolated slips
- Kind: flow story · Findings: 7 (High 1, Medium 2, Low 4) in 6 files, 1 flow · Needs decision: owner: D31
- What is wrong: Castrano named as subscriber of Valdara's subscription; OriginatorParty for the warehouse occupant; a one-time charge type for a monthly item; a tax point date on a reminder without tax. Example: `utilities/03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics` (utilities/03#F6).
- Where it comes from: `tools/examples_scenarios.py` `utilities()` (line 2998)
- What must be true afterwards: Each slip corrected.
- Fix direction: Fix in the scenario; utilities/03#F6 (who subscribes) goes to D31.
- Depends on / blocks: none
- Findings: utilities: 01#F6, 02#F5, 02#F7, 03#F6, 04#F2, 08#F13, 10#F3

### C96 · Qualification requests and responses (ESPD-like) in contest and tender
- Kind: flow story · Findings: 32 (High 1, Medium 11, Low 20) in 8 files, 2 flows · Needs decision: owner: D29
- What is wrong: The buyer's request sets the fulfilment indicator; no exclusion grounds; responses that do not refer to the request; evidence not linked; the same text as description and value; groups whose other member is not encoded; expected values that are thresholds; "all criteria answered" with one answer. Example: `contest/06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF` (contest/06#F3); `tender/07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:Note` = `All criteria answered.` (tender/07#F1).
- Where it comes from: `tools/examples_scenarios.py` `qualification_limits()` (line 6709) and the QualificationApplicationRequest/Response enrichments (lines 6592–6839)
- What must be true afterwards: Requests ask, responses answer, linked to each other and to evidence.
- Fix direction: Fix the shared qualification builders; yes-findings with D29.
- Depends on / blocks: none
- Findings: contest: 05#F3, 05#F10, 06#F3, 06#F4, 06#F5, 06#F12, 06#F13, 06#F14, 07#F5, 10#F1, 10#F8, 11#F1, 11#F4, 11#F6, 11#F7, 11#F8, 11#F9, 12#F5; tender: 06#F4, 06#F5, 06#F6, 06#F7, 06#F8, 06#F13, 06#F14, 06#F15, 06#F16, 07#F1, 07#F4, 07#F5, 07#F6, 07#F7

### C97 · Procurement notices (contest and tender): notice types, defaults, languages, links
- Kind: flow story · Findings: 31 (High 0, Medium 6, Low 25) in 14 files, 2 flows · Needs decision: owner: D29
- What is wrong: Design-contest notices use the standard-procedure notice types CN and CAN; the requested legal form applies to the follow-up contract; the reference criterion's DurationPeriod is the look-back window; CandidateReductionConstraintIndicator says the candidates are reduced; PublishAwardIndicator without its situation; Urvanian declared as a notice language without Urvanian text; calls that do not link the contract notice. Example: `contest/03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD` (contest/03#F7); `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:NoticeLanguageCode` = `en` (tender/01#F14).
- Where it comes from: `tools/examples_scenarios.py` `notice_head()` (line 6476), `tendering_process()` (line 6220), contest helpers (lines 8894–8943)
- What must be true afterwards: Notice coding follows the procedure type (design contest vs open procedure).
- Fix direction: Encoding fixes in the shared notice builders; the yes-findings with D29.
- Depends on / blocks: none
- Findings: contest: 03#F1, 03#F7, 03#F8, 03#F10, 04#F10, 04#F11, 04#F12, 04#F13, 05#F11, 08#F1, 08#F8, 08#F9, 08#F11, 09#F7, 09#F9, 09#F10, 09#F13, 10#F9, 15#F3, 15#F13, 16#F2, 16#F13; tender: 01#F14, 02#F18, 02#F27, 03#F27, 03#F44, 12#F7, 21#F5, 21#F18, 24#F3

### C98 · Contest: the design team, references, prizes and versions
- Kind: flow story · Findings: 24 (High 1, Medium 4, Low 19) in 13 files, 1 flow · Needs decision: owner: D29
- What is wrong: The first prize of 6,000 contradicts the 8,000 of the notice; the winning team is reduced to its lead; one completed task where two references are required; requests addressed to one participant before selection; version 2 documents do not say what they change. Example: `contest/15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:Description` = `First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.` (contest/15#F2).
- Where it comes from: `tools/examples_scenarios.py` `contest_version()` (line 8901), `contest_prizes()` (line 8910), `contest_awarding()` (line 8943)
- What must be true afterwards: The contest tells one story of the team, the criteria and the prize correction.
- Fix direction: Decide D29.
- Depends on / blocks: none
- Findings: contest: 02#F3, 04#F3, 04#F7, 05#F7, 05#F12, 06#F11, 07#F1, 07#F4, 07#F8, 09#F8, 09#F12, 10#F7, 11#F5, 12#F1, 12#F6, 13#F3, 13#F4, 14#F3, 14#F4, 14#F5, 15#F1, 15#F2, 16#F1, 16#F11

### C99 · Contest: the estimated contract amount of 54,000 lume
- Kind: flow story · Findings: 8 (High 0, Medium 0, Low 8) in 8 files, 1 flow · Needs decision: owner: D29
- What is wrong: What the estimate covers is not stated, and it stays the same after the first prize rose. Example: `contest/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00` (contest/01#F6).
- Where it comes from: `tools/examples_scenarios.py` `contest_project()` (line 8924)
- What must be true afterwards: The estimate says what it covers and follows the prize change, or is absent.
- Fix direction: Decide with D29.
- Depends on / blocks: none
- Findings: contest: 01#F6, 02#F7, 03#F11, 04#F14, 08#F12, 09#F11, 15#F12, 16#F12

### C100 · Road flow: isolated slips of the truck shipment
- Kind: flow story · Findings: 25 (High 1, Medium 6, Low 18) in 10 files, 1 flow · Needs decision: owner: D35
- What is wrong: Gross volume smaller than its handling units; journey ID for a one-off trip; required and latest delivery times disagree; notes that narrate the example; trailer seal only in a remark; package level "inner"; a recount with one package more. Example: `road/08-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossVolumeMeasure` = `41.5` (road/08#F2).
- Where it comes from: `tools/examples_scenarios.py` `road()` (line 195), `road_stage()` (line 109), `road_consignment()` (line 139)
- What must be true afterwards: Each slip corrected.
- Fix direction: Encoding fixes; the yes ones with D35.
- Depends on / blocks: none
- Findings: road: 01#F10, 01#F11, 02#F4, 02#F5, 03#F5, 03#F9, 08#F2, 08#F11, 08#F13, 08#F14, 08#F18, 08#F24, 08#F25, 08#F26, 08#F28, 08#F29, 08#F30, 09#F10, 09#F11, 12#F1, 13#F8, 13#F15, 14#F11, 16#F11, 17#F8

### C101 · Road flow: application and certificate of origin
- Kind: flow story · Findings: 14 (High 4, Medium 4, Low 6) in 3 files, 1 flow · Needs decision: owner: D35
- What is wrong: Application and certificate share ID and version; a second endorsement before the first; the buyer's order number as job number; an embassy endorsement by the Trade Accord Council; endorsers' signatory contacts against their definition. Example: `road/06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office` (road/06#F16).
- Where it comes from: `tools/examples_scenarios.py` road certificate of origin documents (`road()` line 195; enrichment `road()` line 3676)
- What must be true afterwards: Application and certificate are two documents with their own IDs, endorsements in order.
- Fix direction: Decide D35 for the endorsement roles; the rest are encoding fixes.
- Depends on / blocks: none
- Findings: road: 06#F1, 06#F3, 06#F7, 06#F15, 06#F16, 06#F17, 07#F1, 07#F6, 07#F9, 07#F10, 07#F16, 07#F17, 07#F18, 10#F3

### C102 · Road flow: the substituted 2026 casting
- Kind: flow story · Findings: 8 (High 0, Medium 1, Low 7) in 7 files, 1 flow · Needs decision: owner: D35
- What is wrong: The order response replaces the old casting by the 2026 casting, but despatch, certificates, receipt and invoice do not identify it (extended ID `2026`); the proposed substitute is the old casting; an extra frame is accepted but never billed. Example: `road/07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180` (road/07#F25).
- Where it comes from: `tools/examples_scenarios.py` `road()` (line 195): the substitute line of the order response and the follow-up lines
- What must be true afterwards: The 2026 casting is identified the same way from the response to the invoice.
- Fix direction: Carry the extended ID through; road/13#F9 (the extra frame) with D35.
- Depends on / blocks: none
- Findings: road: 02#F6, 04#F15, 07#F25, 10#F21, 11#F12, 13#F9, 13#F18, 15#F13

### C103 · Furniture flow: quotation, orders, invoice, return and credit
- Kind: flow story · Findings: 27 (High 0, Medium 1, Low 26) in 9 files, 1 flow · Needs decision: owner: D32
- What is wrong: Optional cushions only in a note; the initial order twice the target inventory; a repeat order while stock suffices; sub-line prices without quantities; a restocking deduction on a return the maker asked for; the quotation used as a contract. Example: `furniture/12-InstructionForReturns.xml:/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-04-29` (furniture/12#F1).
- Where it comes from: `tools/examples_scenarios.py` `furniture()` (lines 3268 and 3685), `set_parts()` (line 3224)
- What must be true afterwards: Order, stock and return figures follow the replenishment profile and the story.
- Fix direction: Decide D32.
- Depends on / blocks: none
- Findings: furniture: 01#F2, 01#F7, 01#F8, 01#F9, 02#F3, 02#F8, 08#F5, 08#F6, 08#F7, 08#F8, 08#F10, 09#F3, 09#F7, 09#F9, 10#F3, 10#F4, 10#F5, 10#F10, 10#F11, 11#F3, 11#F4, 12#F1, 12#F3, 13#F2, 13#F3, 13#F5, 14#F5

### C104 · Furniture flow: the replenishment and sales-reporting documents
- Kind: flow story · Findings: 21 (High 0, Medium 10, Low 11) in 5 files, 1 flow · Needs decision: owner: D32
- What is wrong: Request lines that ask for activity, forecast and metric at once; a replenishment owner that describes a division of work; exception status codes for shipments used for sales; one four-week figure where weekly ones were requested; the weather as an activity property. Example: `furniture/03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode` = `SALES` (furniture/03#F1).
- Where it comes from: `tools/examples_scenarios.py` `furniture()` (lines 3268 and 3685), `collab()` (line 3263)
- What must be true afterwards: Each collaboration document uses its elements by definition, one kind of criterion per line.
- Fix direction: Decide D32 for the yes-findings; encoding fixes otherwise.
- Depends on / blocks: none
- Findings: furniture: 03#F1, 03#F3, 04#F1, 04#F2, 04#F7, 04#F9, 05#F1, 05#F2, 05#F7, 05#F8, 06#F5, 06#F6, 06#F7, 06#F8, 07#F1, 07#F2, 07#F3, 07#F4, 07#F5, 07#F10, 07#F11

### C105 · Furniture flow: the department's desks and installation
- Kind: flow story · Findings: 10 (High 0, Medium 0, Low 10) in 3 files, 1 flow · Needs decision: owner: D32
- What is wrong: A packaging-disposal charge the order does not contain; a zero tax total without category; the place of work named only; an hourly price without base quantity. Example: `furniture/15-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax` (furniture/15#F5).
- Where it comes from: `tools/examples_scenarios.py` `furniture()` documents 15–17
- What must be true afterwards: Invoice and work report bill what was ordered.
- Fix direction: Decide with D32.
- Depends on / blocks: none
- Findings: furniture: 15#F3, 15#F5, 16#F4, 16#F6, 16#F8, 16#F10, 16#F12, 17#F4, 17#F6, 17#F7

### C106 · Cotton flow: self-billing between ginnery and farm, and the mill's forecasts
- Kind: flow story · Findings: 26 (High 1, Medium 4, Low 21) in 6 files, 1 flow · Needs decision: owner: D33
- What is wrong: A customs broker as tax representative of a domestic purchase; invoice periods before the delivery; references that say nothing; a charge whose text calls it an allowance; the farm as payee of a credit that flows to the ginnery; "twenty per cent more" is 25 %. Example: `cotton/03-DeliveryNote.xml:/DeliveryNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26` (cotton/03#F3).
- Where it comes from: `tools/examples_kit.py` `self_billed()` (line 1115); `tools/examples_scenarios.py` `cotton()` (line 2082)
- What must be true afterwards: The self-billed documents and forecasts tell one season agreement.
- Fix direction: Decide D33 for the yes-findings.
- Depends on / blocks: none
- Findings: cotton: 02#F2, 03#F3, 04#F5, 04#F9, 04#F10, 04#F12, 04#F13, 04#F14, 04#F18, 04#F19, 04#F20, 05#F5, 05#F6, 05#F9, 05#F10, 05#F13, 05#F14, 05#F15, 05#F16, 05#F20, 05#F24, 05#F25, 06#F5, 06#F6, 07#F1, 07#F8

### C107 · Cotton flow: classing and phytosanitary certificates
- Kind: flow story · Findings: 15 (High 5, Medium 1, Low 9) in 7 files, 1 flow · Needs decision: owner: D33
- What is wrong: A forecast carries a classing certificate signed 18 days later; a downgrade cites a certificate that says Middling and is signed later; "10 bales sampled out of 80" for 27 bales; a version 1 with a previous version from last season; a phytosanitary certificate issued by a chamber of commerce. Example: `cotton/02-Forecast.xml:/Forecast/cbc:IssueDate` = `2026-02-02` (cotton/02#F1).
- Where it comes from: `tools/examples_scenarios.py` `cotton()` (line 2082), certificate documents 10 and their references
- What must be true afterwards: Certificates exist before they are cited and describe the shipment.
- Fix direction: Decide D33 (who issues the phytosanitary certificate).
- Depends on / blocks: none
- Findings: cotton: 02#F1, 05#F2, 05#F21, 07#F11, 10#F1, 10#F2, 10#F3, 10#F4, 10#F6, 10#F8, 10#F15, 10#F17, 11#F6, 14#F3, 15#F7

### C108 · Cotton flow: the sea export (bill of lading, VGM, pre-arrival report)
- Kind: flow story · Findings: 13 (High 2, Medium 3, Low 8) in 8 files, 1 flow · Needs decision: owner: D33
- What is wrong: The original bill goes to a bank while the instructions ask for the forwarder; the bank as mortgage holder without any financing; "freight collect" while the forwarder invoices freight; the VGM without method or date; the pre-arrival report not tied to the shipment. Example: `cotton/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129` (cotton/11#F5).
- Where it comes from: `tools/examples_scenarios.py` `cotton()` (line 2082), `bl_distribution()` (line 4418)
- What must be true afterwards: The sea documents follow the instructions and one payment arrangement.
- Fix direction: Decide D33 (documentary collection or not).
- Depends on / blocks: none
- Findings: cotton: 08#F9, 09#F1, 11#F5, 12#F1, 12#F2, 12#F4, 13#F1, 13#F3, 13#F7, 14#F4, 15#F6, 17#F2, 17#F5

### C109 · Cotton flow: classing results carried as the applicant's remarks
- Kind: flow story · Findings: 7 (High 0, Medium 0, Low 7) in 7 files, 1 flow · Needs decision: none
- What is wrong: The classing results stand in the applicant's `Remarks` in seven documents. Example: `cotton/10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.` (cotton/10#F10).
- Where it comes from: `tools/examples_scenarios.py` cotton certificate (`cotton()` line 2082)
- What must be true afterwards: The results are in the certificate's own elements.
- Fix direction: Move them (encoding).
- Depends on / blocks: none
- Findings: cotton: 02#F11, 07#F12, 08#F16, 10#F10, 11#F11, 15#F11, 16#F9

### C110 · Retail flow: catalogue request, catalogue, updates and deletion
- Kind: flow story · Findings: 15 (High 3, Medium 4, Low 8) in 5 files, 1 flow · Needs decision: owner: D34
- What is wrong: A request for an update of a catalogue that exists nowhere; a "new" catalogue that supersedes a version; references to the catalogue with wrong issue and revision times; the update line pointing to the bench for the frame; "Unchanged." as trading terms. Example: `retail/03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.` (retail/03#F9).
- Where it comes from: `tools/examples_scenarios.py` retail catalogue enrichments (lines 3847–3990), `catalogue_update_head()` (line 3951)
- What must be true afterwards: The catalogue versions and their references agree.
- Fix direction: Decide D34 (new catalogue vs update).
- Depends on / blocks: none
- Findings: retail: 01#F3, 01#F7, 01#F10, 02#F2, 02#F5, 02#F13, 02#F14, 03#F2, 03#F3, 03#F9, 03#F12, 04#F5, 04#F12, 20#F1, 20#F4

### C111 · Retail flow: promotion, forecast, inventory and the shop sale
- Kind: flow story · Findings: 13 (High 2, Medium 2, Low 9) in 4 files, 1 flow · Needs decision: owner: D34
- What is wrong: The forecast's promotion reference resolves nowhere; a store-opening event nothing supports; the promotion price valid for another period than the promotion; planned sales at the regular price; sale IDs encode 18 May for a purchase on 15 May. Example: `retail/05-Forecast.xml:/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `BM-RE-26` (retail/05#F1).
- Where it comes from: `tools/examples_scenarios.py` `retail()` (lines 953 and 3628), `promo_allowance()` (line 909)
- What must be true afterwards: The promotion has one period and one price chain from event to receipt.
- Fix direction: Decide D34 for the yes-findings.
- Depends on / blocks: none
- Findings: retail: 05#F1, 05#F10, 06#F5, 06#F6, 06#F7, 06#F11, 06#F13, 06#F14, 07#F10, 07#F14, 21#F3, 21#F7, 21#F12

### C112 · Retail flow: isolated slips
- Kind: flow story · Findings: 12 (High 1, Medium 2, Low 9) in 5 files, 1 flow · Needs decision: owner: D34
- What is wrong: Purchase-card data capability described as the e-document channel; the invoice bills 24 benches against a receipt of 23; a tax point date without event; the factor as payee of a credit owed to the buyer. Example: `retail/18-Invoice.xml:/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5` (retail/18#F2).
- Where it comes from: `tools/examples_scenarios.py` `retail()` (lines 953, 3628)
- What must be true afterwards: Each slip corrected.
- Fix direction: With D34.
- Depends on / blocks: none
- Note: Possibly not a problem for retail/22#F7 (full card number and CVV in the webshop order): `note/src/03-world.md` says "A webshop order is different: the card is not at hand, so the order carries the full number, the card's dates and its security code".
- Findings: retail: 08#F5, 08#F8, 08#F12, 10#F4, 18#F2, 18#F10, 18#F11, 18#F13, 19#F2, 22#F2, 22#F5, 22#F7

### C113 · Retail flow: the delivery to the store (carrier references, arrival day)
- Kind: flow story · Findings: 12 (High 3, Medium 2, Low 7) in 6 files, 1 flow · Needs decision: owner: D34
- What is wrong: Three different carrier references for one shipment; the shipping-document reference points to the request; "on its way, expected 29 April 14:00" but received 30 April 10:40; "late" for a slot no document agreed. Example: `retail/13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217` (retail/13#F2).
- Where it comes from: `tools/examples_scenarios.py` `retail()` documents 11–17
- What must be true afterwards: One carrier reference and one delivery day across the transport documents.
- Fix direction: Decide D34 (the delivery day; merge decision Medium/yes).
- Depends on / blocks: none
- Findings: retail: 12#F10, 12#F11, 13#F2, 14#F2, 14#F6, 15#F1, 15#F4, 16#F4, 17#F4, 17#F8, 17#F12, 17#F14

### C114 · Sea flow: bill of lading and ship reports
- Kind: flow story · Findings: 21 (High 3, Medium 7, Low 11) in 5 files, 1 flow · Needs decision: owner: D30
- What is wrong: One SSCC for the frames pallet and a box; the bill's total invoice amount is the goods value; the final delivery party is the buyer, not its 3PL; the road chassis still attached on board; crew lists of 3 of 14; a WHO affected area; the port company issuing sanitation certificates. Example: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254` (sea/14#F1).
- Where it comes from: `tools/examples_scenarios.py` `sea_consignment()` (line 1222), `sea_equipment()` (line 1171), `bl_extras()` (line 4403)
- What must be true afterwards: The bill and the ship reports describe the shipment and the ship consistently.
- Fix direction: Decide D30 for the yes-findings.
- Depends on / blocks: none
- Findings: sea: 13#F7, 14#F1, 14#F4, 14#F5, 14#F6, 14#F7, 14#F8, 15#F7, 15#F8, 16#F6, 16#F7, 16#F8, 16#F13, 16#F14, 16#F15, 16#F16, 16#F18, 16#F20, 16#F21, 17#F2, 17#F9

### C115 · Sea flow: isolated slips
- Kind: flow story · Findings: 20 (High 2, Medium 3, Low 15) in 11 files, 1 flow · Needs decision: owner: D30
- What is wrong: A booking deadline already past when the service is offered; weekly sailing day Friday against a Thursday sailing; a service classified with a goods code; the rejected frame not identified; the full-container discount not applied; the on-carriage leg 19–21 May dated nowhere (timelines#F7). Example: `sea/07-TransportServiceDescriptionRequest.xml:/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT` (sea/07#F3); `sea/06-OrderResponse.xml:/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-05-18` (timelines#F7).
- Where it comes from: `tools/examples_scenarios.py` `sea()` (lines 1527 and 3551)
- What must be true afterwards: Each slip corrected.
- Fix direction: With D30.
- Depends on / blocks: none
- Findings: sea: 05#F14, 06#F5, 06#F6, 06#F12, 07#F3, 08#F1, 08#F2, 08#F6, 08#F7, 08#F12, 08#F13, 10#F10, 11#F14, 12#F6, 18#F8, 19#F14, 21#F7, 21#F8, 21#F9; consistency: timelines#F7

### C116 · Sea flow: factoring, statement, payment and the island's debit note
- Kind: flow story · Findings: 16 (High 5, Medium 4, Low 7) in 6 files, 1 flow · Needs decision: owner: D30
- What is wrong: The status response reports a payment made a month later; paid amounts differ from the remittance advice; the factor as accounting supplier of the invoice line; the storage charge three times in the debit note; the deposit as an invoice period. Example: `sea/24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30` (sea/24#F1).
- Where it comes from: `tools/examples_scenarios.py` `sea_with_debit()` (line 5904) and the sea finance documents 22–28
- What must be true afterwards: Factoring, statement and payments agree.
- Fix direction: Encoding fixes; yes-findings with D30.
- Depends on / blocks: none
- Findings: sea: 22#F7, 22#F13, 22#F14, 24#F1, 24#F2, 25#F3, 25#F6, 26#F4, 26#F6, 26#F7, 27#F1, 27#F2, 28#F2, 28#F5, 28#F6, 28#F12

### C117 · Sea flow: business card, digital agreement and capabilities
- Kind: flow story · Findings: 15 (High 0, Medium 4, Low 11) in 3 files, 1 flow · Needs decision: owner: D30
- What is wrong: Audit evidence issued by the audited company; tendering-only evidence elements in a business card; a bilateral agreement signed by one participant; Lumeway's own EDI terms "signed" by the Trade Accord Council; billing processes that do not match the flow. Example: `sea/01-BusinessCard.xml:/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:EvidenceTypeCode` = `AUDIT` (sea/01#F3).
- Where it comes from: `tools/examples_scenarios.py` `digital_service()` (line 4890), `service_customization()` (line 4881), sea documents 01–04
- What must be true afterwards: The agreement documents describe what the parties actually exchange.
- Fix direction: Decide D30 for the yes-findings.
- Depends on / blocks: none
- Findings: sea: 01#F3, 01#F4, 01#F5, 01#F12, 03#F6, 03#F7, 03#F8, 03#F12, 03#F13, 03#F14, 03#F15, 03#F16, 03#F18, 04#F4, 04#F10

### C118 · Sea flow: the CIF sale, freight and insurance
- Kind: flow story · Findings: 14 (High 3, Medium 3, Low 8) in 10 files, 1 flow · Needs decision: owner: D30
- What is wrong: Freight and insurance are charged on top of a price agreed CIF; the confirmed total differs from the invoice; the insurer as insurance party; one insurance split over two policies; pre-carriage freight that nobody bills; the statement repeats the invoice's freight. Example: `sea/06-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00` (sea/06#F1).
- Where it comes from: `tools/examples_scenarios.py` `sea_invoice_terms()` (line 1357), `cif_value()` (line 1154), `sea_order_response()` (line 1456)
- What must be true afterwards: Under CIF the price includes freight and insurance, consistently in order, invoice, statement and declarations.
- Fix direction: Decide D30 (preferred by sea/22#F3: drop the two charges).
- Depends on / blocks: C52 (D16)
- Findings: sea: 05#F12, 05#F13, 06#F1, 09#F1, 09#F7, 11#F13, 14#F12, 14#F13, 14#F14, 18#F3, 19#F20, 22#F3, 25#F1, 26#F3

### C119 · Tender: tendering terms copied into notices, call, award and contract
- Kind: flow story · Findings: 86 (High 4, Medium 40, Low 42) in 13 files, 1 flow · Needs decision: owner: D28
- What is wrong: The shared terms repeat the same errors in five documents: a security-clearance date with "not required", a guarantee of 2400.00 that is 2 % of nothing, a turnover criterion "at least" coded "greater than", a "precise" subcontract share of 30 % next to 3.5 %, paper copies as a concession fee, variants unconstrained with a maximum of one, an auction and a framework agreement nobody holds, design-contest indicators in a supply procedure. Example: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21` (tender/01#F1).
- Where it comes from: `tools/examples_scenarios.py` `tendering_terms()` (line 6283), `auction_terms()` (line 6189), `tendering_process()` (line 6220), used by tender/01, 02, 03, 21, 22, 23 and 24
- What must be true afterwards: The procedure's terms are stated once, correctly, and the later documents repeat them unchanged.
- Fix direction: Fix `tendering_terms()` once (most options need no decision); D28 for the yes-findings (auction, framework values, budget).
- Depends on / blocks: none
- Findings: tender (86): 01#F1, 01#F7, 01#F8, 01#F9, 01#F10 …. Full list in `analysis/worklist-assignments.csv`.

### C120 · Tender: contract, catalogue and call-off (releases, despatch, credit, reminder)
- Kind: flow story · Findings: 30 (High 2, Medium 6, Low 22) in 11 files, 1 flow · Needs decision: owner: D28
- What is wrong: The contract identifies neither the accepted tender nor the prices; catalogue validity shifted against the contract; 200 benches "outstanding" that were never ordered; no serial numbers although the contract requires them; two statements of how the credit is settled; interest paid that the contract does not make due. Example: `tender/26-Order.xml:/Order/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS` (tender/26#F14).
- Where it comes from: `tools/examples_scenarios.py` `tender()` (lines 2360, 3459) and `tender_with_credit()` (line 6029)
- What must be true afterwards: The call-off documents execute the contract as signed.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Findings: tender: 24#F4, 25#F3, 25#F12, 25#F16, 25#F17, 25#F19, 25#F20, 25#F22, 26#F12, 26#F14, 27#F3, 27#F9, 27#F10, 27#F11, 28#F6, 29#F3, 29#F10, 29#F12, 32#F17, 32#F18, 33#F1, 33#F7, 33#F12, 33#F13, 34#F3, 34#F11, 35#F12, 36#F2, 36#F6, 36#F9

### C121 · Tender: the procurement project and its lots
- Kind: flow story · Findings: 26 (High 3, Medium 0, Low 23) in 11 files, 1 flow · Needs decision: owner: D28
- What is wrong: Lot 2 is works in the prior information notice and services elsewhere; lot 2 is described with the bench data; the buyer's estimates equal the winning tender to the cent; the project and programme have different names and codes. Example: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00` (tender/01#F27).
- Where it comes from: `tools/examples_scenarios.py` `procurement_project()` (line 6110), `procurement_lots()` (line 6462), `contract_name()` (line 6872)
- What must be true afterwards: One description of project and lots, and an estimate made before the tenders.
- Fix direction: Decide D28 (the estimate).
- Depends on / blocks: none
- Findings: tender: 01#F4, 01#F27, 01#F28, 01#F29, 01#F30, 02#F5, 02#F32, 02#F33, 02#F34, 02#F38, 02#F39, 03#F5, 03#F33, 03#F34, 03#F35, 03#F39, 03#F40, 08#F6, 09#F10, 15#F15, 21#F14, 21#F17, 24#F14, 26#F15, 29#F14, 32#F19

### C122 · Tender: the tenders, receipt and withdrawal
- Kind: flow story · Findings: 15 (High 2, Medium 0, Low 13) in 4 files, 1 flow · Needs decision: owner: D28
- What is wrong: Warranty five years on the line and six in the criterion response; the tenderer's own costs as fees of the project; no unit prices although the procedure evaluates them; identical ordering terms in competing tenders. Example: `tender/15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:Quantity` = `240` (tender/15#F16).
- Where it comes from: `tools/examples_scenarios.py` `tender_lines()` (line 6557) and documents 15–19
- What must be true afterwards: Each tender states one offer, evaluated as tendered.
- Fix direction: Decide D28 for the yes-findings.
- Depends on / blocks: none
- Findings: tender: 15#F11, 15#F16, 15#F17, 16#F6, 17#F3, 17#F11, 17#F13, 17#F15, 17#F16, 17#F17, 19#F3, 19#F11, 19#F13, 19#F15, 19#F16

### C123 · Tender: the installation billed but never ordered
- Kind: flow story · Findings: 14 (High 7, Medium 4, Low 3) in 7 files, 1 flow · Needs decision: owner: D28
- What is wrong: The release order has one line (the benches); the invoice bills forty installations, invoiced before they can be done, taxed as a service to a business; the penalty is for late installation of a service billed as supplied; "by the manufacturer's installers" although a subcontractor installs. Example: `tender/32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.` (tender/32#F8).
- Where it comes from: `tools/examples_scenarios.py` `tender()` release order (lines 2360, 3459) and invoice
- What must be true afterwards: The installation is ordered, performed, accepted and then billed, by the party the award names.
- Fix direction: Decide D28 (preferred: order line for the installation, separate later invoice).
- Depends on / blocks: C51 (D22), C54 (D17)
- Findings: tender: 25#F11, 25#F18, 26#F3, 27#F2, 28#F2, 32#F1, 32#F2, 32#F4, 32#F8, 32#F16, 33#F5, 33#F6, 34#F2, 34#F9

### C124 · Tender: expressions of interest, status, register extract and Valdara's qualification
- Kind: flow story · Findings: 13 (High 0, Medium 5, Low 8) in 3 files, 1 flow · Needs decision: owner: D28
- What is wrong: Two competing tenderers presented as one group; OperationType holds the line of business; capability figures that differ between the register extract and Valdara's qualification; one reference supply where three are required. Example: `tender/12-BusinessInformation.xml:/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupTypeCode` = `SAMEACTIVITY` (tender/12#F4).
- Where it comes from: `tools/examples_scenarios.py` tender documents 04–13 (enrichments after line 6508)
- What must be true afterwards: The qualification figures are one set, stated the same everywhere.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Findings: tender: 09#F5, 12#F4, 12#F5, 12#F6, 12#F13, 12#F14, 12#F15, 13#F1, 13#F3, 13#F4, 13#F10, 13#F11, 13#F12

### C125 · Tender: procedure periods against the notices' issue dates
- Kind: flow story · Findings: 10 (High 5, Medium 0, Low 5) in 9 files, 1 flow · Needs decision: owner: D28
- What is wrong: Requested publication and procedure periods lie before the notices' issue dates; interest and registrations after the reception period; the appeal period is the award's before the award existed; the contract signed on the last appeal day. Example: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT` (tender/01#F2).
- Where it comes from: `tools/examples_scenarios.py` `out_day()` (line 6491) and the notice/award dates in `tender()` (lines 2360, 3459)
- What must be true afterwards: Every period lies after the document that announces it and fits the procedure.
- Fix direction: Decide D28 (move the notices to late January, or the periods).
- Depends on / blocks: none
- Findings: tender: 01#F2, 02#F1, 03#F1, 04#F4, 05#F4, 20#F1, 21#F2, 21#F12, 22#F5, 24#F13

### C126 · Tender: the guarantee certificate
- Kind: flow story · Findings: 9 (High 0, Medium 3, Low 6) in 4 files, 1 flow · Needs decision: owner: D28
- What is wrong: A bank guarantee described as immobilised shares of the tenderer itself; the tenderer as issuer of the bank's certificate; value and market value three days apart; tenders that do not refer to their guarantee. Example: `tender/17-Tender.xml:/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.` (tender/17#F12).
- Where it comes from: `tools/examples_scenarios.py` tender document 14 (guarantee)
- What must be true afterwards: One kind of guarantee, issued by the bank, referenced by the tender.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Findings: tender: 14#F1, 14#F2, 14#F3, 14#F7, 14#F8, 14#F9, 15#F12, 17#F12, 19#F12

### C127 · Tender: award, notifications and appeal
- Kind: flow story · Findings: 7 (High 1, Medium 0, Low 6) in 3 files, 1 flow · Needs decision: owner: D28
- What is wrong: The opening still "scheduled" in the award notice; the review board as information party, receiver and mediator without contact; the winner's subcontract price told to the loser. Example: `tender/20-TendererQualificationResponse.xml:/TendererQualificationResponse/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra` (tender/20#F7).
- Where it comes from: `tools/examples_scenarios.py` `tender_result()` (line 6894), `appeal_terms()` (line 6884)
- What must be true afterwards: The award documents report a completed opening and a reachable appeal body.
- Fix direction: Decide D28.
- Depends on / blocks: none
- Findings: tender: 20#F6, 20#F7, 20#F8, 21#F1, 23#F3, 23#F4, 23#F5

### C128 · Tender: moss green ordered, grey identified
- Kind: flow story · Findings: 6 (High 5, Medium 1, Low 0) in 6 files, 1 flow · Needs decision: none
- What is wrong: The order change asks for moss green and the lot is made green, but despatch, declarations, invoice and credit note identify the grey variant while charging the special colour. Example: `tender/30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY` (tender/30#F1).
- Where it comes from: `tools/examples_scenarios.py` tender order change and despatch (`tender()` lines 2360, 3459); colour codes in `world/codelists/lists.json`
- What must be true afterwards: From the change on, every document identifies the green variant.
- Fix direction: Carry the green variant (ExtendedID, colour property) through; add the colour code to the world list if missing.
- Depends on / blocks: none
- Findings: tender: 27#F4, 29#F1, 30#F1, 31#F1, 32#F3, 33#F2

