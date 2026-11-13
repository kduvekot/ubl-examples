# LLM review: 04-CatalogueItemSpecificationUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/04-CatalogueItemSpecificationUpdate.xml`, Git blob `bc08c5d7cc1e9ec6f62cb02c0b6ddfcd217352bc` (committed)
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

## Findings

### retail/04#F1 · Low · Trading terms carry only "Unchanged."
- XPath: `/CatalogueItemSpecificationUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`
- Why: `TradingTerms/Information` is "text describing the terms of a trade agreement". "Unchanged." describes no term; it says only that the catalogue's terms (`02-Catalogue.xml:/Catalogue/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store; 30 days net.`) still apply, which an item specification update without trading terms already implies, and an update of the slat wood has nothing to do with trading terms. Under the no-filler rule the aggregate has no business content here. The same value occurs in 03-CataloguePricingUpdate.xml (counted with `grep -rl --include='*.xml' 'Unchanged\.' world/examples/`: 2 files).
- Condition: The update either has no `TradingTerms` or carries terms that apply to it.
- Options: (a) preferred: remove `TradingTerms`, because the terms did not change; (b) repeat the actual terms with the reference LD-GTC-2026, if the update is meant to be read alone.
- Needs decision: no

## Checked and consistent
- The update carries no price, allowance or tax data, as fits a change of item specifications; the item's price stays the catalogue's (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`).
- Corporate stock of both parties (XBL 2 500 000 for Lumeway, XBL 12 000 000 for Brightmarket) is the same in every retail example (counted over `*.xml` with grep on `CorporateStockAmount`).
