# LLM review: 03-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/03-Invoice.xml`, Git blob `80f13e4ce6ede50f2dc64b8d628230f6cf1de513` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
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

### energy/03#F1 · Medium · Electricity supplied as a service, gas in the same flow as goods
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: `SupplyTypeCode` is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture." The line is the sale of the energy itself ("Electricity fed into the grid at the power station, sold by the megawatt hour"), not of a network service. In the same flow the sale of natural gas by the MWh (06-Invoice.xml, 07-Invoice.xml) is GOODS. In established VAT practice electricity and gas are both treated as goods (own knowledge, e.g. EU VAT Directive Art. 15), and the network use in 02-Invoice.xml is the service. The two energy sales are classified differently without a stated reason in the world.
- Condition: the sale of electricity and the sale of gas have the supply type the world's tax rules give energy, and the same one unless the world says why not.
- Options: (a, preferred) GOODS for the electricity line, consistent with gas; (b) keep SERVICES and record in the world's tax story that Urvania treats electricity as a service.
- Needs decision: yes

### energy/03#F2 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`). World convention through the XU address format; 219 occurrences in 104 of 250 XML examples (`grep -rh --include='*.xml' -o '<cbc:Region>[^<]*'`).
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/03#F3 · Low · Buyer's contact is retail customer service for a wholesale purchase
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Ferrano Energy buys 18 400 MWh wholesale; its customer service in Sales serves its retail customers, not its energy procurement or accounts payable. The seller's contact (Energy trading) fits its role.
- Condition: the accounting customer's contact deals with energy procurement or payables.
- Options: (a, preferred) a procurement/accounts-payable contact; (b) omit the contact.
- Needs decision: no

### energy/03#F4 · Low · Customs-trader number of the seller on a domestic electricity invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- Why: Montebrio's customs-trader number matters for its gas imports (05-ImportCustomsDeclaration.xml), not for a domestic sale of electricity; it looks copied from master data (section 4.8).
- Condition: every identifier of the supplier has a use in this invoice.
- Options: (a, preferred) leave it out here; (b) keep it with a reason.
- Needs decision: no

## Checked and consistent
- 18 400 × 9 800 = 180 320 000 = LineExtensionAmount = TaxableAmount; VAT 20 % = 36 064 000; total 216 384 000 = PayableAmount.
- Settlement discount 2 % of 216 384 000 = 4 327 680; settlement period 10 days, due date 30 days after issue.
- RF32MPINV260151 and the payee account check digits OK (`check_ids.py`); account holder Montebrio Power SUA, branch Serravona, matches the seller's town.
- Physics: Montebrio imports 36 800 MWh of gas in March (05-ImportCustomsDeclaration.xml, 06-Invoice.xml) and sells 18 400 MWh of electricity, an efficiency of 50 %, plausible for a combined-cycle gas power station (own knowledge: about 50–60 %).
- Parties' identifiers and addresses agree with 02-Invoice.xml (Ferrano Energy) and 05/06 (Montebrio Power).

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: suspected a different digit grouping from the other parties' numbers — refuted: grouping is free text and not a semantic error.

## Outside this review
- Whether 18 400 MWh bought in March fits the retailer's network use billed in 02-Invoice.xml (431.4 MWh) is a volume question across documents.
