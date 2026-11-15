# Decisions for the owner

These are the questions only the owner can answer before the causes of `analysis/worklist.md` can be fixed. There are **46 decisions**; 1960 of the 3348 findings wait on one of them, in 45 causes (plus the bulk confirmation D46). The 21 "needs decision" consistency findings, the "Cannot be told from the documents" questions of the six topic files and the per-example "yes" findings are folded in by cause: a cause with many "yes" findings is one decision, and the flow stories are one decision per flow. Where the world story (`note/src/03-world.md`) or an earlier decision (`analysis/codelist-decisions.md`) already says something, it is quoted; several findings contradict them, and those conflicts are the first thing to settle.

The decisions are grouped; a group is meant to be taken together. The world-level groups come first, ordered by the number of findings they unblock, and within a group the decisions are ordered the same way. The flow decisions come after them although some are large (the tender alone holds 210 findings), because they build on the world rules (payment terms, tax, customs, the goods chain); the bulk confirmation is last.

## Language tags and names (393 findings)

### D1 · Does `Language/LocaleCode` stay `en`, or is it dropped (or given a real locale)?
- Why it matters: Cause C45 `Language/LocaleCode` = `en`; 213 findings (0 marked "yes").
- What the documents say now: All 213 files with a full party description carry `LocaleCode` `en` with listID ISO 639. The merge decisions rate it Medium, "no decision": "drop LocaleCode; a locale such as `en-XB` from a locale list is the option". `analysis/codelist-decisions.md` 6b says the opposite: "Coded elements (LocaleCode, Language/ID, DefaultLanguageCode) stay plain `en`, because ISO 639 has no region."
- Options:
  - a) Drop `LocaleCode` from every party description (one change in `party()`, 213 files). Costs nothing; a locale is not needed by any document.
  - b) Give a real locale (`en-XB`, `en-XU`, `en-XL`) from a world locale list (new list, CVA context, 213 files).
  - c) Keep `en` and record in the reviews that decision 6b stands (the 213 findings are then dismissed with that reason).
- Recommendation: a): UBL defines LocaleCode as a locale, `en` is a language, and no document uses the locale; it ends 213 Medium findings with one change. Revise 6b accordingly.
- Related: D2 (the same rule 6b)
- **Decided (owner, 2026-11-15): b).** `LocaleCode` carries the regional English of the party's country: `en-XU`, `en-XB` or `en-XL`, from a world locale list. `Language/ID` stays plain `en`. Decision 6b in `analysis/codelist-decisions.md` is revised for `LocaleCode` only.
- **What it means for the world:** English is not one language across the three countries. Each country's English was shaped by its history and by the language spoken there before, and has drifted from standard English; the locale names that variety. Urvanian English carries the Italian place and street names the British kept, and stands beside Urvanian. Bayvarran English is the settlers' English and the working language between the three countries. Lisavan English stands beside Lisavan on the island. A party whose language is English states which English it writes.
- **To work out when it is implemented:** the world locale list (three codes, with descriptions that say what marks each variety); whether a party whose first language is Urvanian or Lisavan also states its English locale (it writes English too); the paragraph for `note/src/03-world.md`; a few visible traits of each variety for the backstory (spelling, loan words, date and number habits), so that the difference is more than a tag.

### D2 · Which rule tags English text: the issuer's country (as now), the party's country, or plain `en`; and do Urvania's Italian names count as English?
- Why it matters: Cause C46 English renderings tagged with the issuer's country, Italian names tagged as English, legal form untagged; 179 findings (127 marked "yes").
- What the documents say now: The English rendering of a party's address and names is tagged after the issuer of the document in 277 of 277 rows, so the same Urvanian address is `en-XB` in Bayvarran documents and `en-XU` in its own; the legal form is untagged in one rendering. The merge decisions: Low, "one rule for the language tag". `analysis/codelist-decisions.md` 6b: "(a) Every sender tags its English texts with its own region". `note/src/03-world.md`: "the inherited Italian names count as English" and "Each sender tags its English texts with its own country as the region".
- Options:
  - a) Keep 6b (issuer's region) and dismiss the 179 findings with that reason; tag the legal form like the other renderings (small change).
  - b) Tag the English rendering of a party's master data with the party's country, free text with the issuer's (changes `language_tag()` and `city_names()`; 123 files).
  - c) Plain `en` everywhere (drops the private-use regions; contradicts 6b and the story).
- Recommendation: b): a party's address is master data and should read the same in every document; free text still shows the issuer's English. Keep the Italian names as English (the story says so) and tag the legal form.
- Related: D1, D3

