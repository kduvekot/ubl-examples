# ubl-examples: guide for working sessions

## What this repository is

- `xml/`: the UBL sample documents as published by OASIS, one commit per document (history and tools: `history/README.md`).
- `world/`: a fictional **UBL 2.5 example world**, with about 250 validated example documents in `world/examples/<flow>/NN-DocType.xml`. Each has a `.md` next to it that gives the reason for every value.
  - **Countries:** Urvania (XU), Bayvarra (XB) and the island Lisavu (XL), trading under the Lumeport Trade Accord.
  - **Languages:** English, plus the invented Urvanian (`qau`) and Lisavan (`qal`).
- The site (note, examples, coverage, the isometric map) is built from all of this and published to GitHub Pages.

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
- **External code lists:** sources in `world/codelists/sources/` (provenance and SHA-256 in `PROVENANCE.md` and `PROVENANCE-second-round.md`); list definitions in `world/codelists/lists.json`.

## How to work

- **Fix things at the source:** the generators `tools/build_examples.py`, `tools/examples_kit.py`, `tools/examples_scenarios.py`, the world data and `lists.json`. Never edit the generated XML or `.md` by hand.
- **Full build and checks:** `bash tools/build_site.sh <outdir>` (outdir outside the repo or `_site`). It builds the code lists, the examples and the map, and runs the world, identity, address and IND checks plus XSD and phase-2 validation.
- **Validation only:** `python3 tools/validate_examples.py world/examples/*/*.xml`.
- **Coverage** of the endorsed UBL 2.5 elements: `sh tools/coverage_world.sh`. It is now 5153/5160, and the 7 missing elements are uncovered on purpose (see Open work).
- **New words** for the invented languages: when the build reports missing words, save the list as `missing.json` and run `python3 tools/lexicon.py missing.json qau` (or `qal`). Never invent words by hand.
- UBL 2.5 validation files are fetched into `.ubl/` (not committed) by the tools.

## Rules agreed for the examples

These are the general rules at the top of `analysis/codelist-decisions.md`.

- **No fillers, and nothing implied by absence** (UBL IND5/IND6). A value must have a real business reason in the world. An element that has no real case stays out, even if coverage drops.
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
- Deploy by pushing the branch to `main`, and only after a full clean build. `.github/workflows/pages.yml` publishes to the `gh-pages` branch, and only while its commit is still the head of main.
- No pull requests unless asked.

## Open work

1. **The owner's review of the examples, flow by flow,** smallest flows first: waste, carnet, mast …
2. **An encyclopaedia of the world** (name still to choose), linked from the map: clicking a tile opens the page for what is there. It covers:
   - countries, history, settlement and the Trade Accord and other treaties;
   - towns and remarkable buildings;
   - company histories and infrastructure, with timelines.

   Build it from the existing story and data, and extend it where the story has gaps.
3. **A write-up for the OASIS UBL TC and CEN/TC 434** of the findings collected in `analysis/codelist-decisions.md`:
   - three EN 16931 bindings that conflict with UBL 2.5 semantics: ItemClassificationCode, InvoicePeriod/DescriptionCode for the tax point date, and self-billing as Invoice + 389;
   - five issues with UBL's own default code lists and CVA.
4. **The 7 uncovered elements:** RadioactiveMaterial TransportIndex and FissileCriticalitySafetyIndex, ContractExtension/MinimumNumberNumeric, SubcontractTerms/MinimumPercent, ShipmentStage/TransshipPortLocation, Manifest/DeclaredCarriageValueAmount, QualificationResolution/ExclusionReason. Add them only through a real business situation in the world.
5. **Optional sources:**
   - the official UNECE UNTDID directory (unece.org blocks automated access, so the owner has to download it);
   - the names and definitions of the ISO 20022 internal codes (ChargeBearer, ClearingChannel, SequenceType).
