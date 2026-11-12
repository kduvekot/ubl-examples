# LLM review: 05-ExportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/05-ExportCustomsDeclaration.xml`, Git blob `485e09ca0ec698fc71593b783ad60898b71c45fd` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### wood/05#F1 · Medium · Customs value leaves out the pallet charge the buyer pays, and its delivery basis is not stated
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00`
- Why: DeclaredCustomsValueAmount is "the total declared value for customs purposes of the goods item". 34560.00 XBL is exactly the invoice line amount (`08-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `34560.00`); the 240.00 XBL charged to the buyer for heat-treated export pallets (`08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`) is left out. Under customs valuation practice (WTO Customs Valuation Agreement Art. 8.1(a)(iii), from my own knowledge), packing costs borne by the buyer are part of the value; the statistical export value is likewise the value of the goods with their packing at the border. At the same time the price is DAP Ferrano, so it includes transport beyond the Bayvarran border; an export value is usually stated on a border (FOB/FCA-type) basis. The declaration states neither the delivery terms nor how the value was derived, so its value cannot be reconciled with the invoice. The import declaration repeats the same base (`07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000` XUF = 34560.00 × 100).
- Condition: the declared value either includes the packing charge, or the example states a reason why it does not; and the basis of the value (the delivery terms or the border-value adjustment) can be read from the declaration.
- Options: (a) preferred: declare 34800.00 XBL (goods plus packing) and state the delivery terms (DAP) on the shipment's delivery, so the basis is visible; (b) declare a border value (34800.00 less the transport share beyond the border) and say so; (c) keep 34560.00 and explain in the story why packing is excluded. Which value the Bayvarran customs rules require is a story decision.
- Needs decision: yes

## Checked and consistent
- Currency XBL is the exporter's currency and the invoice currency; quantity 4800 EA and goods description agree with order and invoice.
- The declaration references the order `03-Order.xml` (AdditionalDocumentReference VI-PO-26-0627), whose line amount is the declared 34560.00.
