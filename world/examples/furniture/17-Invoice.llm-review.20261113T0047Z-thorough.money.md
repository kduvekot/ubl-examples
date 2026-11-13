# LLM review: 17-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/17-Invoice.xml`, Git blob `66ce2e15ac8d6433692b369df50c1ad798bd1603` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/17#F1 · Low · Office furniture booked to the parks renewal programme
- XPath: `/Invoice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Invoice/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/Invoice/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- XPath: `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `PWD-PARKS-26-AP`
- Why: `AccountingCostCode` is "The buyer's accounting code, applied to the Invoice as a whole". The invoice bills six office desks and their installation for the office project `PWD-PLAN-OFFICE-26`, but books them to the parks renewal programme, which in the tender flow carries the park benches (`tender/26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`, with project `PWD-PARKS-26`). The buyer's accounts-payable reference is the parks one too. Possible if the new office serves the programme, but nothing in the flow says so; project and cost centre point to different budgets.
- Condition: The buyer's cost centre for the desks and installation is the budget of the office project, or the flow states why the parks programme pays for the office.
- Options: (preferred) give the office project its own cost centre code, text and accounts-payable reference in 15, 16 and 17; or say in the order why the parks programme pays.
- Needs decision: yes

### furniture/17#F2 · Low · The party's own exemption is given with a transaction reason
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReasonCode` is "A reason for the party's exemption from tax, expressed as a code", the party's status. The code is the transaction reason of the same list, used in this invoice for the lines and the charge (`/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`); its meaning "Sale to a public body" describes the sale, not the department. The text after the colon states the status. All 55 party-level `ExemptionReasonCode` elements in the examples use this code and text (grep over `world/examples`, `*.xml` only).
- Condition: The party-level code names the party's status, or the list defines the code so it fits both uses.
- Options: (preferred) a status code ("public body") for the party-level element; or redefine the code in the list.
- Needs decision: no

### furniture/17#F3 · Low · Packaging-disposal charge that the order does not contain
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Packaging disposal`
- XPath: `/Invoice/cac:AllowanceCharge/cbc:Amount` = `24.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `24.00`
- Why: The invoice charges 24.00 for packaging disposal on top of the ordered goods and hours. The order (`/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581`) contains no such charge (`15-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `5952.00`, against `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `5976.00`); the only other place it appears is the seller's own work report 16, approved by the department. Nothing shows the department agreed the charge before it was billed, which a public buyer's invoice check would look for (own knowledge).
- Condition: The packaging-disposal charge can be traced to the order or another agreement in the flow, or it is not billed.
- Options: (preferred) add the charge to 15-Order so the invoice matches the order; or rely on the approved work report and say so (the invoice already refers to it); or drop the charge.
- Needs decision: no

## Checked and consistent
- Lines: 6 × 880 = 5280.00 and 14 × 48 = 672.00; `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `5952.00`; + charge 24.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `5976.00` = `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `5976.00`; tax 0.00; tax inclusive and payable 5976.00.
- Tax: exempt STT with reason `PUBLIC` on both lines, on the charge and in the subtotal; supply types GOODS (desks) and SERVICES (installation) fit the lines.
- Against order and work report: prices and quantities equal 15-Order; line 2 and the charge equal `16-WorkReport.xml:/WorkReport/cac:StatementMonetaryTotal/cbc:PayableAmount` = `696.00` (672.00 + 24.00); the line period 2026-04-08 to 2026-04-09 equals the work report's.
- Due date: 2026-04-09 + 30 days = 2026-05-09 = `/Invoice/cbc:DueDate` = `2026-05-09`, as "30 days net" says.
- Penalty: 1.5 % × 5976.00 = 89.64 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `89.64`, for one month from 2026-05-10, the day after the due date.
- Payment: `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF52BFINV260583` passes the ISO 11649 check and is built by the creditor from the invoice number; the account `XB42BLUM38712004503347` passes the IBAN-style check and is the seller's account as in 09-Invoice.
- Prices state their base quantity (1 EA, 1 HUR).

## Outside this review
- The invoice is issued 2026-04-09 at 10:10 for installation work that the work report gives as running until 2026-04-09 (seven hours per installer over two days); whether the work was finished by then is a timeline question.
