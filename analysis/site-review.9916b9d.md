# Site review at 9916b9d

The second review of the published website, made after the first (`analysis/site-review.4242ac3.md`) was closed and
two days of work on the Encyclopedia, the new flows and stage 7 had changed the site. Review only; nothing was
changed for it.

- **Basis:** the site built from `main` commit **`9916b9d`** (2026-11-21; its pages carry `9fd37c8e`, as `9916b9d`
  only added unpublished reviews). Every finding describes that state.
- **Made:** 2026-11-21, by three reviewers in parallel: A (home, navigation, map, About, coverage, history, and a
  link and width check over all 658 pages), B (Trade, the example pages, Parties, Rules), C (the Encyclopedia). Their
  part findings are kept below as the "before" picture; the groups SR2-nn are what is worked.
- **Clean in the mechanical checks:** no broken link or anchor on any page; no page wider than a phone (400 px) in
  light or dark; no D/O/OW/MO/C numbers, real specification names, names of persons or unfilled `{fact:` placeholders
  in published text; on all 302 example pages the place in the story and the neighbours match the Trade page; the
  O279 staff numbers and legal forms agree between the party pages and the Encyclopedia.

## How to keep this file up to date

As for the first review: each group has a **Status** line (`open` → `decided (date, owner: …)` → `solved in <commit>`
or `dropped (reason)`); the part findings stay as written. Its open point is **OW036** in the register.

## Summary: the groups

