# LLM review: 05-Order.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/05-Order.xml`, Git blob `f1e12ba8710e50edcc4d14d6820937dec2dde266` (committed)
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

### sea/05#F1 · Low · Anticipated total of a CIF order leaves out the freight and insurance the seller later bills
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `CIF`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `50688.00`
- Why: `AnticipatedMonetaryTotal` is "the total amount for the Order anticipated by the buyer". The order is placed CIF Selanu, under which the seller contracts and pays the carriage and the cargo insurance to Selanu. The buyer anticipates 50,688.00 lume, the goods at catalogue prices only, while the invoice for this order bills sea freight and insurance on top: `22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00` and `22-Invoice.xml:/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`, total `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`. Either the CIF price includes freight and insurance (then the invoice charges them twice), or the seller passes them on separately (then the buyer, who chose CIF, would anticipate them, or the order would say they are to be added). The order alone cannot tell which; the choice changes the money story of the flow.
- Condition: the order's anticipated total and the way the flow bills freight and insurance under CIF tell the same story: either the anticipated total includes (an estimate of) the freight and insurance the invoice charges, or the flow does not charge them on top of the CIF goods price.
- Options: (a) keep the anticipated total at the goods value and make the seller's surcharges explicit earlier in the flow (order response, see the review of `06-OrderResponse.xml`), so the buyer's figure is a known partial; (b) add an anticipated freight/insurance charge to the order's totals; (c) treat 520 lume as a CIF price and stop billing freight and insurance separately in the invoice. Preferred: (a), because the catalogue price is clearly a trade price ex freight and the invoice already bills the charges.
- Needs decision: yes

## Checked and consistent
- Line 1: 96 × 520.00 = 49,920.00 = `/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `49920.00`; line 2: 12 × 64.00 = 768.00 = `/Order/cac:OrderLine[2]/cac:LineItem/cbc:LineExtensionAmount` = `768.00`; sum 50,688.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `50688.00` = taxable amount of the tax subtotal; tax 0 % → 0.00 = `/Order/cac:TaxTotal/cbc:TaxAmount` = `0.00`.
- Prices 520 and 64 lume per each (base quantity 1) are the catalogue's trade prices (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`, `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `64`) within their validity period; the quantities meet the catalogue's minimum quantities (4 and 1) and line 1 stays below its maximum (192).
- Tax category G, 0 %, exemption EXP under STT agrees with the catalogue, the order response and the invoice; the document currency XBL is the currency of all amounts.
- The same totals are confirmed in `06-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00`.

## Considered and refuted
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`: suspected that the catalogue's 3 % "Full container" allowance, attached to the range 4–192 benches, should have been applied to 96 benches — refuted for this example because the catalogue does not say at which quantity a "full container" is reached; the problem lies in how the catalogue encodes the condition (see the review of `02-Catalogue.xml`), and the order's price is consistent with the allowance not being earned.
- `/Order/cbc:AccountingCostCode` = `500`: suspected a seller-side code — refuted because the definition is "the buyer's accounting code, applied to the Order as a whole", and the order is issued by the buyer; the same code and text return in the invoice as the buyer's references.
