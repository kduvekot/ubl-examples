# LLM review: 21-ReceiptAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/21-ReceiptAdvice.xml`, Git blob `11d4ca627fbbda4c36b71ae5b97e59794bcbb9ae` (committed)
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

### sea/21#F1 · Low · Despatch supplier's sales-tax registration and share capital in the warehouse's receipt advice
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The receipt advice from Nalevi Warehousing reports what was received and rejected; it carries no amounts or taxes. Lumeway's Bayvarran state sales-tax registration and share capital have no use in it (section 4.8).
- Condition: The despatch supplier carries a tax scheme and capital data only if the receipt advice has a stated use for them.
- Options: (a) preferred: leave them out; (b) keep them with a stated reason.
- Needs decision: no

## Checked and consistent
- The rejected quantity (one side frame, `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`) is what the credit note credits: one frame at 64 XBL (`26-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `1`, `26-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:LineExtensionAmount` = `64.00`), at the invoiced price of the frames (`22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `64`).
- The credit note's delivery date matches the receipt (`26-CreditNote.xml:/CreditNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-21`).
