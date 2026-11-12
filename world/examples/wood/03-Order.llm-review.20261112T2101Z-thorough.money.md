# LLM review: 03-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/03-Order.xml`, Git blob `f14d6ba97f84855490d38ffc0a4d1386846aa813` (committed)
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

### wood/03#F1 · Medium · The pallet charge has no tax category and is left out of the taxable amount
- XPath: `/Order/cac:AllowanceCharge/cbc:Amount` = `240.00`
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `34560.00`
- Why: TaxableAmount is "the net amount to which the tax percent (rate) is applied". The order adds a document-level charge of 240.00 XBL (payable total 34800.00) but gives the charge no TaxCategory, and the only subtotal covers the line amount alone, so the tax treatment of 240.00 of the anticipated amount is undefined. The invoice for this order treats the charge as part of the same exempt export supply: `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `G` and `08-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `34800.00`. The order's anticipated tax breakdown therefore does not match the invoice of the same deal.
- Condition: every amount in the order's anticipated total belongs to a tax subtotal (the charge has a TaxCategory), and the sum of the taxable amounts equals line extension plus charges (34800.00), as in the invoice.
- Options: (a) preferred: give the charge the TaxCategory G/EXP/STT and set TaxableAmount to 34800.00, matching the invoice; (b) drop the TaxTotal from the order if the buyer does not anticipate tax.
- Needs decision: no

## Checked and consistent
- 4800 EA × 7.2 XBL / 1 EA = 34560.00; + 240.00 charge = 34800.00 PayableAmount; ChargeTotalAmount 240.00.
- Price, charge, currency and delivery terms (DAP) agree with the quotation `02-Quotation.xml` that the order references.
- Tax category G (UNCL 5305 "Free export item, tax not charged") with exemption reason EXP "Export outside Bayvarra" under STT fits a sale from Upland State (XB) to Ferrano (XU).
- DocumentCurrencyCode XBL matches all currencyIDs.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50`: suspected a wrong factor — refuted because the item is sold in packs of 50, so a factor of 50 from the base unit (one slat) to the orderable unit (a pack) is a correct reading; 4800 slats = 96 packs.
- `/Order/cbc:AccountingCostCode` = `3100`: suspected a copy of the buyer's ISIC code 3100 — refuted because AccountingCostCode is "the buyer's accounting code", and 3100 with the text "Raw materials and parts" is a plausible account in the buyer's chart of accounts; the coincidence with the industry code is not a contradiction. The invoice repeats it, as it should.
