# LLM review: 03-CataloguePricingUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/03-CataloguePricingUpdate.xml`, Git blob `fa746f7555ca2bc6ffeef41cf02e3ca5ac1ffe9d` (committed)
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

### retail/03#F1 · High · The side frame's new price is addressed to the bench's catalogue line
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cbc:ID` = `1`
- XPath: `/CataloguePricingUpdate/cbc:Name` = `Price change of the side frame`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- Why: The line's `ID` is "an identifier for the catalogue line to be updated", and the line carries no `Item`, so the line ID alone says which item gets the new price. In the updated catalogue, line 1 is the park bench at 520 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`; `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`), and the side frame is line 2 at 64 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Name` = `Bench side frame casting`; `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `64`). As encoded, the update sets the bench's price to 58, an 89 % cut, while its name and description announce a change of the side frame (64 → 58, about −9 %).
- Condition: The pricing update line identifies the catalogue line of the side frame (line 2 of LD-CAT-26-0218), or carries the side frame's item identification, so that the price of 58 lands on the side frame.
- Options: (a) preferred: line ID 2, matching the catalogue line, because the line ID is what the receiver uses to synchronise; (b) additionally add `Item` with the seller's item ID LD-10443, which makes the line self-explaining.
- Needs decision: no

### retail/03#F2 · Low · The side frame's dependent price percentage no longer matches its new price
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- Why: In the catalogue the side frame's price is also expressed as a percentage of the bench's (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`, i.e. 64 / 520). With the new price of 58 and the bench unchanged at 520, the relation is 58 / 520 = 11.15 %. The update changes the absolute price but leaves the dependent price reference as it was, so after the update the catalogue states two different prices for the side frame (58, and 12.31 % of 520 = 64.01).
- Condition: After the update, the side frame's absolute price and its dependent price reference agree (11.15 % of 520 = 58), or the dependent price reference no longer applies.
- Options: (a) preferred: carry `DependentPriceReference` with 11.15 % in the update's item location quantity, because the receiver otherwise keeps the old percentage; (b) remove the dependent price reference from the catalogue, if the side frame's price is not meant to follow the bench's.
- Needs decision: no

### retail/03#F3 · Low · The whole price list LD-PL-2026 is declared replaced, though the bench keeps its price on it
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cac:PreviousPriceList/cbc:ID` = `LD-PL-2026`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cac:PreviousPriceList/cbc:StatusCode` = `REPLACED`
- Why: `StatusCode` of a price list signifies "whether this price list is an original, copy, revision, or cancellation". LD-PL-2026 carries both catalogue prices (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`), and only one price changes. Declaring the list replaced by LD-PL-2026-2 leaves the price of the item not mentioned in the update on a list that is no longer active, unless LD-PL-2026-2 also contains it, which the update does not say.
- Condition: It is clear which price list is active for each catalogue item after the update.
- Options: (a) preferred: state in the price list that LD-PL-2026-2 is a revision covering the whole range (e.g. a note), so the replacement of LD-PL-2026 is complete; (b) keep LD-PL-2026 active and give the side frame's new price its own list without declaring LD-PL-2026 replaced.
- Needs decision: no

### retail/03#F4 · Low · Trading terms carry only "Unchanged."
- XPath: `/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`
- Why: `TradingTerms/Information` is "text describing the terms of a trade agreement". "Unchanged." describes no term; it only says that the catalogue's terms (`02-Catalogue.xml:/Catalogue/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store; 30 days net.`) still apply, which an update without trading terms already implies. Under the no-filler rule the aggregate has no business content here. The same value occurs in 2 examples (`grep -l --include='*.xml' 'Unchanged.' world/examples/*/*.xml`: 03-CataloguePricingUpdate and 04-CatalogueItemSpecificationUpdate).
- Condition: The update either has no `TradingTerms` or carries the terms that apply to the updated prices.
- Options: (a) preferred: remove `TradingTerms`, because the terms did not change; (b) repeat the actual terms with the reference LD-GTC-2026, if the update is meant to be read alone.
- Needs decision: no

## Checked and consistent
- New price 58 per 1 EA, valid 2026-05-20 to 2026-07-19, inside the catalogue's validity (to 2026-07-19); the price list's validity matches the update's.
- No order or invoice of the flow falls after 2026-05-20 for a Lumeway item, so no later document had to use the new price (the order and invoice are of 2026-04-24 and 2026-04-30).
