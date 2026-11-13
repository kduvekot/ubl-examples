# LLM review: 15-ImportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/15-ImportCustomsDeclaration.xml`, Git blob `243bca671cf988608608ddfeb177ea4ed50c7765` (committed)
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

### cotton/15#F1 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count; here it carries the nominal bale weight in kilograms. The number of packages (27 bales), which an import declaration normally states, is given nowhere. Same as in 02, 07, 08, 10, 11 and 16.
- Condition: `PackSizeNumeric`, where present, is a count; the number of bales is stated as a count of packages.
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric`; add a `Package` (27 bales) to the goods item.
- Needs decision: no

### cotton/15#F2 · Low · Phytosanitary certificate not presented with the import declaration
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0206`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cbc:ID` = `SCC-GC-26-0202`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: The phytosanitary certificate 10 was issued for this shipment because Bayvarra's plant-health rules require it ("free of the pests named by Bayvarra's plant health rules"), is valid in XB until 2026-03-14 and names the mill as importer. The import declaration for release into free circulation, made on 2026-03-06 within that validity, refers only to the bill of lading; the certificate the release depends on is not referenced, so nothing in the flow uses it at import.
- Condition: the import declaration refers to the phytosanitary certificate `SCC-GC-26-0202`, or the flow shows another way in which it is presented to the Bayvarran authorities.
- Options: (preferred) add an `AdditionalDocumentReference` to `SCC-GC-26-0202` with its document type.
- Needs decision: no

### cotton/15#F3 · Low · Shipment gross weight excludes the transport equipment
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment"; 6190.29 kg is the goods with packaging (the goods item's gross weight in the same document); with the container it is 9940.29 kg (12). Customs practice declares gross mass without the container; under the agreed rule of semantic conformance the UBL definition applies.
- Condition: the shipment gross weight includes the transport equipment, or is left to the goods item.
- Options: (preferred) drop the shipment gross weight; or state 9940.29 kg.
- Needs decision: no

## Checked and consistent
- `AdditionalDocumentReference` `TOL-BL-26-0206` resolves to the bill of lading 13; shipment `SCG-SH-26-0200`, consignor, consignee, goods item gross 6190.29 kg and quantity 6129 kg agree with 10, 11 and 13.
- `PreviousCustomsDeclaration` `SCG-CD-26-0204` is `11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID`, and the exit office "Customs office, port of Selanu" is the same as in 11.
- Customs value 15138.63 XBL = 6055.452 XLC × 2.5 (the XLC → XBL rate used in 04 and 05); whether Bayvarra values on FOB or CIF is a money question.
- Issued 2026-03-06, after the bill of lading (2026-03-02) and the pre-arrival report (2026-03-03), within the validity of the phytosanitary certificate (to 2026-03-14).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`: an export declaration of another country as "previously sent customs declaration" was suspected — refuted because the definition ("a reference to a previously sent customs declaration") does not restrict it to the importing country, and the export declaration is the previous customs declaration of these goods.
