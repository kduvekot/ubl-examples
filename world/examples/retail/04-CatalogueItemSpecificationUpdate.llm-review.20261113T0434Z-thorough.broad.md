# LLM review: 04-CatalogueItemSpecificationUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/04-CatalogueItemSpecificationUpdate.xml`, Git blob `bc08c5d7cc1e9ec6f62cb02c0b6ddfcd217352bc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/04#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: the factor is "used to calculate the value measurement (e.g., emissions per unit of activity)" and the base is "The base quantity to which the value factor applies". With a base of 1 each, the factor says 0.82 kg CO2e per bench, the value 96 kg per bench. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) state the activity and its unit so that the product is 96 kg.
- Needs decision: no

### retail/04#F2 · High · Reference to the catalogue disagrees with the catalogue and lies in the future
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:VersionID` = `1.0`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionDate` = `2026-04-20`
- Why: the reference resolves to 02-Catalogue (ID and UUID), but its issue time 09:00 is not 02's (17:28), and its last revision, 2026-05-21 14:00, is five hours after this document was issued (2026-05-21 09:01) and matches neither 02 (2026-04-20) nor 03-CataloguePricingUpdate (2026-05-20 14:00). With version `1.0` it also refers to the catalogue as it was before 03 made it version 1.1, while dating its last revision after 03.
- Condition: the reference describes one catalogue version consistently (its issue and revision date and time as in that version's document), and nothing in it lies after this document's issue.
- Options: (a, preferred) refer to version 1.1 as left by 03 (revision 2026-05-20, with a time before 03's issue) or to version 1.0 with 02's dates; (b) drop the dates and keep ID, UUID and version.
- Needs decision: no

### retail/04#F3 · Medium · Item specification update about new slat wood that does not state the new wood
- XPath: `/CatalogueItemSpecificationUpdate/cbc:Name` = `New slat wood for the Serra 180`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cbc:Description` = `Park bench, 1800 mm, frame of cast and galvanised steel, five slats of another kiln-dried hardwood, for bolting to the ground.`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:AdditionalItemProperty[2]/cbc:Value` = `Kiln-dried hardwood`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ResourceOriginDescription` = `Slats from Upland State, Bayvarra`
- Why: the purpose of this document is to tell the buyer what changed in the item's specification: the slat wood. The only trace of the change is "another kiln-dried hardwood" in the description; the property "Slat wood", the hardwood consumption (22.5 kg from Upland State), the emission (96 kg, measured over 2025) and the circularity data are exactly those of 02-Catalogue (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[2]/cbc:Value` = `Kiln-dried hardwood`). The receiver cannot see which wood the slats are now made of, nor whether weight, origin or emissions change with it.
- Condition: the updated item states the new slat wood in the property that describes it, and the values that depend on the wood (consumption, origin, emission) are either updated or explicitly confirmed as unchanged.
- Options: (a, preferred) name the new species or wood in the "Slat wood" property and adjust or confirm the dependent values; (b) if the wood is meant to stay unnamed, say so in a note, and explain why the other values do not change.
- Needs decision: yes

### retail/04#F4 · Medium · Language codes in LocaleCode
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats the language code. 362 occurrences in 213 examples (`grep -rho --include='*.xml'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it.
- Needs decision: no

### retail/04#F5 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is a vehicle access detail. 76 examples carry it.
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address; (b) record it in Bayvarra's address format if it really belongs there.
- Needs decision: no

### retail/04#F6 · Low · Two different catalogue versions with the same revision time
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- Why: this update makes the catalogue version 1.2; the pricing update 03 made it version 1.1 and gives the same revision date and time (2026-05-20 14:00). Two revisions of the same catalogue cannot have happened at the same moment; one of the times is a copy.
- Condition: version 1.2 has its own revision date and time, after that of version 1.1 and before this document's issue.
- Options: (a, preferred) a revision time between 03's and this document's issue; (b) drop the revision time.
- Needs decision: no

### retail/04#F7 · Low · Urvanian customs tariff code in a Bayvarran domestic catalogue update
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: the code is from Urvania's national tariff; the catalogue is between two Bayvarran parties for Bayvarra only, so neither uses it.
- Condition: national tariff codes are those of a customs territory the parties deal with, or absent.
- Options: (a, preferred) drop it.
- Needs decision: no

### retail/04#F8 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: name, job title and department contradict each other. Same contact in all 19 retail examples that describe Brightmarket.
- Condition: name, job title and department agree with each other and with the buying role.
- Options: (a, preferred) buyer's job title and purchasing department.
- Needs decision: no

### retail/04#F9 · Low · Header parties repeated on the line
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:ContractorCustomerParty`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:SellerSupplierParty`
- Why: the line's parties are the header's; they add nothing (no-filler rule).
- Condition: line-level parties only where they differ from the header.
- Options: (a, preferred) drop them.
- Needs decision: no

## Checked and consistent
- The update line `1` is the bench line of 02-Catalogue, and the item (seller's ID `LD-10442`, GTIN `9520610000012`, manufacturer's ID `VI-B180`) is the bench, as the name says.
- Item identity, dimensions, load capacity, warranty, classification and transaction conditions agree with 02-Catalogue.
- `VersionID` `1.2` follows 03's `1.1`; signature ID follows the version.
- Validity 2026-05-20 to 2026-07-19 lies within the catalogue's validity.
- GTIN and GLN check digits pass (check_ids.py).

## Considered and refuted
- `/CatalogueItemSpecificationUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`: suspected a retroactive start (issue on 2026-05-21) — refuted because the specification was revised on 2026-05-20 and a validity from the revision date is plausible.
- `/CatalogueItemSpecificationUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`: suspected filler — refuted, it states explicitly that the terms do not change.
