# LLM review: 04-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/04-RemittanceAdvice.xml`, Git blob `ed53a13de1ca0b9a4d9a62d8bc6c094c15743208` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### utilities/04#F1 · Medium · Province of Ferrano held in Region instead of CountrySubentity
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division, which is `CountrySubentity`. The Bayvarran addresses of the world use `CountrySubentity`. The value occurs 219 times in `Region` over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: no Urvanian address carries a province in `Region`; it is in `CountrySubentity`, or the story makes it a non-administrative region.
- Options: (a) move the value to `CountrySubentity` (preferred); (b) keep `Region` only if the province is an economic or geographic region in the story.
- Needs decision: no

### utilities/04#F2 · Low · Payer's master data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: a remittance advice tells the supplier which invoice a payment settles. Valdara's customs trader number, its share listing and its warehousing service provider play no part in that payment. The block is identical in all 75 examples with Valdara's full data.
- Condition: every identifier, listing and service provider in the payer's party has a use in this remittance advice, or is absent.
- Options: (a) drop them here (preferred); (b) keep them only with a stated reason.
- Needs decision: no

### utilities/04#F3 · Low · Payer's contact is its sales order desk, not someone who answers for the payment
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the remittance advice is issued and signed by Valdara as payer; the supplier would turn to Valdara's accounts payable or treasury with questions about the payment and the discount taken. The contact given is Valdara's sales order desk, the same in all 75 examples with Valdara's full data.
- Condition: the payer's contact is a function that deals with payments (accounts payable, treasury), and name, job title and department agree.
- Options: (a) an accounts payable contact for Valdara in the payment documents (preferred); (b) drop the contact.
- Needs decision: no

## Checked and consistent
- Valdara Industries (payer, signatory) and Ferrano Energy (payee) are the accounting customer and supplier of the invoice paid, `02-Invoice.xml` (`02-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`), and both are described as in 01–03.
- `SignatoryParty` is Valdara, the party issuing the advice; the line's `AccountingSupplierParty` and `AccountingCustomerParty` repeat the header parties with the same register numbers.
- Payer account `XU790351041600000000209458` is named after Valdara's registration name and is Valdara's account in the other flows that carry it (rail, road, tender, ore, wood); the payee account `XU080351041600000004084431` is the one invoice 02 gives, named "Ferrano Energy SUA". Both are at Crevalto Bank's Ferrano main branch `03510-41600`, matching the account digits.
- The supplier's contact (customer service) is a usual addressee for the supplier side of a payment notice.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name` = `Valdara Industries SUA`: checked whether the account holder's name is the party's registered name. It is, and it matches the legal entity's `RegistrationName`.
