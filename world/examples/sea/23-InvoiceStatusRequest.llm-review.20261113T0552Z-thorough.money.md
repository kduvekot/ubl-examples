# LLM review: 23-InvoiceStatusRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/23-InvoiceStatusRequest.xml`, Git blob `d407b8e6ab91b5b8570b7d3b3be6645bd5336a72` (committed)
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

## Findings

### sea/23#F1 · Low · Sender's sales-tax registration and share capital in an invoice status request
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The request only asks whether invoice LD-INV-26-0147 has been approved; it carries no amounts or taxes. Lumeway's Bayvarran sales-tax registration and share capital have no use in it (section 4.8).
- Condition: The sender carries a tax scheme and capital data only if the request has a stated use for them.
- Options: (a) preferred: leave them out; (b) keep them with a stated reason.
- Needs decision: no

## Checked and consistent
- The referenced invoice `LD-INV-26-0147` exists (`22-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0147`) and was issued before the request date (2026-05-14 before `/InvoiceStatusRequest/cbc:RequestDate` = `2026-05-29`); the request falls before the invoice's due date.

## Considered and refuted
- `/InvoiceStatusRequest/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: suspected that after the assignment of the receivable the factor, not the seller, should ask — refuted because approval of the invoice by the buyer remains the seller's concern (it bears the risk of disputes under the factoring agreement), and the question is about approval, not about payment.
