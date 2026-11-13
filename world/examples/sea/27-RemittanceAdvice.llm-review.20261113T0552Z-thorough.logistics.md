# LLM review: 27-RemittanceAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/27-RemittanceAdvice.xml`, Git blob `a83f4a9e20f100a4540611eef91ece79f8f5dfa3` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

## Checked and consistent
- References: invoice LD-INV-26-0147 with issue date 2026-05-14 (22-Invoice.xml) and credit note
  LD-CN-26-0152 with issue date 2026-06-15 (26-CreditNote.xml) exist and precede this advice
  (2026-06-25); 43778.00 − 64.00 = 43714.00 = TotalPaymentAmount.
- The payment reference RF20LDINV260147 and the factor's account are those of the invoice; the
  advice is issued before the due date 2026-06-28.

## Outside this review
- 24-InvoiceStatusResponse.xml (issued 2026-05-30) refers to this remittance advice as the
  remittance of its payment, but gives that payment as VT-PAY-26-0199 for 43778.00 XBL, while this
  advice gives `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123` and
  `/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`. The problem lies in 24 (it describes a payment that has
  not happened yet when it is issued); it is reported there.
