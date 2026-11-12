# LLM review: 10-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/10-Invoice.xml`, Git blob `13c4e7c68f3fa88f617d5f615a40ea35e815c2cd` (committed)
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

## Findings

### rail/10#F1 · High · Due date and discount differ from the payment terms agreed in the transport execution plan
- XPath: `/Invoice/cbc:DueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `08-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-14`
- Why: the invoice bills the rail freight agreed in 03-TransportExecutionPlan.xml (it references the
  waybill FRC-WB-26-0334 of that transport). The plan's payment terms for the service are "30 days
  net from the consignment note"; the consignment note is the waybill, issued 2026-04-14, so payment
  is due on 2026-05-14. The invoice instead counts 30 days from its own issue date (2026-04-17 →
  2026-05-17) and offers a 2 % settlement discount within 10 days, which the agreed "net" terms do
  not mention. Two documents of the flow state different payment terms for the same freight.
- Condition: the due dates and any settlement discount in this invoice follow the payment terms
  agreed in 03-TransportExecutionPlan.xml, or those terms are restated so that they agree with this
  invoice.
- Options: (a) preferred: align the plan's terms with the carrier's standard terms used here (30 days
  from the invoice, 2 % within 10 days), which the same carrier also applies in ore/06; (b) keep the
  plan's terms and make this invoice due 2026-05-14 (all three due dates) without a settlement
  discount.
- Needs decision: no

### rail/10#F2 · Medium · Late-payment penalty differs from the penalty agreed in the transport execution plan
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:TimeBasisCode` = `ANN`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: the plan encodes its penalty in PenaltySurchargePercent, "the penalty for payment after the
  settlement period, expressed as a percentage of the payment", i.e. as a late-payment penalty of 5 %
  (per day, capped at 25 %, by its note). This invoice charges late payment with 8 % a year, simple
  interest. If the plan's penalty is a late-payment penalty, the two contradict each other; if it is
  a penalty for late delivery (the likelier reading, see the review of 03), the plan uses the wrong
  element and the invoice is right. The contradiction cannot be settled from the XML alone.
- Condition: the late-payment penalty in this invoice and any late-payment penalty stated in
  03-TransportExecutionPlan.xml agree.
- Options: (a) preferred: treat the plan's penalty as a late-delivery penalty and fix the encoding in
  03 (this invoice stays as it is); (b) if the plan means late payment, state the same penalty in
  both documents.
- Needs decision: yes (which penalty the agreement means)

### rail/10#F3 · Low · The buyer's cost account for outbound freight is "Raw materials and parts"
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `One container slot on the container train to the distributor's siding.`
- XPath: `11-Invoice.xml:/Invoice/cbc:Note[2]` = `Delivered at place: the price includes the carriage to the siding.`
- Why: AccountingCostCode/AccountingCost is "the buyer's accounting code, applied to the Invoice as a
  whole". The buyer here is Valdara Industries, and the service is the carriage of its own finished
  benches to its customer under DAP: an outbound distribution cost of the sale, not a purchase of raw
  materials or parts. The code fits Valdara's inbound freight (ore/06 bills ore to the factory with
  the same code), but not this invoice. Elsewhere in the world freight has a cost account of its own
  (`plastics/07-Invoice.xml:/Invoice/cbc:AccountingCost` = `Freight`).
- Condition: the buyer's accounting cost names a cost account that fits outbound freight on sales.
- Options: (a) preferred: a freight-out / distribution cost account of Valdara; (b) leave the
  accounting cost out if Valdara has no such account in the world.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2 × 54,600 = 109,200 (line, LineExtensionAmount, TaxExclusiveAmount, TaxableAmount);
  20 % × 109,200 = 21,840; 109,200 + 21,840 = 131,040 = TaxInclusiveAmount = PayableAmount.
- Price and quantity agree with the waybill: 54,600 XUF "per container"
  (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`)
  and two containers (FRXU1044175, FRXU1044180) billed as 2 service units (E48).
- Settlement discount: 2 % × 131,040 = 2,620.8, rounded 2,621; the discount is computed on the
  tax-inclusive amount, as in the other XU invoices with the same terms (ore/06: 2 % × 2,064,529 =
  41,290.58 → 41,291; plastics/07: 2 % × 215,280 = 4,305.6 → 4,306). Settlement period 2026-04-17
  to 2026-04-27 is 10 days; due date 2026-05-17 is 30 days after issue.
- PaymentTerms/PaymentMeansID 1 points to the PaymentMeans with ID 1. The payee account
  XU920351041700000000523645 (check digits OK) belongs to Ferrano Rail Cargo SRU at the Serravona
  branch 03510-41700, the bank and branch codes inside the account number agree, and the same
  account is used for the same carrier in ore/06.
- The customer billed (Valdara Industries) is the BillToParty of 02 and 03 and the consignor that
  prepays the freight under DAP (08, 03).
- Tax category S 20 % with SupplyTypeCode SERVICES on the line and S 20 % in the subtotal agree.
- PenaltyInterestRate TimeBasisCode ANN means "year" in UNECE Rec. 20.

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID`: standard-rated VAT on
  cross-border freight to Bayvarra, where many real VAT systems exempt transport directly linked to
  the export of goods (own knowledge, e.g. EU VAT Directive Art. 146(1)(e)) — refuted because the
  customer is established in Urvania, and the world's examples consistently charge Urvanian VAT on
  freight for Urvanian customers (plastics/07, river freight to Bayvarra, S 20 %) and use the
  exemption SVCABROAD only for customers established abroad (road/14); the world's tax rules are
  taken as given.
- `/Invoice/cbc:TaxPointDate`: tax point on the invoice date while the delivery was planned for
  2026-04-15 — refuted because the flow carries no actual delivery date, and an invoice issued two
  days after the supply with the tax point on the invoice date is a common rule.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a domestic payment of 131,040 XUF
  — refuted because a real-time gross settlement channel is a legitimate choice for a domestic
  credit transfer between two XU companies; nothing in the flow contradicts it.
