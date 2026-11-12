# LLM review: 09-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/09-PurchaseReceipt.xml`, Git blob `8c680565e9cab9b2d106e8f8d8cf3831c5abddd0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/09#F1 · Low · Three shirts without the "5.00 off the pair" given the day before
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:Quantity` = `3`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:LineExtensionAmount` = `35.940`
- XPath: `08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Two shirts: 5.00 off the pair`
- Why: on 2026-05-22 the same till (`C1`) gave Robin Ashdale 5.00 off for a pair of the same shirt (`BM-778120`). On 2026-05-23 Velumi Trading buys three of them at the full price (3 × 11.98 XLC = 3 × 29.95 XBL); no allowance is applied, although three shirts contain a pair. Either the promotion ended on 22 May, which neither receipt says, or one discount of 5.00 XBL (2.00 XLC at 0.4) is missing here.
- Condition: either the line carries the pair discount like `08-PurchaseReceipt.xml`, with the line, tax and totals recalculated, or the two receipts make clear why it applied on 22 May and not on 23 May (e.g. the promotion's period stated in the allowance reason of 08).
- Options: (a, preferred) state the promotion's validity in the reason text of 08 (e.g. "weekend offer, 22 May") so 09 at full price is explained, which keeps the arithmetic of 09; (b) add the discount to 09 and recalculate.
- Needs decision: yes (whether the promotion applies is part of the story)

## Checked and consistent
- Pricing in coral (dynamic currency conversion, `/PurchaseReceipt/cbc:Note` = `Paid in coral: the card's currency was chosen at the till.`): `/PurchaseReceipt/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4` from XBL to XLC; 29.95 × 0.4 = 11.98 = `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `11.98`; 3 × 11.98 = 35.94 = `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `35.940` (XLC has 3 decimals per the world's currency list).
- Tax in document currency: 6.5 % × 35.940 = 2.3361 → `/PurchaseReceipt/cac:TaxTotal[1]/cbc:TaxAmount` = `2.336`; 35.940 + 2.336 = `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `38.276` = `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.276` = `/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `38.276`.
- Tax in tax currency: `/PurchaseReceipt/cac:TaxExchangeRate/cbc:CalculationRate` = `2.5` from XLC to XBL, the reciprocal of 0.4; 35.940 × 2.5 = 89.85 = `/PurchaseReceipt/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `89.85` (= 3 × 29.95); 6.5 % × 89.85 = 5.84 = `/PurchaseReceipt/cac:TaxTotal[2]/cbc:TaxAmount` = `5.84`, which is also 2.336 × 2.5. XBL is the currency of Brightmarket's STT registration.
- Card: credit card on the Coralcard network, issuer on Lisavu, holder Velumi Trading = the customer; PAN masked.

## Considered and refuted
- `/PurchaseReceipt/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL` while `/PurchaseReceipt/cac:TaxExchangeRate/cbc:SourceCurrencyCode` = `XLC`: suspected inconsistent directions (UBL: the source is "the currency from which the exchange is being made") — refuted because the two conversions really run in opposite directions: the till converts the lume shelf price into coral, and the coral amounts are converted into lume for the tax; each rate is stated in the direction of its conversion, and the rates are reciprocal.
- Two `TaxTotal` for the same scheme STT: suspected a double statement of the tax — refuted because the second one is the same tax in the tax currency, linked by `TaxExchangeRate`; the receipt has no `TaxCurrencyCode` element in UBL 2.5, so the currencyID of the amounts carries it.
- Sales tax charged to a company from Lisavu: refuted because it is an over-the-counter retail sale in Lumeport, taxable where the goods are handed over; there is no export.
