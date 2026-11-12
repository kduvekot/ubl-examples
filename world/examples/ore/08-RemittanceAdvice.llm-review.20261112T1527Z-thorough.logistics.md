# LLM review: 08-RemittanceAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/08-RemittanceAdvice.xml`, Git blob `ba4a236a16cc3b9d330f7fd945ee82d84e44ac69` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### ore/08#F1 · Low · The same invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SM-INV-26-0312`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SM-INV-26-0312`
- Why: `BillingReference/InvoiceDocumentReference` is "a reference to an invoice", the dedicated
  element; `DocumentReference` is "a reference to a document associated with this remittance advice
  line". Both point to the same invoice with the same issue date, so the second reference adds
  nothing (it only adds the type code `Invoice`). The same double reference is in 9 remittance advices
  (lxml over `*/*RemittanceAdvice*.xml`: same ID in both on one line).
- Condition: each referenced document appears once on the line, in the element meant for it.
- Options: (a, preferred) keep only the billing reference; (b) keep the generic reference only for a
  document that is not an invoice.
- Needs decision: no

## Checked and consistent
- `SM-INV-26-0312` with issue date 2026-03-11 resolves to 07-Invoice.xml (issued 2026-03-11); the
  RF reference `RF73SMINV260312` (check digits valid) is the invoice's payment ID.
- Issued 2026-04-09 12:10, after the invoice and before its due date 2026-04-10.

## Outside this review
- No remittance advice in the flow covers the freight invoice 06-Invoice.xml (FRC-INV-26-0311); whether
  one is missing is a question of the flow's story.
