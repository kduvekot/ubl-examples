# Site review at 4242ac3

A review of the published website (the `gh-pages` branch): are its texts correct, up to date,
relevant and in line with what the project is making? Review only; nothing has been changed for it.

- **Basis:** the site at `gh-pages` commit `4e9ebf5`, built from `main` commit **`4242ac3`**
  (2026-11-20 00:39 UTC, "O226 done"). Every finding describes that state. The file name carries the
  commit, so a later review gets a file of its own beside this one.
- **Made:** 2026-11-20, by six reviewers in parallel (parts A to F below), merged and grouped here.
  The owner's instruction for the examples: no detailed value review (the November reviews cover that),
  but the page structure and the flow, whether a value's explanation is still in line with what was
  decided, and whether the process that makes the explanations keeps them right.
- **Authorities:** `analysis/worklist-decisions.md` first, then `analysis/codelist-decisions.md`, then
  `note/src/03-world.md` and the world data (as in `CLAUDE.md`).
- **Mechanical checks done once, clean:** every internal link and anchor of the 420 pages resolves
  (the `world.html#NN-xx` hashes are handled by the map's script); every absolute link to the published
  code lists resolves; the published code lists are byte-identical to `world/codelists/`
  (`build_codelists.py --check`); no console errors or failed requests on any page type.

## How to keep this file up to date

- Each grouped finding **SR-nn** has a **Status** line. Change it when something happens:
  `open` → `decided (date, owner: …)` → `solved in <commit>` (or `dropped (reason)`).
  When a group is partly solved, say which part findings are done.
- The part findings (A-01 … F-10) stay as written: they are the "before" picture, like the November
  reviews. Do not renumber them; refer to them from the SR status lines.
- The questions (Q-…) have their own status in the register below; an answer goes there with its date,
  and the SR groups that depend on it are updated in the same commit.
- The open point **OW001** in `analysis/worklist-decisions.md` points to this file and is closed when
  every SR group is solved or dropped.

## Summary

80 part findings (5 high, 51 medium, 24 low), grouped into 24 causes, and 21 questions for the owner.

The main points:
1. **The front of the site still tells the OASIS-samples story** (SR-01, SR-02). The landing page's
   figures (27 % of elements, 55/101 document types) and the coverage page are about the OASIS
   samples; the world examples (4571/5160 = 88.6 %, 93/93 endorsed document types) appear nowhere.
   Examples, specifications and code lists have no card; specifications and code lists no nav entry.
2. **How an explanation is kept up to date** (SR-09, high). A flow's story is kept by hand in four
   copies (reasons in `examples_scenarios.py`, texts in `world/documents.json`, the story lines in the
   decisions file, `note/src/03-world.md`). Reasons computed from the world data stay current; hand-written
   sentences that copy a fact do not, and no check compares them with the decisions. The only safeguard
   is the O112 read-through, recorded for 6 of 18 flows; the stale texts were found in the others.
3. **Texts left behind by taken decisions** (SR-13, SR-10, SR-18): "consortium partner" on three tender
   pages (D28), the debit note the customer issues (D9), the public-billing claim against D17.2, northern
   seasons (D27), the fair in Lumeport (O133), and five flow introductions that do not tell their decided story.
4. **Internal references in reader texts** (SR-07): thousands of D-, O-, Q-, cause and review-finding
   numbers in the reasons and party texts, none of which a site reader can resolve.
5. **Navigation** (SR-04): an example page has no way back to its flow, no previous/next, and no link
   to its parties, its specification or the map.
6. **Gaps, order and status** (SR-11, SR-12): removed numbers (furniture/14, sea/28, tender/34) and
   documents added out of time order are not explained; nothing says that the examples were reviewed in
   November, which flows have their decisions built, or which flows are planned (D47, D48, O137).
7. **The method note** (SR-21 to SR-23) is still dated 5 November, lists checks as "still to come" that
   the build runs, and puts 1,660 lines of backstory before the method.
8. **Outside the site:** three story lines in the decisions file lag behind later decisions (D32 by
   O155, D37's hub by O214, D34's "new wood" by O149; also ore's 180 km against 159 km, the mast stowage
   against O210). The site follows the later decisions. (SR-09, E-12.)

## The principle that governs the answers

**Two layers (owner, 2026-11-20, SR-09):** decisions, reviews and story lines are the internal workshop; the site
shows the world as fact. Several later groups follow from it: SR-07 (no internal numbers), SR-08 (no staging
markers), SR-11 (gaps are a project artifact), SR-12 (no per-flow status or planned flows in the world).

## Grouped findings

Severity of a group is the highest of its parts. Kind: wrong (today) · stale (against a decision) ·
irrelevant · structure · process.

| SR | Cause | Sev. | Parts | Questions | Status |
|---|---|---|---|---|---|
| SR-01 | Headline figures and coverage page describe only the OASIS samples | high | A-01, A-03, A-05, A-11 | Q-A-01 | decided |
| SR-02 | Site structure: missing landing cards, nav labels, specifications and code lists unreachable | medium | A-02, A-04, A-06, A-07, A-08, D-09, E-03 | Q-A-02 | open |
| SR-03 | Pages outside the site frame | low | A-10, B-18 | | open |
| SR-04 | No navigation between examples, flows, parties, specifications, map and story | medium | E-04, C-12, D-09, B-05 | | open |
| SR-05 | Map sheet: image overflow, misplaced and overlapping labels, no legend | medium | A-09, C-11 | | open |
| SR-06 | Interactive map texts: opening card, no legend or scale, jargon | medium | C-02, C-10, A-10 | | open |
| SR-07 | Decision, open-point, cause and review-finding numbers in reader texts | medium | C-03, E-07, F-09, B-16 | Q-C-04, Q-E-01 | decided (by SR-09) |
| SR-08 | "Proposed addition to the 26+C set", "new" and "Parties 27 and up" leftovers | medium | C-05 | Q-C-02 | open |
| SR-09 | Process: hand-kept copies of each story drift, and no check ties them to the decisions | high | E-08, E-12, B-20, C-16, D-11, A-05 | Q-D-03 | decided |
| SR-10 | Flow introductions do not tell the decided story (O112) | medium | F-06, E-10 | Q-F-01 | open |
| SR-11 | Removed numbers and documents added out of time order are not explained | medium | E-01, E-02, F-08, B-06 | Q-F-02, Q-E-04 | open |
| SR-12 | Review and implementation status, and the planned flows, are invisible | medium | E-09, B-04 | Q-E-02, Q-E-03, Q-B-04 | open |
| SR-13 | Leads and reasons left behind by a taken flow decision | high | F-01, F-02, F-03, F-04, F-05, F-07, E-11 | | decided |
| SR-14 | Party descriptions wrong or told from the bench chain only | medium | C-01, C-08, C-09 | | open |
| SR-15 | A party page is not the party's full self-description (O86) | medium | C-06, C-07 | Q-C-03 | open |
| SR-16 | Party page naming and template wording | low | C-13, C-14, C-15 | Q-C-01 | open |
| SR-17 | Country and geography texts against the generated map | medium | C-04, B-19, B-03 | Q-C-05 | open |
| SR-18 | Specification texts that contradict decisions or the examples | high | D-01, D-02, D-03, D-04, D-05 | Q-D-02 | solved |
| SR-19 | Specification pages list examples that only name the specification (build bug) | medium | D-06 | | open |
| SR-20 | Specification pages define nothing, and their relation to EN 16931/Peppol is unexplained | medium | D-07, D-08, D-10 | Q-D-01, Q-D-04 | open |
| SR-21 | Method note: date, state and checks out of date | medium | B-01, B-02, B-09, B-10, B-11, B-13, B-14 | Q-B-03 | open |
| SR-22 | Method note: statements that contradict the world or a decision | medium | B-07, B-08, B-12 | | open |
| SR-23 | Method note: order, weight, unpublished paths and references | medium | B-15, B-16, B-17 | Q-B-01, Q-B-02 | open |
| SR-24 | Reason texts: repeated boilerplate and concatenation artifacts | medium | E-05, E-06, F-10 | | open |

### SR-01 · Headline figures and coverage page describe only the OASIS samples
- **Status:** decided 2026-11-20 (owner, Q-A-01): **A, the world examples only.** The site no longer points
  to the OASIS samples for its figures: "ours are more complete and better" (owner). What follows:
  - the landing figures and the coverage page are about the world examples (4571/5160 endorsed elements,
    93/93 endorsed document types at the time of the review), with no OASIS baseline beside them;
  - the figures are computed by the build (from `tools/coverage_world.sh` and the model), not scraped from
    prose; the build fails when a figure cannot be computed (removes A-05);
  - the coverage register is published, with the elements left out on purpose and why;
  - the "initial analysis" of the OASIS samples (`analysis/element-coverage*.md`) leaves the site; whether the
    OASIS history pages (Releases, History) stay is part of SR-02 (Q-A-02).
- **What:** the landing tiles ("55 / 101 document types", "27% of UBL 2.5 elements used", "36 UBL releases",
  "76 OASIS example files") are scraped by `sed` from the hand-written `analysis/element-coverage.md`
  (OASIS samples, counted against 5,443 elements including deprecated ones); "36 releases" counts
  publication stages. `coverage.html` is the November "initial analysis" (46 types without example,
  an "Open decision" long taken, "part 2", "My corrections") and never mentions world coverage; the
  coverage register is not published. The scraping silently blanks a tile if the wording changes.
- **Source:** `tools/build_site.sh` (landing block), `site/index.html`, `analysis/element-coverage*.md`, `tools/coverage.py`.
- **Parts:** A-01 (high), A-03 (high), A-05, A-11.

### SR-02 · Site structure: missing cards, nav labels, unreachable sections
- **Status:** open
- **What:** no landing card for Examples, Specifications or Code lists; the second button leads to the OASIS
  release log; `releases.html` is the README titled "ubl-examples" about `xml/` only; "Releases" and "History"
  are both OASIS history and "History" reads as the world's; specifications are linked from one sentence
  on examples.html; the code lists from nowhere (`codelists/` gives a 404) and the "-2.4-world" names are
  explained only inside the files; examples.html has no contents list and an unexplained flow order.
- **Source:** `site/index.html`, `NAV_ITEMS` in `tools/build_site.sh`, `README.md`, `tools/build_world.py`.
- **Parts:** A-02, A-04, A-06, A-07, A-08, D-09, E-03.

### SR-03 · Pages outside the site frame
- **Status:** open
- **What:** `world.html` has its own toolbar instead of the site header (and at 400 px its layer buttons
  are cut off); the method note has its own bar, no site nav and no build line.
- **Source:** `site/world.html`, `note/xsl/draft-note-html.xsl`.
- **Parts:** A-10, B-18.

### SR-04 · No navigation between examples, flows, parties, specifications, map and story
- **Status:** open
- **What:** an example page has no link back to its flow, no previous/next, no table of contents, and no
  link to its parties, its specification or the map; the World section does not link to the note's world
  chapter; the note's flows section has no list of the flows and no link to the examples.
- **Source:** example loop in `tools/build_site.sh`, `tools/build_examples.py` (page md), `tools/build_world.py`, `note/src/`.
- **Parts:** E-04, C-12, D-09, B-05.

### SR-05 · Map sheet
- **Status:** open
- **What:** the 4,961 px PNG (6.8 MB) is shown at natural size, so the page scrolls sideways at every width
  (no image rule in `site/site.css`); "Port of Selanu" stands about 45 km from its symbol, "Selanu Airport"
  reads as a village, "Euridice Crossing" overprints "Tallowford"; no legend, so border and pipelines look
  alike; the offshore gas line ends without a platform.
- **Source:** `site/site.css`, `analysis/world-position/refine_map.py`.
- **Parts:** A-09, C-11.

### SR-06 · Interactive map texts
- **Status:** open
- **What:** the opening card says "54 places" (parties), tells only the bench chain and gives every country a
  chamber of commerce (Bayvarra has none); no legend, no scale (3.5 km a square), no note that Lisavu is drawn
  nearer than it lies (D19 promised an inset); towns cannot be clicked; the foot uses unexplained terms.
- **Source:** `site/world.html`, `tools/build_world.py`.
- **Parts:** C-02, C-10, A-10.

### SR-07 · Internal references in reader texts
- **Status:** decided 2026-11-20 by the two-layer principle (SR-09): all D/O/MO/Q/ID-Q/C numbers and review-finding
  IDs leave the published texts; traceability goes into code comments or unprinted keys; the build check of SR-09
  point 3 keeps them out. The note's unpublished repository paths (B-16) are part of SR-23.
- **What:** reasons cite about 1,900 D-, 332 O-, 570 Q/ID-Q-numbers, about 250 review-finding IDs and 237
  worklist causes (513 review IDs on 125 pages); party pages and map cards print "(decision D37)", "(D30, O105)",
  "(O226, O50)" on 43 pages; none resolves on the site; tender/38 cites a finding of the removed tender/34;
  "decision D1" and "decision ID-Q7" look alike. The note cites 28 repository paths that are not published.
- **Source:** `tools/examples_scenarios.py`, `tools/examples_kit.py`, texts in `world/*.json`, `note/src/`.
- **Parts:** C-03, E-07, F-09, B-16.

### SR-08 · Leftover staging markers on party pages
- **Status:** open
- **What:** "proposed addition to the 26+C set" (19 pages), the "new" badge and the map foot "Parties 27 and up
  are proposed"; inconsistent with the data (#45–#47 not flagged); all decisions are taken.
- **Source:** `tools/build_world.py`, `tools/party_cover.py`, `site/world.html`.
- **Parts:** C-05.

### SR-09 · Process: how an explanation stays current
- **Status:** decided 2026-11-20 (owner). **The principle: two layers.** Decisions, choices, reviews and story
  lines are internal (the workshop); they exist to make a coherent, plausible and believable world. The site
  shows the world as fact; there is no need for the outside world to know why a decision was made, just as the
  reasons behind a real company's choices, or why a town exists or moved, are not known outside (owner).
  Recorded as a general rule in `analysis/codelist-decisions.md` and in `CLAUDE.md`. What follows:
  1. the published source is the world data (`world/*.json`, the scenarios' reasons, the note's world
     chapter), written in-world, present tense, complete on its own; the decisions file is internal and nothing
     published depends on it or refers to it;
  2. O112 reads the published story and the XML against each other for coherence, using the decisions to see
     that nothing was left behind; it is recorded for every remaining flow and is part of "flow done" for each
     new flow (D47, D48, O137); the lagging story lines are brought into line as O197 requires (E-12);
  3. a build check fails on D/O/MO/Q/ID-Q/C numbers and review-finding IDs in published text, and warns on
     change words ("no longer", "now instead", "was moved", "removed", "proposed");
  4. traceability to a decision is kept internally: a code comment or an unprinted key (`"source": "D28"`);
  5. key facts of each flow as assertions in the style of `ORE_ARRIVES`; counts and figures in hand texts
     (map cards, note figures, specification members) computed from the data where possible;
  6. specifications stay at version 1.0 (Q-D-03): in-world there is no history of changes to version.
- **What:** four hand-kept copies of each flow's story (E-08); 34 story assertions in the scenarios are the only
  automated tie; the O112 read-through is recorded for road, furniture, retail, cotton, sea and contest only.
  The story lines themselves lag their "Overtaken" notes (E-12; also D32/O155, D37/O214, D34/O149 from part F).
  The note's figures are copied by hand (B-20); the map's card, foot and meta texts are hand-written (C-16);
  `specifications.json` is checked by nothing and covered by no worklist cause or open point (D-11); the
  landing figures and coverage details are scraped (A-05).
- **Source:** `tools/examples_scenarios.py`, `world/documents.json`, `analysis/worklist-decisions.md`,
  `note/src/03-world.md`, `world/specifications.json`, `tools/check_world.py`.
- **Parts:** E-08 (high), E-12, B-20, C-16, D-11, A-05.

### SR-10 · Flow introductions do not tell the decided story
- **Status:** open
- **What:** the intros on examples.html (`flows[].text`) for road, cotton, sea, contest and retail are the old
  generic texts (road's 11–12–13 sequence unexplained); utilities (D31: household account, second suppliers),
  energy (D44: export split by buyer, each buyer's import), carnet (D40: lost voucher and proof; "both countries"
  in a three-country flow) and packaging (D41 goods balance, O168) lag their decisions.
- **Source:** `world/documents.json` `flows[].text`.
- **Parts:** F-06, E-10.

### SR-11 · Gaps and out-of-order documents
- **Status:** open
- **What:** the gaps furniture/14, sea/28, tender/34 are silent although `removed_documents` holds their reasons;
  documents added later (retail/23, furniture/19, tender/37–39, contest/17–18, rail/14, energy/10, waste/04)
  appear at the end of number-ordered tables without dates; only plastics/12 explains itself; the note does
  not explain the D28 numbering.
- **Source:** `tools/build_world.py` / `tools/build_examples.py` (examples.html), `world/documents.json`, `note/src/`.
- **Parts:** E-01, E-02, F-08, B-06.

### SR-12 · Status and plans are invisible
- **Status:** open
- **What:** nothing tells a reader about the November reviews, which flows have their decisions built, the
  pending world rules (O86, D6), or the planned flows (D47 medicines, D48 lpg, O137 reefer); the note does not
  mention them either.
- **Source:** examples.html generator, `world/documents.json`, `note/src/`.
- **Parts:** E-09, B-04.

### SR-13 · Leads and reasons left behind by a taken flow decision
- **Status:** decided 2026-11-20 (owner): fix all seven points at the source as proposed in the parts, in one fix
  commit that also records O112 for those passages:
  1. tender/13, 15, 20: "consortium partner" becomes the subcontractor Saltmere (`world/documents.json`);
  2. tender/02 and the review board's party text: "for appeals" (no mediation), also `tools/party_cover.py`;
  3. road/01 and rail/01: reasons of the southern calendar (autumn stock; rebuild stock before winter), dates kept;
  4. sea/24: issued on the next working day (Monday 1 June);
  5. **tender/40 Tender Receipt is built, as D38 decided** (owner), and tender/18 cites it instead of the receipt
     "(not shown)";
  6. road/11, tender/26, contest/05 and 10: one clause each for the turn of the story;
  7. packaging/09: the trade fair in its place per O133.
- **What:**
  - tender/13, 15, 20: "consortium partner" while the page shows `SOLE` and Saltmere as subcontractor (D28 p.3; `world/documents.json:2321, 2345, 2401`) (high);
  - tender/02: review body "for appeals and mediation" (D28 p.7; also `world/parties.json:1698`, `tools/party_cover.py:40`);
  - road/01 "spring stock", rail/01 "summer season" in March/April under the southern calendar (D27, O109; `examples_scenarios.py:350, 1127`);
  - sea/24 dated Saturday 30 May (D30 p.6; `examples_scenarios.py:5851`);
  - tender/18 cites a receipt "(not shown)"; tender/40 decided in D38 but not built and not deferred;
  - leads that leave out what the document now says: road/11, tender/26, contest/05, contest/10;
  - packaging/09 "During the trade fair in Lumeport" against O133.
- **Parts:** F-01 (high), F-02, F-03, F-04, F-05, F-07, E-11.

### SR-14 · Party descriptions wrong or told from the bench chain only
- **Status:** open
- **What:** the three customs services described as export-only or import-only, against their own documents;
  Codana "issues item identifiers" (against D5) with empty sections and "listed per flow below" at zero counts;
  Lumeway's text uses "#5/#26/#1"; the water company without district heating; the consumer without the web
  order and water bills; banks and ports from one chain; "Seller's Bank" for a bank of ten parties.
- **Source:** "what"/"how" texts in `world/parties.json`, `tools/build_world.py`.
- **Parts:** C-01, C-08, C-09.

### SR-15 · A party page is not the party's full self-description
- **Status:** open
- **What:** founding date, legal entity, customs trader number, Codana number or GS1 prefix, industry class and
  language are missing (O86, D4, D5, O22); fleets are on no party page and the map's vehicles are unexplained.
- **Source:** `tools/build_world.py`, `world/parties.json`.
- **Parts:** C-06, C-07.

### SR-16 · Party page naming and template wording
- **Status:** open
- **What:** page IDs `world-N-cc` mean nothing and #16, #19 repeat across countries; the footnote says "place"
  for a party element and repeats method text on every page; Valdara's page shows two identical "Park bench
  Serra 180" sections.
- **Source:** `tools/build_world.py`.
- **Parts:** C-13, C-14, C-15.

### SR-17 · Country and geography texts against the map
- **Status:** open
- **What:** "Urvania: Mainland, inland" on all 54 party pages against the map's coast and Porto Riparo (O152);
  Lisavu only "the overseas buyer" though it exports cotton; the note does not say party positions inside a
  town are a diagram (O82, O92) and gives the island's distance as both 1,080 and 1,100 km; the world's
  position still "to be confirmed" though O55 checked it.
- **Source:** `world/countries.json`, `tools/build_world.py`, `note/src/03-world.md`.
- **Parts:** C-04, B-19, B-03.

### SR-18 · Specification texts that contradict decisions or the examples
- **Status:** decided 2026-11-20 (owner, Q-D-02: B) and **solved in the commit "SR-18: specification texts …"**:
  - D-02: an invoice to a Bayvarran public body claims only Bayvarra's rules for public buyers, whatever the
    seller's country, and those rules now say that the tax on it is the seller's own (the exemption for public
    bodies is the Bayvarran supplier's); `national()` puts the public buyer's rule first by rule, not by the
    order of the file; the Urvanian page says so too. tender/32, 33, 39 already claimed only XB (unchanged);
  - D-01: billing: the supplier "charges an amount it billed too little with a debit note";
  - D-03: Urvania's invoice rules are its VAT content only (no discount, no statutory interest);
  - D-04: the port community applies to what passes through the port (documents of its types in the sea and
    cotton flows between two parties in Bayvarra, one a member): cotton/11, 12 and sea/15, 16, 17, 19, exchanged
    on or with the island, no longer claim it; the procurement community applies to every document a member
    sends or receives (no example changed); the page sentence is generated from the rule;
  - D-05: the roles of transport progress status and transportation status follow the examples.
- **What:** tender/32, 33, 39 claim only `XB:public-billing` (`national()` takes the first match) and the XB page
  says its exemption applies "whatever the seller's country", against D17.2 (high); the billing transaction
  says the customer issues the debit note (D9; rail/12, 13 are the supplier's); `XU:invoice` makes the seller's
  standard payment terms national rules (D22, D23); the port and procurement communities apply by flow, so
  cotton/11 and sea/19 claim the Lumeport port community, and "Members" lines mislead; role texts of transport
  progress status and transportation status do not match the examples.
- **Source:** `world/specifications.json`, `tools/world_specs.py`.
- **Parts:** D-02 (high), D-01, D-03, D-04, D-05.

### SR-19 · Specification example lists include nested CustomizationIDs
- **Status:** open
- **What:** "Examples that claim it" lists sea/03 DigitalAgreement (twice) and sea/04 DigitalCapability on six
  pages, because the build collects every CustomizationID in a document, not only the root's.
- **Source:** `tools/build_world.py:283-284`.
- **Parts:** D-06.

### SR-20 · Specification pages define nothing
- **Status:** open
- **What:** 54 of 70 transaction pages only repeat the UBL definition; no page states roles, rules, code lists or
  identifier schemes; the relation to EN 16931 and Peppol is unexplained and the URN prefix not marked invented;
  the self-billing page does not mention the Invoice + 389 deviation; stored title case ("Bill Of Lading"),
  UBL's own definition flaws quoted unmarked, community pages without owner or version.
- **Source:** `world/specifications.json`, `tools/build_world.py:275-331`.
- **Parts:** D-07, D-08, D-10.

### SR-21 · Method note: date, state and checks
- **Status:** open
- **What:** dated 5 November with revision "Skeleton"; the world chapter opens "as decided on 18 November" but
  holds decisions of 19 November and points to `analysis/` files; the principles promise business "between
  continents" and checks chapter 5 calls "still to come"; §5.9 lists checks the build already runs; chapter 5
  leaves out others (terrain, place list, coverage register, routes and vehicles, 40 t road rule, aircraft load,
  party profiles, price margins, reason-per-value); "Two rules" followed by four; "endorsed only" twice; the
  promised review and maintenance chapter is missing; §1.3 suggests the set "starts from" the OASIS samples.
- **Source:** `note/src/*.md`, `tools/md2docbook.sh`.
- **Parts:** B-01, B-02, B-09, B-10, B-11, B-13, B-14.

### SR-22 · Method note: statements against the world or a decision
- **Status:** open
- **What:** §4.3 says the party identifier is always the company register number (wrong for public bodies and the
  farm) and §3.7 calls Codana's `0990:` number "its party identifier" (the XML carries it as additional
  identification); chapter 4 "Where values come from" predates O86, D11, D24; §5.4 "every account in the same
  country" against O226.
- **Source:** `note/src/03-world.md`, `04-rationale.md`, `05-validation.md`.
- **Parts:** B-07, B-08, B-12.

### SR-23 · Method note: order, weight and references
- **Status:** open
- **What:** the world chapter is 84 % of the note and comes before the method, with method rules inside it;
  28 cited repository paths are unpublished ("see the party cover analysis" without a path); references
  missing for many cited standards, entries without address (ISO/IEC 15459, ISO 8601, the WTO agreement);
  Global Test Data listed but cited nowhere.
- **Source:** `note/src/`.
- **Parts:** B-15, B-16, B-17.

### SR-24 · Reason texts: boilerplate and artifacts
- **Status:** open
- **What:** 55 % of 42,344 value rows repeat a reason that occurs 20 times or more, a third are party or country
  master data, so the document's own reasons are buried (partly the state before O86); on 199 pages the
  IssueTime reason says "in the sender's local time; in the issuer's local time"; 4,560 rows start lower case
  after a full stop; an internal route key appears ("the map's route gas-field"); tender/13 shows "City of
  ferrano", "Town of valico euridice" (`.capitalize()` at `examples_scenarios.py:9454`).
- **Source:** `tools/examples_kit.py`, `tools/examples_scenarios.py`.
- **Parts:** E-05, E-06, F-10.

## Questions for the owner

Each question is given in full, with options and the reviewer's recommendation, in its part below.

| Q | Question | Recommendation | SR | Status |
|---|---|---|---|---|
| Q-A-01 | Headline figures and coverage page about the world examples, OASIS as a labelled baseline? | A: world first | SR-01 | **decided 2026-11-20 (owner): A, without the OASIS baseline** (see SR-01) |
| Q-A-02 | Specifications and code lists as sections, with a code-list index? | B: one "Reference" nav item; Releases + History merged into "OASIS samples" | SR-02 | open |
| Q-B-01 | Keep the Global Test Data reference? | B: as related work, with one sentence on why invented countries | SR-23 | open |
| Q-B-02 | Backstory in the method note? | A now (method first, backstory in an annex), B later (to the encyclopaedia) | SR-23 | open |
| Q-B-03 | Describe the review process in the note? | A: a chapter "Reviewing and maintaining the examples" | SR-21 | open |
| Q-B-04 | Decided but unbuilt flows in the note? | B: one sentence naming them | SR-12 | open |
| Q-C-01 | Readable names for party pages? | B now (hide "#n"), A (name slugs) with the encyclopaedia | SR-16 | open |
| Q-C-02 | Drop the "proposed / new" marking? | A on the site | SR-08 | open |
| Q-C-03 | How much master data on a party page? | A: the O88 "about itself" record, no personal data of persons | SR-15 | open |
| Q-C-04 | Where do D/O references live? | A: a separate, unprinted key; flow by flow with O112 | SR-07 | **decided 2026-11-20 (owner) by the two-layer principle (SR-09):** out of published text, into comments or an unprinted key |
| Q-C-05 | Is Urvania still inland? | A: a coast without a deep-water port | SR-17 | open |
| Q-D-01 | Do transaction specifications state rules? | A: generated sections from the examples, hand rules only where a decision makes one | SR-20 | open |
| Q-D-02 | Which national levels does a cross-border public invoice claim? | A: chain both, `XU:invoice` then `XB:public-billing` | SR-18 | **decided 2026-11-20 (owner): B**, the public buyer's rules only, their text cut back; `#compliant#` chains restrictions, not two countries' parallel rules |
| Q-D-03 | New version of a specification when a decision changes it? | A: keep 1.0 until a first release | SR-09 | **decided 2026-11-20 (owner): A**; in-world there is no change history |
| Q-D-04 | National specifications for the new flows? | decide with O138; B unless a real rule exists | SR-20 | open |
| Q-E-01 | How do decision and review references appear to readers? | B: link D/ID-Q/O to the decisions, strip review and cause IDs | SR-07 | **decided 2026-11-20 (owner) by the two-layer principle (SR-09):** not B; no reference of any kind in published text |
| Q-E-02 | Show review and implementation status per flow? | A: a status line in the data plus a paragraph on examples.html | SR-12 | open |
| Q-E-03 | Announce the planned flows? | A: titles only, no numbers | SR-12 | open |
| Q-E-04 | How to show removed numbers? | A: a muted row with the removal reason | SR-11 | open |
| Q-F-01 | Flow intro = the whole decided story line? | A: yes, the story lines brought up to date | SR-10 | open |
| Q-F-02 | How to show documents out of time order and removed numbers? | A: number order, a clause in each out-of-order "why", a row per removed number | SR-11 | open |

Q-C-04 and Q-E-01 are one question seen from two sides (where the references live, and how they show);
Q-E-04 and Q-F-02 overlap on the removed numbers; answer them together.

## The parts

The six reviewers' part files follow unchanged except for the heading levels. They hold the full text of every
finding (pages, source, quotation, what it should be) and of every question.


### Part A: landing page, navigation/template, releases/history/coverage pages, code lists (mechanical), presentation

Pages covered:
- `index.html`: read in full, every figure traced to `tools/build_site.sh` (landing-page block, lines ~128-138).
- Nav and template: `site/page.html`, `nav()`/`footer()` in `tools/build_site.sh`; `site/world.html` toolbar; the note's `site-bar` (`note/xsl/draft-note-html.xsl:61`). Scripted link graph over all 420 pages (reachability, incoming links to spec pages, map sheet, coverage-details).
- `releases.html` (README.md), `history.html` (history/README.md), `coverage.html` (analysis/element-coverage.md): read in full. `coverage-details.html`: header and summary read; regenerated with the current `tools/coverage.py` and diffed against the committed md.
- `codelists/`: scripted byte comparison of all 302 `gc/*.gc`, both `*-2.4-world.gc` and `UBL-World-2.5.cva` against `world/codelists/`; `python3 tools/build_codelists.py --check` ("up to date"). All files match; the published set is the repo's set.
- World coverage figures recomputed with `sh tools/coverage_world.sh` (output to scratch): 4571/5160 (88.6 %), 93 of 93 endorsed document types, 291/307 aggregates, 262 example documents.
- Presentation: Playwright, 1280 px and 400 px, DPR 1: index, note, world.html, world-5-xu, map-sheet, world-specifications, world-spec-transaction-waybill, examples, example-air-04-Waybill, coverage, coverage-details, releases, history (screenshots were working files, not kept). No console errors, no failed requests, no 4xx; the world map canvas renders at both widths. Only real layout problem: the map sheet (A-09).

#### Findings

##### A-01 The landing page's key figures describe the OASIS samples, not the project's examples
- Kind: wrong (misleading today)
- Severity: high
- Pages: `index.html`
- Source: `site/index.html` (stats section); `tools/build_site.sh` landing block: `n_doctypes` and `coverage` are scraped with `sed` from `analysis/element-coverage.md` (the OASIS `xml/` analysis), `n_examples=$(ls xml/*.xml | wc -l)`, `n_releases=$(grep -c '^### ' README.md)`.
- Finding: Under the hero "One coherent set of sample documents for UBL, set in a single fictional world …", the four tiles read "36 UBL releases, 2.0 to 2.5 · 76 OASIS example files · 55 / 101 document types with an example · 27% of UBL 2.5 elements used". The last two are the coverage of the 75 OASIS samples in `xml/`, against all 5,443 elements incl. deprecated ones and 101 document types incl. non-endorsed ones. The world examples, the subject of the hero line, cover **93 of 93** endorsed document types and **4571 / 5160 (88.6 %)** of the endorsed elements (`tools/coverage_world.sh`, CLAUDE.md). The tile labels do not say "OASIS", so a reader takes 27 % and 55/101 as the project's own coverage. No tile counts the 262 world examples, the flows or the parties. "36 UBL releases" counts publication stages (CSD/PRD/CS/COS/OS) from README headings; UBL 2.0 to 2.5 has six versions. history.html calls them "stages".
- Should be: The tiles lead with the world: number of example documents and flows, 93/93 document types, 88.6 % (4571/5160) of endorsed UBL 2.5 elements, with "endorsed" said. The OASIS figures, if kept, are labelled as such ("OASIS samples: 55/101 types, 27 %") and "releases" becomes "release stages". The figures come from the generators (`coverage_world.sh` / `coverage.py --endorsed`, `world/documents.json`), not from scraping a hand-written md.
- Related: Q-A-01; A-03, A-05.

##### A-02 The landing page has no card for the examples, the specifications or the code lists, and its call to action points at the OASIS releases
- Kind: structure
- Severity: medium
- Pages: `index.html`
- Source: `site/index.html` (hero `.actions`, `section.cards`)
- Finding: The six cards are Method, The UBL world, The map sheet, Releases, How the history was built, Element coverage. The project's main product, `examples.html` (262 documents with a reason for every value), has no card. It is reachable only from the nav. `world-specifications.html` (the Trade Accord's transactions, profiles and national/community specifications) and the published code lists have no card either. The two hero buttons are "Read the method" and "Browse the releases"; the second leads to the OASIS release log. Three of six cards (Releases, History, Coverage) are about the OASIS `xml/` history. The "Element coverage" card says "Which UBL 2.5 elements the examples use, which are missing", but the page covers the OASIS samples (see A-03).
- Should be: The cards include Examples (and Specifications, Code lists, see A-06/A-07), ordered world-first: Method, World, Examples, Specifications, Map sheet, then OASIS history (Releases + How the history was built, possibly one card), Coverage. Make the second hero button "Browse the examples". Reword the coverage card to say which set it measures.
- Related: Q-A-01.

##### A-03 coverage.html is the November "initial analysis" of the OASIS samples: stale, with an "Open decision" long taken, and no world coverage
- Kind: stale / irrelevant
- Severity: high
- Pages: `coverage.html`, `coverage-details.html`
- Source: `analysis/element-coverage.md` (hand-written, rendered by `page analysis/element-coverage.md coverage.html …`); `analysis/element-coverage-details.md` (output of `tools/coverage.py --examples xml`, committed).
- Finding: The page is titled "UBL 2.5 element coverage: initial analysis" and measures "the 75 sample documents" in `xml/`. Nothing on it says the world examples exist or that they are measured otherwise. Stale or wrong parts:
  - "New example documents needed: 46 document types have no example": Catalogue, SelfBilledInvoice, DeliveryNote, BillOfLading, the whole eTendering set, UtilityStatement, WasteMovement and others now all have world examples (93/93).
  - "## Open decision: Should coverage be added by changing the OASIS example files … or by adding new example files next to them": decided long ago. The world examples are separate ("kept apart from the examples of the OASIS UBL Technical Committee", examples.html).
  - "the document chains of part 2", "the part 2 party set": leftovers of an earlier plan; the site has no "part 2".
  - "My corrections" (first person), "Priority 1/2/3" lists, "Existing examples to extend": a work plan for editing OASIS files, which the project does not do.
  - Counting bases differ without explanation: 5,443 elements / 101 document types here, versus 5,160 endorsed elements / 93 endorsed types for the world (`coverage.py --endorsed world/ubl-model.json`).
  - The world's coverage register (`analysis/coverage-register.md`: every element lost by removing fillers, with its candidate case), the 7 elements left out on purpose (CLAUDE.md Open work 4) and the rule that the build stops when an element goes missing without a register row are not published anywhere on the site. Searches for "4571" and "coverage-register" over all pages find nothing.
- Should be: coverage.html shows the world examples' coverage (summary per document level and library, 93/93 types, the 589 missing elements in three groups: lost and registered with a candidate case, left out on purpose, never covered) and links the coverage register, generated by `coverage_world.sh` at build. The OASIS analysis stays as a short, clearly labelled baseline section, or moves under the OASIS history, without the open decision and the work plan. coverage-details.html lists the world's missing elements, or is labelled "OASIS samples".
- Related: CLAUDE.md "Coverage"; Open work 4; O102 and D47 (planned ExclusionReason, TransportIndex); Q-A-01.

##### A-04 The README rendered as releases.html describes only `xml/`, not the project
- Kind: stale / structure
- Severity: medium
- Pages: `releases.html` (and the GitHub repository front page, which shows the same README.md)
- Source: `README.md` lines 1-16; `page README.md releases.html "Releases" 3`
- Finding: The page's H1 is the repository name "ubl-examples" under the browser title "Releases". It opens with "A set of validated sample documents for UBL … `xml/` holds the sample documents published by the OASIS UBL Technical Committee", then repeats "How this history was built", which is the history page's job. It never mentions the world, its 262 examples, the site or the note. The release log itself (36 stages, files, added/removed) agrees with history/README.md and with the 36 tags on origin. The tags are named in plain text ("Tag `os-UBL-2.5`") with no link to the tag on GitHub.
- Should be: releases.html gets a proper H1 ("OASIS sample documents: releases") and a short intro saying that these are the OASIS samples, separate from the world examples, with a link to examples.html. Take the release log out of README.md into its own file, or render README.md from the "## Releases" heading only. README.md, as the repository front page, describes the whole project (world, examples, site). The tags could link to `…/releases/tag/<tag>` or `…/tree/<tag>`.
- Related: A-08.

##### A-05 Landing-page figures and the coverage details are scraped from hand-maintained files and would silently break or go stale
- Kind: process
- Severity: medium
- Pages: `index.html`, `coverage.html`, `coverage-details.html`
- Source: `tools/build_site.sh`: `n_doctypes=$(sed -n 's/.*Document types with an example:\*\* \([0-9]*\) of.*/\1/p' analysis/element-coverage.md)` and `coverage=$(sed -n 's/^| \*\*All\*\* |.*| \*\*\([0-9]*%\)\*\* |$/\1/p' …)`; `analysis/element-coverage-details.md` is committed output.
- Finding: (1) The figures come from bold markup in a hand-written md; any rewording gives an empty tile without a build error (`set -eu` does not catch an empty `sed` result). (2) `element-coverage-details.md` was made by an older `tools/coverage.py`. The current script writes "28.4% / 25.4% / 26.8%" where the committed file has "28% / 25% / 27%" (diff of 3 lines; everything else is equal). Nothing checks that the committed file is current. If it were regenerated and copied into element-coverage.md, "**26.8%**" no longer matches `[0-9]*%` and the tile goes blank. (3) The "/ 101" in the tile is hard-coded in `site/index.html`.
- Should be: The build computes the figures (`coverage.py`, `coverage_world.sh`, the world data) and fails when one is empty. A committed generated file gets a `--check` like the other generators, or is generated at build.
- Related: A-01, A-03.

##### A-06 Specifications are hard to find: no nav entry, no card, and the example pages name them without linking
- Kind: structure
- Severity: medium
- Pages: `world-specifications.html` and its 90 `world-spec-*.html` pages; all 262 `example-*.html`
- Source: `NAV_ITEMS` and `nav()` in `tools/build_site.sh` (the `world-*.html` pattern files spec pages under "World"); `site/index.html`; the CustomizationID/ProfileID reason text in the example md generator (`tools/build_examples.py` / `examples_kit.py`).
- Finding: Link graph: `world-specifications.html` has exactly one incoming link from outside the spec pages, a sentence on `examples.html` ("see the world's specifications"). No example page links to its specification. In example-air-04-Waybill the text reads "CustomizationID = urn:ubl-examples:world:trns:waybill:1.0 … Each has a public description on the world's pages (world/specifications.json)", with neither a link to `world-spec-transaction-waybill.html` nor to the profile page. World.html (the target of the "World" nav item) does not link to the specifications. The nav highlights "World" on spec pages, but nothing under World leads to them.
- Should be: Each example page links its CustomizationID and ProfileID values to the transaction/profile page. Specifications get a nav entry or a card, and spec pages are filed under Examples (or their own section) in `nav()`.
- Related: Q-A-02.

##### A-07 The published code lists have no landing page and are linked from nowhere; the "-2.4-world" names are explained only inside the files
- Kind: structure
- Severity: medium
- Pages: `codelists/` (302 `gc/*.gc`, `CountryIdentificationCode-2.4-world.gc`, `CurrencyCode-2.4-world.gc`, `UBL-World-2.5.cva`)
- Source: `tools/build_site.sh` (`cp world/codelists/*.gc …`, no index); `tools/build_codelists.py` (names derived from UBL's `CountryIdentificationCode-2.4.gc`, `CurrencyCode-2.4.gc`).
- Finding: Mechanically correct: every published file is byte-identical to `world/codelists/`, `build_codelists.py --check` says up to date, and the LocationUri values point to the published paths. No page links to any code-list file. `codelists/` has no index.html, so on GitHub Pages the directory URL is a 404. The note mentions only the repo paths (`world/codelists/lists.json`, `…/UBL-World-2.5.cva`) as text. In a UBL 2.5 world, the two files named "…-2.4-world.gc" are explained only by an XML comment inside them ("Derived from …/os-UBL-2.5/cl/gc/default/CountryIdentificationCode-2.4.gc … unchanged, with the codes of the UBL example world added"). The fact that UBL 2.5 itself ships these lists under their 2.4 names (the list versions did not change) appears nowhere on the site.
- Should be: A generated `codelists/index.html` (from `lists.json`/`world-codes.json`): every list with listID, agency (Trade Accord / national / world copy of an external list), version, source and link to the .gc, plus the CVA. One sentence on why two files carry "2.4". Link it from the landing page, the nav or the note §3.5, and from listID values on example pages if cheap.
- Related: Q-A-02.

##### A-08 Nav labels and order: "Releases" and "History" are OASIS-only but read as project sections; "History" collides with the world's history
- Kind: structure
- Severity: low
- Pages: all 414 pages with the site header
- Source: `NAV_ITEMS="… releases.html|Releases history.html|History coverage.html|Coverage"` in `tools/build_site.sh`
- Finding: The nav is "Method · World · Examples · Releases · History · Coverage". "Releases" and "History" both concern the reconstructed git history of the OASIS `xml/` folder. In a site whose world has its own invented history (countries, Trade Accord, company timelines; the planned encyclopaedia), a reader clicking "History" expects the world's history. Two of six top-level entries go to a side topic, while Specifications and Code lists have none (A-06, A-07).
- Should be: e.g. "Method · World · Examples · Specifications · Coverage · OASIS samples" (Releases + How the history was built under one section, the history page reached from it).
- Related: A-02, A-04.

##### A-09 Map sheet page: the 4,961 px image is shown at natural size, so the page scrolls horizontally at every width
- Kind: structure (presentation)
- Severity: medium
- Pages: `map-sheet.html`
- Source: `tools/build_site.sh` heredoc `.map-sheet.md` (`[![…](map-sheet.png)](map-sheet.png)`); `site/site.css` has no `img` rule at all (`grep img site/site.css`: none).
- Finding: Measured scrollWidth 5205 px at a 1280 px viewport and 4981 px at 400 px. The text column sits at the left, and the sheet runs far off to the right (screenshot `shots/map-sheet-400.png`). The page also loads the 6.8 MB PNG inline, although its own text offers it as a separate "Open the sheet at full size" link.
- Should be: `.prose img { max-width: 100%; height: auto; }` in `site/site.css`, and ideally a scaled preview (e.g. 1600 px wide JPEG/PNG made at build) inline, with the full sheet behind the link.

##### A-10 world.html (the "World" target) has its own toolbar instead of the site header; its footer text uses unexplained internal jargon
- Kind: structure / stale
- Severity: low
- Pages: `world.html`
- Source: `site/world.html` lines ~95-125 (toolbar, `.foot`)
- Finding: The page has only "←" to index.html and "Map sheet". There is no way to Examples, Specifications or Method other than going back to the landing page, while every party page reached from it has the full nav. At 400 px the layer buttons are cut off at the right edge ("Government" partly visible; Finance and Procurement hidden; screenshot `shots/world-400.png`), with no visible cue that the row scrolls. The footer says "Parties 27 and up are proposed additions to the 26+C set". "26+C set" is a working-paper term the site never explains, and parties 27-48 send and receive published examples. The list's "new" badges come from the same flag (`proposed` in `world/parties.json`, 19 parties).
- Should be: A compact link to the site nav (at least Examples) in the toolbar; wrapping or a scroll cue for the layer buttons at narrow widths. Drop the "proposed / 26+C" footer and the "new" badges, or explain them. (Party-page wording is left to the world reviewer.)
- Related: O86/O88 (party set and profile now applied).

##### A-11 Small text leftovers on coverage, history and releases pages
- Kind: irrelevant
- Severity: low
- Pages: `coverage.html`, `history.html`, `index.html`
- Source: `analysis/element-coverage.md`, `history/README.md`, `site/index.html`
- Finding:
  - coverage.html shows the link text "`element-coverage-details.md`". Only the href is rewritten by the `sed` in `page()`, so the reader sees a .md filename.
  - history.html's section "Relation to earlier attempts" ("The branches `claude/ubl-samples-hist-3IuwR` and `sample-research` (`official/`) held partial copies…") is repository housekeeping, not something a site reader needs. The branches still exist on origin.
  - "76 OASIS example files" (index) versus "75 sample documents" (coverage) is consistent only once you know about the detached signature file. A tile label "OASIS sample files (75 documents + 1 signature)" or a footnote would avoid the apparent mismatch.
- Should be: Use link text such as "the details page"; move the earlier-attempts paragraph to the repo (or drop it from the site); label the count.

#### Questions

##### Q-A-01 Should the site's headline figures and the coverage page be about the world examples, with the OASIS samples as a labelled baseline?
- Context: The landing tiles and coverage.html measure only the 75 OASIS samples (27 %, 55/101). The world examples reach 88.6 % of endorsed elements and 93/93 types, and their coverage register is the project's working instrument, but none of this is published (A-01, A-03).
- Options: A: world first, OASIS as a small labelled baseline (clear, shows the project's result; needs coverage_world output at build). B: show both side by side with equal weight (keeps the "before/after" story; busier). C: keep OASIS figures but label them (smallest change; still hides the project's result).
- Recommendation: A, because the hero text promises the world's examples, and CLAUDE.md treats world coverage (4571/5160) as the figure the project tracks.
- Findings depending on it: A-01, A-02, A-03, A-05.

##### Q-A-02 Should Specifications and Code lists become top-level sections (nav + landing card), and should the build generate a code-list index page?
- Context: Both are published (91 spec pages, 305 code-list files), but specifications are reachable from one sentence and the code lists from nowhere (A-06, A-07).
- Options: A: both in the nav and as cards, with a generated `codelists/index.html` (findable; two more nav items). B: one "Reference" nav item holding Specifications, Code lists and Coverage (compact nav). C: cards only, nav unchanged.
- Recommendation: B together with A-08's merge of Releases/History into "OASIS samples", which keeps the nav at six items.
- Findings depending on it: A-06, A-07, A-08.

Note on method: running `tools/coverage_world.sh` fetched `UBL-Entities-2.5.gc` into the repo's git-ignored `.ubl/mod/` (the tool's standard cache). Nothing tracked changed (`git status` clean).

### Part B: the method note `note/ubl-examples-method.html`

Pages covered: `note/ubl-examples-method.html` (one page, 6 chapters + appendix). How I covered it: I read all six sources `note/src/01…06-*.md` in full; `md2docbook.sh --check` in `build_site.sh` makes sure they match the HTML. I also checked the HTML for its title block, table of contents, footer and encoding, and read the hub `note/ubl-examples-method.xml`. I read the sources against `analysis/worklist-decisions.md` (story lines; D5, D19, D24, D27, D28, D38, D47, D48; O34, O55, O81–O86, O91, O92, O112, O152, O197, O214, O226), `analysis/place-list.md`, `tools/check_world.py`, `tools/build_site.sh`, `tools/build_examples.py` (its check_* functions), `tools/world_parties.py` and a sample of the XML (party identifiers in `world/examples/road/*.xml`).

Overall: the world chapter (`03-world.md`) has been kept close to the decisions, often closer than the story lines themselves. Examples: the bench model of O149/C69, the map distances of O152/O214, statutory interest (O148), share capital (O147), public-body registers (O142/O157/O158) and the lume account (O226). Where the story lines in the decisions file are older than a later point, the note follows the later point. I did not count that as a finding. Most problems are in the method chapters (1, 2, 4, 5), the title block, the references, and the structure.

#### Findings

##### B-01 Title block and revision history show the skeleton of 5 November
- Kind: wrong (today)
- Severity: medium
- Pages: note/ubl-examples-method.html (title block, page footer, Appendix A)
- Source: `note/ubl-examples-method.xml`: `<!ENTITY pubdate "5 November 2026">`, `<!ENTITY stage "wd01">`, the one revision row
- Finding: the page is dated "5 November 2026" three times, as "Working Draft 01 (proposal)". Appendix A gives the only revision as "wd01 | 5 November 2026 | Skeleton: introduction and principles." Since then the note has gained a world chapter of about 1,660 lines, a validation chapter and references, and its sources changed up to 2026-11-20 (`git log -- note/src`). Unlike every other page, the page has no "built from commit … of <date>" line (`footer()` in `build_site.sh` is not applied to the note).
- Should be: a publication date and revision rows that match the content: a row per published revision, or at least "wd01, in progress, last changed <date>". Alternatively, the build fills in the date of the last commit to `note/`.
- Process: nothing in the build touches `pubdate`, so the date will stay wrong. Let the build fill it in, e.g. `git log -1 --format=%cd -- note/` passed as an entity or an xsltproc parameter.
- Related: none

##### B-02 The world chapter's opening caveat is out of date and points readers to internal files
- Kind: stale (O81)
- Severity: medium
- Pages: note §3 (first paragraph)
- Source: `note/src/03-world.md:3-7`
- Finding: "This section describes the world as decided on 18 November 2026. The examples are being brought into line with it, and until that work is done some of them still differ … `analysis/worklist.md` and `analysis/worklist-decisions.md` say what is to be done."
  - The chapter already contains decisions of 19 November: O226 (the lume account), O157/O158 (registers), O148 (interest), O55 (position checked), the bench model C69. So "as decided on 18 November" understates it.
  - Stages G1–G8 were built on 2026-11-19, so "being brought into line" is now partly done.
  - A TC reader cannot open either file from the site.
- Should be: per O81, the paragraph goes once the examples follow the decisions. Until then it should name the date of the latest decision it covers. It should also say in plain words which parts may still differ, or link to the repository files on GitHub.
- Related: O81, CLAUDE.md "Nothing in the examples has been changed for them yet" (the same stale caveat)

##### B-03 The world's position is still called "to be confirmed", though O55 checked it
- Kind: stale (O55)
- Severity: low
- Pages: note §3.3 Geography
- Source: `note/src/03-world.md:284-287`
- Finding: "It is still to be confirmed against a nautical chart that both areas lie outside the 200-nautical-mile zones of the nearest islands and that no extended-shelf claim or sea-bed licence reaches them." O55 was checked on 2026-11-19 against Marine Regions EEZ v12, the CLCS submissions and the ISA contract areas: both areas are clear (the mainland is 220 km from Tristan's zone, Lisavu 188 km from Namibia's pending claim). Only the nautical chart is still open, plus a rerun before the position is cited outside the world.
- Should be: "Checked on 2026-11-19 against the published zones, shelf claims and sea-bed contracts: both areas are clear (the mainland 220 km from Tristan da Cunha's zone, Lisavu 188 km from Namibia's pending Walvis Ridge claim); a nautical chart is still to be consulted, and the check is rerun before the position is cited outside the world." Source: `analysis/world-position/README.md`.
- Related: O55, D19

##### B-04 The decided new flows (medicines D47, lpg D48) and the reefer case (O137) are missing
- Kind: stale (D47, D48, O137), depends on Q-B-04
- Severity: low
- Pages: note §3.17 Flows of documents, §3.8 Parties
- Source: `note/src/03-world.md:1451-1615`
- Finding: the chapter says it describes the world "as decided", but it does not mention the two flows decided on 2026-11-17:
  - medicines: Selanu General Hospital, a pharmaceutical wholesaler in Lumeport, an active temperature-controlled ULD, dry ice, and a Type A radioactive package with its transport index;
  - lpg: Kelpstone propane to the Coastal State Water Company's peak boilers, a new dangerous-goods road haulier, orange plates 23/1965.

  It also leaves out that the food reefer elements wait for a case of their own (O137). The text even says "No container is cooled: batteries … need no temperature control" (line 1581). That is right for the mast flow, but a reader would conclude that the world has no temperature-controlled transport at all.
- Should be: per O112, a flow's story goes into the note when the flow is implemented. Until then, one sentence in §3.17 should name the planned flows and the coverage they are for (Q-B-04, recommendation B).
- Related: D47, D48, O124, O126, O137, O138, O112; CLAUDE.md Open work 4 (TransportIndex)

##### B-05 "Flows of documents" gives no list of the flows and does not link to the examples
- Kind: structure
- Severity: medium
- Pages: note §3.17
- Source: `note/src/03-world.md:1451-1466`
- Finding: the section describes flows in general ("Goods cross the land border by road, rail and river barge … a public tender and a design contest, a temporary export with an ATA carnet, a utility in each country, and gas by pipeline"). Then it tells only the contest, the waste, the carnet and the air/ship rules in detail.
  - There are 18 flows with 262 documents (`world/examples/*`). The reader never learns their names (air, carnet, contest, cotton, energy, furniture, mast, ore, packaging, plastics, rail, retail, road, sea, tender, utilities, waste, wood), what each shows, or where to see them.
  - No link goes to `examples.html` or `world.html`. The note is the "Method" entry of the site navigation but does not lead into the rest of the site.
- Should be: a table of the flows (name, one-line story, document count, link to the flow on `examples.html`), generated from `world/documents.json` so that it cannot go stale. The individual stories can then stay as illustrations.
- Related: D28–D45 (the flow stories), O112

##### B-06 The numbering of example files and the visible gaps are not explained
- Kind: stale (D28, D38)
- Severity: low
- Pages: note (nowhere); visible on examples.html
- Source: missing from `note/src/04-rationale.md` / `05-validation.md`; the rule is in `analysis/worklist-decisions.md` "Example files: numbers (D28)"
- Finding: D28 says that a new document gets the next free number of its flow, even when it falls earlier in time, and that a removed number is never used again. D38 lists what was added and removed (tender −34, sea −28, furniture −14). The note says nothing about this. A reader therefore meets gaps (no tender/34, sea/28 or furniture/14) and numbers out of time order (tender/40, the tender receipt, is earlier than 18) without a reason.
- Should be: a short paragraph in the maintenance part (see B-14): example numbers are stable references that reviews and findings cite; new documents are appended; removed numbers stay free.
- Related: D28, D38

##### B-07 What the party identifier is: two chapters disagree with each other and with the XML
- Kind: wrong (today)
- Severity: medium
- Pages: note §4.3 and §3.7
- Source: `note/src/04-rationale.md:49-50`, `note/src/03-world.md:762-764`
- Finding:
  - §4.3: "The identifier is the party's number in its country's company register, given as `PartyIdentification` with the register as its scheme." That is wrong for public bodies, which carry their public-body register number (for example `xu_m2vd`, `3071845926` under `…:public-body-register` in road/*.xml; §3.6 line 637 says so), and for the farm (`XL:farm-register`).
  - §3.7: "its one number serves as its party identifier (`0990:` and the number)". In the XML the business register number is in `PartyIdentification` and `0990:…` is in `AdditionalPartyIdentification` (`0990:10014` 80 times). `check_party_profiles` also keys parties on `PartyIdentification/ID` = `registry_id`.
- Should be: one statement, in one place. The party identifier is the number in the register the party is entered in (business register, public-body register or farm register). A Codana or GS1 party also gives its Codana number (`0990:`) or GLN as an additional identification.
- Related: D5, O142, O86

##### B-08 Chapter 4, "Where values come from", is still from before O86, D11 and D24
- Kind: stale (O84, O86, D11, D24, D26, D27, O152)
- Severity: medium
- Pages: note §4.1, §4.3
- Source: `note/src/04-rationale.md:9-31`
- Finding:
  - "Party names, addresses, identifiers and accounts come from the identity of the party … These values are the same in every document that uses them." Under O86 (§3.8.1) a document carries a party's data to the depth its kind needs, and the receiver is described with only what the sender knows. Under D11 an item fact is stated only from the moment it becomes known.
  - "Document numbers, dates, quantities and the references between documents are what a flow adds." O84 records this as incomplete under D24, and it still reads the same. Since D24 numbers are each issuer's own sequence across flows, `ProfileExecutionID` belongs to one collaboration (D26), dates fall on working days (D27), and distances and times come from the map and the place list (O152).
  - Chapter 4 does not mention the party table (`analysis/party-profile.md`) or the item table (`analysis/item-profile.md`), although §3 says the build checks both.
- Should be: §4.1 names the layers as they are today: identity, the party and item tables (who says what about whom and when), the flow and its collaboration, the issuer's numbering, the calendar, the place list, code lists and calculation. §4.3 states the O86 rule in one sentence and refers to §3.8.1.
- Related: O84, O86, C01, D11, D24, D26, D27, O152

##### B-09 The principles promise business "between continents" and checks that chapter 5 calls "still to come"
- Kind: stale (O84, O51) and wrong (internal contradiction)
- Severity: medium
- Pages: note §2.2, §2.4 against §5.9
- Source: `note/src/02-principles.md:13-14`, `:24-33`
- Finding:
  - §2.2: "The world includes business within one country, within a region and between continents." The world has three countries in one free trade area and no outside partner (O51 is a later enhancement). O84 already asks for this sentence to change.
  - §2.4 says the documents are checked for "totals, dates and internal references" and "quantities along a process". §5.9 lists the same things as "Still to come".
- Should be: §2.2: "within one country, across a land border, overseas between a mainland and an island, and between members of a regional trade area". §2.4 and §5 must agree (see B-10).
- Related: O84, O51

##### B-10 "Still to come" lists checks the build already runs
- Kind: wrong (today)
- Severity: medium
- Pages: note §5.9
- Source: `note/src/05-validation.md:139-144`
- Finding: "Later layers add their own checks: document lines with items and quantities, amounts and taxes that add up, dates in a believable order, references between documents, and quantities that agree from order to invoice." Today:
  - every amount is calculated by `examples_kit` and the statements of a bill are checked to add up (`check_utility_statements`);
  - dates are checked by `check_calendar` (working days, D27/O79), `check_issue_order` (C72) and `check_due_dates`;
  - references by `check_reference_uuids` and `check_reference_targets` (C73);
  - quantities by `check_packages` and the goods-chain ledger (D21), and resale margins by the margin check in `world_items.py`.
- Should be: §5.9 is dropped or replaced by what is really still missing. Per `analysis/worklist.md`, that is stage 7 "build checks" and the signatures stage. The checks now in place go into the sections before it (B-11).
- Related: worklist stage 7, C72, C73, C94, D21, D27

##### B-11 Chapter 5 leaves out many checks the build runs and repeats others that are only in chapter 3
- Kind: stale / structure
- Severity: medium
- Pages: note §5.1–5.8, and §3 (9 places "the build checks it")
- Source: `note/src/05-validation.md`; `tools/check_world.py` (sequence: terrain.py --check, place_list.py --check, world_model, world_docs, world_parties, world_items, build_codelists --check, coverage_register); `tools/build_examples.py` (the check_* calls around line 3650-3711, the reason check at :1630)
- Finding: the chapter that says "The world is checked automatically every time the site is built" does not mention:
  - the terrain must be the output of its inputs (`terrain.py --check`, O152);
  - the place list must be current (`place_list.py --check`, O91);
  - the coverage register: the build stops when an element loses its last example without a row in `analysis/coverage-register.md`. This is a central rule of the "no fillers" method and the reader should meet it;
  - routes laid within gradients; legs on routes and carriers with a vehicle of the mode; the pipeline rules; the 40 t road rule and payload; the ATR 72-600F load;
  - the party table and the "who knows what about whom" check (`check_party_profiles`, `check_party_knowledge`);
  - payment terms and due dates; the price margins and the turnover bands;
  - "every value needs a reason" (it exists, at build_examples.py:1630, but §4's "a document with a value without a reason is not built" does not say how);
  - the calculation of `UBLVersionID` and the specification pages;
  - `md2docbook.sh --check`.

  Some of these are described only inside the world chapter (§3.3, §3.14, §3.15, §3.16, §3.17 "the build checks it"). §5.6 still says "believable terrain", though the terrain is now generated from geology and checked against its inputs.
- Should be: §5 lists every check group once, with a pointer to the world rule it enforces. §3 keeps the rule and says "checked, see §5.x".
- Related: O152, O91, CLAUDE.md "Coverage" (coverage register), O134 (40 t rule), O79, O90

##### B-12 "Every account at a bank in the same country": out of date since O226
- Kind: wrong (today)
- Severity: low
- Pages: note §5.4
- Source: `note/src/05-validation.md:60-62` against `note/src/03-world.md:1213-1221` and `tools/world_parties.py:21-23, 284-298`
- Finding: §5.4 says "every account is held at a bank of the world in the same country". §3.13 describes Valdara's lume account at Bank of Lumeport, and the check allows `account_abroad` with a stated reason (O226).
- Should be: "… in the same country, apart from a second account abroad held for a stated reason (Valdara's lume account for its framework contract)".
- Related: O226

##### B-13 Small errors in chapter 5
- Kind: wrong / structure
- Severity: low
- Pages: note §5.3, §4.4/§5.2
- Source: `note/src/05-validation.md:24-50`; `04-rationale.md:52-58` and `05-validation.md:17-22`
- Finding:
  - §5.3 opens with "Two rules of the UBL specification shape the data the world needs:" and then lists four (IND5, IND7/IND8, IND9, IND6).
  - The citation "(section 2.2.2, "Manifest Values")" does not say of which document.
  - "Only what UBL 2.5 endorses" is a section in both chapter 4 (§4.4) and chapter 5 (§5.2), with overlapping text.
- Should be: "Four rules …", name the document cited (the UBL 2.5 specification), and keep one "endorsed only" section.
- Related: none

##### B-14 The scope promises review and maintenance, but no chapter covers them; "Starting point" is misleading
- Kind: structure / stale; depends on Q-B-03
- Severity: medium
- Pages: note §1.2, §1.3
- Source: `note/src/01-introduction.md:15-33`
- Finding:
  - §1.2 promises "how examples are reviewed and maintained over UBL versions". No chapter describes the review (the per-example semantic review against the UBL 2.5 model, the cross-flow consistency review, findings grouped into root causes and stages, owner decisions with open points, the story read against the XML per flow, O112). Nor is maintenance described (regenerating on a new UBL release, the coverage register, `UBLVersionID` from the published models, stable example numbers D28). This is the part a TC most needs to judge whether the set can be maintained.
  - §1.3 says "The example set starts from the sample documents that OASIS published with each UBL 2.x release." The world examples are generated from the world data and kept apart from the OASIS samples (§4.5). The OASIS history is the base of the repository, not of the example set.
- Should be: a chapter "Reviewing and maintaining the examples", in general terms and without internal file names. §1.3 rephrased: "The repository starts from … ; the world's examples are made new, beside them."
- Related: O112, D28, CLAUDE.md "Where the reviews, the worklist …"

##### B-15 Order and weight: a TC reader meets 1,660 lines of backstory before the method
- Kind: structure; depends on Q-B-02
- Severity: medium
- Pages: note §3 against §4–§5
- Source: `note/ubl-examples-method.xml` (entity order s-world before s-rationale and s-validation); `note/src/03-world.md` is 1,661 of 1,974 source lines (84 %)
- Finding:
  - After two short chapters the reader gets the countries, a 130-line history (Tuscan voyages, the Sardinian corvette, Crimean War, peace treaty of 1947), towns and populations, holiday tables, prices and shop margins. Only then come "Choosing and documenting values" (64 lines) and "Checking" (144 lines).
  - Method rules sit inside the world chapter: §3.5 Code lists (including the deliberate departures from EN 16931 that are the core of the TC write-up), §3.6 Identifiers, §3.18 Specifications, §3.20 Who sends and who receives.
  - §3.19 Signatures is a three-sentence placeholder.
- Should be: Introduction; Principles; Method (values and reasons, code lists, identifiers, specifications, who sends and receives); Checking; Reviewing and maintaining; then the world as a short overview (countries, taxes, languages, flows) with the full backstory in an annex or, later, in the encyclopaedia (CLAUDE.md Open work 2). The departures from EN 16931 (§3.5 "Some choices differ …") deserve a section of their own that a TC reader finds from the table of contents.
- Related: CLAUDE.md Open work 2 and 3

##### B-16 The note sends readers to repository files that are neither published nor linked
- Kind: structure
- Severity: medium
- Pages: note §3 (28 path mentions across the sources), §4.5
- Source: e.g. `03-world.md:6` (`analysis/worklist.md`, `analysis/worklist-decisions.md`), `:264` ("The table of founding years and figures in `analysis/worklist-decisions.md`"), `:402` (`analysis/place-list.md`), `:902` (`analysis/party-profile.md`), `:966` (`analysis/item-profile.md`), `:829` ("see the party cover analysis", with no path at all; it is `analysis/party-cover.md`), `:291` (`tools/terrain.py`), `:1051` (`world/bench/`)
- Finding: none of these is on the site, and none is a link. A TC reader of the HTML cannot follow them. The founding data of the parties is sent to the owner's decisions file, not to the world data or the party pages on the site.
- Should be: either link each to its file on GitHub (`https://github.com/kduvekot/ubl-examples/blob/main/…`), or publish the profile tables and the place list as site pages (like `coverage.html`) and link those. Party data should point to `world.html` and the party pages.
- Related: O91 (place list), O86/O90 (party table), D11 (item table)

##### B-17 References: one is cited nowhere, many cited standards are missing, entries lack addresses
- Kind: irrelevant / stale (O84); the first point depends on Q-B-01
- Severity: medium
- Pages: note §6
- Source: `note/src/06-references.md`
- Finding:
  - **Global Test Data** (<https://sipico.github.io/global-test-data/>) is described as "safe example identifiers per country". It is a public catalogue of real-country test values: for 20 real countries, company and tax numbers, addresses, phones and bank details that pass validation but belong to no one, plus "traps to avoid". The text cites it nowhere. It dates from the first draft of 5 November (site commit 260d805c), from before the world moved to invented countries XU/XB/XL with their own schemes. Nothing in the repository uses it (`analysis/source-verification.md` does not mention it).
  - O84 asks for titles and addresses for the four added references. ISO/IEC 15459, ISO 8601, ISO 11228-1, ISO 13616 and the WTO Valuation Agreement have no URL, and ISO 8601 has no title.
  - Standards the text relies on are missing: ISO 639 / BCP 47, ISO/IEC 6523, ISO 9362, ISO 11649, ISO 6166, ISO/IEC 7812 and 7816-5, ISO/IEC 7064, ISO 10383, ITU-T E.164, UN/ECE Recommendations 20, 21 and 28, the UNTDID lists 1001, 4465, 5189, 5305, 6313, 7161 and 8339, EN 16931, Peppol BIS, eForms and ESPD, the WCO HS and UN CPC, the IMDG Code and IATA DGR, COTIF/CIM, the ATA Convention, the common transit convention of 1987, the European List of Waste, EN 15343, Directives 91/440/EEC, 2012/34/EU, (EU) 2016/2370 and (EU) 2017/1132, Incoterms 2020, PCI DSS, and the UBL 2.5 sections cited (§4.7, §7.2, IND5–IND9).
  - The UN/EDIFACT 5153 link points to d16b. Check it against the directory version in `world/codelists/sources/PROVENANCE.md`.
- Should be: every work the text names, once, with title and address. Global Test Data either removed or cited where it is relevant (Q-B-01).
- Related: O84, CLAUDE.md "Fictional values must not be mistaken for real ones"

##### B-18 The note page sits outside the site frame
- Kind: structure
- Severity: low
- Pages: note/ubl-examples-method.html
- Source: `tools/build_site.sh` (xsltproc of `note/xsl/draft-note-html.xsl`; `nav()`/`footer()` are applied only to pandoc pages)
- Finding: the note has the OASIS layout with a back link ("← UBL Example Documents"). It has no site navigation, no "Work in progress" footer and no build commit or date, so a reader cannot tell how current it is (see B-01). The page is served as ISO-8859-1 while every other page is UTF-8 (characters outside Latin-1 are written as character references, so nothing is broken).
- Should be: a short status line with the build commit and date under the back link. Optionally, UTF-8 output (`xsl:output encoding`).
- Related: B-01

##### B-19 Party positions inside a town are a diagram, and the note does not say so
- Kind: stale (O82, O92)
- Severity: low
- Pages: note §3.3
- Source: `note/src/03-world.md:400-421`; `analysis/place-list.md:11`; `site` map-sheet text in `build_site.sh`
- Finding:
  - The note says "The map is leading: a distance is the length of the route laid on the map, and every distance and time a document states comes from it … A document states the kilometres driven on its own leg, from party to party." The place list adds what the note leaves out: "a party takes a whole 3.5 km square, so the parties of a town spread over two to five times its built-up width (O92, open). Distances inside and around a town are therefore longer on the map than on the ground." A reader of the note will take in-town legs (e.g. 21 km from Selanu airport cargo to Nalevi, 17.5 km from the port to Nalevi) as true distances.
  - The note gives Lisavu as "about 1,080 km east of Lumeport" (line 275) and the printed sheet's note as "about 1,100 km" (line 420, also on map-sheet.html).
- Should be: one sentence saying that inside and around towns the map stretches distances, with O92 still open; and one figure for the island's distance, or say that 1,100 is the rounded figure printed on the sheet.
- Related: O82, O92, O152, O197

##### B-20 The figures in the note are copied by hand from the world data
- Kind: process
- Severity: medium
- Pages: note §3 (distances, populations, areas, Codana numbers, prices, bench weights, tax rates, holidays)
- Source: `note/src/03-world.md`; `tools/md2docbook.sh --check` only compares Markdown with DocBook
- Finding: the note repeats many figures that live in the world data or in generated files. Examples: 192/81/166/207/97/83 km and 1,196 km/48 h (generated in `analysis/place-list.md`); the Codana registration table (`world/parties.json`); 399/520/749/674.10/68.00 and 0.22 % (`world/items.json`); 44.1 kg, 47.0 kg and 216 kg (`world/bench/`); tax rates 4/5/6.5 % (`world/countries.json`). They are right today because each fix also updated the note by hand (e.g. O197 "overtaken decision texts"). No check catches a figure that drifts, and figures have moved often (the ore line went 154 → 180 → 159 → 166 km across D19, D45, O214 and O152).
- Should be: either generate the figure tables of §3 from the world data (as `place_list.py` does), or add a check that compares the figures the note quotes with their sources. At minimum, list the note in the commit checklist of every world change.
- Related: O112, O197, O152

#### Questions

##### Q-B-01 Is the "Global Test Data" reference still meant to be in the note?
- Context: the note cites it nowhere. It catalogues safe test values for 20 real countries. The world uses invented countries (XU/XB/XL) with their own schemes, and checks its invented values against the real registers (ISO 4217, MIC, ITU, BIC …) recorded in `analysis/source-verification.md`, which does not use this site. The reference dates from the skeleton of 5 November.
- Options:
  - A: remove it. The list then has only works the text uses. But the "real-country" alternative goes unmentioned.
  - B: keep it as related work, with a sentence in §2.2 or §3.6: "for examples set in real countries, a catalogue of safe test values exists (Global Test Data); this world avoids the question by using user-assigned country codes." This credits the alternative, but adds a non-normative pointer to a third-party site.
  - C: use it as a source for the "traps to avoid" (real values that look fictional) in `analysis/source-verification.md`, and cite it there. This strengthens the fictional-values rule, but is extra work.
- Recommendation: B. It explains a design choice a TC reader will ask about ("why not real countries with safe values?"), and it costs one sentence.
- Findings depending on it: B-17 (first point)

##### Q-B-02 Should the backstory stay in the method note?
- Context: 84 % of the note is the world chapter. A TC reader judging the method meets history, holidays and prices before the method and the checks. CLAUDE.md plans an encyclopaedia of the world.
- Options:
  - A: reorder now. Method and checks come first; the world becomes a short overview plus an annex with the full backstory. This is cheap and keeps everything in one document.
  - B: split. The note keeps only what the method needs (the countries and their differences, languages, identification, the flows), and the backstory moves to the site, later to the encyclopaedia. The note gets shorter and more relevant, but two places must be kept in step.
  - C: keep it as it is.
- Recommendation: A now, and B when the encyclopaedia exists.
- Findings depending on it: B-15, partly B-05, B-16

##### Q-B-03 Should the note describe the review process?
- Context: §1.2 promises it. The repository has a full review method (the per-example semantic review, the cross-flow review, findings grouped into causes and stages, decisions with open points, the story read against the XML). It is the main evidence that "every value has a reason" is checked by more than the build.
- Options:
  - A: add a chapter "Reviewing and maintaining the examples" in general terms (no run-ids, no tool names). This is complete and shows the method at work.
  - B: drop "reviewed and maintained" from the scope. This is shorter, but hides the strongest part of the method.
- Recommendation: A.
- Findings depending on it: B-14, B-06

##### Q-B-04 Should flows that are decided but not yet built appear in the note?
- Context: the head of §3 says "the world as decided". D47 and D48 are decided but not built, and O112 ties a flow's story in the note to its implementation.
- Options:
  - A: describe them now, marked as planned. The note is complete against the decisions, but a reader may look for examples that do not exist.
  - B: one sentence in §3.17 naming the planned flows and why they exist (coverage of temperature-controlled and radioactive air cargo, and road tanker dangerous goods); the full story when built (O112). This is honest and needs little text.
  - C: nothing until built.
- Recommendation: B, with the head paragraph saying "as built, with the decided changes noted".
- Findings depending on it: B-04, B-02

### Part C: World section (map, map sheet, party pages)

Pages covered:
- `world.html`: the visible HTML and the card and list code read in the source template `site/world.html`. Rendered headless in Chrome (overview, and with `#5-xu` selected). The embedded data checked through `tools/build_world.py`, which writes it.
- `map-sheet.html`: read fully. `map-sheet.png`: looked at whole, plus crops of the Lumeport/Euridice area, the north coast with the gas line, and the Lisavu panel.
- Party pages `world-<n>-<cc>.html`: there are **54**, not 49 (parties.json has 54). Read fully: world-5-xu, world-31-xu, world-c-xb, world-18-xu and world-23-xu (identity part). All 54 checked by script against `world/parties.json` and `world_data.load()`: h1 = identity name, what/how, registry/tax/endpoint, counts of sent, received and named-in documents, and that every example link resolves (all clean). The script also listed which master-data fields a page leaves out, and scanned every page for decision references.
- Generators: `tools/build_world.py` (party pages), `site/world.html` (map template, card, list, foot), `tools/build_site.sh` (map-sheet text), `analysis/world-position/refine_map.py` (sheet drawing).
- Not checked: the MO001–MO010 drawing details tile by tile (terrain corners, trees, curves, building directions). They are rendering outcomes with no text on the page. At overview zoom the screenshot shows no contradiction.

#### Findings

##### C-01 What the customs services do is wrong on their pages, map cards and party list
- Kind: wrong
- Severity: medium
- Pages: world-19-xu, world-19-xb, world-19-xl (and their cards on world.html) (3)
- Source: `world/parties.json` "what" at lines 985, 1091, 2596
- Finding:
  - Urvania: "Export customs at the land border crossing." It also receives three import declarations (wood/07, energy/05, energy/10), and the energy imports come by pipeline, not through a border crossing.
  - Bayvarra: "Import customs at the land border crossing and at the seaport." It also receives export declarations (sea/11, wood/05, energy/04).
  - Lisavu: "Import customs on the island." It also receives the ginnery's export declaration (cotton/11) and the manifest (sea/15).
- Should be: each customs service described as its country's customs authority, for imports, exports and transit, at the border crossing, the port and the airport (and the pipeline entry for Urvania). This is what world/documents.json already shows.
- Related: D18 (customs between the three countries), D44

##### C-02 The map's opening card misdescribes the world
- Kind: wrong / stale
- Severity: medium (it is the first text a visitor reads in the World section)
- Pages: world.html (no party selected)
- Source: `site/world.html` `showCard(null)`, lines 1600–1602
- Finding:
  - "Three countries, 54 places, one story": the 54 are parties, not places. Since O152 the world has a place list of about 600 towns and villages (analysis/place-list.md), so "places" now means something else.
  - "Ore is mined and processed in Urvania, crosses the land border by road, rail and river to the distributor in Bayvarra …": this tells only the bench chain. The ore flow is domestic, and what crosses by river is recycled granulate going to Rivermouth, not ore or benches. Cotton, energy, utilities, the tender and the contest are not mentioned.
  - "Every country has its own customs, chamber and banks": Bayvarra has no chamber of commerce. The chambers are 20-xu and 20-xl only; Bayvarra's business registry is kept by the Bayvarra Information Service (21-xb).
- Should be: "54 parties", a summary that covers all 18 flows (or a pointer to them), and no claim of a Bayvarran chamber.
- Related: O152 (place list), O91

##### C-03 Decision and open-point numbers leak into reader texts
- Kind: irrelevant
- Severity: medium
- Pages: 43 of 54 party pages: world-1-xl, 10-xb, 11-xb, 13-xu, 14-xu, 15-xu, 16-xb, 16-xl, 18-xu, 19-xb, 19-xl, 19-xu, 2-xb, 20-xu, 21-xb, 22-xl, 23-xu, 24-xb, 25-xb, 26-xb, 27-xb, 28-xb, 29-xb, 3-xl, 30-xl, 32-xb, 33-xu, 34-xb, 36-xb, 37-xb, 38-xl, 4-xu, 41-xb, 42-xb, 46-xu, 47-xu, 48-xb, 5-xu, 6-xb, 7-xu, 8-xu, 9-xl, c-xb. About 140 distinct occurrences. The same texts show in the map cards (`what`) and probably in the example `.md` pages (group of the examples).
- Source:
  - flow texts in `world/documents.json` (ore "(decision D45)", rail "(decision D37)", plastics "(decision D41)", sea "(Incoterms 2020; D30, O105)", waste "(decision D42)", wood "(decision D43)");
  - document "why" texts (48 occurrences in documents.json);
  - `parties.json` "what" and `account_abroad.why` (11 occurrences);
  - `items.json` descriptions (35);
  - `countries.json` (22).
- Finding: quotes from the pages:
  - "… a debit note to its freight invoice under the framework contract: the world's real debit note (D37, D9)" (world-14-xu);
  - "… its currency risk covered by its forward contract (O226, O50)" (world-5-xu, Account abroad);
  - "the tracks and the train paths are the rail infrastructure manager's (decision D37)" (world-18-xu, the party description itself).

  A reader of the site has no access to analysis/worklist-decisions.md, and phrases such as "the world's real debit note" talk about the project, not about the world.
- Should be: world texts tell the world. The traceability to D and O numbers belongs in the repository (decisions file, commit messages, a separate `source` key), not in strings the site prints. CLAUDE.md, "Rules agreed": a value has a business reason in the world.
- Related: O112 (story and XML read against each other, flow by flow): the natural moment to clean each flow's texts. See Q-C-04.

##### C-04 Country notes contradict the current map: "Urvania: Mainland, inland"
- Kind: stale (O152, "Land, history and settlement")
- Severity: medium
- Pages: all 54 party pages, in the "In the world" line ("Urvania: Mainland, inland. Raw materials and manufacturing." on the 15 Urvanian pages; "Lisavu: Island. The overseas buyer, reached by sea and air." on the 11 Lisavan pages)
- Source: `world/countries.json` `countries.<c>.note` (line 6 for XU), printed by `tools/build_world.py` line 247
- Finding:
  - Since O152 the mainland is generated from terrain, and Urvania has coasts: Porto Riparo "at the head of a long inlet on the north-west coast, the most sheltered anchorage of Urvania's coast" (world/map.json, analysis/place-list.md), Duefiumi and Lanternino on the west and south coasts. The map sheet shows this.
  - "Inland" comes from D19 ("Urvania in the west, inland"), which the O152 story line replaces "where they differ". The D4 founding table's "Landlocked Urvania always shipped bulk down the river" (Fiumella Barges) has the same problem.
  - Lisavu is no longer only "the overseas buyer": it exports cotton (the cotton flow).
- Should be: notes that agree with the place list: Urvania mostly inland, with a short coast and Porto Riparo; Lisavu as buyer and cotton exporter. See Q-C-05.
- Related: O152, D19, D4 (founding table), O35

##### C-05 "Proposed addition to the 26+C set", "new" and "Parties 27 and up …" are leftovers and contradict the data
- Kind: irrelevant / wrong
- Severity: medium
- Pages:
  - 19 party pages say "proposed addition to the 26+C set": world-27-xb, 28-xb, 29-xb, 30-xl, 31-xu, 32-xb, 33-xu … 44-xu, 48-xb.
  - world.html: the card heading says "PARTY #n · … · PROPOSED"; the party list shows a "new" badge; the foot says "Parties 27 and up are proposed additions to the 26+C set."
- Source:
  - `tools/build_world.py` line 234;
  - `site/world.html` line 124 (foot), line 141 (comment "27-32 proposed"), lines 1604 and 1615;
  - `parties.json` `proposed` flags.
- Finding:
  - "26+C set" refers to `analysis/session-decisions.md` on another branch (sample-research, per tools/party_cover.py). No reader can know what it is.
  - The foot contradicts the flags: #45 (Department of Agriculture of Lisavu), #46 and #47 are numbered above 27 but are not marked proposed.
  - Since D28–D48 all these parties are fully part of the world, with documents and examples. Nothing about them is "proposed" any more.
- Should be: drop the "proposed/new" notion from the pages, or replace it with something a reader can use, such as the flows a party takes part in. See Q-C-02.
- Related: D28–D48, CLAUDE.md "the parties"

##### C-06 A party page is not the party's full self-description, so O86 cannot be read against it; the founding dates and identification conventions are missing
- Kind: stale (O86, D4, D5, O22) / structure
- Severity: medium
- Pages: all 54 party pages
- Source: `tools/build_world.py` `identity()` (line 133). It prints only name, registry, tax number, address, endpoint, one contact, accounts, BIC and the country's currency and tax.
- Finding: these fields from `parties.json` never appear on a page, by script check:
  - `legal.founded`, headcount, legal form, share capital, listing (the founding table of D4 is implemented in the data: Bank of Lumeport 1903, Valdara 1962-04-12, Tidewell 1974, Kelpstone 2011 …);
  - `customs_id` (the customs trader number, a stated rule of D18 and D5);
  - `identification.convention` with the Codana number and its registration date, or the GS1 company prefix. These show only indirectly, inside the item rows of a party that sells items. Castrano, Montebrio and Ferrano Grid are Codana parties (O22) and their pages show no Codana number at all.
  - industry class (D8), website, language (D1/O86), departments and desks.

  O86 makes each party "the authority on its own data": what a document says about it may be less and must never contradict it. The page is the natural place to show that full "about yourself" record, which a reader can compare with what each document says (`analysis/party-profile.md`). Today the page shows less than several documents do.
- Should be: an identity section with the full master data relevant to documents: legal entity and founding, register, tax and customs numbers, the identification convention and its numbers, industry class, language, website. A short history line could come from the founding table of D4.
- Related: O86, O88 (party table, applied), D4, D5, O22, D8, D1; Open work 2 (encyclopaedia: company histories)

##### C-07 Fleets are not on the party pages, and the vehicles on the map are not explained
- Kind: structure
- Severity: low
- Pages: 13 party pages with a fleet in parties.json: 8-xu, 14-xu, 13-xu, 15-xu, 26-xb, 10-xb, 11-xb, 12-xl, 9-xl, 36-xb, 37-xb, 38-xl, 42-xb. Also world.html.
- Source: `tools/build_world.py` (no fleet section); `site/world.html` (vehicles drawn from the legs, no text)
- Finding:
  - The ship *Tidewell Harbour*, the ATR 72-600F freighter, the barge *Fiumella IV*, the trains FRC 4417/2208, the trucks with their plates, and the pipeline as "transport means" are all world data that the documents cite (TransportMeans, vessel IDs, plates). No page shows them.
  - The map draws trucks, trains, barges, a ship and a plane moving along the legs, but no text says what they are or which flow or document they belong to. CLAUDE.md: "vehicles are derived from the legs".
- Should be: a "Fleet" section on the operator's page (name, type, identifiers, which legs it runs), and a caption or legend on the map for the moving vehicles.
- Related: O82/O152 (map), D19

##### C-08 Codana's page contradicts the identification story and is mostly empty
- Kind: wrong (D5) / structure
- Severity: medium
- Pages: world-31-xu (and its map card)
- Source:
  - `parties.json` line 1050, "what";
  - `tools/build_world.py` lines 237–241, which print the template even when the party has no documents.
- Finding:
  - "Issues item and property identifiers used across the world (a fictional numbering organisation)." D5's rule book says "Codana does not hand out item numbers. It gives a company its number; the company numbers its own items, lots, pallets and places." The page does not say:
    - founded 1999;
    - ISO/IEC 15459 agency code `KXU`;
    - the ISO/IEC 6523 register `0990`;
    - which companies are registered with it (Valdara 10014, Montebrio 10087, Serravona 10252, Castrano 10519, Rinova 13362, Rivermouth 15128, Ferrano Grid 16043, Kelpstone 19676; O22).
  - The page then says "In this world it sends 0 and receives 0 documents, and is named in 0 documents between other parties. They are listed per flow below." No flows follow. "The party elements in which this party appears:" is followed by nothing.
  - The same template sentence ("They are listed per flow below") appears on the four other pages with 0 sent and 0 received: 22-xl, 23-xu, 28-xb, 29-xb. They do have named-in lists.
- Should be: Codana described as D5 tells it, with a list of its registered companies (derived from `identification.codana_cin`). The template should leave out empty sections and use a sentence that fits zero counts. Codana is a party with no document of its own: say so ("named in identifiers as agency KXU …").
- Related: D5, O22; story line "Identification, the GS1 way and the Codana way"

##### C-09 Party descriptions and role labels still tell the original bench chain only
- Kind: wrong / stale
- Severity: medium
- Pages: the cards and list on world.html, and these party pages:
  - world-6-xb: "Buys finished goods from #5, stocks them … and sells to #26 and overseas to #1." Internal party numbers appear in prose, not linked.
  - world-34-xb: "Supplies drinking water in Coastal State, to shops and households." The company also runs Lumeport's district heating and bills it (world/items.json "District heating"; note 03-world §money; D31; D48).
  - world-c-xb: "A private person buying in the shop; receives a purchase receipt." The page lists seven documents, including the web order he sends (retail/22) and the water company's utility statement, invoice, reminder and credit note (utilities/08–11).
  - world-23-xu: "Holds the manufacturer's account and receives the payments from abroad." The same page says it "Holds the accounts of" ten parties. Valdara's payments from Bayvarra go to its lume account at Bank of Lumeport (O226).
  - world-22-xl: "Holds the buyer's account and sends the payment abroad."
  - world-16-xb "Port of loading", world-16-xl "Port of discharge on the island". In the cotton flow the roles are reversed: Selanu loads and Lumeport discharges (cotton/14).
  - world-4-xu "Mines the ore at the start of the chain …": nothing about the underground mine on the massif at 721 m (O152 story line) or the 1958 founding.
  - Party list and card headings: role names of the 26+C set, relative to one chain: "#1 Commercial Buyer", "#23 Seller's Bank", "#22 Buyer's Bank", "#6 Distributor". A reader meets "Seller's Bank" for a bank that serves ten parties.
- Source: `parties.json` `what` and `name` (lines 848, 1147, 1453, 2888, 3183 …); `site/world.html` lines 1604, 1615.
- Should be: descriptions that cover every flow the party is in (the data already lists them), with no `#n` references. The list should show the company name, or a role that is not relative to one chain ("Bank, Ferrano" rather than "Seller's Bank").
- Related: D31, D23, D48, O86 (each party is the authority on its own data), O112

##### C-10 The interactive map has no legend or scale, and does not say the island is drawn nearer
- Kind: structure / stale (O82, O152, D19)
- Severity: medium
- Pages: world.html
- Source: `site/world.html`: the toolbar, the hint (line 119) and the foot (line 124). The canvas text is limited to signs, country names and town names (lines 1481, 1543, 1569).
- Finding:
  - Without a key a reader cannot tell apart: roads, railways, the gas pipelines (yellow dotted lines from #42 to #43 and Ferrano), the border (red dotted), the sea route (white dashes) and the air route (white dots); the moving vehicles; the building kinds; the five layer colours (the card tag says "commerce" while the layer button says "Supply chains").
  - "Grid: Show the tile grid" does not say a square is 3.5 km (O152). There is no scale.
  - Lisavu is drawn a few hundred kilometres off the coast, in the same frame. On the sheet and in note §3.3 it lies "about 1,100 km east of Lumeport" and "the island is drawn nearer than it lies". The interactive map gives no such note. D19 promised "on the map of the site the island stands in an inset".
  - Towns and villages cannot be clicked. Only parties can.
- Should be: a collapsible legend (route modes, border, pipeline, vehicles, layer colours, scale bar of 3.5 km per square), and a note on the island ("drawn nearer; about 1,100 km east, 48 h by sea, 2 h 45 by air"), as the sheet has.
- Related: O82 (map is a diagram; the parties' buildings are symbolic, MO004), O152, D19, O91 (closed)

##### C-11 Map sheet: labels sit away from their symbols, labels overlap, there is no legend, and the offshore line has no platform
- Kind: wrong / structure
- Severity: medium
- Pages: map-sheet.png (shown on map-sheet.html)
- Source: `analysis/world-position/refine_map.py` (label placement, `sheet` mode); the text on `tools/build_site.sh` lines 98–109
- Finding (from crops of the 4,961 × 3,508 sheet):
  - Lisavu panel: "Port of Selanu" stands on the south coast under Linukaha, about 19 mm (about 45 km at 1 : 2,500,000) from the port symbol (blue dot), which is at Selanu on the east coast. "Selanu Airport" is set up and to the left of its symbol, across the hills and over a village dot, so it reads as that village's name. A reader would place the port, and probably the airport, wrongly. This goes against the O82 rule that the drawing "must be true in everything else".
  - Mainland: "Euridice Crossing" overprints "Tallowford" and a stray mark ("\Euridice"). "Fontebrina" and "Salicora" touch.
  - There is no legend. The border (purple dotted) and the gas pipelines (lilac dotted) look alike. The subsea line from Gullhaven ends in open sea with no platform symbol or name, although the text promises "pipelines" and the note names "the subsea line from the platform about 83 km".
  - The sheet shows no parties except the ports and airports. Fine for a topographic sheet, but the page does not say so.
- Should be: labels anchored next to their symbols, no overprinting, a legend (roads, railways, pipelines, border, sea and air routes, symbols), and the platform marked.
- Related: O82, O92, O152, MO001–MO003 (coast drawing, sheet unaffected), O151

##### C-12 Navigation: no way back from examples to parties or map, no link to the world's story, no country or Accord pages
- Kind: structure
- Severity: medium
- Pages:
  - all 262 example pages (no link to any party page or to the map, except the "World" nav item);
  - world.html and all 54 party pages (no link to note §3 "The UBL example world");
  - the map card link "How UBL helps <name> →".
- Source: the example page generator (other group); `tools/build_world.py` lines 245–252 ("In the world" only links to `world.html#id`); `site/world.html` line 1607.
- Finding:
  - The path map → party → example works ("See the example document" on each entry, all links resolve). An example page cannot lead back to its sender's or receiver's page, to its flow, or to the map.
  - The countries, their history, the Trade Accord, the languages and the two identification systems are told in note §3.1–3.7 (anchors `S-03-world-*`). The World section never links there.
  - Each party page ends with only "Lisavu: Island. The overseas buyer …", and there is no page per country, town or flow.
  - The card's link text "How UBL helps Valdara Industries →" undersells a page that holds identity, items, all documents per flow and partners.
- Should be:
  - example pages link their parties to `world-<id>.html` and their flow to its section;
  - party pages link the country to note §3.1 and the identification system to §3.7;
  - the card link reads e.g. "Valdara Industries: identity, items and documents →".

  Country, town and Accord pages are the encyclopaedia (CLAUDE.md Open work 2; place list as its skeleton, O82/O152). Until then, at least the note chapter should be linked.
- Related: Open work 2, O82, O152, O35

##### C-13 The page IDs world-N-cc mean nothing to a reader and repeat across countries
- Kind: structure
- Severity: low
- Pages: all 54 party pages (URLs, map hashes `world.html#5-xu`, page meta "#5 Manufacturer")
- Source: `parties.json` `id` and `n`; `tools/build_world.py` `link()` and the file name; `site/world.html` list (`#${p.n}`)
- Finding:
  - The number comes from the 26+C role set (see C-05). #16 is both Port of Lumeport and Port of Selanu, and #19 is three customs services; "C" is the consumer.
  - The number is shown as "#5" in the page meta, on map signs and in the list, as if it were an identifier of the world. It is not used in any document.
  - The URL tells nothing (world-41-xb = Rivermouth Packaging).
- Should be: see Q-C-01 (recommended: readable slugs such as `world-valdara-industries.html` with redirects or kept aliases; the number kept only as an internal key).
- Related: C-05

##### C-14 Template wording that misleads
- Kind: irrelevant
- Severity: low
- Pages: all 54 party pages
- Source: `tools/build_world.py` lines 237–252
- Finding:
  - The footnote "Every place named in a document is checked against the UBL 2.5 structure" means party element paths. Since O152 "place" means a town or village (the place list).
  - "Completed by the party role table of the UBL specification where the model does not say it" sits on every page as method text. It belongs once in the method note (§3.20 "Who sends and who receives").
- Should be: "every party element named …"; the method sentence moved to the note and linked.
- Related: O152

##### C-15 Two items under one heading and one seller's ID
- Kind: structure
- Severity: low
- Pages: world-5-xu ("What it sells")
- Source: `tools/build_world.py` `sells()`, line 116 (heading = item name); `world/items.json` (the standard bench and the RAL 6005 special colour share name "Park bench Serra 180", `VI-B180`, `KXU10014B180`)
- Finding: two identical "### Park bench Serra 180" sections with the same seller's item ID, standard item number and price. Only the description tells them apart ("in moss green (RAL 6005), a special colour"). A reader takes it for a duplicate. If the variant is a real item of its own, it would normally carry its own identification or a property.
- Should be: a heading that tells the variant ("… special colour RAL 6005"). Whether the variant needs its own ID is an item-data question for the examples' review (D7/D11 "packs, kits and offers").
- Related: D7, D11, D20 (bench data on the page agrees with the implemented C69: 44.1/47.0 kg)

##### C-16 Process: hand-written texts in the map template and generator do not follow the data
- Kind: process
- Severity: low
- Pages: world.html, all party pages
- Source: `site/world.html` lines 124, 141, 1600–1602; `tools/build_world.py` line 234; `tools/build_site.sh` lines 98–109
- Finding:
  - The opening card, the foot, the "26+C" and "27–32 proposed" comments and the meta suffix are literal strings. They drifted from the data (C-02, C-05) without any check noticing.
  - The new parties of D47 (wholesaler, Selanu General Hospital), D48 (road-tanker haulier) and O137 (fruit cooperative, Bayvarra's plant protection organisation, the new island buyer) will get pages automatically once they are in parties.json, but will need map tiles. The opening card will stay wrong unless it is derived from the data.
- Should be: derive counts and summaries from the data (number of parties, flows, the list of flows), and put the map-sheet text with the sheet's own facts (scale, island distance) next to the generator that draws them.
- Related: D47, D48, O137, O138

#### Questions

##### Q-C-01 Should the party pages get readable names instead of world-<n>-<cc>?
- Context: the numbers come from a role set that readers never see, repeat across countries (#16, #19), and are shown as "#n" everywhere (C-13). The example pages do not link to party pages yet, so only examples.html, the map hashes and the party pages themselves link to these URLs.
- Options:
  - A. Slugs from the company name (`world-valdara-industries.html`), with the old file names kept as redirect stubs. Readable and stable while names are stable, but a rename (D3-like) changes the URL.
  - B. Keep the IDs and stop showing "#n" to readers. Least work, URLs stay opaque.
  - C. Slugs from place and role (`world-ferrano-manufacturer`). Readable, but fragile when roles widen.
- Recommendation: A, done when the encyclopaedia pages come (Open work 2), so that towns and parties share one naming scheme. Until then B, with "#n" removed from page meta and list.
- Findings depending on it: C-13, C-05

##### Q-C-02 Drop the "proposed / new" marking of parties?
- Context: all decisions D1–D48 are taken; the flagged parties all have documents. The flag is inconsistent (#45–#47 unflagged) and points to a set on another branch (C-05).
- Options:
  - A. Remove the flag and the "26+C" text everywhere. Simple, and true now.
  - B. Keep the flag internally (party_cover.py) and show nothing on the site.
  - C. Replace it with "added with flow X / decision" history. Interesting for the encyclopaedia, but needs decision references, which C-03 asks to keep out.
- Recommendation: A for the site (B for the analysis script if still needed).
- Findings depending on it: C-05

##### Q-C-03 How much of a party's master data should its page show?
- Context: O86 makes the party the authority on its own data. The page shows only part of it (C-06). parties.json also holds an employee's national ID, birth date and passport, and staff mobile numbers, all fictional, used in documents.
- Options:
  - A. Show everything a document can say about the party "about itself" (the O88 table's left column), including the legal entity, founding, customs number, identification, industry, language, website and desks. Leave out persons' personal data (employee birth date, national ID, passport), which a company register would not publish.
  - B. Show everything in parties.json. Complete, but it publishes person-level data as if it were company master data.
  - C. Keep it as it is.
- Recommendation: A, because it is the reference that O86 and the "never contradicts" build check rest on, and it begins the company histories of the encyclopaedia.
- Findings depending on it: C-06, C-07

##### Q-C-04 Where should the traceability to D/O numbers live, if not in the world texts?
- Context: the flow, document, party and item texts carry "(decision D37)", "(D30, O105)", "(O226, O50)". The site prints them on 43 party pages and in the map cards (C-03).
- Options:
  - A. Strip them from the world texts and keep the reference in a separate key (for example `"source": "D37"`) that the generators do not print. Clean pages, and traceability is kept.
  - B. Keep them in the data and have the generators strip parenthesised references when printing. No data change, but fragile and hidden.
  - C. Keep them visible and add a legend that links to the decisions file. Transparent, but the decisions file is a working file, not a publication.
- Recommendation: A, done flow by flow with O112.
- Findings depending on it: C-03

##### Q-C-05 Does Urvania count as an inland country now that the generated map gives it a coast?
- Context: D19 says "Urvania in the west, inland", and the D4 table says "Landlocked Urvania always shipped bulk down the river". The O152 terrain (leading) gives Urvania coasts on the north-west, west and south, with Porto Riparo as "the most sheltered anchorage of Urvania's coast" (C-04).
- Options:
  - A. Urvania has a coast but no deep-water port, so its trade still goes down the river and through Lumeport. The note becomes "Mainland, west; a rugged coast without a deep-water port; raw materials and manufacturing". This keeps Fiumella's reason, reworded.
  - B. Urvania is inland, and the map is changed so that the coast belongs to Bayvarra. This contradicts O152 and the place list.
- Recommendation: A, because the map is leading (O152), and it keeps the river trade, the land border and Lumeport's role.
- Findings depending on it: C-04

### Part D: the specifications section (world-specifications.html and 90 world-spec-*.html)

Pages covered:
- `world-specifications.html`: read fully.
- 2 national, 4 community and 14 profile pages: read fully.
- 70 transaction pages: checked by script. For each page, the examples it lists were compared with the root-level `CustomizationID`/`ProfileID` of all 262 XML files in `world/examples/`. For each transaction, the roles it claims were compared with sender and receiver in `world/documents.json` (via `world_data.load()`). Document-type coverage was compared both ways.
- 6 transaction pages were also read fully: billing, self-billing, order, invoice-response, transport-progress-status, transportation-status.

Source of all pages: `tools/build_world.py` lines 275-331 (the index and page loop, `spec_page()`), `tools/world_specs.py` (`national()`, `community()`, `profile()`), and the texts in `world/specifications.json`.

Mechanical results:
- Every document type in the examples is carried by exactly one transaction and one profile.
- Every transaction and profile document type has at least one example.
- Apart from D-06, the example list on each page matches the XML.
- The transaction pages state no business rules, code lists or identifier schemes at all (see D-07).

#### Findings

##### D-01 Billing transaction says the customer issues the debit note
- Kind: wrong (today) and stale (D9)
- Severity: medium
- Pages: world-spec-transaction-billing.html, plus its row on world-specifications.html (2)
- Source: `world/specifications.json` transactions.billing.purpose
- Finding: The page says "The supplier bills the customer, corrects a bill with a credit note, and the customer claims a debit with a debit note."
  - D9 decided that in this world a debit note is the supplier's addition to an invoice it issued.
  - The buyer's debit notes were removed: furniture/14, sea/28 and tender/34 (D38 list).
  - The only debit notes on the site are rail/12 (carrier to Valdara) and rail/13 (Valdara to Lumeway), both issued by the supplier. So the page contradicts its own examples.
- Should be: "…the supplier corrects a bill with a credit note, or adds to it with a debit note when more became due afterwards" (D9).
- Related: D9, D38, C66

##### D-02 An Urvanian seller's invoice to a Bayvarran public body claims only Bayvarra's rules, and the page says these override the seller's tax
- Kind: wrong (today) and stale (D17)
- Severity: high
- Pages: world-spec-national-XB-public-billing.html and world-spec-national-XU-invoice.html (2). The chain affects the examples tender/32-Invoice, tender/33-CreditNote and tender/39-Invoice.
- Source:
  - `tools/world_specs.py` `national()` returns the first matching national specification only. XB:public-billing comes first in the JSON, so an Urvanian seller to a Bayvarran public body never gets XU:invoice.
  - `world/specifications.json` national."XB:public-billing".purpose.
- Finding: The XB page says "Bayvarra's rules for invoices to its public bodies: the exemption from the state sales tax, the withholding … A public body's own rules come first: an invoice to it follows them whatever the seller's country".
  - D17.2 decided "A seller states its own country's tax": Valdara invoices the department with Urvania's treatment (export, a service supplied abroad), not with Bayvarra's `PUBLIC` exemption.
  - Valdara's three documents carry `trns:billing#compliant#XB:public-billing` and lack `XU:invoice`, although they apply Urvania's VAT. The XU page therefore misses them from its list too.
- Should be:
  - The XB specification should cover only what Bayvarra imposes on invoices to its public bodies: the public body's 10 % withholding from a non-established business (`INCOME` scheme) and the tax representative. The `PUBLIC` exemption should apply only to Bayvarran sellers.
  - An Urvanian seller's invoice should claim both national levels (see Q-D-02).
- Related: D17 (O47), C54, conditions#F4/#F8

##### D-03 Urvania's national invoice specification makes payment terms national rules
- Kind: stale (D22, D23)
- Severity: medium
- Pages: world-spec-national-XU-invoice.html (1)
- Source: `world/specifications.json` national."XU:invoice".purpose
- Finding: The page lists as Urvania's invoice rules "the 2 % cash discount for payment within ten days, statutory interest on late payment".
  - D22 makes these layer 2 (the seller's standard terms `XU-STD`) and layer 3 (statutory interest, only where the contract and the terms are silent). A contract's terms win.
  - D23 gives utility bills the Accord's own 21-day term with no discount.
  - Several examples that claim this specification fall under exactly these exceptions:
    - framework agreements, "30 days net", no discount: ore/06, rail/10 and plastics/07;
    - a utility bill: utilities/02;
    - energy market invoices: energy/02 and energy/03.
- Should be: VAT content only (the seller's VAT number, category and rate per line, the bilingual notes). The standard terms and statutory interest belong to the country's practice (`countries.json`), not to the invoice specification. Otherwise the page should say "unless a contract or the Accord's utility terms say otherwise".
- Related: D22, D23, O70, O148, C51, C55

##### D-04 The community specifications apply by flow, not by membership, so documents of non-members claim them
- Kind: wrong (today)
- Severity: medium
- Pages: world-spec-community-port-lumeport.html and world-spec-community-procurement.html (2)
- Source:
  - `tools/world_specs.py` `community()`, branch `flow_and_documents`;
  - `world/specifications.json` communities."port-lumeport" and communities.procurement (members, flows, purpose);
  - `tools/build_world.py` line 318 (the "Members:" sentence).
- Finding: The port page says that "The port, its customs, the shipping lines and the forwarders of Lumeport exchange … the declarations the port's customs office needs before the ship arrives". It lists four members. But every document of the listed types in the flows sea and cotton claims it, including documents on the island:
  - cotton/11 ExportCustomsDeclaration, Selanu Cotton Ginnery to the Island Customs Service (19-xl);
  - sea/19 ImportCustomsDeclaration, a Lisavan broker to the Island Customs Service;
  - cotton/12 WeightStatement, ginnery to carrier.

  Neither party of the two declarations is a member, and neither declaration is lodged in Lumeport.

  The procurement page names only two members (the Public Works Department and the Procurement Review Board). Its text speaks of "the economic operators that take part", and all its examples are between the department and operators or the Government Information Service, none of them members. The "Members:" line therefore misleads on both pages.
- Should be:
  - Port community: claimed only by documents whose sender and receiver are members, or which pass through Lumeport. The Island Customs Service documents should claim no port-community specification, or a Selanu port community if one is wanted.
  - Procurement: the page should say that it applies to every party of a Bayvarran procedure, and drop the "Members" wording.
- Related: none recorded. This is not in the worklist (see D-11).

##### D-05 Roles in the transaction texts do not match the examples
- Kind: wrong (today)
- Severity: low
- Pages: world-spec-transaction-transport-progress-status.html and world-spec-transaction-transportation-status.html (2), plus their index rows
- Source: `world/specifications.json` transactions."transport-progress-status".purpose and transactions."transportation-status".purpose
- Finding:
  - Transport progress status says "A party asks for the progress of a transport, and the carrier answers." In rail/04-05 the carrier (Ferrano Rail Cargo) asks and the rail infrastructure manager answers.
  - Transportation status says "A party asks for, or the carrier reports, the status of a consignment." Of its 7 status reports, none comes from a carrier: they come from the seaports (sea/13, 17), the airports (air/05, 09), the rail hub (rail/07), the forwarder (retail/15) and the road carrier (road/09). Only road/09 fits.
- Should be: roles that match UBL's definitions and the examples, for example "the infrastructure manager answers" and "a party in the transport chain reports". Better still, generate the roles from the examples (D-07).
- Related: rail and sea flow decisions (D37, D30)

##### D-06 "Examples that claim it" lists the digital agreement and capability, which only name the specification
- Kind: wrong (today)
- Severity: medium
- Pages (6):
  - world-spec-transaction-billing.html: 46 listed, 43 claim it;
  - world-spec-transaction-order.html: 21 listed, 18 claim it;
  - world-spec-transaction-order-response.html: 8 listed, 5 claim it;
  - world-spec-transaction-invoice-status.html: 5 listed, 2 claim it;
  - world-spec-profile-billing.html: 56 listed, 54 claim it;
  - world-spec-profile-ordering.html: 30 listed, 28 claim it.
- Source: `tools/build_world.py` line 283, `etree.parse(path).getroot().iter("{*}CustomizationID", "{*}ProfileID")`. It collects every descendant, including the `DigitalProcess`, `SendingDigitalService` and `ReceivingDigitalService` IDs inside sea/03-DigitalAgreement and sea/04-DigitalCapability.
- Finding: On four transaction pages "sea 03-DigitalAgreement" appears twice, and sea/04-DigitalCapability appears too. These documents claim `trns:digital-agreement` and `trns:digital-capability`; they do not claim billing or ordering.
- Should be: list only the root-level children under "Examples that claim it". Put a second list "Agreed in" or "Named in" for the agreements and capabilities that name the specification, which is useful in itself, since it shows the specification in use.
- Related: none

##### D-07 The transaction pages define nothing: no roles, no rules, no code lists, no identifiers
- Kind: irrelevant and structure
- Severity: medium
- Pages: all 70 transaction pages. 54 of them are only boilerplate. Also the 14 profile pages.
- Source: `world/specifications.json` transactions.*.purpose; `tools/build_world.py` lines 309-328 (the page has only name, identifier, purpose, owner and version, document types, examples)
- Finding:
  - 54 purposes read only "One document type carries the transaction, the X, which UBL 2.5 defines as follows: '…'". That is the UBL definition, not a specification.
  - No page states the roles. `analysis/codelist-decisions.md` defines a transaction as "between two roles, with a defined purpose, information content and rules".
  - No page states rules, code lists (listIDs) or identifier schemes.
  - `codelist-decisions.md` says "The world's code-list rules can be tied to the specification a document claims", and none are.

  A reader cannot tell what a document that claims a specification has promised. This also leaves the decided world rules without a visible home. Examples that would naturally belong there:
  - self-billing only as SelfBilledInvoice (P-SB);
  - the debit note meaning (D9);
  - `ProfileExecutionID` per collaboration (D26);
  - the utility terms (D23).
- Should be: a short section per transaction, generated from the examples where possible:
  - the sender and receiver roles seen;
  - the code lists and identifier schemes used;
  - the decided rules that apply, by reference to the decision.

  See Q-D-01.
- Related: codelist-decisions "Document identification"; D26/O77; P-SB

##### D-08 How the world's specifications relate to the real ones is not explained
- Kind: irrelevant (missing context)
- Severity: medium
- Pages: world-specifications.html, world-spec-transaction-self-billing.html, world-spec-transaction-billing.html and the national pages (5)
- Source: `tools/build_world.py` lines 294-298 (index intro); `world/specifications.json` purposes
- Finding: The index says only that the chain works "as EN 16931, Peppol and XRechnung do" and that "the world claims no compliance with real ones such as EN 16931". What is missing:
  - The analogy is not given: Accord transaction is like EN 16931 / Peppol BIS; national is like a CIUS such as XRechnung; community is like a partner-group CIUS; `ProfileID` is like the Peppol process identifier. The URN prefix `urn:ubl-examples:` is not marked as an invented, unregistered namespace.
  - The self-billing page does not say that EN 16931/Peppol send self-billing as Invoice + 389 and that the world deliberately does not (P-SB; codelist-decisions line 194, the three EN 16931 bindings in conflict with UBL 2.5 semantics; CLAUDE.md Open work item 3).
  - The billing page is silent on the tax point date and `ItemClassificationCode` differences.

  This is the one place on the site where a reader from the EN 16931/Peppol world meets the world's specifications, and the project's main argument (semantic conformance over established practice) is missing here.
- Should be:
  - one paragraph on the index with the mapping, and "fictional, not registered";
  - on billing and self-billing, a "Differs from EN 16931/Peppol" note linking to the findings in codelist-decisions (or to their future write-up).
- Related: codelist-decisions P-SB and the EN 16931 section; Open work item 3

##### D-09 The specification pages are hard to reach and examples do not link to them
- Kind: structure
- Severity: medium
- Pages: all 91; the 262 example pages; party pages of community members
- Source:
  - `tools/build_world.py` line 262 (the only link, a sentence on examples.html);
  - `tools/build_examples.py` lines 3619-3621 (the reason for `CustomizationID` says "Each has a public description on the world's pages (world/specifications.json)" without a link);
  - `tools/build_world.py` party page (no community membership).
- Finding:
  - The index is linked only from one sentence on examples.html. It is not in the menu and not linked from world.html.
  - None of the 262 example pages links to the specification it claims. The reason text points the reader to a JSON file in the repository instead.
  - The party pages of the 13 community members do not mention their community.
- Should be:
  - each example's `CustomizationID`/`ProfileID` reason should link each URN to its page (`spec_page()`);
  - the party pages should name the communities;
  - world.html should link to the index.
- Related: none

##### D-10 Presentation: frozen title case, quoted UBL flaws, ordering
- Kind: structure
- Severity: low
- Pages: about 40 transaction pages, and the index
- Source: `world/specifications.json` (the purposes are stored text, made with an older form of `world_docs.words()`); `tools/build_world.py` lines 300-306
- Finding:
  - Title case inside sentences: "the Bill Of Lading", "the Certificate Of Origin", "the Call For Tenders", "the Instruction For Returns". The current `words()` lowercases " Of ", but the JSON text was never regenerated.
  - UBL's own flaws are quoted with no mark: Waybill "describing a shipment It is issued…"; TransitCustomsDeclaration "describes an import customs declaration".
  - The transactions table follows JSON order (the multi-document transactions, then the single ones alphabetically) without saying so.
  - Community pages show no owner or version, although `owner.community` exists in the JSON.
- Should be:
  - generate the boilerplate at build time from the model, not store it;
  - mark verbatim UBL text with [sic] where it is wrong;
  - sort the table alphabetically or by profile;
  - show owner and version on every page.
- Related: none

##### D-11 Process: the hand-written parts of the specifications are not checked and are not in the worklist
- Kind: process
- Severity: medium
- Pages: all 91
- Source: `world/specifications.json`; `tools/build_examples.py` lines 2898ff. (the check that only verifies every URN used is described)
- Finding: These parts are regenerated on every build and stay right: the example lists, and the transaction chosen by document type. These parts are not, and nothing checks them:
  - the purposes, roles, community members and flow lists, and the national rule texts are hand text;
  - no check compares the roles with documents.json (D-05), the members with the parties of claiming documents (D-04), or the national texts with the tax and payment rules in countries.json (D-02, D-03);
  - every specification stays version 1.0 while D9, D17, D22 and D23 change what they say;
  - no worklist cause or O-point covers `world/specifications.json`, so the D-decisions will be implemented without it.

  The new flows show the gap:
  - D47 medicines: an invoice to Selanu General Hospital, a public body of Lisavu (D46). Lisavu has no national specification. An air shipment from Lumeport falls in no community.
  - D48 lpg: "the haulier's consignment note under Bayvarra's national rules" has no national transport specification. `national()` only handles Invoice/CreditNote by accounting supplier and customer.
  - O137 (reefer by sea): would fall under the port community only if "sea, cotton" is extended by hand.
  - The D38 additions join automatically, for example tender/40 TenderReceipt once built.
- Should be:
  - an O-point "specifications follow the decisions" with the D-01 to D-05 changes;
  - a build check that the roles and community membership in specifications.json match the claiming documents;
  - a step in "when a flow is implemented" (O112) to review its specifications;
  - a decision on versioning (Q-D-03).
- Related: O112, O138, O137, D46, D47, D48

#### Questions

##### Q-D-01 Should a transaction specification state rules, or stay a one-line description?
- Context: All 70 transaction pages carry no rules, roles, code lists or identifiers, and 54 only repeat the UBL definition (D-07). The decisions define a transaction as having rules, and the examples' reasons claim the documents "follow" these specifications.
- Options:
  - A: Generated sections per transaction: roles, code lists and schemes from the examples, plus links to the decisions that apply. This is cheap and always current, but describes rather than prescribes.
  - B: Hand-written rules per transaction in specifications.json. This is a real specification, but much work, and it drifts without checks.
  - C: Keep them as they are, and say on the index that the pages are identifiers with a purpose, not specifications. This is honest and costs nothing, but the pages stay of little use.
- Recommendation: A. A few hand rules should be added only where a decision makes one (P-SB, D9, D23, D26).
- Findings depending on it: D-07, D-05, D-11

##### Q-D-02 Which national levels does an invoice claim when the seller's and the public buyer's countries both have one?
- Context: Valdara (XU) invoices the Bayvarran Public Works Department with Urvanian VAT (D17.2), but claims only XB:public-billing (D-02). A `#compliant#` chain is linear.
- Options:
  - A: Chain both: `trns:billing#compliant#XU:invoice#compliant#XB:public-billing`. Every rule the document follows is visible, at the cost of a four-part chain.
  - B: Keep one national level (the buyer's), but restrict the XB text to the withholding and the representative, and state that the tax is the seller's. This is simpler, but the XU rules are applied without being claimed.
  - C: The seller's level only; the public body's withholding is shown in the document without a specification claim. This is simple, but loses the public-billing claim.
- Recommendation: A, because it follows D17.2 literally. In real practice a CIUS on a CIUS (for example XRechnung on EN 16931) is also chained.
- Findings depending on it: D-02

##### Q-D-03 Do specifications get a new version when a decision changes their rules?
- Context: Every URN ends in `:1.0`, and D9, D17, D22 and D23 change what billing, XU:invoice and XB:public-billing say (D-11). A new version changes `CustomizationID` in every document that claims it.
- Options:
  - A: Keep 1.0 until the world is first "released", and correct the texts in place. This is no churn, but no history either.
  - B: Raise the version (1.1) on each rule change, with a change note on the page. This is realistic and shows how versioning works, but causes churn in many examples.
- Recommendation: A for now, since the world is still being built. Add a sentence on the index ("version 1.0, texts follow the owner's decisions of November 2026") and adopt B after the first release.
- Findings depending on it: D-11

##### Q-D-04 Do the new flows need national specifications of their own?
- Context: D47 has an invoice to a Lisavan public hospital and an import declaration on the island. D48 has a road consignment note "under Bayvarra's national rules". The world has no Lisavan specification and no national transport specification, and `national()` only handles invoices and credit notes.
- Options:
  - A: Add them (XL public billing if Lisavu has rules for public bodies; XB road consignment note) at O138.
  - B: Keep the national level to tax and invoices only, and word D48's "national rules" as content of the consignment note, not a specification claim.
- Recommendation: decide with O138. Choose B unless the island's public bodies or Bayvarra's dangerous-goods road rules give a real business rule to state.
- Findings depending on it: D-11

### Part E: Examples section (structure and process); flows waste, carnet, mast, ore, packaging, wood, energy, utilities, air

Pages covered:
- `examples.html`: read fully.
- The example page template: read in its source (`tools/build_examples.py` `page()`, `tools/build_site.sh` example loop). Read fully: `example-waste-01-WasteNotification.html` and `example-carnet-01-GoodsItemPassport.html`.
- Scripted over all 262 example `.md` files (the part before `## The document`): internal references, repeated reasons, concatenation artifacts.
- Flows: all nine flow introductions (`world/documents.json` `flows[].text`) and all document "why" texts. Sampled: waste/01; carnet/01, 02, 03; mast/02, 03; air/04, 07, 11; ore/05; wood/01 to 03; energy/04, 06 to 08; utilities/08 to 11; packaging/09. Each was read against D31, D36, D39 to D45, the story lines, the "Built with"/"Overtaken" notes and O112, O133, O168, O197, O210.
- Reference state: 262 examples in 18 flows. Gaps are sea/28, tender/34 and furniture/14, removed on 2026-11-19. The flow decisions of my flows are built: G1 waste, plastics, wood; G2 carnet, mast, air; G3 ore, rail; G4 energy, utilities; G7 packaging.

#### Findings

##### E-01 Removed document numbers leave silent gaps in the flow tables
- Kind: structure
- Severity: medium
- Pages: `examples.html` (sea: 27 is followed by 29; tender: 33 by 35; furniture: 13 by 15)
- Source: `tools/build_world.py:262-273` (the examples index) uses only `world["documents"]`. `world["removed_documents"]` (`tools/world_data.py:35-45`) is never used by the site.
- Finding: the D28 numbering rule (a removed number is never reused) shows up on the site only as a missing row. Nothing says that number 28 of the sea flow existed and why it went. The reason is in the data and is written for readers: "Removed 2026-11-19 (D30 point 3, O6, D9): the customs inspection and the day of storage that Velumi paid are a cost passed on, which Lumeway credits as the second line of its credit note (sea/26) … Its number 28 is not used again (D28)." The same holds for tender/34 and furniture/14. The intro of `examples.html` does not explain the numbering rule either.
- Should be: the table shows a muted row for each removed number with its `removed` text, and the page intro has one sentence on the rule. Authority: D28 "Example files: numbers", D38.
- Related: D28, D30, D32, D38, O6, D9

##### E-02 Flow tables are in number order with no dates, so documents added later appear out of story order
- Kind: structure
- Severity: medium
- Pages: `examples.html`, all 18 flow tables. Visible in tender (37 guarantee, 38 receipt advice and 39 invoice after the remittance advice 36), retail/23, furniture/18 and 19, rail/12 to 14, energy/10, air/11 and waste/04.
- Source: `tools/build_world.py:265-271`. The columns are only "| | Document | From | To |", and the rows follow `nn`.
- Finding: under D28 a new document takes the next free number "even when it falls earlier in time". The table therefore no longer gives the story's reading order, and it shows neither an issue date nor the document's "why". The "why" exists in `documents.json` and is already shown on the party pages (`entry()` in `build_world.py:186-208`). A reader cannot tell, for example, that energy/10 (Ferrano Energy's import) belongs beside 05, or that waste/04 (the weighbridge) comes before the invoice 03.
- Should be: an issue-date column, taken from the generated XML, with rows in date order and the number kept as the stable ID. Or keep number order and add the date and a one-line "why". Authority: D28 (numbers are IDs, not order).
- Related: D28, D38

##### E-03 Examples section entry points: no landing card, no counts, no contents, flows in an unexplained order
- Kind: structure
- Severity: low
- Pages: `index.html`, `examples.html`
- Source: `site/index.html` (cards for Method, World, Map sheet, Releases, History and Coverage; none for Examples). `tools/build_world.py:255-263` (the intro of `examples.md`). `tools/build_site.sh:119-122` calls `page` without a toc-depth.
- Finding:
  - The landing page has no card for the 262 world examples, which are the core of what the project makes. Its key figures ("76 OASIS example files", "27% of UBL 2.5 elements used") are about the OASIS `xml/` set only.
  - The world coverage of 4571/5160 (CLAUDE.md, 2026-11-20) appears nowhere on the site.
  - `examples.html` is one long page with 18 sections and no "On this page" list. It gives no count of flows or documents.
  - Its flow order (ore, road, rail, plastics, retail, sea, air, tender, contest, carnet, waste, utilities, wood, furniture, cotton, packaging, mast, energy) is the order in `documents.json`, with no grouping such as goods chain, procurement, services or the island, and no explanation.
  - "whose history is in this repository's `xml/` folder" is a repo path, not a link to `releases.html` or `history.html`.
- Should be: an Examples card on the landing page with the world counts (documents, flows, world coverage). A table of contents on `examples.html`. The flows grouped, or their order explained. A link instead of the folder name.
- Related: none (presentation)

##### E-04 Example pages have no navigation: no way back to the flow, no previous/next, no links to party or specification pages
- Kind: structure
- Severity: medium
- Pages: all 262 `example-*.html`
- Source: `tools/build_examples.py:1848-1875` (`page()`) and `tools/build_site.sh:125-131`, where `page` is called without a toc-depth.
- Finding:
  - Each page opens with "*Example 1 of the flow "Production waste to recovery (domestic, Urvania)" · [Waste Notification in the UBL 2.5 specification]*", the document's "why" and the XML link. The flow name is plain text with no link to `examples.html#<flow>`.
  - There is no previous or next document of the flow.
  - Sender and receiver in the title are not linked to their party pages (`world-<n>-<c>.html`), although the party pages link to the examples.
  - The `CustomizationID`/`ProfileID` reasons say "Each has a public description on the world's pages (world/specifications.json)" but do not link the spec page that exists (`world-spec-*.html`).
  - Pages run 300 to 1,100 lines with no table of contents.
- Should be: a header line with the flow (linked), "previous / next" in flow order (or date order, see E-02), and the parties and specifications linked. A TOC of the value groups.
- Related: none (presentation)

##### E-05 The document-specific reasons are buried under repeated party and country boilerplate
- Kind: structure
- Severity: medium
- Pages: all 262 example pages
- Source: party, address, contact and telephone reasons in `tools/build_examples.py` (`src = f"identity of {idn['name']} (world/parties.json)"` at lines 196, 400, 606, 758, and the address-format and telephone-plan texts from `world/countries.json`).
- Finding: of 42,344 value rows, 55 % repeat a reason text that occurs 20 times or more, and 33 % are party or country master data. Examples:
  - "The country's name, for readers of the address." (733 times)
  - The full address-format rule of about 600 characters, repeated for every party in every document (418 times for Bayvarra alone)
  - The +999 telephone-plan explanation
  On `example-waste-01` the reader meets about 40 lines of Valdara's master data before the document says anything particular. Part of this is the pre-O86 state: every document copies full master data. waste/01 gives a waste notification's sender the contact "Order desk / Order administrator / Sales". Part of it is presentation, which holds even after O86.
- Should be: the build shows a party's master data once, as "as on the party page" with a link, plus the values this document adds or differs in. It also shows each recurring rule once per page (or links a glossary), so that the reasons particular to the document stand out. The XML content follows O86 when that is applied (stale against O86, pending O88).
- Related: O86, O88, C01, D11

##### E-06 Concatenation artifacts and internal keys in reason texts
- Kind: wrong
- Severity: low
- Pages: 199 pages (IssueTime) and all 262 pages (identity suffix)
- Source:
  - `tools/build_examples.py:3327` appends "; in the issuer's local time, with its offset from UTC (D27)" to a reason that already says "in the sender's local time" (line 3634).
  - Lines 196/400/606/758 append ". identity of …" after a full stop.
  - Line 713 prints the route key.
- Finding:
  - "The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27)." (199 pages)
  - "Building number of the postal address. identity of Valdara Industries (world/parties.json)." (4,560 rows with a lower-case sentence after a full stop)
  - "The distance is the length of the map's route gas-field, rounded to 10 km." (an internal route ID, energy/04, 06, 07, 08)
  - Source file paths such as "(world/parties.json)" and "(world/codelists)" are shown without links.
- Should be: one clean sentence each time. The route named by its places. Data sources linked to the repository file, or named in words.
- Related: D27

##### E-07 Reasons cite decision, open-point, cause and review-finding IDs that a reader of the site cannot resolve
- Kind: process
- Severity: medium
- Pages: 262 pages. References per type:
  - D-numbers: about 1,900 (D27 937, D1 261, D20 186 and others);
  - ID-Q (codelist decisions): 342 (ID-Q7 319);
  - Q: 228 (Q29 225);
  - O-numbers: 332 on 158 pages;
  - review findings: about 250 on 219 pages (tender 240, contest 65, retail 47, sea 44, …);
  - worklist causes: about 237 ("worklist C15").
  Four flow intros also cite decisions ("(decision D42)" waste, "(decision D45)" ore, "(decision D43)" wood, "(decision D37)" rail), and so do some document "why" texts ("(D31 point 4)", "(D44)").
- Source: hand-written strings in `tools/examples_scenarios.py` and `world/documents.json`; generated suffixes in `tools/build_examples.py`.
- Finding:
  - Examples: "…deducts 1.5 % of the value (D45, ore/07#F2)."; "The framework contract for container slots, … (rail/02#F13, 03#F14)."; "The commercial invoice the customs value rests on (worklist C12)".
  - The site publishes neither `analysis/worklist-decisions.md`, `analysis/codelist-decisions.md`, the worklist nor the reviews (`build_site.sh:126` leaves the reviews out on purpose), and it has no link to them.
  - Two numbering systems look alike: "decision D1" (worklist) and "decision ID-Q7" (codelist decisions).
  - Some references point to a document that no longer exists: tender/38 says "What the penalty clause counts (tender/34#F3)." (`examples_scenarios.py:11000`).
  - Some cite open points that are still open (O107, O30, O152, O176, O123, O127, O128, O145, O155, O172, O173, O117), without telling the reader that the value is provisional.
- Should be: see Q-E-01. Either link each D/ID-Q/O reference to a stable anchor in the published or GitHub decisions file, or render the reason without internal IDs and keep the IDs in the source. Review-finding and cause IDs belong in commit messages or source comments, not in the reader's text, because the reviews are not published.
- Related: O112, O197; CLAUDE.md "The reviews are kept"

##### E-08 How a reason is kept up to date: four hand-kept copies of each story, and no check that ties the prose to the decisions
- Kind: process
- Severity: high
- Pages: all example pages and `examples.html`
- Source:
  - The per-value reasons are hand-written `V(value, why)` pairs in `tools/examples_scenarios.py` (12,978 lines), plus generated reasons in `build_examples.py` and `examples_kit.py`.
  - Flow and document texts: `world/documents.json` (`flows[].text`, `documents[].why`).
  - Story lines: `analysis/worklist-decisions.md`.
  - The flows in `note/src/03-world.md`.
- Finding:
  - What stays current by construction:
    - reasons computed from data, such as party, address and code-list texts and distances from the map ("ran 159 km on the line past Ferrano", ore/05; "about 80 kilometres out", energy);
    - the generated `.md`, which `build_examples.py --check` keeps in step with the generators;
    - the 34 story assertions in the scenarios (for example `examples_scenarios.py:54`: "ore: the train no longer arrives on the afternoon of 10 March (D45, O152)").
  - What is not: every hand-written sentence that copies a fact (a date, a place, an amount, who does what). No check compares it with the decisions. The only safeguard is O112, a manual sentence-by-sentence reading. It is recorded as done for road (G5), furniture and retail (G7), cotton and sea (G8) and the contest. There is no record of it for the G1 to G4 flows (waste, plastics, wood, carnet, mast, air, ore, rail, energy, utilities) or for packaging.
  - The gaps found in this part fall exactly there: E-10, E-11.
  - The story lines themselves, the reference O112 reads against, have not followed their own "Overtaken" notes (E-12).
  - Nothing catches a reason that cites a removed document (tender/34#F3, E-07).
- Should be:
  - Run O112 for the remaining flows.
  - Add a mechanical check to `check_world.py` or `build_examples.py` that fails when:
    - a D/O/MO number in a reason does not exist in the register;
    - a reason cites a removed document (`removed_documents`) or one of its findings;
    - a reason cites an O-point that is still open (warn).
  - For each decided story line, add assertions for its key facts, in the style of `ORE_ARRIVES`, so that a world change stops the build instead of leaving a stale sentence.
  - Make one copy the source: let the flow intro come from the story line, or the reverse.
- Related: O112, O197, O214, D28, D38

##### E-09 The review and implementation status is invisible to the reader
- Kind: structure
- Severity: medium
- Pages: `examples.html`, all example pages
- Source: `tools/build_world.py:255-263` (intro). No data key holds a flow's status.
- Finding:
  - Nothing on the site says that the examples were reviewed in November 2026 (3,348 findings, 128 causes), that the decisions D1 to D48 are being implemented in stages, which flows have their decisions built (G1 to G8, 2026-11-19/20), which world rules are still to come, or which flows are planned.
    - Rules still to come: O86 for party data, pending O88; signatures D6 in their own stage; the D1/D2 locale and tag rules in the stage where they belong.
    - Planned flows: medicines D47, lpg D48, the reefer O137.
  - The only hint is the footer "Work in progress". A reader cannot tell a settled value from one awaiting a decision. For example, waste/01's sender contact "Order desk … Sales" waits for O86, while its `WasteNotificationTypeCode` DOMESTIC is D42 as built.
- Should be: see Q-E-02. One paragraph on `examples.html` about the state of the work, and a status line per flow taken from data (for example a `status` key in `documents.json` flows: "decisions built 2026-11-19 (G1); party data to follow O86"). The planned flows listed as planned, without numbers.
- Related: D6, D47, D48, O86, O88, O137

##### E-10 Four flow introductions do not tell the decided story (utilities, energy, carnet, packaging)
- Kind: stale (D31, D44, D40, D41/O133/O168)
- Severity: medium
- Pages: `examples.html` (four sections) and the party pages, which repeat `f["text"]` (`build_world.py:217`)
- Source: `world/documents.json` `flows[].text`: carnet at line 298, utilities 429, packaging 698, energy 829.
- Finding: the ore, waste, wood, air and mast intros were rewritten with their decisions and agree with them; ore and mast already follow O197 and O210. These four were not rewritten, although the document texts beneath them were:
  - **utilities** (D31): "Every business and household pays a utility. UBL bills a utility with an Invoice and supplements it with a Utility Statement … the three countries tax them differently." The intro misses what the decision says the flow shows: the household on account with the annual statement and settlement bill (08 to 11), the second supplier on a bill (Ferrano Grid's network charges, the city's sewage levy), the warehouse owned by Valdara and run by Castrano, and the Coral net account. The title "Electricity, water and telecom" omits the district heat that D31 adds.
  - **energy** (D44): "The documents show the grid operator's metering …, the wholesale and network invoices, the customs declarations of a pipeline, and a reminder across currencies." The intro misses D44's subject: one export declaration with a consignment per buyer, and each buyer declaring its own import (energy/10, added). Neither the 36,800 and 2,400 MWh, Montebrio as one of several stations, nor the field about 80 km offshore are mentioned.
  - **carnet** (D40): "An ATA carnet, guaranteed by the chambers of commerce of both countries, …" The flow involves three countries, and the wording leaves unsaid which two chambers guarantee. Three of the flow's four documents (02 to 04) concern the lost re-exportation voucher and the proof requested after the 30 June limit, and the intro does not mention them. D40: "a missing voucher as the reason for the claim".
  - **packaging**: two sentences with no reason or story ("The packaging maker supplies the manufacturer in Urvania and the textile mill at home; …"). The intro does not tie the flow to the D41 goods balance (film from Rinova's granulate for Valdara's bench pallets, garment bags for the mill's shirts) or to O168 ("a year's supply" of film).
- Should be: each intro tells its decided story, as the D31, D44 and D40 story lines and D41 point 4 / O168 have it. Then O112 is applied to these flows.
- Related: D31, D40, D41, D44, O112, O168; worklist C78, C82, C91 to C95

##### E-11 packaging/09: the trade fair placed in Lumeport, against O133
- Kind: stale (O133)
- Severity: medium
- Pages: `example-packaging-09-PurchaseReceipt.html`, and the party pages that show its "why"
- Source: `world/documents.json:3750` (document "why"); `tools/examples_scenarios.py:11673` (`"IssueDate": V(f.date(26), "During the trade fair in Lumeport.")`)
- Finding: the page says "The island trader's buyer, in Lumeport for the trade fair, buys shirts for the stand team …" and gives IssueDate 2026-05-23 with the reason "During the trade fair in Lumeport." O133 was settled on 2026-11-17: "one fair: the island trader's buyer is in Lumeport on business and buys shirts for Velumi's team at the Selanu chamber's fair of early June (D40); the receipt says so." The world has no trade fair in Lumeport, and the XML says nothing about the purpose.
- Should be: the "why" and the IssueDate reason as O133 has them, and the receipt stating it (in a note) as O133 asks.
- Related: O133, D40, D41 point 4

##### E-12 The story lines in the decisions file lag behind their own "Overtaken" notes; the site is right where they are wrong
- Kind: stale (O197, O210, O214), in the authority, not on the page
- Severity: low
- Pages: none wrong on the site (the ore and mast intros are correct). This affects the reference that O112 reads against.
- Source: `analysis/worklist-decisions.md`, story lines "Ore from the mine (D45)", "Equipment for the island's telecom mast (D36)" and "Containers by rail to Lumeway (D37)"
- Finding:
  - The ore story line says "the train runs about 180 km"; O197/O214 make it 159 km, and the site intro says "about 160 km".
  - The mast story line says "the detectors and the stripper in a closed container kept away from them". O210 puts the stripper (cargo aircraft only) where the crew can reach it, beside the batteries, which is what the site's intro and mast/02 say.
  - The rail story line says "the intermodal hub at the border"; by O214 it is in Ferrano (reviewer F's flow).
  - The story line, which should drive the text, is behind the text.
- Should be: the story lines brought into line with O197, O210 and O214, as O197 decided ("the later decision wins, recorded with a note in each overtaken decision"). The notes exist in the decisions but not in the story-line section.
- Related: O197, O210, O214, D36, D37, D45, O112

##### Flows checked with no conflicts beyond the above
- **waste** (D42): the intro and waste/01 follow D42: domestic notification, environment agency, DOMESTIC type, the weighbridge waste/04, net 22.9 t. E-05 and E-09 apply (O86).
- **ore** (D45): the call-off, the 159 km run from the map, the 2 % bonus and the moisture clause agree.
- **wood** (D43): bundles of 50, oak with ash as an alternative, and 96 bundles in every document agree.
- **air** (D39, O162): KXL209 missed, KXL207 flown, a direct air waybill, and air/11 added; all agree.
- **mast** (D36 as revised by O210): the intro and mast/02 and 03 agree with O210.
- **utilities** and **energy** documents: the figures follow D31/D44 as built: utilities/09 1,149.20 less 1,008.00, giving 141.20; the reminder 146.42; the credit note 5.54; energy/04 two consignments; "about 80 kilometres". The only gap is the intros (E-10).
- **carnet** documents: they follow D40 (counterfoils unstamped at issue, a missing voucher, 43.912 coral). The only gap is the intro (E-10).

#### Questions

##### Q-E-01 How should decision and review references appear in the reasons that readers see?
- Context: about 1,900 D-, 342 ID-Q-, 228 Q-, 332 O-, about 250 review-finding and about 237 worklist-cause references appear in the public reason texts (E-07). None can be resolved on the site.
- Options:
  - A. Strip them in the rendered page and keep them in the source. Clean for readers, but the link to the reasoning is lost.
  - B. Link the D, ID-Q and O references to stable anchors in the decisions files on GitHub (or publish a "Decisions" page), and strip the review-finding and cause IDs. This keeps the method visible and needs anchors and a link-rewrite step.
  - C. Keep them as they are. No work, but opaque to readers.
- Recommendation: B, because the decisions are part of the method the site presents, while the reviews are deliberately unpublished.
- Findings depending on it: E-07, E-08 (the check's form)

##### Q-E-02 Should the site show the review and implementation status per flow?
- Context: the November reviews and the staged implementation are invisible (E-09). Some values wait on O86, D6 or D1/D2.
- Options:
  - A. A status line per flow from a data key in `documents.json`, plus one paragraph on `examples.html`. Accurate and maintained with the flow, but it adds a field to keep current.
  - B. One general paragraph only. Cheap, but it says nothing about the individual flows.
  - C. Nothing. This keeps the site clean but can mislead.
- Recommendation: A, because it is kept in the same commit as the flow change and states what a reader may rely on.
- Findings depending on it: E-09

##### Q-E-03 Should planned flows (medicines D47, lpg D48, reefer O137) be announced on `examples.html`?
- Context: the flows are decided but not built. Their numbers and documents do not exist yet.
- Options:
  - A. A short "Planned" list with titles only. It shows where the work is going.
  - B. Nothing until they are built.
- Recommendation: A, titles only and no document numbers, so that nothing is promised that D28 would later have to retire.
- Findings depending on it: E-09

##### Q-E-04 How should removed document numbers be shown?
- Context: the `removed` texts exist in `documents.json` (E-01).
- Options:
  - A. A muted row in the flow table with the removal reason.
  - B. A footnote under the table.
  - C. Nothing, as now.
- Recommendation: A, because the reviews and the worklist cite these numbers, and the reader then sees why they are missing.
- Findings depending on it: E-01

### Part F: example pages of the flows road, rail, sea, cotton, plastics, retail, furniture, tender, contest

Pages covered: all 186 `example-<flow>-NN-*.html` of the nine flows, plus their intros and tables on `examples.html`.
- **Read in full:** road/01, 02, 11, 12, 13; rail/01, 08, 12, 13, 14; sea/05, 14, 22, 26, 29; cotton/01, 10, 13; plastics/07, 12; retail/01, 04, 06, 20, 22, 23; furniture/01, 06, 08, 12, 13, 18, 19; tender/02, 13, 15, 18, 20, 26, 32, 36, 37, 38, 39; contest/03, 05, 15, 16, 17, 18.
- **Scripted over all 186 pages** (working files, not kept):
  - the lead sentence and the IssueDate reason of every page , and every document's `why` in `world/documents.json` ;
  - issue dates in number order against time order, and weekend issue dates;
  - grep for terms that the decisions removed (consortium, mediation, documentary collection, Tevaro, the restocking deduction, the Container Convention, CMR, spring or summer, the debit notes, PWD-RCPT …);
  - the D/O/Q numbers and the review-finding IDs cited in the reasons;
  - party names in `PartyName` checked against `world/parties.json`.
- **Authority read:** `analysis/worklist-decisions.md`: D27 to D41 for these flows, D38, the story lines of the flows, and the O-points they cite (O30, O102, O109, O112, O119, O149, O155, O170, O172, O174, O193, O196, O197, O214, O220, O226).

Overall: the pages follow the "Built with G1 to G8" state of the decisions closely. Debit notes, CIF, open account, the plant protection service, the parcel on the wrong pallet, the reopening, the dining set, CIM, demurrage, the subcontractor in the values, the guarantees and the excluded studio are all there. What is left over is small and sits mostly in the one-line `why` texts in `world/documents.json`, which were not rewritten when the values were. The other gaps are the flow intros and the way the numbering is explained.

#### Findings

##### F-01 Tender leads still speak of a "consortium partner" (D28 point 3)
- Kind: stale (D28 point 3)
- Severity: high (the first sentence on each page contradicts the value shown below it)
- Pages: example-tender-13-TendererQualification, example-tender-15-Tender, example-tender-20-TendererQualificationResponse (3)
- Source: `world/documents.json` `why` of tender 13 (line 2321), 15 (2345) and 20 (2401).
- Finding: the leads read:
  - tender/13: "The manufacturer declares its qualifications and those of its consortium partner."
  - tender/15: "The tender, with the consortium partner as subcontractor."
  - tender/20: "The manufacturer and its consortium partner are admitted to the evaluation."

  On the same pages the values say `TendererRoleCode` = SOLE ("The manufacturer tenders alone (tender/13#F2)") and "Saltmere Engineering as its subcontractor for the installation (lot 2); the manufacturer is liable for it" (tender/13).
- Should be: D28 point 3 says Valdara tenders alone, with Saltmere as subcontractor and not as a consortium partner. For example: "The manufacturer declares its qualifications, with its subcontractor for the installation"; "The tender, alone, with Saltmere Engineering as subcontractor for lot 2"; "The manufacturer is admitted to the evaluation."
- Related: D28 point 3; C124; tender/13#F2.

##### F-02 The review body "for appeals and mediation" (D28 point 7)
- Kind: stale (D28 point 7)
- Severity: medium
- Pages: example-tender-02-ContractNotice (lead). The same wording is on the party's world page, outside this scope.
- Source: `world/documents.json` `why` of tender 02 (line 2197); `world/parties.json` "what" of the Procurement Review Board of Bayvarra (line 1698); `tools/party_cover.py:40` ("Review body (procurement appeals and mediation)"); `tools/examples_scenarios.py:3529` (`appeal_why`, not used on the pages).
- Finding: the lead reads "The call for competition is published; it names the review body for appeals and mediation." The page has no mediation element: it shows only `AppealTerms` with the `AppealReceiverParty`.
- Should be: D28 point 7 says the board is "only the party appeals go to … there is no separate mediation step". The lead should read "it names the review body for appeals", and the party's "what" should drop "and mediation".
- Related: D28 point 7; C127.

##### F-03 Northern seasons in March and April (D27, O109)
- Kind: stale (D27 story line "The calendar", O109)
- Severity: medium (it undoes the very reasoning behind D32 and D34)
- Pages: example-road-01-Order (IssueDate 16 March: "The distributor orders for its spring stock."); example-rail-01-Order (IssueDate 6 April: "Full container loads for the summer season.") (2)
- Source: `tools/examples_scenarios.py:350` (road order), `:1127` (rail order).
- Finding: under D27 the world has the seasons of the south: March to May is autumn, winter starts on 20/21 June (retail/20 says so). For the same reason D32 rewrote the furniture line and D34/O109 rewrote the retail promotion. The two bench orders still give a northern spring or summer as their reason. No other page in scope does: the retail and furniture pages say "autumn and winter" and "winter catalogue".
- Should be: a reason that fits the southern calendar. Examples: the road order "for its autumn stock, and for the reopening at Brightmarket and the island order" (the chain of D21); the rail order "full container loads to rebuild stock before winter" (O109 rule: change the names, keep the dates).
- Related: D27, O109, D32, D34, D21.

##### F-04 sea/24 is issued on a Saturday by an office (D30 point 6, D27)
- Kind: stale (D30 point 6)
- Severity: low
- Pages: example-sea-24-InvoiceStatusResponse (IssueDate 2026-05-30, a Saturday; reason "Answered the next day.")
- Source: `tools/examples_scenarios.py:5851` (`head(f, "invoice-status", doc, 26, "Answered the next day.")`).
- Finding: D30 point 6 names the office documents on a weekend, "09, 12, 24, 25", which "move to working days". Velumi Trading is of kind `office` in `world/parties.json` (Monday to Friday under D27). 09, 12 and 25 were moved, but 24 still answers on Saturday 30 May. Its reason, "the next day", hides that. sea/08, 16 and 17 are on a weekend too, but their issuers are carriers and ports, which D27 lets work every day.
- Should be: answered on Monday 1 June, or the request moved, per D27 rule 1. The D27 build check (issue weekday per issuer kind) does not seem to catch an InvoiceStatusResponse (process).
- Related: D27, D30 point 6, C53.

##### F-05 tender/18 still cites a receipt that is "not shown"; tender/40 decided but not built (D38)
- Kind: stale (D38)
- Severity: medium
- Pages: example-tender-18-TenderWithdrawal ("TenderNotificationDocumentReference/ID = PWD-RCPT-BF-1 — The receipt the platform issued for the tender withdrawn (not shown).")
- Source: `tools/examples_scenarios.py:9792`; `world/documents.json` (no tender 40).
- Finding: D38 decided "Tender, new document 40: a Tender Receipt … for Brackenmere's first tender (17) … which [18] cites instead of `PWD-RCPT-BF-1`", and lists it under "All documents added and removed" (tender +40). D28's "Built with G6 (2026-11-20)" and D38's "Built 2026-11-20 (G6)" list +37, +38, +39 and −34, but not +40, and no O-point defers it. So the page shows the state before the decision, and the "(not shown)" explanation is what D38 meant to end.
- Should be: tender/40 built and cited by 18. Alternatively, if it was dropped on purpose, an O-point that records this, and a correction of D38's list.
- Related: D38, tender/18#F2.

##### F-06 Flow intros on examples.html lag the decided stories (O112)
- Kind: stale (O112) / structure
- Severity: medium
- Pages: examples.html, sections road, sea, cotton, contest and retail. The intros of rail, plastics, furniture and tender carry their decided story.
- Source: `world/documents.json` `flows[].text`: road (line 29), sea (146), cotton (517), contest (292), retail (111). The decided wording is in the story lines of `analysis/worklist-decisions.md` (lines 1404 to 1432).
- Finding: O112 says that when a flow is implemented "its decided story is written into the world's texts (`world/documents.json` …)". D35 even says "The road story read against its XML (O112)". The intros are still the earlier generic texts:
  - **road:** "The distributor buys park benches free carrier (FCA) … the seller clears them for export, the distributor for import." Not a word on the 2026 casting, the chamber's certificate with its application (06, 07), or the bench parcel on the wrong pallet. Without that, a reader cannot see why a receipt advice (11), a fulfilment cancellation (12) and a second receipt advice (13) follow each other.
  - **cotton:** "The island's export. The farm delivers seed cotton … and gets a goods certificate." It does not mention the harvest (March to May) that D33 moved the flow into, the advance before the harvest (01 is a self-billed invoice dated 13 January), the mill's forecast and its revision, classing and the self-billed credit, the Plant Protection Service (O170), or the collect freight recharged by the forwarder.
  - **sea:** covers the CIF purchase up to receipt. It does not cover the deposit and the 45 days, the factor (18, 22, 25, 27), the crushed frame and the inspection credited (26), or the shop sale at 375 coral (29). Those are all in the D30 story line.
  - **contest:** lists the revisions only. Missing: the Brackenmere and Saltmere team and the change of design lead (D29 point 2), the check of every team member (17, D29 point 6), and the excluded design studio (18, O102).
  - **retail:** covers the reopening and the catalogue. Missing: the slot delivery that is ten minutes late (23, 15, 17), the refused bench and its credit set off against the factor, the lower side-frame price (03, O15), the datasheet update (04), and that retail/22 is the furniture flow's Marrow set. Those are all in the D34 story line.
- Should be: each flow's `text` brought up to its story line ("The road delivery to Lumeway (D35)", "Cotton from the island (D33)", "The island's first order by sea (D30)", "The design contest … (D29)", "The reopened department (D34)"), with the later O-points applied: O172 (104 benches), O196 (68.00), O174 and O155. See Q-F-01.
- Related: O112, D29, D30, D33, D34, D35.

##### F-07 Leads that ignore what the built document now says
- Kind: stale (D28, D29, D35)
- Severity: low
- Pages:
  - example-road-11-ReceiptAdvice: lead "The distributor confirms what arrived …". The page reports "one bench short of a parcel, one frame carton over" (D35 point 1).
  - example-tender-26-Order: lead "The first call-off … the manufacturer delivers". The order now carries the 40 installations as a second line, which D28 point 9 added because the installation had been "billed but never ordered".
  - example-contest-05-QualificationApplicationRequest and contest-10: lead "asks for the self-declaration on the design lead's professional qualification". D29 point 6 adds exclusion grounds, and the pages ask for them (16 mentions each).

  (4 pages)
- Source: `world/documents.json` `why` (road 11 at line 1118, tender 26 at 2472, contest 05 at 3981, contest 10).
- Finding: these leads are not wrong, but they leave out the reason the decision gave the document. A reader following the flow table misses the turn of the story: road/11 reads like a normal receipt that 12 then cancels for no visible reason.
- Should be: one clause each, for example "… and reports one bench short and a frame carton over", "… 40 benches and their 40 installations", "… exclusion grounds and the design lead's qualification".
- Related: D28 point 9, D29 point 6, D35 point 1.

##### F-08 Added documents numbered out of time, and the removed numbers, are not explained
- Kind: structure
- Severity: medium
- Pages:
  - Added documents that come earlier in time than their number:
    - example-retail-23-TransportExecutionPlan (27 April, between 11 and 12);
    - example-furniture-19-DespatchAdvice (23 March, before 09);
    - example-tender-37-GuaranteeCertificate (19 February, before the tenders), tender-38 (13 April) and tender-39 (14 April), both before 33 and 35;
    - example-contest-17-BusinessInformation (5 May, before 14), contest-18 (12 May, before 15);
    - example-rail-14-ImportCustomsDeclaration (15 April, before 10, 12 and 13).
  - Gaps in the flow tables: furniture 14, sea 28, tender 34. The sea/29 page still says "Example 29 of the flow".
- Source: `world/documents.json` `why` of these documents. The flow tables on examples.html come from the examples-page generator (reviewer E's scope).
- Finding: D28's numbering rule (the next free number, a removed number never reused) is applied correctly. But only plastics/12 tells the reader: "It is numbered after the flow's other documents although it comes first in time (D28)." For the others the flow table on examples.html lists them last. In the tender this puts Brackenmere's guarantee after the remittance advice; in retail, the carrier's confirmation of the slot comes after the shopper's webshop order. Nothing says why 14, 28 and 34 are missing, although `world/documents.json` keeps a `removed` text for each that would explain it.
- Should be: the plastics/12 clause on each added page that comes earlier in time, and a line in the flow table for each removed number (its `removed` text), or the table in time order with the numbers kept. See Q-F-02.
- Related: D28 ("Example files: numbers"), D38.

##### F-09 Reasons cite review findings and decision numbers that the site does not publish
- Kind: irrelevant (for a site reader) / process
- Severity: low (overlaps with reviewer E, the page template)
- Pages:
  - Review-finding IDs: 513 citations on 125 of the 186 pages in scope, for example "(tender/13#F2)" or "not a catalogue (furniture/01#F2)". example-tender-38-ReceiptAdvice cites "What the penalty clause counts (tender/34#F3)", a finding on the removed document 34.
  - D/O numbers throughout: D27 649 times, O142 81 times, O19 37 times, among others.
- Source: free text in `tools/examples_scenarios.py` (for example line 11000 for tender/34#F3) and `tools/examples_kit.py`.
- Finding: the reviews (`*.llm-review.*.md`) are deliberately not published, and neither is `analysis/worklist-decisions.md`, so "(D27)", "(O142)" or "(sea/29#F11)" lead nowhere for a reader of the site. "tender/34" also names a document that is no longer in the flow.
- Should be: either links to a published decisions page, or the reference kept in the generator's comments or the `.md` and left out of the page text. At least, no citation of a removed document's findings.
- Related: D28 (removed numbers), CLAUDE.md "the reviews are kept / not published".

##### F-10 Customer names in lower case in Valdara's references
- Kind: wrong
- Severity: low
- Pages: example-tender-13-TendererQualification: "RecipientCustomerParty/Party/PartyName/Name = City of ferrano", "Town of conciaro", "Town of valico euridice". The text above them correctly says "City of Ferrano".
- Source: `tools/examples_scenarios.py:9454`: `customer[4:].capitalize()` lower-cases every word after the first.
- Should be: "City of Ferrano", "Town of Conciaro", "Town of Valico Euridice" (strip "the " and upper-case the first letter only).
- Related: tender/13#F4.

#### Per flow: does the sequence tell a readable story?

- **road:** mostly. The leads of 02, 06, 07, 12 and 13 carry the D35 story; the intro (F-06) and the lead of 11 (F-07) do not, so the 11–12–13 sequence only becomes clear at 12.
- **rail:** yes. The intro tells the whole story (CIM, infrastructure manager, transit, demurrage, the two debit notes), consistent with O214 (the hub in Ferrano). Only 14, the import of 15 April, comes after the debit notes of 23 and 24 April (F-08). rail/01's "summer season" (F-03).
- **sea:** yes, page by page; each lead says why the document exists. The intro stops at the receipt (F-06). The table has a gap at 28 (F-08). sea/24 is dated a Saturday (F-04).
- **cotton:** yes, page by page, and in time order (after D33's move into the harvest). The intro is still the old generic text (F-06), so a reader meets a "Self Billed Invoice" dated 13 January as the first document without knowing it is the advance.
- **plastics:** yes. The intro is current (D41, O193) and the out-of-time catalogue 12 is explained.
- **retail:** yes, through the leads. The intro covers only the reopening and the catalogue, and the carrier's plan 23 appears after the webshop order (F-06, F-08).
- **furniture:** yes. The intro and the leads follow O155 (the first sale on 11 May, the trial as the first four weeks of sales, the June dates). The public-works part (15–17) sits between the return (13) and the store's transport invoice (18), and the despatch advice of 23 March is last (F-08).
- **tender:** yes; the intro is current. Spoilt by the consortium leads (F-01), "mediation" (F-02), the guarantee 37 and the acceptance 38 listed after the remittance, and the empty 34 (F-08).
- **contest:** yes, through the leads, which state each version's change, as D29 point 4 asks. The intro omits the team, 17 and 18 (F-06).

#### Note for the coordinator (not a site finding)
Some story lines in `analysis/worklist-decisions.md` are older than later decisions. The site follows the later ones, which per O197 win:
- "The Marrow dining set (D32)" still says the five-week trial from March and three benches after four weeks; O155 superseded this.
- "Containers by rail to Lumeway (D37)" and D37 point 4 still have the hub at the border; O214 superseded this.
- "The reopened department (D34)" says "on 21 May it tells the store that the bench's slats are of a new wood"; O149 made one bench in thermally modified ash throughout, and retail/04 now passes on a revised datasheet about the slats' finish.

Whoever brings the decisions file into line should update these story lines. F-06 recommends using the story lines as flow intros, so they should be current first.

#### Questions

##### Q-F-01 Should a flow's intro on examples.html (`flows[].text`) tell the whole decided story, or stay a short summary of trade terms?
- Context: O112 asks that the decided story be "written into the world's texts (`world/documents.json` …)". The rail, plastics, furniture and tender texts were rewritten; road, cotton, sea, contest and retail were not (F-06). The story lines in the decisions file are written as readable paragraphs of the right length.
- Options:
  - A: use each flow's story line (brought up to date with the later O-points) as its intro. The intro then explains the sequence, and stays current only if both are maintained.
  - B: keep short summaries of the trade terms and add a "what happens" paragraph. More text to maintain.
  - C: leave the intros short. The sequence then has to be read from the per-page leads.
- Recommendation: A. The story lines exist, are decided, and say exactly what a reader needs to understand why each next document exists.
- Findings depending on it: F-06.

##### Q-F-02 How should a flow table show documents numbered out of time and removed numbers?
- Context: D28 fixes the numbers (the reviews cite them), but the flow tables list by number, so added documents appear at the end and the gaps 14, 28 and 34 are unexplained (F-08).
- Options:
  - A: keep the number order; add the plastics/12 clause to each such `why`, and a table row for each removed number with its `removed` text. Small change; the order stays as cited.
  - B: sort the table by issue date and show the number. Reads as a story; but the numbers jump, and reviewer E's template changes.
  - C: both, a time-ordered table with a note on the numbering.
- Recommendation: A, because it costs only data in `world/documents.json` and keeps the table matching the cited numbers. B is worth considering together with reviewer E.
- Findings depending on it: F-08.
