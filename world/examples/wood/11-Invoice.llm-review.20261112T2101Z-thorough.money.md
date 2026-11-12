# LLM review: 11-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/11-Invoice.xml`, Git blob `d14230a475262f9f8b47c7b7e1cbf9ab963fc61a` (committed)
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

### wood/11#F1 · Low · Resale/manufacture exemption without the buyer's exemption certificate
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- Why: the seller charges no state sales tax on a domestic sale within Upland State because the buyer, a furniture maker, uses the timber for manufacture. In state sales-tax practice (my own knowledge, e.g. US resale and manufacturing exemptions) such an exemption is not the seller's to decide: it rests on an exemption or resale certificate issued by or for the buyer, which the seller keeps and usually quotes on the invoice. The invoice (and the order 10-Order.xml, which anticipates the same treatment) names no such certificate, so nothing in the documents supports the exemption.
- Condition: the exemption can be traced to the buyer's exemption certificate or registration (e.g. a referenced certificate or an identifier in the buyer's tax scheme data), or the story says why Bayvarra's state sales tax needs none.
- Options: (a) preferred: reference the buyer's resale/manufacture certificate (AdditionalDocumentReference with its number) in the invoice, and in the order; (b) record in the story that the exemption is granted without a certificate.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 12 MTQ × 540 XBL / 1 MTQ = 6480.00 LineExtensionAmount = TaxExclusiveAmount = TaxableAmount; tax 0.00; TaxInclusiveAmount = PayableAmount = 6480.00.
- Price, quantity, tax treatment and accounting cost (1100 "Timber and materials") agree with the order `10-Order.xml` (BF-PO-26-0637).
- Tax category E (exempt) with reason RESALE "Sale for resale or manufacture" under STT fits seller and buyer both in Upland State (XB-UL) and a furniture maker buying timber.
- Terms: DueDate 2026-04-08 = 2026-03-09 + 30 days; PenaltySurchargePercent 1.5 × 6480.00 = 97.20 PenaltyAmount; PenaltyPeriod starts 2026-04-09, the day after the due date.
- Payment means: RF02MSINV260638 has a valid ISO 11649 check; payee account XB78BLUM38712004398618 (valid check) is the same as in 08-Invoice.xml; MPNS with rail LUMEPAY fits a domestic payment in XBL.
- Price plausibility: 540 XBL/m³ for kiln-dried sawn hardwood against about 1108 XBL/m³ for the planed slats of 02-Quotation.xml.
