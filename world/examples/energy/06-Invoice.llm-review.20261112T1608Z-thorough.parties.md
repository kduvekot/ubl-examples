# LLM review: 06-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/06-Invoice.xml`, Git blob `7c0dad8fdbb0040b1dab2a0e3035fb59f281af39` (committed)
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

### energy/06#F1 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is a language code repeating `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 `*.xml` examples (lxml count).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID; (b) leave it out.
- Needs decision: no

### energy/06#F2 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the supplier's bank address in this invoice does (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). 219 occurrences in 104 `*.xml` examples (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/06#F3 · Low · The customer's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The English renderings of Montebrio Power's street and town carry `languageID="en-XB"`, while the same texts are `en-XU` in `03-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`, in 05 and in 09; the legal form, given in `qau` and `en-XU` there, is one untagged text here. The tag follows the issuer's country rather than the rendering. 107 Urvanian addresses in 39 `*.xml` files carry an `en-XB` rendering (lxml count).
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag Urvanian names' English renderings `en-XU` and keep the `qau` legal form; (b) record an issuer-locale rule and apply it consistently.
- Needs decision: no

### energy/06#F4 · Low · Kelpstone's plant location copied into the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: The invoice bills gas measured at the border station; the location of the producer's treatment plant plays no part in it and looks copied from master data. Its `InformationURI` ("a document providing information about this location") is moreover the company's home page, the same as `WebsiteURI`.
- Condition: the supplier carries no physical location the invoice does not use; any `InformationURI` is about the location itself.
- Options: (a) preferred: leave `PhysicalLocation` out of the commercial documents (06–09) and keep it in the customs documents, without the home-page URI; (b) keep it only with a reason in the invoice.
- Needs decision: no

## Checked and consistent
- Supplier Kelpstone Gas and customer Montebrio Power are the exporter/consignor and the importer of 04/05; Montebrio buys exactly the 36800 MWh it imports in `05-ImportCustomsDeclaration.xml`.
- Kelpstone's description is identical in 04–09 (59 leaf values); Montebrio's identifiers, legal entity, tax scheme and contact match 03, 05 and 09 apart from the language tags of F3.
- Seller contact (Gas sales, Commercial) fits the seller of a gas supply; buyer contact (Energy trading) fits the buyer of wholesale gas. `BuyerCustomerParty`/`SellerSupplierParty` repeat the accounting parties; their definitions have no "if different" condition.
- Payee account holder `Kelpstone Gas Ltd` is the supplier's registration name; the bank branch is in Gullhaven where the supplier sits.
