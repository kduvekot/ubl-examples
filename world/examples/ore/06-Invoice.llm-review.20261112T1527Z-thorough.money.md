# LLM review: 06-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/06-Invoice.xml`, Git blob `b3fee4995e687ca616a88364c0b3bc9ec2261466` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### ore/06#F1 · High · Due date and terms contradict the payment terms of the transport plan the invoice refers to
- XPath: `/Invoice/cbc:DueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`
- Why: the invoice refers to the transport plan (`/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`) and to the consignment note (`/Invoice/cac:AdditionalDocumentReference[2]/cbc:ID` = `FRC-WB-26-0310`). The plan agrees freight payment at 30 days net from the consignment note, which was issued on 10 March: due on 9 April 2026. The invoice instead counts 30 days from its own issue date (12 March → 11 April) and offers a 2 % settlement discount (`/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`, `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `41291`) that the plan does not contain. The terms ID `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD` and the identical note, rate and penalty interest in 07-Invoice.xml (another seller) suggest the seller's standard terms were used instead of the contract terms of this service.
- Condition: the invoice's due date(s) and payment terms agree with the payment terms of the transport plan it refers to, or the plan's terms are changed so that both say the same.
- Options: (a) preferred: the invoice follows the contract: due date 2026-04-09, note quoting the agreed terms, and the 2 % discount only if the framework agreement grants it (then also in the plan); (b) change the plan's PaymentTerms to the terms the invoice applies (30 days from the invoice date, 2 %/10 days), if that is what the framework agreement says.
- Needs decision: no

### ore/06#F2 · Low · Bonus and penalty of the transport plan neither applied nor excluded
- XPath: `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `1720441`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note` = `2 % of the freight when the train is delivered on the first day of the window, so that the factory can start the blend a day early.`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10`
- Why: the plan gives a bonus of 2 % of the freight for delivery on the first day of the window and a penalty for late delivery. The invoice bills plain freight (1788.4 t × 962 = 1 720 441) with no allowance or charge and no delivery date, and no XML example of the flow states when the train arrived (02–05 carry no actual delivery or arrival date; the consignment note was issued at 11:35 on 10 March, the first day of the service window, for a run within the Province of Ferrano). So the reader cannot tell whether the 2 % bonus (34 409 XUF on 1 720 441) was earned and omitted, or not earned. It is also open which "window" is meant: the plan's service window (from 10 March) or the buyer's requested delivery period (`01-Order.xml:/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-09`), whose first day the train cannot meet.
- Condition: the flow states when the train was delivered, and the freight invoice either carries the bonus (or penalty) as a charge or allowance with its reason, or its amount is consistent with the bonus not being earned on that date.
- Options: (a) preferred: give the invoice the actual delivery date (e.g. `cac:Delivery/cbc:ActualDeliveryDate`) and, if delivered on 10 March, a charge line or AllowanceCharge for the 2 % bonus; (b) if the story says the train arrived later, the delivery date alone explains the absence of a bonus.
- Needs decision: yes (whether the bonus was earned is part of the story)

## Checked and consistent
- Line: 1788.4 × 962 = 1 720 440.8 → `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `1720441`; quantity equals the despatched quantity `04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4` and the consignment note's gross weight 1 788 400 kg.
- Tax: 20 % of 1 720 441 = 344 088.2 → `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `344088`; 1 720 441 + 344 088 = 2 064 529 = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `2064529` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `2064529`. Category S, 20 %, supply type `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES` fit a domestic freight service.
- Settlement discount: 2 % of the payable amount 2 064 529 = 41 290.58 → `41291`; settlement period 12–22 March is 10 days, as the note says.
- Payee account `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU920351041700000000523645` passes the IBAN-style check, is held in XUF, named after the seller, at the Serravona branch whose ID (`03510-41700`) is embedded in the account number; the same account is used for Ferrano Rail Cargo in rail/10-Invoice.xml. RF reference `RF09FRCINV260311` passes its check digits. RTGS channel (ISO 20022 ClearingChannel2Code) with a credit transfer (4461 code 30) is coherent.
- Penalty interest 8 % per annum (`ANN`), simple — coherent. No remittance advice for this invoice exists in the flow, which is not required.

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `41291`: suspected that the discount should be on the net amount (2 % of 1 720 441 = 34 409) — refuted: the definition ("The amount of a settlement discount offered for payment under these payment terms") does not fix the base, a cash discount on the amount paid is common practice, and 07-Invoice.xml computes it the same way.
- `/Invoice/cbc:TaxPointDate` = `2026-03-12`: suspected that the tax point should be the date the service was performed — refuted: the definition is "The date of the Invoice, used to indicate the point at which tax becomes applicable", and the invoice date is a legitimate tax point; the world's tax-point rule is outside what this review may consult.
- `/Invoice/cbc:AccountingCostCode` = `3100` with `/Invoice/cbc:AccountingCost` = `Raw materials and parts` on a freight invoice — refuted: inbound freight for raw materials is commonly booked to the raw-material cost; Valdara uses this code in all 12 XML examples that carry it.
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF09FRCINV260311` repeats `/Invoice/cac:PaymentMeans/cbc:PaymentID` — refuted as a money problem: the note tells the payer what to quote, consistent with the structured value.
