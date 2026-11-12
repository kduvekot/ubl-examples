# LLM review: 14-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/14-Invoice.xml`, Git blob `1173f55bda6f9ffdefd8413a5ce62500697f236a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

## Checked and consistent
- Line: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `186` km × `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `240.5` per `/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1` km = 44 733.0 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `44733`; the price and quantity are in the same unit (KMT), and the description says the price is per kilometre driven loaded, tolls included.
- Totals: `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `44733` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `44733` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `44733` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `44733`; the tax subtotal's taxable amount is the same, tax 0 at 0 %.
- Payment terms: 2 % of 44 733 = 894.66, rounded to `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `895`; the settlement period runs 10 days from the issue date (`/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-04`); the due date is 30 days after issue and the same in `/Invoice/cbc:DueDate` = `2026-04-24`, `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-24` and `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-24`, matching the note "30 days net; 2 % discount when paid within 10 days."
- Payment means: `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF49THINV260165` has a valid ISO 11649 check (check_ids.py) and is the one the instruction note asks to quote; the payee account `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU320351041600000000628374` has a valid IBAN-style check, is held in XUF like the invoice, and is named after the supplier's registered name.
- The party billed is the bill-to party of the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyIdentification/cbc:ID` = `20410274`), and the waybill says the consignee pays the freight (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:CollectPaymentTerms/cbc:Note` = `The freight is paid by the consignee under its contract with the carrier.`), consistent with FCA (buyer pays main carriage).
- `/Invoice/cbc:TaxPointDate` = `2026-03-25` is the day the service ended (`/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:ActualDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-03-25`).

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O` with `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`: suspected that an Urvanian haulier's transport starting in Urvania is taxable there — refuted because it is a business-to-business transport of goods for a customer established in Bayvarra, registered for tax there (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`); under the usual general rule for B2B services the place of supply is the customer's country, so the service is outside the scope of Urvanian VAT, which is what code O ("Services outside scope of tax") and the reason text say (own knowledge of VAT practice).
- `/Invoice/cbc:AccountingCost` = `Stock purchases` (code `4410`, as on the goods order): suspected that the buyer's cost code of the goods was copied onto a freight invoice — refuted because under FCA the buyer bears the main carriage, and inbound freight is part of the cost of the inventory (IAS 2, costs of purchase include transport; own knowledge), so booking it to stock purchases is a legitimate choice of the buyer.
- `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`, the same as in `15-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD` from another seller: suspected copied terms — refuted because the world uses country standard terms (XB-STD, XL-STD, XU-STD: 13 examples carry `XU-STD`, counted with `grep -rl --include='*.xml' '<cbc:ID>XU-STD</cbc:ID>' world/examples`), and each seller links its own terms page.
- No reference to the framework contract of the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-TH-FW-2026`) on which the kilometre price presumably rests: considered as missing — refuted because the invoice's purpose does not depend on it; the waybill it references identifies the transport.

## Outside this review
- `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `LD-RA-26-0164` points to the corrected receipt advice issued 2026-03-26 10:48 (`13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `10:48:00`), the day after this invoice (`/Invoice/cbc:IssueDate` = `2026-03-25`); even the first receipt advice is later than this invoice (`11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00` on 2026-03-25). An order-of-documents question for the references (logistics) review.
