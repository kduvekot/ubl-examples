# LLM review: 05-Order.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/05-Order.xml`, Git blob `f1e12ba8710e50edcc4d14d6820937dec2dde266` (committed)
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

### sea/05#F1 · High · Ordered package holds 24 benches, the pallet holds 4
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:Quantity` = `24`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:PackagingTypeCode` = `PX`
- Why: `Package/Quantity` is "The quantity of items contained in this package". The order says one pallet (`PX`) contains 24 benches. The catalogue it orders from packs 4 benches per pallet (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Package/cbc:Quantity` = `4`), the line's own transaction conditions say "per pallet of four benches", and the bill of lading carries 24 pallets of 4 benches each (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`). 24 is the number of pallets (96 / 4), not the content of one. A pallet of 24 benches of 1800 × 620 × 780 mm would also not fit through a container door.
- Condition: the package's quantity is the number of benches per pallet (4); the number of pallets, if the order states it, is carried in an element meant for a count of packages.
- Options: `Quantity` 4 with the pallet count left to the despatch documents (preferred: matches the catalogue's package `PAL-4`); or keep 24 pallets as a count (e.g. on the ordered shipment's `TotalTransportHandlingUnitQuantity`) and the package with 4.
- Needs decision: no

### sea/05#F2 · High · Emission factor times base does not give the emission value
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies"; 0.82 × 1 EA = 0.82, not 96 kg CO2e. The data is copied from the catalogue (`02-Catalogue.xml`, same values); the same triple is in 39 XML examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>' world/examples`).
- Condition: factor × base = value, or factor and base are absent.
- Options: as for the catalogue: drop factor and base (preferred), or give a factor on a base whose product is 96.
- Needs decision: no

### sea/05#F3 · Low · Delivery places described only in text, though identified elsewhere in the flow
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Lanoro warehouse, Selanu`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Port of Selanu`
- Why: the Incoterms place is the port the order response, bill of lading and invoice identify as UN/LOCODE `XLSEL` (`06-OrderResponse.xml:/OrderResponse/cac:DeliveryTerms/cac:DeliveryLocation/cbc:ID` = `XLSEL`). The delivery location "Lanoro warehouse" appears in no other example (`grep -rn --include='*.xml' Lanoro world/examples` finds only this one); the despatch advice delivers to Nalevi Warehousing at Lagoon Road 9, Selanu (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `95940358`). Without an ID or address, the place in the order cannot be matched to the later documents.
- Condition: the delivery terms' location carries the port's LOCODE, and the delivery location is identified (delivery-point ID or address) the same way as in the despatch advice.
- Options: add `XLSEL` and the warehouse's delivery-point ID/address (preferred); or name the warehouse the same way in all documents.
- Needs decision: no

## Checked and consistent
- Quantities 96 benches and 12 frames are the same in the order response, packing list, export declaration and bill of lading (24 pallets × 4 benches + 1 pallet of 12 frames).
- The order references the catalogue `LD-CAT-26-0124` (exists, `02-Catalogue.xml`, issued 2026-05-04 and valid from that day); prices and item identifiers match it.
- 96 is within the catalogue's minimum 4 and maximum 192 and a multiple of the delivery unit of 4.
- `check_ids.py`: GLN and GTIN-related identifiers valid.
