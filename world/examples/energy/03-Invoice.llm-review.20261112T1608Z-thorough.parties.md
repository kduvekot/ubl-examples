# LLM review: 03-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/03#F1 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). `Province of Ferrano` occurs 219 times in 104 `*.xml` examples, always in `cbc:Region` (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity` (with a subentity code); (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/03#F2 · Low · Buyer's contact is its customer service
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Ferrano Energy buys 18400 MWh of wholesale electricity from Montebrio Power. The contact of the accounting customer of a wholesale purchase is its energy procurement/trading or accounts-payable desk, not the customer service of its Sales department, which serves the retailer's own customers. The seller's contact (`Energy trading`) fits its role; the buyer's does not.
- Condition: the accounting customer's contact deals with buying or paying for wholesale energy.
- Options: (a) preferred: give Ferrano Energy a procurement or accounts-payable contact in its wholesale purchases (also 07); (b) leave the contact out.
- Needs decision: no

### energy/03#F3 · Low · Ferrano Energy's industry classification leaves out gas
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 covers electricity; Ferrano Energy also retails gas (`01-UtilityStatement.xml`) and buys gas (`07-Invoice.xml`), which is ISIC 3520 (own knowledge). This invoice is about electricity, so the gap matters less here, but the party description should be the same in every example.
- Condition: Ferrano Energy's classification covers its gas activity, the same way in every example of the flow.
- Options: (a) preferred: add 3520 next to 3510; (b) keep the main activity only, if that is the world's rule.
- Needs decision: no

## Checked and consistent
- Montebrio Power (`XU-R-105918`) is described identically here, in `05-ImportCustomsDeclaration.xml` (importer) and `09-RemittanceAdvice.xml` (accounting customer): same address, identifiers, legal entity and contact. Ferrano Energy matches 01 and 02.
- A power station operator (ISIC 3510, contact Energy trading, Trading department) selling electricity fed into the grid fits the seller role; the payee account holder `Montebrio Power SUA` is its registration name, and its branch is in Serravona where the company sits.
- `BuyerCustomerParty`/`SellerSupplierParty` repeat the accounting parties by ID and name; the definitions carry no "if different" condition.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`: a trader as invoicing contact — refuted because for a wholesale sale the trading desk is the counterpart of the deal and the usual contact for the invoice's content.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona` with `cbc:Region` `Province of Ferrano`: whether Serravona lies in the Province of Ferrano — not refutable from the XML alone, but every example that names Montebrio places it there consistently, so it is not a finding of this review.
