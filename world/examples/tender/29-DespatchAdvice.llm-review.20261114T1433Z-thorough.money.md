# LLM review: 29-DespatchAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/29-DespatchAdvice.xml`, Git blob `79edc7989dc6f0f5e4d8a3b040fb4fdfaa8e1ecc` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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
- The despatch advice carries no amount, price, tax, charge, declared value or payment element; the money lens applies only to its accounting references and to the quantities that the invoice and the credit note of the flow bill against.
- Quantities against the money documents: 40 benches despatched = 40 ordered (26-Order.xml) = 40 invoiced (`32-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `40`); outstanding 200 = 240 − 40, the figure the invoice's annotation repeats ("First release: 40 benches; 200 remain.").
- `AccountingCostCode` PWD-PARKS-26 / "Parks renewal programme 2026" is the same buyer's code as in the order and the invoice.

## Considered and refuted
- `/DespatchAdvice/cbc:AccountingCostCode`: the buyer's accounting code in a document issued by the seller's logistics provider, and repeated on the line (`/DespatchAdvice/cac:DespatchLine/cbc:AccountingCostCode`) — refuted because the element is "the accounting cost centre, applied to the Despatch Advice", the code was given by the buyer in the order (`26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`) and lets the buyer book the receipt; the repetition on the single line says the same thing twice but contradicts nothing.

## Outside this review
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderQuantity` = `4`: four of the forty ground anchor sets are on back order, while 32-Invoice.xml bills all forty benches at the full price "supplied with four ground anchors". The consequence for the amount billed is a finding of the invoice's review (32#F9 of this part); the despatch advice itself states the shortage correctly.
