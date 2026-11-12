# LLM review: 07-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/07-Invoice.xml`, Git blob `a1e9b7e2c326a01d31d3b741f419d375d10a04e9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### plastics/07#F1 · High · Due date contradicts the payment term agreed in the transport plan
- XPath: `/Invoice/cbc:DueDate` = `2026-05-22`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-05-22`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-22`
- Why: the transport contract for this freight agrees `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` The consignment note is the waybill this invoice refers to (`/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`), issued `06-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-19`; 30 days from it is 2026-05-19. The invoice counts 30 days from its own issue date (`/Invoice/cbc:IssueDate` = `2026-04-22`) and so falls due three days later than agreed.
- Condition: the invoice's due dates follow the payment term agreed in `04-TransportExecutionPlan.xml`, or the plan's term is the one the invoice applies.
- Options: (a, preferred) align the plan's term with the carrier's standard terms used here (30 days from invoice), see also F2; (b) make the invoice due 2026-05-19 (and its settlement period start at the consignment note).
- Needs decision: no

### plastics/07#F2 · Low · Settlement discount offered although the contract says "net"
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- Why: "30 days net" in the transport plan (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`) means payment without deduction; the invoice offers a 2 % settlement discount (`/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4306`). A carrier may grant more than agreed, so this is not a contradiction in itself, but the two documents describe the payment terms of the same contract differently.
- Condition: the payment terms in the plan and in the invoice describe the same arrangement (with or without settlement discount).
- Options: (a, preferred) state the discount in the plan's payment terms as well (the invoice terms look like the carrier's standard terms); (b) drop the discount from the invoice.
- Needs decision: no

## Checked and consistent
- Line: 120 t × 1,495 `XUF` (base quantity 1 t) = 179,400 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `179400` = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `179400` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `179400`. Same rate and amount as `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`.
- Tax: 20 % of 179,400 = 35,880 = `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount` = `35880` = `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `35880`; 179,400 + 35,880 = 215,280 = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `215280` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `215280`. Category `S` and supply type `SERVICES` on the line agree with the subtotal.
- Settlement discount: 2 % of the payable 215,280 = 4,305.6, rounded 4,306 = `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4306`; the same (gross) basis as Rinova's discount in `10-Invoice.xml` (2 % of 9,984,000 = 199,680). Settlement period 2026-04-22 to 2026-05-02 = 10 days, as the note says.
- Bill-to: the customer is Rinova, the seller under `CPT` and the bill-to party of the plan (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`).
- Payment means: credit transfer to the carrier's own `XUF` account (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Fiumella Barges SRU`), domestic RTGS between two Urvanian parties; RF reference and IBAN-like check digits OK (`check_ids.py`).
- Penalty interest 8 % per year, simple, in an invoice between two Urvanian parties: plausible and the same as Rinova's terms.

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S` at 20 % on cross-border freight for exported goods — suspected because real VAT systems exempt or zero-rate international transport linked to an export (own knowledge: EU VAT Directive Art. 146(1)(e)). Refuted for this world: the customer Rinova is established in Urvania, and the Urvanian exemption list (`world/codelists/gc/XU-TaxExemptionReasonCode.gc`, read for code meanings) has no exemption for transport of exported goods (`EXP` covers goods, `SVCABROAD` services to customers established abroad), so standard rate is the consistent treatment.
- `/Invoice/cbc:TaxPointDate` = `2026-04-22` — suspected as a filler equal to the issue date; refuted: the service ends with the discharge in Lumeport (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:OccurrenceDate` = `2026-04-22`), so the tax point is the day the service is completed, which happens to be the invoice date.
