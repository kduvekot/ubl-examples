# LLM review: 18-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/18-RemittanceAdvice.xml`, Git blob `47eb48a5adfeabc95404a79c9aab2a6843d04e46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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
- `InvoiceDocumentReference` `SCG-INV-26-0210` with issue date 2026-03-02 resolves to 16; the amount paid (6055.452 XLC) is the invoice's payable amount, and the RF reference `RF46SCGINV260210` is the one 16 asks the payer to quote (`check_ids.py`: valid).
- Paid on 2026-03-29, before the due date stated in 16 (2026-04-01; see the review of 16 for that date itself).
- Payee account `XL31BSEL0020004922263` is the gin's account given in 16.

## Considered and refuted
- `/RemittanceAdvice/cbc:PaymentOrderReference` = `LTM-PAY-26-0191`: the serial 0191 is the same as that of the gin's prepayment invoice `SCG-SBI-26-0191` (01), so an identifier reused across documents was suspected — refuted because the two are in different issuers' series (`LTM-PAY` of the mill, `SCG-SBI` of the gin), and `PaymentOrderReference` is "an internal reference to the order for payment from the payer to the payer's bank", which the mill numbers as it likes.
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SCG-INV-26-0210`: the same invoice cited twice in the line was checked as a possible reference of the wrong kind — refuted for this lens because both references point to the invoice 16 and the `DocumentTypeCode` says so; whether the second is needed is a question of presence (context lens).
