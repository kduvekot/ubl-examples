# LLM review: 10-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/10-Invoice.xml`, Git blob `13c4e7c68f3fa88f617d5f615a40ea35e815c2cd` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### rail/10#F1 · High · Payment terms differ from those agreed in the transport plan
- XPath: `/Invoice/cbc:DueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `2621`
- Why: The carrier and Valdara agreed "30 days net from the consignment note" (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`). The consignment note the invoice itself refers to is dated 14 April (`08-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-14`), so payment falls due on 14 May with no discount. The invoice counts 30 days from its own date (due 17 May) and offers a 2 % settlement discount that the plan does not mention.
- Condition: Due date and discount of the invoice follow the terms agreed for the transport, or the plan states the terms the invoice applies.
- Options: (a) preferred: due date 2026-05-14 and no settlement discount, as agreed; (b) change the plan's terms to the carrier's standard terms XU-STD if those are what the framework contract says.
- Needs decision: no

### rail/10#F2 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity). 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as non-administrative.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/10#F3 · Low · Outbound freight booked as raw materials
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: AccountingCostCode is "The buyer's accounting code, applied to the Invoice as a whole". Valdara buys the carriage of finished benches to its customer under DAP, an outbound distribution cost; booking it to raw materials and parts does not fit the service invoiced. (The code also equals Valdara's ISIC class 3100, which may be a coincidence.)
- Condition: The buyer's accounting code and text describe a cost centre that fits outbound freight.
- Options: (a) preferred: a distribution or outbound freight account; (b) drop both if Valdara's chart of accounts is not part of the story.
- Needs decision: no

### rail/10#F4 · Low · Contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Freight desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: In an invoice the accounting supplier's contact answers billing questions (accounts receivable) and the accounting customer's contact deals with the invoice (accounts payable). Here the carrier's operations planners and Valdara's sales order desk are given.
- Condition: The accounting parties' contacts are billing/accounts functions, or absent.
- Options: (a) preferred: accounts receivable / accounts payable contacts; (b) drop Contact.
- Needs decision: no

### rail/10#F5 · Low · Customer's warehouse provider copied into the invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The freight invoice does nothing with Valdara's warehousing provider; it is master data of the customer copied into a document that does not use it.
- Condition: ServiceProviderParty is absent from the invoice.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2 × 54 600 = 109 200 XUF = line, LineExtension and TaxExclusive amounts; 20 % of 109 200 = 21 840; 109 200 + 21 840 = 131 040 = TaxInclusive = Payable. Settlement discount 2 % of 131 040 = 2620.8, rounded 2621; settlement period 17 to 27 April = 10 days, as the note says.
- Price 54 600 XUF per container slot equals the waybill's rail freight per container (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`); two containers in the consignment.
- Reference: `FRC-WB-26-0334` resolves to the waybill (08), which documents the service invoiced. Valdara as accounting customer and buyer agrees with BillToParty in 02 and 03 and with DAP (01).
- Tax: standard rate 20 % on a service to a business established in Urvania; the XU exemption list has no exemption for transport linked to an export (only EXP for goods and SVCABROAD for customers abroad), so standard rate is consistent with the world's rules.
- Payment: RF13FRCINV260336 (ISO 11649) and the account XU92 0351 0417 0000 0000 5236 45 pass their checks (check_ids.py); branch 03510-41700 matches the bank and branch digits of the account; RTGS channel and rail FERRA-RTGS are consistent.
- Parties described as in the other rail examples.

## Considered and refuted
- `/Invoice/cbc:TaxPointDate` = `2026-04-17`: suspected a tax point that should be the date the service was completed (15 April) — refuted because the world's tax point rules are not stated as completion-based and the invoice date is a legitimate tax point for many VAT systems.
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`: suspected a reference that does not say what it refers to — refuted because the WB number prefix and the context (a freight invoice) make the waybill obvious.
