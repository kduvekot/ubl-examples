# LLM review: 05-Invoice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/05-Invoice.xml`, Git blob `a846f2c92225b4f657cb71040b2ccfd1f8ecfc9d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/05#F1 · High · Due date is 45 days after the invoice, the terms say 30 days net
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-07-19`
- XPath: `/Invoice/cbc:DueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-07-20`
- Why: the invoice is issued on `/Invoice/cbc:IssueDate` = `2026-06-04`; 30 days net gives 2026-07-04, but all three due dates say 2026-07-19, 45 days after the invoice, and the penalty period starts the day after that. The note does not name another start for the 30 days (delivery, receipt), and none of the documents of the flow has a date from which 30 days would end on 2026-07-19 (the despatch advice and the waybill are of 2026-06-04 as well). Every other invoice with the terms `XB-STD` and this note has its due date exactly 30 days after the invoice, except `utilities/06-Invoice.xml` (counted over `*.xml`: 15 other such invoices, PaymentTerms/PaymentDueDate minus IssueDate) (e.g. `air/10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-06-14` for an invoice of 2026-05-15).
- Condition: the due dates (`DueDate`, `PaymentMeans/PaymentDueDate`, `PaymentTerms/PaymentDueDate`) and the start of the penalty period agree with the payment terms the note states, counted from the date the note names (the invoice date when it names none).
- Options: (a) preferred: due date 2026-07-04 and penalty period from 2026-07-05, as the seller's standard terms say; (b) keep 2026-07-19 and state the agreed term (e.g. "45 days net", or 30 days from an arrival date the flow documents).
- Needs decision: no

### mast/05#F2 · Low · PricingReference carries no pricing information
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:HazardousRiskIndicator` = `true`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:BatchQuantity` = `1`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:HazardousRiskIndicator` = `true`
- Why: PricingReference is "A reference to pricing and item location information associated with this invoice line", and OriginalItemLocationQuantity is "An original set of location-specific properties (e.g., price and quantity) associated with this item". Here it holds no price, no quantity condition and no location, only a dangerous-goods flag that the line already carries in `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:HazardousRiskIndicator` = `true` and a delivery batch of one battery. The invoice does nothing with either for its price, which is the plain `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `2400` per battery, as in the order; lines 2 and 3, also dangerous goods, have no such block. The order has no PricingReference either, so it is not an "original" condition carried over. (The same use of PricingReference without a price occurs in one other example, `retail/18-Invoice.xml`, with a lead time; counted over `*.xml`.)
- Condition: every `PricingReference` in the invoice carries information that bears on the price of its line, or the block is absent.
- Options: (a) preferred: remove the block; (b) if the batch of one battery per delivery unit is a price condition (e.g. a price that applies per single-battery delivery), say so with the price it conditions.
- Needs decision: no

## Checked and consistent
- Line arithmetic: 6 × 2,400 = 14,400.00, 1 × 180 = 180.00, 20 × 9.5 = 190.00 (base quantity 1 in each line's unit); sum 14,770.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `14770.00` = TaxExclusiveAmount = TaxInclusiveAmount (tax 0.00) = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `14770.00`. No allowances, charges or prepayments. The same prices and quantities as `01-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `14770.00`; quantities as despatched in `04-DespatchAdvice.xml`.
- Tax: category G (free export item) with the exemption reason "Export outside Bayvarra" at document and line level, supply type goods, under the seller's Upland State sales tax; seller in Bayvarra, buyer on Lisavu, so an export; percent 0 and tax 0.00 agree; the order states the same treatment.
- Penalty: `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `221.55` = 1.5 % × 14,770.00 for the one-month `PenaltyPeriod`, matching `PenaltySurchargePercent` and the note.
- Payment means: credit transfer to the seller's own current account at Bank of Lumeport, in lume, account country Bayvarra; `check_ids.py` passes the IBAN-like account `XB69BLUM38712001885122` and the creditor reference `RF78SEINV260719`, which is also the one quoted in `InstructionNote`. Cross-border payment from Lisavu over the Trade Accord rail with shared charges fits the parties' countries. Payee account and PaymentTerms/PaymentMeansID `1` point to the one PaymentMeans.
- No freight is invoiced, which agrees with `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CPT` (seller pays carriage).
- BLUMXBLX is not a real BIC: its country part XB is not an assigned ISO 3166 code (own knowledge).

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XBL`: suspected redundant with DocumentCurrencyCode — refuted, the buyer is on Lisavu (coral), so stating that payment is in lume has a reason.
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR`: checked against the cross-border situation; shared charges is the usual choice and nothing in the flow says otherwise.
