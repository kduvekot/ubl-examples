# LLM review: 02-Quotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/02-Quotation.xml`, Git blob `b8dd536e88f83270060fe92537f76080cae01be9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### wood/02#F1 · High · Free text says the price is per thousand slats; the structured price is per slat
- XPath: `/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `7.2`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`
- Why: BaseQuantity is "the quantity at which this price applies"; here it is 1 EA, so the price is 7.2 XBL per slat, and 4800 × 7.2 = 34560.00 = the line extension amount, which confirms the per-slat reading. The transaction conditions ("a specification of purchasing, sales, or payment conditions applying to Orders related to this Quotation") say the slats are quoted per thousand. A price per thousand would be BaseQuantity 1000 EA with a PriceAmount of 7200. The text and the structured price contradict each other, and the order and invoice (`03-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`, `08-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1`) follow the structured value.
- Condition: the transaction conditions and the Price (PriceAmount, BaseQuantity) state the same price basis, and PriceAmount × InvoicedQuantity/BaseQuantity still gives the line amount.
- Options: (a) preferred: change the text to the actual basis ("Quoted per slat; minimum one truck"), since order and invoice already use the per-slat price; (b) quote per thousand (PriceAmount 7200, BaseQuantity 1000 EA) here and in the order and invoice.
- Needs decision: no

### wood/02#F2 · Low · Zero tax total without a subtotal that says why no tax is charged
- XPath: `/Quotation/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Quotation/cac:QuotationLine/cbc:TotalTaxAmount` = `0.00`
- Why: the quotation states a tax amount of zero but no TaxSubtotal and no TaxCategory, so the reason (the seller's state sales tax is not charged on an export to Urvania) is only implied by the zero. The order of the same deal carries it explicitly (`03-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G` with exemption reason `EXP`), as does the invoice. Under the rule "nothing implied by absence" a zero tax needs its category, or the tax total stays out.
- Condition: either the quotation's TaxTotal carries a TaxSubtotal with the category (G, STT, exemption reason) that explains the zero amount, or the quotation carries no tax amounts at all.
- Options: (a) preferred: add the same TaxSubtotal as the order (taxable 34800.00 incl. the pallet charge, G, EXP), so the quotation says what the buyer will pay and why; (b) drop TaxTotal and the line tax amounts.
- Needs decision: no

### wood/02#F3 · Low · Substitute and alternative items offered without a price
- XPath: `/Quotation/cac:QuotationLine/cac:SellerProposedSubstituteLineItem/cbc:ID` = `1-S`
- XPath: `/Quotation/cac:QuotationLine/cac:AlternativeLineItem/cbc:ID` = `1-A`
- Why: the quotation proposes a 35 mm substitute and an oak alternative for 4800 slats each, but neither line item has a Price or LineExtensionAmount. A quotation is the seller's priced offer; an alternative without a price cannot be accepted or compared, and the line note "As drawn; ash or oak." suggests the oak option is a real choice. (Ash and oak are normally priced differently.)
- Condition: each proposed substitute and alternative line item states its price (or the quotation states that it is priced the same as the main line).
- Options: (a) preferred: give each a Price (and LineExtensionAmount); (b) state in a note that they are offered at the same price; (c) drop them if they are not really offered.
- Needs decision: no

## Checked and consistent
- Line arithmetic: 4800 EA × 7.2 XBL / 1 EA = 34560.00 (line, LineItem and QuotedMonetaryTotal LineExtensionAmount); 34560.00 + 240.00 charge = 34800.00 PayableAmount.
- `/Quotation/cac:QuotedMonetaryTotal/cbc:ChargeTotalAmount` = `240.00` equals the single charge.
- ACH (UNCL 7161 "Heat treatment") fits the reason "Heat-treated export pallets"; the same charge (240.00 XBL) is in the order and invoice.
- Validity: "Valid for 30 days" from 2026-02-19 ends 2026-03-21 = ValidityPeriod/EndDate; it matches the RFQ's requested 30 days; the order (2026-02-22) falls within it.
- PricingCurrencyCode XBL matches the RFQ's requested currency and all amounts' currencyID.
- PaymentMeansCode 30 (credit transfer) matches the means in the invoice.
- DAP: the seller bears transport to Ferrano, consistent with Marrowdale as BillToParty in 04-TransportExecutionPlanRequest.xml.
- Plausibility of the price: one slat is 1.8 × 0.095 × 0.038 = 0.0065 m³, so 7.2 XBL is about 1108 XBL/m³, about twice the 540 XBL/m³ for unprocessed boards in 10-Order.xml, plausible for planed, cut-to-size hardwood.

## Considered and refuted
- `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50`: suspected a wrong factor, since quantity and base quantity are both in EA — refuted because the item is sold in packs of 50 (`/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `50`), so the orderable unit is a pack of 50 slats, 50 times the base price unit; 4800 is a whole number of packs (96).