### D3 · What is Lisavu's capital called in English: Selanu or Port Wrenfield?
- Why it matters: Cause C59 Lisavu's capital: "Port Wrenfield" in English addresses, "Selanu" in every other English text; 1 finding (1 marked "yes").
- What the documents say now: The English addresses of the 12 Lisavan parties say "Port Wrenfield"; about 140 party names, every place name and the free texts say "Selanu" (parties#F1). `note/src/03-world.md`: "Selanu is also *Port Wrenfield*, a name checked not to be a real place" and "An address gives both, Lisavan first."
- Options:
  - a) "Selanu" also as the English name (drop the exonym; changes countries.json and the story).
  - b) Keep Port Wrenfield in addresses and add one note in a document (e.g. the business card) that it is Selanu's English name.
  - c) Use Port Wrenfield in all English free texts and place names (about 30 texts; party names stay).
- Recommendation: b): it keeps the story and needs one sentence; English readers of an address then know both names.
- Related: D2

## Party master data and signatures (332 findings)

### D4 · Give each party its own founding date and a size that fits it (including the farm's registration expiry)?
- Why it matters: Causes C60 Default founding date 1996-01-01 and size classes that do not fit the parties, C63 Lisavu Cotton Farm: address lines that repeat the structured address, and a yearly expiring registration; 192 findings (184 marked "yes").
- What the documents say now: 25 companies have `founded` "1996-01-01" in `world/parties.json`, with headcounts and turnovers that make them all SMALL (ports, the state water company, the telecom operator, the rail operator, the sawmill with 85 stated employees); Valdara is LARGE with 180 persons and 9.2 million lume capability (conditions#F12, parties#F2). The farm's register entry expires yearly. The size follows from headcount and turnover by the Trade Accord's limits (codelist-decisions Q16; `note/src/03-world.md`).
- Options:
  - a) Per party a founding date, headcount and turnover that fit what it is (25 parties in parties.json; the size then follows; about 170 files change).
  - b) Drop `RegistrationDate` and `EntitySizeCode` where no document uses them (fewer values, but tender and contest use size and headcount).
  - c) Keep the data and dismiss the findings (the 1996 date is then a stated default).
- Recommendation: a), with Valdara MEDIUM unless a turnover above 50 million lume is wanted, and the sawmill MEDIUM (it states 85 persons); keep the farm's yearly registration only if the island's register really expires (then say so).
- Related: D8

### D5 · Who allocates the standard item identifier, and may world item numbers look like valid GTIN-12s?
- Why it matters: Cause C61 World item numbers that are valid GTIN-12s; Valdara's items under Lumeway's GS1 prefix; 76 findings (76 marked "yes").
- What the documents say now: Valdara's documents identify the bench and frame by the world item numbers (`771020000027`, `771020000034`); Lumeway's by GTINs in its own prefix 9520610, with the world number as additional ID (items#F2). The world item numbers are valid GTIN-12s in a real range (76 findings, all "yes"). `note/src/03-world.md`: "where the maker has no GTIN, the GS1 distributor gives the item one of its own, as GS1 allows a wholesaler or importer to do". `analysis/codelist-decisions.md` ID-Q4: "item numbers with a non-company GS1 prefix (world scheme, check digit kept)".
- Options:
  - a) Keep both conventions as the story states (dismiss the GTIN-prefix findings) and change only the world item numbers so that they cannot be read as real GTIN-12 (e.g. a check character, or a 952 prefix as for the GS1 parties).
  - b) The world item number as the one standard ID everywhere, Lumeway's GTIN as additional (items#F2 option a).
  - c) Keep everything and record the reason in the reviews.
- Recommendation: a): the distributor-assigned GTIN is a stated, real GS1 practice; the only real risk is numbers that pass as real GTINs.
- Related: D10, D11

### D6 · What must a Signature carry, and where is one kept?
- Why it matters: Cause C49 Signature aggregates with only an ID and a signatory; 38 findings (36 marked "yes").
- What the documents say now: 137 of 147 Signature aggregates have only an ID and a signatory (merge decisions: Low, yes); some IDs carry the flow name (C13).
- Options:
  - a) Keep signatures only where the document is signed in the story, with method, time and an attached or referenced signature value.
  - b) Drop all Signature aggregates except the few full ones (coverage of Signature elements must be checked).
  - c) Keep them as they are and dismiss.
- Recommendation: a): it keeps coverage where a signature has a business reason (bills of lading, certificates, the agreement) and removes fillers (IND5/IND6).
- Related: none

### D7 · Is the garden set sold under the store's own label or under Brackenmere's brand?
- Why it matters: Cause C62 The maker's brand on the store's own-line garden set; 12 findings (12 marked "yes").
- What the documents say now: Twelve furniture documents give the store's own-line set Brackenmere's brand (all "yes").
- Options:
  - a) Store's own label: the brand becomes the store's line name in items.json.
  - b) Maker's brand: the story drops "own line".
- Recommendation: a): the story (an own-line set made by the furniture maker) is the reason for the flow.
- Related: none

### D8 · Which industry class does each party get where the class leaves out what it does?
- Why it matters: Cause C64 Industry classes that leave out what the party does; 9 findings (5 marked "yes").
- What the documents say now: Selanu Telecom (mast operator) is 6110 wired telecommunications; Ferrano Energy and Ferrano Grid are 3510 (electricity) but also trade and carry gas.
- Options:
  - a) Selanu Telecom 6120 (wireless); Ferrano Energy 3520 or two classes if the element allows only one: the main activity.
  - b) Keep and dismiss.
