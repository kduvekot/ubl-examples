# LLM review: 10-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

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

### rail/10#F1 · Medium · Province in Region of three Urvanian addresses
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"); the flow's Bayvarran addresses do so (`11-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/10#F2 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/10#F3 · Low · Supplier's contact on the invoice is the freight operations desk
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Freight desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- Why: Section 5: the contact fits the role. On an invoice the accounting supplier's contact answers questions about the bill and the payment (accounts receivable, billing). An operations planner on the freight desk plans trains; the same contact is used for Ferrano Rail Cargo in every role in the flow.
- Condition: the accounting supplier's contact is Ferrano Rail Cargo's billing or accounts-receivable function.
- Options: (a) a billing contact (preferred); (b) role-specific contacts in the carrier's master data.
- Needs decision: no

### rail/10#F4 · Low · Customer's contact on the invoice is the sales order desk
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact handles the invoice and its payment (accounts payable) or, as buyer of the freight, transport purchasing. Valdara's order desk takes Valdara's customer orders.
- Condition: the accounting customer's contact is Valdara's accounts-payable or transport-purchasing function.
- Options: (a) an accounts-payable contact (preferred); (b) role-specific contacts in Valdara's master data.
- Needs decision: no

### rail/10#F5 · Low · Customer master data the freight invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- Why: Section 4.8: a freight invoice from the carrier does nothing with the customer's stock-exchange listing, share capital or warehousing provider.
- Condition: every legal-entity and service-provider element of the customer has a purpose in the invoice.
- Options: (a) drop them here (preferred); (b) keep share capital only where the world's invoicing rules require it for the supplier (not the customer).
- Needs decision: no

## Checked and consistent
- Accounting supplier and seller Ferrano Rail Cargo (`XU-R-104685`), accounting customer and buyer Valdara (`XU-R-104274`): Valdara is the bill-to party of the request and plan (`02-TransportExecutionPlanRequest.xml`, `03-TransportExecutionPlan.xml`) and the consignor of the waybill referenced (`08-Waybill.xml`), consistent with DAP.
- Both parties' full descriptions are identical to the other examples of the flow; both are registered for national VAT in Urvania, matching the domestic standard-rated service.
- Payee account name `Ferrano Rail Cargo SRU` equals the supplier's registration name; the account's branch is in Serravona, the supplier's town; the account (IBAN-like) and the RF payment reference have correct check digits; BIC-like `CREVXUFR` carries the user-assigned country code XU, so it is not a real BIC.
