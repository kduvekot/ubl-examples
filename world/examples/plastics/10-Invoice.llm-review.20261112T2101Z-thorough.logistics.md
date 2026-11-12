# LLM review: 10-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/10-Invoice.xml`, Git blob `1e3f9e5ae5dac5d74b0e7b9130b9a13721e9ec83` (committed)
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

## Checked and consistent
- References: `OrderReference` `RP-PO-26-0882` resolves to 01, order line 1 is the order's only line; `DespatchDocumentReference` `RR-DA-26-0892` resolves to the despatch advice 08, issued the day before (2026-04-19 17:57).
- Quantity 120 TNE equals the order line (01) and the despatched quantity (08); 120 × 83200 XUF = 9984000 XUF.
- The note "the price includes the barge to the river quay" agrees with the CPT place in the order (`01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`) and the unloading place in 04 and 06.
- The invoice 10 is referenced by the remittance advice 11.

## Considered and refuted
- `/Invoice/cbc:IssueDate` = `2026-04-20`: suspected an invoice issued before the goods arrive (planned discharge 2026-04-22, 04/06) — refuted because under CPT the seller has delivered when the goods are handed to the carrier (2026-04-19, 06), so invoicing on 2026-04-20 is after delivery.
- `/Invoice/cac:DespatchDocumentReference/cbc:ID` = `RR-DA-26-0892`: suspected that the transport document (waybill 06) should be referenced — refuted because the despatch advice is the seller's own record of the despatch and is the document this element is meant for; the waybill belongs to the carrier's contract.
