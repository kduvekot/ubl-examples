# LLM review: 11-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/11-Invoice.xml`, Git blob `ee9c00c2aed8b2e82ac3390db74cfce890bdf1a1` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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
- Arithmetic: 192 × 49,900 = 9,580,800 = line LineExtensionAmount = LineExtensionAmount =
  TaxExclusiveAmount = TaxableAmount; tax 0 at 0 %; TaxInclusiveAmount = PayableAmount = 9,580,800.
- Agrees with the order `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `192`,
  `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900` and its
  anticipated totals and tax category (G, EXP); the buyer's accounting code (4410 "Stock purchases")
  is the one the buyer gave in the order and fits a wholesaler buying goods for resale.
- Tax: category G ("Free export item, tax not charged"), exemption reason EXP "Export of goods
  outside Urvania", SupplyTypeCode GOODS; the customer is in Bayvarra and the goods leave Urvania
  under the transit declaration 06-TransitCustomsDeclaration.xml with a preceding export declaration.
- Payment terms: 2 % × 9,580,800 = 191,616 = SettlementDiscountAmount; settlement period
  2026-04-17 to 2026-04-27 (10 days); due 2026-05-17 (30 days), equal in DueDate, PaymentMeans and
  PaymentTerms; PaymentMeansID 1 points to the PaymentMeans; penalty 8 % a year (ANN = year).
- Payee account XU790351041600000000209458 (check digits OK) is Valdara's account at the Ferrano main
  branch 03510-41600 of Crevalto Bank, the same as in road/15, tender/32 and the remittance advices
  that pay Valdara (`grep -rn --include='*.xml' XU790351041600000000209458`); the RF reference
  RF20VIINV260337 has valid check digits and matches the instruction note.
- Cross-border payment from Bayvarra: RTNS on the Trade Accord rail with charges shared (SHAR) is
  coherent; the note on DAP agrees with the order's delivery terms and with the freight being
  billed to Valdara in 10-Invoice.xml.

## Considered and refuted
- `/Invoice/cbc:TaxPointDate`: tax point on the invoice date (2026-04-17), while the train left
  Ferrano on 2026-04-14 — refuted because no actual date of export or delivery is stated in the
  flow, and a tax point on an invoice issued within days of the supply is a common rule; nothing in
  the flow contradicts it.
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: basis of the discount (gross or net) —
  refuted as a problem here because tax is 0, so both give 191,616.
- `/Invoice/cbc:DocumentCurrencyCode`: invoice in XUF to a Bayvarran customer whose tax scheme
  currency is XBL — refuted because the order was placed in XUF, and the tax scheme currency only
  concerns Lumeway's own tax reporting.
