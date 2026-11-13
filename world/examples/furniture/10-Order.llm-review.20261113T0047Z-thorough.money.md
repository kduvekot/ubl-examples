# LLM review: 10-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/10-Order.xml`, Git blob `4c325d25cd05fed989cbd0f6f69ef7970de5cb48` (committed)
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

### furniture/10#F1 · High · Taxable amount ignores the 3 % repeat-order allowance
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `11834.00`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `11834.00`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:Amount` = `366.00`
- Why: `TaxableAmount` is "The net amount to which the tax percent (rate) is applied to calculate the tax amount". The only line is 20 × 610 = 12200.00 less the line allowance of 3 % (0.03 × 12200.00 = 366.00), i.e. 11834.00, which is the line and document line extension amount. The tax subtotal still uses the gross 12200.00, which is the figure of the earlier order 08-Order without the allowance. The tax amount is 0.00 either way (exempt), but the amounts contradict each other.
- Condition: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` equals the sum of the line extension amounts it covers (11834.00).
- Options: (preferred) set the taxable amount to 11834.00; no other option keeps the arithmetic.
- Needs decision: no

### furniture/10#F2 · Low · "Price as quoted" with a repeat-order discount the quotation does not contain
- XPath: `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Repeat order`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`
- Why: The order claims a 3 % repeat-order discount, but the quotation it refers to (02-Quotation, and `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`) quotes 610 per set with no allowance and no volume or repeat terms (`02-Quotation.xml:/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount` = `12200.00`). The line note says the price is as quoted, which is true of the unit price, but the line amount is not as quoted. Nothing in the flow shows where the discount was agreed (the allowance's reason code 95 "Discount" names no agreement).
- Condition: The repeat-order discount can be traced to an agreement in the flow (the quotation, the contract, or a statement in this order), or the order line amount equals the quoted amount.
- Options: (preferred) let the quotation (or a referenced contract) offer the repeat-order discount, so the order applies agreed terms; or state in the order that the discount was agreed separately; or drop the discount.
- Needs decision: yes

### furniture/10#F3 · Low · Sub-line prices without base quantity
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cac:Price/cbc:PriceAmount` = `380`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[2]/cac:Price/cbc:PriceAmount` = `115`
- Why: `BaseQuantity` is "The quantity at which this price applies". The main line states it (1 SET), the sub-lines do not, so "per piece" is implied by absence (IND6). Same as in 08-Order and 09-Invoice; 12 of 117 `Price` elements with a `PriceAmount` in `world/examples/*/*.xml` lack it (script count).
- Condition: Every `Price` in the order states the quantity it applies to, or the convention is recorded as a decision.
- Options: (preferred) add `BaseQuantity` 1 EA to both sub-line prices.
- Needs decision: no

## Checked and consistent
- Allowance: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:BaseAmount` = `12200.00` × 0.03 = 366.00; 12200.00 − 366.00 = 11834.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11834.00`.
- Sub-lines: 7600.00 + 4600.00 = 12200.00, the allowance's base amount.
- The order date 2026-04-16 lies within the quotation's validity (to 2026-05-05).
- Cancellation: 11-OrderCancellation cancels this order "before production" with "No cost"; no charge for the cancelled order appears in any later document of the flow.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cbc:LineExtensionAmount` = `7600.00`: suspected that the sub-lines should carry the 3 % allowance too (they sum to 12200.00, not 11834.00). Refuted because the allowance is applied on the main line to the base 12200.00, which the sub-lines make up; the sub-lines are a breakdown before the allowance.
- `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`: suspected a filler equal to the line price. Refuted because it records the quoted price the note "Price as quoted." refers to.
