# LLM review: 11-ExportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/11-ExportCustomsDeclaration.xml`, Git blob `6df68444b58544480345d9e469661ab775d8d16a` (committed)
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

### sea/11#F1 · Medium · Shipment-level customs and statistical values add up goods of two different tariff headings
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredCustomsValueAmount` = `50688.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredStatisticsValueAmount` = `50688.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `940179`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- Why: under Shipment, `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of those goods in this shipment that are subject to the same customs procedure and have the same tariff/statistical heading", and `DeclaredStatisticsValueAmount` is "the value, declared for statistical purposes, of those goods in this shipment that have the same statistical heading". The shipment holds two goods items under different headings (HS 940179 benches, HS 732599 cast side frames; national 94017910 and 73259990). 50,688.00 is the sum of both goods items (49,920.00 + 768.00), i.e. a value across two headings, which the definitions exclude. Per heading, the values are already given on the goods items (`/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`, `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `768.00`). (The Consignment-level element in the bill of lading has a different definition, "regardless of whether they are subject to the same … tariff/statistical categorization", and would fit a total; the Shipment-level one does not.)
- Condition: no Shipment-level customs or statistical value in the declaration covers goods of more than one tariff/statistical heading.
- Options: (a) preferred: drop the two Shipment-level values and keep the per-goods-item customs values (adding per-item statistical values if the export statistics need them); (b) if a declaration total is wanted, carry it in an element whose definition allows a total across headings.
- Needs decision: no

### sea/11#F2 · Low · Ocean freight and insured value in an export declaration valued free on board
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:FreightAllowanceCharge/cbc:Amount` = `2950.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:InsuranceValueAmount` = `59155.80`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:FreeOnBoardValueAmount` = `50688.00`
- Why: the export declaration values the goods at the frontier of Bayvarra: customs, statistical and FOB values are all 50,688.00, the value on board at Lumeport. The ocean freight from Lumeport to Selanu (`FreightAllowanceCharge`, "a cost incurred by the shipper in moving goods … under the terms of the contract of carriage") and the insured value for the voyage arise after the goods leave Bayvarra's customs territory and enter none of the values declared; Bayvarra's customs does nothing with them in this declaration. They are needed at import in Lisavu, where the import declaration does use them (`19-ImportCustomsDeclaration.xml` adds a freight share to the customs value). This is data the document's purpose does not use (no fillers).
- Condition: the export declaration carries the post-export freight and the insured value only if Bayvarra's export procedure uses them (e.g. for a CIF-based statistical value), and then the declared values reflect that use.
- Options: (a) preferred: remove both from the export declaration; (b) if Bayvarra's export statistics are CIF-based, state the statistical value on that basis (53,778.00) and keep the freight and insurance as its components.
- Needs decision: no

## Checked and consistent
- Goods-item values: 96 × 520.00 = 49,920.00 and 12 × 64.00 = 768.00, as in the order, the order response and the invoice; sum 50,688.00 = the declared FOB value, and equal to the invoice's goods total (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`).
- Freight 2,950.00 = ocean freight 2,700.00 + bunker surcharge 250.00 of the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `2700.00`, `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:ExtraAllowanceCharge/cbc:Amount` = `250.00`) and the sea-freight charge of the invoice.
- Insured value 59,155.80 = 110 % of the CIF value 53,778.00, the same in the forwarding instructions, the bill of lading and the import declaration.
- The customs agent Bayforth Forwarding bills the lodging of this declaration to the exporter in `18-Invoice.xml` (85.00 lume).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:FreeOnBoardValueAmount` = `50688.00`: suspected that the FOB value should include the pre-carriage by road to Lumeport (310.00 in `14-BillOfLading.xml`), which happens before the goods are on board — refuted because under CIF the seller bears that cost and does not bill it to the buyer; the goods price of 50,688.00 is the price at which the seller delivers on board, so it is the FOB value whether or not the seller's own haulage cost is listed somewhere.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredCustomsValueAmount` = `50688.00` against `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`: suspected two customs values for the same consignment — refuted because export (FOB at the Bayvarran frontier) and import into Lisavu (CIF) value the same goods differently by design; the difference is the freight and insurance (2,950.00 + 140.00).
