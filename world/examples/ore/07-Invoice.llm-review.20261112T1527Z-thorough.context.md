# LLM review: 07-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/07-Invoice.xml`, Git blob `0e28c5a596e22d95a0c87b535ac9b772716f3863` (committed)
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

### ore/07#F1 · Medium · A province is given in `Region`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries"; a province is "the political or administrative division of a country" (`CountrySubentity`), as for Bayvarra's states. 104 XML examples carry "Province of Ferrano" (`grep -rl --include='*.xml'`).
- Condition: the province is in `CountrySubentity` in every address.
- Options: (a) preferred: move it; (b) rename it if it is an economic region.
- Needs decision: no

### ore/07#F2 · Low · The moisture deduction has no basis in the invoice
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Moisture deduction`
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.015`
- Why: the line deducts 1.5 % for moisture, but nothing in the invoice (or in the order and despatch advice it references) states a moisture content, a contractual moisture limit or the analysis it rests on: the item properties give only the iron content (62 %). The flow's only assay reference (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID` = `SM-ASSAY-26-11`) sits in the transport request to the carrier, which has no use for it, instead of here, where the deduction depends on it.
- Condition: the invoice lets the buyer verify the deduction: the measured moisture (e.g. as an item property or in the allowance reason) and/or a reference to the assay it is based on.
- Options: (a) preferred: an AdditionalDocumentReference to the assay (with its type) and a "Moisture content" item property; (b) a fuller allowance reason text naming the measured and the contractual moisture.
- Needs decision: no

### ore/07#F3 · Low · The contacts do not fit invoicing
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- Why: the accounting customer's contact receives and approves the invoice (accounts payable); Valdara's sales order desk is given. The supplier's sales office can answer about a sale, but invoices are usually queried with billing/accounts receivable. Both copied from master data, as in every ore example.
- Condition: the customer's contact is a function that deals with incoming invoices (and the supplier's one with billing, if a contact is given).
- Options: (a) preferred: Valdara's accounts-payable contact; Serravona's billing contact; (b) omit.
- Needs decision: no

### ore/07#F4 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: the customer's stock-exchange listing and warehousing provider (in no role in the flow), and the road-access conditions and coordinates of the mine, have no use in an invoice for ore. Same master data in 75 XML examples each (SecurityListing, service provider).
- Condition: every aggregate of the parties has a use in this invoice.
- Options: (a) preferred: leave them out.
- Needs decision: no

## Checked and consistent
- References: OrderReference `VI-PO-26-0304` → 01, OrderLineReference line 1 exists there; DespatchDocumentReference `SM-DA-26-0308` → 04.
- Quantity 1788.4 t = despatched quantity of 04; price 8060 XUF/t = order price of 01; item data identical to 01/04.
- Arithmetic: 1788.4 × 8060 = 14 414 504 (ItemPriceExtension and BaseAmount); 1.5 % of it = 216 217.56 → 216 218; 14 414 504 − 216 218 = 14 198 286; 20 % = 2 839 657.2 → 2 839 657; total 17 037 943.
- Dates: issued 2026-03-11, after the despatch on 2026-03-10 (FCA, delivery at hand-over to the carrier); tax point date equal to the issue date.
- Payee account and RF reference are the ones the remittance advice 08 quotes.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: "Special agreement" for a moisture deduction — refuted because a moisture deduction is a contractual price adjustment of the ore sale, which 64 covers; no UNTDID 5189 code names moisture.
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: buyer and seller repeated next to the accounting parties — refuted, separate roles in UBL, identification only.
- `/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `260111`: HS code in a domestic invoice — refuted, also used for national statistics.
- `/Invoice/cbc:AccountingCostCode` = `3100`: refuted, Valdara's raw-materials cost centre (consistent in 12 XML examples), right for ore.
