# LLM review: 02-Catalogue.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/02-Catalogue.xml`, Git blob `1c92d827b4d756ddbac6f7506b2c222c22480912` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### retail/02#F1 · Low · "Full container" discount offered in a price band that a pallet already meets
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `4`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MaximumQuantity` = `192`
- Why: The allowance sits in the item location quantity whose conditions are "the minimum quantity that can be ordered to qualify for a specific price" (4 EA) and the maximum (192 EA), so by its placement the 3 % discount applies to every order from one pallet of four upwards; its reason text, however, makes it conditional on a full container, which nothing in the catalogue quantifies. The flow has no container at all: the distributor delivers DDP to the store by a full truck load (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`), and the order of 24 benches, inside the 4–192 band, neither claims nor receives the 3 % (`08-Order.xml:/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Promotion support`; `18-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.05`). The arithmetic itself holds (520.00 × 0.03 = 15.60). The condition of the allowance cannot be checked or met in this world as written.
- Condition: The discount's condition is one the catalogue states and the flow can meet or not meet visibly: either it has its own item location quantity whose quantities express the condition (e.g. the quantity of a full truck load), with a reason that matches the way the distributor delivers, or it is removed; and the order and invoice are consistent with whether the 24 benches qualify.
- Options: (a) preferred: give the discount its own `RequiredItemLocationQuantity` with a `MinimumQuantity` for a full load and a reason that matches road delivery ("full truck load"), and leave the 4–192 band without it, because then the order of 24 benches visibly does or does not qualify; (b) remove the allowance from the catalogue.
- Needs decision: no

### retail/02#F2 · Low · Dependent price restricted to Coastal State while both prices apply in all of Bayvarra
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cac:LocationAddress/cbc:CountrySubentity` = `Coastal State`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: The dependent price reference gives "the price of the item as a percentage of the price of some other item", with `LocationAddress` "the reference location for this dependent price reference". The percentage itself is right (64 / 520 = 12.31 %). But both the side frame's price and the bench's price it depends on apply to the whole of Bayvarra, and the catalogue has no state-specific price; limiting the reference to Coastal State says that the 12.31 % relation holds only there, which nothing else in the catalogue supports (Coastal State is where the buyer's store is, not a price territory).
- Condition: The reference location of the dependent price is the territory where both prices apply (Bayvarra), or there is a price for which Coastal State is the territory.
- Options: (a) preferred: drop `LocationAddress` or set it to the country only, because the catalogue has one territory; (b) introduce state-specific prices, which changes the catalogue's story.
- Needs decision: no

### retail/02#F3 · Low · Item comparison repeats the unit price
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:PriceAmount` = `520`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:Quantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:BaseQuantity` = `1`
- Why: `ItemComparison` is "a combination of price and quantity used to provide price comparisons based on different sizes of order". The only comparison given is 520 for one bench, which is exactly the line's price per one bench; it compares nothing (there is no second order size, and the pallet of four costs 4 × 520 at the same rate). Under the no-filler rule a value needs a business reason in the document.
- Condition: Either the line has no `ItemComparison`, or its comparisons show prices for different order sizes that differ from (or explain) the line's price.
- Options: (a) preferred: remove `ItemComparison`, because the catalogue has one price per bench for the whole 4–192 band; (b) use it for a real comparison, e.g. the price per bench with and without the discount of F1, if F1 is resolved with its own quantity band.
- Needs decision: no

## Checked and consistent
- Line 1 allowance: 520.00 × 0.03 = 15.60 (`/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:Amount` = `15.60`), base 520.00 equals the unit price.
- Line 2 dependent price: 64 / 520 = 0.12308, i.e. 12.31 % (`/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`), referring to line 1.
- Prices: 520 per bench and 64 per side frame, price list LD-PL-2026, valid 2026-04-20 to 2026-07-19 like the catalogue; the order and invoice use 520 (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`; `18-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `520`); the store's inventory is valued at it (`07-InventoryReport.xml:/InventoryReport/cac:InventoryReportLine/cbc:InventoryValueAmount` = `1560.00`, 3 × 520).
- Tax: category E, 0 %, exemption RESALE under the state sales tax STT on both lines, the same as the order, invoice and credit note (`18-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`); the exemption reason is the transaction (sale for resale), not a party status.
- Trading terms "30 days net" match the order's and invoice's payment terms (`08-Order.xml:/Order/cac:PaymentTerms/cbc:Note` = `30 days net, as agreed with the distributor.`; `18-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-30`, 30 days after the issue date).
- The price applies to deliveries from 2026-04-27; the order's delivery on 2026-04-30 qualifies.
- Currency XBL is not an ISO 4217 code (own knowledge of the list).

## Considered and refuted
- `/Catalogue/cbc:Note` = `Prices for trade customers, before sales tax.`: suspected a contradiction with the exempt tax category (no sales tax is due on a sale for resale) — refuted because the note states that the prices exclude sales tax, which is true whatever the category; the exemption is then stated per line.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`: suspected the wrong list for a discount — refuted, 95 "Discount" in UN/EDIFACT 5189 is the allowance reason list.

## Outside this review
- `03-CataloguePricingUpdate.xml` changes the side frame's price to 58 without updating the dependent price percentage of line 2 (58 / 520 = 11.15 %); recorded as a finding of that example's review.
