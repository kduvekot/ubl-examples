# LLM review: 10-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/10-Invoice.xml`, Git blob `13c4e7c68f3fa88f617d5f615a40ea35e815c2cd` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/10#F1 · Medium · Province in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: A province is "the political or administrative division of a country" (CountrySubentity), not a "geographic or economic region or group of countries" (Region).
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/10#F2 · Low · Buyer's cost account for raw materials on an outbound freight invoice
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: AccountingCost is "the buyer's accounting code, applied to the Invoice as a whole". The buyer is Valdara, which pays the rail freight for delivering its benches to its customer under DAP (rail/03: "Freight prepaid by the consignor under DAP"). That is an outbound freight or distribution cost, not a purchase of raw materials and parts.
- Condition: the buyer's cost account fits what is invoiced (carriage of sold goods).
- Options: (a) preferred: an outbound freight / distribution cost account of Valdara; (b) drop both.
- Needs decision: no

### rail/10#F3 · Low · Share listing and warehouse provider of the invoiced customer
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty`
- Why: The freight invoice does nothing with the customer's share listing or with its warehousing provider.
- Condition: no party data without a reason in the invoice.
- Options: (a) preferred: drop both here.
- Needs decision: no

## Checked and consistent
- 2 container slots × 54600 = 109200; VAT 20 % = 21840; total 131040; settlement discount 2 % of 131040 = 2620.8, stated 2621 (rounded): arithmetic holds.
- The invoice references the waybill (`/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`, rail/08) whose freight charge per container is 54600.
- Seller = accounting supplier (Ferrano Rail Cargo), buyer = accounting customer (Valdara): fit the bill-to party of rail/02 and rail/03.

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: suspected redundant next to the accounting customer — refuted because UBL defines the buyer as a role of its own; giving it is not a misuse.
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2`: checked unit E48 (service unit) for container slots — fits.
