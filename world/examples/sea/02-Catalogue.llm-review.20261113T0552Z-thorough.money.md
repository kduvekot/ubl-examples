# LLM review: 02-Catalogue.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/02-Catalogue.xml`, Git blob `9ab014c2e27df7270bfea2ec3db014a3637bf54d` (committed)
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

## Findings

### sea/02#F1 · High · Sales territory Bayvarra contradicts the export exemption of the same price
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- Why: `ApplicableTerritoryAddress` is "the applicable sales territory" of the item location quantity, and `ApplicableTaxCategory` is "a tax category applicable to this item location quantity". In both lines the same item location quantity says the price applies to sales in Bayvarra and, at the same time, that the Upland State sales tax (STT) is not charged because of "Export outside Bayvarra" (category G, 0 %). A sale within the territory Bayvarra is not an export; an export price needs a sales territory outside Bayvarra. The catalogue is sent to Velumi Trading on Lisavu, and the flow treats the sale as an export everywhere (`05-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`, the invoice `22-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`), so it is the territory that does not fit.
- Condition: in each `RequiredItemLocationQuantity`, the sales territory and the tax category agree: either the territory lies outside Bayvarra (Lisavu) and the tax category is the export exemption, or the territory is Bayvarra and the tax category is the one charged on domestic sales.
- Options: (a) preferred: territory `XL` (Lisavu), the place the catalogue's receiver sells into, keeping the export exemption that the rest of the flow uses; (b) two item location quantities, one for Bayvarra with the domestic tax and one for Lisavu with the export exemption, if the catalogue is meant to serve both.
- Needs decision: no

### sea/02#F2 · Medium · "Full container" discount is attached to the whole quantity range from 4 benches
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `4`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MaximumQuantity` = `192`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`
- Why: the allowance is "an allowance or charge associated with this item location quantity", and the item location quantity applies from `MinimumQuantity` 4 to `MaximumQuantity` 192 ("the minimum/maximum quantity that can be ordered to qualify for a specific price"). As encoded, every order of 4 to 192 benches qualifies for the 3 % allowance, so the condition named in the reason ("Full container") is never checked; a pallet of four is not a full container. The flow shows the ambiguity: Velumi orders 96 benches that travel in one 40-foot container (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason` = `Ocean freight, 40-foot container`), within the range 4–192, yet the order, the order response and the invoice all price the bench at 520 without the allowance (`05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`, `22-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `520`). Either the condition was met and 96 × 15.60 = 1,497.60 lume of allowance is missing downstream, or (more likely) the condition was not met and the catalogue should not offer it for this range.
- Condition: the quantity (or other condition) at which the "Full container" allowance applies can be read from the catalogue, and the order, order response and invoice of the flow are consistent with it.
- Options: (a) preferred: a separate `RequiredItemLocationQuantity` for full-container orders (its own `MinimumQuantity`, the allowance only there), the range 4–192 without the allowance; (b) keep one range but state the condition in the allowance (e.g. a reason that names the full-container quantity) and check that 96 benches do not reach it.
- Needs decision: no

### sea/02#F3 · Low · Price list status "Active" is not a status the element names
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- Why: `PriceList/StatusCode` is "a code signifying whether this price list is an original, copy, revision, or cancellation". "Active" (from the world list RecordStatusCode) describes whether the list is in force, which the price's `ValidityPeriod` already says (2026-05-04 to 2026-10-31); it is not one of the document states the definition names.
- Condition: the price list status is a value of the kind the definition names (original, copy, revision, cancellation), or the element is absent.
- Options: (a) preferred: a status meaning "original" (the first issue of LD-PL-2026); (b) drop the element, since validity is carried by the period.
- Needs decision: no

## Checked and consistent
- Line 1 allowance: `MultiplierFactorNumeric` 0.03 × `BaseAmount` 520.00 = 15.60 = `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:Amount` = `15.60`; the base amount equals the unit price with `BaseQuantity` 1.
- Alternative currency prices: 520 × 0.4 = 208 (`/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:AlternativeCurrencyPrice/cbc:PriceAmount` = `208`) and 64 × 0.4 = 25.6 (`/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:AlternativeCurrencyPrice/cbc:PriceAmount` = `25.6`); 0.4 XLC per XBL is the rate used throughout the flow (`22-Invoice.xml:/Invoice/cac:PaymentTerms[2]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`).
- Dependent price: 64 / 520 = 12.308 %, given as `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31` (rounded to two decimals; 520 × 12.31 % = 64.01).
- Prices 520 and 64 lume are the prices used in the order, the order response and the invoice of the flow; the tax category (G, 0 %, EXP, STT) is the one used in all of them.
- The price validity period (2026-05-04 to 2026-10-31) equals the catalogue's validity period; the order of 2026-05-07 lies within it.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`: suspected that the percentage does not reproduce the price 64 — refuted because 520 × 12.31 % = 64.012, which rounds to the stated 64; a percentage with two decimals cannot be more exact.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:AlternativeCurrencyPrice/cbc:PriceAmount` = `208`: suspected that a fixed alternative-currency price over a six-month validity ignores exchange-rate changes — refuted because the Coral price is a stated price in its own right ("the price expressed in an alternative currency"), not a conversion the catalogue promises to recalculate; the rate 0.4 is constant across the flow.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`: suspected a code from the wrong list (UN/EDIFACT 5189 is the allowance list, 7161 the charge list) — refuted because the entry is an allowance (`ChargeIndicator` false) and 95 "Discount" is the 5189 code for it.
