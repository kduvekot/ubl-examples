# LLM review: 07-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/07-Invoice.xml`, Git blob `a1e9b7e2c326a01d31d3b741f419d375d10a04e9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/07#F1 · High · Freight billed as bulk cargo, which the flow says it is not
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Bulk cargo down the river to the coast of Bayvarra, per tonne.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `River freight, bulk`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FB-BULK`
- Why: The item of the freight invoice is bulk cargo ("Bulk cargo down the river", "River freight, bulk"). The transport request says the consignment is not bulk (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:BulkCargoIndicator` = `false`) and the waybill carries the granulate in 120 jumbo bags (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`).
- Condition: The invoiced service describes the cargo as the transport documents do (packaged, not bulk).
- Options: Bill a service for packaged or bagged cargo (preferred); or, if Fiumella's tariff calls all loose-loaded cargo "bulk", say so without contradicting the indicator.
- Needs decision: no

### plastics/07#F2 · Medium · A province is held in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/07#F3 · Low · The waybill reference does not say what it refers to
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`
- Why: AdditionalDocumentReference is "A reference to an additional document associated with this document." It gives only the number of the waybill, with no document type; the contract the freight rests on, the transport execution plan 04 with its payment terms, is not referenced.
- Condition: Each referenced document is identified by type, and the invoice references the document that sets its terms.
- Options: Add DocumentTypeCode, and a reference to 04-TransportExecutionPlan.xml (preferred).
- Needs decision: no

### plastics/07#F4 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in a freight invoice depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/07#F5 · Low · Contacts do not fit the role the party has in this document
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Chartering desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact answers questions on the invoice (accounts receivable), not the "Chartering desk" in Operations; the accounting customer's contact receives and pays it (accounts payable), not "Customer service" in Sales.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/07#F6 · Low · Every party registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

## Checked and consistent
- 120 t × 1495 XUF = 179400 XUF, the freight charge of 06-Waybill.xml.
- Parties: Fiumella bills Rinova, the transport user and bill-to party of 03 and 04.
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890` resolves to 06-Waybill.xml.

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty` and `/Invoice/cac:SellerSupplierParty` repeating the accounting parties — refuted because the buyer and seller of the freight are the same companies.
- `/Invoice/cbc:DefaultLanguageCode` = `en` with texts tagged `en-XU` — refuted because the untagged texts (payment means description, notes) are English.
