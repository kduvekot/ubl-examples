# LLM review: 02-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/02-Invoice.xml`, Git blob `b2993194ed77fe144060459952d69428ed29f5bc` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/02#F1 · Medium · Province of Ferrano held in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located"; a province is "the political or administrative division of a country", which is `CountrySubentity`. The Bayvarran addresses of the world use `CountrySubentity` for their states. The value occurs 219 times in `Region` over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: no Urvanian address carries a province in `Region`; the province is in `CountrySubentity` (and its code in `CountrySubentityCode` if the world defines one), or the story makes it a non-administrative region.
- Options: (a) move the value to `CountrySubentity` (preferred: it is what the definition names); (b) keep `Region` only if the province is an economic or geographic region in the story.
- Needs decision: no

### utilities/02#F2 · Medium · OriginatorParty used for the consumer of a line, not for the party who originated an order
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: UBL defines `InvoiceLine/OriginatorParty` as "The Party who originates the Order to which the Invoice is related." Line 2 bills the electricity of the warehouse meter under Valdara's supply contract (`/Invoice/cac:PurchaseReference/cbc:ID` = `FE-C-0047120`, "Supply contract"); `03-UtilityStatement.xml` says the supply is "under the customer's contract" with Valdara as `UtilityCustomerParty`. Nothing in the flow says Castrano Logistics ordered anything: it is the party at whose warehouse the electricity is consumed. The element is therefore used for a role (consumer, occupant of the delivery point) its definition does not have.
- Condition: line 2 names Castrano Logistics only in an element whose definition fits its role (e.g. the party the supply is delivered to), or the story says Castrano originated the order for this connection.
- Options: (a) replace `OriginatorParty` by `cac:Delivery/cac:DeliveryParty` on line 2, next to the delivery location (preferred: the definition "the party to whom goods should be delivered" fits the occupant of the consumption point); (b) keep `OriginatorParty` and make the story say that Castrano requested the warehouse connection under Valdara's contract.
- Needs decision: no

### utilities/02#F3 · Low · Customer's master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: a domestic electricity and gas invoice has no customs aspect and no use for the customer's share listing. The block is identical in all 75 examples that carry Valdara's full data, which suggests copied master data.
- Condition: every identifier and listing in the customer party has a use in this invoice, or is absent.
- Options: (a) drop the customs trader ID and the security listing here (preferred); (b) keep them only with a stated reason.
- Needs decision: no

### utilities/02#F4 · Low · Customer's contact is its sales order desk, not someone who handles supplier invoices
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the accounting customer's contact is the one who receives and settles the invoice (accounts payable). Valdara's contact here is the sales order desk with a customer service officer, the contact Valdara gives its own customers; it is the same in all 75 examples with Valdara's full data, whatever role Valdara has.
- Condition: the accounting customer's contact deals with incoming invoices (or utilities purchasing), and name, job title and department agree.
- Options: (a) an accounts payable contact for Valdara in the billing documents of this flow (preferred); (b) drop the contact.
- Needs decision: no

### utilities/02#F5 · Low · Delivery location of line 2 is a company name without the place's address or ID
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Castrano Logistics warehouse, Ferrano`
- Why: a location should name the place, not the company, and identify it where the same place is identified elsewhere. `03-UtilityStatement.xml` identifies the same consumption point (`03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID` = `FE-CP-4160-07`) with its address (Via del Magazzino 24, 4130 Ferrano). The invoice line only carries a description built on the company's name, so the line cannot be linked to the consumption point except through the meter number.
- Condition: the delivery location of line 2 identifies the warehouse consumption point (its ID and/or address) as statement 03 does.
- Options: (a) add the consumption point ID and the address to the delivery location (preferred); (b) describe the place itself ("Warehouse, Via del Magazzino 24, Ferrano") if no ID is wanted.
- Needs decision: no

## Checked and consistent
- Ferrano Energy (supplier and seller) and Valdara Industries (accounting customer and buyer) are described identically in 01–04 and in every other example with their full data.
- `BuyerCustomerParty` and `SellerSupplierParty` repeat the accounting parties; UBL defines them without a condition ("The buyer.", "The seller."), so stating them explicitly follows the rule that nothing is implied by absence.
- Payee account `XU080351041600000004084431` is named "Ferrano Energy SUA", the supplier's registration name; its branch code `03510-41600` matches the account's bank and branch digits (0351 0416 00); the same account is the payee account in `04-RemittanceAdvice.xml`.
- Castrano Logistics' register number `XU-R-104411` on line 2 matches the party in statement 03 and in Valdara's service provider entry.
- `ServiceProviderParty` of the customer (Castrano, warehousing and despatch) has a reason here: line 2 bills the warehouse that Castrano runs for Valdara.

## Considered and refuted
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`: suspected as copied master data. Refuted for this invoice: it explains why Valdara pays for the electricity of Castrano's warehouse on line 2.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: a billing contact in Sales was suspected as unfitting. Refuted: for a supplier, customer service in the sales organisation is a usual contact for questions about an invoice.
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: a real BIC was suspected. Refuted: the country part `XU` is not an ISO 3166 code, so no real BIC can have this form.
