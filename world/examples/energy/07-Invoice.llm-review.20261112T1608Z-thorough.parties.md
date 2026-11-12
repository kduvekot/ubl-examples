# LLM review: 07-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/07-Invoice.xml`, Git blob `c9439fcedf37997f7173ad361e9246f5cc5439d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### energy/07#F1 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is a language code repeating `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 `*.xml` examples (lxml count).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID; (b) leave it out.
- Needs decision: no

### energy/07#F2 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the supplier's bank address in this invoice does (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). 219 occurrences in 104 `*.xml` examples (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/07#F3 · Low · Ferrano Energy imports gas, but no customs declaration names it
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- Why: Kelpstone (Bayvarra) sells Ferrano Energy (Urvania) 2400 MWh of March gas measured at the border station, so Ferrano Energy is the receiver and importer of that gas. The flow's export declaration names only Montebrio as consignee, for 39200 MWh, which includes these 2400 MWh (39200 − 36800), and its only import declaration is Montebrio's for 36800 MWh. The buyer of this invoice therefore cannot be linked to the customs documents that should cover its gas (the contradiction itself is finding F1 of `04-ExportCustomsDeclaration.xml`).
- Condition: the 2400 MWh sold here are covered by customs documents that name Ferrano Energy as consignee and importer (or the story states who else imports them).
- Options: (a) preferred: add Ferrano Energy as consignee for its share in the export and an import declaration by Ferrano Energy; (b) let Montebrio import all gas and resell, changing this invoice's story.
- Needs decision: yes

### energy/07#F4 · Low · The customer's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Ferrano Energy's English address renderings carry `languageID="en-XB"`, while the same texts are `en-XU` in `02-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`, in 01 and in 03; the legal form, given in `qau` and `en-XU` there, is one untagged text here. 107 Urvanian addresses in 39 `*.xml` files carry an `en-XB` rendering (lxml count).
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag Urvanian names' English renderings `en-XU` and keep the `qau` legal form; (b) record an issuer-locale rule and apply it consistently.
- Needs decision: no

### energy/07#F5 · Low · Buyer's contact is its customer service
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Ferrano Energy buys wholesale gas here; the contact of the accounting customer is its procurement/trading or accounts-payable desk, not the customer service of its Sales department. Montebrio, buying the same gas in 06, gives its trading desk.
- Condition: the accounting customer's contact deals with buying or paying for wholesale gas.
- Options: (a) preferred: a procurement or accounts-payable contact (also in 03); (b) leave the contact out.
- Needs decision: no

### energy/07#F6 · Low · Industry classification of the gas buyer leaves out gas
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 covers electricity; Ferrano Energy buys gas here for its gas customers (01), which is ISIC 3520 (own knowledge).
- Condition: Ferrano Energy's classification covers its gas activity, the same way in every example.
- Options: (a) preferred: add 3520 next to 3510; (b) keep the main activity only, if that is the world's rule.
- Needs decision: no

### energy/07#F7 · Low · Kelpstone's plant location copied into the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: The plant's location plays no part in billing gas measured at the border station and looks copied from master data; the `InformationURI` ("a document providing information about this location") is the company home page, as in `WebsiteURI`.
- Condition: the supplier carries no physical location the invoice does not use; any `InformationURI` is about the location itself.
- Options: (a) preferred: leave `PhysicalLocation` out of 06–09; (b) keep it only with a reason in the invoice.
- Needs decision: no

## Checked and consistent
- Kelpstone Gas is described identically in 04–09 (59 leaf values); Ferrano Energy's identifiers, legal entity data, tax scheme and contact match 01, 02 and 03 apart from the language tags of F4.
- `BuyerCustomerParty`/`SellerSupplierParty` repeat the accounting parties; no "if different" condition.
- Payee account holder `Kelpstone Gas Ltd` is the supplier's registration name.
