# LLM review: 01-Order.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/01-Order.xml`, Git blob `af435c2882d01f0ca686e44a410c2da3f745d496` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Checked and consistent
- Line arithmetic: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `1800` × `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `8060` per `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1` = 14 508 000 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `14508000` = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `14508000`.
- Tax: 20 % of 14 508 000 = 2 901 600 = `/Order/cac:TaxTotal/cbc:TaxAmount` = `2901600`; 14 508 000 + 2 901 600 = 17 409 600 = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `17409600`.
- The price per tonne is the one the seller invoices (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `8060`); category S at 20 % is the one both invoices of the flow apply.
- FCA mine siding (`/Order/cac:DeliveryTerms/cbc:ID` = `FCA`): the buyer bears the main carriage, which matches the freight invoice of Ferrano Rail Cargo to Valdara Industries (06-Invoice.xml) and the bill-to party of the transport plan.

## Considered and refuted
- `/Order/cbc:AccountingCostCode` = `3100`: suspected to be the buyer's ISIC code (`/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`) copied into the accounting code — refuted because the same code with the text `Raw materials and parts` is used in every one of the 12 XML examples that carry `3100` as AccountingCostCode, all of them Valdara Industries documents (counted with `grep -rl --include='*.xml' '<cbc:AccountingCostCode>3100'` and `grep -L Valdara` on the result, which returned none), so it reads as Valdara's own cost account; the equality with the ISIC code is a coincidence that does no harm.
- `/Order/cac:AnticipatedMonetaryTotal`: no TaxExclusiveAmount/TaxInclusiveAmount — refuted: both are optional and LineExtensionAmount plus PayableAmount state the anticipated total completely for a one-line order without allowances.
