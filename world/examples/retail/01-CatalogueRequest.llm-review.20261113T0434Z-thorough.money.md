# LLM review: 01-CatalogueRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/01-CatalogueRequest.xml`, Git blob `571e96113517945d8ea407ef7718908cdaf87ade` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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
- `/CatalogueRequest/cac:CatalogueRequestLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `24`: the pallet price is requested for at least 24 benches; the catalogue answers with a price band of 4 to 192 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `4`), and the order then buys exactly 24 (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `24`).
- `/CatalogueRequest/cbc:PricingUpdateRequestIndicator` = `true` fits a request for prices on a pallet basis.
- The trading terms asked for (DDP to the store) are the ones the catalogue, the order and the invoice apply (`08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DDP`).

## Considered and refuted
- `/CatalogueRequest/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store.`: suspected that "duty paid" makes no sense for a delivery within Bayvarra (both parties in XB) — refuted because Incoterms DDP may be used for domestic trade, and here it also covers the import into Bayvarra of benches made in Urvania (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XU`), which the distributor bears.
