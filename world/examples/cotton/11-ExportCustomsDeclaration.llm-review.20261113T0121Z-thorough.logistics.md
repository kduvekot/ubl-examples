# LLM review: 11-ExportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/11-ExportCustomsDeclaration.xml`, Git blob `6a4c14a5a30406d882ebdc39fccad12bc46c7e0e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/11#F1 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count; here it carries the nominal bale weight in kilograms. A customs declaration normally states the number and kind of packages (27 bales); that count is stated nowhere. Same as in 02, 07, 08, 10, 15 and 16.
- Condition: `PackSizeNumeric`, where present, is a count; the number of bales is stated as a count of packages.
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric`; add a `Package` (27 bales) to the goods item.
- Needs decision: no

### cotton/11#F2 · Low · Shipment gross weight excludes the transport equipment
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment". 6190.29 kg is the goods with packaging (= the goods item's gross weight in the same document); with the container (tare 3750 kg, 12) the shipment weighs 9940.29 kg. Customs practice declares the gross mass without the container; under the agreed rule of semantic conformance the UBL definition applies.
- Condition: the shipment gross weight includes the transport equipment, or is left to the goods item, whose definition fits 6190.29 kg.
- Options: (preferred) drop the shipment gross weight (the goods item carries it); or state 9940.29 kg.
- Needs decision: no

### cotton/11#F3 · Low · Exit office only by name, and no container or transport at exit
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cbc:ID` = `XLSEL`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4123110`
- Why: The exit office is named only by text, while the port of Selanu is identified elsewhere in the flow by `XLSEL`. The declaration, made "before the goods leave", does not say how they leave: no container (`TWLU4123110`, weighed the same afternoon, 12), no mode or means of transport at the border. An export declaration normally carries the container identification and the mode of transport at exit (own knowledge of customs data models). These are details the document could carry, not contradictions.
- Condition: the exit office location carries the identifier used for the same port elsewhere in the flow; the container and the transport mode at exit are stated, or their absence is deliberate.
- Options: (preferred) add `ID` `XLSEL` to the exit office location and a transport handling unit with the container to the shipment; optionally the main-carriage mode (sea).
- Needs decision: no

## Checked and consistent
- Shipment `SCG-SH-26-0200` and consignment `LTM-CS-26-0201` are the same as in 09, 10, 12, 13 and 15; goods item gross 6190.29 kg, quantity 6129 kg, declared value 6055.452 XLC agree with 10 and with the order value (08).
- The FOB value 6055.452 XLC is the export value at the frontier, consistent with FOB Port of Selanu (08).
- Issued 2026-03-01 13:33, before the weight statement (12, 15:19) and the bill of lading (13, 2026-03-02); validity 90 days.
- `AdditionalDocumentReference` `LTM-PO-26-0198` resolves to the order 08.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`, different from the document ID `SCG-EX-26-0203`: suspected as a duplicate identifier — refuted because `CustomsDeclaration/ID` is "an identifier associated with customs related procedures", a reference of the procedure distinct from the message ID, and 15 refers to it as the previous customs declaration.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID`: the phytosanitary certificate `SCC-GC-26-0202` (10) is not referenced — refuted as a finding of this example because the certificate is required by the importing country (its applicable territory is XB), so the export declaration has no need to carry it.
