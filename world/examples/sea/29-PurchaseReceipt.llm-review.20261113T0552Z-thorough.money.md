# LLM review: 29-PurchaseReceipt.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/29-PurchaseReceipt.xml`, Git blob `9863e47f157fcadd2d5f437f7b6156444ebcc978` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

## Findings

### sea/29#F1 · Low · Tax category "Services outside scope of tax" for a sale of goods, in a tax scheme that is the absence of tax
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: UNCL 5305 code O is "Services outside scope of tax" (code meaning from the listing; in UNCL 5305 "taxes are not applicable to the services"), but the line sells goods, as its own supply type says. The tax scheme is named "No general sales tax", without an identifier, i.e. a scheme that consists of the absence of tax. EN 16931 uses O for any supply outside the scope of VAT, but under the agreed semantic-conformance rule that practice does not make the code fit goods. The same combination (O with supply type GOODS) occurs in 5 examples (cotton 01, 04, 05, 16, sea 29; counted over `world/examples/*/*.xml` by parsing every `cac:ClassifiedTaxCategory` with ID O and SupplyTypeCode GOODS); the scheme name "No general sales tax" occurs 20 times.
- Condition: A sale of goods in Lisavu carries either no tax category, or a category and scheme that state what applies (a real tax with its category, or an outside-scope category whose definition covers goods), consistently across the examples that sell goods in Lisavu.
- Options: (a) leave tax category and tax total out of Lisavan receipts, since the island has no general sales tax (preferred if the world's rules accept that the absence of tax is shown by absence; this needs a decision under the "nothing implied by absence" rule); (b) keep O as the closest UNCL 5305 code and record the misfit as a finding about the code list; (c) give Lisavu a real scheme (e.g. a customs-only regime) with an identifier.
- Needs decision: yes

## Checked and consistent
- 2 × 289 = 578.000 XLC; tax 0.000; totals 578.000; card payment of 578.000 approved at the same time as the transaction; tax-inclusive price equals the price.
- Price plausibility: the bench cost Velumi 520 XBL × 0.4 = 208 XLC plus a freight and insurance share of 3090.00 × 0.4 × 19968.000 / 20275.200 / 96 ≈ 12.7 XLC, about 221 XLC landed (before duties and the customs inspection), so 289 XLC is a margin of about 31 %, plausible for a trader.
- Payment: debit card (UNCL 4461 code 55) on the Coralcard network, issuer `BSELXLSL`, the bank that holds Velumi's account; card holder the customer.

## Considered and refuted
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:Quantity` = `2`: suspected a conflict with the manufacturer's transaction conditions ("Sold to trade customers only, per pallet of four benches", `21-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`) and with the order's purpose "Stock for municipal projects" — refuted because those conditions govern Lumeway's sales to traders, not Velumi's resale, and a trader may sell from its stock to other customers.
