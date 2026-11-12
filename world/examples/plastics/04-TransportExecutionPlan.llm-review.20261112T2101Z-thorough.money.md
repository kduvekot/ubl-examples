# LLM review: 04-TransportExecutionPlan.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/04-TransportExecutionPlan.xml`, Git blob `dc8723ba3179d86f1689569b00ab4ceab21fea05` (committed)
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

### plastics/04#F1 · High · Agreed payment term contradicts the due date of the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- Why: the plan fixes payment at 30 days net from the consignment note. The consignment note is the waybill `06-Waybill.xml` (`06-Waybill.xml:/Waybill/cbc:Name` = `Inland waterway consignment note under the CMNI`), issued `06-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-19`, so payment is due on 2026-05-19, net. The freight invoice for this transport instead counts 30 days from its own issue date and adds a discount: `07-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-22`, `07-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-22`, `07-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.` The two documents of the same transport contract state different due dates (19 vs 22 May) and different terms (net vs with settlement discount).
- Condition: the payment term agreed in the plan and the due date, discount and terms of `07-Invoice.xml` agree (same start of the 30 days, same due date, discount either agreed in the plan or absent from the invoice).
- Options: (a, preferred) word the plan's term as the carrier actually bills (30 days from invoice, 2 % within 10 days), since the invoice terms are the carrier's standard terms; (b) keep "from the consignment note, net" and make the invoice due 2026-05-19 without discount.
- Needs decision: no

### plastics/04#F2 · Medium · Late-payment surcharge element used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: `Payment Terms. Penalty_ Surcharge Percent` is defined as "The penalty for payment after the settlement period, expressed as a percentage of the payment" — a surcharge the debtor pays for paying late. Here it carries the carrier's penalty for delivering late (per day, capped at 25 %), which the carrier owes to the transport user: the opposite direction and a different event. The parent `PenaltyPaymentTerms` ("Terms of payment applying to a penalty specified in the transport execution plan") can hold a delivery penalty, but not through this element; the "per day" basis and the 25 % cap are only in the note.
- Condition: no element defined for late payment carries the late-delivery penalty; the penalty is stated in text (or in an element whose definition fits) and its rate, basis and cap agree with that text.
- Options: (a, preferred) keep the penalty in `PenaltyPaymentTerms/cbc:Note` only and drop `PenaltySurchargePercent`; (b) if a late-payment surcharge is also agreed, state it separately in `PenaltySurchargePercent` with its own text.
- Needs decision: no

### plastics/04#F3 · Low · Commission and penalty are percentages of a freight the plan never states
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note` = `Brokerage of 1.25 % of the freight, …`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: the confirmed plan is the transport contract; two of its terms are expressed as a percentage of "the freight", but the plan states no freight rate or amount (the document has no amount element at all). The rate appears only afterwards, in `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400` and `07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `1495` per tonne. `Consignment` in the plan can carry a `FreightAllowanceCharge`.
- Condition: the agreed freight (rate per tonne, or amount) is stated in the plan, and equals what the waybill and the invoice use.
- Options: (a, preferred) add the freight to the plan's consignment as a freight charge (1,495 `XUF` per tonne, 179,400 `XUF` for 120 t); (b) reference a price list or framework contract that holds the rate.
- Needs decision: no

### plastics/04#F4 · Low · Waiting-time charge without currency, implausibly low
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- Why: the charge has no currency. Read in the contract's currency `XUF`, 40 `XUF` an hour is 0.40 `XBL` (rate 100 `XUF` = 1 `XBL` used throughout the examples), against a freight of 1,495 `XUF` per tonne and goods worth 83,200 `XUF` per tonne. Taking the goods price as a scale (recycled PE granulate costs roughly 1,000 EUR per tonne, own knowledge), 40 `XUF` is about half a euro an hour, far below any real waiting or demurrage charge for a barge.
- Condition: the waiting-time charge names its currency and its amount is plausible against the freight.
- Options: (a, preferred) state the currency and a plausible hourly amount (e.g. in the order of the freight for a few tonnes); (b) express it as a share of the freight.
- Needs decision: no

### plastics/04#F5 · Low · Consignee's bank account in the transport plan
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". The consignee pays nothing under this plan (`/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`); its current account is copied master data. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`).
- Condition: the consignee party in the plan carries no financial account unless the plan uses it.
- Options: (a, preferred) drop it; (b) keep it only with a freight-collect arrangement involving the consignee.
- Needs decision: no

## Checked and consistent
- `BillToParty` (defined as "The Party who executes the Payment for the transport service") = Rinova Recovery, who receives and (by `CPT`) bears the freight invoice `07-Invoice.xml`.
- Waiting time is announced consistently: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportServiceProviderSpecialTerms` = `Waiting time beyond two hours is charged.` matches the service-charge note (apart from F4). No waiting time or late-delivery penalty is billed in `07-Invoice.xml`, which agrees with a transport delivered in the estimated 3 days.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note` = `Brokerage of 1.25 % of the freight, …`: a commission between the carrier and a broker who is not a party of the plan — refuted because brokerage clauses ("brokerage x % on freight") are a standard part of charter terms in inland and sea shipping (own knowledge), and `CommissionPaymentTerms` is defined for exactly this.