| Group | What | Parts | Severity | Owner |
|---|---|---|---|---|
| SR2-01 | Saltmere Engineering still "Consortium Partner" (D28: Valdara's subcontractor), called a village, a staff member named on its page | A-01, B-07 | High | working session (party data) |
| SR2-02 | Published text that explains the project, not the world: "the build checks …", "outside the examples", "India, outside the world", "the address is fictional", "as the world's languages are invented", real-world comparisons in flow introductions, "ISO 3166-1, user-assigned" in country infoboxes; `check_published.py` does not catch these | A-05, B-04, B-13, C-04 | High | working session (generators); encyclopedia (C-04, the check) |
| SR2-03 | The Lumeport port community still applies by flow (its page names flow keys), so the reefer's port documents do not claim it, against SR-18/D-04 (what passes through the port) | B-02 | High | encyclopedia session (`world_specs.py`, as in SR-18) |
| SR2-04 | Encyclopedia generator faults: transport infoboxes print every row twice and unfilled `{flight_km}`; company descriptions lower-cased in the towns' lists; localities filed as villages; "Encyclopedia · Encyclopedia" titles; the capitals' climate tables put port towns 120 m up and call radiation "sunshine" | C-01, C-02, C-05, C-08, C-14, A-10 | High (C-01), Medium | encyclopedia session |
| SR2-05 | ISO dates (1903-05-20, 2026-01-01) in an encyclopedia whose English writes "15 April" | C-03 | Medium | encyclopedia session |
| SR2-06 | Encyclopedia conventions not followed everywhere: no References section anywhere, See also patchy, uneven sections per article type, timelines uneven, side menu incomplete and last on a phone, water-map and table polish, disambiguation, false precision | C-06, C-07, C-11 to C-13, C-15, C-16, C-18 | Medium / Low | encyclopedia session |
| SR2-07 | Hand-written and summary texts out of date: About ("the first articles are there"), the map's opening card and the country notes (the economies before the new flows; Bayvarra's note only Lumeport), releases.html opening as the repository README (regression of SR-02), history.html's "earlier attempts" (first review A-11) | A-02, A-03, A-04, A-06, B-09, C-10 | Medium | encyclopedia session (site texts); working session (country notes) |
| SR2-08 | Main-site template glitches: literal backticks in the party-data fold (221 pages), internal keys "58-in"/"51-nl" on specification pages, every party "Language: English", industry codes without names (missing in the world's ISIC list), fleet table and link artifacts, party-page wording, names that differ between pages, hard-to-read example lists on specification pages | B-01, B-03, B-05, B-06, B-14, B-16 to B-18 | Medium / Low | encyclopedia session (`build_world.py`, site); working session (B-05, B-06 data) |
| SR2-09 | Main site against the Encyclopedia: the ore train missing from Ferrano Rail Cargo's fleet, facts one side leaves out or states differently, Lisavu's infobox naming customs duty as its main tax | B-08, B-15, C-09 | Medium | both, per fact |
| SR2-10 | Flow stories and the Trade page: the reefer's "pays the import tax like every import" against the medicines and carnet exemptions; the medicines introduction leaves out 6 of 14 documents; the Trade page has no contents list and its flow order is unexplained | B-10, B-11, B-12 | Medium | working session (stories); encyclopedia session (Trade page) |
| SR2-11 | The map page outside the common frame ("Map" not "World", no footer); the map sheet page loads the 6.9 MB image inline; coverage pages with unexplained terms, empty rows, unstable anchors | A-07 to A-09 | Low | encyclopedia session (site); working session (map page) |
| SR2-12 | A copy error in UBL 2.5's own definitions (a Debit Note element "applied to the Credit Note"), shown on coverage-details: for `analysis/ubl-findings.md` | A-11 | Low | TC write-up |

## Status

- **SR2-01:** solved in `ae97dc698` (Saltmere Engineering's role "Engineering Firm", its subcontract for Valdara in its text; Saltmere a town on its page; no staff member named on its page).
- **SR2-02:** solved on the working session's side in `dd13e60c4` and `c7646b6ba` (every phrase of A-05, B-04 and B-13 rewritten in-world at the source; makers abroad read "a maker in India / the Netherlands"; the .example reasons on contacts and websites; the country code reason without "user-assigned"); the built site has 0 hits of the project-voice phrases: they can become failures.
- **SR2-09:** partly solved in `dd13e60c4` (the ore train in Ferrano Rail Cargo's fleet; Owner and Staff rows on the party pages); open on the Encyclopedia's side: C-09, B-08's pipeline route and "village of", B-17's fleet formatting.
- **SR2-10:** solved on the working session's side in `ae97dc698` (the reefer "like most imports"; the medicines introduction with all 14 documents); B-12 is the Encyclopedia's.
- **SR2-07 (c), SR2-08 (d, e):** solved in `dd13e60c4` (the country notes describe the current economies, the map's opening card matches; party languages follow their country; ISIC 0124, 7410, 8610, 4630 added, Hafefo 4631 → 4630).
- **SR2-12:** solved (U-A24 in `analysis/ubl-findings.md`).
- **SR2-03:** solved in `46091d39` (the port community by its rule: every flow with a sea leg from or to XBLMP; the reefer's forwarding instructions, export declaration and bill of lading now claim it; no flow keys on the page).
- **SR2-04:** solved in `46091d39` (transport infoboxes once and filled; descriptions keep proper names; villages and localities together; the capitals' climate at the town's own ground, "solar radiation"; the main page titled "The UBL World").
- **SR2-05:** solved in `46091d39` (long dates in infoboxes, weekday dates in the holiday tables).
- **SR2-06:** partly solved in `46091d39` (See also with related articles; every category and the five main pages in the side menu, shown first on a phone; Lisavu's taxes listed). References added (OW038: every article cites the world's own sources, all leading to one sources page for now). Open: uneven sections per article type, disambiguation, false precision, table polish.
- **SR2-07:** partly solved in `46091d39` (About describes the Encyclopedia as it is; releases.html has its own head; history.html without the earlier branches). Open: the map's opening card and the country notes (working session first, then the card).
- **SR2-08:** partly solved in `46091d39` (the party-data fold; the suppliers abroad by name and "a supplier abroad"; counts in the singular and no zero counts; a contents list on the Trade page; the flow's title beside each example on specification pages). Open: B-05 and B-06 (working session's data), B-17 (fleet table, floor and room, `.example` links), B-18 (names; party data).
- **SR2-11:** partly solved in `46091d39` (the map sheet page shows a 1,600 px preview; coverage explains its placements, leaves out zero rows and the empty table, stable anchors; the map page says World, its title follows the pattern, "supply chain" for the commerce kind). Open: the map page's footer and Source link, and whether it follows the device's light theme (A-08 b, d).


## Part A

Checked (part A, site built from main 9916b9d; its footer says 9fd37c8e, the last commit before the review-run commit, which changed no site input): index.html, about.html, world.html (toolbar, opening card, party cards, party list), map-sheet.html, coverage.html, coverage-details.html, releases.html, history.html, the header/nav/footer of all 658 pages; mechanical link-and-anchor check over all 658 HTML pages (lxml, every href/src, every #fragment against the target's ids); the 61 distinct `world.html#NN-xx` hashes opened in Playwright, each card name compared with its party page; page width at 400 px and 1280 px, light and dark, for one page of each kind (21 kinds incl. wiki, note, spec, code lists, example, party); the phone menu; nav/footer/stylesheet/title signatures grouped over all pages; a published-text scan of all pages (internal numbers, real specifications, change words, project words, the two named persons in the Encyclopedia).

Clean: no broken link or anchor anywhere (the 121 `world.html#NN-xx` links on the party and spec pages are not ids but are all resolved by the map's script, each to the right party); no page wider than the viewport at 400 px in either theme; no console errors on the map; the phone menu opens on the main site and the Encyclopedia; every main-site page has the same header, nav, footer, stylesheet and `· The UBL World` title except the map (A-08); the active nav item is right for every page kind; no D/O/OW/MO/WK numbers, no real specification names in published text (the hits are UN/ECE unit codes D61, C62 and item numbers like VI-C180); the Encyclopedia names neither person; the Encyclopedia is linked from About only; the first review's A-01 to A-03, A-06 to A-08, A-09 (width), A-10 and the A-11 link-text point are still solved.

## A-01 Saltmere Engineering is still labelled "Consortium Partner" everywhere, against D28
- **Pages:** world.html (party list and card heading "CONSORTIUM PARTNER"), parties.html, world-27-xb.html ("*Consortium Partner · Bayvarra (XB)*", "See Consortium Partner on the map"), world-spec-transaction-order/-despatch-advice/-forwarding-instructions/-billing.html (party tables).
- **What:** the role label is `"name": "Consortium Partner"` (`world/parties.json`, id 27-xb). Its own "what" text says it installs the benches "as Valdara's subcontractor in the public tender"; it is a consortium member only in the design contest.
- **Why:** D28.3 (worklist-decisions.md, l. 472): "Valdara tenders alone (`SOLE`), with Saltmere Engineering as its subcontractor for lot 2, not as a consortium partner". The label is the one leftover of the SR-13 "consortium partner" fix; it is the most visible place (map card, every table it appears in, including the Order/Despatch/Billing pages, where it is there only as the tender's installer).
- **Fix:** rename the role label in `world/parties.json` to what it is in both flows, e.g. "Engineering Contractor" or "Mast and Site Engineer"; the per-flow roles (subcontractor, group member) are already told in the text. Check the "See … on the map" link text, which uses the role label, not the name (cosmetic, all party pages).
- **Severity:** Medium (stale against a decision; half-true for the contest).

## A-02 The map's opening card sums up the three economies as they were before the new flows
- **Pages:** world.html (opening card, hand-written in `site/world.html` l. 1865); the same picture in `world/countries.json` "note" (shown on country tables and party pages).
- **What:** "Urvania … mines ore, casts benches and makes power. Bayvarra … distributes, builds and runs the port of Lumeport. The island of Lisavu … grows cotton and buys from both." Bayvarra also has the gas field and gas plant (Kelpstone, lpg), the textile mill, the sawmill and furniture maker, the packaging maker, the pharmaceutical wholesaler, the fruit growers' cooperative and the federal agriculture department; Urvania the wood modification plant and the waste recovery; Lisavu the ginnery, the hospital and the fresh produce wholesaler. "builds" for Bayvarra is unclear (the public works department buys, Saltmere installs). countries.json's Bayvarra note still says only "Distribution, retail, the seaport and the airport hub of Lumeport".
- **Why:** the card is one of the three hand-written texts (CLAUDE.md) and the first text most readers see; the first review's C-16 (hand-written map texts do not follow the data) recurs. D47/D48 (medicines, lpg), O137 (reefer), O150 (modification), D34 (wood) added these activities.
- **Fix:** rewrite the sentence from the parties' kinds per country (or generate it from `world/parties.json` categories), e.g. "Urvania … mines ore, casts benches, makes power, modifies timber and recovers waste; Bayvarra … distributes and retails, saws and makes furniture, weaves cotton, produces gas in the north and runs the port and airport of Lumeport; Lisavu … grows and gins cotton and buys food, medicines and goods from both." Bring the three country notes in `countries.json` into line in the same commit.
- **Severity:** Medium (out of date).

## A-03 About: the Encyclopedia is described as just begun, and coverage as a to-do list
- **Pages:** about.html (`site/about.md`).
- **What:** "It is being written; the first articles are there." The Encyclopedia has 191 article pages (countries, towns, villages, rivers, companies, treaties, languages). And: coverage "lists every element that has no example **yet**", which contradicts the next sentence ("some stay out on purpose").
- **Why:** out of date against the built Encyclopedia (open work item 2); the "yet" reads as a plan, which the two-layer rule keeps off the site (SR-12).
- **Fix:** "The Encyclopedia is the world's own reference work: its three countries, their towns, villages and rivers, its companies and institutions and the Trade Accord, each article made from the world's data." and "… lists every element that has no example, with where it would fit."
- **Severity:** Medium.

## A-04 releases.html still opens as the repository README (regression of A-04 / SR-02)
- **Pages:** releases.html.
- **What:** title "The OASIS sample documents: releases", but the H1 is "ubl-examples" (also the first "On this page" entry) and the lead says "A set of validated sample documents for UBL …", then "`xml/` holds …", a link whose text is the repo path "`history/README.md`", and "the scripts in `tools/`".
- **Why:** SR-02 is marked solved and lists "`releases.html` is the README titled 'ubl-examples' about `xml/` only" among its problems; the page now sits under About as the OASIS samples' page, but its head still describes the repository as "a set of validated sample documents", which is neither the project nor the page.
- **Fix:** in `tools/build_site.sh`, give the page its own head (H1 "The OASIS sample documents: releases", one sentence: the samples the OASIS UBL TC published with each UBL 2.x release, rebuilt one document per commit, each release tagged with its directory name on docs.oasis-open.org) and render only the README's release list below it; link text "how the history was built" instead of the file path.
- **Severity:** Medium.

## A-05 Two Dangerous Goods reasons explain a value by the build (two-layer rule), site-wide scan
- **Pages:** 9 example pages, 15 occurrences: example-lpg-02, example-mast-0x (3 pages), example-medicines-0x (5 pages). (Example pages are another part; reported from the site-wide check.)
- **What:** ProperShippingName: "The proper shipping name of the UN entry; **the build checks** that UN number, name and class agree with the Dangerous Goods List."
- **Why:** CLAUDE.md "Two layers": a value is explained by the world, never by the project; `tools/check_published.py` does not catch "the build".
- **Fix:** `tools/build_examples.py` l. 1060: "The proper shipping name of the UN entry, as the Dangerous Goods List gives it for this UN number and class." Keep the check in a code comment; add "the build" (outside the About, coverage and history pages) to the published-text check.
- **Severity:** Medium.

## A-06 history.html still carries "Relation to earlier attempts" (A-11, not solved)
- **Pages:** history.html (from `history/README.md`).
- **What:** "The branches `claude/ubl-samples-hist-3IuwR` and `sample-research` (`official/`) held partial copies …".
- **Why:** repository housekeeping that no reader can use (the first review's A-11; the SR closing note does not mention it). Both branches still exist on origin.
- **Fix:** drop the section from the published page (keep it in the README, or move it under a comment the converter skips).
- **Severity:** Low.

## A-07 The map sheet page still loads the 6.9 MB sheet inline
- **Pages:** map-sheet.html.
- **What:** `<a href="map-sheet.png"><img src="map-sheet.png">` shows the full 4,961 × 3,508 PNG (6,862,501 bytes) scaled down, also on a phone; the same text offers it separately "at full size". The home page already uses a 200 KB preview of the 3D map, but no preview of the sheet exists.
- **Why:** the second half of the first review's A-09 ("ideally a scaled preview … inline, with the full sheet behind the link"); SR-05 closed only the width.
- **Fix:** let `tools/map_sheet.py` (or the build) write a ~1,600 px JPEG/WebP preview next to the sheet and inline that; "about 6 MB" may then say "6.9 MB".
- **Severity:** Low.

## A-08 The map page is the one page outside the common frame
- **Pages:** world.html (`site/world.html`).
- **What:** (a) its nav says "**Map**" where every other page says "World" for the same target; (b) no "Source" link and no site footer (no build line, no "About this project"); (c) title "UBL World Map" where all others are "<page> · The UBL World"; (d) it stays dark when the device is light (every other page follows the device); (e) the filter buttons say "Supply chains" but the card's colour legend and each party card's tag say "commerce" for the same colour (`KIND_NAME`, raw `p.cat`); (f) the footer's "with ISO user-assigned codes" is unexplained shorthand.
- **Why:** SR-02 look and feel (owner, 2026-11-20): "one identity with the map … light and dark following the device"; the nav label is in all other pages "World".
- **Fix:** label the nav item "World" and mark it current; add the Source link; title "The map · The UBL World"; use "Supply chains" (or one word for both) in `KIND_NAME`; footer "… Lisavu (XL): codes from the range ISO 3166 leaves to its users, so they can never be a real country's." (d) can stay if the owner prefers the dark map; then say so in the decisions.
- **Severity:** Low.

## A-09 Coverage pages: unexplained placement words, empty rows and tables, unstable anchors
- **Pages:** coverage.html, coverage-details.html.
- **What:** "Where the missing elements fit": extend 500 · add structure 39 · extend (other) 0 · new example 0 · not reachable 0; the words are explained nowhere and three rows are zero. "Document types without an example" is a heading over an empty table (93 of 93 have one). The details page's anchors carry the counts (`#extend-500`, `#add-structure-39`), so any link to them breaks with the next change. The file names ("rail-12-DebitNote.xml — 56 elements") are not linked to their example pages.
- **Why:** polish; the page is the project layer, so a reader needs the words explained; links that change with counts are fragile.
- **Fix:** one line per placement ("extend: fits in an existing example as a child of an element it already has; add structure: needs a new aggregate in that example"); omit zero rows and empty sections ("Every document type has at least one example."); anchors without counts (`#extend`, `#add-structure`); link each file name to its `example-<flow>-NN-….html`.
- **Severity:** Low.

## A-10 Small naming and repetition points
- **Pages:** wiki/index.html, map-sheet.html, index.html, about.html.
- **What:** (a) the Encyclopedia's main page title is "Encyclopedia · Encyclopedia"; (b) map-sheet.html calls it "the printed map of the **example world**", everywhere else "the UBL World"; (c) the home card says "the OASIS sample documents of **every UBL release**", while history.html says "UBL 1.0 is out of scope" (2.0 to 2.5); (d) "work in progress · not an OASIS publication" stands twice on the home page (hero and footer) and three times on About (Status, footer).
- **Fix:** (a) "Encyclopedia of the UBL World" or "Main page · Encyclopedia"; (b) "of the UBL World"; (c) "of every UBL 2 release"; (d) keep it in the footer only (About's Status section may stay, without the footer repeating it there).
- **Severity:** Low.

## A-11 A copy error in UBL 2.5's own definitions, shown on coverage-details
- **Pages:** coverage-details.html (17 rows).
- **What:** DebitNote/AccountingCost: "The Buyer's accounting code, applied to the **Credit Note** as a whole", and similar rows; the text is from `UBL-Entities-2.5.gc`, not from this project.
- **Why:** not a site error; a candidate for `analysis/ubl-findings.md` (UBL's definitions copied between Credit Note and Debit Note), which does not mention it.
- **Fix:** record it in `analysis/ubl-findings.md`; nothing to change on the site.
- **Severity:** Low.

## Part B

Checked (part B, site built from 9916b9d): examples.html, all 302 example pages (structure, story order, navigation, folds; reasons sampled in every flow, read closely in lpg, medicines, modification, reefer, wood, rail), parties.html and all 61 party pages, world-specifications.html and all 90 specification pages, world-codelists.html with the code-list files and the `codelists/` redirect. Checks run: every internal link and anchor on my pages (clean); width at 400 px with Playwright on all 458 pages (none wider than the screen); "Document N of M" and the previous/next links on every example page against the Trade tables (all consistent); unfilled `{fact:` (none); D/O/OW/MO/C numbers (none, only unit and code values); "dispatch" for the UBL concept (none; "dispatches every train" is rail traffic control); Urvanian/Lisavan own names binbir/kopele (in place); legal form, founding date, employees and website on every party page against the Encyclopedia's infobox (all equal, O279 figures and the SOC/corporation forms in place); screenshots at 400 and 1280 px.

## B-01 Literal Markdown backticks in the party-data fold on 221 example pages
- **Pages:** 221 example pages, e.g. example-lpg-01-Order.html: the fold reads "The party's own data in \`Party\`, as Coastal State Water Company gives it (25 values)", with the backticks shown as characters.
- **Why:** an artifact of the presentation built for SR-24/E-05; the fold is the most visible line of every party block.
- **Fix:** in the fold summary (`tools/build_world.py`, the fold at about line 426) write `<code>Party</code>`, or drop the element name ("The party's own data, as …").
- **Severity:** Medium.

## B-02 The Lumeport port community applies by flow, so the reefer's port documents do not claim it
- **Pages:** world-spec-community-port-lumeport.html ("It applies to the documents of these types in the flows sea, cotton that pass through the port"); example-reefer-05-ExportCustomsDeclaration.html (Bayforth Forwarding to the Customs and Border Service of Bayvarra), example-reefer-07-BillOfLading.html (Tidewell Ocean Lines to Bayforth Forwarding).
- **What:** the reefer is shipped from Lumeport on Tidewell's service, booked by Bayforth and cleared for export at Lumeport, all members. The same documents in the sea flow claim the community (sea/11, sea/14 are on its page), the reefer's do not. The page also prints the internal flow keys "sea, cotton".
- **Why:** SR-18/D-04 (owner, 2026-11-20): the community "applies to what passes through the port (documents of its types … between two parties in Bayvarra, one a member)", a rule, not a list of flows. A spec page that says "pass through the port" while a port document doesn't claim it is wrong.
- **Fix:** derive the community claim from the rule (document type, a member taking part, exchanged in Bayvarra, through the port) for every flow, the reefer included; generate the sentence without flow keys ("… the documents of these types exchanged in Bayvarra for goods passing through the port, with a member taking part").
- **Severity:** High.

## B-03 Internal party keys "58-in" and "51-nl" on the specification pages
- **Pages:** world-spec-transaction-order.html, world-spec-transaction-billing.html, world-spec-profile-ordering.html, world-spec-profile-billing.html: "Order, Quillmoor Pharma Distribution to 58-in", "… to 51-nl"; the role table says "Pharmaceutical Wholesaler → a party outside the world".
- **What:** the Trade page and the example pages name the makers ("Nilavar Biologics (India, …)", "Haarvliet Isotopes"); the specification pages fall back to the internal key because the makers are not in `world/parties.json`.
- **Why:** SR-16 (no role-set numbers or keys shown anywhere); consistency between pages.
- **Fix:** give the spec builder the same name lookup as the example pages (party name from the document), and a plain role ("a maker abroad").
- **Severity:** Medium.

## B-04 Reasons and labels that explain the project instead of the world
- **Pages:** about 120 pages. "a document outside the examples" (42 pages, e.g. tender, contest, wood); "Nilavar Biologics (India, outside the world)" and "Netherlands, a real country outside the world" (Trade page, medicines pages, spec role tables); "the address is fictional, in a real town" (6 medicines pages, appended as "Street of the postal address.; the address is fictional …", a ".;" artifact); "as the world's languages are invented" (59 pages); "a number of the world, not an IMO number" (10 pages).
- **Why:** the two-layer rule (CLAUDE.md, owner 2026-11-20): published text states the world as fact; a value is explained by the world, never by why the project chose it. SR-24 also removed concatenation artifacts.
- **Fix:** in-world wording: "a document the authority holds, not exchanged here" or simply "(cited)"; "a maker in India" / "abroad"; drop "the address is fictional" (or keep it only in the method note); the ISO 639 sentence ends at "reserves for local use (qaa–qtz)"; the vessel number "in its country's register of ships". Fix the ".;" join in `examples_kit.py`.
- **Severity:** Medium.

## B-05 Every party page says "Language: English", against the documents
- **Pages:** all 34 Urvanian and Lisavan party pages, e.g. world-38-xl.html (Lisavu Cotton Farm), world-14-xu.html (Ferrano Rail Cargo), world-59-xu.html (Tostara).
- **What:** the farm writes Lisavan (qal) in all four of its documents; Ferrano Rail Cargo, Serravona, Valdara, Rinova, Fiumella, Ferrano Energy, Ferrano Grid, Montebrio, Tostara and others write Urvanian (qau) in their domestic and customs documents. The party page gives only English.
- **Why:** SR-15/O86: the party page is the party's full self-description, the language included; it must agree with what the party says of itself in its documents.
- **Fix:** list the languages the party writes, by context ("Urvanian at home; English abroad"), computed from the party data the documents use.
- **Severity:** Medium.

## B-06 Industry classes without a name for the new parties; the codes are not in the world's ISIC list
- **Pages:** world-48-xb.html (Fernhollow Studio "7410 (ISIC Rev.4)"), world-50-xl.html (hospital "8610"), world-55-xb.html (Harrowmead "0124"), world-56-xl.html (Hafefo "4631").
- **Why:** SR-15 ("the industry class with its name"); the code list rule (real codes from verified sources). The four codes are missing from `codelists/gc/ISICRev4Code.gc` (39 codes), so the page cannot name them.
- **Fix:** add the four codes with their names from the verified ISIC source to `lists.json`, or make the party-page builder fail when a code has no name.
- **Severity:** Medium.

## B-07 Saltmere Engineering: role name, place and person
- **Pages:** parties.html and world-27-xb.html ("Consortium Partner"), world-spec-transaction-order.html ("Telecom Utility → Consortium Partner"); wiki/saltmere-engineering.html.
- **What:** (1) the role is still "Consortium Partner", though Saltmere is Valdara's subcontractor in the tender, a team member in the contest and the seller in the mast flow; the spec table makes the island's telecom company order batteries from a "Consortium Partner". (2) The party page says Saltmere is "the east-coast village it is named after"; the Encyclopedia calls it "the east-coast town" and lists Saltmere under towns. (3) The party page names a staff member ("a registered architect, Edda Corwin, is on its staff"), which the Encyclopedia leaves out.
- **Why:** SR-13 left the role name for SR-14 (D28: subcontractor); the main site and the Encyclopedia must not contradict each other (brief); the Encyclopedia names no persons, and the party page need not either.
- **Fix:** role "Engineering Firm" (or "Mast Engineer"); "town"; "a registered architect on its staff".
- **Severity:** Medium.

## B-08 Other contradictions between the party pages and the Encyclopedia
- **Pages:** world-14-xu.html: the Fleet table lists the container train FRC 4417 and the road tractor, not the ore train FRC 2208, which the Encyclopedia's Fleet names and the ore flow uses. world-42-xb.html: the fleet entry "Kelpstone–Ferrano gas pipeline"; the Encyclopedia says the pipeline runs about 207 km to Montebrio (near Serravona). Tender/contest reasons ("for the town of Valico Euridice", "Reference letter of the town of Conciaro"): both are villages in the Encyclopedia.
- **Why:** the main site and the Encyclopedia must not contradict each other.
- **Fix:** derive the party-page fleet from the same vehicle list as the Encyclopedia; name the pipeline by its route as the map has it; "village of" (or the council's name) in the tender texts.
- **Severity:** Medium.

## B-09 Bayvarra's country note describes Lumeport only
- **Pages:** all 26 Bayvarran party pages: "Bayvarra: Mainland, in the east, on the estuary. Distribution, retail, the seaport and the airport hub of Lumeport."
- **What:** the note is wrong for Kelpstone Gas (Northern Territory), Gullhaven Tank Haulage, Marrowdale's sawmill, furniture maker and distributor, Harrowmead's fruit growers. The Encyclopedia: "a federal country … the plateau, the dry east and the low north coast. Its capital and port city is Lumeport, at the narrows of the estuary."
- **Why:** SR-17/Q-C-05 fixed the Urvanian and Lisavan notes only; consistency with the Encyclopedia.
- **Fix:** "Mainland, east of Urvania: the plateau, the dry east and the low north coast, with the capital and port of Lumeport on the estuary. Distribution and retail, timber and furniture, fruit, gas, the seaport and the airport hub." (in `world/countries.json`).
- **Severity:** Medium.

## B-10 The island's import consumption tax: "like every import" against two exemptions
- **Pages:** examples.html and the reefer pages: "Food pays the island's import consumption tax like every import"; the medicines intro: the hospital's import is "free of duty and exempt from the import consumption tax"; the carnet intro: samples enter "without its import consumption tax".
- **Why:** the flow stories must agree with each other (O112).
- **Fix:** "Food pays the island's import consumption tax like most imports; the island taxes imported food to encourage its own farms."
- **Severity:** Medium.

## B-11 The medicines introduction leaves out six of its fourteen documents
- **Pages:** examples.html (medicines), repeated on the party pages of Quillmoor and the Customs and Border Service.
- **What:** the table opens with Quillmoor's order to Nilavar Biologics in India (20 April), its invoice and import, and later the order, invoice and import from Haarvliet in the Netherlands; the introduction starts with the hospital's order and never mentions the wholesaler buying abroad, in rupees and euros, or clearing the imports into Bayvarra.
- **Why:** SR-10/O112: the introduction tells the decided and built story, so that the reader sees why each document exists (G9).
- **Fix:** one or two sentences at the start: the wholesaler buys the vaccines and insulin from a maker in India in April for the southern winter, and the generator every week from a maker in the Netherlands, and clears both into Bayvarra.
- **Severity:** Medium.

## B-12 The Trade page has no contents, and the order of its 22 flows is unexplained
- **Pages:** examples.html (about 1,870 lines of text, 22 flows, no in-page links).
- **What:** the newest flows are appended at the end (energy, reefer, lpg, medicines), modification stands between wood and furniture, and nothing groups them (goods chain, public procurement, utilities and energy, island supply). A reader has to scroll to find a flow; the anchors `#flow-…` exist but nothing lists them.
- **Why:** SR-02 named the missing contents list and the unexplained order; the redesign did not add a contents list. Look and feel: the page is now three times longer than at the first review.
- **Fix:** a short contents list at the top (flow title, route, number of documents), linking `#flow-…`, grouped or ordered along the goods chain.
- **Severity:** Medium.

## B-13 Real-world comparisons and project voice in the flow introductions
- **Pages:** examples.html and the party pages that repeat the introductions: rail "the consignment note follows the Accord's uniform rules for international carriage by rail, modelled on the CIM" (11 pages) and "…in a debit note to its goods invoice: the world's debit notes" (10 pages); world-57-xb.html "the country's plant protection organisation under the IPPC".
- **Why:** SR-10 removed real-world comparisons from the introductions (the EU, the ICC on CIF); "the world's debit notes" speaks about the example set, not the world (two layers).
- **Fix:** drop "modelled on the CIM" and ": the world's debit notes"; "the country's plant protection organisation, which inspects …".
- **Severity:** Low.

## B-14 Party page template wording
- **Pages:** world-22-xl.html, world-23-xu.html, world-28-xb.html, world-29-xb.html ("it sends 0 and receives 0 documents"); world-16-xl.html, world-2-xb.html and others ("named in 1 documents", "receives 1 documents"); banks' "How UBL helps": Bank of Selanu "The buyer's bank sends the payment abroad", Crevalto "The seller's bank receives payments from many countries".
- **Why:** SR-14 (the banks told by the accounts they hold, not as one chain's seller's or buyer's bank; no empty sections).
- **Fix:** singular/plural and leave out zero counts ("It is named in 7 documents between other parties"); bank texts by role in the world ("A bank holds the accounts of …; the invoice's payee account and payment reference let it match the incoming payments").
- **Severity:** Low.

## B-15 Facts in the Encyclopedia that the party pages leave out or state differently
- **Pages:** public bodies' party pages (customs services, Codana, Public Works Department, Trade Accord Council, Maritime Administration, Review Board): no staff, though OW031 decided them and the Encyclopedia prints them in its text. world-16-xl.html and world-35-xl.html: the Port of Selanu and Selanu Telecom are "Island limited company" while the Encyclopedia says "Owner: the island's state"; the Bayvarran state-owned companies were given the SOC form under O279 (2).
- **Why:** SR-15 (the identity table); O279 (2): "state 'state-owned company limited by shares' where that is meant".
- **Fix:** an Employees row for public bodies (about N staff); either an island form for state-owned companies or an "Owner" row on the party page, as in the Encyclopedia.
- **Severity:** Low.

## B-16 Specification pages: example lists hard to read
- **Pages:** world-spec-transaction-order.html and the other transaction and profile pages: "Examples that claim it" is unordered, and repeats indistinguishable entries ("Order, Brightmarket Stores to Brackenmere Furniture" twice; "Order, Lumeway Distribution to Valdara Industries" twice).
- **Why:** polish (the lists became long with the new flows).
- **Fix:** group by flow in story order and add the date or the flow's title to each entry.
- **Severity:** Low.

## B-17 Fleet table and link artifacts
- **Pages:** world-14-xu.html "Container train Ferrano–Marrowdale | Train | train FRC 4417"; world-42-xb.html "Kelpstone–Ferrano gas pipeline | pipeline |" (lower case, no registration, not a vehicle); the bank addresses print a bare "3 301" line (floor and room) on world-22-xl, 23-xu, 25-xb; fictional web addresses (`https://www.valdara.example/terms`, `https://ap.lumeway.example/as4` …) are clickable links on example pages and lead nowhere.
- **Why:** polish; a link that leads nowhere looks broken.
- **Fix:** registration "FRC 4417"; move the pipeline to an "Installations" line or leave it out of the fleet; print floor and room as "Floor 3, Room 301" on party pages; show `.example` addresses as text, not links.
- **Severity:** Low.

## B-18 Names that differ between pages
- **Pages:** parties.html and world-55-xb.html role "Fruit Packers' Cooperative" vs the party "Harrowmead Fruit Growers" and the reefer intro's "fruit growers' cooperative"; the reefer intro's "the plant health service of Bayvarra's Department of Agriculture" vs the party "Federal Department of Agriculture of Bayvarra" (whose page calls it the Plant Health Service); medicines reasons "Postal code in the format of Netherlands".
- **Why:** consistency.
- **Fix:** role "Fruit Growers' Cooperative"; "the Plant Health Service of Bayvarra's federal Department of Agriculture"; "of the Netherlands".
- **Severity:** Low.

## Part C

Checked: all 191 pages under wiki/ of site-9916b9d (index, 14 categories, every article type). Checks run: a link and anchor check over every href/src, including the map's #party anchors, which world.html resolves in JS (all resolve; no orphan pages); Playwright at 400 px on every page (no page wider than the screen; only the climate, districts and rivers tables scroll inside their own box; every image loads); screenshots at 400/1280 px, light and dark; a text scan of every <main> (project numbers, real specifications, persons, business-document words, change words, template leftovers, doubled infobox rows, false precision); a read of the index, categories, countries, the Accord, the capitals, towns, villages, localities, rivers, Rivers and watersheds, landmarks, transport, languages, currencies, product and a sample of companies. Passed: no Wikipedia name, logo or design; no D/O/OW numbers; no Peppol/CEN/EN 16931; no persons; no lists of business documents (only descriptions of how the work is done); the dark theme follows prefers-color-scheme, as the main site does.

## C-01 · Transport infoboxes: every row twice, and template placeholders printed
- Pages: all 7 transport articles: ore-line, port-line, wool-line, ferranomarrowdale-line, kelpstoneferrano-gas-pipeline, lumeportselanu-shipping-service, lumeportselanu-air-cargo-route.
- What: the infobox repeats its facts: "Length about 166 km · Country Urvania · Length about 166 km · Country Urvania" (Ore line), "Country Bayvarra" twice (Port line, Wool line), Length/Countries/Opened twice (pipeline), Distance/Passage/Since twice (shipping). The air route's second copy is an unfilled template: "Distance about {flight_km} km · Timetable {flight_east} east, {flight_west} west".
- Why: wrong output on the page; the build's published-text check misses braces.
- Fix: in tools/build_wiki.py emit the transport facts once (the generic rows and the route rows seem to be added on top of each other); have the wiki check reject `{…}` in published text.
- Severity: High

## C-02 · Short descriptions lower-cased in the towns' company lists
- Pages: ferrano (8 entries), lumeport (5), marrowdale (2), selanu (1).
- What: "Environment Agency of Urvania, urvania's environment agency…", "Fiumella Barges, urvanian river barge operator at Ferrano", "Lumeway Distribution, bayvarran wholesale distributor in Marrowdale", "lisavu's department of agriculture".
- Why: proper names and adjectives must keep their capital letter; the generator lower-cases the first letter of every short description.
- Fix: lower-case the first letter only when the first word is not a proper noun or adjective, or use the description as it stands.
- Severity: Medium

## C-03 · ISO dates in an encyclopedia that writes "15 April"
- Pages: every company infobox (e.g. "Founded 1903-05-20" on bank-of-lumeport, "1962-04-12" on valdara-industries; about 40 pages) and the holiday tables of urvania, bayvarra and lisavu ("2026-01-01 New Year and Accord Day", with the column header just "2026").
- What: the infoboxes of towns and timelines write "4 September 1840" and "8 November 1999", and the article English says the three countries write "dates as 15 April or Monday 11 May".
- Why: the owner's decision on the Englishes (OW028), as the article English itself states; inconsistent with the encyclopedia's other dates.
- Fix: format dates as "20 May 1903"; in the holiday tables write "Thursday 1 January" and name the column "Date (2026)".
- Severity: Medium

## C-04 · "ISO 3166-1, user-assigned" in the country infoboxes
- Pages: urvania, bayvarra, lisavu ("Country code XU (ISO 3166-1, user-assigned)").
- What: "user-assigned" gives the project's reason for the code (a code range kept free for private use), not a fact of the world.
- Why: the two-layer rule (CLAUDE.md; SR-09): published world text states the world as fact and does not say why the project chose a value.
- Fix: "Country code: XU".
- Severity: Medium

## C-05 · Capitals' climate tables: port towns 120 m above the sea; "Sunshine" in kWh
- Pages: lumeport ("Climate data for Lumeport (about 120 m above the sea)"), selanu (same), ferrano (200 m).
- What: Lumeport stands "on the shore of the bay", and Selanu on its bay with the wharf, yet both are given 120 m, and their temperatures are lowered by about 0.8 °C because of it. tools/build_wiki.py `town_climate` takes the mean of the four terrain corners of the town's square, which includes the hills behind. The row "Sunshine (kWh/m² a day)" is solar radiation, not sunshine (which is given in hours).
- Why: spot check against the articles' own geography (OW034: "corrected for the town's height").
- Fix: use the town's own height (from the place list or the lowest corner on the coast), or say "the town (at sea level)"; rename the row "Solar radiation (kWh/m² a day)".
- Severity: Medium

## C-06 · Decided conventions not followed everywhere: no References, See also patchy
- Pages: all articles; lumeport-trade-accord, the 7 transport articles, the 3 languages, the 3 currencies, park-bench-serra-180, the 3 landmarks and rivers-and-watersheds have no See also; port-line has no section at all (lead and infobox only).
- What: no article has a References section. Where See also exists on countries, towns and villages, it holds only "The map of the world · the printed map sheet" (the same for every place, not focused on it); companies get only "… on the map".
- Why: CLAUDE.md open work item 2: "short description, infobox, lead, contents, sections, see also, references, categories".
- Fix: decide with the owner what References means in the world (for example in-world sources such as the business registry of the Bayvarra Information Service, Codana's register, the national statistics, the Accord's text), or record that it is dropped. Give every article a See also with related articles (the Accord: its council and the currencies; currencies: the other two and the Accord; landmarks: Selanu and the rivers). Move the main-site links into a separate "External links" line.
- Severity: Medium

## C-07 · Navigation: side menu incomplete, main-site links incomplete, menu last on a phone
- Pages: every wiki page.
- What: the Encyclopedia menu has Main page, Countries, Towns, Rivers, Companies and institutions, Treaties; the index has 11 sections (Villages, Landmarks, Transport, Languages, Currencies and Products are missing from the menu, although their category pages exist). The "The UBL World" block has "The map, Trade, Parties", without Rules and About (the main nav is World · Trade · Parties · Rules · About), and calls World "The map". At 400 px the menu moves below the article (on ferrano that means after about 5,000 px), and the header offers only "Encyclopedia" and "The UBL World ↗" (the arrow suggests an external site, though the link opens in the same tab).
- Why: the decided main navigation (CLAUDE.md, owner 2026-11-20); navigation on a phone.
- Fix: list every category in the menu; mirror the main nav's five items with its labels; on narrow screens add a compact row of category links under the header (or a <details> menu at the top).
- Severity: Medium

## C-08 · Localities filed as villages
- Pages: gullhaven, euridice-crossing, valico-euridice; index, category-villages.
- What: the short description is "Locality in Bayvarra", but the only category and the index heading are "Villages". Gullhaven is "a fishing village" in its own lead, while Euridice Crossing is "the customs post, its truck park and a few houses".
- Why: the article type and its category contradict each other.
- Fix: a category "Villages and localities" (and index heading), or call them villages where they are.
- Severity: Medium

## C-09 · Lisavu's infobox names the wrong main tax
- Pages: lisavu (infobox "Tax: Customs duty").
- What: the article says "Lisavu has no general sales tax: customs collects an import consumption tax on every import, whatever its origin, and a duty on goods from outside the Accord", and the Accord article says the island stopped charging duty on its partners' goods.
- Why: world data (countries.json tax schemes; codelist decisions on the island's import consumption tax).
- Fix: "Tax: Import consumption tax (and duty on goods from outside the Accord)".
- Severity: Medium

## C-10 · The About page describes an Encyclopedia that has just begun
- Pages: about.html, section "The Encyclopedia" (the Encyclopedia's only way in).
- What: "It is being written; the first articles are there." There are now 177 articles; the list "its countries, towns, companies and institutions" leaves out villages, rivers, landmarks, transport, languages and currencies.
- Why: out of date (overlaps with part A).
- Fix: describe what it covers now, without a progress statement.
- Severity: Medium

## C-11 · False precision
- Pages: country infoboxes (urvania "Population 1,199,920", bayvarra "800,010", lisavu "60,010", against the leads' "about 1.2 million / 800,000 / 60,000"); the leads of 22 company articles ("employs about 3,083 people" valdara-industries, "about 2,313" bank-of-lumeport, "about 987" serravona-mining …); runmek and rivers-and-watersheds "rises … at about 1,511 m" against urvania "about 1,510 m".
- What: "about" placed before an exact figure; the population sums of the place list ending in …010 look made up.
- Fix: round in the infobox (1.2 million) and the leads ("about 3,100 people"), or drop "about" where the exact staff number is meant; round heights to 10 m everywhere.
- Severity: Low

## C-12 · Timelines uneven
- Pages: 21 of 57 company articles have a Timeline (missing on e.g. lumeport-textile-mill, port-of-lumeport, kelaro-air-cargo, marrowdale-sawmill, the customs services); none on countries or towns (OW032 lists them still to do); on valdara-industries the timeline repeats the History paragraph almost word for word.
- Why: OW032/OW033; consistency between articles of the same type.
- Fix: a timeline wherever an article has three or more dated events; keep the prose for the story and the timeline for the dates.
- Severity: Low

## C-13 · Water maps and river locator maps
- Pages: rivers-and-watersheds, the 40 river articles.
- What: at 400 px the labels of the water maps cannot be read, and the images are not linked to their full size (on desktop either). The locator maps show unlabelled town dots and have no caption. The infobox "Mouth: the sea" (most rivers) says nothing about where the river meets the sea; "Source: about 1,511 m" gives only a height.
- Fix: wrap each map in a link to the PNG; add a caption ("The Runmek and its basin; dots: Ferrano, Forte Euridice, Lumeport"); "Mouth: the bay at Lumeport / the north coast"; "Source: the Mukrir, about 1,510 m".
- Severity: Low

## C-14 · Titles, casing and sorting
- Pages: the-litakima (h1 and caption "the Litakima"; it is listed in lower case and sorted last in the index and in category-landmarks); index.html (<title> "Encyclopedia · Encyclopedia"); country leads and infoboxes ("Its currency is the Ferra (XUF)") against "the ferra, the lume and the coral" in the Accord and currency articles.
- Fix: title "Litakima", with "the Litakima" in running text; index title "Encyclopedia of Urvania, Bayvarra and Lisavu"; lower-case currency names in running text everywhere.
- Severity: Low

## C-15 · Disambiguation and slugs
- Pages: 10 rivers titled "Brina (river)", "Bruna (river)", "Canneto (river)" … although no other article has the same name, while Gemella, Lontra, Nevola and others carry none; slugs ferranomarrowdale-line, kelpstoneferrano-gas-pipeline, lumeportselanu-shipping-service (the dash dropped).
- Fix: add "(river)" only on a real clash (Tapetu, beside Mount Tapetu, is arguably not one either); turn the en dash into a hyphen in slugs.
- Severity: Low

## C-16 · Uneven section structure of the same article type
- Pages: selanu, marrowdale and larkmouth have no Geography section (ferrano and lumeport do); only urvania has a Languages section (Bayvarra and Lisavu say nothing about their languages beyond the infobox); village Histories are one sentence ("It was founded by English settlers in the 1860s.", bollworth); bollworth's Lisavan name Pakesa is only in the infobox, while ferrano gives "(Urvanian Ruldraz)" in the lead.
- Fix: the same section set per type, with the second name in the lead for every place that has one.
- Severity: Low

## C-17 · Small wording slips (spot checks)
- marrowdale: "since 1899 it is Upland State of Bayvarra" → "it has been".
- lumeport: "laid out the town as the colony's seat [1841] … Lumeport took over from Larkmouth as capital in 1852" reads as a contradiction; say "as a fortified station" or explain seat against capital.
- ore-line: "Its river bridge crosses the river's deep valley" names no river.
- lumeportselanu-air-cargo-route: short description "between Lumeport and Lisavu" mixes a town and a country (the shipping service does the same); "Lumeport and Selanu".
- Severity: Low

## C-18 · Tables at phone width
- Pages: rivers-and-watersheds (rivers table), ferrano, lumeport, selanu (climate tables).
- What: "53,248 km²" breaks between number and unit; the climate tables scroll sideways without a visible cue (the first column scrolls away too).
- Fix: `white-space:nowrap` on number cells; a sticky first column, or a hint, for the climate table.
- Severity: Low
