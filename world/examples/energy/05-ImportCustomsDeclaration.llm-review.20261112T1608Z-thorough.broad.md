# LLM review: 05-ImportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### energy/05#F1 · High · Same shipment ID as the export declaration, different quantity and weight
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2760000`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2940000`
- Why: `Shipment/ID` is "An identifier for this shipment". The export declaration gives shipment KG-SH-26-0154 39 200 MWh and 2 940 000 kg; this import declaration gives the same shipment 36 800 MWh and 2 760 000 kg. The difference, 2 400 MWh, is Kelpstone's sale to Ferrano Energy (07-Invoice.xml), for which no import declaration exists in the flow. One shipment cannot have two contents.
- Condition: a shipment ID describes the same goods in both declarations; the gas imported by Montebrio and the gas for Ferrano Energy are distinguishable (separate consignments or shipments), and each is imported by its importer.
- Options: (a, preferred) give Montebrio's 36 800 MWh its own consignment (ID shared with a split export declaration) and reference it here; (b) declare the whole 39 200 MWh here with both consignees, if the world lets one importer declare for both (less plausible: Ferrano Energy is the owner of its gas).
- Needs decision: yes

### energy/05#F2 · Medium · Natural gas in gaseous state classified as dry bulk cargo
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: the code means "Dry bulk"; the goods are pipeline gas (HS 271121). Same value in 04-ExportCustomsDeclaration.xml.
- Condition: the cargo type, if present, fits gas carried by pipeline.
- Options: (a, preferred) omit `CargoTypeCode`; (b) a gas/liquid-bulk code of the world list.
- Needs decision: no

### energy/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` is the language, already in `Language/ID`. 362 occurrences in 213 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'`).
- Condition: LocaleCode holds a locale (e.g. `en-XB`) or is absent.
- Options: (a, preferred) `en-XB`; (b) omit.
- Needs decision: no

### energy/05#F4 · Medium · Province given in Region
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`, which the consignor's Bayvarran address in the same document uses). World convention; 219 occurrences in 104 of 250 XML examples.
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/05#F5 · Low · Customs authority described as a company
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:ID` = `XU:CR`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`
- Why: the Customs Administration of Urvania (ISIC 8411) is registered in the commercial register and has a liquidation status, which describe a company; its contact is a generic public-service officer rather than the office handling pipeline imports. 90 public-body parties in 75 XML examples carry a liquidation status (lxml count over `*/*.xml`).
- Condition: the authority's legal-entity data fit a public body; its contact is the office that processes the declaration.
- Options: (a, preferred) drop liquidation status and commercial register for public bodies; (b) keep with a world rule.
- Needs decision: no

### energy/05#F6 · Low · No link to the export declaration or the invoice the customs value comes from
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000`
- Why: the customs value equals 06-Invoice.xml's total and the goods come under the export declaration 04-ExportCustomsDeclaration.xml, but the import declaration references neither; the period of flow (March 2026) is also only implicit in the journey ID.
- Condition: the declaration can be linked to the export declaration and to the invoice its value is based on, and states the period of flow.
- Options: (a, preferred) document references to KG-EX-26-0152 and KG-INV-26-0157 where the document allows; (b) a note.
- Needs decision: no

## Checked and consistent
- 36 800 MWh × 3 600 XUF = 132 480 000 XUF, equal to 06-Invoice.xml; weight 75 kg/MWh as in the export declaration.
- Importer = consignee = Montebrio Power; consignor Kelpstone Gas with the same data as in 04/06; classification codes as in 04.
- Pipeline transport (mode 7, means type 71) and journey KG-P1-2603 as in 04.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:IssueDate`: suspected the declared value is taken from an invoice not issued until the next day (06, 2026-04-03 11:25) — refuted: the price is fixed in the supply contract, so the value is known before the invoice is issued.
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox`: suspected a postal address mixing PO box and street — refuted: an address with both is common and the type code says postal.
