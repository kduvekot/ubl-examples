# LLM review: 09-RemittanceAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/09-RemittanceAdvice.xml`, Git blob `41a5df331d4ec5f08a936109c93263e9b39bd319` (committed)
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

### wood/09#F1 · Low · The same invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `MS-INV-26-0635`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `MS-INV-26-0635`
- Why: BillingReference/InvoiceDocumentReference is "A reference to an invoice", the dedicated element for what the line pays; RemittanceAdviceLine/DocumentReference is "A reference to a document associated with this remittance advice line". Both point to the same invoice with the same issue date, the second adding only `DocumentTypeCode` `Invoice`. The second reference adds no document and makes a reader look for a second associated document that does not exist.
- Condition: the line refers to the invoice once, in the element meant for it; any `DocumentReference` on the line refers to a different associated document.
- Options: (a) preferred: remove the line's `DocumentReference`; (b) keep it only if it is replaced by a reference to another document the payment relates to (none exists in the flow).
- Needs decision: no

## Checked and consistent
- Both references resolve to `08-Invoice.xml` (an invoice, `08-Invoice.xml:/Invoice/cbc:ID` = `MS-INV-26-0635`, issued 2026-02-26, the date quoted here).
- Creditor reference `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF83MSINV260635` is the RF reference of the invoice's `08-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF83MSINV260635`; check_ids.py confirms its check digits.
- Dates: issued 2026-03-26, before the invoice's due date 2026-03-28.

## Considered and refuted
- `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0625`: suspected confusion with the request for quotation `VI-DOC-26-0625` (same serial 0625) — refuted because the prefixes name different series of the buyer (payment orders, documents), and nothing in the flow uses the payment order number as a document reference.
