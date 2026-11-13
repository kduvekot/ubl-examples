# LLM review: 01-CatalogueRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/01-CatalogueRequest.xml`, Git blob `571e96113517945d8ea407ef7718908cdaf87ade` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 89446f0 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/01#F1 · Medium · Requested catalogue reference points to a catalogue that exists nowhere, and the answer is a new catalogue
- XPath: `/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ID` = `LD-CAT-26-0218`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ActionCode` = `NEW`
- Why: UBL defines RequestedCatalogueReference as "A reference to a specific Catalogue; used if the Catalogue Request is for an update." The identifier `LD-CAT-SPRING-26` occurs in no other example (searched over `world/examples/*/*.xml`), and the catalogue sent in reply, 02-Catalogue, has a different ID and declares itself a new catalogue (`NEW`), not an update of an existing one. Either the request asks for an update of a catalogue the flow should be able to resolve, or it asks for a new catalogue and the reference has no business reason.
- Condition: either the request carries no RequestedCatalogueReference (a request for a new catalogue), or the referenced ID is that of a catalogue that the reply 02-Catalogue updates or replaces, consistent with 02's ActionCode and PreviousVersionID.
- Options: (a, preferred) drop the reference: the story is a first spring catalogue for the garden department, which 02's `NEW` already says; (b) make 02 an update/replacement of a named earlier catalogue and cite that ID here. The two indicators PricingUpdateRequestIndicator and ItemUpdateRequestIndicator lean towards (b); the fixing session should settle the story with 02/F1.
- Needs decision: yes

### retail/01#F2 · Medium · Requested HS classification: a non-HS code as subcategory, and a heading wider than its description
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cac:CategorizesClassificationCategory/cbc:CodeValue` = `FUR-OUT-SP`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:CodeValue` = `9401`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:Description` = `Outdoor furniture and its spare parts.`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:Note` = `Six-digit subheadings.`
- Why: The scheme is the WCO Harmonized System 2022 (`/CatalogueRequest/cac:RequestedClassificationScheme/cbc:ID` = `HS`). CodeValue is "The value of a code used to identify this category within the classification scheme"; `FUR-OUT-SP` is not an HS code, so the subcategory does not belong to the scheme it is placed in. The note asks for six-digit subheadings, but the category is the four-digit heading 9401, and the HS subheading for parts of seats is 9401.99 (HS 2022: 9401.91 parts of wood, 9401.99 other; own knowledge of the HS nomenclature). Heading 9401 is "Seats", not "outdoor furniture" (outdoor tables fall under 9403). 02-Catalogue then classifies the spare side frame under `732599`, outside the requested heading (see 02/F3).
- Condition: every CodeValue inside the HS scheme is an HS 2022 code, and the description matches the HS heading or subheading it describes.
- Options: (a, preferred) category `9401` "Seats", subcategory `940199` "Parts of seats, other than of wood"; (b) if the retailer's own category code is wanted, put it in a second ClassificationScheme of Brightmarket's own.
- Needs decision: no

### retail/01#F3 · Medium · LocaleCode carries a language code
- XPath: `/CatalogueRequest/cac:RequestedLanguage/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used", i.e. a language in a region (e.g. English as used in Bayvarra), whereas `en` with `listID="ISO 639"` is the language alone and repeats `/CatalogueRequest/cac:RequestedLanguage/cbc:ID` = `en`. The value adds nothing to the ID next to it. The same `ISO 639` value in LocaleCode occurs in all 22 retail examples (counted with `grep -c LocaleCode world/examples/retail/*.xml`) and in 213 examples over the whole world (`grep -rl --include='*.xml' LocaleCode world/examples | wc -l`), most of them in party Language aggregates.
- Condition: LocaleCode holds a locale (language plus territory, from a locale list), or is absent.
- Options: (a, preferred) drop LocaleCode where it only repeats the language ID; (b) use a locale code (e.g. a BCP 47 / CLDR style `en-XB`) with its own listID, if the world defines such a list.
- Needs decision: yes (the binding of LocaleCode to the language list is a repository-wide choice)

### retail/01#F4 · Low · Document reference with an ID only
- XPath: `/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: The reference has no DocumentTypeCode or DocumentType, so a reader cannot tell what `BM-RANGE-26` is. The only other occurrence is `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` = `BM-RANGE-26`, where it is Brightmarket's own range catalogue; in this request it is not obvious.
- Condition: the reference says what kind of document `BM-RANGE-26` is (type code or type text).
- Options: add DocumentType "Brightmarket range plan 2026" (or the matching type code).
- Needs decision: no

## Checked and consistent
- ValidityPeriod 2026-04-20 to 2026-07-19 starts on the issue date and equals the validity period of 02-Catalogue (`02-Catalogue.xml:/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2026-07-19`).
- Party identifiers: GLNs `9520610900008` and `9522610900002` pass the GS1 check digit (check_ids.py); prefix 952 is GS1's demonstration range, so they cannot be mistaken for real ones.
- ReferencedContract `LD-BM-SUPPLY-2026` is the same contract as in 02-Catalogue.
- HS version 2022 with LastRevisionDate 2022-01-01: HS 2022 entered into force on 1 January 2022 (own knowledge).
- LineCountNumeric `2` equals the number of CatalogueRequestLine elements.

## Considered and refuted
- `/CatalogueRequest/cac:CatalogueRequestLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `24`: suspected to contradict the pallet of four benches in 02-Catalogue — refuted because MinimumQuantity here is the quantity from which the retailer asks for a price ("Pallet prices, please"); 24 benches are six pallets of four, so the request is compatible with 02's pallet unit and its 4–192 price band.
- `/CatalogueRequest/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store.`: suspected odd for a domestic sale — refuted because both parties are in Bayvarra and DDP to the store is still a meaningful delivery term (seller bears transport to the store); it agrees with 02-Catalogue's trading terms.
