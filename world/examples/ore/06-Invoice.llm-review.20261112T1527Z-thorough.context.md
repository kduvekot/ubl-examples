# LLM review: 06-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### ore/06#F1 · High · The invoice applies the carrier's standard terms, not the terms of the referenced plan
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- Why: the invoice references the transport execution plan 03, whose payment terms for this service are "30 days net from the consignment note." (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`). The consignment note 05 is dated 2026-03-10 (`05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`), so payment is due on 2026-04-09; the invoice instead uses an identifier for standard terms ("XU-STD"), counts 30 days from its own date (2026-03-12 + 30 = 2026-04-11) and adds a settlement discount the plan does not mention. The values are valid payment terms, but not the ones agreed for this carriage.
- Condition: the invoice's payment terms and due dates are those of the plan it references (due 30 days after the consignment note), or the plan's terms say what the invoice applies.
- Options: (a) preferred: due date 2026-04-09 in PaymentTerms, PaymentMeans and DueDate, note and ID referring to the framework agreement `VI-FRC-FW-2026`, no discount unless the plan grants one; (b) change the plan's terms to the carrier's standard terms (story change).
- Needs decision: no

### ore/06#F2 · Medium · A province is given in `Region`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries"; a province is "the political or administrative division of a country" (`CountrySubentity`), as for Bayvarra's states. 104 XML examples carry "Province of Ferrano" (`grep -rl --include='*.xml'`).
- Condition: the province is in `CountrySubentity` in every address.
- Options: (a) preferred: move it; (b) rename it if it is an economic region.
- Needs decision: no

### ore/06#F3 · Low · The contacts do not fit invoicing
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Freight desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the accounting supplier's contact answers questions about the invoice (billing/accounts receivable), the accounting customer's contact receives and approves it (accounts payable). Here the carrier's operations planner and Valdara's sales order desk are given, copied from the parties' master data.
- Condition: both contacts are functions that deal with the invoice.
- Options: (a) preferred: billing contact of Ferrano Rail Cargo and accounts-payable contact of Valdara; (b) omit the contacts.
- Needs decision: no

### ore/06#F4 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: the customer's stock-exchange listing and its warehousing provider (in no role in the flow) have no use in a freight invoice. Same master data in 75 XML examples each.
- Condition: every aggregate of the parties has a use in this invoice.
- Options: (a) preferred: leave them out.
- Needs decision: no

### ore/06#F5 · Low · The two document references do not say what they are
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- XPath: `/Invoice/cac:AdditionalDocumentReference[2]/cbc:ID` = `FRC-WB-26-0310`
- Why: AdditionalDocumentReference is "a reference to an additional document associated with this document"; with only the IDs the recipient must guess that one is the transport plan (the contract basis, 03) and the other the consignment note (the proof of performance, 05).
- Condition: each reference states its kind.
- Options: (a) preferred: DocumentTypeCode (`TransportExecutionPlan`, `Waybill`) from the world's document-type list.
- Needs decision: no

## Checked and consistent
- References: `FRC-TEP-26-0307` resolves to 03 and `FRC-WB-26-0310` to 05; supplier Ferrano Rail Cargo (provider in 03, carrier in 05), customer Valdara (bill-to party in 02/03).
- Quantity: 1788.4 t, the weighed quantity of 04/05; description "from the mine siding to the factory siding" and name "ore in bulk wagons" fit the carriage.
- Arithmetic: 1788.4 × 962 = 1 720 440.8 → 1 720 441 (line, taxable, tax exclusive); 20 % = 344 088.2 → 344 088; 1 720 441 + 344 088 = 2 064 529.
- Tax: standard rate on a domestic transport service (SupplyTypeCode SERVICES), both parties Urvanian VAT-registered.

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode` = `3100`: the buyer's raw-materials cost centre on a freight invoice — refuted because inbound freight is commonly booked with the material it brings (part of the acquisition cost); the code is Valdara's cost centre (used in 12 XML examples).
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: buyer and seller repeated next to the accounting parties — refuted because the roles are defined separately in UBL and the repetition is identification only.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: share capital in an invoice — refuted because a legal mention of the share capital on commercial documents is required in several real jurisdictions (own knowledge), so it can have a reason here.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: real-time gross settlement for an ordinary supplier payment — refuted because the world's payment rail FERRA-RTGS is named and RTGS payments of this size are plausible.
