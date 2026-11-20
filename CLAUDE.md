# ubl-examples: guide for working sessions

## What this repository is

- `xml/`: the UBL sample documents as published by OASIS, one commit per document (history and tools: `history/README.md`).
- `world/`: a fictional **UBL 2.5 example world**, with about 250 validated example documents in `world/examples/<flow>/NN-DocType.xml`. Each has a `.md` next to it that gives the reason for every value.
  - **Countries:** Urvania (XU), Bayvarra (XB) and the island Lisavu (XL), trading under the Lumeport Trade Accord.
  - **Languages:** English, plus the invented Urvanian (`qau`) and Lisavan (`qal`).
- The site is built from all of this and published to GitHub Pages. **The world is front and centre** (owner, 2026-11-20): nav World (the isometric map) · Trade (the flows and their documents) · Parties · Rules (specifications and code lists) · About (the project: coverage, the OASIS samples, the method note, tucked away). Every page and figure is generated; the hand-written texts are `site/index.html`, `site/about.md` and the map's card in `site/world.html`. The world's pages name no real specification (no Peppol, CEN, EN 16931): the world is separate and independent.

## Where the story and the decisions are

- **The world's story:** `note/src/03-world.md` covers countries, history, languages, taxes, payments, energy market, addresses, map rules, vehicles and self-billing. The DocBook is generated from it with `bash tools/md2docbook.sh`.
- **The world's data:**
  - `world/countries.json`: histories, tax schemes, formats, vocabularies, identifier schemes;
  - `world/parties.json`: each party's role, "what" and "how", identity and fleet;
  - `world/documents.json`: flows, documents with their "why", transport legs;
  - `world/items.json`, `world/map.json`, `world/specifications.json`.
- **Decisions and their reasons:** `analysis/codelist-decisions.md` is the authority. Supporting files:
  - `analysis/codelist-classification.md` and `analysis/identifier-classification.md` (the Q- and ID-Q-numbers);
  - `analysis/source-verification.md` and `analysis/q18-payment-channel.md`.
  - `analysis/o150-design.md`: the design study for a possible flow of thermal modification as contract processing (O150), decided at the end of stage 6.
- **External code lists:** sources in `world/codelists/sources/` (provenance and SHA-256 in `PROVENANCE.md` and `PROVENANCE-second-round.md`); list definitions in `world/codelists/lists.json`.

## Where the reviews, the worklist and the open decisions are

The examples were reviewed in November 2026 and the findings are being worked through. Nothing in the examples has been changed for them yet.

