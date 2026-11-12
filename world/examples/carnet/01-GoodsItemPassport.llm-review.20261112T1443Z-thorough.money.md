# LLM review: 01-GoodsItemPassport.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/01-GoodsItemPassport.xml`, Git blob `b7c20e53167125d7f3ee0260e4bdca609da4e0b0` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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
- `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99800` for `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `2` benches: 49,900 XUF each, the same unit price as the seller's own price for item VI-B180 in `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900` and `road/15-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `49900` (checked over every `*.xml` that carries the item: the XUF values in rail, road and tender are all 49,900 XUF per bench). The currency of the holder's country (XU, ferra) is the right one for a carnet issued in Urvania.
- The carnet carries no fee, guarantee amount or tax amount, and none is needed: the ATA carnet itself is the guarantee, given by the guaranteeing associations named in `ExportingGuarantorParty` and `ImportingGuarantorParty`.
- XUF ("Ferra") is not an ISO 4217 code assigned to a real currency (own knowledge of the ISO 4217 list).

## Considered and refuted
- `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: suspected a mismatch with the definition the listing prints ("The number of shares in the capital stock of a corporation"), since the value is an amount in XUF — refuted because the element is an Amount type with a currencyID; the definition text is UBL's own wording, and a share capital of 250 million ferra (2.5 million lume at the rate `tender/32-Invoice.xml:/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`) is plausible for a listed manufacturer. Whether the holder's capital belongs in a carnet at all is a question for the parties lens, not this one.
