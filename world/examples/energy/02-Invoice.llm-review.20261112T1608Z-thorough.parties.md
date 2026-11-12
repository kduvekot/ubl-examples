# LLM review: 02-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/02-Invoice.xml`, Git blob `ca1ffa8a13476757483bcb761f1e9079132080e5` (committed)
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

### energy/02#F1 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`. Bayvarran addresses of the same flow use `CountrySubentity` (e.g. `06-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). `Province of Ferrano` occurs 219 times in 104 `*.xml` examples, always in `cbc:Region` (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity` (with a subentity code); (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/02#F2 · Low · Contacts that do not fit an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Metering office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Metering`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contacts of the accounting supplier and accounting customer of an invoice are the ones who deal with the bill: the supplier's billing or accounts-receivable desk and the customer's accounts-payable or purchasing desk. Ferrano Grid's metering office fits the utility statement (`01-UtilityStatement.xml`), not the invoice for network use; Ferrano Energy's customer service in Sales serves its own customers, not its grid supplier. The same contacts are copied unchanged from `01-UtilityStatement.xml`.
- Condition: each accounting party's contact in the invoice deals with invoicing or payment of the network charges.
- Options: (a) preferred: give each party a billing/accounts contact for this document; (b) leave the contacts out.
- Needs decision: no

### energy/02#F3 · Low · Industry classification leaves out the gas business
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is "Electric power generation, transmission and distribution". Ferrano Grid bills gas network use here (`/Invoice/cac:InvoiceLine[3]/cac:Item/cbc:Name[2]` = `Gas network use`), and Ferrano Energy retails gas (`01-UtilityStatement.xml`) and buys gas (`07-Invoice.xml`). Distribution of gaseous fuels through mains and their sale is ISIC 3520 (own knowledge). Incomplete rather than wrong.
- Condition: the classification of both parties covers their gas activity, the same way in every example of the flow.
- Options: (a) preferred: add `IndustryClassificationCode` 3520 next to 3510; (b) keep the main activity only, if that is the world's rule.
- Needs decision: no

## Checked and consistent
- Supplier Ferrano Grid and customer Ferrano Energy are described exactly as in `01-UtilityStatement.xml` (sender and receiver), and Ferrano Energy as in `03-Invoice.xml`.
- `BuyerCustomerParty` and `SellerSupplierParty` name the same parties by ID and name; their UBL definitions ("The buyer.", "The seller.") carry no "if different" condition.
- The grid operator invoices the retailer for network use of its customers (the retailer is the subscriber's supplier in 01), which fits the roles: the retailer buys the grid service.
- Payee account holder `Ferrano Grid SUA` is the accounting supplier's registration name.

## Considered and refuted
- `/Invoice/cac:AccountingCustomerParty`: whether the grid should invoice the end customer Valdara instead of the retailer — refuted because 01 shows the retailer as buyer of the grid service with the subscriber as its customer (supplier model), so Ferrano Energy is the right accounting customer.
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: a possible real BIC — refuted because the country part `XU` is not an ISO 3166 code assigned to a country, so no real BIC can have it.
