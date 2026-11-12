# LLM review: 03-TransportExecutionPlan.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/03-TransportExecutionPlan.xml`, Git blob `b9cd241a833ef55a0d6d59ac19ae0579457b6de6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

## Findings

### ore/03#F1 · Medium · Late-payment surcharge used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: PenaltySurchargePercent is defined as "The penalty for payment after the settlement period, expressed as a percentage of the payment", i.e. a surcharge the debtor owes for paying late. Here it carries the carrier's penalty for delivering late (the note: 5 % of the freight per day late, capped at 25 %). The aggregate PenaltyPaymentTerms ("Terms of payment applying to a penalty specified in the transport execution plan") fits the delivery penalty; the element inside it does not: it states a late-payment surcharge of 5 % that nobody agreed, and it loses the per-day basis and the 25 % cap. The same pattern (same note, same value) occurs in 3 XML examples: `grep -rh --include='*.xml' -B3 PenaltySurchargePercent world/examples` shows it in rail/03-TransportExecutionPlan.xml, plastics/04-TransportExecutionPlan.xml and this one.
- Condition: no element whose definition is about late payment carries the late-delivery penalty rate; the penalty (5 % of the freight per day late, at most 25 %) is still stated in PenaltyPaymentTerms.
- Options: (a) preferred: keep the penalty in `cbc:Note` of PenaltyPaymentTerms and drop PenaltySurchargePercent, because UBL has no structured element for a per-day delivery penalty; (b) if the story wants a late-payment surcharge for the freight, state it in the freight PaymentTerms with its own note, separate from the delivery penalty.
- Needs decision: no

### ore/03#F2 · Low · Waiting-time charge without currency and at an implausible rate, in an element meant for payment terms
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportServiceProviderSpecialTerms` = `Waiting time beyond two hours is charged.`
- Why: ServiceChargePaymentTerms is "Payment terms for the service charge associated with the transport service"; the note gives the rate of the charge, not when or how it is paid, and "40" has no currency. Against the freight of this service (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `962` XUF per tonne, 1 720 441 XUF for the train) 40 XUF per hour of a whole train waiting is about 0.002 % of the freight per hour; by my own knowledge of rail practice, an hour of waiting for a block train costs in the order of ten to a few hundred times the freight of one tonne, not 4 % of it. The same note occurs in 3 XML examples (`grep -rh --include='*.xml' -A2 '<cac:ServiceChargePaymentTerms>'`: rail/03, plastics/04, ore/03), so the amount looks like a shared default rather than a rate set for this service.
- Condition: the waiting-time rate states its currency and a level plausible against the freight of this train, and the element that carries it says what is charged and/or how it is paid in line with its definition.
- Options: (a) preferred: state the rate with currency (e.g. "XUF … per hour of waiting beyond two hours, invoiced with the freight, 30 days net") so that the note is both the charge and its payment terms; (b) move the rate into TransportServiceProviderSpecialTerms and leave ServiceChargePaymentTerms for how the charge is paid, or drop it.
- Needs decision: no

## Checked and consistent
- `/TransportExecutionPlan/cac:BillToParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274` (Valdara Industries), as in 02-TransportExecutionPlanRequest.xml, matches the FCA terms of `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA` (buyer pays main carriage) and the customer of the freight invoice 06-Invoice.xml.
- The freight payment terms `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` are clear in themselves; the freight invoice does not follow them (recorded as a finding of 06-Invoice.xml).
- The bonus terms (`/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note`) and the penalty note are expressed as text in aggregates whose definitions fit; whether the invoice applies them is recorded in the review of 06-Invoice.xml.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note`: suspected that the bonus condition ("delivered on the first day of the window") can never be met, because the buyer's requested delivery window starts on `01-Order.xml:/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-09`, before the train can leave on `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10` — refuted because the window this plan agrees is its own service window (10–13 March), whose first day is reachable on a short run from mine to factory in the same province; the remaining ambiguity is noted in the review of 06-Invoice.xml.
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note`: the penalty is capped at 25 %, i.e. five days late; with a service window ending `/TransportExecutionPlan/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-03-13` this is a coherent rule — no inconsistency.
