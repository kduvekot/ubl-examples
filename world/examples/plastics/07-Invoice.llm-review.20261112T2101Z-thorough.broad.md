# LLM review: 07-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/07-Invoice.xml`, Git blob `a1e9b7e2c326a01d31d3b741f419d375d10a04e9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/07#F1 · High · Freight invoiced as bulk cargo, but the goods travelled in jumbo bags
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `River freight, bulk`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Bulk cargo down the river to the coast of Bayvarra, per tonne.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FB-BULK`
- Why: The invoiced service is bulk river freight, but the consignment is not bulk: the request says so (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:BulkCargoIndicator` = `false`), and the waybill the invoice refers to describes 120 jumbo bags (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`). The invoice contradicts the documents of the transport it bills.
- Condition: the invoiced service describes the carriage as it took place (bagged cargo, 120 jumbo bags), consistent with `03` and `06`.
- Options: (a) a freight item for bagged/general cargo (preferred); (b) if Fiumella's tariff item is called "bulk" for any dry cargo per tonne, say that in the description so it does not contradict the waybill.
- Needs decision: no

### plastics/07#F2 · High · Payment terms differ from the agreed transport plan
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cbc:DueDate` = `2026-05-22`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- Why: The plan under which the carriage was agreed sets `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` With the consignment note of 2026-04-19 (`06-Waybill.xml`, referenced by this invoice) payment is due 2026-05-19 without discount. The invoice applies 30 days from its own date (due 2026-05-22) and grants a 2 % settlement discount, using generic terms (`XU-STD`, the same ID and text as in the goods invoice of another seller, `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`).
- Condition: the invoice's payment terms (start, period, discount, due date) are those of the transport plan, or the plan says the carrier's standard terms apply.
- Options: (a) due 2026-05-19, no discount, terms text from the plan (preferred: the plan is the contract basis); (b) change the plan's terms if the standard terms were agreed.
- Needs decision: no

### plastics/07#F3 · Medium · Province of Urvanian addresses in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/07#F4 · Low · Standard VAT on the international carriage of exported goods
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `20`
- Why: The service is the carriage of goods being exported from Urvania to Bayvarra (`05-ExportCustomsDeclaration.xml`), and the goods themselves are invoiced as a VAT-free export (`10-Invoice.xml`, category `G`). In most VAT systems the transport of goods directly connected with their export is zero-rated or exempt (e.g. EU VAT Directive art. 146(1)(e); own knowledge). Standard 20 % Urvanian VAT may be what the world's tax rules intend, but it is a tax-treatment judgment this review cannot settle.
- Condition: the tax category and rate of the freight follow the world's rule for international carriage of exported goods, and that rule is recorded.
- Options: (a) zero-rate or exempt the freight with an exemption reason for transport linked to export (preferred if the world follows common VAT practice); (b) keep 20 % and record in the world's tax rules that such carriage is taxable in Urvania.
- Needs decision: yes

### plastics/07#F5 · Low · Reference to the waybill with only an ID; contract not referenced
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`
- Why: The reference does not say it is the consignment note, and the invoice does not refer to the transport contract or plan (`RR-FB-FW-2026`, `FB-TEP-26-0886`) whose terms it applies.
- Condition: the waybill reference has its document type; the agreement whose terms are billed is referenced.
- Options: (a) add `DocumentTypeCode` to the waybill reference and a contract document reference (preferred); (b) at least the type.
- Needs decision: no

### plastics/07#F6 · Low · Contacts are operations and sales, not accounts
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Chartering desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: For an invoice the supplier's contact answers billing questions and the customer's contact handles payables; here they are the carrier's chartering desk (operations planner) and Rinova's sales customer service.
- Condition: the accounting parties' contacts are accounting functions.
- Options: accounting contacts in billing documents (preferred).
- Needs decision: no

### plastics/07#F7 · Low · Waste-recovery permit in a freight invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The customer's waste-recovery permit plays no part in billing the freight; master data copied into a document that does not use it.
- Condition: no permit in the invoice.
- Options: remove it (preferred).
- Needs decision: no

### plastics/07#F8 · Low · Both companies registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for both companies (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 120 t × 1 495 XUF = 179 400 XUF (= freight in `06-Waybill.xml`); VAT 20 % = 35 880; total 215 280 = tax-inclusive = payable; settlement discount 2 % × 215 280 = 4 305.6 → 4 306 XUF (on the gross amount); settlement period 2026-04-22 to 2026-05-02 = 10 days.
- `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF45FBINV260891` has a valid ISO 11649 check (`check_ids.py`), and the payee account `XU590351041620000000733103` passes its check; account holder Fiumella Barges SRU, Ferra account for a Ferra invoice.
- Parties: supplier Fiumella, customer Rinova = the bill-to party of the plan; CPT makes the seller (Rinova) pay the freight.
- Tax point 2026-04-22 = day of discharge (`04`/`06`), service completed.

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat the accounting parties — refuted: allowed and harmless; they are the same parties.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a payment of 215 280 XUF — refuted: a legitimate choice of channel.
