# LLM review: 05-ImportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/05-ImportCustomsDeclaration.xml`, Git blob `7a7660d1d073ae04f45f02effa30b140182e1c33` (committed)
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

### energy/05#F1 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania is a public authority (ISIC 8411). The legal entity places it in the commercial register of Urvania and gives it a liquidation status ("the party's liquidation status"), which presumes a company that can be wound up; neither applies to a government agency. Over all `*.xml`, 18 `CustomsParty`/`AuthorityParty` elements in 18 files carry a liquidation status, and 18 a `COMMERCIAL` registration type (lxml counts).
- Condition: the authority's legal entity contains no commercial-register scheme and no liquidation status.
- Options: (a) preferred: reduce the authority's `PartyLegalEntity` to its registration name and the identifier under which public bodies are listed (or leave it out); (b) add a register of public bodies to the world and use it.
- Needs decision: no

### energy/05#F2 · Medium · Province held in Region
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as this document does for the consignor (`/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). 219 occurrences in 104 `*.xml` examples (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is a language code repeating `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 `*.xml` examples (lxml count).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID; (b) leave it out.
- Needs decision: no

### energy/05#F4 · Low · Importer's contact is its trading desk; customs VAT data unused
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Energy trader`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The importer is "the Party who makes the import declaration"; its contact is the one customs turns to about the declaration and the duties (customs or tax compliance), not the trader who bought the gas. The consignor's sales manager is likewise its general master-data contact. The customs authority's VAT registration plays no part in an import declaration it processes; it looks copied from master data (the Bayvarran authority in `04-ExportCustomsDeclaration.xml` carries none).
- Condition: the importer's and consignor's contacts deal with the customs formalities or the gas movement; the authority carries no tax registration the declaration does not use.
- Options: (a) preferred: customs/compliance contacts for importer and consignor, and no `PartyTaxScheme` on the authority; (b) leave the contacts out.
- Needs decision: no

### energy/05#F5 · Low · Plant's InformationURI is the company's home page
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: `Location/InformationURI` is "The Uniform Resource Identifier (URI) of a document providing information about this location"; the value repeats the party's `WebsiteURI` and is not about the gas treatment plant.
- Condition: `InformationURI` points to information about the location, or is absent.
- Options: (a) preferred: leave it out; (b) point it to a page about the plant.
- Needs decision: no

## Checked and consistent
- Importer Montebrio Power is the buyer of 36800 MWh in `06-Invoice.xml`, the same quantity imported here; its description (52 leaf values) matches 03 and 09, including the `en-XU` tags. Its customs trader ID `XU-TR-105918` matches the consignee in 04.
- Consignor Kelpstone Gas matches the exporter in 04 and the supplier in 06–09.
- `ConsigneeParty` repeats the importer by ID and name; the definition ("The Party who receives the goods.") has no "if different" condition, and the importer does receive the gas.
- The customs party is the Urvanian authority, which processes an import into Urvania; the same party (`XU-R-105507`) appears with 44 identical leaf values in ten examples of other flows.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox` = `PB 18` together with a street and building number under `AddressTypeCode` `POSTAL` — refuted because a postal address may give both the box and the office's street location; the type code says it is the address for mail.
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`: generic title — refuted because the contact name `Border office` identifies the office and title and department agree.

## Outside this review
- The flow's second buyer, Ferrano Energy (2400 MWh in `07-Invoice.xml`), has no import declaration, although `04-ExportCustomsDeclaration.xml` exports the whole 39200 MWh on the shipment ID used here; that is reported as a finding of 04 and 07.
