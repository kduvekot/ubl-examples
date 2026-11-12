# LLM review: 03-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/03-Invoice.xml`, Git blob `80f13e4ce6ede50f2dc64b8d628230f6cf1de513` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/03#F1 · Medium · Wholesale electricity classified as a supply of services, gas in the same flow as goods
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture." The line sells the energy itself ("Electricity fed into the grid at the power station, sold by the megawatt hour"), not a network service. VAT systems commonly treat electricity, gas, heat and the like as goods (e.g. Art. 15(1) of the EU VAT Directive; own knowledge), and the flow itself classifies the natural gas of invoices 06 and 07 as GOODS. Classifying electricity as services is inconsistent with that, unless the world's tax law says otherwise. (The network-use lines of 02 are services, correctly.)
- Condition: The supply type of the electricity sale follows one rule for energy supplies that is also applied to the gas of 06 and 07, and that rule is the one the world's tax description gives.
- Options: (a) preferred: GOODS, consistent with the gas invoices and established VAT practice; (b) keep SERVICES only if Urvanian VAT law in the world treats electricity as a service, and then say so where the tax scheme is described.
- Needs decision: yes (tax treatment)

### energy/03#F2 · Low · Customs trader number of the seller on a domestic electricity invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- Why: The invoice is a domestic sale of electricity between two Urvanian companies; no customs procedure is involved. The customs trader identifier of Montebrio Power has no use in this document and looks copied from the party's master data. The same identifier appears in the customs declarations 04 and 05, where it belongs.
- Condition: The seller carries only identifiers that this invoice uses, or the invoice's purpose explains the customs trader number.
- Options: (a) preferred: leave the customs trader identifier out of this invoice; (b) keep it only with a business reason in the story.
- Needs decision: no

## Checked and consistent
- Arithmetic: 18400 MWh × 9800 XUF = 180320000; 20 % VAT = 36064000; total 216384000; settlement discount 2 % = 4327680.
- InvoicePeriod (March 2026) matches the period of the other energy invoices of the flow.
- Seller and buyer: Montebrio Power (generator) sells to Ferrano Energy (retailer); BuyerCustomerParty and SellerSupplierParty repeat the accounting parties, which their definitions ("The buyer.", "The seller.") allow.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:PaymentRailID` = `FERRA-RTGS`: suspected data without use — refuted because it names the rail the RTGS channel code points to, which the payer needs.
