# LLM review: 01-Order.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/01-Order.xml`, Git blob `888e6ba193f9e99d9a10149a112547e954b6d115` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

## Checked and consistent
- Line arithmetic: `/Order/cac:OrderLine[1]/cac:LineItem/cbc:Quantity` = `96` × `/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900` per `/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1` gives 4 790 400, which is `/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `4790400`; 12 × `/Order/cac:OrderLine[2]/cac:LineItem/cac:Price/cbc:PriceAmount` = `5980` gives `/Order/cac:OrderLine[2]/cac:LineItem/cbc:LineExtensionAmount` = `71760`.
- Totals: 4 790 400 + 71 760 = 4 862 160 = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `4862160` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `4862160` = `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `4862160`; tax 0 at 0 %.
- Every amount is in the document currency `/Order/cbc:DocumentCurrencyCode` = `XUF`; the prices reappear unchanged in `15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `49900` and `15-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `5980`, and the "same price" of the substitution in `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Price/cbc:PriceAmount` = `5980`.
- `/Order/cbc:AccountingCostCode` = `4410` / `/Order/cbc:AccountingCost` = `Stock purchases` (the buyer's code) is repeated in `15-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `4410`.
- XUF and XBL are not assigned ISO 4217 codes (own knowledge of the list: the X-codes in use are XAF, XAG, XAU, XBA–XBD, XCD, XCG, XDR, XOF, XPD, XPF, XPT, XSU, XTS, XUA, XXX).

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G` with `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`: suspected that an export exemption does not fit a sale delivered `/Order/cac:DeliveryTerms/cbc:ID` = `FCA` at the seller's 3PL in Ferrano, where the buyer arranges the transport — refuted because the seller itself declares the export (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`), so the export can be proved by the supplier, which is what zero-rating of an export requires (own knowledge of VAT practice); the order only anticipates the treatment the invoice applies.
