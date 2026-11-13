# LLM review: 16-WorkReport.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/16-WorkReport.xml`, Git blob `ff4f75f1f6e61357a2aa095fc65cac1d3e911e09` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
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

### furniture/16#F1 · Low · Office furniture booked to the parks renewal programme
- XPath: `/WorkReport/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/WorkReport/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- Why: `AccountingCostCode` is "An accounting cost code applied to this Work Report" and `AccountingCost` "An accounting cost centre or account to which this Work Report is charged". The goods and work are six office desks and their installation, which the work report and invoice attach to the office project `PWD-PLAN-OFFICE-26` ("Furnishing: the new office is furnished" in 16-WorkReport). The cost centre is the parks renewal programme, which in the tender flow carries the park benches (`tender/26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`, with project `PWD-PARKS-26`). Booking office desks to the parks programme is possible (e.g. if the new office serves the programme), but nothing in the flow says so, and the project and the cost centre point to different budgets.
- Condition: The buyer's cost centre for the desks and installation is the budget of the office project, or the flow states why the parks programme pays for the office.
- Options: (preferred) give the office project its own cost centre code and text in 15, 16 and 17; or say (e.g. in the order note) that the new office belongs to the parks renewal programme.
- Needs decision: yes

### furniture/16#F2 · Low · Packaging-disposal charge that the order does not contain
- XPath: `/WorkReport/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Packaging disposal`
- XPath: `/WorkReport/cac:AllowanceCharge/cbc:Amount` = `24.00`
- XPath: `/WorkReport/cac:StatementMonetaryTotal/cbc:ChargeTotalAmount` = `24.00`
- Why: The work report adds a document-level charge of 24.00 for packaging disposal (code `AEO` "Collection and recycling") to the 14 installation hours. The order it reports against (`/WorkReport/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581`, 15-Order) contains only the desks and the installation hours (`15-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `5952.00`) and no such charge, and no other document of the flow agrees it. A public buyer's purchase order normally fixes what may be billed; a charge outside it needs a basis (own knowledge of public procurement practice). 17-Invoice bills the same 24.00.
- Condition: The packaging-disposal charge can be traced to the order or another agreement in the flow, or it is not reported and billed.
- Options: (preferred) add the charge to 15-Order (as a document-level charge, so the anticipated total becomes 5976.00); or state in the work report that the department's officer approved it on site (the report is signed by the department); or drop it from 16 and 17.
- Needs decision: no

### furniture/16#F3 · Low · Zero tax total without category, and a charge without tax category
- XPath: `/WorkReport/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/WorkReport/cac:WorkReportLine/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/WorkReport/cac:AllowanceCharge`
- Why: `TaxTotal` is "A total amount of taxes of a particular kind applicable to this Work Report". The work report states a tax amount of 0.00 at document and line level without a `TaxSubtotal` or tax category, so it does not say why no tax applies (exempt, not subject, or not yet calculated); the charge has no `TaxCategory` either. 17-Invoice, which bills the same amounts, states the exempt STT category with reason `PUBLIC` for the lines and the charge. Under IND6 the exemption is only implied here.
- Condition: The work report's tax figures state the category and reason they rest on, as in 17-Invoice, or the work report carries no tax figures.
- Options: (preferred) add a `TaxSubtotal` with the exempt STT category and reason `PUBLIC` (taxable amount 696.00) and the same category on the charge; or remove the tax totals, since the work report is not the billing document.
- Needs decision: no

### furniture/16#F4 · Low · The party's own exemption is given with a transaction reason
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReasonCode` is "A reason for the party's exemption from tax, expressed as a code". The code's meaning "Sale to a public body" is the transaction reason of the same list, not the department's status; the text after the colon states the status. All 55 party-level `ExemptionReasonCode` elements in the examples use this code and text (grep over `world/examples`, `*.xml` only).
- Condition: The party-level code names the party's status, or the list defines the code so it fits both uses.
- Options: (preferred) a status code ("public body") for the party-level element; or redefine the code in the list.
- Needs decision: no

### furniture/16#F5 · Low · Hourly price without base quantity
- XPath: `/WorkReport/cac:WorkReportLine/cac:Price/cbc:PriceAmount` = `48`
- Why: `BaseQuantity` is "The quantity at which this price applies". The rate 48 is per hour per installer (14 h × 48 = 672.00), which the order and the invoice state with `BaseQuantity` 1 HUR (`17-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:BaseQuantity` = `1`); here it is implied by absence (IND6). 12 of 117 `Price` elements with a `PriceAmount` in `world/examples/*/*.xml` lack `BaseQuantity` (script count).
- Condition: The price states the quantity it applies to (1 HUR).
- Options: (preferred) add `BaseQuantity` 1 HUR.
- Needs decision: no

## Checked and consistent
- Hours: sub-lines 7 h + 7 h = 14 h = `/WorkReport/cac:WorkReportLine/cbc:Quantity` = `14` = `/WorkReport/cac:WorkQuantityTotal/cbc:Quantity` = `14`, the ordered quantity in 15-Order.
- Amounts: 14 × 48 = 672.00 = `/WorkReport/cac:WorkReportLine/cbc:LineExtensionAmount` = `672.00` = `/WorkReport/cac:StatementMonetaryTotal/cbc:LineExtensionAmount` = `672.00`; 672.00 + 24.00 = 696.00 = `/WorkReport/cac:StatementMonetaryTotal/cbc:PayableAmount` = `696.00`; tax-inclusive line amount 672.00 with tax 0.00.
- 17-Invoice bills exactly these figures (line 2 672.00, charge 24.00) and refers to this report and its line 1.
- Accounting cost code `PWD-PARKS-26` is the same as in 15-Order and 17-Invoice (whether it is the right budget is F1).
