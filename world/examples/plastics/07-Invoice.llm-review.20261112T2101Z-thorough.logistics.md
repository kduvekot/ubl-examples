# LLM review: 07-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/07-Invoice.xml`, Git blob `a1e9b7e2c326a01d31d3b741f419d375d10a04e9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/07#F1 · High · Freight invoiced as bulk cargo, while the goods travel in jumbo bags
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Bulk cargo down the river to the coast of Bayvarra, per tonne.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `River freight, bulk`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FB-BULK`
- Why: The carrier bills the voyage as bulk freight. The cargo it carried is 120 jumbo bags, not bulk: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:BulkCargoIndicator` = `false`, and the waybill this invoice refers to declares packages of type JB, `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`. Bulk and bagged cargo are different services (handling, rates), so the invoice describes a different service from the one in the transport documents. The Urvanian description and name repeat the same meaning.
- Condition: The invoice line describes the service actually performed (river freight of packed goods in jumbo bags, per tonne), consistent with 03 and 06, in both languages.
- Options: (a) preferred: rename the service to bagged or general cargo (e.g. "River freight, jumbo bags, per tonne") with a matching seller's item ID, because the transport documents are consistent among themselves; (b) if the carrier's tariff really has only a "bulk" rate, say so in the description ("bulk rate applied to bagged cargo").
- Needs decision: no

### plastics/07#F2 · Low · Reference to the waybill carries no document type
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`
- Why: `AdditionalDocumentReference` with an ID only does not say that it is the consignment note (06) on which the freight is based; the plan's payment terms say "30 days net from the consignment note", so it is the document that matters for this invoice. The referenced transport contract `RR-FB-FW-2026` (03, 04) is not referenced either.
- Condition: The waybill reference says what it refers to (document type code or description).
- Options: (a) preferred: add `DocumentTypeCode` `Waybill` (the world's UBL document type list, as used in 06 and 11); (b) a `DocumentDescription`.
- Needs decision: no

## Checked and consistent
- Freight arithmetic: 120 TNE × 1495 XUF per 1 TNE = 179400 XUF, equal to the waybill's freight charge (06) and to the line and tax-exclusive totals.
- Invoiced quantity 120 t equals the waybill's chargeable weight 120000 kg (06).
- Issue on 2026-04-22 14:20, after the planned discharge of 2026-04-22 08:00 (04, 06).
- Parties: carrier as supplier and Rinova as customer fit CPT and the bill-to party of 03/04.
