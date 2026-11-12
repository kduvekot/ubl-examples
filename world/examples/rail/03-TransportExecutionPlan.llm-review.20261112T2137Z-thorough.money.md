# LLM review: 03-TransportExecutionPlan.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/03-TransportExecutionPlan.xml`, Git blob `10a1218954b5cf3553a1e440bbc205476072297d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### rail/03#F1 · High · Agreed payment terms contradict the due date of the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `08-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-14`
- XPath: `10-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-17`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-17`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- Why: TransportExecutionTerms/PaymentTerms are the "payment terms associated with the transportation
  service" agreed in this plan. They run 30 days from the consignment note, which is the waybill
  FRC-WB-26-0334 issued 2026-04-14, so the freight falls due on 2026-05-14. The freight invoice
  10-Invoice.xml, which bills exactly this service (it references the waybill), sets the due date
  to 2026-05-17 (30 days from its own issue date, 2026-04-17) and adds a 2 % settlement discount for
  payment within 10 days that the agreed terms ("net") do not mention. The two documents state
  different payment terms for the same freight. The same note occurs in plastics/04 and ore/03
  (`grep -rl --include='*.xml' '30 days net from the consignment note'` over world/examples: 3 files).
- Condition: the payment terms agreed in this plan and the due date, discount and basis date applied
  in 10-Invoice.xml agree with each other.
- Options: (a) preferred: state the plan's terms as the carrier actually bills them (30 days from the
  invoice date, with the 2 % / 10 days discount), since the invoice terms are the carrier's standard
  terms used across the world's XU invoices; (b) keep "from the consignment note" and make the
  invoice due 2026-05-14 without a discount.
- Needs decision: no

### rail/03#F2 · Medium · PenaltySurchargePercent carries a per-day penalty that is not a late-payment percentage
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:TimeBasisCode` = `ANN`
- Why: PenaltySurchargePercent is "the penalty for payment after the settlement period, expressed as
  a percentage of the payment", a single percentage of the late payment. The note describes something
  else: 5 % of the freight for every day late, capped at 25 %. Read as a penalty for late delivery
  (the usual meaning of a percentage of the freight per day of delay in rail transport, own
  knowledge), the element carries a meaning other than its definition. Read as a penalty for late
  payment, 5 % per day contradicts the freight invoice 10-Invoice.xml, whose penalty for late payment
  is 8 % a year, simple interest. Either way the structured value does not express the note: the
  "per day" basis and the 25 % cap are lost. The same pair of values occurs in plastics/04 and ore/03
  (grep for `5 % of the freight per day late` over `*.xml`: 3 files).
- Condition: PenaltySurchargePercent is present only if the penalty is a percentage of a payment made
  after the settlement period, and then agrees with the late-payment terms of 10-Invoice.xml; a
  late-delivery penalty is not expressed in it.
- Options: (a) preferred, if the penalty is for late delivery: keep the note, drop
  PenaltySurchargePercent (or move the penalty to an element meant for delivery penalties) and say
  in the note that it is the carrier's liability for delay; (b) if it is for late payment: make it
  agree with the invoice's 8 % a year (e.g. PenaltyPaymentTerms with that rate) and remove the
  per-day wording.
- Needs decision: yes (which penalty the agreement means)

### rail/03#F3 · Low · Waiting-time charge without a currency, at an implausible rate
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`
- Why: the note gives a rate but no currency, while every amount of the flow is in XUF. Read as
  40 XUF, an hour of waiting would cost less than a thousandth of the freight for one container
  (54,600 XUF in the waybill; 40 / 54,600 = 0.07 %), which is not a plausible waiting-time charge
  for a train or a tractor and crew. The same note occurs in plastics/04 and ore/03 (grep for
  `Waiting time 40 per hour` over `*.xml`: 3 files).
- Condition: the waiting-time charge names its currency, and its amount is plausible against the
  freight rate of the same carrier.
- Options: (a) preferred: give the rate with its currency at a plausible level (e.g. a few thousand
  XUF per hour); (b) state only that waiting time is charged per the framework contract, without a
  figure.
- Needs decision: no

## Checked and consistent
- BillToParty is Valdara Industries, the same party billed as AccountingCustomerParty in
  `10-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`.
- PrepaidPaymentTerms ("Freight prepaid by the consignor under DAP") agrees with the waybill
  (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Freight prepaid by the consignor under DAP.`),
  with the delivery terms of the sale (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`) and with
  the freight invoice addressed to the consignor.
- TransportServiceProviderSpecialTerms ("Waiting time beyond two hours is charged.") and
  ServiceChargePaymentTerms describe the same charge; ChangeConditions ("without charge") does not
  conflict with any charge billed in the flow.
- The tax registrations of the parties (Valdara XU007299291, Ferrano Rail Cargo XU007328060,
  Lumeway UL-1230822 under STT/XBL) are the same in every example of the flow (compared over all
  PartyTaxScheme aggregates of the 11 XML files).

## Considered and refuted
- `/TransportExecutionPlan/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note`: "prepaid" freight
  while the freight is invoiced afterwards on 30 days — refuted because "prepaid" is the freight
  term (paid by the consignor at origin, as opposed to collect at destination), not payment in
  advance, and the consignor is the party invoiced.
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions`:
  demurrage "per container day" without a rate — refuted because the element holds instructions, not
  a charge; the rate belongs to the framework contract the plan refers to, and no demurrage is
  billed in the flow.
