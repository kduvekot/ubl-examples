# LLM review: 03-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/03-Invoice.xml`, Git blob `80f13e4ce6ede50f2dc64b8d628230f6cf1de513` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/03#F1 · Medium · Electricity sold as a commodity classified as a supply of services, gas in the same flow as goods
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: `SupplyTypeCode` is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture." The line sells 18400 MWh of electricity "fed into the grid at the power station, sold by the megawatt hour", i.e. the energy itself, not the use of a network (which 02-Invoice.xml rightly classifies as services). In the same flow the wholesale sale of natural gas by the MWh is GOODS (06, 07). VAT practice treats electricity and gas alike, as goods (EU VAT Directive Art. 15(1), own knowledge). The question is wider than this example: the retail energy lines of utilities/02-Invoice.xml (two electricity lines and the gas line for the same 61200 kWh as 01-UtilityStatement.xml) are SERVICES too (checked in the merge: 3 SERVICES codes in that file), so the world classifies gas once as goods and once as services, and electricity as services, without a stated rule (counted by the money part: SERVICES 29, GOODS 32 occurrences over `*.xml`).
- Condition: the supply type of electricity and gas sold as energy follows one rule throughout the world, the one the world's tax description gives; network use stays services.
- Options: (a) preferred: GOODS for the electricity line here (and for the energy lines of utilities/02), consistent with 06/07 and with VAT practice; (b) keep SERVICES only if Urvanian VAT law in the world treats electricity as a service, say so where the tax scheme is described, and explain why gas differs.
- Needs decision: yes (tax treatment)
- From: broad F1, money F1, context F1

### energy/03#F2 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). World convention through the XU address format; `Province of Ferrano` occurs 219 times in 104 of the 250 `*.xml` examples, always in `cbc:Region`.
- Condition: no Urvanian address carries its province in `cbc:Region`, or the world states why it is an economic region.
- Options: (a) preferred: move the province to `CountrySubentity` (with a subentity code); (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no
- From: broad F2, parties F1

### energy/03#F3 · Low · Buyer's contact is its retail customer service for a wholesale purchase
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Ferrano Energy buys 18400 MWh of wholesale electricity; the contact of the accounting customer of such a purchase is its energy procurement/trading or accounts-payable desk, not the customer service of its Sales department, which serves the retailer's own customers. The seller's contact (`Energy trading`) fits its role.
- Condition: the accounting customer's contact deals with buying or paying for wholesale energy.
- Options: (a) preferred: a procurement or accounts-payable contact for Ferrano Energy in its wholesale purchases (also 07); (b) leave the contact out.
- Needs decision: no
- From: broad F3, parties F2

### energy/03#F4 · Low · Customs trader number of the seller on a domestic electricity invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- Why: the invoice is a domestic sale of electricity between two Urvanian companies; no customs procedure is involved. Montebrio Power's customs trader number belongs to its gas imports (04-ExportCustomsDeclaration.xml, 05-ImportCustomsDeclaration.xml) and looks copied from master data (section 4.8). Unlike the export invoices 06/07, nothing in this invoice supports a customs declaration.
- Condition: the seller carries only identifiers this invoice uses, or the invoice's purpose explains the customs trader number.
- Options: (a) preferred: leave it out of this invoice; (b) keep it only with a business reason in the story.
- Needs decision: no
- From: broad F4, context F2

### energy/03#F5 · Low · Ferrano Energy's industry classification leaves out gas
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 covers electricity; Ferrano Energy also retails gas (01-UtilityStatement.xml) and buys gas (07-Invoice.xml), which is ISIC 3520 (own knowledge). This invoice is about electricity, so the gap matters little here, but the party should be described the same way in every example (energy/01#F8, energy/02#F5).
- Condition: Ferrano Energy's classification covers its gas activity, the same way in every example of the flow, or the world states that parties carry their main activity only.
- Options: (a) preferred: add 3520 next to 3510; (b) keep the main activity only and record that rule.
- Needs decision: no
- From: parties F3

## Checked and consistent
- Arithmetic, recalculated: 18400 × 9800 = 180320000 = line, LineExtensionAmount, TaxExclusiveAmount and TaxableAmount; 20 % = 36064000 = `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `36064000`; total 216384000 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `216384000`.
- Settlement discount 2 % of 216384000 = 4327680 = `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4327680`; settlement period 10 days, due date 2026-05-03 (30 days).
- Payment: RF32MPINV260151 and the payee account pass their check digits; Montebrio's account XU720351041700000005021992 is the one that pays Kelpstone in `09-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XU720351041700000005021992`; account holder Montebrio Power SUA, branch in Serravona.
- Physics: Montebrio buys and imports 36800 MWh of gas in March (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`, `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`) and sells 18400 MWh of electricity: 50 % efficiency, plausible for a combined-cycle plant (about 50–60 %, own knowledge); average output 18400 / 744 h = 24.7 MW; fuel cost 2 × 3600 = 7200 XUF per MWh of electricity against 9800 selling price.
- Downstream: Ferrano Energy resells 431.4 MWh of electricity in utilities/02-Invoice.xml, within the 18400 MWh bought.
- Dates and units: InvoicePeriod March 2026 before the issue date 2026-04-03; MWH on quantity and base quantity.
- Parties: Montebrio Power (`XU-R-105918`) described identically here, in 05 and 09; Ferrano Energy matches 01 and 02; Buyer/Seller parties repeat the accounting parties, which their definitions allow; a power station operator with an Energy trading contact fits the seller role.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: digit grouping differs from other parties — refuted: grouping is free text, not a semantic error (from broad)
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S`: wholesale electricity between traders is often reverse-charged — refuted: that is an option of the EU directive (Art. 199a), not a rule a fictional national VAT must follow (from money)
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4327680`: discount on the amount including VAT — refuted: a legitimate reading of the element (from money)
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`: a trader as invoicing contact — refuted: for a wholesale sale the trading desk is the counterpart of the deal (from parties)
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona` with Region `Province of Ferrano`: whether Serravona lies in that province — not refutable from the XML, but every example places Montebrio there consistently (from parties)
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Electricity fed into the grid at the power station, sold by the megawatt hour.`: missing delivery or metering point — refuted: a monthly invoice for one station's feed-in to one buyer is unambiguous; place in the description, period in InvoicePeriod (from logistics)
- `/Invoice/cac:PaymentMeans/cbc:PaymentRailID` = `FERRA-RTGS`: data without use — refuted: it names the rail the RTGS channel points to, which the payer needs (from context)

## Changed in the merge
- broad F1, money F1, context F1 → F1: combined; the merge added that the retail gas line of utilities/02-Invoice.xml is also SERVICES, so gas itself is classified both ways in the world.
- broad F2, parties F1 → F2: Needs decision set to no (broad had yes); same decision across the flow.
- broad F4, context F2 → F4: combined; added why the refutation accepted for the export invoices 06/07 (in the other half of this flow's merge) does not apply here.

## Outside this review
- Whether the 18400 MWh bought in March fit the retailer's network use billed in 02-Invoice.xml (431.4 MWh) is a volume question across documents (from broad).
