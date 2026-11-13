# LLM review: 08-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/08-Order.xml`, Git blob `01257b4f8b6e604e5ea78070a814e95bca35ab3d` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/08#F1 · Low · Sub-line prices without the quantity they apply to
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cac:Price/cbc:PriceAmount` = `380`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[2]/cac:Price/cbc:PriceAmount` = `115`
- Why: `BaseQuantity` is "The quantity at which this price applies". The main line states it (`/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`, unit SET), the two sub-line prices do not, so "per one piece" is only implied by absence (IND6). The arithmetic works with a base of 1 EA (20 × 380 = 7600.00; 40 × 115 = 4600.00). Across the examples, 12 of the 117 `Price` elements with a `PriceAmount` have no `BaseQuantity`, in 6 files (counted with a script over `world/examples/*/*.xml`).
- Condition: Every `Price` in the order states the quantity it applies to, or the flow's convention that a missing base quantity means one unit of the line's unit is recorded as a deliberate decision.
- Options: (preferred) add `BaseQuantity` 1 EA to both sub-line prices, matching the main line; or record the convention.
- Needs decision: no

## Checked and consistent
- Main line: 20 sets × 610 = 12200.00 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `12200.00` = `/Order/cac:OrderLine/cac:LineItem/cac:ItemPriceExtension/cbc:Amount` = `12200.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `12200.00`.
- Sub-lines: 7600.00 + 4600.00 = 12200.00; per set 380 + 2 × 115 = 610, matching "bench and two chairs per set".
- Tax: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00` equals the line total; exempt category E with `RESALE` fits a department store buying its own-label line for resale; 0.00 at document and line level (`/Order/cac:OrderLine/cac:LineItem/cac:TaxTotal/cbc:TaxAmount` = `0.00`). The same treatment is used in 09-Invoice and 13-CreditNote.
- Price as quoted: 610 per set as in `02-Quotation.xml:/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610`; the order lies within the quotation's validity (to 2026-05-05).
- Currency `XBL` throughout.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`: suspected a filler that only repeats the line price. Refuted because the line note "Price as quoted." makes the pricing reference the quoted price the order relies on; a price reference equal to the actual price is a legitimate statement that no change was made.
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID` = `STT`: suspected that the state whose sales tax exemption applies (seller in Upland State, buyer and delivery in Coastal State) is not stated. Refuted for this lens because no tax is due under either state, the parties' tax schemes name their jurisdictions, and no tax category in the examples carries a jurisdiction (checked over every STT category in `world/examples/*/*.xml`).
- `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cbc:LineExtensionAmount` = `7600.00`: suspected double counting of the sub-lines with the main line. Refuted because the totals use only the main line (12200.00); the sub-lines break it down and sum to it.
