# LLM review: 02-Catalogue.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/02-Catalogue.xml`, Git blob `1c92d827b4d756ddbac6f7506b2c222c22480912` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### retail/02#F1 · High · Emission value is not factor × base
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines ValueFactorNumeric as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure as "The base quantity to which the value factor applies". With a base of 1 EA, 0.82 × 1 = 0.82, not the 96 kg stated. No other quantity in the item gives 96 either: the bench's stated materials are 34 kg steel + 22.5 kg hardwood = 56.5 kg (`/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`, `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`), and 0.82 × 56.5 = 46.3 kg. The 96 kg itself is plausible (steel at about 2 kg CO2e/kg gives 68 kg, plus galvanising and sawing; own knowledge). The same three values occur in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`), 10 of them in retail.
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure (in consistent units), or ValueFactorNumeric and ValueBaseMeasure are absent.
- Options: (a, preferred) drop factor and base: the 96 kg is a product total from an LCA (VI-LCA-2025), not a calculation from an activity; (b) factor 96 per 1 EA; (c) a factor per kg of steel with the steel mass as base, if the LCA works that way (then the value must still equal the product).
- Needs decision: no

### retail/02#F2 · Medium · New catalogue that supersedes a previous version, in reply to a request for an update
- XPath: `/Catalogue/cbc:ActionCode` = `NEW`
- XPath: `/Catalogue/cbc:PreviousVersionID` = `0.9`
- XPath: `01-CatalogueRequest.xml:/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`
- Why: ActionCode `NEW` means "New catalogue" in the world's CatalogueActionCode list (with `REPLACE` "The catalogue replaces the earlier one in full" and `UPDATE` as the alternatives). PreviousVersionID is "An identifier for the previous version of the Catalogue that is superseded by this version": a catalogue that supersedes a version 0.9 is a replacement, not a new catalogue. The request 01 asks for an update of `LD-CAT-SPRING-26`, an ID that this catalogue does not carry. The three statements do not describe the same story. Every catalogue line has ActionCode `ADD`, which fits a new catalogue.
- Condition: ActionCode, PreviousVersionID and the request's RequestedCatalogueReference agree: either a new catalogue without a superseded previous version, or a replacement/update of a named earlier catalogue.
- Options: (a, preferred) a new catalogue: drop PreviousVersionID (and RequestedCatalogueReference in 01, see 01/F1); (b) ActionCode `REPLACE` with the earlier catalogue identified in 01.
- Needs decision: yes

### retail/02#F3 · Low · Spare bench side frame classified as a general cast article instead of a part of seats
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- XPath: `01-CatalogueRequest.xml:/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:Description` = `Outdoor furniture and its spare parts.`
- Why: The item is "Spare side frame for the Serra bench" (`/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Description`), a part solely designed for one seat. Under the HS (own knowledge of the nomenclature and its General Interpretative Rules), identifiable parts of seats of heading 9401 that are not parts of general use fall under 9401.99 ("Parts: other", not of wood), not under 7325.99 "Other cast articles of iron or steel". The request 01 also asks for HS 9401 with its spare parts. The bench itself is classified under `940179`, so the two lines use two different chapters for a bench and its own frame.
- Condition: the side frame's HS code and national tariff code are those of parts of seats (940199 and its national subdivision), or the example states why the frame is classified as a cast article.
- Options: (a, preferred) HS `940199` and the matching XU tariff line; (b) keep 7325 and accept the difference to 01 explicitly.
- Needs decision: yes (tariff classification judgement)

## Checked and consistent
- Emission magnitude: 96 kg CO2e cradle-to-gate for a bench of 34 kg galvanised cast steel and 22.5 kg hardwood is plausible (steel about 2 kg CO2e/kg, hardwood well under 0.5; own knowledge). Only the factor × base arithmetic fails (F1).
- Slats: 22.5 kg hardwood for five slats (`/Catalogue/cac:CatalogueLine[1]/cac:ComponentRelatedItem[1]/cbc:Quantity` = `5`) is 4.5 kg per slat of 1800 mm; at a hardwood density of about 700 kg/m³ that is 6.4 dm³, e.g. 1800 × 90 × 40 mm. Plausible.
- Load capacity 450 kg over three seats (150 kg per seat) is plausible for a park bench.
- Pallet: PackagingTypeCode `PX` (Rec. 21: pallet), Package quantity 4, DeliveryUnit BatchQuantity 4, ContentUnitQuantity 4, OrderQuantityIncrementNumeric 4 and MinimumOrderQuantity 4 agree with "Pallet of 4". MaximumOrderQuantity 192 is a multiple of 4 (48 pallets).
- Four benches of 1800 × 620 × 780 mm on one pallet: two benches side by side take 1800 × 1240 mm in plan; stacked two high (one inverted) that is about 1.6 m high. Fits a pallet of 1.8 m length or an overhang on a 1200 mm pallet; plausible.
- Dimensions: seat height 450 mm within its range 440–460 mm, below the back height 780 mm.
- DependentPriceReference: 64 / 520 = 12.31 %, as stated.
- ApplicableDeliveryPeriod starts 2026-04-27, after the issue date plus the 3-day lead time, and ends with the catalogue validity.
- Validity periods of the catalogue, both lines and both prices all end 2026-07-19, as in 01.
- GTINs `9520610000012` and `9520610000029` pass the check digit (check_ids.py) and lie in GS1's demonstration prefix 952.
- References: `LD-BM-SUPPLY-2026`, `LD-GTC-2026`, `LD-PL-2026` and the item documents `VI-DS-B180`, `VI-LCA-2025`, `VI-RM-B180` are used with the same meaning in the other retail examples and in other flows (road, rail, sea, tender).
- HS `940179` (other seats with metal frames) fits a bench with cast steel frames and hardwood slats.

## Considered and refuted
- `/Catalogue/cac:SourceCatalogueReference/cbc:ID` = `VI-CAT-2026`: suspected broken reference (no example has this ID) — refuted because the source catalogue is Valdara's own catalogue to its distributor, outside this flow; the reference is to an external document, not to an example.
- `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`: suspected unresolved — refuted because ReplacedRelatedItem names an item in an earlier catalogue, which need not be an example; the newer casting `VI-C180-2026` is used in `tender/15-Tender.xml`, which fits the story of a casting revision.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteMeasure` = `0.4`: 0.4 kg stretch film and straps per bench, 1.6 kg per pallet of four — plausible.
