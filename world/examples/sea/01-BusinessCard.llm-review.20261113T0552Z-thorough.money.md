# LLM review: 01-BusinessCard.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/01-BusinessCard.xml`, Git blob `3b6f96c9fc61de8c4dad42aecf09e84a3a8c83dc` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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
- `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount` = `1040000.00` against `/BusinessCard/cac:BusinessCapability/cbc:ValueQuantity` = `2000`: 1,040,000.00 / 2,000 = 520.00 lume per bench, which is the trade price of the same bench in `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`, and the currency (XBL, lume) is Lumeway's tax currency in `/BusinessCard/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XBL`.
- `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000` is the same as in the other examples of the flow that describe Lumeway (e.g. `22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`).

## Considered and refuted
- `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`: suspected that an amount does not fit a definition that speaks of "the number of shares in the capital stock" — refuted because the element is of type Amount in UBL 2.5 (it carries `currencyID`), so the definition text is UBL's own inconsistency; a share capital of 2,500,000 lume is the only reading the data type allows.
- `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount` = `1040000.00`: suspected that a stock is valued at the sales price rather than at cost — refuted because the element is "a monetary amount as a measure of this capability", not a balance-sheet value; the trade value of the stock is a legitimate measure of a warehousing capability offered to a customer.