- **Reviews of each example:** `world/examples/<flow>/NN-DocType.llm-review.<run-id>.merged.md` (250 files, made with the skill `.claude/skills/ubl-example-review`; the part files next to them are the merge's input). Status and the merges' decisions on recurring problems: `analysis/review-merge-decisions.md`.
- **Review across flows:** `analysis/consistency-review.20261114T2143Z-consistency.md` (index) and one file per topic beside it.
- **The worklist:** `analysis/worklist.md` groups the 3,348 findings into 128 root causes, in stages. `analysis/worklist-assignments.csv` links every finding to its cause.
- **The owner's decisions:** `analysis/worklist-decisions.md`. It holds the decisions D1 to D48 with their outcome, the **story lines** (the backstory decided so far: history, geography, languages, identification, prices, calendar and more) and the register of **open points** (O-numbers). It is maintained by hand and is the authority for what was decided on 2026-11-15/16; where it revises `analysis/codelist-decisions.md` or `note/src/03-world.md`, it wins until those are brought into line. Read its section "Open points", and the rules at its head, before deciding or fixing anything.
  - **State on 2026-11-17:** all decisions D1 to D48 are taken (D47 and D48 are the new flows medicines and lpg) (D6, signatures, goes to a stage of its own), and so are the open points O82 (the map is a diagram; geography comes from a place list), O83 (what the energy protocol asks of networks) and O86 (what a document says about a party). D28 set the rule for example file numbers: a new document gets the next free number of its flow, and a removed number is never reused; D38 lists the documents added and removed. **Next is implementation**, in the stages of `analysis/worklist.md`, with the open points. The new flows medicines (D47) and lpg (D48) are built after the other findings; a reefer of fresh food by sea (O137) is still to design. When a flow is implemented, its story and its XML are read against each other (O112).
  - **The site review** (2026-11-20, of the site built from `4242ac3`): `analysis/site-review.4242ac3.md`, findings grouped as SR-01 to SR-24 with a status line each, and the owner's answers; its open points are numbered OW001 onwards in the same register.
  - **The map session's points** (the 3D map and the terrain under it) are numbered MO001 onwards in the same register, so they take no O-numbers; MO001 to MO010 are all done or closed (2026-11-19). The map session is finished (owner, 2026-11-20): changes to the map and the 3D map are now made in the working session, following the agreed principles (O152, O241).
  - **Owed to the owner before they are applied:** the party table with the coverage before and after (O88), the place list (O91) and the coverage before and after each flow decision (O95, O101, O104, O108, O113, O116, O118 and the coverage parts of O125, O128).
- **Tables and checks over all examples** (no tokens, seconds): `python3 -I .claude/skills/ubl-example-review/scripts/extract_tables.py` writes CSV tables to `.review/tables/` (not committed; `--check` says whether they are current); `check_consistency.py` prints mechanical hits; `list_findings.py` collects every finding of every review.
- **The world's position on the real ocean:** `analysis/world-position/` (maps, drawing scripts, sources).
- **The reviews are kept** (the owner's decision): the worklist and the decisions cite their findings (`sea/29#F12`), and they are the "before" picture for a later review run. Do not delete or regenerate them; a new run gets a new run-id beside them.
- **Never run `analysis/review-scripts/worklist/make_docs.py`:** it would overwrite the decisions file.

## How to work

- **Fix things at the source:** the generators `tools/build_examples.py`, `tools/examples_kit.py`, `tools/examples_scenarios.py`, the world data and `lists.json`. Never edit the generated XML or `.md` by hand.
- **Full build and checks:** `bash tools/build_site.sh <outdir>` (outdir outside the repo or `_site`). It builds the code lists, the examples and the map, and runs the world, identity, address and IND checks plus XSD and phase-2 validation.
  - Requires Python 3 with `lxml`, and `xsltproc`, `xmllint` and `pandoc` (`apt-get install -y xsltproc libxml2-utils pandoc`). It fetches the OASIS stylesheets into `.oasis` and the UBL 2.5 files into `.ubl`, so it needs access to github.com and docs.oasis-open.org.
  - The reviews `*.llm-review.*.md` next to the examples are not generated: the build leaves them alone and does not publish them.
- **Terrain:** the landscape is generated by `python3 tools/terrain.py` from `world/terrain-inputs.json` into `world/terrain.json` and `world/terrain/*.png` (committed). Generating needs numpy, scipy and numba (`pip install numpy scipy numba`); the site build does not. `check_world.py` runs `terrain.py --check`, so change the inputs or the generator only together with a regenerated terrain (O152).
- **Validation only:** `python3 tools/validate_examples.py world/examples/*/*.xml` (about 10 s: parallel workers and batched Saxon runs; `VALIDATE_JOBS=n` sets the number of workers).
- **Coverage** of the endorsed UBL 2.5 elements: `sh tools/coverage_world.sh`. It is now 4621/5160 (2026-11-20). Of the 539 missing elements, 6 were never covered and are left out on purpose (see Open work); the others were lost by removing fillers and misplaced values and by the item and party tables, each with its row in `analysis/coverage-register.md` (where it was lost, its candidate case, its place); the build stops when an element goes missing without a row (`tools/coverage_register.py`, run by `check_world.py`), so a change that removes an element's last example adds its row in the same commit.
- **New words** for the invented languages: when the build reports missing words, save the list as `missing.json` and run `python3 tools/lexicon.py missing.json qau` (or `qal`). Never invent words by hand.
- UBL 2.5 validation files are fetched into `.ubl/` (not committed) by the tools.

## Rules agreed for the examples

These are the general rules at the top of `analysis/codelist-decisions.md`.

- **No fillers, and nothing implied by absence** (UBL IND5/IND6). A value must have a real business reason in the world. An element that has no real case stays out, even if coverage drops.
- **Two layers: the workshop and the world** (owner, 2026-11-20). Decisions, open points, reviews and story lines are internal: they exist to make the world coherent, plausible and believable. Everything published about the world states it as fact, in the present, complete on its own; a value is explained by the world, never by why the project chose it. No D/O/MO/Q/ID-Q/C numbers, review-finding IDs or change words ("no longer", "was moved", "proposed") in published world text; keep the traceability in code comments or unprinted keys. The method note may describe the process in general terms.
- **Semantic conformance** (UBL 2.5 §4.7/§7.2): use every element according to its UBL definition, even where established practice (EN 16931/Peppol) differs. Record such differences as findings.
- **Code lists:**
  - every code has a listID (except the party-internal codes of Q1);
  - real external lists come from verified sources;
  - UN/EDIFACT lists only where UBL itself, established practice or the domain authority uses them;
  - otherwise regional (Trade Accord) or national lists.
- **Identifiers:**
  - schemeIDs keep their current style;
  - codes held in IDs carry their list as schemeID;
  - identification conventions per party (GS1 / ISO via Codana / own numbers);
  - address registers by country level.
- **Fictional values must not be mistaken for real ones.** Check them against the real registers (ISO 4217, MIC, GS1, ITU, ICAO, BIC owner codes …), as recorded in the sources.
- **The world must stay consistent:** transport legs run on the map's routes, vehicles are derived from the legs, and the pipelines follow the pipeline rules.

## Git and deployment

- Work on the session's designated branch and commit with clear messages.
- Deploy by pushing the branch to `main`, and only after a full clean build. **Owner, 2026-11-19:** while working through the worklist, each fix is checked, fully built and then deployed to `main` on its own (no need to ask again for each). `.github/workflows/pages.yml` publishes to the `gh-pages` branch, and only while its commit is still the head of main.
- No pull requests unless asked.

## Open work

0. **Work through the review findings** (see "Where the reviews, the worklist and the open decisions are"):
   - the flow decisions D28 to D48 are taken (2026-11-17); now the stages of `analysis/worklist.md`: fixes that need no decision, the world rules decided in D1 to D27, master data, the goods chain, time and numbering, the flow stories, build checks, and last the signatures stage;
   - rules agreed for this work: every decision is recorded in the decisions file with what it means for the world; every open question goes into the open-points register in the same turn; nothing made in a session is left outside the repository by accident.
1. **The owner's review of the examples, flow by flow,** smallest flows first: waste, carnet, mast … (now done together with the flow decisions of item 0).
2. **An encyclopaedia of the world**, linked from the map: clicking a tile opens the page for what is there. **Decided (owner, 2026-11-20):** its name is simply **"Encyclopedia"**; it lives under **`/wiki/`** on the site for now (later perhaps `wiki.ublworld.eu`, so links between it and the site come from one setting); it **looks different from the main site** (a classic reference work: paper-like, serif text, framed infoboxes), with encyclopedic conventions (short description, infobox, lead, contents, sections, see also, references, categories) but **nothing of Wikipedia's own name, logo or design**; the example documents serve as its **references**. **Everything is generated** from the world data at every build: facts and figures from the data, prose from new in-world fields in the world data (no hand-edited pages), checked by the build (links, dates against founding dates and the calendar, named things exist, the published-text check). The party pages become its company articles. It covers:
   - countries, history, settlement and the Trade Accord and other treaties;
   - towns and remarkable buildings;
   - company histories and infrastructure, with timelines.

   Build it from the existing story and data, and extend it where the story has gaps.
3. **A write-up for the OASIS UBL TC and CEN/TC 434** of the findings collected in `analysis/codelist-decisions.md`:
   - three EN 16931 bindings that conflict with UBL 2.5 semantics: ItemClassificationCode, InvoicePeriod/DescriptionCode for the tax point date, and self-billing as Invoice + 389;
   - five issues with UBL's own default code lists and CVA.
4. **The 7 uncovered elements:** RadioactiveMaterial TransportIndex and FissileCriticalitySafetyIndex, ContractExtension/MinimumNumberNumeric, SubcontractTerms/MinimumPercent, ShipmentStage/TransshipPortLocation, Manifest/DeclaredCarriageValueAmount, QualificationResolution/ExclusionReason. Add them only through a real business situation in the world. TransportIndex is now covered by the medicines flow (D47); planned: ExclusionReason with an excluded contest candidate (O102).
5. **The method note** (`note/src/`): no rework now (owner, 2026-11-20); it may be reworked later. The site review's findings on it (SR-21 to SR-23: its date and state, the checks it lists, the party identifier, the order of its chapters) wait until then.
6. **Optional sources:**
   - the official UNECE UNTDID directory (unece.org blocks automated access, so the owner has to download it);
   - the names and definitions of the ISO 20022 internal codes (ChargeBearer, ClearingChannel, SequenceType).
