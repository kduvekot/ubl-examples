# LLM review: 11-RemittanceAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/11-RemittanceAdvice.xml`, Git blob `d0c26e7bbd846569482f83cb92b801d665bd1d34` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/11#F1 · Medium · A province is held in Region
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/11#F2 · Medium · A language code is held in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID `ISO 639` is the language itself and repeats Language/ID; it says nothing about the locale (language and country or region, such as the `en-XB` the examples use in languageID). All 362 LocaleCode elements in the example files carry `en` with listID `ISO 639` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*' world/examples | sort | uniq -c`).
- Condition: Every LocaleCode names a locale from a list that its listID names, or is absent.
- Options: Use a locale code (for example `en-XB` from BCP 47, with that as listID; preferred, it matches the languageID tags of the examples); or remove LocaleCode where the party's locale has no use in the document.
- Needs decision: no

### plastics/11#F3 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in a remittance advice depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/11#F4 · Low · The invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `RR-INV-26-0894`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `RR-INV-26-0894`
- Why: BillingReference/InvoiceDocumentReference is "A reference to an invoice"; the line's DocumentReference, "A reference to a document associated with this remittance advice line", names the same invoice with the same date. The second reference adds nothing.
- Condition: Each document the line settles is referenced once, in the element meant for it.
- Options: Keep the billing reference and remove the document reference (preferred).
- Needs decision: no

### plastics/11#F5 · Low · Two references to the payer's payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `RP-PAY-26-0882`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `RP-0882`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank" and PayerReference "An internal reference to the payer's order for payment"; both name the payer's payment order, here with two different values. `RP-0882` looks like a shortened purchase order number (01-Order.xml) rather than a payment order.
- Condition: The payer's payment order has one reference, or the two values are visibly different things.
- Options: Keep the payment order reference and drop PayerReference (preferred); or give PayerReference a distinct meaning.
- Needs decision: no

### plastics/11#F6 · Low · Contacts do not fit the role the party has in this document
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The payer's contact answers for the payment (accounts payable) and the payee's contact reconciles it (accounts receivable); "Order desk" and "Customer service" in Sales are the contacts for orders.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/11#F7 · Low · Every party registered on 1 January 1996
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

## Checked and consistent
- The invoice reference resolves to 10-Invoice.xml; 9984000 XUF = its payable amount; balance 0.
- Paid on 2026-05-19, before the due date 2026-05-20 and after the discount period ending 2026-04-30, so the full amount is right.
- RF reference and payee account agree with 10-Invoice.xml.

## Considered and refuted
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount`: party account in a remittance advice — refuted because Rivermouth pays from it; it is the same account as the payer account.
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF89RRINV260894` — fits the definition (a reference the payee asked to accompany the remittance).
