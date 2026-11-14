# Thorough reviews of the examples: status and merge decisions

This file goes with the review skill `.claude/skills/ubl-example-review`. It records:

1. which flows have a thorough review, and with which run ID;
2. the decisions the merges made on problems that recur across examples and flows (severity, whether
   a person must decide, the preferred option), so that a later run rates the same problem the same
   way;
3. the full decision tables of every merge, as the mergers wrote them (appendix).

A merge reads this file before it writes its own decisions (see the skill, section "Running a
thorough review"). When a run is finished, its decision tables are appended to the appendix.

## Status (2026-11-14)

| Flow | Examples | Run ID | Merged files |
|---|---|---|---|
| waste | 3 | `20261112T1415Z-thorough` | 3 |
| carnet | 4 | `20261112T1443Z-thorough` | 4 |
| mast | 5 | `20261112T1443Z-thorough` | 5 |
| ore | 8 | `20261112T1527Z-thorough` | 8 |
| energy | 9 | `20261112T1608Z-thorough` | 9 |
| packaging | 9 | `20261112T1631Z-thorough` | 9 |
| plastics | 11 | `20261112T2101Z-thorough` | 11 |
| wood | 11 | `20261112T2101Z-thorough` | 11 |
| rail | 11 | `20261112T2137Z-thorough` | 11 |
| air | 10 | `20261112T2137Z-thorough` | 10 |
| utilities | 14 | `20261112T2230Z-thorough` | 14 |
| road | 17 | `20261112T2311Z-thorough` | 17 |
| contest | 16 | `20261112T2358Z-thorough` | 16 |
| furniture | 17 | `20261113T0047Z-thorough` | 17 |
| cotton | 18 | `20261113T0121Z-thorough` | 18 |
| retail | 22 | `20261113T0434Z-thorough` | 22 |
| sea | 29 | `20261113T0552Z-thorough` | 29 |
| **tender** | 36 | **not reviewed yet** | 0 |

Five manual reviews (run `20261112T0851Z-manual`) also exist; they predate the skill.

Not done yet:
- the thorough review of **tender**;
- the separate **consistency review** across documents and flows (timelines, capacity, where
  equipment is, the map). Many reviews list such questions under "Outside this review".

`python3 -I .claude/skills/ubl-example-review/scripts/list_reviews.py <flow>` lists every review of a
flow with its findings and the version it reviewed.

## Decisions on recurring problems

The rows below are the decisions most merges converged on. Where a merge differed, the appendix says
why. "Decision" is the "Needs decision" value of the finding.

| Problem | Severity | Decision | Preferred option / note |
|---|---|---|---|
| `Language/LocaleCode` = `en` with listID ISO 639 (a language, not a locale; 362 in 213 files) | Medium | no | drop LocaleCode; a locale such as `en-XB` from a locale list is the option |
| Province ("Province of Ferrano") in `Region` instead of `CountrySubentity` (219 in 104 files) | Medium | no | move to CountrySubentity |
| `AdditionalStreetName` = "Gate 3" in Lumeway's postal address (79 in 76 files) | Medium | no | drop from the postal address; a gate belongs in a delivery location |
| `RegistrationDate` 1996-01-01 for about 25 unrelated companies (271 in 181 files) | Low | yes | per company a real date. Some merges (sea 16–29) did not add it where no part raised it |
| Contacts whose name, job title and department contradict each other or the party's role | Low | no | one finding per example, all contacts grouped |
| Party master data copied into documents that do nothing with it (tax schemes, share capital, customs trader IDs, logos, web shop, social media, service provider) | Low | no | one finding per example; the issuer's own share capital on its own invoice is accepted |
| Catalogue / product-passport data copied into business documents | Low | no | own finding, separate from party data |
| `CorporateStockAmount` holds share capital, UBL defines "number of shares" | Low | no | grouped with master data; a note for the OASIS TC write-up |
| English text tagged `en-XB` / `en-XU` / `en-XL` depending on the issuer; Italian(ate) street names tagged English | Low | yes | one rule for the language tag; the untagged legal form is a separate Low/no finding in most merges |
| Bench emission triple: value 96 kg, factor 0.82, base 1 EA (39 files) | High | no | 0.82 × 1 ≠ 96; drop factor and base or correct them |
| `FullnessIndicationCode` = `CRADLETOGATE` (system boundary in an element about full equipment; 39 files) | Medium | no | drop; TC write-up |
| `LifecycleStageCode` MANUFACTURING (A3) with a cradle-to-gate description | Medium | no | — |
| World item numbers (771…, 077…) that are valid GTIN-12s; GTINs in Lumeway's GS1 company prefix | Low | yes | — |
| Side frame classified HS 732599 instead of 9401.99 (part of a seat; 22 files) | Medium | no | own knowledge of the nomenclature |
| Public bodies (customs, councils, chambers, port authorities) as companies in a commercial register with a liquidation status | Medium | no | drop the company attributes; the world list has no register type for public bodies |
| Shipment `GrossWeightMeasure` without the transport equipment its definition includes | Medium (High where the same document gives the container's weight) | no | add the container tare |
| `ShippingOrderID` holding the consignment or shipment ID | Medium (High where it contradicts another document) | no | — |
| Signature with only an ID and a signatory (137 of 147 Signature aggregates) | Low | yes | — |
| `NoStatus` as status code | Low | no | drop |
| References with only an ID and no document type | Low | no | DocumentTypeCode |
| Exchange rates with nothing to convert, or between a currency and itself | Low (Medium where the element's own condition is not met) | no | drop |
| Due date that contradicts the payment-terms text ("30/45 days net") | High | no | preferred: correct the due date where the same terms ID means the same days elsewhere |
| Dates, events or references after the document's own issue time | High | no | — |
| Taxable amount that ignores the document's own allowance or charge (orders in furniture and retail, invoices in cotton) | High | no | recalculate |
| Debit note with accounting supplier/customer reversed against seller, buyer and payee (furniture/14, sea/28) | High | yes | probably one pattern in the generator |
| Waybill note "three originals" against the distribution list | High | no | — |
| Tax category O ("services outside scope") used for goods | Medium | yes | — |
| Lumeport and Selanu 3.2 nm apart by their coordinates, against days at sea | High where one document contradicts itself, otherwise "Outside this review" | yes | a map-scale question for the consistency review |
| Benches that do not fit pallet, trailer or container when assembled (rail, road, sea) | Low–Medium | yes | the story must say whether they ship knocked down |
| Customs value basis (FOB vs CIF) not stated or contradicting the bill of lading | Medium | yes | the world's valuation rule is undecided |
| MMSI MID 298 or 297, call signs starting with Q | refuted | — | `world/codelists/sources/PROVENANCE-second-round.md`: no MID 280–299 and no Q call-sign series allocated |

## Appendix: the decision tables of each merge

Each table is copied unchanged from the merge that wrote it. A letter (a, b, c, d) is one merger;
a flow with several mergers split its examples between them. Waste, carnet, mast and ore were merged
before the decision files were introduced.


### energy-merge-decisions-a

#### Energy merge, run 20261112T1608Z-thorough, half a (01-05): decisions on recurring problems

Read energy-merge-decisions-b.md before writing this; I agree with every row there.

| Problem | Severity | Needs decision | Why |
|---|---|---|---|
| Province in `cbc:Region` (`Province of Ferrano`) | Medium | no | Same as b. Section 6 names "a province in Region" as its Medium example; the fix is encoding (CountrySubentity + XU address format), not story. Broad said yes, parties said no; I follow parties and b, and record the change. |
| `LocaleCode` = `en` (listID ISO 639) | Medium | no | Same as b. Section 6 names it Medium; all parts agree. |
| Contacts copied from master data (01, 02, 03 receiver/customer "Customer service, Sales"; 01 subscriber "Order desk"; 02 supplier "Metering office"; 04/05 exporter's/consignor's "Gas sales manager", importer's "Energy trader") | Low | no | Same as b. Section 6: a contact that does not fit the role is Low. |
| `en-XB` tags on Urvanian renderings (04 consignee) + untagged `CompanyLegalForm` | Low | no | Same as b; one finding, legal form as extra XPath line. |
| 39200 / 36800 + 2400 MWh split, shipment KG-SH-26-0154 | High | yes | Same as b. In 04 two High findings: (F1) sole consignee Montebrio for gas 07 sells to Ferrano Energy; (F2) shipment KG-SH-26-0154 carries 39200 MWh/2 940 000 kg in 04 but 36800 MWh/2 760 000 kg in 05 (logistics split these; the broad/context parts combined them; I keep them apart because the shipment-ID clash contradicts 05, the consignee clash contradicts 07). In 05 one High finding (shipment-ID clash with 04). Needs decision yes everywhere (fix adds/changes documents). Money's "a consignee may differ from the buyer" is quoted in Why as the possible reading. |
| Kelpstone plant "four kilometres" vs field coordinates 6.1 km (04, 05) | Low | no | Same as b. Context in 04 refuted it (origin is a grid tile); I keep it Low and quote that argument. |
| Customs-trader number on 03 (domestic electricity sale Montebrio -> Ferrano Energy) and on the subscriber in 01 | Low | no | Copied master data. Unlike b's export invoices 06/07, 03 and 01 have no customs link, so the refutation b accepted does not apply. |
| ISIC 3510 for Ferrano Grid / Ferrano Energy, which also run/sell gas | Low | no | Incomplete classification, not wrong; context refuted it as "main activity". Kept Low with both arguments. |
| Customs authority with liquidation status and COMMERCIAL registration (04, 05) | Medium | no | Parties gave Medium, broad Low. The registration type states a commercial register for a public body: a value with a meaning that does not fit (Medium). |
| CargoTypeCode BULK ("Dry bulk") for pipeline gas (04, 05) | Medium | no | All parts Medium. |
| Pipeline flow period / exit-entry point missing (04, 05) | Medium | no | The document's purpose (declaring a month's flow) depends on it. |


### energy-merge-decisions-b

#### Energy merge, run 20261112T1608Z-thorough, half b (06-09): decisions on recurring problems

| Problem | Severity | Needs decision | Why |
|---|---|---|---|
| Province in `cbc:Region` (`Province of Ferrano`) | Medium | no | The skill names "a province in Region" as its Medium example. Moving it to `CountrySubentity` changes the encoding, not the story. Broad said yes ("or document the convention"), parties said no; the world convention has no stated reason that makes the province an economic region. In 09, both places (the customer's address and the payer bank's address) go in one finding. |
| `LocaleCode` = `en` (listID ISO 639) | Medium | no | Section 6 names "a language code in LocaleCode" as Medium. All parts agree. |
| Contacts copied from master data (sales/trading desks on the reminder and the remittance advice; customer service as the buyer's contact in 07) | Low | no | Section 6: "a contact that does not fit the role" is Low. Changing a contact does not change the story. |
| `en-XB` tags on the English renderings of Urvanian addresses (plus an untagged legal form where 01-03, 05 and 09 have `qau` + `en-XU`) | Low | no | A consistency remark (section 6 Low). One finding per example, with the untagged `CompanyLegalForm` as an extra XPath line (from parties). |
| 39200 MWh export (04) = 36800 (Montebrio, 05/06) + 2400 (Ferrano Energy, 07); sole consignee Montebrio; no import by Ferrano Energy; shipment KG-SH-26-0154 | **High** in 07 | **yes** | The parts of 07 gave High (logistics, context), Medium (broad) and Low (money, parties). I chose High: section 6 makes "a statement in one example that another example of the flow contradicts" High. The invoice sells 2400 MWh measured at the border to Ferrano Energy and exempts them as an export, while the export declaration consigns those same MWh to Montebrio Power. All five parts of 04 also rate this High. Money's argument (a consignee may differ from the buyer) goes into "Why" as the possible reading, but nothing in the flow states it. Needs decision: yes, because the fix adds or changes documents of the flow. In 06 the split itself is not a finding: 06's 36800 MWh match 05, and Montebrio is the consignee. The shipment-quantity clash between 04 and 05 (KG-SH-26-0154: 39200 against 36800) lies entirely in 04/05, so in 06/07 it goes under "Outside this review". |
| Kelpstone `PhysicalLocation` (plant description, coordinates, InformationURI = home page) on 06-09 | Low | no | Copied master data, section 4.8. |
| Customs-trader numbers on the reminder (08) and the remittance advice (09) | Low | no | Copied master data. On the invoices 06/07 the parts refuted it (the invoice of an export supports the customs declarations). I accept that refutation. |
| "Four kilometres" in the plant description against field coordinates 6.1 km away (06/07, which carry both the plant and the field coordinates) | Low | no | Added in the merge, to match the Low the 04/05 parts gave. The platform need not sit at the field's grid coordinates, so Low. |

Read energy-merge-decisions-a.md afterwards: it agrees with every row above. There is nothing to reconcile.


### packaging-merge-decisions-a

#### Packaging merge, run 20261112T1631Z-thorough: decisions of merger A (examples 01–05)

Recurring problems and how merger A treats them in its merged files. Counts are re-done by merger A
over `world/examples/*/*.xml` only.

| Problem | Severity | Needs decision | Preferred option | Why |
|---|---|---|---|---|
| LocaleCode `en` (listID ISO 639) | Medium | no | (a) remove LocaleCode; (b) a real locale (e.g. `en-XB` with a locale list) as alternative | All parts agree on Medium (section 6 names "a language code in LocaleCode" as Medium). Broad and context prefer removal, parties prefers `en-XB`; removal is preferred because Language/ID already says English and nothing in the documents uses a locale (IND5). Verified: 362 occurrences in 213 files, always `en`. |
| Province in Region (`Province of …`) | Medium | no | move to CountrySubentity | Section 6 names it as Medium. Verified: 219 occurrences in 104 files. |
| RegistrationDate 1996-01-01 | Low | yes | individual dates from the company histories; or omit; or confirm as story fact | Changes the companies' histories (story), and could be a deliberate story fact. Verified: 271 occurrences in 181 files, 25 distinct CompanyIDs. |
| Contacts copied from master data (one contact per party whatever the role; sales job title/department on purchasing desks) | Low | no | role-specific contacts with agreeing name, job title and department | Section 6 example of Low ("a contact that does not fit the role"). Encoding of contacts, not the story. Verified: ('Order desk','Customer service officer','Sales') 89 contacts, ('Purchasing',…,'Sales') 52, ('Buying office',…,'Sales') 41; 89 files with a Purchasing/Buying office contact in Sales; 229 files with 'Customer service officer'. |
| Other master data the document does nothing with (seller FinancialAccount in orders, ServiceProviderParty Castrano, SecurityListing, customs trader IDs in domestic documents, logo/web shop/social media in orders) | Low | no | remove where not used | Section 4.8: Low. Verified: `VI-SP-2026-01` and `Castrano Logistics` each in 75 files (the context part's "84" was corrected to 75); seller FinancialAccount only in packaging/01 and 03 among the 18 Orders. |
| World item numbers (`urn:ubl-examples:world:item`) that are valid GTIN-12 in the GS1 US range 077 | Low | yes | change the scheme's format so it is not a valid GTIN | Could not be checked against GEPIR whether the numbers are assigned; changing the world's item scheme is a decision. Verified: 8 distinct values, all valid GS1 mod-10, 82 occurrences in 64 files. |
| Cost centre fixed per party (`2200 Raw cotton` for garment bags, `6120 Garden department` for shirts) | Low | no | a cost centre that fits the goods, same in order and invoice; or omit | Plausibility of a buyer's internal code (Low); does not change the story. Verified: `Raw cotton` in 5 files, `Garden department` in 12. `3100 Raw materials and parts` for stretch film (01/02) refuted by all parts and by the merge. |
| en-XB tags on the English rendering of an Urvanian party's address in a document issued from Bayvarra (packaging/02) | Low | yes | (a) the party's own variety (en-XU), or (b) the issuer's variety as a stated convention | Parties made it a finding, broad and context refuted it ("the tag follows the issuer"). Both readings are defensible; the merge cannot settle it, so per the skill it stays Low with Needs decision: yes and both arguments. Verified: Valdara's English street name is tagged en-XU in 24 places, en-XB in 18. |
| PenaltyPeriod of 1 month next to "1.5 % surcharge per month late" | Low | no | start date only, PenaltyAmount stated as per month | Money part only; definition "the period during which penalties may apply". Verified: 18 files with PenaltyPeriod, all `DurationMeasure unitCode="MON"` = 1. |
| Order without requested delivery/despatch date; invoice without delivery information | Low | no | RequestedDeliveryPeriod / RequestedDespatchPeriod; Delivery/ActualDeliveryDate on the invoice | Completeness remarks. Verified: 15 of the 18 Orders carry no requested/promised/estimated delivery period, LatestDeliveryDate or RequestedDespatchPeriod. |

##### After reading packaging-merge-decisions-b.md
Merger B's decisions agree with these on every shared problem. B's Medium for the missing date in
06-DespatchAdvice is a different document type (its purpose depends on the date); A keeps the
missing requested date in the Orders as Low. Nothing in 01–05 changed because of B's file.


### packaging-merge-decisions-b

#### Packaging merge, run 20261112T1631Z-thorough: decisions of merger B (06–09)

For problems that recur in both halves. Merger A: please read; where you decide otherwise, say so
in your "Changed in the merge". Merger B read `packaging-merge-decisions-a.md` before finishing
(it did not exist when this file was first written).

| Problem | Severity | Needs decision | Why |
|---|---|---|---|
| LocaleCode `en` (listID ISO 639) | Medium | no | Skill §6 lists "a language code in LocaleCode" as Medium. Encoding only. Options: (a) remove (preferred by broad/context), (b) a real locale such as `en-XB` from a locale list named in listID (preferred by parties). I keep both, preferring (a) because it needs no new list; the fixing session chooses. Counts: 362 occurrences in 213 files (grep over `*.xml`). |
| Province in `Region` | Medium (skill §6) | no | Does not occur in 06–09 (they use CountrySubentity `Coastal State`); no finding in my half. |
| RegistrationDate `1996-01-01` | Low | yes | Looks like a default (25 companies, 271 occurrences in 181 files). Fixing it means inventing company histories (story), so yes. |
| Contacts copied from master data (Purchasing / Buying office in Sales, Export desk) | Low | no | Skill §5/§6: a contact that does not fit the role is Low. Fix is encoding of contacts, not the story. I group all places in one document into one finding, except the carrier's "Export desk", which has its own reason (export desk for a domestic delivery) and stays a separate Low. |
| GTIN-like world item numbers (`urn:ubl-examples:world:item`, e.g. `772030000090`, valid GTIN-12 in GS1 US range) | Low | yes | Rule "fictional values must not be mistaken for real ones"; but the format is a world-wide convention, so changing it is a decision. |
| GTIN of the Lumeport shirt under Brightmarket's prefix (08, 09) | Low | yes | Who owns the brand is story. Only my half. |
| Cost centre fixed per party (`Garden department` / `6120` for shirts) | Low | no | Plausibility; the order (05) carries the same value, so 05 and 07 should change together. 12 files carry it. |
| en-XB tag on the English rendering of a Lisavan party's address (Velumi in 09: en-XB in 11 files, en-XL in 8) | Low | yes | Broad and context refuted it ("tag follows issuer's country"), parties found it. No convention is stated, so I cannot settle it: Low + needs decision yes, with both arguments. |
| Marketing data (logo, web shop, social media, share capital) and customs trader ID in party blocks | Low (despatch advice, invoice); refuted on purchase receipts (customer-facing) | no | Copied master data, skill §4.8. On receipts the logo/web/social is what a store prints, so refuted there; customs trader ID on a domestic till receipt stays Low. |
| One-month PenaltyPeriod against "1.5 % surcharge per month late" (07; same in 02, 04) | Low | no | PenaltyPeriod is "The period during which penalties may apply"; one month limits the surcharge the note makes recurring. |
| Forwarder (ISIC 5229) as CarrierParty | refuted | – | Bayforth acts as carrier elsewhere in the world; a forwarder can contract as carrier. |

##### After reading packaging-merge-decisions-a.md
Merger A's decisions agree with these on every shared problem (severity, Needs decision, preferred
option). No disagreement; nothing changed in the 06–09 merged files because of it. One difference of
document type only: A treats a missing requested date in an Order as Low; B treats the missing
despatch/delivery date in the DespatchAdvice (06 F2) as Medium, because skill §6 makes missing
information that the document's purpose depends on Medium, and a despatch advice exists to say when
goods are sent and arrive.


### plastics-merge-decisions-a

#### plastics merge decisions, merger A (plastics 01-05), run 20261112T2101Z-thorough

Final (after reading plastics-merge-decisions-b.md and wood-merge-decisions-a/-b.md). Aligned where the problem is the same; differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region | Medium | no | move to CountrySubentity (+ code if Urvania has a list). Same as b, wood. |
| LocaleCode `en` (ISO 639) | Medium | no | drop LocaleCode (preferred), or a real locale (en-XB) from a locale list. Same as b, wood. |
| RegistrationDate 1996-01-01 | Low | yes | own date per company; or record a 1996 (re-)registration in the story. Parties part said no; aligned with b and wood: yes. |
| Contacts not fitting the role | Low | no | role-specific contacts per document, or drop contacts the document does not need. Same as b, wood. |
| Rivermouth's bank account XB96BLUM… in documents that pay nothing (01-05) | Low | no | drop. Same as b. |
| Rinova's waste permit XU-ENV-2024-0311 (R3) | Low | no | drop where unused. Aligned with b: no (parties part said yes; broad refuted it in 01/02 as backing the recycled-content claim; the merge disagrees: the claim has its own item-level EnvironmentalCertificate and nothing links the party permit to it; removing it changes no story). |
| Chamber of commerce as recycled-content certificate issuer (01, 05) | Low | yes | certification body / environment authority as issuer, or story reason. Differs from b's "no": changing who certifies recycled content changes a party in the story (b itself says "yes if it changes who certifies"). Both parts that raised it said yes. |
| Italian text tagged en-XU/en-XB | Low | yes | cannot settle (one part refuted as world convention for proper names; legal form is the stronger case). Same as b, wood. |
| Same party rendered differently by issuer (en-XB vs en-XU tag; legal form/permit type single untagged in Rivermouth-issued 01) | Low | yes | one rule, documented, or identical master data everywhere. Same as wood ("cannot settle: tag can follow the issuer"). |
| GTIN-like item numbers (771030000048, valid GS1 check digit) | Low | yes | change world item-number format (preferred), or record GS1 verification. Broad part's choice; b had not yet decided. |
| NoStatus DocumentStatusCode (03) | Low | no | drop. Same as b, wood b. |
| Signature IDs: flow name (05 RR-SIG-EX-plastics), unrelated number (04 FB-SIG-882 = order number) | Low | no | signatory's own numbering. Same as b. |
| Customs authority as a company (commercial register, liquidation status, register-scheme ID) (05) | Medium | no | drop company attributes, public-body scheme. Same as b, wood b. |
| Customs authority's VAT registration (05) | Low, own finding | no | drop. Differs from b/wood b (they fold it into the Medium finding): a VAT registration of a public body is possible (broad refuted it on that ground), so it does not contradict the party's nature; it is copied master data (section 4.8), hence Low and separate. |
| References with ID only (05 order reference) | Low | no | add DocumentTypeCode. Same as b. |
| From/To locations = company name + business address (03, 04) | FromLocation High (contradicts Note[2] of the same document and the loading port of 04/06; in 04 its own LoadingPortLocation); ToLocation Low (separate: that Estuary Road 28 is not at the river quay cannot be shown) | no | From = Rinova's quay, To = River quay Lumeport, named as places. |
| Missing goods description in transport documents (03 request, 04 plan) | Medium | no | add goods item / packages / volume. |
| Goods item quantity in TNE, no packages, no net mass in export declaration (05) | Medium | no | net mass in NetWeightMeasure, packages declared. |
| No transport mode / means at the border (05) | Low | no | add main-carriage stage with mode 8 and the barge. |
| Order without requested delivery period (01) | Low | no | add RequestedDeliveryPeriod (or drop the waybill's "allowed by the buyer" date). |
| Missing despatch/delivery dates | - | - | no such finding in 01-05 except the order's delivery period above. |


### plastics-merge-decisions-b

#### plastics merge b (06–11): decisions on recurring problems, run 20261112T2101Z-thorough

Final (06–11 merged). Read plastics-merge-decisions-a.md and wood-merge-decisions-a/-b.md; aligned where the problem is the same, differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region | Medium | no | Move to CountrySubentity (as the Bayvarran "Coastal State"). Same as a, wood. |
| LocaleCode `en` (ISO 639) | Medium | no | Drop LocaleCode where no locale matters (preferred), or en-XB from a locale list. Same as a, wood. |
| RegistrationDate 1996-01-01 | Low | yes | Own date per company; or record a 1996 (re-)registration in the story. Parties said no; same as a, wood: yes. |
| Contacts not fitting the role | Low | no | Role-specific contacts; or drop. Same as a, wood. |
| Rivermouth's bank account in documents that pay nothing (06, 08) | Low | no | Drop. Same as a. In 09 it is combined with the note "duties paid by the importer's account at customs" (money part): Low, yes (whether duty is due). |
| Rinova's waste permit (R3, XU-ENV-2024-0311) | Low | no | Drop. Parties said yes; same as a. |
| Chamber of commerce as recycled-content certificate issuer (08, 09, 10; not raised in 11) | Low | yes | Certification body / environment authority, or story reason. Aligned with a (draft 1 said "no unless it changes who certifies": it does). |
| Italian text tagged en-XU/en-XB | Low | yes | Record convention (legal form in English) or translate. Same as a, wood. |
| Same party rendered differently by issuer (09, 11: Rivermouth-issued) | Low | yes | One rule, documented, or identical master data. Same as a, wood. In 09 combined with the Italian-text finding (same XPaths). |
| GTIN-like item number 771030000048 | Low | yes | Non-GTIN format (preferred), or record verification. Same as a. |
| Signature ID with flow name (09) or doubled prefix (06 FB-SIG-FB-WB-26-0890) | Low | no | Signatory's own numbering. Same as a. |
| Customs authority as a company (09) | Medium | no | Drop company attributes, public-body scheme. Same as a, wood b. (09 has no VAT registration of customs, so a's separate Low VAT finding does not arise.) |
| References with ID only | Low | no | DocumentTypeCode. Same as a. |
| NoStatus | Low | no | Drop. Same as a, wood b. |
| Missing despatch/delivery dates | DespatchAdvice 08: Medium | no | Add actual despatch and estimated delivery. Same as wood b. |
| GoodsItem/Quantity in TNE | refuted in the merge (06 logistics/F7, 09 logistics/F1 part) | - | Differs from a (05: Medium "quantity in TNE, no packages, no net mass"). b: the tonne is a legitimate unit of a Quantity for a commodity sold by the tonne, so Quantity 120 TNE is not a misuse; what is missing is the package count (06: Medium, in the waybill's package finding; 09: Low, because 09 gives the net mass as CustomsTariffQuantity 120000 KGM, while 05 has no mass of the goods item at all, which justifies a's Medium there). |
| Lot/trace ID mismatch 06/08 | Low | no | One lot number in both. |
| Latest delivery date "allowed by the buyer" without source (06) | Low | no | Same as a's order finding (add RequestedDeliveryPeriod to 01). |
| Exit office in the import declaration (09) | Low | yes | Lowered from Medium (broad, context): UBL 2.5 ImportCustomsDeclaration has only CustomsExitOfficeLocation (checked in the gc), and the value fits it literally; only the presence question remains. |
| VAT on carriage of exported goods (07) | Low | yes | Money refuted with the world's exemption list; cannot settle; prefer recording the rule. |


### wood-merge-decisions-a

#### wood merge decisions, merger A (wood 01-05), run 20261112T2101Z-thorough

Final. Read wood-merge-decisions-b.md; aligned on every shared row (differences noted).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region | Medium | no (context part said yes; the name itself says "Province", so moving it is encoding) | move to CountrySubentity (+ code if the world has one). Same as b. |
| LocaleCode `en` (ISO 639) | Medium | no | drop LocaleCode where no locale matters; alternative a real locale (en-XB) from a locale list. Same as b. |
| RegistrationDate 1996-01-01 | Low | yes | each company its own date, unless a 1996 re-registration is the story. Same as b. |
| Contacts: Sales customer-service desk in every role | Low | no | role-specific contacts per document. Same as b. In 05 the customs office's weekday hours (broad) refuted in the merge, with parties: the declaration is made within those hours. |
| Copied master data (Castrano ServiceProviderParty, SecurityListing, CorporateStockAmount) | Low | no; yes only in 04 (parties: if Castrano does Valdara's warehousing, does it receive this delivery? same story question b raised for 06) | leave out where unused. |
| Commercial item specification (tolerance, test method) in customs declaration | Low, own finding (05) | no | as b. |
| Italian text tagged en (Via delle Officine, Società urvaniana per azioni) | Low | yes (broad finding, parties refuted as world convention; cannot settle) | record the convention in the story, or English renderings; legal form is the stronger case. Same as b. Count corrected: 219 English-tagged Via/Viale/Piazza/Corso/Strada/Valico/Banchina street names in 104 files. |
| Same Urvanian text tagged en-XB here, en-XU elsewhere | Low | yes (broad finding; parties/context refuted: tag follows issuer's English) | one rule, documented. Same as b. |
| Legal form of Urvanian party in one untagged rendering (02, 04, 05) | Low | no | render like the address (both, tagged). Same as b. Includes 02 CertificateType without its qau rendering. |
| UsabilityPeriod 12 MON on Surface | Low | no | remove. Same as b. |
| MeasurementDimension repeats Item/Dimension length | Low | no | Item/Dimension only. Same as b. |
| Signature ID with flow name (MS-SIG-EX-wood, 05) | Low | no | signatory's numbering. Same as b. 01 VI-SIG-26-RFQ and 02 MS-SIG-26-QT not affected. |
| Customs authority as a company (05) | Medium | no | drop liquidation status / commercial scheme / PartyLegalEntity. Same as b (broad Medium; context, parties Low). |
| Missing delivery period in the order (03) | Low | no | add RequestedDeliveryPeriod. |
| Transport window (04) ends 2026-03-01, before promised window 2026-03-02..16 | High | yes | logistics High, broad/context Low; a date in one example contradicted by another example of the flow (section 6 High). |
| Packing charge left out of customs value (05) | Medium | yes | declare 34800.00 and state the basis (DAP); same as b. |
| NoStatus DocumentStatusCode (04) | Low | no | drop. Same as b. |
| Shipment/GrossWeightMeasure = goods gross weight (05) | Low | yes | cannot settle (no transport equipment declared). Same as b. |
| Packages only in a note (04 TEPR, 05) | Low | no | in 04 Medium: "a transport request that does not say what is to be carried" is the skill's own Medium example (broad Medium; logistics, context Low). 05 Low. |
| Pallet charge outside the order's tax subtotal (03) | Medium | no | money Medium; broad refuted (tax 0 either way) - not followed. |
| OrderableUnitFactorRate 50 with quantities in EA (02, 03) | Low | yes | broad finding, money refuted (pack of 50 is the orderable unit); cannot settle. |


### wood-merge-decisions-b

#### wood merge b (06–11): decisions on recurring problems, run 20261112T2101Z-thorough

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region | Medium | no | Move to CountrySubentity (as Bayvarra). Context part said "yes" (are provinces administrative?); the name says "Province", so no world decision is needed for the encoding. |
| LocaleCode `en` (ISO 639) | Medium | no | Drop LocaleCode where no locale matters (preferred), or a real locale (en-XB) from a locale list. |
| Registration date 1996-01-01 | Low | yes | Own date per company from its history; or record a 1996 re-registration in the story. One context part refuted it (register start) – carried as counter-argument. |
| Contacts (Sales / Customer service officer) whatever the role | Low | no | Role-specific contacts per party; or drop JobTitle/Department. |
| Copied master data (Castrano ServiceProviderParty, SecurityListing, CorporateStockAmount) | Low | no (yes only in 06-DespatchAdvice, where Castrano "Warehousing and despatch" could be the receiver: story question) | Leave out where the document does not use them. |
| Commercial item specification (tolerance, test method) in customs declaration / invoice | Low, separate finding from party master data | no | Keep only what the document uses. |
| Italian text tagged en-XU/en-XB (street names, legal form) | Low | yes | Cannot settle (parties part refuted as world convention for proper names; legal form "Società urvaniana per azioni" is not a proper name). Prefer record the convention in the story, or English renderings. |
| Same address en-XB here, en-XU elsewhere | Low | yes | Cannot settle (tag can follow the issuer's English). Prefer one rule, documented. |
| Legal form of Urvanian party in one untagged rendering (Bayvarran-issued docs) | Low | no | Render like the address (both, tagged). |
| UsabilityPeriod 12 MON on "Surface" | Low | no | Drop it. |
| Length in SellersItemIdentification/MeasurementDimension and Item/Dimension | Low | no | Keep in Item/Dimension only. |
| Signature ID with flow name (VI-SIG-IM-wood) | Low | no | Signatory's own numbering. |
| Customs authority as a company (COMMERCIAL register, liquidation status, VAT registration) | Medium | no | Drop PartyLegalEntity/liquidation/commercial scheme (and VAT reg). Medium because the values contradict the party's own ISIC 8411 and the code meaning does not fit a public body (parts: broad Medium, parties/context Low). |
| Missing despatch/delivery dates | 06 DespatchAdvice: Medium (purpose depends on it); 08/10/11: Low | no | Add Delivery dates. |
| Packing (pallet) charge left out of customs value; no exchange rate | Medium | yes | Declare 3 480 000 XUF and state the rate; or story reason. |
| Packages/pallets only in a note / nowhere in logistics docs | Low | no | TransportHandlingUnit/Package in despatch advice. |
| NoStatus Document/LineStatusCode | Low | no | Drop (definition's condition "found to be incorrect" not met); broad's refutation recorded as disagreed. |
| Shipment/GrossWeightMeasure = goods gross weight | Low | yes | Cannot settle: no transport equipment is declared, so equal may be correct. |
| NotifierParty = importer | Low | no | Drop. |
| HS code / origin in domestic sale (10, 11) | Low | no | Drop or state domestic use. |

##### Final (after reading wood-merge-decisions-a.md)
- Aligned on every shared row.
- OrderableUnitFactorRate 50 (08): Low, Needs decision yes, as a for 02/03 (I had first meant to refute it). The broad part's "drop it, as in the order" is wrong: 03-Order carries the same factor.
- Italian street-name count: 219 in 104 files (recount), as a.
- Customs authority as company (07): Medium, as a for 05.
- Missing despatch/delivery dates in 06 DespatchAdvice: Medium (purpose depends on it); 08, 10, 11 Low.


### rail-merge-decisions-a

#### rail merge decisions, merger A (rail 01-05), run 20261112T2137Z-thorough

FINAL for 01-05 (merged files written and checked). Read rail-merge-decisions-b.md (draft 1), wood-, plastics-, air-merge-decisions-*. Aligned with b on every shared row; differences explained in the rows.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region (01-05) | Medium | no | move to CountrySubentity. broad/context/logistics said yes, parties no; aligned with b, wood, plastics. |
| LocaleCode `en` (01, 02, 03) | Medium | no | drop LocaleCode (preferred; parties), or en-XB. broad/context preferred en-XB. Same as b. Recount: 364 occurrences (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<' | wc -l`). |
| Gate 3 in AdditionalStreetName (01, 02, 03) | Medium | no | drop from postal address. Same as b, air. |
| RegistrationDate 1996-01-01 (Ferrano Rail Cargo 02-05, Hub 04-05) | Low | yes | not raised by any part of 01-05; added by the merge, as b. 271 occurrences in 181 xml files. |
| Contacts not fitting the role (buyer/consignee = Customer service/Sales; transport user = Order desk/Sales) | Low | no | role-specific contacts; one finding per example grouping parts. Same as b. |
| Terminal control "Weekdays 08:00-17:00" while acting at 05:30-06:45 (04, 05) | Low | no | hours that cover the train times, or drop the note. Own finding (contradiction of availability with the document's own times, but a contact note -> Low). |
| Copied master data (SecurityListing, CorporateStockAmount; Castrano ServiceProviderParty only in 01) | Low | no | drop where unused. In 02/03 Castrano is refuted (FromLocation is its warehouse). Same as b. |
| Catalogue/passport item data in the order (01: CircularityProfile, EnvironmentalEmission, warranty) | Low | no | own finding, separate from party master data (as b). |
| Italian text tagged en-XU/en-XB | Low | yes | cannot settle (broad refuted as world convention). Same as b. Recount: 217 renderings in 102 files tagged en-XU/en-XB starting Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina. |
| Valdara tagged en-XB in 01 vs en-XU elsewhere | Low | yes | one rule (cannot settle: tag can follow issuer). Same as wood/plastics. |
| Valdara legal form single untagged rendering in 01 | Low | no | both renderings, tagged. Same as wood/plastics (split from parties F4). |
| Bench emission triple 96 / 0.82 / 1 EA (01) | High | no | verified: 0.82 x 1 = 0.82 != 96. Drop factor and base. Same as b. |
| CRADLETOGATE in FullnessIndicationCode (01) | Medium | no | drop; record missing boundary element for the TC. Context said yes; same as b: no. |
| LifecycleStageCode MANUFACTURING for A1-A3 text (01) | Medium | no | omit code (or two entries). Same as b. |
| FTL as main service of rail request/plan (02, 03) | High | no | verified: FTL "one truck ... from place of loading to place of delivery" vs mode 2 container train, two 40ft boxes, rail border station, 09 RAILCONT. RAILCONT main; road leg as pre-carriage stage (CARRHAUL's text is about ports/shipping lines). 02 context said Medium; logistics yes (option b splits the flow) -> no, preferred option is encoding. |
| ToLocation = hub, service ends at Marrowdale (02, 03) | High | no | separate finding from FTL (different element); context said Medium. |
| Pickup 13 Apr before ServiceStartTimePeriod 14 Apr (02, 03) | High | no | verified; 08 actual pickup 13 Apr confirms. Start period 13 Apr. |
| Payment terms of 03 vs invoice 10 | High | no | verified: 14 Apr + 30 = 14 May vs DueDate 2026-05-17 and 2 % discount vs "net". |
| PenaltySurchargePercent 5 for "5 % of the freight per day late" (03) | Medium | yes | money: yes (which penalty); either reading misuses the element. |
| Locations named after companies (02/03 FromLocation Castrano; 03 AtLocation = carrier; 04/05 StatusLocation) | FromLocation/StatusLocation Low; AtLocation Medium (no stationary service) | no | place names + identifiers. Same as b, air. |
| Terminal operator as network manager (04 receiver, 05 sender) | Medium | yes | parties Medium/yes, context Low/yes; changes who a party is. |
| Actual departure 06:52 after issue 06:45 (05) | High | no | verified. "On time" for 7 min late split off as Low. |
| Planned/estimated Marrowdale arrivals under the hub's status location (05) | Medium | no | logistics High; broad/context Medium: events carry no location, read as ambiguity, not a hard contradiction. |
| PassengerQuantity 0 (03) | Low | no | drop. |
| Contract under two identifiers (02, 03) | Low | no | one identifier. 03 broad Medium, context yes. |
| NoStatus (02) | Low | no | broad refuted; aligned with wood b/plastics: drop -> finding. |
| SourceIssuerParty = SenderParty (05) | Low | no | parties Low; broad refuted as harmless; kept (no fillers). |
| GTIN-like item number 771020000027 (01) | Low | yes | broad refuted (world scheme, Code128); not followed, aligned with plastics a/b (valid GS1 check digit, US/Canada prefix). |
| Terminal control hours / "On time" for 7 min late / question at 06:30 (04, 05) | Low | no | own findings. |
| Demurrage instructions under a vessel definition (03) | Low | yes | logistics finding, context refuted; cannot settle. |
| Generic events / ShippingOrderID / customs authority / FTL elsewhere | - | - | do not arise in 01-05. |

##### Notes for b (after reading b's merged 06-10)
- Aligned: FTL/RAILCONT High no (b 09 F2), payment terms 03 vs 10 High no (b 10 F1), PassengerQuantity 0 Low no (b 08 F22), demurrage Low yes (b 08 F24), terminal control hours Low no (b 07 F7), contacts Low no, registration date Low yes, Italian Low yes.
- Penalty: my 03 F7 (PenaltySurchargePercent for a per-day late penalty) Medium, yes; b's 10 F3 (invoice late-payment interest may differ from the plan's penalty) Low, yes: the two findings are the two sides of the same question and cite each other's values; severities differ because 03 misuses the element, 10 only may differ.
- Difference: the GTIN-like item number 771020000027 (valid GS1 check digit) is a Low/yes finding in 01 F15 (aligned with plastics a/b); it also occurs in 06 (and 11), where no rail 06-11 part raised it.


### rail-merge-decisions-b

#### rail merge decisions, merger B (rail 06-11), run 20261112T2137Z-thorough

FINAL (merged files 06-11 written; check_xpaths/check_values pass). Read rail-merge-decisions-a.md (final), wood-, plastics-, air-merge-decisions-*. Aligned with a on every shared row; differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region (06-11) | Medium | no | move to CountrySubentity. Broad/context said yes, parties no; aligned with a, wood, plastics. |
| LocaleCode `en` (06, 08, 11) | Medium | no | drop (preferred) or en-XB. Recount 364 in 213 files (parts said 362). Same as a. |
| Gate 3 in AdditionalStreetName (06, 08, 11) | Medium | no | drop from postal address. Same as a, air. |
| RegistrationDate 1996-01-01 (Ferrano Rail Cargo 06-10, Hub 07) | Low | yes | not raised by any part; added by the merge, as a. 271 in 181 xml files. |
| GTIN-like item number 771020000027 (06, 11) | Low | yes | not raised by any 06-11 part; added by the merge to align with a (01 F15) and plastics. Check digit recalculated: valid. |
| Contacts not fitting the role (06, 08, 09, 10, 11) | Low | no | role-specific contacts, one finding per example. 11: the supplier's Order desk refuted in the merge (parties: legitimate for a goods invoice following an order); customer contact kept. |
| Terminal control hours (07) | Low | no | own finding, as a (04, 05). |
| Customs border office hours (06, broad) | refuted in the merge | - | train crosses at 13:00-13:20, within the hours (parties); the 17:29 lodgement is the timeline problem. |
| Copied party master data (SecurityListing, CorporateStockAmount, Castrano ServiceProviderParty) | Low | no | drop where unused. 08: Castrano refuted (loading-proof party, pickup place). 11: supplier's own share capital refuted (company law). Same as a. |
| Catalogue/passport item data (06 customs, 11 invoice) | Low | no | own finding, separate from party master data. Same as a (01). |
| Italian text tagged en-XU | Low | yes | cannot settle. Count 217 renderings in 102 files (a's recount). Same as a. |
| Bench emission triple 96 / 0.82 / 1 EA (06, 11) | High | no | 0.82 x 1 = 0.82; 96/0.82 = 117.1, neither bench gross 41.5 kg nor consumption 56.5 kg. Drop factor and base. Same as a. |
| CRADLETOGATE in FullnessIndicationCode (06, 11) | Medium | no | drop; TC write-up. Context said yes. Same as a. |
| LifecycleStageCode MANUFACTURING for A1-A3 (06, 11) | Medium | no | omit code or two entries. Same as a. |
| Shipment GrossWeightMeasure 7968 = goods only (06, 08) | High | no | 2 x 7884 = 15 768; tare 3900/box (40HC ~3.7-3.9 t). 15 768 at shipment level. |
| 96 benches per 45G1 (06 broad Low/yes; 08 logistics Medium/yes) | Low | yes | 0.870 m3/bench, 83.6 m3 > 76.3 m3; best box layout 72 (6x3x4 on the back), upright 54; weight 3984 kg vs ~26.5 t payload is fine. Low in both: rests on the unstated assumption "assembled"; cast-frame benches often ship knocked down. |
| Customs authority as a company (06) | Medium | no | drop company attributes. VAT registration of customs: own Low (as plastics a). |
| FreightForwarderParty = rail carrier (06) | Medium | no | drop. Parties said yes. |
| PreviousCustomsDeclaration = export declaration not in the flow (06) | Medium | yes | gc: "previously sent transit customs declaration". Yes: flow may gain a document. |
| Customs office elements (06) | ImportCustomsExitOffice Marrowdale Medium/no; TransitCustomsExitOffice + OfficeOfEntry Low/yes (contested readings, logistics refuted the first); office IDs Low/no | | |
| Means of transport missing in transit declaration (06) | Low | no | logistics Medium; Low as plastics 05 (world rule unknown). |
| Customs value includes carriage in XB (06, money) | Low | yes | broad refuted; cannot settle. |
| ShippingOrderID = consignment ID (07, 08) | Medium | no | drop or VI-TR-26-0326. Medium, not High as in air: no example states a different shipping-order ID. |
| DocumentReference = consignment ID (07) | High | no | split from ShippingOrderID: a referenced document that does not exist (section 6). Parts had Medium. |
| Generic events instead of dedicated loading event (07) | Medium | no | LoadingTransportEvent 05:40 at the hub. Same as air. |
| Warehouse pickup in main carriage (07) | Medium | no | pre-carriage stage. |
| Optional takeover without reason (07) | Low | no | drop (logistics yes; only option b is story). |
| Locations named after companies (07 StatusLocation/event; 08 IssueLocation, hub) | Low | no | place names + identifiers. Same as a, air. |
| CMR for rail (08) | High | yes | type vs mode 2 in the same doc; CMR art. 2 does not cover containers on trains. Yes: convention is story, option b adds a document (context no). |
| Actual waypoint 13:20 after issue 13:10 (08) | High | no | |
| Customs declaration issuer = customs (08) | High | no | contradicts 06 (Valdara makes and signs). |
| Waybill 13:10 cites declaration issued 17:29 (08) | High | yes | logistics Medium/yes, broad inside its High; parties/context: Outside. Kept as a broken reference; yes because the flow's timeline changes. |
| Distribution vs note (08) | High | no | party contradicts its own distribution type and the note (broad High; parties Medium/yes; context Medium). |
| ContainedInTransportEquipment = wagon (08) | Medium | no | definition governs (semantic conformance); TC write-up for the name/definition conflict. Logistics yes. |
| StorageLocation while loaded (08) | Medium | no | broad Medium, logistics/context Low; misuse rather than hard contradiction. |
| Waypoints without location (08) | Medium | no | |
| EmissionCalculationLocation = office (08) | Medium | no | factor 410/1220 = 0.336 kg/kWh. |
| OperatingParty = hub (08) | Low | yes | parties Medium; broad and logistics refuted; cannot settle. |
| PassengerQuantity 0 (08) | Low | no | drop. Same as a (03). |
| Performing carrier = carrier (08) | Low | no | drop. |
| Demurrage under vessel definition (08) | Low | yes | same as a (03). |
| LegalStatusIndicator false under customs seal (08) | Low | yes | |
| Freight charge on one container only (08) | Low | no | waybill states no total: incompleteness. |
| Note "two containers" vs one referenced (09) | High | no | |
| RAILCONT vs plan FTL (09) | High | no | fix in 03 (a: FTL High no). Logistics yes. |
| Itinerary without places/times (09) | Medium | no | |
| Package KXU104413250000013 unknown (09) | Medium | no; ISO 15459 "K" agency Low/yes (not checkable) | |
| Payment terms 03 vs 10 | High | no | 14 Apr + 30 = 14 May vs 17 May + 2 %. Preferred: invoice follows the agreement (money preferred aligning the plan). Same as a. |
| Penalty 03 vs 10 | 10: Low | yes | money Medium/yes lowered: contradiction depends on reading. a: 03 Medium/yes (element misused either way). |
| AccountingCost "Raw materials and parts" for outbound freight (10) | Low | no | |
| References with ID only (06 plan, 10 waybill) | Low | no | 10: broad's refutation (WB prefix) not followed. Same as plastics, air. |
| EXP without evidence/delivery (11) | Low | no | broad; logistics refuted within lens. |


### air-merge-decisions-a

#### air merge decisions, merger A (air 01-05), run 20261112T2137Z-thorough

FINAL (01-05 merged files written and checked). Read air-merge-decisions-b.md (draft 1), wood-* and plastics-*; aligned on every shared row, differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) | Medium | no | drop LocaleCode (preferred), or a real locale. Same as b, wood, plastics. |
| Gate 3 in AdditionalStreetName of Lumeway's postal address | Medium | no | drop from the postal address; in 03 (pickup arranged) move to Pickup/PickupLocation. Same as b. |
| RegistrationDate 1996-01-01 (25 companies, 181 files, lxml/grep) | Low | yes | own date per company or a story event. Same as b, wood, plastics. |
| Contacts not fitting the role | Low | no | role-specific contacts; one finding per example (broad + parties). Same as b. |
| en-XB vs en-XL tags for island addresses (02, 03, 05; 01 and 04 use en-XL and carry the parties' refutation) | Low | yes | one rule, documented; preferred en-XL for island names. Broad refuted (tag follows issuer): carried as counter-argument. Same as b, wood, plastics. |
| Island party's legal form in one untagged rendering (02, 03, 05) | Low | no | render like the address. Separate finding (parties had it as a remark / refuted separately), for consistency with wood/plastics "Legal form ... in one untagged rendering". b: please align for 06-10 if the same occurs. |
| VT-PO-26-0319 (03) | High | no | VT-OC-26-0320 and/or VT-PO-26-0127 with DocumentTypeCode, as 07 does. Verified: only 03, 06, 08 carry it, as references. Same as b. |
| Line ID 1 = bench line (01, 02) | High | no | new line ID 3 + LineStatusCode Added, carried into 02, 06, 08. Separate from the totals finding in 01 (money had combined them). Same as b. |
| Order change totals 51200.00 vs one line of 512.00 (01) | High (raised from Medium: arithmetic does not hold) | no | totals = amount of change, 512.00 (definition); money's "restate all lines" as option (b). |
| ShippingOrderID = consignment ID LD-CS-26-0324 (04, 05; 09 for b) | High | no | one value in 03/04/05/09; preferred LD-FI-26-0322 (the FI exists; Waybill definition names "Forwarding Instruction"), with 03's own ShippingOrderID (= Shipment ID, Low in 03) dropped; option (b) LD-SH-26-0323 everywhere. b: use this preference for 09 (drop in 09 also acceptable). |
| Waybill referenced before it is issued (05, 10:05 vs 10:43) | High | no | report after 10:43. Refutation attempt (AWB number pre-allocated at booking) fails: the reference is the document ID, the carrier's AWB number is a different value. |
| Status / issue location = company name (04 IssueLocation, 05 StatusLocation) | Low | no | place name + XBLMA. Same as b (09: XLSLA). |
| Signature without signature (02, 03, 04, 05) | Low | yes | convention; drop (preferred) except 04 waybill, where adding method/attachment is preferred (the carrier's signature matters). Count re-made: 137 of 147 Signature aggregates hold only ID + SignatoryParty (lxml, all *.xml). Signature IDs with the example's number (LD-SIG-FI-03, LACT-SIG-TS-05) or doubled prefix (KXL-SIG-KXL-WB-...) noted inside the same finding, as in plastics. |
| Generic event instead of stage event (03 untyped event 13 May 19:00; 05 acceptance) | Medium | no | dedicated element (AcceptanceTransportEvent) with time and location; missing time folded in. Same as b (09 arrival). |
| Exchange rate (03 undated and unused: Low; 04 dated 2026-05-20 after issue 2026-05-13: High; 04 unused: separate Low) | as stated | no | drop the rate. |
| AdValoremIndicator false (03) vs true (04) | High in both | no | leave out of both (definition is about duties; neither document deals with them); option same value by Lisavu duty. Context's valuation-charge reading kept in Why only. |
| ConsolidatedIndicator false with ConsolidatedShipment + ChildConsignment (04) | High | yes | direct air waybill, drop consolidation data. |
| Box 0.072 m3 for 0.42 m3 of frames (03) | High | no | 8 boxes or one 0.576 m3 crate (matches waybill 96 kg chargeable). 04 chargeable-weight finding Low, no (follows 03). |
| Missed-flight story (04 flight KXL207 14 May vs 07 "next day's flight", 09 arrival 14 May) | 04: Low, yes (logistics High lowered) | yes | same reading as b: a 13 May flight was missed (07 cites KXL-OFFLOAD-26-0513), KXL207 on 14 May is the replacement; contradictions sit in 07 (timing vs 08, 09), findings of 07/09 for b. In 04 what remains is that the waybill does not show it is the replacement booking. |
| NoStatus DocumentStatusCode (03) | Low | no | drop. Added by the merge (no part raised it), as b did for 06/08. |
| Copied master data / XU national tariff code in 01 | Low | no | drop; broad refuted (origin country, original order has it), carried as counter-argument. |
| "Send the bill of lading" in air FI (03) | Medium | no | drop. Count corrected: 4 files (air/03, cotton/09, sea/09, sea/12). |


### air-merge-decisions-b

#### air merge decisions, merger B (air 06-10), run 20261112T2137Z-thorough

FINAL (06-10 merged files written and checked). Read air-merge-decisions-a.md (final), wood-* and plastics-*; aligned on every shared row, differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) | Medium | no | drop LocaleCode (preferred), or a real locale. Same as a, wood, plastics. |
| Gate 3 in AdditionalStreetName (Lumeway's postal address) | Medium | no | drop from the postal address; gate only in a despatch/pickup location where it matters. Same as a. |
| RegistrationDate 1996-01-01 | Low | yes | own date per company, or a story event. Same as a, wood, plastics. |
| Contacts not fitting the role (Purchasing / Goods inwards = CSO in Sales; Cargo sales = Operations planner; invoice contacts = export desk / customer service) | Low | no | role-specific contacts. One finding per example, grouping broad and parties; the invoice-party contacts (10) are a separate Low (billing role, not name/title clash). Same as a. |
| en-XB vs en-XL tags for island addresses (06, 07, 08, 10) | Low | yes | one rule, documented. Broad refuted (tag follows issuer); cannot settle, so finding Low/yes with both arguments. Same as a. |
| VT-PO-26-0319 (06, 08) | High (verified: no example has the ID; 07 names VT-OC-26-0320 / VT-PO-26-0127 for the same despatch) | no | VT-PO-26-0127 with the order change as DocumentReference, as in 07. Same as a. |
| Line ID 1 = bench line (06, 08 OrderLineReference) | High (verified: sea/05 line 1 = 96 benches; 01's own line 1 = 8 frames, which reuses the bench line's ID) | no | follow 01's fix (new line ID 3). Separate finding from VT-PO-26-0319 (context part merged them): different element, different fix. Same as a. |
| ShippingOrderID = consignment ID (09) | High (verified: 03 says LD-SH-26-0323, 04/05/09 LD-CS-26-0324) | no | one shipping-order ID in 03/04/05/09; preferred LD-FI-26-0322 as a; LD-SH-26-0323 everywhere and drop in 09 as options. Same as a. |
| Status location = company name (09 StatusLocation) | Low | no | place name + XLSLA. Same as a (05: XBLMA). |
| Signature without signature (07, 09; context only) | Low | yes | drop; convention across many examples. Count 137 of 147 (lxml), as a. Same as a. |
| Generic event instead of stage event (09 arrival) | Medium | no | MainCarriageShipmentStage/ActualArrivalTransportEvent with time and XLSLA. Same as a. The missing time (logistics Low) folded in. |
| Consignment note in air freight (06, 08 Note) | Low | no | "air waybill". Logistics refuted ("air consignment note" is the Warsaw term); partly survives: the flow's document is the air waybill and the note says "consignment note" without "air"; kept Low. |
| Missing despatch / delivery dates in the despatch advice (06, 08) | Medium (despatch advice purpose depends on it; same as wood b, plastics b) | no | Shipment/Delivery with actual despatch + estimated delivery; waybill reference / SSCC. Broad's Low raised to Medium (logistics Medium). |
| NoStatus DocumentStatusCode / LineStatusCode (06, 08) | Low | no | drop. Not raised as a finding by any air part (08 context cites it as evidence); added by the merge for consistency with wood/plastics. |
| Replacement despatch advice (08) identical to 06 apart from dates; cancellation (07) without visible reason | Low in both (07 context's Medium lowered: cancel-and-reissue is a legitimate use; missing data is plausibility) | yes | the flow's story: either 06/08 carry flight-dependent data, or replace 07+08 by a transport status. |
| Cancellation timing (07 note "follows today" 17:53 vs 08 issued 10:48) | High | no | issue replacement after cancellation, or reword note. One finding in 07, one in 08 (each side cites the other). |
| Missed-flight story (07 "next day's flight" vs 09 arrival 14 May, waybill flight 14 May 07:00) | High | yes | settle once; preferred: a flight on 13 May was missed, the cargo flew KXL207 on 14 May; 07 issued on 13 May. Finding in 07 and in 09. |
| Serial numbers with two manufacture dates (06 10 May / 08 11 May) | High | no | 10 May in both. Finding in both. |
| Chargeable weight (10) | High (redone: 0.576 m3 x 1e6 / 6000 = 96.0 kg > 81.6 kg gross; 96 x 6.8 = 652.80; penalty 9.79) | no | invoice 96 KGM. |
| Statement reference BF-SOA-26-05 (10) | Low (money said High) | yes | drop. A statement outside the flow is not a broken in-flow reference; that it is the May statement is an inference from the ID, so cannot be settled. |
| Copied master data (Port of Selanu originator/beneficiary in 07; carrier master data in 10; HeadOfficeParty in 09 Medium/yes) | Low (HeadOfficeParty Medium, yes) | no (HeadOffice yes) | drop. |
| Island party's legal form in one untagged rendering (06, 07, 08, 10; not 09, island-issued) | Low | no | render like the address (10: drop with the carrier's master data). Separate finding, as a asked and as wood/plastics (parties had it as a remark in its tag finding). |
| Copied XU national tariff code (06, 08) | Low | no | drop; broad's refutation (only national list, XU origin) carried as counter-argument. Same as a (01). |
| Delivery-slot instruction without a stated slot (09) | Low | no | state the slot or drop. Same as a (05). |

No finding was refuted outright in 06-10 ("Refuted in the merge" empty in all five). Differences from a: none on shared rows.


### utilities-merge-decisions-a

#### utilities merge decisions, merger A (utilities 01-07), run 20261112T2230Z-thorough

FINAL (merged files 01-07 written; check_xpaths/check_values pass). Read utilities-merge-decisions-b.md (final) and wood-, plastics-, air-, rail-, energy-, packaging-merge-decisions-*. Aligned with b on every shared row; changes since draft 1 marked CHANGED.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Due date vs "30 days net" note (02, 06: issue 2026-04-02, +30 = 2026-05-02, given 2026-04-23 = +21; 06 penalty period from 2026-04-24) | High | no | CHANGED preference, now aligned with b's reasoning for 13: due dates 2026-05-02 (06: penalty from 2026-05-03), because XU-STD means 30 days in all 12 other invoices that carry it, and XB-STD in 14 of 15 outside this flow (mast/05: 45 days); option (b) note "21 days net" with its own terms ID kept. 09's XB-STD note "Collected by direct debit 21 days after the invoice date" is the in-flow outlier for b. |
| AverageAmount = current month's amount while the description gives a 3-month average (01, 03, 05) | High | no | 01: (10876320+11059230+11269440)/3 = 11068330; 03: 488670; 05: 192.70 (all redone). b: 08 coincides (not a finding). |
| CustomerParty = ReceiverParty (01, 05; not 03) | Medium | no | drop. Same as b. |
| SupplierConsumption with one supplier (01, 03, 05) | Medium | yes | record model issue (ConsumptionLine only under SupplierConsumption) + Consumption only or real 2nd supplier. Same as b. |
| SubscriberID = contract number (01, 03, 05) | Low | yes | Same as b. In 03 the subscriber conflict (Castrano as subscriber, Valdara's ID/contract, contradicts 01) is its own High/yes finding (parties High; others Medium). |
| SubscriberType/Code on UtilityItem = utility | Low | yes | Same as b. |
| Filler descriptions / delivery location | Low | no | Same as b. |
| One-time charge type on the monthly kWh item (01) | Medium | no | drop. |
| Energy tax: 01 reports the invoice's 288840 for one point (needs 431400 kWh; factory alone <= 277680); 03 reports none; both statements' totals omit excise + VAT on it | 01: two High (amount; totals), 03: High (totals; broad's Medium raised) | no | per-point share and totals incl. excise and VAT. |
| Excise PerUnitAmount 1 vs 60000/228840 (02) | High | no | 1.2 / 0.6 (redone; gas-inclusive and per-meter readings do not give 288840). TaxableAmount = TaxAmount: own Medium. |
| Estimate correction in 03 (27 x -750 = -20250 != -20475; correction double-counts and is applied nowhere; district-heating element definitions) | High no / High yes / Medium no | | three findings. |
| SupplyTypeCode SERVICES for electricity, gas, water (02, 06) | Medium | no | GOODS per world list. Same as b. SERVICES on the levy line (06): Low/no, own finding (same as b). |
| Category O with 0 % (06) | Low | no | drop Percent. Same as b. LEVY exemption reason on O (06): Low/yes, own finding (same as b). |
| BeneficiaryParty = CollectedForParty (06, broad) | refuted in the merge | - | parties/context: two definitions, both true; nothing implied by absence. b: please align for 09/11 if raised. |
| Sewage levy not in the statement's payable amount (05) | Low | yes | CHANGED: money's Medium lowered, three parts refuted it (levy collected for the city); cannot settle. Preferred: a note in the statement. Same question in 08 (b). |
| Remittance ID VI-RM-26-0316 shared by 04, 07, 14 | High in 07 (and 14) | no | In 04 (Valdara's own number) under "Outside this review". Same as b. |
| Payment-order references ...0313 (07) | Low | no | own finding (with the PayerReference duplication). Same as b (14). |
| PaymentOrderReference vs PayerReference with two values (04) | Low | yes | broad finding, logistics refuted (payables voucher); cannot settle. |
| Purpose code SUPP vs ELEC/GASB/WTER (04, 07) | Low | no | invoice's code. Same as b. |
| Province in Region (01-04) | Medium | no | CountrySubentity. Recount 219 in 104 files. |
| LocaleCode en (05, 06, 07) | Medium | no | drop. Recount: 364 occurrences in 213 files (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<' | wc -l`); b and the parts said 362, the rail merges 364. |
| RegistrationDate 1996-01-01 (+ SMALL for the water company) (03 Castrano; 05, 06, 07 water company) | Low | yes | Same as b. Recount 271 in 181 files. |
| Contacts not fitting the role | Low | no | own finding per example, split from master data. |
| Copied master data (customs trader ID, SecurityListing, ServiceProviderParty, marketing data) | Low | no | ServiceProviderParty Castrano refuted in 02 (line 2 is its warehouse) and in 03 (with ShareholderParty: explains the arrangement); kept in 01 and 04. |
| Cost centres ("Raw materials and parts" 3100 for energy in 01, 02; "Garden department" in 05, 06) | Low | no | Garden: 16 occurrences in 12 files. In 03 the cost centre contradicts invoice line 2 (7100): High/no. |
| Signature without method (04, 07) | Low | yes | Same as b and air (137 of 147, lxml). broad said no; context (04) refuted. |
| AdditionalDocumentReference with ID only (04, 07) | Low | no | Same as b. |
| Italian text tagged en-XU (streets, legal form) (01-04) | Low | yes | ADDED by the merge (no part raised it; parties refuted it in 01 as proper names) for alignment with wood/plastics/rail. b: Bayvarran/Lisavan parties in 08-14 may not have it. Recount 217 street renderings in 102 files, 112 tagged legal forms. |
| Water meter "Maximum flow" 2.5 m³/h = Q3 (05) | Low | no | same property in 08 (b). |
| Refuted in the merge | | | only 06 broad/F6 (BeneficiaryParty). |


### utilities-merge-decisions-b

#### utilities merge decisions, merger B (utilities 08-14), run 20261112T2230Z-thorough

FINAL (merged files 08-14 written; check_xpaths/check_values pass). Read utilities-merge-decisions-a.md (draft 1, unchanged at 23:13) and wood/plastics/air/rail/energy/packaging decisions. Aligned with a on every shared row; one difference of preferred option explained (13 due date).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Payments on account in 08 (monthly direct debit, settled by the bill) vs invoice 09 billing and collecting the full 38.78 with no PrepaidAmount, 21 days after issue; 10 treats the 23 April debit of 38.78 as the only one | High (08 and 09) | yes | (a) drop OnAccountPayment/MainOnAccountPayment from 08 (09, 10, 11 already follow monthly billing on the reading). One finding in 08 and one in 09, each citing the other. |
| Mandate 09: MaximumPaymentInstructionsNumeric 12, open validity from 2024-09-02, RCUR, monthly bills: about 19 monthly collections Oct 2024 to Apr 2026 | Medium (broad High lowered) | no | drop the limit. Lowered: the contradiction rests on the assumption that every month since 2024 was collected under this mandate; no value states it. |
| Due date vs terms note (13: "45 days net", +45 = 2026-05-17, given 2026-04-23 = +21) | High | no | note and due dates state the same term. DIFFERENCE from a's preference (note '21 days net' for 02/06): in 13 I prefer due dates 2026-05-17, because the same terms ID XL-STD means 45 days in cotton/04-SelfBilledInvoice.xml (issued 2026-02-07, due 2026-03-24); XB-STD of 02/06 is defined nowhere else. Both options kept. 09: note and due date agree (checked). |
| AverageAmount = current month | not a finding in 08 | - | 08: (35.25 + 30.55 + 32.90) / 3 = 32.90 = March's amount by coincidence (quantities 15, 13, 14 average 14). Under "Checked". |
| CustomerParty = ReceiverParty (08, 12) | Medium | no | drop. Same as a. |
| SupplierConsumption with one supplier (08, 12) | Medium | yes | Same as a (model issue: ConsumptionLine only under SupplierConsumption). |
| SubscriberID = contract number (08, 12) | Low | yes | Same as a; context Medium/no and logistics Low/no noted. |
| SubscriberType/Code on UtilityItem = utility (08 Water, 12 Telephone) | Low | yes | Same as a. |
| Filler descriptions / delivery location (08, 12) | Low | no | Same as a. |
| Remittance ID VI-RM-26-0316 (14, Velumi) | High | no | Same as a. Payment-order refs ...0313 (14): Low/no, own finding. |
| SUPP vs PHON (14) | Low | no | Same as a. |
| SupplyTypeCode SERVICES for water (09, 11) | Medium | no | GOODS per world list. Same as a. SERVICES on the levy line (09, 11, context only): own Low/no (a levy is no supply). Telecom SERVICES (13): refuted (context). |
| Category O with 0 % (09, 11 levy; 12, 13 telecom) | Low | no | drop Percent. Same as a. TaxExemptionReasonCode LEVY on O (09, 11, broad): Low/yes (EN 16931 vs UBL), own finding. |
| LocaleCode en (08-11) | Medium | no | drop. Recount 362 in 213 files. |
| RegistrationDate 1996-01-01 + SMALL (water company 08-11; Selanu Telecom + Velumi 12-14) | Low | yes | Same as a and earlier flows. Recount 271 in 181 files. |
| Contacts (Velumi "Purchasing"/Customer service officer/Sales in 12, 13, 14) | Low | no | Same as a. |
| Copied master data (Robin's bank account under Person in 08, 09, 10, 11; Velumi's customs trader ID in 12, 13, 14) | Low | no | drop where unused. 11: account refuted by broad/money/parties (refund "unless refunded"); context's finding (settlement not stated) kept Low/yes. 10: parties refuted (account of the returned debit); kept Low/no with both arguments. |
| Cost centres: Velumi "500 Stock for municipal projects" for telecom (12, 13); water company's own ledger accounts in 10 (buyer's AccountingCost) | 12/13 Low/no; 10 Medium/no | | 10 is a different problem (seller's accounts in buyer's element = meaning other than definition), all parts Medium. Count: 10 occurrences in 9 files. |
| Signature without method (08, 10, 14) | Low | yes | Same as a and air (137 of 147 aggregates, lxml). broad said no. |
| BlockchainID on a current account (13, 14) | Medium | yes | drop. Broad Low, money/context Medium: definition ("crypto or stablecoin being held") not met by a CACC IBAN account. |
| AdditionalDocumentReference with ID only (14 VT-BANK-26-04; 08 guidance/quality refs) | Low | no | Same as a. |
| 6 MON for six lines of one month (12, 13) | Low | no | money Medium, logistics Low; Low because 6 line-months is arithmetic-consistent, only ambiguous against the period. Count unit C62 preferred. |
| PrivacyCode MASKED with full called number (12) | High | no | world list: "last digits replaced". broad Low, context High. |
| 35 GB twice (12) | High | yes | |
| Line totals ignoring line allowances; allowance 2.400 on a call priced 0 (12) | High | no | redone: 21.180-1.059=20.121; 127.080-6.354=120.726; 0-2.400 != 0. |
| Nothing refuted outright in 08-14 ("Refuted in the merge" empty). Part refutations I disagreed with became findings with both arguments: 08 bank account (parties), 08 password (context, Low/yes), 09 Person account (money), 10 account (parties), 11 CollectedForParty (context), 11 settlement (context's finding kept against broad/money/parties), 13 line references (context). | | | |


### road-merge-decisions-a

#### road merge decisions, merger A (road 01-06), run 20261112T2311Z-thorough

FINAL (merged files 01-06 written; check_xpaths/check_values pass). Read rail-, air-merge-decisions-*, road-merge-decisions-b (draft 1) and -c (draft 1). Aligned on every shared row; differences explained. Counts re-made over *.xml (grep, from world/examples).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region (01-06) | Medium | no | CountrySubentity. 219 occurrences in 104 files. |
| LocaleCode `en` (01-06) | Medium | no | drop (preferred) or en-XB. Parties said yes; aligned no. Count 362 in 213 files with `grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>'` (c counted 364 with another pattern). |
| Gate 3 in AdditionalStreetName (01-06) | Medium | no | drop from postal address; 01 DeliveryAddress and 03 ToLocation: move to a delivery location/description. 79 in 76 files. |
| RegistrationDate 1996-01-01 (Castrano, Trasvia: 01, 03, 04, 05) | Low | yes | own date. Parties said no; aligned yes (rail, air, b, c). 271 in 181 files. Only where parties raised it (as b). |
| Contacts not fitting the role | Low | no | one finding per example; customs/chamber "Public service officer" folded in (05, 06). |
| Customs border office hours 08-17 vs truck at border 07:30, examined 07:45 (05) | Low | no | parties; contact hours != office hours keeps it Low. |
| Copied party master data (SecurityListing, CorporateStock, ShareholderParty, carrier PartyAuthorization) | Low | no | drop. Castrano ServiceProviderParty refuted (pickup at its warehouse), as rail/b. Carrier permit: parties refuted (qualifies carrier), kept as weakest part with the argument. |
| Catalogue/passport item data (01, 04, 05, 06) | Low | no | own finding, separate from party data (rail, b, c). 01 added by the merge. |
| Bench emission triple 96 / 0.82 / 1 EA (01, 04, 05, 06) | High | no | drop factor and base (preferred, as rail, c); context's Medium raised. |
| CRADLETOGATE in FullnessIndicationCode | Medium | no | drop; TC write-up. |
| LifecycleStageCode MANUFACTURING vs A1-A3 text | Medium | no | context said High; lowered as rail, b, c. |
| GTIN-like item number 771020000027 (01, 04, 05, 06) | Low | yes | check digit recomputed (7): valid. |
| Italian street names / legal forms tagged en-XU/en-XB (01-06) | Low | yes | added by the merge from parties' (and 01 broad's) refutation, aligned with rail and c. 01/03: the en-XB vs en-XU subtag question (rail's separate Low/yes) folded into the same finding. |
| Urvanian legal form in one untagged rendering in Bayvarra-issued documents (01, 03) | Low | no | added by the merge, aligned with rail, air, c. |
| NoStatus (03 DocumentStatusCode; 04 DocumentStatusCode + both LineStatusCodes) | Low | no | drop. Added by the merge, as rail/air. Refuted for 02 line 1: in an order response with a revised line 2, NoStatus says "unchanged" (broad/context checked it). |
| Despatch time vs issue time (04: actual 16:20, issue 15:15) | High | no | verified. Merged with logistics' "despatch (pickup) = 15:05" (Medium): preferred ActualDespatchTime 15:05 (definition says pickup; 08 and 09 say pickup 15:05; then 15:15 issue is after it). Broad's refutation (despatch = truck leaving) not followed. 08 issued 08:16 reports 15:05/16:20 as actual: 08's problem (Outside here). |
| Export declarant (05: Valdara declares itself; 08 "declared by the 3PL", 08 IssuerParty = customs) | High | yes | preferred: waybill follows the declaration (exporter declares). Customs as issuer in 08 used as second contradiction; the element error itself is 08's. |
| Customs as a company (05) | Medium | no | drop commercial register + liquidation status. Customs VAT registration refuted (parties). |
| Chamber as a company (06) | Low | yes | legal nature of the chamber open. |
| Substitute casting (02: proposed substitute = 2025 "from stock" while notes say replaced) | Medium | no | drop proposed substitute. Broad Low/yes, context High; "no longer made" and "from stock" can both be true, so no hard contradiction; but substitute = ordered item misfits the definition. |
| 2026 casting not identified (04) | Low | no | ExtendedID 2026 (as c). Considered and refuted for 05 and 06: version irrelevant for customs value, HS, origin. |
| ResponsibleParty = Castrano (02) | Medium | no | Trasvia or drop. |
| Promised delivery 23 Mar vs guaranteed despatch 24 Mar (02) | Medium | no | logistics Low, context High; target vs outer limit is no hard contradiction. |
| Locations named after companies (03) | Low | no | place names + identifiers. |
| ID-only references (02, 05, 06) | Low | no | type code. |
| Signature IDs with flow name / example number (05 VI-SIG-EX-road, 06 VI-SIG-CO-06, VI-SIG-COA) | Low | no | signer's numbering. Same as b (no). c has yes for a signature with ID + signer only and an ID from the type name (16), following air's "signature without signature" convention; here the parts' finding is the ID, an encoding fix, so no; the empty signature is mentioned with air's option (drop). |
| Two CoO documents with same ID and version (06/07) | High | no | aligned with b: separate IDs preferred (application gets Valdara's own ID), VersionID 2 as option. Context's yes set to no. Refutation attempt (pre-numbered chamber forms) recorded. |
| Endorsement order (06: insurer #2 Endorsed, chamber #1 Pending) | High | no | context High, parties Low. Preferred: drop the insurance endorsement (tied to the Low/yes insurance finding). 07 has embassy and insurer both #2 (Outside, for b). |
| Insurance endorsement without role (06) | Low | yes | |
| OriginalJobID = PO (06) | Medium | no | |
| PreviousJobID (06) | Low | no | |
| SignatoryContact definition (06) | Low | yes | context; broad's refutation (UBL defect) carried; TC write-up. Desk names (parties) separate Low/no. |
| Customs values on CoO (06) | Low | yes | money. |
| Handling units only in text (03) | Low | no | logistics; broad/context refuted as missing info; kept as completeness remark (21 single-stacked pallet places < 24 on 13.6 m). |
| RegistrationID on castings (04) | Low | yes | context; broad refuted (distinct concepts, warranty); cannot settle. |
| Maximum delivery unit 100 (01) | Low | no | context Medium lowered (a delivery may hold several batches). |
| ShippingOrderID = consignment ID | - | - | only in 08/09 (merger b). |


### road-merge-decisions-b

#### road merge decisions, merger B (road 07-12), run 20261112T2311Z-thorough

FINAL (merged files 07-12 written; check_xpaths/check_values pass). Read rail-, air-merge-decisions-a/-b and road-merge-decisions-a (draft 1) and -c (draft 1). Aligned with a and c on every shared row; differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region (07-12) | Medium | no | CountrySubentity. 104 files. |
| LocaleCode `en` (07-12) | Medium | no | drop (preferred) or en-XB. Parties said yes; aligned no. 362 in 213 files (c counts 364 with another grep). |
| Gate 3 in AdditionalStreetName (07-12) | Medium | no | drop from postal address; 08 has its own delivery instruction (dock 4). |
| RegistrationDate 1996-01-01 (08, 09 Trasvia; 11, 12 Castrano) | Low | yes | parties said no; aligned yes. |
| Contacts not fitting the role (07-12) | Low | no | one finding per example; chamber/customs "Public service officer" folded in (as a). |
| Customs border office hours 08-17 vs border at 07:30 (10, parties) | Low | no | own finding, as a (05). |
| Copied party master data (SecurityListing; 09 carrier permit; 10 ServiceProviderParty Castrano) | Low | no | drop. ServiceProviderParty refuted in 07 (warehouse = where goods leave), kept in 10 (import has no use). Castrano ShareholderParty (11, 12 context) refuted in the merge, as c (13). Carrier permit in 08 waybill: context checked as justified (international haulage); in 09 status: Low finding. |
| Catalogue/passport item data (07, 10, 11) | Low | no | own finding, separate from party master data. |
| Bench emission triple 96 / 0.82 / 1 EA (07, 10, 11) | High | no | drop factor and base preferred (as rail; broad/logistics preferred a real factor, kept as option). Context's Medium raised. |
| CRADLETOGATE (07, 10, 11) | Medium | no | drop; TC write-up. |
| LifecycleStageCode MANUFACTURING (07, 10, 11) | Medium | no | context High lowered, as a, c, rail. |
| GTIN-like item number (07, 10, 11) | Low | yes | recomputed: valid. |
| 2026 casting not identified (07, 10: added by the merge; 11: logistics) | Low | no | ExtendedID 2026. Same as a, c. |
| Italian street names / legal forms tagged en-XU/en-XB (07-12) | Low | yes | added by the merge from parties' refutation, aligned with c and rail. |
| Urvanian legal form in one untagged rendering (10, 11, 12: Bayvarra-issued) | Low | no | added by the merge, aligned with c, rail, air. Not in 07-09 (Urvania-issued). |
| ShippingOrderID = consignment ID (08, 09) | Medium | no | LD-TR-26-0151 (transport request) or drop. Medium as rail b: no example states a different shipping-order ID. |
| Customs as issuer of the export declaration (08 IssuerParty) | High | no | parts had Medium; raised as rail b: contradicts 05 (Valdara makes and signs). |
| Export declarant in the waybill text (08 "declared by the 3PL") | High | yes | aligned with a (05 High yes) and broad/logistics; context said no. Preferred: text follows 05 (seller declares, FCA). |
| Customs as a company (10 CustomsParty) | Medium | no | drop commercial register + liquidation status. Same as a (05), rail b. |
| Chamber as a company (07) | Low | yes | same as a (06). |
| Locations named after companies (08 IssueLocation, 09 StatusLocation) | Low | no | logistics/parties had Medium for 09; aligned Low with rail/air. |
| Signature IDs with flow name / example number (07 FCC-SIG-CO-07, VI-SIG-COA; 09 TH-SIG-TS-09; 10 LD-SIG-IM-road) | Low | no | signer's own numbering. Same as a. |
| ID-only references (07 SupportingDocumentReference; 09 waybill) | Low | no | 09: context refuted, not followed (as rail, c). |
| Documents reporting events after their issue time (08 waybill 08:16: pickup 15:05, departure 16:20, exam next day, transit end, fuel) | High | no | issue at takeover after 15:15. |
| Waybill 08:16 cites export declaration (13:25) and despatch advice number (15:15) | High | no | added by the merge as own finding (rail b had the same as High/yes); no here because F1's fix (issue after 15:15) resolves it without changing the story. |
| Import declaration accepted/released (09 at 08:55) before it is issued (10 at 09:54) | High | no | pre-lodge the declaration. Finding in both 09 and 10. |
| CoO 06/07 same ID and VersionID 1; 10 reference resolves to both | High | no | preferred (aligned with a): version 2 for the approved certificate; option own application ID. 07 F1, 10 F3 (context Medium, logistics Low raised). |
| Endorsement sequence numbers (07: legalisation and insurer both 2) | Medium | no | a has High for 06 (insurer #2 Endorsed while chamber #1 Pending: status vs sequence contradiction). In 07 the problem is two equal numbers, which can be read as parallel: Medium. |
| Embassy endorsement by the Trade Accord Council (07) | Medium | yes | parties Medium; broad/context Low. |
| Insurance endorsement without role (07) | Low | yes | same as a (06). |
| OriginalJobID = PO (07) Medium no; PreviousJobID (07) Low no; SignatoryContact definition (07) Low yes; desk names Low no; customs values on CoO (07) Low yes | | | same as a (06). |
| CMR waybill as delivery note (11 DeliveryNoteDocumentReference) | Medium | no | same as c (13). |
| Waybill physics (08) | | | volume 48.48 m3 vs 41.5: High. Trailer fit: 1.65 m units, STACK2 -> 3.30 m > ~2.7 m inner height; single layer 14.8 m > 13.6 m: Medium, yes (rests on own knowledge of trailer height). 4 assembled benches (1800x620x780) per 1850x650x1650 pallet: 2 layers = 1560 + ~150 > 1650: Medium, yes (rail b had Low/yes for benches in a box; here the gap is a factor of two in height and the packaging says whole benches). Weights 4106.4 = 3984 + 122.4, tare 344.4 kg: consistent. |
| ISO 15459 agency "K" not verifiable (08) | Low | yes | as rail b. |


### road-merge-decisions-c

#### road merge decisions, merger C (road 13-17), run 20261112T2311Z-thorough

FINAL (merged files 13-17 written; check_xpaths/check_values pass). Read utilities-, rail-, air-, plastics-, packaging-merge-decisions-* and road-merge-decisions-a/-b (both DRAFT 1). Aligned with a/b on every shared row; differences explained in the rows.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Province of Ferrano in Region (13-17) | Medium | no | CountrySubentity. Recount 219 in 104 files. |
| LocaleCode `en` (13-17) | Medium | no | drop (preferred), or en-XB. Parties said yes; aligned no with all earlier flows and road a/b. Recount 364 in 213 files (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<'`); parts and road a said 362. |
| Gate 3 in AdditionalStreetName (13-17) | Medium | no | drop from postal address. 79 in 76 files. |
| RegistrationDate 1996-01-01 (13 Castrano, 14 Trasvia) | Low | yes | parties said no; aligned yes. 271 in 181 files. |
| Contacts not fitting the role | Low | no | own finding per example, split from master data (context grouped them). |
| Copied party master data (SecurityListing, ServiceProviderParty Castrano, PartyAuthorization of Trasvia in the invoice) | Low | no | drop where unused. 13: Castrano's ShareholderParty (context) taken out of the finding: it explains why Castrano despatches for Valdara (parties checked); ServiceProviderParty in 13 not raised. |
| Catalogue / passport item data (Keyword, Warranty, CircularityProfile) in 13, 15 | Low | no | own finding, separate from party master data (as rail). |
| Bench emission triple 96 / 0.82 / 1 EA (13, 15) | High | no | 0.82 x 1 = 0.82 != 96; 96/0.82 = 117.1. Drop factor and base preferred (as rail); broad/logistics preferred a real factor, kept as option. Context's Medium raised. |
| CRADLETOGATE in FullnessIndicationCode (13, 15) | Medium | no | drop; TC write-up. |
| LifecycleStageCode MANUFACTURING for A1-A3 text (13, 15) | Medium | no | context said High; lowered to align with rail a/b (Medium). |
| GTIN-like item number 771020000027 / ...034 (13, 15) | Low | yes | check digits recomputed: valid. Same as rail, plastics. |
| 2026 casting not identified (13 receipt line 2, 15 invoice line 2) | Low | no | ExtendedID 2026. Same as a (04); b 'to fill'. Verified: ExtendedID 2026 only in 02 in this flow. |
| Freight invoice 14 (2026-03-25 11:07) cites receipt advice LD-RA-26-0164 (2026-03-26 10:48) | High | no | verified; refutation (pre-allocated number) fails. Preferred: drop the ReceiptLineReference (logistics; also resolves the line-1-only finding); option: issue after 2026-03-26 10:48 (broad). |
| Three-way match 16 at 06:12 before delivery 09:40 and before any receipt advice | High | no | verified; also the issue time 12:55 precedes the first receipt (15:40). Preferred: respond after 2026-03-26 10:48. |
| Payment exchange rate XUF->XBL with payment currency XUF (15) | High | no | broad Medium raised (money High): contradicts PaymentCurrencyCode in the same document. Drop the rate. |
| ID-only references (14 waybill, 16 invoice) | Low | no | DocumentTypeCode. 14: context refuted (carrier's own note), kept with counter-argument. |
| Signature with ID + signer only, ID `LD-SIG-26-AR` from the type name (16) | Low | no | CHANGED from draft (yes): aligned with road a/b (ID is encoding: no); air/utilities' yes for empty signatures noted in Why, drop kept as option (b). |
| Invoice referenced twice in the remittance line (17) | Low | no | context finding; broad refuted ("adds the document type, harmless"), not followed: the billing reference could carry the type itself. |
| Italian street names / legal forms tagged en-XU or en-XB (13-17) | Low | yes | added by the merge from the parties' refutation, aligned with utilities a, rail a/b, packaging. 217 renderings in 102 files. DIFFERENCE: road a/b have no row; the parties part refuted it in every road example, so a/b may not carry it; I follow the earlier flows. |
| Urvanian legal form in one untagged rendering in Bayvarra-issued documents (13, 16, 17) | Low | no | added by the merge, aligned with rail a, air, wood, plastics. |
| Category O with Percent 0 (14) | Low | no | added by the merge, aligned with utilities a/b. |
| DeliveryNoteDocumentReference = CMR waybill TH-WB-26-0159 (13) | Medium | no | logistics. Same value in 11-ReceiptAdvice (b: 'to fill'; please align: Medium/no, preferred AdditionalDocumentReference with the waybill type). |
| Revised receipt advice without reference to LD-RA-26-0162 (13) | Low | no | context said Medium; broad/logistics Low. The cancellation 12 carries the link. |
| Over-supplied side frame never settled (13) | Low | yes | money only. |
| 109 packages received vs 108 on the CMR (13) | Low | yes | broad finding, logistics refuted; cannot settle. |
| Freight on receipt line 1 only (14) | Low | no | |
| Buyer's stock cost code on the carrier's invoice (14) | Low | yes | context finding; broad and money refuted (landed cost, IAS 2); context's point (the transport request gave no code) stands. |
| DocumentResponse Issuer/Recipient reversed or redundant (16) | Low | yes | broad + parties; context's "checked" reads them as the response's parties (counter-argument). |
| Payer account alias "Lumeway receivables" (17) | Low | no | drop. |
| Line-level accounting parties repeat header (17) | Low | no | |

Counts: Refuted in the merge: 0 in 13-17. Considered and refuted (merged files): 13: 8, 14: 9, 15: 9, 16: 6, 17: 8.


### contest-merge-decisions-a

#### contest merge decisions, merger A (contest 01-08), run 20261112T2358Z-thorough

FINAL (merged files 01-08 written; check_xpaths.py and check_values.py pass: all XPaths resolve, 351 values match). Re-read b (still draft 1) before finalising: aligned on every shared row. Province in Region and en-XB-tagged text do not occur in 01-08 (no cbc:Region, no languageID). Read contest-merge-decisions-b.md (draft 1) and road-, utilities-, air-, rail-, wood-, plastics-, energy-, packaging-merge-decisions-*. Aligned with b on every shared row (changes from my draft 1 marked ALIGNED).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (all) | Medium | no | drop LocaleCode (preferred) or a real locale (en-XB). Recount: 362 cbc:LocaleCode in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`); a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also hits other *LocaleCode elements. |
| Public bodies (PWD, Information Service, Review Board) as COMMERCIAL-register companies with liquidation status | Medium | no | drop CompanyLiquidationStatusCode and the COMMERCIAL type (keep register name/ID), or a public-body register type. Same as b and customs in earlier flows. Parties (Medium/yes), broad (Low/yes), context (Low/no). "City of Lumeport as the legal entity" kept as option (that one would change the story). In 05-07 only the PWD is a public body. |
| Customs-trader ID of the contracting authority, and the economic operators' own tax schemes (04-07), in procurement documents | Low | no | drop where unused. ALIGNED with b (operator tax schemes folded in). Context refuted the operators' tax schemes (05, 06, 07: a qualification may check the tax registration); carried as counter-argument. |
| PartyTaxScheme of the contracting authority itself | Low | yes | ALIGNED with b: own finding. Money refuted (exemption tells candidates amounts are net of sales tax); broad/context/money(05-07: "neither prices nor pays") found it copied. |
| PUBLIC exemption text "Sale to a public body: ..." | Low | no | ALIGNED with b: own finding; reword text to the party's status; code fits (list description is a buyer status). Money's refutation of the code carried. |
| Contacts not fitting the role (Review Board "Registry"/Procurement officer in 03, 04, 08; Brackenmere "Trade sales"/Customer service officer in 04-07; Saltmere "Bids office"/Procurement officer in 07) | Low | no | one finding per example (broad + parties + context's separate findings merged). |
| 54,000 lume estimate (01-04, 08) | Low | yes | money; broad refuted the prize-change part (no breakdown), carried. Same as b. |
| NoticeTypeCode CN for a design contest (03, 08; context only) | Medium | no | verified: world list describes CN as "eForms cn-standard"; eForms has a separate design-contest notice (cn-desg; can-desg for awards); UBL ContractAwardNotice/NoticeTypeCode definition itself names "Design". Preferred: add design-contest notice types to the list. Context said yes; set to no (list encoding, not story). b: please use the same for CAN in 15/16. |
| CandidateReductionConstraintIndicator true in notice/call (03, 04, 08) | Low | no | context; broad refuted ("describes the procedure"), carried. eForms maps BT-52 (successive reduction) to it: practice, not semantics. Same as b. |
| Documents addressed to one participant before selection (04 call, 05 request) | Low | yes | broad/context (04) and broad (05); parties/logistics refuted (documents available to interested operators; QAR's EconomicOperatorParty is "receiving" by definition). Same as b. |
| ID-only references (04 brief, site plan) | Low | no | DocumentType/TypeCode + attachment or URI. Broad's "rules not referenced" sub-claim dropped (rules are in the call itself, logistics). Context refuted (Note says what they are); carried. |
| Missing reference to the contract notice (04 call), to the notice (05 request), to the request (06 response) | Low | no | logistics (+ broad in 04). NoticeDocumentReference / AdditionalDocumentReference. |
| New version does not say what changed (02, 08) | Low | no | broad; context (02) refuted it as a welcome addition, carried. b folded the 09 case into ID-only references; here own finding (no references involved). |
| FulfilmentIndicator true in a request (05 CR-PROF) | Medium | no | broad + context; verified (definition "has been fulfilled"; only CR-PROF carries it). |
| Reference criteria CR-REF-PUBLIC / CR-REF-COAST unanswered (06) | Medium | no | broad/context/logistics all Medium; verified (one TenderingCriterion, one response). Not High: missing information, no value contradicts another. |
| One completed task vs threshold 2 (07) | Medium | no | broad/logistics Medium, context Low; Medium kept: the threshold is stated, and the document's purpose (declaring the qualifications the selection rests on) depends on it. |
| Coastal criterion property does not ask for the site (05) | Low | no | context. |
| No exclusion grounds in request/response (05, 06) | Low | yes | context. |
| Consortium: group named but only one EO party, no role (06) | Low | no | parties + context merged; broad refuted (lead answers for the group), carried. |
| Design lead "of Saltmere" vs note "engineering firm does the structure" (06 parties Low/yes; 07 broad Low/no; context refuted) | Low | yes | both arguments; same in 06 and 07. |
| Evidence not linked (06) | Low | no | SuppliedEvidence (EvidenceSupplied is deprecated in 2.5; broad/context named the deprecated one). |
| Duplicate response text (06) | Low | no | context; broad refuted (harmless), carried. |
| BusinessIdentityEvidenceID = register number (07) | Low | yes | context/parties Low/no, broad/logistics refuted (register entry is the evidence). Cannot settle -> yes. |
| Saltmere registered name without legal form (07) | Low | no | parties. |
| TendererQualificationRequest LTD vs text (03, 04, 08) | Low | yes | context Low/no; broad refuted (text explains). Cannot settle. |
| DurationPeriod = look-back window (03, 04, 08) | Low | no | context. |
| Registration date 1996-01-01 (Brackenmere 04-07) | Low | yes | Same as all flows. 271 in 181 files. |


### contest-merge-decisions-b

#### contest merge decisions, merger B (contest 09-16), run 20261112T2358Z-thorough

FINAL (merged files 09-16 written; check_xpaths.py and check_values.py pass for all eight). Read contest-merge-decisions-a.md (FINAL) and the earlier flows' decisions files; aligned with a on every shared row (09 F13 and 12 F5 and 09 F9 changed to match a). Counts recounted over *.xml.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (all) | Medium | no | drop LocaleCode; or en-XB from a locale list. 362 in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`). Same as a and earlier flows. |
| Public bodies (PWD, Information Service, Review Board) with COMMERCIAL register type + liquidation status (09-16) | Medium | no | drop liquidation status and register type for public bodies; or a public-body register type; City of Lumeport as legal entity kept as option. broad/parties said yes; aligned no (as a, customs-as-company in all earlier flows). |
| Customs-trader IDs (PWD; Valdara in 15/16) and economic operators' own tax schemes | Low | no | drop where unused. Context refuted the operators' tax registrations in qualification documents (10, 11, 12); merge kept them (no criterion asks for them), counter-argument carried. 13/14: only the receiver's data (money: an extract reports its subject's registrations). Same as a. |
| PartyTaxScheme of the contracting authority itself | 09, 15, 16: Low / yes; 10-12: inside the copied-data finding, Low / no | | 09: money refuted (production limit; amounts net of sales tax), 15/16: money refuted (follow-up contract fees net) -> cannot settle -> own Low/yes. 10-12: money itself found it copied (no amounts) -> no refutation, so folded into the Low/no finding. Same as a in substance. |
| PUBLIC exemption text "Sale to a public body: ..." | Low | no | reword as status; code fits (list definition = buyer status). Same as a. |
| Contacts (Brackenmere Trade sales, Review Board Registry/Procurement officer, Saltmere Bids office/Procurement officer, Valdara Order desk) | Low | no | one finding per example. DIFFERENCE: 13 and 14 (register extracts) refuted in the merge (broad and parties findings moved to "Refuted in the merge"), following context: the business party of an extract carries the contact the register holds. |
| 54,000 estimate (09, 15, 16) | Low | yes | money; broad's refutation (no breakdown) carried. Same as a. |
| Reference criteria unanswered (11) | Medium | no | broad/logistics/context all Medium; verified. Same as a (06). |
| One completed task vs two references (12) | Medium | no | broad/logistics Medium, context Low. Same as a (07). |
| FulfilmentIndicator in request (10) | Medium | no | Same as a (05). |
| Coastal criterion property (10) | Low | no | context. Same as a. |
| No exclusion grounds (10, 11) | Low | yes | context. Same as a. |
| NoticeTypeCode CAN for design contest (15, 16) | Medium | no | context said yes; aligned with a (03/08 CN): add design-contest types (cn-desg/can-desg) to the list. UBL's CAN NoticeTypeCode definition names "Design" (checked in the model). |
| CandidateReductionConstraintIndicator (09) | Low | no | context; broad refuted, carried. ALIGNED with a (was yes in my draft). |
| Call addressed to one participant before selection (09) | Low | yes | broad/context; parties/logistics refuted, carried. Same as a. |
| ID-only references brief/site plan; site plan A->B change unexplained (09) | Low | no | one finding (version change folded in, since it concerns the reference). a has a separate "new version" finding for 02/08 where no reference is involved. |
| Missing reference to contract notice (09 call), to "the contest notice" (10 request), to the request (11 response) | Low | no | logistics (+ broad in 09). Same as a. |
| New version not saying what changed: 14 (capability amount; subtype EXTRACT vs CORRECTION), 16 (first prize 6,000->8,000), 11 (design lead, noted in F5) | Low | no | 14: broad + logistics + context/money parts. 16: broad; money refuted (version chain suffices, explanation belongs to 15) — kept with counter-argument. |
| First prize 6,000 vs 8,000 (15) | High | yes | all four parts High/yes; refutation attempt failed; diff 15/16 shows the prize is the only content change. Preferred if correction is the story: keep 6,000 in 15, state the correction in 16. |
| Capability amount 6,410,000 / 6,830,000 (13, 14) | Low | yes | money (Low/yes: implausible against Brackenmere's 2025 turnover 410,000 in tender/07, verified), broad/context (no measure). Combined; parties refuted the size code, logistics the type code (carried). |
| Only lead's register extract (13, 14) | Low | yes | broad. |
| Consortium: one EO party without role (11) | Low | no | parties + context; broad/logistics refuted, carried. Same as a (06). |
| Winning team reduced to the lead (15, 16) | Medium | no | parties Medium, broad/context Low. Medium because who won is the purpose of an award notice; differs from 11 (Low). Not High (lead may represent group). |
| Design lead not attributed to a member (11) | Low | yes | parties. |
| Evidence not linked (11) | Low | no | SuppliedEvidence (2.5). Same as a. |
| Duplicate response text (11) | Low | no | context; broad refuted, carried. Same as a. |
| BusinessIdentityEvidenceID = register number (12) | Low | yes | ALIGNED with a (was no in my draft). |
| Saltmere registered name without legal form (12) | Low | no | parties. Same as a. |
| TendererQualificationRequest LTD vs text (09) | Low | yes | context Low/no; no part refuted it in 09, but aligned with a: the text can be read as explaining the code (merge's own counter-argument recorded). |
| DurationPeriod = look-back window (09) | Low | no | context. Same as a. |
| Copied master data of the second-prize winner (15, 16: share capital, listing, mobile, logistics provider) | Low | no | own finding, separate from customs/tax numbers. |
| PublishAwardIndicator (15, 16) | Low | yes | context; broad refuted (services, published), carried. |
| Province of Ferrano in Region (15, 16, Valdara) | Medium | no | CountrySubentity. 219 in 104 files. Same as earlier flows. |
| Italian street name tagged en-XB + untagged Italian legal form (15, 16, Valdara) | Low | yes | broad; parties refuted (exonym convention), carried; legal-form line added by the merge (as earlier flows). |
| RegistrationDate 1996-01-01 (Brackenmere 09-16) | Low | yes | 271 in 181 files. 13/14 broad said no; aligned yes. |


### furniture-merge-decisions-a

#### furniture merge decisions, merger A (furniture 01-08), run 20261113T0047Z-thorough

FINAL (merged files 01-08 written; check_xpaths.py and check_values.py pass: all XPaths resolve, 270 values match). Re-read b (draft 1, and b's merged files 09-17) before finalising: aligned on every shared row except RegistrationDate (see last row; explained). Read contest-, road-, utilities-, air-, rail-, wood-, plastics-, energy-, packaging-merge-decisions-*.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (01-08, all) | Medium | no | drop LocaleCode (preferred, as all earlier flows and b); broad's en-XB kept as option b. Count 362 in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, verified). Same as b. |
| Brightmarket contact "Buying office" / Customer service officer / Sales (01-08) | Low | no | one finding per example; buyer/planning contact in purchasing. Brackenmere's own contact refuted by parties (small firm, consistent) - carried. Same as b. |
| Copied store master data: LogoReferenceID, AdditionalWebSite, SocialMediaProfile, CorporateStockAmount (01-08) + both parties' PartyTaxScheme in non-tax documents (03-07, parties) | Low | no | ONE finding per example (context + parties grouped; tax scheme folded in), same as b. Parties refuted the logo in 01/02 (own label) - carried as counter-argument, logo kept as the weakest part. PartyTaxScheme not raised in 01, 02, 08 (tax-relevant documents). |
| Maker's BrandName `Brackenmere` on the own-line item (01-08) | Low | yes | store's own-line brand (preferred) or reword as exclusive maker-branded line. Verified: item BF-GS-01 in 12 files; BrandName Brackenmere in 14 (15, 17 = PWD order/invoice). Same as b. |
| Originator/Beneficiary = buyer (01, 02) | Low | no | drop both; broad refuted (IND6 explicit statement), carried into Why; kept because IND5 and no document uses the roles. Same as b (11). |
| Lines mixing request/exception types: 03 (SALES+TOTAL+SALESUNITS), 05 line 1 (SALES+SALESUNITS), 07 (SALES+SALESUNITS+ForecastException) | Medium | no | keep the operational SALES only. Verified against the definitions (03 ForecastTypeCode: "either … or … or"; 05/07 SupplyChainActivityTypeCode "one of the three types"). 05: logistics had Low, raised. |
| 07 ForecastException content (forecast 2026-03-16 10:00 not in the flow; no forecast criterion matches) | Medium | no | context said yes; set to no (same removal as the type finding). ComparisonDataCode ACTUAL (not a partner) separate Medium/no (broad). |
| 07 ComparisonForecastIssueTime 18:00 vs 06 IssueTime 16:35 | Medium | no | CHANGED from logistics' High: link of the 18:00 to 06 is an inference via the misused line reference; the element is a forecast's issue time used for actual data (Medium). Broad had Low. |
| 07 line DocumentReference BS-DOC-26-0572 (activity report) where the definition names the Exception Criteria | Medium | no | all three parts Medium; verified. |
| 05 sales threshold without time basis | Medium | no | broad Medium; context/logistics Low; Medium because the criterion cannot be evaluated (information the purpose depends on). |
| ExceptionStatusCode ACTIVE/OPEN, definition "shipment exception" (05, 07) | Low | yes | context only; broad refuted in 05 (carried). 05 preferred remove, 07 preferred keep + TC write-up note. Not in 09-17. |
| 05 ThresholdValueComparisonCode LT/GT and ExceptionResolutionCode REVIEW vs values named in the UBL definitions | Low | yes | logistics; broad refuted LT (same meaning). TC write-up candidate. |
| 07 Source/Compared values swapped | Low | yes | broad + logistics; context's opposite reading carried. |
| 04 ReplenishmentOwnerDescription is a process description | Medium | no | broad Medium, context Low/yes; logistics refuted the note/description contradiction (carried). |
| 04 ItemLocationQuantity/MinimumQuantity without price | Medium | no | broad, context Medium; logistics Low. |
| 06 weather in ActivityProperty | Low | yes | CHANGED from context's Medium: definition too open to exclude the other reading. |
| 06 line Buyer/Seller = trading partners; ActivityFinalLocation "Customers' gardens" | Low | yes | 2 vs 2 parts; cannot settle -> yes. |
| Delivery place in text only / no delivery date (08) | Low | no | Delivery/DeliveryLocation with GLN 9522610900019 + requested period; broad+parties+logistics grouped. Same as b (10, 15). |
| Initial order 20 vs target inventory 10 (08) | Low | yes | logistics; broad refuted in 04 (opening stock). Same as b's repeat-order row (Low/yes). |
| "Original" price = price (08) | Low | no | broad, context; money refuted (carried). Same as b (10). |
| Sub-line prices without BaseQuantity (08) | Low | no | money. Same as b. |
| Quotation used as contract; public body as company; parks cost centre; customs trader no.; "Invoice" in PaymentNote | - | - | do not occur in 01-08 (PWD only in 15-17; the cost centre "Garden department" 6120 in 08 is the buyer's own, only the duplication was raised and refuted). |
| RegistrationDate 1996-01-01 (Brackenmere, 01-08) | Low | yes | DIFFERENCE from b: parties refuted it in every example; I disagreed with the refutation and made it a finding (Low/yes) in all 8, because every earlier flow's merge (incl. contest a/b for Brackenmere itself, wood, plastics, rail, air, road, utilities) kept it as Low/yes. Verified: 271 in 181 files, 25 distinct CompanyIDs (lxml). b (09-17) carried it under Considered and refuted; b, please consider aligning, or the person working through the reviews should treat the two halves as one question. |


### furniture-merge-decisions-b

#### furniture merge decisions, merger B (furniture 09-17), run 20261113T0047Z-thorough

FINAL (09-17 merged files written; check_xpaths and check_values pass). Read furniture-merge-decisions-a.md (draft 1) and the earlier flows' files; aligned on every shared row, differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639), every example | Medium | no | drop LocaleCode (preferred), or en-XB from a locale list. Broad preferred en-XB; aligned with a and all earlier flows. 362 in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`). |
| Brightmarket contact "Buying office" / Customer service officer / Sales | Low | no | one finding per example; buyer in purchasing for buying documents, accounts contact in billing documents (09, 13, 14). Same as a. Brackenmere's trade-sales contact refuted (parties), carried. |
| Copied store master data (logo, AdditionalWebSite, SocialMediaProfile, CorporateStockAmount) | Low | no | ONE finding per example (parties + context grouped). PartyTaxScheme of both parties folded in only where the document has no tax content (11, 12), as a (03-07); not raised in 09, 10, 13, 14 (billing/ordering). |
| Maker's BrandName on the own-line item (09, 10, 12, 13) | Low | yes | store's own label (preferred) or exclusive maker-branded line. Same as a. 15: refuted (desks are the maker's own products). |
| Originator/beneficiary repeating the buyer (11) | Low | no | drop both; broad's refutation (IND6) carried in the finding. Same as a (01, 02). |
| Delivery place in text only / no delivery date (10, 15; 09 no delivery date; 16 place of work by name only) | Low | no | DeliveryLocation with GLN / address register ID + requested period. Same as a (08). |
| Return destination missing in the InstructionForReturns (12) | Medium | no | purpose depends on it (logistics, parties Medium; broad, context Low raised). Carrier/cost arrangement split off as Low/yes. |
| Quotation number used as contract (11 Contract/ID, 14 ContractDocumentReference) | Medium | no | 11: BM-OWN-BRAND-2026 preferred (2 of 3 parts); 14: remove / move to AdditionalDocumentReference preferred (charge arises from the return instruction). Logistics' Low in 14 (accepted quotation may be the contract) carried as argument. Not in a's range. |
| Public body (PWD) as commercial company with liquidation status (15, 16, 17) | Medium | no | drop liquidation status and COMMERCIAL type; City of Lumeport kept as option (b). Parties said yes; aligned no with all earlier flows. |
| Parks cost centre PWD-PARKS-26 for the office furniture (15, 16, 17; 17 also the AP routing code) | Low | no | office-project cost centre in 15/16/17. ALL THREE PARTS SAID YES; set to no, aligned with the earlier flows' cost-centre findings (internal accounting code, neither option changes what happens). a: not in range. |
| Store's cost centre 6120 as buyer's code in the debit note (14), where the buyer is the maker | Medium | no | remove. Same kind as utilities b (seller's accounts in buyer's element = Medium). |
| Customs trader number XB-TR-410548 in domestic documents (15, 16, 17) | Low | no | drop. 55 files (36 tender, 16 contest, 3 furniture). Same as earlier flows. |
| PUBLIC exemption text "Sale to a public body: ..." at party level (15, 16, 17) | Low | no | reword text as status; code fits (list description is a buyer status), money's code argument carried with option (c). Same as contest a/b. |
| "Invoice ..." in PaymentNote of the credit note (13) and the debit note (14) | Low | no | "Credit note ..."/"Debit note ...". 09/17 are invoices: correct, listed as checked. |
| RF creditor reference built by the refunding party (13) | Low | no | plain PaymentID without RF, no "Quote". Split from the PaymentNote finding (broad had both). |
| Debit-note accounting roles (14) | High | yes | swap accounting parties, drop PayeeParty (preferred, all parts). Yes because sea/28-DebitNote has the same pattern (looks like a convention; UBL defines none). Money's Medium raised. |
| Prices without BaseQuantity (09 sub-lines + free line; 10 sub-lines + original price; 16 hourly) | Low | no | add BaseQuantity. 12 of 117 Price elements (lxml recount). |
| Unresolved DeliveryNoteDocumentReference BF-DN-26-0320 (09) | High | yes | add a despatch advice (preferred) / describe as paper note / remove. Logistics' Medium raised (section 6: referenced document that does not exist). |
| Order 10 taxable 12200.00 vs 11834.00 after 3 % allowance | High | no | recalculated: 0.03 x 12200 = 366; 12200 - 366 = 11834. |
| Repeat order 10 vs stock (17 to 20 on hand on 2026-04-16, reorder point 4, target 10) | Low | yes | logistics High lowered: profile is a policy, not a statement the order contradicts; both arguments in the finding. |
| Unagreed charges/discounts (10 repeat-order discount; 16/17 packaging disposal 24.00) | Low | yes | who agreed it is story; broad/money split yes/no, aligned yes. |
| Restocking deduction on a maker-requested return (13) | Low | yes | merge prefers removing the deduction (3660.00). |
| RegistrationDate 1996-01-01 (Brackenmere, 09-17) | Low | yes | ALIGNED with a (coordinator's request): moved from Considered and refuted to a Low/yes finding in all 9 (09#F10, 10#F12, 11#F8, 12#F8, 13#F9, 14#F9, 15#F7, 16#F13, 17#F9; appended as last finding, no renumbering), parties' refutation carried as counter-argument. 271 in 181 files. |
| Refuted in the merge | | | only 12 broad/F3 (store's BM- prefix on the return shipment: the store carries the goods). |


### cotton-merge-decisions-a

#### cotton merge decisions, merger A (cotton 01-09), run 20261113T0121Z-thorough

FINAL (merged files 01-09 written; check_xpaths.py and check_values.py pass: all XPaths resolve, 432 values match). Re-read b (FINAL) before finalising: aligned on every shared row. Read the earlier flows' files (furniture, contest, road, utilities, air, rail, wood, plastics, energy, packaging).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| Tax category O ("Services outside scope of tax") for goods (SupplyTypeCode GOODS) (01, 04, 05) | Medium | yes | decide once world-wide how goods outside any sales tax are coded; or keep O as recorded EN 16931 deviation. 17 files use 5305 O; 5 with O + GOODS (cotton 01, 04, 05, 16, sea/29; lxml). O for the haulage charge (a service): refuted. |
| "No general sales tax" scheme without ID | Low | yes | name a Lisavan scheme with ID, or no tax total; decide once for Lisavu. Same as utilities/13#F8. 9 files. Context's IND6 refutation carried (01). |
| Category O with Percent 0 | Low | no | drop Percent. Added by the merge (no part raised it), as utilities, road. |
| LocaleCode en | Medium | no | drop (preferred) or a locale from a locale list; 362 in 213 files. |
| RegistrationDate 1996-01-01 | Low | yes | own dates; 271 in 181 files. |
| Contacts (ginnery "Cotton sales"/CSO/Sales in buying/receiving role; farm CSO/Sales for a micro sole proprietorship; mill "Purchasing"/CSO/Sales) | Low | no | one finding per example, all parties' contacts grouped. Broad refuted the farm's "Sales" in 03 (micro farm) - carried. |
| Copied master data (customs-trader number in domestic/non-customs docs, farm PhysicalLocation outside the delivery note, PartyTaxScheme in forecast/order-type docs) | Low | no | one finding per example. |
| PayeeParty = seller in self-billed invoices (01, 04) | refuted in the merge | - | definition has no "if different" condition; IND6; broad and context refuted. |
| Farm address lines repeating the structured parts (01, 03) | Low | no | drop lines; parties' Lisavan-print-format argument carried. |
| RegistrationExpirationDate on the farm's company-register entry (01, 03) | Low | yes | cannot settle (seasonal farm registration reading, parties). |
| en-XB tags on the ginnery's Lisavan address / item text in Bayvarran-issued docs (02, 07, 08, 09) | Low | yes | one rule, documented; parts said no, aligned yes with earlier flows and b. Untagged single legal form: SEPARATE Low/no (aligned with b and road/rail/air). |
| NoStatus (03 DocumentStatusCode, 04 LineStatusCode) | Low | no | drop; broad's IND6 refutation recorded as not followed. |
| Identity exchange rates / tax and payment currency = document currency (04, 05) | Low | no | drop. Alternative payment currency XBL without reason: own Low/no (money said yes in 04). |
| PricingCurrencyCode XBL with XLC prices + pricing rate (04, 05) | High | no | drop both (preferred, no story change); option b Lume price = story. |
| 04 taxable amount 4068 vs tax-exclusive 4248 (haulage 180 in O omitted) | High | no | recomputed. |
| DespatchDocumentReference = the delivery note (04, 05) | Medium | no | drop. |
| Mill as originator/beneficiary of the farm-ginnery purchase (03, 04, 05) | 03: Low / 04 (and 05 if present): Medium | yes | drop; or story (mill pre-buys crop, LTM-SEASON-2026). 03 Low because its definition ("a customer party as originator") does not tie the role to the order; 04's does ("originated the Order to which this Invoice is related"). |
| Tax representative (customs broker) for a domestic farm (04, 05) | Medium | yes | drop. |
| PackSizeNumeric 227 (02, 07, 08) | Low | yes | ALIGNED with b (per-kg reading); preferred drop + item property. |
| Region "North coast" vs District (02, 07?, 08?) | Low | no | District. Same as b. |
| Classing certificate XL-CLS-2026-0042 (validated 2026-02-20) in the forecast 02 (issued 02-02) | High | no | drop from forecast. 07/08: by date. |
| Classing results in Certificate/Remarks | Low | no | drop the remark. Same as b. |
| Season agreement SCG-SEASON-2026 (ginnery-farm) cited in the mill's forecast (02) | Medium | yes | mill-ginnery agreement or none. |
| Delivery note gross weight 20400 vs 18000 kg (3 loose trailer loads, 800 kg each) (03) | Low | yes | drop / tare / deduction. Context's refutation (trailers included) answered by the calculation. Not the containerised case of b's Medium row. |
| Project reference SCC-COTTON-QUALITY-26 (03, 04, 05) | Low | yes | drop or story. |
| Weighbridge ticket SCG-WB-26-0311: ID only in 03, as ReceiptDocumentReference in 04/05 | Low | no | AdditionalDocumentReference with type. |
| DAP + haulage charge (04, 05) | Low | yes | buyer-pays term or drop charge. |
| AdValoremIndicator + DeclaredCarriageValueAmount (09) | Low | yes | drop indicator; same as b (13). Broad listed it as consistent (shipping reading), not followed. |
| 09 "Send the bill of lading to the forwarder" vs 13 distribution (bank original, mill scan) | High | no | ALIGNED with b (logistics said yes): original to the forwarder in 13; bank question is b's Medium/yes in 13. |
| Shipment gross weight 6190.29 without the container (09) | Medium | no | ALIGNED with b (logistics Low). |
| Forwarding instructions without goods/places/dates (09) | Medium | no | three parts. |
| ShippingOrderID = shipment ID (09) | Medium | no | drop. |
| Unused exchange rate XBL->XLC (09) | Low | no | drop; same as b (13). |
| Signature ID LTM-SIG-FI-09 (example number?) (09) | Low | no | added by the merge, aligned with b/road. Reading uncertain (could be the mill's 9th). |
| 05 PayeeParty = farm on a set-off credit note | Medium | no | drop (not the 01/04 refutation: the farm receives nothing). |
| 05 cites XL-CLS-2026-0042 (Middling, validated 02-20) for an SLM downgrade issued 02-14 | High | yes | rely on SCC-CLS-26-0311. |
| 05 taxable 75 vs tax-exclusive 70 (allowance without category) | High | no | as 04 (money Medium raised). |
| 05 classing-fee allowance direction | Low | yes | broad Medium lowered (ginnery refund reading possible). |
| 07 "twenty per cent more" vs 24000 -> 30000 (25 %) | High | no | recomputed; period coverage split off Low/no. |
| Farm address lines / expiry date in 04, 05, 06 (no part raised them there) | Low | no / yes | appended by the merge for consistency with 01/03 (no renumbering). |


### cotton-merge-decisions-b

#### cotton merge decisions, merger B (cotton 10-18), run 20261113T0121Z-thorough

FINAL (merged files 10-18 written; check_xpaths.py and check_values.py pass for all nine). Re-read cotton-merge-decisions-a.md (draft 2) before finalising: aligned on every shared row (PackSizeNumeric, en-XB tags + separate legal-form row, O/Percent/scheme rows, Region, Remarks, contacts, RegistrationDate, LocaleCode); a accepts the Medium shipment-gross-weight row for the containerised case. Read and furniture-, road-, rail-, utilities-, wood-, plastics-, air-, contest-, energy-, packaging-merge-decisions-*.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) | Medium | no | drop LocaleCode (preferred), or en-XB/en-XL from a locale list. Same as a and all earlier flows. 213 files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`). |
| Contacts not fitting the role (mill "Purchasing" / Customer service officer / Sales, 52 files; ginnery "Cotton sales" as shipper; customs "Import office" in the export declaration; chamber "Carnet office") | Low | no | role-specific contacts, one finding per example (all contacts of the example in one finding where they are the same kind of problem; the chamber's carnet office in 10 own Low). Same as a. |
| RegistrationDate 1996-01-01 | Low | yes | own date per company; same as a and all earlier flows. 271 in 181 files. |
| Region `North coast` (item origin) vs District in the farm's address | Low | no | District. Region can be read as a geographic region, so consistency remark. 13 files carry "North coast". |
| PackQuantity 1 / PackSizeNumeric 227 | Low | yes | CHANGED from logistics/context Medium: the item is traded per KGM (quantities and base quantity in KGM), so "227 one-kilogram units per pack" is a possible reading of "number of items in a pack"; cannot settle. Preferred: drop pack elements, nominal bale weight as item property. a: please align or explain. |
| Bale count not stated (10 certificate, 11 export declaration, 13 B/L, 15 import declaration) | Low | no | package quantity 27 bales. In 13 folded into the Medium "B/L without goods/container/vessel/ports". |
| Classing certificate XL-CLS-2026-0042 in documents that do nothing with the grade | 10: Low/no (inside a "data the certificate does not use" finding); 11, 15: refuted (context: the grade affects the customs value) | - | kept in order/invoice. |
| Classing results in Certificate/Remarks ("Remarks by the applicant for the certificate") | Low | no | drop the remark. |
| Chamber of commerce as a company (commercial register, liquidation status) (10) | Low | yes | as road a/b (chamber's legal nature is story). |
| Customs authority as a company (11 Island Customs Service; 15 Customs and Border Service) | Medium | no | drop company attributes; same as all earlier flows. |
| Phytosanitary certificate issued by the chamber, sanctioned by customs (10) | Medium | yes | plant protection authority as issuer. |
| Copied tax/master data (tax schemes, share capital, customs-trader IDs in non-tax / non-customs documents) | Low | no | drop; one finding per example. |
| Shipment GrossWeightMeasure 6190.29 = goods only (11, 13, 15?) | Medium | no | DIFFERENCE from a's prelim Low/yes: the same shipment SCG-SH-26-0200 is containerised (12: TWLU4123110, VGM 9940.29 = 6190.29 + 3750 tare), so "no equipment, equal may be correct" (utilities) does not hold; the value misfits the definition and 12. Not High because the declaration itself names no equipment (rail b High had the containers in the same document). Preferred: drop shipment gross weight, keep goods-item gross weight. |
| VGM (12): no method/date, not in VerifiedGrossMass | Medium | no | VerifiedGrossMass with method/date. Sum 6190.29+3750 = 9940.29 to the gram vs port as weighing party: Low/no, preferred method 1 (port) with weighed figure. ResponsibleParty = shipper: Medium/no (payer = debtor pattern). |
| B/L distribution (bank original + mill scan) vs 09 "Send the bill of lading to the forwarder." (13) | High | no | original to the forwarder (preferred); the bank's role is the separate Medium/yes mortgage-holder finding. As rail b "Distribution vs note High no". |
| Mortgage holder Bank of Selanu on a straight B/L, open-account sale (13) | Medium | yes | drop (preferred) or add financing to the story. |
| AdValoremIndicator true with DeclaredCarriageValueAmount (13) | Low | yes | leave out (definition is about duties) or add the value-based charge; money's flat-freight argument + context's definition argument in one finding. a: 09 has the same pair. |
| Unused exchange rate XBL->XLC 0.4 (13) | Low | no | drop. Same as a's identity-rate row. |
| en-XB tags on the ginnery's Lisavan address in Bayvarran-issued documents (13, 15, 18) | Low | yes | one rule, documented (tag follows issuer is consistent: 02, 07, 08, 09, 13, 15, 18 en-XB; ginnery-issued en-XL). Parties said no; aligned yes with earlier flows. Untagged single legal form (Lisavan rendering dropped): separate Low/no, as road/rail/air. |
| Signature ID with flow name (11 SCG-SIG-EX-cotton, 13 TWL-SIG-BL-cotton, 15 LTM-SIG-IM-cotton) | Low | no | added by the merge (no part raised it), aligned with road a/b. 8 files over all flows. |
| NoStatus | - | - | does not occur in 10-18 (grep). |
| Tax category O for goods (16) | Medium | yes | as a. |
| "No general sales tax" scheme without ID (16) | Low | yes | as a. 9 files. |
| Category O with Percent 0 (16) | Low | no | added by the merge, as a. |
| Due date 2026-04-01 vs "45 days net" (16: 2026-03-02 + 45 = 2026-04-16) | High | no | due dates 2026-04-16 (XL-STD = 45 days in 04), as utilities b. |
| Payment currency = document currency (16, broad) | refuted in the merge | - | Lume-account buyer needs it; IND6. |
| TotalCreditAmount 0.000 (18, money) | refuted in the merge | - | IND6 (explicit zero); broad and context refuted. |
| Customs value FOB vs CIF (15: 15138.63 = 6055.452/0.4; CIF would be +2950.00 = 18088.63) | Low | yes | decide Bayvarra's valuation basis. |
| Freight collect vs forwarder invoicing the freight (13, 17) | Low | yes | money's refutation (forwarder pays at destination, recharges) carried. |
| Phyto certificate not referenced in export/import declaration (11, 15); bale count missing (10, 11, 15) | Low | no | add references / package count 27. |


### retail-merge-decisions-a

#### retail merge decisions, merger A (retail 01-07), run 20261113T0434Z-thorough

FINAL (merged files 01-07 written; check_xpaths.py and check_values.py pass for all seven: 371 values match). Read the earlier flows' files (cotton, furniture, contest, road, rail, air, utilities, wood, plastics, energy, packaging) and re-read retail-merge-decisions-b.md (FINAL) and -c.md (DRAFT 1): aligned on every shared row.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) | Medium | no | drop LocaleCode (preferred), en-XB from a locale list as option. Context preferred en-XB and 01 logistics said yes: aligned no/drop with all earlier flows. 362 in 213 files. |
| Gate 3 in Lumeway's AdditionalStreetName | Medium | no | drop from postal address. 79 in 76 files. |
| Brightmarket contact "Buying office" / Customer service officer / Sales | Low | no | one finding per example (broad+parties+context grouped). |
| Copied party master data: CorporateStockAmount, logo/web shop/social media, customs trader ID XB-TR-410274, both parties' PartyTaxScheme | Low | no | ONE finding per example (as furniture a/b). Parties' "CorporateStockAmount = share capital vs definition 'number of shares'" (Low/yes) folded in, with the TC write-up note; set to no (encoding; decision is the same everywhere: drop where unused). |
| GTIN issuer Codana with full master data on line 1 (02) | Low | no | reduce to ID + name (as line 2). Codana's nature (SRU with "Public service officer") own Low/yes. |
| Province of Ferrano in Region (02, Codana) | Medium | no | CountrySubentity. |
| RegistrationDate 1996-01-01 (Codana, 02) | Low | yes | own date. |
| Bench emission triple 96 / 0.82 / 1 EA (02, 04, 05, 07) | High | no | drop factor and base. 0.82 x 1 = 0.82; 0.82 x 56.5 kg = 46.3; 96/0.82 = 117.1. |
| CRADLETOGATE in FullnessIndicationCode | Medium | no | drop; TC write-up. |
| LifecycleStageCode MANUFACTURING vs "from the ore at the mine" | Medium | no | context here said Low: raised to Medium to align with rail/road/air. |
| GTINs 9520610000012/029 in Lumeway's company prefix 9520610 | Low | yes | Valdara's own prefix (parties). |
| GTIN-like world item number 771020000027/034 (valid check digit) | Low | yes | added by the merge (no part raised it) in 02, 04, 05, 07, aligned with rail/road/plastics and b/c. |
| MANUFACTURING in 05, 07 | Medium | no | added by the merge (only context raised it, in 02/04, as Low). |
| Romance exonym 'Via dei Codici' tagged en-XB (02, Codana) | Low | yes | added from broad's remark; parties' refutation (world convention) carried; as road/rail/cotton. |
| Full catalogue item data copied into forecast / inventory report (05, 07) | Low | no | own finding, separate from party data. |
| Catalogue references in 03/04 with issue/revision times that are not the catalogue's (IssueTime 09:00 vs 02's 17:28; RevisionDate 2026-05-21 14:00 after 03's and 04's issue; 04 VersionID 1.0 after 03 made 1.1) | High | no | correct from 02 (or reduce to ID/UUID/issue date). Same block in 20 (c: High/no, aligned). |
| 03 RevisionTime 14:00 after IssueTime 13:10 | High | no | broad High, logistics/context Medium: High (two values of the document in the wrong order, as road's despatch-after-issue). 04's identical revision timestamp: Low/no (plausible on its own; the impossible one is 03's). |
| 03 update line ID 1 = bench, update is for the side frame (58 vs 520/64) | High | no | line ID 2. Recomputed 58/520 = 11.15 %, 12.31 % x 520 = 64.01. Dependent price not updated: Low/no. |
| 02 ActionCode NEW vs PreviousVersionID 0.9 / ReplacedRelatedItem; 01 requests update of LD-CAT-SPRING-26 (exists nowhere) | Medium | yes | new catalogue, drop PreviousVersionID and 01's reference. context said High: lowered (internal draft 0.9 reading possible). |
| 06 PromotionalEventLineItem/Amount 74.90 = reduction, definition says promotional price (674.10) | Medium | no | 674.10. Planned impact 17976.00 = 24 x 749.00 (16178.40 at 674.10): Low/no. |
| 06 STOREOPEN MiscellaneousEvent without story | Medium | yes | drop. |
| 05 FrozenDocumentIndicator false (definition: modifiable true/not false) | Low | yes | context Medium lowered (frozen forecast is a possible reading); TC note. |
| 07 'Counted on Sunday evening' vs Thursday issue/period end | Medium | no | note to match the dates. |
| 07 AvailabilityDate = issue date; 03/04 'Unchanged.' | Low | yes | IND6 reading (broad refuted both): settle once. |
| Header parties repeated on lines (02, 03, 04) | Low | no | drop. |
| Locations named after companies (06, 07) | Low | no | place name + identifier. |
| Signature with ID + signatory only (01-07) | Low | yes | as air/utilities and b/c (137 of 147, lxml). Context said no; split from context's grouped master-data findings in 03, 04, 06. |
| NoStatus | - | - | does not occur in 01-07 (grep). |
| Urvanian tariff codes (02, 04) | Low | no | broad finding; context's refutation (no Bayvarran tariff list in the world: all 61 tariff codes use the XU list) carried as counter-argument. As earlier flows' "copied XU national tariff code". |
| "Unchanged." trading terms (03, 04) | Low | yes | CHANGED from draft (no): drop preferred (money, context), but broad's IND6 refutation (explicit statement instead of absence) is a possible reading -> yes. Only 03 and 04 carry it. |


### retail-merge-decisions-b

#### retail merge decisions, merger B (retail 08-14), run 20261113T0434Z-thorough

FINAL (merged files 08-14 written; check_xpaths.py and check_values.py pass for all seven). Read retail-merge-decisions-a.md and -c.md (DRAFT 1 each) and the earlier flows' files (road, rail, air, cotton, furniture, utilities, wood, plastics, packaging, contest, energy); aligned on every shared row.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) (08-14) | Medium | no | drop (preferred), locale from a locale list as option. Context preferred en-XB: aligned drop. Recount: 362 Language/LocaleCode in 213 files (parties' 364 also counted PreferredLanguageLocaleCode + TenderLanguageLocaleCode). |
| Gate 3 in AdditionalStreetName (08-14) | Medium | no | drop from postal address. 11: postal address AND FromLocation in one Medium finding (context had FromLocation Low; raised, element meaning); FromLocation: gate in the location's description/name. 79 in 76 files. |
| Contacts (Brightmarket "Buying office"/CSO/Sales; Lumeway "Customer service"/Sales in despatch/transport roles; Bayforth "Export desk" for a domestic haul) | Low | no | ONE finding per example, all contacts grouped (as a, c, cotton). |
| Copied party master data (logo/web/social, CorporateStockAmount, XB-TR-410274, PartyTaxScheme in non-tax docs 09, 10, 11, 14) | Low | no | ONE finding per example. CorporateStockAmount's definition conflict in Why as TC note; parties' yes set to no (as a, c, furniture). Tax schemes not raised in 08 (order with tax total), 12, 13. |
| Signature with ID + signatory only (08, 09, 10, 13, 14) | Low | yes | own finding (context had grouped it with master data; split). Drop preferred; 13 waybill: complete it and add the consignor's (as air). 13 ID doubled prefix BF-SIG-BF-WB-26-0231 noted inside. |
| Full catalogue item data (08, 12) | Low | no | own finding, separate from party data. |
| Bench emission triple 96 / 0.82 / 1 EA (08, 12) | High | no | drop factor and base. 0.82 x 1 = 0.82; 96/0.82 = 117.1; 0.82 x 56.5 = 46.3. 39 files. |
| CRADLETOGATE (08, 12) | Medium | no | drop; TC write-up. 08: split from the LocaleCode finding context combined it with. |
| LifecycleStageCode MANUFACTURING (A3) vs "From the ore at the mine ..." (08, 12) | Medium | no | added by the merge (no part raised it), as a, c. |
| GTIN 9520610000012 in Lumeway's prefix 9520610 (08, 12) | Low | yes | Valdara's own prefix. |
| World item number 771020000027 (valid check digit 7) (08, 12) | Low | yes | added by the merge, as a, c. |
| RegistrationDate 1996-01-01 (Bayforth 11, 12, 13, 14) | Low | yes | own date. |
| NoStatus (11 DocumentStatusCode; 12 DocumentStatusCode + LineStatusCode) | Low | no | drop; broad's refutation recorded as not followed. |
| Duplicate line IDs (08 substitute ID 1; 12 HandlingUnitDespatchLine 1 vs DespatchLine 1) | Low | no | 12: logistics High lowered (6 x 4 = 24 holds; ambiguity, not contradiction), as c for 17. |
| ShippingOrderID = consignment ID LD-CS-26-0228 (13, 14) | Medium | no | LD-TR-26-0227 (preferred) or drop. No example states another shipping-order ID. |
| Carrier references differing (13 BF-CMR-26-0217, 14 BF-WB-26-0231, 15 BF-ROAD-26-0231) | High | no | BF-CMR-26-0217 everywhere (as c). |
| Three originals (note) vs distribution (consignee original, consignor electronic copy) (13) | High | no | list the consignor's original. Logistics Low / context Medium raised, as rail b and cotton. |
| CMR for domestic carriage (13) | Low | yes | world list has no national road note type, so preferred: record in the story that Bayvarra applies the CMR domestically; option new list entry. |
| Waybill without goods/packages/places (13); transport request without goods (11); despatch advice without despatch date/delivery place (12) | Medium | no | purpose depends on it. |
| BF-TEP-26-0227 does not exist (14) | High | yes | add Bayforth's TEP, or drop the reference. |
| 10's "Accepted" for Lumeway's own transport request LD-TR-26-0227 | Low | no | drop the additional response (four parts combined). |
| 09/10 status request (11:52) after the status (11:14) | High | no | request before 11:14 or status after 11:52. |
| 08 taxable amount 12480.00 vs 11856.00 after the 624.00 allowance | High | no | 11856.00, as 18-Invoice. Recomputed. |
| 12 pallet listed as ActualPackage of itself (all six units; broad wrongly said only unit 1) | Medium | no | logistics High lowered (count 4 vs 1 listed is not a contradiction; misuse of element). Cartons per 17/19. |
| 12 issued 15:34 after the expected arrival 14:00 (15); receipt 30 Apr (17) | Medium | yes | as c (15, 17); broad's Outside note as counter-argument. |
| Locations named after companies (11 From/ToLocation; 13 IssueLocation; 14 RequestedStatusLocation unidentified) | Low | no | place names + GLNs. |
| 08 DataSendingCapability for the e-document network | Medium | no | drop (three parts). |
| 08 green substitute not in the catalogue | Low | yes | broad finding, context refuted: both arguments, cannot settle. |


### retail-merge-decisions-c

#### retail merge decisions, merger C (retail 15-22), run 20261113T0434Z-thorough

FINAL (merged files 15-22 written; check_xpaths.py and check_values.py pass for all eight: all XPaths resolve, 312 values match). Re-read retail-merge-decisions-a (DRAFT 1) and -b (FINAL) before finalising: aligned on every shared row. Read the earlier flows' files (cotton, furniture, contest, road a/b/c, rail, air, utilities, wood, plastics, energy, packaging). LocaleCode count corrected to 362 Language/LocaleCode in 213 files (as b; parties' 364 includes PreferredLanguageLocaleCode/TenderLanguageLocaleCode).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) (15-22) | Medium | no | drop (preferred), en-XB from a locale list as option. Context preferred en-XB: aligned drop with a/b and all earlier flows. |
| Gate 3 in Lumeway's AdditionalStreetName (15-20) | Medium | no | drop from postal address. Same as a/b. |
| Contacts (Brightmarket "Buying office"/CSO/Sales; Lumeway "Customer service"/Sales; Bayforth "Export desk" for a domestic haul; Harbourline "Client accounts" facing the debtor) | Low | no | ONE finding per example, all contacts grouped (as a/b, cotton). |
| Copied party master data (customs trader ID XB-TR-410274, CorporateStockAmount, logo/web shop/social media; PartyTaxScheme in 20, no tax content) | Low | no | ONE finding per example, as a/b. CorporateStockAmount's "number of shares" vs Amount: in Why as TC write-up note, not yes. Issuer's own share capital on its invoice (18 Lumeway) / its own till receipt and consumer order (21, 22 Brightmarket): refuted (business-letter mention), customer's share capital on 16/18/19 kept. Logo on invoice/credit note: parties' refutation carried. Logo/web/social on 21/22 (consumer documents): parties' refutation accepted (as packaging). |
| Full catalogue item data (emission, circularity, load test, XU tariff code) in receipt advice / invoice / credit note / till receipt | Low | no | own finding, separate from party data (as a/b). 21: context's refutation (consumer may get footprint/repairability) carried, option b. |
| Bench emission triple 96 / 0.82 / 1 EA (17, 18, 19, 21) | High | no | drop factor and base; 0.82 x 1 = 0.82 != 96; 96/0.82 = 117.1. |
| CRADLETOGATE in FullnessIndicationCode (17, 18, 19, 21) | Medium | no | drop; TC write-up. Split from the LocaleCode finding the context part combined it with. |
| LifecycleStageCode MANUFACTURING vs "From the ore at the mine to ... factory gate" (17, 18, 19, 21) | Medium | no | added by the merge (no part raised it in 15-22), aligned with a/b/road/rail. |
| GTIN 9520610000012 in Lumeway's prefix 9520610 (17, 18, 19; 21 added by the merge) | Low | yes | Valdara's own prefix. Same as a/b. |
| World item number 771020000027 (valid GS1 check digit 7) (17, 18, 19, 21) | Low | yes | added by the merge, as a. |
| RegistrationDate 1996-01-01 (Bayforth 15/16, Harbourline 18/19) | Low | yes | own date. Same as all flows. |
| Carrier references differing (15 BF-ROAD-26-0231, 13 BF-CMR-26-0217, 14 BF-WB-26-0231) | High | no | waybill's BF-CMR-26-0217 everywhere; all four parts. b: please align (13/14). |
| Delivery day: 15 "on its way" 29 Apr 11:49, expected 14:00; 17 received 30 Apr 10:40; 12 despatch advice 29 Apr 15:34 | Medium | yes | logistics; broad/context put it under Outside (timeline). Kept as finding in 15 and 17: same consignment, actual "on its way" statement for a 38 km trip. |
| Freight invoice 16 issued 30 Apr 10:31, before the receipt 10:40 | Low | yes | depends on the delivery day. |
| Signature with ID + signatory only (17, 20, 21) | Low | yes | as a/b, air, utilities. |
| NoStatus (17) | Low | no | drop. Same as b. |
| Duplicate receipt line ID 1 (17: handling-unit receipt line 1 = 3 benches vs receipt line 1 = 23) | Low | no | logistics said High; lowered (the pallet line can be read as line 1's part on pallet 3; ambiguity, not contradiction), aligned with b's Low for 08's substitute line. |
| Consumer bank account on card payments (21, 22) | Low | no | drop. Same as utilities (Robin's account). |
| Full card number and CV2 in the consumer order (22) | Low | yes | mask PAN, drop CV2ID. money said Medium (lowered: practice, not element meaning). yes because CV2ID would become uncovered (only occurrence; coverage list in CLAUDE.md). |
| Locations named after companies (21 PointOfSaleLocation) | Low | no | parties' refutation (store name) carried. |
| Invoice 18 bills 24, refers to receipt 17 (23 accepted, 1 rejected, credit requested) | Low | yes | broad/context High lowered: RejectActionCode CREDIT requests a credit note, so invoice-on-despatch + credit (19) is a legitimate reading; cannot settle -> Low/yes. |
| Lead time 5 in invoice 18 PricingReference vs catalogue 3 | High | no | drop PricingReference. money/context Medium (element carries no pricing) folded in. |
| Factor as PayeeParty of the credit note 19 | Medium | yes | drop payee; say the credit reduces the payment to Harbourline. Cotton had Medium/no for a plain set-off; yes here because the factoring settlement is story. |
| Saturday vs 2026-05-17 (Sunday) in 21 | High | no | 2026-05-16. |
| Promotion price validity 12-18 May vs promotion 11-24 May (21 vs 06) | High | no | broad only; verified. |
| Catalogue deletion reference (20): IssueTime 09:00 vs 17:28, revision 2026-05-21 14:00 vs 04, PreviousVersionID 0.9 for 1.2 | High | no | correct or reduce. a: same reference block in 03/04 (please align). |
| Catalogue deletion ValidityPeriod end 19 Jun vs effective 20 Jun 00:00 (20) | Low | no | broad High lowered: 20 Jun 00:00 is the end of 19 Jun, so the two can describe the same instant; redundant, ambiguous. |

Counts in 15-22: Refuted in the merge: 4 (15 context/F3 CURRENT vs DELIVERY; 18 parties/F5 and 19 parties/F6 for the issuer's own share capital; 21 parties/F2). Considered and refuted carried: 15: 2, 16: 4, 17: 4, 18: 5, 19: 5, 20: 2, 21: 8, 22: 5. Merge-added findings: MANUFACTURING (17, 18, 19, 21), world item number (17, 18, 19, 21), GTIN prefix (21).


### sea-merge-decisions-a

#### sea merge decisions, merger A (sea 01-08), run 20261113T0552Z-thorough

FINAL (merged files 01-08 written; check_xpaths.py and check_values.py pass for all eight: all XPaths resolve, 398 values match). Re-read sea-merge-decisions-b (DRAFT 1), -c (FINAL), -d (FINAL) and the earlier flows' files before finalising; aligned on every shared row, differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) (01-08) | Medium | no | drop (preferred), en-XB as option. Broad/context preferred en-XB: aligned. 362 in 213 files. |
| Gate 3 in Lumeway's AdditionalStreetName (01-08) | Medium | no | drop from postal address. Context said Low everywhere: raised. |
| Contacts (Velumi "Purchasing" = CSO/Sales; Nalevi "Goods inwards" = CSO/Sales in 05; Lumeway sales customer service as transport user in 07/08; Codana "Member services" = public service officer in 02) | Low | no | one finding per example (02: Codana's contact separate, preferred drop with its master data, so retail a's "Codana's nature yes" is not needed). |
| Copied party master data (receiver's legal data 01/02/04; Codana full master data 02; both parties' tax/legal data + customs-trader ID in 07/08) | Low | no | one finding per example. CorporateStockAmount "number of shares": refuted / TC note. |
| Copied catalogue data in the order (05: keywords, warranty, test method, emission, circularity, XU tariff code) | Low | no | own finding. 06 items carry none. |
| Bench emission triple 96 / 0.82 / 1 EA (02, 05) | High | no | drop factor and base. |
| CRADLETOGATE (02, 05) | Medium | no | drop. |
| MANUFACTURING vs "From the ore ..." (02, 05) | Medium | no | 02: broad's refutation not followed; 05: added by the merge. |
| Side frame HS 732599 vs 9401.99 (02, 05) | Medium | no | HS 940199. Context (02) listed 732599 as fitting: not followed. Same as b. |
| GTIN in Lumeway's prefix 9520610 / world item numbers 771020000027/034 (02, 05) | Low | yes | added by the merge, as retail, b, d. |
| en-XB tags + English-only legal form for Velumi (01-04, 06); 05 = the en-XL side, finding kept as the inconsistency | Low | yes | one documented rule, preferred en-XL. Broad said no: set yes. |
| Via dei Codici tagged en-XB (02) | Low | yes | parties' refutation not followed, as retail a. |
| RegistrationDate 1996-01-01 (01-06; none in 07/08) | Low | yes | parties raised it everywhere it occurs. |
| Signature with ID + signatory only | Low | yes | 01 (context refuted: not followed), 07 (context refuted a different point: not followed), 08 (added by the merge, as b/c), 04 noted inside the prefix finding. |
| Public body as company: Trade Accord Council (03, 04) | Medium | YES | DIFFERENCE from c/earlier flows (no): legal entity (COMMERCIAL, liquidation), ISIC 9411 (association) and public-service contact contradict each other, so the council's legal nature is undecided; contact grouped in. |
| Tendering-only Evidence elements (01: CandidateStatement, Evidence/Language) | Medium | no | drop. |
| CatalogueIndicator in a catalogue (02) | Medium | no | drop. |
| References with ID only (01 LD-REG-XB; 03 certification refs; 06 originator doc) | Low | no | type/description. |
| Sales territory XB vs export exemption (02) | High | no | territory XL. Logistics Low/yes raised. |
| Full-container discount over 4-192 (02 Medium; 05 Low/yes, money's refutation carried) | Medium / Low | no / yes | separate ILQ for full-container orders. 96 benches 41.5 m3 vs 67.7 m3: not full. |
| Dependent price 12.31 % (02) | Low | no | 520 x 12.31 % = 64.012 -> 64.01 != 64.00; money's rounding refutation not followed. |
| PriceList StatusCode ACTIVE (02) | Medium | no | code from another list (money Low raised with context). |
| CIF price vs freight on top: 05 anticipated 50688; 06 confirmed 50688 vs invoice 22 53778 (deposit 19.73 % vs 18.59 %) | 06 High / 05 Low | yes | preferred: 520 as CIF price, drop invoice charges (aligned with c); recharge in the order response as option (money's preference). |
| 24 vs 4 benches per pallet (05) | High | no | Package/Quantity 4. |
| Order response weights 3762/4106.4 against their definitions (06) | Medium | no | drop (preferred). |
| Volume 41.5 m3 vs 96 x 0.87 m3 = 83.6 m3 (06) | Low | yes | flat-packed statement or other volume. |
| "Invoice LD-SO-26-0123" in PaymentNote (06) | Low | no | broad/context Medium lowered, aligned with furniture b / d "Invoice ..." notes. |
| NoStatus (06 lines) | Low | no | broad's refutation not followed, as all flows. |
| TotalPackagesQuantity 108 (06, context Low) | refuted in the merge | - | B/L counts 108 packages. |
| Signature verified 09:05 vs issue 12:59 / terms 12:00 (03) | High | no | context Low raised. |
| Booking deadline 2026-05-09 10:00 vs issue 12:03 and booking 05-10 (08) | High | no | deadline e.g. 2026-05-12. |
| Friday WeekDayCode vs Thursday 2026-05-14 (08) | High | no | WeekDayCode 4; context's cut-off reading carried; 15-Manifest's 15 May noted Outside. |
| Lumeport-Selanu distance (08: two days vs 3.2 nm from 13/17 coordinates, 120 nm in 16) | High | yes | DIFFERENCE from c ("cross-document voyage time Outside"): kept as a finding (logistics) because 08 states the duration as a fact of the same two ports whose positions 13/17 state; not a timeline question. Map scale decides. |
| TransportServiceCode OCEANCONT = kind, not extent (07, 08) | Medium | no | port-to-port. |
| MMSI MID 298 | - | - | does not occur in 01-08. |
| Exchange rates, ShippingOrderID, public customs bodies | - | - | do not occur in 01-08. |


### sea-merge-decisions-b

#### sea merge decisions, merger B (sea 09-15), run 20261113T0552Z-thorough

FINAL (merged files 09-15 written; check_xpaths.py and check_values.py pass for all seven: all XPaths resolve, 470 values match). Re-read sea-merge-decisions-a (DRAFT 1), -c (FINAL), -d (FINAL) and the earlier flows' files before finalising. Aligned on every shared row; differences explained.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639), all 09-15 | Medium | no | drop (preferred), locale as option (broad/context preferred locale). 362 in 213 files. |
| Gate 3 in Lumeway's AdditionalStreetName (09-12, 14, 15) | Medium | no | drop from postal address. Context's Low raised. 79 in 76 files. |
| Contacts (Lumeway CSO/Sales as consignor/exporter; Velumi "Purchasing"/CSO/Sales; Nalevi goods inwards as CSO; insurer "Cargo claims"/relationship manager; carrier "Bookings" towards customs) | Low | no | ONE finding per example. |
| Copied party master data (CorporateStockAmount, PartyTaxScheme; customs-trader IDs only where no customs use: 10) | Low | no | ONE finding per example; added by the merge where no part raised it (09, 10, 11, 14, 15; 12 and 13 from context). Customs-trader IDs kept out in FI/export decl./B/L/manifest (customs use). |
| Copied product data in packing list / export declaration (+ customs values in packing list, 10) | Low | no | own finding. Context's refutation of the customs value carried as option. |
| Bench emission triple 96 / 0.82 / 1 EA (10, 11) | High | no | drop factor and base. |
| CRADLETOGATE (10, 11) | Medium | no | drop; TC write-up. |
| MANUFACTURING vs "From the ore ..." (10, 11) | Medium | no | added by the merge. |
| GTIN in Lumeway's prefix / world item number with valid GS1 check digit (10, 11) | Low | yes | added by the merge, as c, d, retail. |
| Side frame HS 732599 / XV / CPC 42999 vs 9401.99 (10, 11) | Medium | no | broad only; verified (Section XV Note 1 excludes Chapter 94 articles; own knowledge HS 2022). 22 files carry 732599. a: "to verify in 02". |
| Shipment GrossWeightMeasure 4106.4 without the container (09, 11, 12: Medium; 10, 14, 15: High) | as stated | no | High where the same document states the container's gross weight 7856.4 (= 4106.4 + 3750, recomputed); same as c. |
| ShippingOrderID (09 = shipment ID: Medium, precedes the booking; 12 = shipment ID while 14 names 12's own ID: High; 13 = consignment ID: High; 14 BF-FI-26-0137 correct) | as stated | no | BF-FI-26-0137 / drop. Same as a, c. 13 DocumentReference = consignment ID: separate High (document does not exist). |
| 14 assigned IDs (ConsignorAssigned = PO, ForwarderAssigned = LD-FI) | Medium | no | context's High (grouped with shipping order) lowered: the shipping order in 14 is right. |
| SSCC 095206101230000254 for pallet 25 (PX, 12 packages) and a box (BX, 12 items) (14) | High | no | drop the container-level Package. |
| B/L DeclaredCustomsValueAmount 53778 (CIF) vs 11 50688 and 19 20275.200 XLC (= 50688 x 0.4) (14) | High | yes | DIFFERENCE from c (Medium/yes in 19): High here because 14 contradicts 19 whichever basis is chosen; preferred aligned with c (CIF basis, fix 19: 21511.200 XLC). Money/context refutations not followed. |
| B/L TotalInvoiceAmount 50688 vs invoice 53778 and own DeliveryTerms (14) | High | no | money High kept, broad Low raised. |
| B/L FinalDeliveryParty Velumi vs Nalevi (on-carriage, 05 delivery party, 10) (14) | High | no | parties High kept. |
| BillOfLadingHolderParty Velumi vs originals to Bayforth (14) | Low | yes | cannot settle (holder at issue vs intended). |
| Insurance: 09 InsuranceParty = insurer vs 14 PolicyHolder Lumeway | High | no | Lumeway. 14 two partial InsurancePolicy aggregates + certificate as policy doc: Low/no. Deductible = excess: Low/no. |
| CIF: 09 FinalDeliveryTransportationService (on-carriage) under CIF | Low | yes | broad + context. |
| 14 pre-carriage freight 310.00 billed by nobody | Low | yes | money. |
| Public bodies as companies (11 Customs and Border Service; 15 Island Customs Service) | Medium | no | as all flows. |
| en-XB tags on Lisavu addresses in Bayvarran-issued docs | Low | yes | preferred en-XL. Untagged single English legal form: separate Low/no. |
| RegistrationDate 1996-01-01 | Low | yes | parties raised it in every one of 09-15, so a finding everywhere (consistent with a/c/d "where a part raised it"). |
| Unused exchange rate XBL->XLC 0.4 (09, 12, 14) | Low | no | drop. |
| References with ID only (09-12 VT-PO-26-0127; 14 BF-FI/LD-PL + broker TCB-26-0331 found nowhere else; 15 B/L) | Low | no | type code. |
| NoStatus (09, 12) | Low | no | added by the merge. |
| Signature with ID + signatory only (09-15; IDs with example number 09/12/13, flow name "sea" 11/14) | Low | yes | added by the merge, as c, retail, air. |
| DocumentDistribution to the addressee (09, 12, 15, broad) | refuted in the merge | - | no receiver element; definition does not exclude the addressee. |
| Departure: 13 actual 14 May 18:10 at issue 16:05 (High/no) vs 15 estimated 15 May 06:00 at issue 16:08 (High/yes: which time is the story; 08 gives 14 May 18:00 and Friday frequency) | High | 13 no / 15 yes | |
| 13 port facility security officer as ship's SSO (16 names Marrin) | High | no | parties High kept. |
| 15 crew 2 of 14 + passenger in a cargo manifest | Low | yes | context Medium lowered. |
| Lumeport-Selanu coordinates 3.2 nm (13, logistics High) | refuted in the merge -> Outside | - | 13 states no distance/duration itself; finding in 16 (as a, c). |
| 10 net volume 38.9 m3 vs 96 assembled benches 83.6 m3 (> 67.6 m3 inside a 40'); 4 stacked benches 3.12 m > 2.39 m | Low | yes | knocked down/nested not stated. Logistics' floor/height refutation (two tiers of 1.17 m) carried, rests on the stated volume. |
| MMSI MID 298 | refuted | - | PROVENANCE-second-round.md: ITU MID table (re-read 2026-11-11) lists none of 280-299. No 09-15 part claimed a real allocation (14/15 parts already said unallocated); recorded in 14 and 15 "Checked and consistent". |


### sea-merge-decisions-c

#### sea merge decisions, merger C (sea 16-22), run 20261113T0552Z-thorough

FINAL (merged files 16-22 written; check_xpaths.py and check_values.py pass for all seven). Read sea-merge-decisions-a (draft 1), -b (draft 1), -d (draft 1) and the earlier flows' files. Aligned on every shared row; differences explained below.

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) (16-22) | Medium | no | drop (preferred), en-XB from a locale list as option. 362 in 213 files. Same as a/b/d. |
| Gate 3 in Lumeway's AdditionalStreetName (18-22) | Medium | no | drop from postal address. Same as a/b/d. |
| Contacts (Tidewell "Bookings", Maritime Administration "Ship registry" with office hours for a 06:00 arrival, Velumi "Purchasing"/CSO/Sales, Nalevi "Goods inwards"/CSO/Sales, Bayforth "Export desk", Harbourline "Client accounts") | Low | no | ONE finding per example, all contacts grouped. |
| Copied party master data (tax schemes in non-tax docs, CorporateStockAmount, carrier master data in 18, factor's tax scheme in 22) | Low | no | ONE finding per example. Issuer's own share capital on its invoice (22 Lumeway): refuted (carried). Customer's share capital in 18: kept (as retail c). |
| Copied catalogue item data (19, 20, 21, 22) | Low | no | own finding, separate from party data. |
| Bench emission triple 96 / 0.82 / 1 EA (19, 20, 21, 22) | High | no | ADDED by the merge (no part raised it); drop factor and base. |
| CRADLETOGATE in FullnessIndicationCode (19-22) | Medium | no | ADDED by the merge; drop; TC write-up. |
| LifecycleStageCode MANUFACTURING vs "From the ore ..." (19-22) | Medium | no | ADDED by the merge. |
| GTIN in Lumeway's prefix 9520610 (19-22) / world item number 7710200000xx valid GS1 check digit (19-22) | Low | yes | ADDED by the merge, as b/d/retail. |
| Signature with ID + signatory only (16, 17, 19, 20, 21; IDs with example number 17 / flow name "sea" / document type) | Low | yes | ADDED by the merge, appended as last finding (as b, retail, air, utilities). Not in 18, 22 (no Signature). |
| Shipment gross weight 4106.4 without the 3750 kg container (19, 20) | Medium | no | 4106.4 + 3750 = 7856.4 (B/L/packing list container gross weight). Neither 19 nor 20 states the container in the same document, so Medium (b: High only in 10/14 where it does). |
| ShippingOrderID = consignment ID LD-CS-26-0133 (17) vs B/L BF-FI-26-0137 | High | no | BF-FI-26-0137 (preferred, as b), drop as option. Context Medium raised. |
| en-XB vs en-XL tags for Lisavu addresses (16, 20, 22) | Low | yes | one rule, preferred en-XL. Parties said no: set yes (as a/b/d). DIFFERENCE from b: the English-only, untagged legal form is folded into the same finding (parties raised them together and the condition is one: "described the same way in every example"), not a separate Low/no row. |
| Public bodies as companies (16 Maritime Administration of Lisavu; 19 Island Customs Service) | Medium | no | drop company attributes. Broad Low raised. |
| RegistrationDate 1996-01-01 | - | - | NOT added: no part raised or considered it in 16-22 (as d; b adds it, a where raised/considered). |
| Lumeport-Selanu distance: coordinates 3.2 nm apart vs 40/120 nm positions in the same document (16) | High | yes | finding in 16 only (contradiction inside one document); cross-document voyage time in Outside. As a/b. |
| Position / speed / requested arrival (16): 40 nm / 13.5 kn = 3.0 h vs 38.4 h to 05-18 06:00, no anchoring; ISPS/health at 120 nm | High | no | one position fitting the arrival; recalculated. |
| Ballast exchange "more than 200 nm from land" at 120 nm from Selanu (16) | High | no | NoControlActionsReason misuse split off as Medium. |
| MMSI MID 298 | refuted | - | PROVENANCE-second-round.md line 206: ITU MID table (2026-11-11) lists none of 280-299. No part in 16-22 made the claim; recorded under Checked in 16. |
| NoStatus (16, 20 doc + lines, 21) | Low | no | drop. Context said yes: aligned no. |
| References with ID only (16 manifest, 18 B/L, 19 B/L (in transport finding), 21 B/L (in linking finding)) | Low | no | DocumentTypeCode. |
| Customs value FOB (20275.200 XLC = 50688 x 0.4) vs B/L CIF customs value 53778 (19) | Medium | yes | CIF basis (21511.200 XLC) preferred; Lisavu's valuation law is story. Not High: the valuation basis is undecided, not a hard contradiction inside 19. |
| Urvanian tariff code in a Lisavu import declaration (19) | Medium | yes | Lisavan/Accord tariff list. Differs from earlier "copied XU tariff code Low/no": here it is the classification the declaration rests on. |
| CIF price 50688 (order/order response) vs invoice 22 adding freight 2950 + insurance 140 = 53778 | High | yes | money; drop charges (preferred) or agree recharge in order response. |
| Due date 2026-06-28 vs "30 days net" from shipment 2026-05-14 (= 06-13; 06-28 = +45) (22) | High | no | preferred "45 days net" (keeps statement/remittance timing); 06-13 as option (would need a decision). Money said yes. |
| Exchange rate dated 2026-05-18 after issue 2026-05-14, same rate dated 05-14 in PaymentAlternativeExchangeRate; terms validity from 05-18 (22) | High | no | drop or date 05-14. Same as d's "references dated after issue" row. |
| Pre-carriage 310.00 by Bayforth on the B/L not invoiced (18) | Medium | yes | broad only; grep: 310.00 only in 14. |
| RTNS + NURG (22) | Low | yes | broad finding, context/money refuted; cannot settle (ISO 20022 internal code names are an open source). |
| Tax category O for goods | - | - | does not occur in 16-22 (18 E/SVCB2B, 22 G/EXP). |
| Exchange rates within one currency | - | - | do not occur in 16-22. |

Counts in 16-22: Refuted in the merge: 0. Merge-added findings: 16: 1, 17: 1, 19: 6, 20: 6, 21: 6, 22: 5.


### sea-merge-decisions-d

#### sea merge decisions, merger D (sea 23-29), run 20261113T0552Z-thorough

FINAL (merged files 23-29 written; check_xpaths.py and check_values.py pass for all seven: all XPaths resolve, 299 values match). Re-read sea-merge-decisions-c.md (still DRAFT 1) before finalising: aligned on every shared row (LocaleCode, Gate 3, contacts, copied master data, emission triple, CRADLETOGATE, MANUFACTURING, en-XB/en-XL Low/yes, references after issue High, identity rates Low, RegistrationDate only where raised). Rows a/c do not have: GTIN prefix and world item number (Low/yes, added in 26 and 29, as retail). Read sea-merge-decisions-a.md and -c.md (DRAFT 1 each) and the earlier flows' files (furniture a/b, retail a/b/c, cotton, road, rail, air, utilities, wood, plastics, contest, energy, packaging).

| Problem | Severity | Needs decision | Preferred option / note |
|---|---|---|---|
| LocaleCode `en` (ISO 639) (23-28; not in 29) | Medium | no | drop (preferred), en-XB from a locale list as option. Same as a, c and all flows. 362 in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`). Only parties raised it; broad/money/context silent. |
| Gate 3 in Lumeway's AdditionalStreetName (23-28) | Medium | no | drop from postal address. 79 in 76 files. |
| Contacts (Velumi "Purchasing" = Customer service officer / Sales; Lumeway customer service in billing docs; Harbourline "Client accounts" facing the debtor; farm office in Sales) | Low | no | ONE finding per example, all contacts grouped. |
| Copied party master data (tax schemes, CorporateStockAmount, customs-trader IDs, legal-entity data) in status request/response, statement, remittance, debit note, receipt | Low | no | ONE finding per example (context + money + parties grouped). Not in 26 (Lumeway's own credit note: parties checked its tax scheme/share capital as the issuer's; customer's customs ID refuted by parties, carried). |
| en-XB tags on Velumi's Lisavu address + English-only legal form in Lumeway-issued 23, 25, 26 | Low | yes | one rule, documented; preferred en-XL. Parties said no: set to yes, aligned with a, c, air, wood, plastics, cotton. |
| Exchange rate whose definition condition is not met (24 Payment XBL->XLC; 25 StatementLine; 27 RemittanceAdviceLine) | Medium | no | drop. Definitions name the condition ("if the payment currency differs ..."; "between the currency of the Statement/Remittance Advice and the currency of the document"); 24 money said Low: raised (element meaning). Differs from cotton/c "unused rate Low" because here the element's own condition is not met, not merely unused. |
| 26 PaymentAlternativeCurrencyCode + rate without amount | Low | no | money finding; broad and context refuted (XLC equivalent for the Lisavan buyer) - carried as counter-argument. As cotton's unused rate. |
| 28 identity rates XLC->XLC (tax, pricing, payment alternative) + Tax/PricingCurrencyCode = document currency + TaxPointDate without tax | Low | no | CHANGED from broad/context Medium: aligned with cotton a/b "identity exchange rates: Low/no drop". |
| 28 PayableAlternativeAmount 128.13 XBL vs PaymentAlternativeCurrencyCode XLC | High | no | money High (two values in one document contradict); split off from broad/context's grouped Medium. |
| References/payments dated after issue: 24 PaidDate 06-25 + remittance VT-RM-26-0150 (issued 06-25) in a response of 05-30; 28 StatementDocumentReference HF-ST-26-0151 (issued 06-13) in a debit note of 05-22 | High | no | drop the Payment (24) / the statement reference (28). Same as c. 24 money said yes: aligned no (drop is encoding; the note already says "will be paid"). |
| 24 vs 27 payment: 43778.00 / VT-PAY-26-0199 vs 43714.00 / VT-PAY-26-0123 | High | no | finding in both 24 and 27 (contradiction with another example); fix in 24 preferred. Recomputed 43778.00 - 64.00 = 43714.00. |
| 27 line AccountingSupplierParty = Harbourline (factor) vs header/invoice Lumeway | High | no | Lumeway on the line or drop. All four parts. |
| Factor vs seller in settlement texts (26 "Settled against the next payment to the seller") | Low | yes | name the factor / say deducted from the payment of LD-INV-26-0147 to Harbourline. Broad/context/money said no, parties yes: set to yes, aligned with retail c (factoring settlement is story). |
| Debit-note role reversal (28: AccountingSupplier Lumeway / AccountingCustomer + Payee + Seller Velumi) | High | yes | swap accounting parties, drop PayeeParty (preferred), as furniture b (14). Money said yes, others no: aligned yes with furniture b (same pattern in furniture/14: UBL defines no convention, settle once). |
| 28 storage charge three times / line arithmetic | High | no | recomputed: 38.5 x 1 = 38.500; + charge 12.750 = 51.250 != line 38.500; ItemPriceExtension 51.250 != 38.5 x 1; sub-lines 38.500 + 12.750 = 51.250 != parent 38.500; total 51.250 = 38.500 + 12.750 (line 2). Merge adds PricingReference/AlternativeConditionPrice 51.25 as a further place. |
| Tax category O for goods (29) | Medium | yes | as cotton a/b. Money said Low: raised. 5 files with O + GOODS (cotton 01, 04, 05, 16, sea 29). |
| Category O with Percent 0 (28, 29) | Low | no | drop Percent. Added by the merge (no part raised it), as cotton, utilities, road. |
| Bench emission triple 96 / 0.82 / 1 EA, CRADLETOGATE, MANUFACTURING vs "From the ore ..." (29) | High / Medium / Medium | no | ADDED by the merge (no part raised them in 29), as a, c, retail. 39 files with factor 0.82. |
| Full catalogue item data in the till receipt (29: emission, circularity, load test, XU tariff code, keywords) | Low | no | own finding (keywords: broad + context); broad's/context's warranty refutation carried; merge extends it to the rest of the catalogue data with retail c's consumer-receipt counter-argument. |
| GTIN in Lumeway's prefix 9520610 (26 side frame 9520610000029, 29 bench 9520610000012) / world item number 7710200000xx with valid GS1 check digit | Low | yes | ADDED by the merge, as retail a/b/c. a/c: please consider (not in your rows). |
| Copied XU national tariff code in 26 (credit note, Bayvarra->Lisavu) | Low | no | folded into 26's catalogue-data finding (merge-added). |
| RegistrationDate 1996-01-01 (Velumi in all seven, Harbourline in 25/27) | - | - | NOT added: no part raised or considered it in 23-29; aligned with c ("only where a part raised it") and a ("raised or considered"). 271 in 181 files. |
| References with ID only (25 HF-FA-2026-007, HF-ASSIGN-26-0091) | Low | no | DocumentTypeCode / DocumentType. |
| Public bodies as companies | - | - | does not occur in 23-29 (Island Customs Service in 28 only with ID + name). |
| "Invoice ..." in PaymentNote of the debit note (28) | Low | no | "Debit note VT-DOC-26-0153". Same as furniture b (14). |
| 28 CollectedForParty customs for an outlay already paid; port as BeneficiaryParty on the collection line | Medium | no | money + parties. |
| 28 OriginatorParty = Island Customs Service; B/L as DeliveryNoteDocumentReference | Medium | no | separate findings (broad grouped both; context/parties/logistics separate). |

