# LLM review: 02-Quotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/02-Quotation.xml`, Git blob `6e768c2e81f270872df5b742e223f22c2e4950bf` (committed)
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

### furniture/02#F1 · Low · Quoted payable amount says nothing about tax
- XPath: `/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount` = `12200.00`
- XPath: `/Quotation/cac:QuotedMonetaryTotal/cbc:LineExtensionAmount` = `12200.00`
- Why: `PayableAmount` is "The amount of the monetary total to be paid". The quotation has no `TaxTotal` and no tax category on its line, so the payable amount equals the net line amount without saying whether the supply is taxed, exempt or quoted net of tax. The order that accepts this quotation states the treatment explicitly (`08-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`, state sales tax exempt), and the RFQ already says the goods are for the store's own line (resale). Under the repository's rule "nothing implied by absence" (IND6) the zero tax in the quoted total is only implied.
- Condition: The quotation either states the tax treatment of the quoted amount (a `TaxTotal` with the exempt STT category and reason, as in the order) or its payable amount is not presented as a tax-inclusive amount to be paid.
- Options: (preferred) add a `TaxTotal` with `TaxSubtotal` E / `RESALE` under STT, mirroring 08-Order, so quotation, order and invoice agree; or keep the quotation net and say so (e.g. a note that prices exclude state sales tax).
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Quotation/cac:QuotationLine/cac:LineItem/cbc:Quantity` = `20` × `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610` per `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1` set = 12200.00, equal to the line and document totals.
- Currency: `/Quotation/cbc:PricingCurrencyCode` = `XBL` is the currency the RFQ asked for (`01-RequestForQuotation.xml:/RequestForQuotation/cbc:PricingCurrencyCode` = `XBL`); XBL is not an assigned ISO 4217 code (own knowledge: assigned X-codes are XAF, XAG, XAU, XBA–XBD, XCD, XDR, XOF, XPD, XPF, XPT, XSU, XTS, XUA, XXX and the newer XCG), so it cannot be mistaken for a real currency.
- Validity: `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-05-05` is exactly 60 days after the issue date 2026-03-06, as requested in `01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestedValidityPeriod/cbc:DurationMeasure` = `60`. The orders 08 (2026-03-16) and 10 (2026-04-16) fall within it.
- The price 610 per set is what 08-Order, 09-Invoice and 13-CreditNote use.
