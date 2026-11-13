# LLM review: 02-Catalogue.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/02-Catalogue.xml`, Git blob `9ab014c2e27df7270bfea2ec3db014a3637bf54d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/02#F1 · High · Emission factor times base does not give the emission value
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". Factor × base is therefore the value: 0.82 × 1 EA = 0.82, not 96 kg CO2e. No other reading closes the gap: 96 / 0.82 = 117, which is neither the bench's mass (the packing list's net weight is about 38 kg per bench, `10-PackingList.xml:/PackingList/cac:Shipment/cbc:NetWeightMeasure` = `3762` for 96 benches and 12 frames) nor its material input (34 kg steel + 22.5 kg hardwood in the circularity profile). The same triple occurs in 39 XML examples, 9 of them in this flow (counted with `grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>' world/examples`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` = `ValueMeasure` (in the units given), or the factor and base are absent.
- Options: drop factor and base and keep the 96 kg per bench as a plain value (preferred: the catalogue states a per-unit footprint, which `ValueMeasure` alone carries); or give the factor on a real base (e.g. kg CO2e per kg of steel, with the base in KGM) so that the product is 96.
- Needs decision: no

### sea/02#F2 · Low · Applicable sales territory is Bayvarra for a catalogue priced for export to Lisavu
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: `ApplicableTerritoryAddress` is "The applicable sales territory" of the item location quantity, i.e. where these prices, lead times and delivery units apply. The same quantity block applies tax category `G` "Free export item" with reason `Export outside Bayvarra`, the catalogue goes to Velumi Trading in Lisavu, and the order delivers CIF Port of Selanu (`05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`). A territory of Bayvarra and an exemption for export outside Bayvarra describe two different places of sale.
- Condition: the territory of each line agrees with the tax treatment and the delivery it is priced for.
- Options: territory Lisavu (XL) (preferred: matches the export exemption and the receiver); or keep Bayvarra and say in the block that the price is ex Bayvarra for export (a story choice).
- Needs decision: yes

## Checked and consistent
- Packaging data agree: `Package` `PAL-4` holds 4 benches, the delivery unit `BatchQuantity` is 4, `MinimumQuantity` is 4 and the transaction conditions say "per pallet of four benches"; the bill of lading's bench pallets each carry 4 (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`). The order of 96 benches lies between minimum 4 and maximum 192 and is a multiple of 4.
- Dimensions (1800 × 620 × 780 mm, seat 450 mm within 440–460 mm) are the same in the order, packing list and export declaration.
- Physics: material input of 34 kg steel and 22.5 kg hardwood per bench against the packing list's net weight of about 38 kg per bench: with a casting yield of about 0.7 and a sawing yield of about 0.6 (own knowledge) the input gives about 24 + 13.5 = 37.5 kg of product, so "consumed" material above the product mass is plausible. Packaging waste of 0.4 kg film and straps per bench is plausible for stretch film.
- 96 kg CO2e cradle-to-gate per bench against 34 kg steel: about 2 kg CO2e per kg of galvanised cast steel (own knowledge) gives about 70 kg, plus sawing and transport, so the value itself is plausible (the problem is only F1).
- GTINs `9520610000012` and `9520610000029` have valid check digits (`check_ids.py`); prefix 952 is GS1's demonstration prefix.
- Validity: catalogue and price validity 2026-05-04 to 2026-10-31; the order of 2026-05-07 and the shipment of 2026-05-14 fall inside it, and inside the applicable delivery period starting 2026-05-11.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MaximumQuantity` = `192`: suspected as "one full container" next to the full-container discount, which would not fit the volumes in the flow (96 benches take 41.5 m³ gross, `06-OrderResponse.xml:/OrderResponse/cbc:GrossVolumeMeasure` = `41.5`, so 192 would need about 83 m³ against about 67.7 m³ inside a 40-foot box) — refuted because nothing in the catalogue ties the maximum to one container; the discount's condition is stated only as "Full container".
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180` and the other item document references (`VI-LCA-2025`, `VI-RM-B180`, `LD-GTC-2026`) resolve to no example — refuted as a problem: each sits in an element that names what it is (specification, emission factor source, product documentation, transaction conditions).
