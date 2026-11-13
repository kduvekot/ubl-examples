# LLM review: 11-ExportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/11-ExportCustomsDeclaration.xml`, Git blob `6a4c14a5a30406d882ebdc39fccad12bc46c7e0e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/11#F1 · Medium · Shipment gross weight without the container
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment"; the goods item's gross weight is the same figure "excluding the carrier's equipment". Both cannot be true for a shipment in a container of 3750 kg tare; the verified gross mass declared the same day is 9940.29 kg.
- Condition: the shipment gross weight includes the transport equipment, or only the goods-item gross weight is given.
- Options: (preferred) drop the shipment gross weight and keep the goods-item figure, which is what customs needs; or 9940.29 kg.
- Needs decision: no

### cotton/11#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/11#F3 · Low · The customs authority's contact for an export is its import office
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Import office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:ElectronicMail` = `import@customs-xl.example`
- Why: the customs party "processes this Customs Declaration", an export declaration lodged for exit at the port of Selanu; its contact is the import office.
- Condition: the customs party's contact is the office that handles exports (or the exit office at the port).
- Options: (preferred) an export / port office contact; or a neutral customs contact.
- Needs decision: no

### cotton/11#F4 · Low · Neither the number of bales nor the phytosanitary certificate
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`
- Why: an export declaration normally states the number and kind of packages and the documents that accompany the goods (own knowledge of customs practice). The 27 bales are not counted, and the phytosanitary certificate issued the day before for this shipment (`10-GoodsCertificate.xml:/GoodsCertificate/cbc:ID` = `SCC-GC-26-0202`) is not referred to; the only reference is the buyer's order.
- Condition: the declaration states the number of bales and refers to the phytosanitary certificate.
- Options: (preferred) a package count of 27 bales and an additional document reference to SCC-GC-26-0202 with its type.
- Needs decision: no

### cotton/11#F5 · Low · The consignee's contact is its purchasing desk in sales
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: as cotton/09#F7: a consignee's contact receives goods; here name and department also contradict each other.
- Condition: a receiving contact whose name and department agree.
- Options: (preferred) goods-in / import desk of the mill.
- Needs decision: no

### cotton/11#F6 · Low · Classing results in the applicant's remarks
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: as cotton/02#F5.
- Condition: the result is not carried as an applicant's remark.
- Options: (preferred) drop the remark.
- Needs decision: no

### cotton/11#F7 · Low · Origin area in `Region`, in `District` in the farm's address
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- Why: as cotton/02#F6.
- Condition: the north coast in the same element everywhere.
- Options: (preferred) `District`.
- Needs decision: no

### cotton/11#F8 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: as cotton/02#F7.
- Condition: the bale weight is not carried as a count.
- Options: (preferred) drop the pack elements; count the bales (F4).
- Needs decision: no

## Checked and consistent
- The customs declaration ID SCG-CD-26-0204 is cited by the import declaration as the previous declaration (`15-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`).
- Declared value 6055.452 XLC = invoice 16 (FOB value, the usual basis of an export value); exit office port of Selanu = exit office in 15.
- Shipment and consignment IDs, exporter, consignor and consignee agree with 09, 10, 13 and 15; issued on 1 March, before loading (bill of lading 2 March), as the note says.
- Function code 9 (Original) of UN/EDIFACT 1225; permanent export, reason sale.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 90 days of validity — refuted: a plausible period within which the goods must leave.
