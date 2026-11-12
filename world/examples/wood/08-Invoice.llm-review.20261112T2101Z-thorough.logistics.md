# LLM review: 08-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/08-Invoice.xml`, Git blob `cc18be7786d6372f4c7794e335c9b6d55250ba96` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### wood/08#F1 · Low · Invoice does not link to the despatch, delivery or export of the goods it bills
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0627`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `MS-DA-26-0633`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:ID` = `MS-EX-26-0630`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- Why: the invoice refers only to the order. It has no `DespatchDocumentReference` to the despatch advice issued 25 minutes earlier (`06-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `08:31:00`, the invoice at `/Invoice/cbc:IssueTime` = `08:56:00`), no `Delivery` with a delivery date or place, and no reference to the export declaration, although the zero rate is justified by export. A reader of the invoice cannot tell which despatch it bills or when the goods were delivered (a DAP delivery in Urvania), and the flow has no other document that says so.
- Condition: the invoice identifies the despatch it bills and states the delivery (date and place), or the export evidence, so that it can be matched to the logistics documents of the flow.
- Options: (a) preferred: add `DespatchDocumentReference` to `MS-DA-26-0633` and `Delivery` with the delivery place and the (actual or expected) delivery date; (b) add an `AdditionalDocumentReference` to the export declaration as export evidence (the tax side is for the money part).
- Needs decision: no

## Checked and consistent
- Reference `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0627` resolves to `03-Order.xml`; quantity `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `4800` equals the ordered and the despatched quantity (`06-DespatchAdvice.xml`).
- The invoice is referenced as `MS-INV-26-0635` (issue date 2026-02-26) by `09-RemittanceAdvice.xml`; both references resolve and the issue date agrees.
- Item data (seller's ID `MS-SL-1800`, HS `440799`, origin `XB`, certificate `XB-FOR-2025-0118`) agree with the despatch advice and the customs declarations.