- Recommendation: a), main activity per party (ISIC allows one main class).
- Related: D4

### D9 · In a debit note issued by the buyer, is the buyer the accounting supplier?
- Why it matters: Cause C66 Debit notes with accounting supplier and customer reversed; 5 findings (5 marked "yes").
- What the documents say now: All three debit notes (furniture/14, sea/28, tender/34) carry the issuer as accounting customer and the debited party as accounting supplier; their numbers and language tags name the real issuer. Merge decisions: High, yes, "probably one pattern in the generator". The parties come from `world/documents.json`.
- Options:
  - a) The issuer (creditor) is the accounting supplier: swap the roles in documents.json (3 documents, plus tender/35 and 36 then stand).
  - b) Replace the buyer's debit notes by self-billed credit notes or supplier credit notes.
- Recommendation: a): it matches UBL's definitions and all reviews; one data change.
- Related: none

## Item data in documents (128 findings)

### D10 · Does `FullnessIndicationCode` CRADLETOGATE stay, and which lifecycle stage does a cradle-to-gate footprint get?
- Why it matters: Cause C47 `FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING for a cradle-to-gate footprint; 74 findings (0 marked "yes").
- What the documents say now: The bench footprint carries `FullnessIndicationCode` CRADLETOGATE and `LifecycleStageCode` MANUFACTURING (74 findings, Medium, no). `analysis/codelist-decisions.md` Q21: "LifecycleStageCode uses a regional list with the UBL definition's stages … FullnessIndicationCode gets a consistent separate list (CRADLETOGATE …)." The reviews read FullnessIndicationCode as being about full transport equipment.
- Options:
  - a) Drop FullnessIndicationCode from the footprint (revise Q21; note for the OASIS TC write-up); the stage covers A1–A3 (SOURCING + MANUFACTURING, or a list code for cradle-to-gate).
  - b) Keep Q21 and dismiss the findings with its reason.
- Recommendation: a): the UBL 2.5 definition of FullnessIndicationCode decides (semantic conformance, §7.2); record the ambiguity as a finding for the TC.
- Related: D11

### D11 · Do the maker's item facts travel into every document, or only into the documents that use them?
- Why it matters: Cause C48 Catalogue and product-passport data copied into business documents; 41 findings (3 marked "yes").
- What the documents say now: The full bench description (properties, footprint, warranty, keywords, catalogue data) stands in orders, despatch advices, invoices, customs declarations and till receipts (merge decisions: Low, no). `note/src/03-world.md`: "The maker's facts travel with the item wherever it appears: brand and model, properties …, certificates, the carbon footprint and the circularity profile."
- Options:
  - a) Profile per document type: catalogues and product information carry everything; orders, invoices and receipts the identification, name and the facts the line needs; customs declarations classification, origin and weights (change in `item()`; about 40 files; revise the story sentence).
  - b) Keep the story rule and dismiss the findings.
- Recommendation: a): copying everything is the same filler problem as party master data (C01) and hides what a document really needs.
- Related: D10, D5

### D12 · What is the pack of a cotton bale?
- Why it matters: Cause C65 Bale weight of about 227 kg as `PackSizeNumeric`; 7 findings (7 marked "yes").
- What the documents say now: Seven cotton documents give `PackQuantity` 1 and `PackSizeNumeric` 227 for a bale "of about 227 kg".
- Options:
  - a) No pack size; the bale count as package quantity and the weight as weight.
  - b) Pack size 1 (one bale per package).
- Recommendation: a): the weight is already given; the pack size element counts units.
- Related: none

### D13 · Is the spare side frame classified as a cast article (7325.99) or as a part of a seat (9401.99)?
- Why it matters: Cause C67 Side frame classified HS 7325.99 instead of a part of a seat; 5 findings (1 marked "yes").
- What the documents say now: The frame is HS 732599 in every document (merge decisions: Medium, no, "9401.99"). `analysis/codelist-decisions.md` P5 confirmed "7325.99 → 42999 Metal goods n.e.c. (bench casting)" against the UNSD correspondence.
- Options:
  - a) 9401.99 with CPC and the Urvanian subheading adjusted (items.json; the frame stands in 22 files, by the merge decisions' count).
  - b) Keep 7325.99 (P5) and dismiss the 5 findings with the reason that the casting is sold as a casting.
- Recommendation: a), as the merge decisions and five reviews prefer, because the frame is sold as a spare part of the bench; P5 checked only the CPC correspondence of the code it was given, so revise it with the HS heading.
- Related: none

### D14 · Should the price chain manufacturer → distributor → public buyer be made plausible?
- Why it matters: Cause C68 Valdara's distributor price equals its public contract price; Lumeway's revised frame price is below cost; 1 finding (1 marked "yes").
- What the documents say now: Valdara sells the bench to Lumeway at 49900 XUF (499 XBL) and to the public works department at the same price; Lumeway's revised frame price (58 XBL) is below its cost of 59.80 (conditions#F11).
- Options:
  - a) A distributor discount on Valdara's list in road and rail.
  - b) A reason in tender/25 and retail/03.
  - c) Leave it.
- Recommendation: a), as conditions#F11 prefers.
- Related: none

## Customs and tax (57 findings)

### D15 · Which tax category do Lisavan sales of goods get, and does Lisavu's scheme get an identifier?
- Why it matters: Cause C50 Tax category O for goods, 0 % on O, and Lisavu's tax scheme without ID; 29 findings (15 marked "yes").
- What the documents say now: Lisavan goods are taxed with category O "Services outside scope of tax", with a 0 % rate; the scheme is named "No general sales tax" without ID (merge decisions: Medium, yes).
- Options:
  - a) Category O stays (UNCL 5305 O is "Services outside scope of tax"; the world list adds a description that it covers any supply outside a tax) and no percent on O; the scheme without ID stays.
  - b) Category E with a reason "No sales tax in Lisavu" under a named scheme.
  - c) No TaxTotal at all on Lisavan documents.
- Recommendation: c) for documents with no tax at all, a) where a withholding or levy is stated on the same document; drop the 0 % everywhere.
- Related: D18

### D16 · On which basis do the three countries value imports for customs?
- Why it matters: Cause C52 Customs value on a different basis in each flow; 12 findings (9 marked "yes").
- What the documents say now: Bayvarra values on four bases (freight added in plastics, FCA/FOB without freight in road and cotton, a delivered price in tender); document-level charges are never included; the sea bill of lading declares a CIF value (conditions#F5; merge decisions: "the world's valuation rule is undecided").
- Options:
  - a) One Trade Accord rule: value at the importing border (CIF-type), charges that are part of the price included (plastics/09 is the model; road/10, cotton/15, sea/19, tender/31, wood/07 change).
  - b) FOB-type value at the exporting border for all.
  - c) Per country, stated in each declaration.
- Recommendation: a), as conditions#F5 prefers; it is the common practice (WTO valuation, own knowledge of the reviews).
- Related: D18

### D17 · When does Bayvarra withhold tax on non-residents' services and require a tax representative, and how does Urvania treat a foreign public body?
- Why it matters: Cause C54 Bayvarran withholding tax and tax representative only in the tender, and Urvania's "service to a business abroad" for a public body; 10 findings (8 marked "yes").
- What the documents say now: Only the tender invoices withhold 10 % and name a tax representative; the notices state exemption PUBLIC; Urvania's SVCABROAD ("to a business") is used for the public works department (conditions#F4, #F8). `note/src/03-world.md`: "A public body in Bayvarra withholds 10 % of the price of a service from a business not established there and pays it to the state; such a supplier names a tax representative in Bayvarra."
- Options:
  - a) Keep the story rule (public bodies only): state it in the scheme name or a note, give the representative a registration, and widen SVCABROAD to "a customer established outside Urvania"; road/14 stays.
  - b) Drop the withholding and the representative (conditions#F4 option c; changes the story).
- Recommendation: a): the story already states it; conditions#F4's preferred (c) would contradict `note/src/03-world.md`.
- Related: none

### D18 · Are imports between Accord members duty-free with a preference claim, and what import taxes are due?
- Why it matters: Cause C57 Duties, import taxes and Trade Accord preference stated nowhere; 6 findings (6 marked "yes").
- What the documents say now: Every import says "Duties paid by the importer's account at customs." without duty; preference is claimed once (conditions#F6). `note/src/03-world.md`: "Lisavu (XL) has no general sales tax. Customs collects a customs duty and an import consumption tax when goods enter the island." `analysis/codelist-decisions.md` Q24: "The Accord is a free trade area, not a customs union, so tariffs, rates and exemptions stay national."
- Options:
  - a) Accord-origin goods duty-free with a preference claim (criterion, proof of origin) in every import; import VAT in Urvania stated; Lisavu's import consumption tax stated in the Lisavan imports (sea/19, carnet claim).
  - b) Duties due: amount, rate and tax category in each import.
  - c) Leave silent and drop "Duties paid".
- Recommendation: a): a free trade area with certificates of preferential origin (road/07) implies preference; Lisavu's import tax is already in the story.
- Related: D16, D15

## Geography and the goods chain (23 findings)

### D19 · What is the map scale, and how long does each mode take between the towns?
- Why it matters: Causes C56 The map scale: all coordinates inside 35 km, against distances and times of hours and days, C58 One sea voyage with four passage times; 12 findings (5 marked "yes").
- What the documents say now: All coordinates come from map tiles at 0.01° (`world/countries.json` `degrees_per_tile`), so Lumeport–Selanu is 6 km and the whole world lies in 21 × 32 km, while documents state two days at sea, a three-hour flight, 186 km by road (timelines#F1); the one voyage has four passage times (timelines#F5).
- Options:
  - a) Scale the coordinates (e.g. ×10–20 from the origin): Lumeport–Selanu 60–120 km, a night crossing and a short flight; then settle one passage time for TH-26-19E (about 10–15 files).
  - b) Shrink distances and durations to a 30 km world (sea voyage, flight, road distances change in 7 flows).
  - c) Drop party coordinates; keep and scale only ports and airports.
- Recommendation: a): one constant changes, and the many stated distances and times stay; the site's map rendering must be checked.
- Related: D21

### D20 · Does the bench ship assembled or knocked down, how large is its pallet, and what does it weigh?
- Why it matters: Cause C69 The bench as shipped: pallets that do not fit, and a bench lighter than its parts; 7 findings (6 marked "yes").
- What the documents say now: 24 pallets of 4 assembled benches fit neither the trailer, a 40-foot container nor (per 24) a 45-foot one (equipment#F1); the bench weighs 41.5 kg gross, less than its five slats and two side frames as other flows ship them (items#F3).
- Options:
  - a) Knocked down (flat packs), a flat-pack pallet size stated wherever pallets are measured, and a gross weight of about 50 kg with the consignment and container weights that follow (road, rail, sea, tender).
  - b) Assembled, fewer benches per hold (changes quantities and invoices in road, sea, rail).
- Recommendation: a), as the merge decisions and equipment#F1 prefer.
- Related: D21

### D21 · How did the May lots reach Lumeway's stock, and under which declaration?
- Why it matters: Cause C71 Goods "from the distributor's stock" made days before they leave, and no document moves them; 4 findings (3 marked "yes").
- What the documents say now: The retail, sea and air goods are made in Urvania days before Lumeway despatches them "from stock"; only the March road and April rail deliveries move goods to Lumeway; the sea export cites the March road import for goods made in May (timelines#F4, items#F1).
- Options:
  - a) Give the later goods lots of the existing deliveries (sea: the March road lot `VI-LOT-260320`; retail and air: a lot of the rail delivery).
  - b) Keep the lots and add an import and a transfer to Lumeway (new documents).
  - c) Direct supply from Valdara (drop "from the distributor's stock").
- Recommendation: a): it keeps every flow's dates and changes only product data; then C70 (melt, serials, batches) follows.
- Related: D19, D20

## Payment terms (20 findings)

### D22 · Under a contract with its own payment terms, do invoices follow the contract or the seller's country practice?
- Why it matters: Cause C51 Contract payment terms never applied by the invoices under the contract; 12 findings (3 marked "yes").
- What the documents say now: The framework transport plans say "30 days net from the consignment note", the tender contract "30 days after each accepted release"; every invoice under them applies the seller's standard terms (XU-STD: 30 days from invoice, 2 % discount, 8 % interest) (conditions#F3; 12 findings, 10 High). `note/src/03-world.md`: "Each country also has its own payment practice, which every invoice of a seller there follows."
- Options:
  - a) The contract wins: invoices, reminders and remittances follow the contract terms (ore, rail, plastics, tender; about 10 files); the story sentence says "unless a contract says otherwise".
  - b) The practice wins: change the plans' and the contract's terms to the standard terms (4 documents and the tender notices).
- Recommendation: a): a contract that is never applied is the worse inconsistency, and conditions#F3 shows it would recur in every new contract flow.
- Related: D23

### D23 · Does every standard terms ID mean one period everywhere, and are utility bills due in 21 days?
- Why it matters: Cause C55 Standard terms IDs that do not mean the same number of days everywhere; 8 findings (1 marked "yes").
- What the documents say now: XU-STD/XB-STD mean 30 days and XL-STD 45 days in 27 of 34 invoices; all four utility invoices of 2026-04-02 are due 21 days later under all three IDs (utilities/09 redefines XB-STD as "Collected by direct debit 21 days after the invoice date."); the three Bayvarra–Lisavu invoices use the buyer's period (conditions#F2). `note/src/03-world.md`: "the island gives 45 days".
- Options:
  - a) Utilities get their own terms ID and text for 21 days; the three cross-border invoices are corrected to the seller's period (conditions#F2 preferred).
  - b) All seven due dates corrected to the cited terms.
  - c) A buyer's-period rule for cross-border invoices (story change).
- Recommendation: a).
- Related: D22

## Numbering and identity of documents (15 findings)

### D24 · Does each issuer number its own documents, in order of issue, across flows?
- Why it matters: Cause C74 Document numbers: one counter per flow shared by all issuers; 10 findings (3 marked "yes").
- What the documents say now: Every flow uses one block of consecutive numbers shared by all issuers (`Flow.number()`); per issuer the numbers jump with the flow (identifiers#F2); three payers share one remittance number in utilities.
- Options:
  - a) One counter per issuer (and per type, if wanted), numbered in global issue order; every reference and RF reference follows (all 250 files).
  - b) Keep flow blocks and state the rule (does not explain inversions within one issuer).
- Recommendation: a), after the issue times are settled (C72) so that the order is final.
- Related: D25, D26

### D25 · Which prefix does each party use, and is `BF` given to Bayforth or Brackenmere?
- Why it matters: Cause C75 Issuer prefixes: `BF` for two parties, second prefixes for signatures; 4 findings (1 marked "yes").
- What the documents say now: `initials()` gives Bayforth Forwarding and Brackenmere Furniture both `BF`; seven parties sign under a second prefix (identifiers#F1, #F5).
- Options:
  - a) A fixed prefix per party in parties.json (e.g. Brackenmere `BFU`), used for documents, items, signatures and RF references.
  - b) Keep and state that the prefix is not an issuer key.
- Recommendation: a).
- Related: D24

### D26 · Does `ProfileExecutionID` stay one per flow, or one per collaboration?
- Why it matters: Cause C76 `ProfileExecutionID` is the flow name in all 250 documents; 1 finding (1 marked "yes").
- What the documents say now: Every document carries `<FLOW>-2026-01` (identifiers#F3). `analysis/codelist-decisions.md`: "ProfileExecutionID: stays one per flow instance."; `note/src/03-world.md`: "`ProfileExecutionID` still names the run of the process".
- Options:
  - a) One per collaboration and profile (e.g. per order-to-invoice cycle of two parties).
  - b) Drop it where no collaboration needs it.
  - c) Keep the earlier decision and dismiss.
- Recommendation: a): the flow is a story, not an execution; the earlier decision predates the cross-flow view.
- Related: D24

## Calendar (12 findings)

### D27 · Is the world's week Monday to Friday, and may documents be issued at the weekend?
- Why it matters: Cause C53 Documents dated at the weekend against a Monday-to-Friday week; 12 findings (4 marked "yes").
- What the documents say now: By the count of conditions#F7, 48 documents (19 %) fall on a Saturday or Sunday, 47 of them by issuers whose contact says "Weekdays 08:00–17:00"; no holiday is stated (conditions#F7).
- Options:
  - a) Monday to Friday; move the weekend documents of people and offices to working days, keep weekend dates only for systems (port, carrier) whose contacts say so.
  - b) Systems issue at any time; contact hours concern people only (no date changes; the text contradictions remain).
  - c) Another week (story change).
- Recommendation: a), with a build check on the issue weekday per issuer kind; decide together with the issue-time mechanism (C72).
- Related: none

## Flow stories (decide per flow) (877 findings)

### D28 · tender: How is the tender told: lots, estimate, procedure dates, installation, guarantee?
- Why it matters: Causes C119 Tender: tendering terms copied into notices, call, award and contract, C120 Tender: contract, catalogue and call-off (releases, despatch, credit, reminder), C121 Tender: the procurement project and its lots, C122 Tender: the tenders, receipt and withdrawal, C123 Tender: the installation billed but never ordered, C124 Tender: expressions of interest, status, register extract and Valdara's qualification, C125 Tender: procedure periods against the notices' issue dates, C126 Tender: the guarantee certificate, C127 Tender: award, notifications and appeal; 210 findings (65 marked "yes").
- What the documents say now: Lot 2 works vs services; estimates equal the winning tender; periods before the notices; the installation billed but not ordered; a bank guarantee as immobilised shares.
- Options:
  - a) Lot 2 services; an estimate made before the tenders; notices moved to late January; the installation ordered and billed after acceptance; one guarantee by the bank.
- Recommendation: a), as the reviews prefer for each point.
- Related: none

### D29 · contest: How is the design contest coded and told (notice types, team, prize correction, estimate)?
- Why it matters: Causes C96 Qualification requests and responses (ESPD-like) in contest and tender, C97 Procurement notices (contest and tender): notice types, defaults, languages, links, C98 Contest: the design team, references, prizes and versions, C99 Contest: the estimated contract amount of 54,000 lume; 95 findings (35 marked "yes").
- What the documents say now: Standard-procedure notice types; the team reduced to its lead; the prize correction; an estimate unchanged after the prize rose.
- Options:
  - a) Design-contest notice codes from the Accord list, both team members as winners, version 2 stating the prize correction, an estimate that says what it covers.
- Recommendation: a).
- Related: none

### D30 · sea: Does the CIF price include freight and insurance; what does the agreement cover?
- Why it matters: Causes C114 Sea flow: bill of lading and ship reports, C115 Sea flow: isolated slips, C116 Sea flow: factoring, statement, payment and the island's debit note, C117 Sea flow: business card, digital agreement and capabilities, C118 Sea flow: the CIF sale, freight and insurance; 86 findings (24 marked "yes").
- What the documents say now: Freight and insurance charged on top of a CIF price; Lumeway's EDI terms "signed" by the Accord Council.
- Options:
  - a) CIF price includes them (drop the charges, adjust totals and follow-up documents); agreement signed by both partners.
- Recommendation: a), as sea/22#F3 prefers.
- Related: none

### D31 · utilities: Does the household pay on account; who subscribes to the warehouse's electricity; what is the telecom data pool?
- Why it matters: Causes C91 Utility statement builder: average amount, supplier consumption, subscriber data, C92 Utilities: the telecom statement and invoice, C93 Utilities: the household's water on account, the mandate and the levy, C95 Utilities: isolated slips; 65 findings (31 marked "yes").
- What the documents say now: Statement on account vs full invoice; Castrano named subscriber of Valdara's subscription; 35 GB twice.
- Options:
  - a) Monthly billing on actual reading (drop on-account), Valdara as subscriber, one data pool with a roaming share.
- Recommendation: a), as the reviews prefer.
- Related: none

### D32 · furniture: What do the replenishment figures and the return story say?
- Why it matters: Causes C103 Furniture flow: quotation, orders, invoice, return and credit, C104 Furniture flow: the replenishment and sales-reporting documents, C105 Furniture flow: the department's desks and installation; 58 findings (21 marked "yes").
- What the documents say now: Initial order twice the target inventory; a repeat order while stock suffices; a restocking deduction on a return the maker asked for.
- Options:
  - a) Figures that follow the replenishment profile; no restocking deduction on a maker-requested return.
- Recommendation: a).
- Related: none

### D33 · cotton: Who issues the phytosanitary certificate, is the bill of lading under documentary collection, and who represents the ginnery?
- Why it matters: Causes C106 Cotton flow: self-billing between ginnery and farm, and the mill's forecasts, C107 Cotton flow: classing and phytosanitary certificates, C108 Cotton flow: the sea export (bill of lading, VGM, pre-arrival report); 54 findings (17 marked "yes").
- What the documents say now: A chamber issues the phytosanitary certificate; the original bill goes to a bank with no collection; a customs broker as tax representative of domestic farm purchases.
- Options:
  - a) A plant-health authority issues it; open account, original to the forwarder as instructed; no tax representative.
- Recommendation: a).
- Related: none

### D34 · retail: Is the store's catalogue new or an update; when did the delivery arrive?
- Why it matters: Causes C110 Retail flow: catalogue request, catalogue, updates and deletion, C111 Retail flow: promotion, forecast, inventory and the shop sale, C112 Retail flow: isolated slips, C113 Retail flow: the delivery to the store (carrier references, arrival day); 52 findings (15 marked "yes").
- What the documents say now: A "new" catalogue that supersedes a version; "on its way, expected 29 April 14:00" but received 30 April.
- Options:
  - a) A new catalogue without previous version (or an update with one); one delivery day across the documents.
- Recommendation: a).
- Related: none

### D35 · road: Who endorses the certificate of origin, and what happens to the extra side frame?
- Why it matters: Causes C100 Road flow: isolated slips of the truck shipment, C101 Road flow: application and certificate of origin, C102 Road flow: the substituted 2026 casting; 47 findings (7 marked "yes").
- What the documents say now: An embassy endorsement by the Trade Accord Council on a preferential certificate; an extra frame accepted, never billed or returned.
- Options:
  - a) The chamber certifies, the Council endorses only if a rule says so; the extra frame is billed or returned.
- Recommendation: a).
- Related: none

### D36 · mast: Which dangerous-goods packing and air data does the mast consignment have?
- Why it matters: Causes C79 Mast flow: dangerous-goods data of the battery, detector and stripper consignment, C80 Mast flow: the air waybill and the ULDs; 42 findings (15 marked "yes").
- What the documents say now: Crates over the PI 965 IA limit; CAO liquid in a closed AKE; placard endorsements; the waybill without flight.
- Options:
  - a) Split the battery crates under the limit, stow the CAO liquid as the IATA rules ask, drop the road data from orders and invoices, give the waybill its flight.
- Recommendation: a).
- Related: none

### D37 · rail: Which roles do the hub and the terminal play, and which consignment note applies?
- Why it matters: Cause C90 Rail flow: container train documents; 33 findings (8 marked "yes").
- What the documents say now: The terminal operator as transportation network manager; CMR for an international rail carriage; "not under the Container Convention" under customs seal.
- Options:
  - a) The hub as terminal operator only; CIM for the rail leg with a road pre-carriage stage; drop the Container Convention indicator.
- Recommendation: a).
- Related: none

### D38 · Which documents that the flows cite but do not contain should be added?
- Why it matters: Cause C73 References to documents under IDs no document has, or to documents the flow does not contain; 27 findings (7 marked "yes").
- What the documents say now: Correctable wrong IDs (tender call for tenders, air order, replaced notices) need no decision. Documents cited but not modelled: the waste weight statement (waste/02#F1), the furniture delivery note (furniture/09#F1), Bayforth's transport plan (retail/14#F1), the tender receipt (tender/18#F2), the ore standing plan (ore/02#F10).
- Options:
  - a) Add the documents the story rests on (weight statement, furniture despatch advice) and drop the other references.
  - b) Keep all as typed references to documents outside the examples.
- Recommendation: a) for the weight statement and the despatch advice (they carry quantities the flow bills); b) for the rest.
- Related: none

### D39 · air: Which flight was missed, and is the air shipment a consolidation?
- Why it matters: Causes C85 Air flow: the missed-flight story and the CPT order change, C86 Air flow: packing, consolidation and charges of the castings; 23 findings (11 marked "yes").
- What the documents say now: "Next day's flight" but arrived the same day; "not consolidated" with a house waybill.
- Options:
  - a) An evening flight on 13 May missed, KXL207 on the 14th; a direct air waybill without consolidation.
- Recommendation: a), as air/07#F2 and air/04#F2 prefer.
- Related: none

### D40 · carnet: What is the carnet's timeline (fair, re-export, re-import) and which counterfoils exist?
- Why it matters: Cause C78 Carnet flow: counterfoils, time limits and the duty claim; 20 findings (7 marked "yes").
- What the documents say now: The carnet shows all counterfoils stamped at issue; proof is requested before the time limit; the duty claim exceeds three times the value.
- Options:
  - a) Counterfoils stamped as the goods move; request after the limit; the claim from the declared value (with D18).
- Recommendation: a).
- Related: none

### D41 · plastics: Who certifies the recycled content, and is international carriage of exports taxed in Urvania?
- Why it matters: Causes C87 Plastics flow: barge waybill and goods data, C88 Plastics flow: recycled-content certificate issued by a chamber of commerce; 20 findings (6 marked "yes").
- What the documents say now: A chamber of commerce issues the recycled-content certificate; standard VAT on the river freight of exported goods.
- Options:
  - a) A certification body issues it; keep the customer-location VAT rule (conditions found it consistent).
- Recommendation: a).
- Related: none

### D42 · waste: Is the waste movement domestic or transboundary, and how is the billed net weight shown?
- Why it matters: Cause C77 Waste flow: a transboundary notification for a movement inside one town; no weighbridge statement; 19 findings (10 marked "yes").
- What the documents say now: The notification and movement are addressed to customs for a movement inside Ferrano; the weight statement does not exist; the invoice bills gross tonnes.
- Options:
  - a) Domestic movement under Urvania's waste authority, a weight statement added, net weight billed.
  - b) A real transboundary movement (other destination, customs involvement).
- Recommendation: a).
- Related: none

### D43 · wood: In which unit are the slats quoted, ordered and invoiced?
- Why it matters: Cause C89 Wood flow: slat units and isolated slips; 10 findings (6 marked "yes").
- What the documents say now: "Per thousand" in the quotation, per slat elsewhere; OrderableUnitFactorRate 50.
- Options:
  - a) Per slat everywhere, the minimum as a quantity; drop the factor.
- Recommendation: a).
- Related: none

### D44 · energy: How are the 2400 MWh for Ferrano Energy exported and imported?
- Why it matters: Cause C82 Energy flow: 2400 MWh exported to Montebrio, sold to Ferrano Energy, imported by nobody; 9 findings (5 marked "yes").
- What the documents say now: The export consigns all 39200 MWh to Montebrio; the import covers 36800 MWh; Ferrano Energy's 2400 MWh are imported by nobody.
- Options:
  - a) Two consignments in the export, a second import declaration by Ferrano Energy.
  - b) Ferrano Energy buys from Montebrio domestically.
- Recommendation: a), as all reviews prefer.
- Related: none

### D45 · ore: When did the ore train arrive, and is a bonus or penalty due?
- Why it matters: Cause C81 Ore flow: monthly call-off, plan "as requested", bonus and moisture; 7 findings (5 marked "yes").
- What the documents say now: The plan confirmed "as requested" differs from the request; bonus and penalty neither applied nor excluded; arrival never recorded.
- Options:
  - a) Record the arrival in the waybill or a status, apply or exclude the bonus in the invoice; type the order as a call-off.
- Recommendation: a).
- Related: none

## Bulk confirmation (103 findings)

### D46 · Confirm in one go the "yes" findings inside causes whose direction is already settled
- Why it matters: 103 findings marked "yes" in causes without an owner decision: C01 (15), C02 (1), C03 (4), C04 (16), C06 (2), C08 (6), C11 (7), C12 (12), C13 (5), C14 (1), C15 (4), C17 (1), C19 (4), C23 (1), C24 (1), C26 (1), C29 (4), C30 (3), C31 (1), C33 (2), C36 (3), C41 (1), C70 (1), C72 (5), C84 (1), C94 (1).
- What the documents say now: Some findings are marked "Needs decision: yes" although their cause is settled by the merge decisions or an earlier decision (e.g. the authority's tax scheme in procurement documents, public bodies in registers, the Urvanian tariff in foreign declarations (Q24), fillers in transport documents). They are listed in `analysis/worklist-assignments.csv` with D46.
- Options:
  - a) Confirm: they are fixed with their cause.
  - b) Pick out the ones to decide separately.
- Recommendation: a).
- Related: none

