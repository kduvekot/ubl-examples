# LLM review: 01-Order.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/01-Order.xml`, Git blob `b65397fa0c7cc5caf77d2e114d9eb2db2610109c` (committed)
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
- 192 × 49,900 = 9,580,800 = line LineExtensionAmount = AnticipatedMonetaryTotal LineExtensionAmount
  = PayableAmount = TaxableAmount; tax 0.
- Price, quantity, totals and tax category agree with the sales invoice
  (`11-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9580800`).
- The delivery terms DAP to Lumeway's siding agree with the invoice note and with the freight being
  paid by the seller (03, 08, 10).
- AccountingCostCode 4410 "Stock purchases" fits a wholesaler (ISIC 4649) buying goods for resale and
  is repeated in the invoice.

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode`: the buyer
  states the seller's Urvanian export exemption in its order — refuted because the Order's TaxTotal
  is the anticipated tax of the order, the buyer knows the goods are exported from Urvania to
  Bayvarra, and the invoice applies the same treatment.
- `/Order/cbc:DocumentCurrencyCode`: a Bayvarran buyer ordering in XUF — refuted because ordering in
  the seller's currency is a legitimate choice and the invoice follows it.
