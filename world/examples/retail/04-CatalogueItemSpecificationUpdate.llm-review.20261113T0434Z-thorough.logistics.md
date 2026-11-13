# LLM review: 04-CatalogueItemSpecificationUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/04-CatalogueItemSpecificationUpdate.xml`, Git blob `bc08c5d7cc1e9ec6f62cb02c0b6ddfcd217352bc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/04#F1 · High · Reference to the catalogue gives an issue time and a revision that the catalogue does not have
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:IssueTime` = `09:01:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:VersionID` = `1.0`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:VersionID` = `1.1`
- Why: The reference describes the catalogue being updated. Its IssueTime (09:00) is not 02's issue time (17:28; 09:00 is 02's RevisionTime). Its "last revised" date and time, 2026-05-21 14:00, lie five hours after this document was issued (2026-05-21 09:01), so they are in the future. Its VersionID 1.0 ("the current version of the catalogue") ignores the pricing update 03, which made the catalogue version 1.1 the day before; this update makes it 1.2. The same reference values occur in 03 and 20.
- Condition: the reference's issue date and time are those of 02; its revision date/time and version are those of the catalogue as it stood when this document was issued (after 03: version 1.1, revised 2026-05-20), never later than this document's issue time.
- Options: (a, preferred) IssueTime `17:28:00`, revision 2026-05-20 with 03's revision time, VersionID `1.1`; (b) drop revision date/time and version from the reference and keep ID and UUID.
- Needs decision: no

### retail/04#F2 · High · Emission value is not factor × base
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement"; 0.82 × 1 EA = 0.82, not 96 kg. Same problem as 02/F1; it occurs in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base (the 96 kg is an LCA product total); (b) factor 96 per 1 EA.
- Needs decision: no

### retail/04#F3 · Low · The specification update changes only the description; the structured data still describe the old slats
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cbc:Description` = `Park bench, 1800 mm, frame of cast and galvanised steel, five slats of another kiln-dried hardwood, for bolting to the ground.`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:AdditionalItemProperty[2]/cbc:Value` = `Kiln-dried hardwood`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ResourceOriginDescription` = `Slats from Upland State, Bayvarra`
- Why: The document's purpose is "New slat wood for the Serra 180" (`/CatalogueItemSpecificationUpdate/cbc:Name`). Only the free-text description says "another" hardwood, without naming it; the slat-wood property, the hardwood mass, its origin, the emission (measured over 2025, i.e. for the old wood) and every identifier are unchanged from 02. A receiver cannot tell what the new wood is or whether the bench's mass changed: a different hardwood (density from about 550 to over 900 kg/m³; own knowledge) changes the 22.5 kg of slats accordingly.
- Condition: the structured item data that the change affects (slat wood property; hardwood mass and origin, if they change) describe the new wood, and the description names it.
- Options: (a, preferred) name the new wood in the description and the "Slat wood" property, and update the hardwood ResourceConsumption; (b) if mass, origin and emissions are truly unchanged, say so in the description.
- Needs decision: yes (which wood replaces the old one is part of the story)

### retail/04#F4 · Low · Own revision date and validity start lie before the issue, on the day of the pricing update
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:IssueDate` = `2026-05-21`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- Why: This update creates version 1.2, but carries the same revision date and time as the pricing update 03 (version 1.1), and its new specification is valid from the day before it was sent. Either both changes were one revision (then two versions are one too many), or this revision was made on 2026-05-21 and takes effect then; a retroactive change of a product specification is unusual and not explained.
- Condition: the revision date/time are those of this revision (version 1.2) and not later than the issue; the validity start is not before the issue date unless a note gives the reason.
- Options: (a, preferred) revision date 2026-05-21 before 09:01 and validity from 2026-05-21; (b) keep 2026-05-20 and add a note that the new wood was already delivered from that day.
- Needs decision: no

## Checked and consistent
- RelatedCatalogueReference ID `LD-CAT-26-0218` and UUID `f5163e36-0159-5b9f-b172-a86137e369e6` match 02-Catalogue.
- Update line ID `1` is catalogue line 1, the bench (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10442`), the item this update is about; the seller's item ID, GTIN `9520610000012` (check digit OK) and manufacturer ID `VI-B180` agree with 02.
- Dimensions (1800 × 620 × 780 mm, seat height 450 mm within 440–460 mm), HS `940179` and national tariff `94017910` agree with 02.
- Validity end 2026-07-19 agrees with the catalogue.
- LineCountNumeric `1` equals the number of update lines.

## Considered and refuted
- `/CatalogueItemSpecificationUpdate/cbc:VersionID` = `1.2`: suspected to skip a version — refuted because 03 made version 1.1, so 1.2 follows it; only the reference's VersionID is stale (F1).
