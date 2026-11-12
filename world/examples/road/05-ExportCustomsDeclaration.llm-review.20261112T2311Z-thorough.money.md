# LLM review: 05-ExportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/05-ExportCustomsDeclaration.xml`, Git blob `0fa315bd3a963ac3f8916911094b6904a7e60fbf` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

## Checked and consistent
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400` is 96 × 49 900, the order and invoice line amount (`15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `4790400`); `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `71760` is 12 × 5 980 (`15-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `71760`). Both are in XUF, the currency of the sale.
- The exporter here is the seller of the invoice (`/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`, `15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`), which supports the export exemption `G`/`EXP` of the invoice.
- The import side converts the same values at 0.01 XBL per XUF (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400`: suspected that an export value should be the value at the frontier of the exporting country (FOB-type), i.e. include the haulage from Ferrano to the border, not the FCA warehouse price — refuted because the declared customs value of an export is commonly the transaction value of the sale (here FCA, the price the exporter actually invoices); the frontier value is a statistical value, which UBL holds in a separate element (`DeclaredStatisticsValueAmount`), absent here (own knowledge of customs practice).
