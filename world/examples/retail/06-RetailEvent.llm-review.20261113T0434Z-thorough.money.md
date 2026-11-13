# LLM review: 06-RetailEvent.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/06-RetailEvent.xml`, Git blob `d0b57c7c84cd16cde8dca7daf766830c3f61056c` (committed)
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

### retail/06#F1 · Medium · The promotional line item carries the reduction, not the promotional price
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cbc:Amount` = `74.90`
- Why: A `PromotionalEventLineItem` is "a line item for a promotional event involving a specific product at a specific location; it describes the expected impacts associated with the event and specifies the promotional price of the item", so its `Amount` is the promotional price. The store's regular price of the bench is 749.00 and the promotion takes 10 % off (`/RetailEvent/cbc:Description` = `Ten per cent off garden furniture for two weeks.`; `21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:BaseAmount` = `749.00`), so the promotional price is 674.10 (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `674.1`). 74.90 is the amount of the reduction (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:Amount` = `74.90`). Read as a price, 74.90 would also be far below the distributor's trade price of 520 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`).
- Condition: The promotional event line item's amount is the bench's promotional price, 674.10, consistent with the till price in the purchase receipt.
- Options: (a) preferred: 674.10, because the definition names the promotional price and the receipt already shows it; (b) if the reduction is what the event should communicate, state it in the event tactic or description and still give the price here.
- Needs decision: no

### retail/06#F2 · Low · Planned sales value is at the regular price, not the promotional price
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:RetailPlannedImpact/cbc:Amount` = `17976.00`
- Why: `RetailPlannedImpact/Amount` is the "estimated monetary value of the planned event as an impact", here of sales (forecast purpose SALES) over the two promotion weeks. 17976.00 = 24 × 749.00, i.e. 24 benches at the regular price; at the promotional price of 674.10 that the event is about, 24 benches are 16178.40. It cannot be reconciled with the line item's own amount either (17976.00 / 74.90 = 240 benches, against shelf space for 12, `/RetailEvent/cac:EventComment/cbc:Comment` = `Shelf space for 12 benches at the entrance.`, and a forecast of 40 benches for six weeks, `05-Forecast.xml:/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `40`). The quantity 24 itself is consistent with the order (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `24`), so only the valuation is off.
- Condition: The planned sales value equals the planned quantity times the promotional price (e.g. 24 × 674.10 = 16178.40), or the event states that it values at regular prices.
- Options: (a) preferred: value at the promotional price, because the impact is of the promotion; (b) keep 17976.00 and add a quantity-based impact or a note that the value is at regular prices.
- Needs decision: no

## Checked and consistent
- The promotion period 2026-05-11 to 2026-05-24 contains the consumer's purchase at the promotional price (`21-PurchaseReceipt.xml:/PurchaseReceipt/cbc:PurchaseDate` = `2026-05-15`), and the 10 % in the description matches the receipt's factor (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.1`).

## Considered and refuted
- The distributor's promotion support of 5 % in the order and invoice (`08-Order.xml:/Order/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.05`) is not mentioned in the retail event: suspected that the order's allowance has no basis — refuted because the retail event describes the consumer-facing promotion, and the note says the event was agreed with the distributor's sales team; the supplier's contribution belongs to the trade documents, which state it consistently.
