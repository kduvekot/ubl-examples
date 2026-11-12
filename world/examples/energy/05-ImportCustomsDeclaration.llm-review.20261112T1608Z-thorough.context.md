# LLM review: 05-ImportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

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

### energy/05#F1 · High · Same shipment as the export declaration, different quantity and weight
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2760000`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2940000`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- Why: The import declaration and the export declaration identify the same shipment (KG-SH-26-0154) but describe different goods: 36800 MWh / 2760000 kg here, 39200 MWh / 2940000 kg there. The difference, 2400 MWh, is the gas sold to Ferrano Energy in 07, for which the flow has no import declaration. A shipment identifier must describe the same goods wherever it is used; as it stands, either this declaration under-declares the shipment or the export declaration consigns gas to Montebrio that Montebrio does not receive.
- Condition: The shipment identifier, quantity and weight of this declaration agree with the export declaration, and every quantity exported in the flow is imported under a declaration naming its actual importer.
- Options: (a) preferred: keep 36800 MWh here but as Montebrio's part of a shipment that the export declaration splits into two consignments (36800 MWh Montebrio, 2400 MWh Ferrano Energy), with a separate import declaration by Ferrano Energy; (b) give each buyer's gas its own shipment identifier in both directions; (c) Montebrio imports all 39200 MWh and resells 2400 MWh, which changes invoice 07.
- Needs decision: yes (documents of the flow and who imports the gas)

### energy/05#F2 · Medium · Cargo type "Dry bulk" for natural gas in a pipeline
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: CargoTypeCode is "A mutually agreed code signifying the type of cargo for purposes of commodity classification." The world list defines BULK as "Dry bulk: Loose dry goods such as ore or grain, poured into the hold". The goods are gaseous natural gas (HS 271121) in a pipeline (mode 7, means 71). The code does not mean what is carried; the list has no code for gas.
- Condition: No cargo type, or one whose meaning covers gas in a pipeline.
- Options: (a) preferred: leave CargoTypeCode out; (b) add a gaseous bulk code to the world list.
- Needs decision: no

### energy/05#F3 · Medium · A language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` (ISO 639) is the language itself, repeating Language/ID, not a locale. The same value occurs 362 times in 213 of 250 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: LocaleCode is absent or holds a locale (e.g. en-XB).
- Options: (a) preferred: `en-XB`, matching the languageID of English renderings in the world; (b) leave it out.
- Needs decision: no

### energy/05#F4 · Medium · No period or date of the imported flow
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: The declaration imports 36800 MWh that flowed over a period, but no element states when (no ShipmentStage/TransitPeriod, "The period during which this shipment stage actually took place", no Note). Only the JourneyID hints at March 2026. The period is what ties the declared quantity to the March invoice 06 on which the customs value rests.
- Condition: The declaration states the period of the imported flow in a structured element.
- Options: (a) preferred: ShipmentStage/cac:TransitPeriod 2026-03-01 to 2026-03-31; (b) a Note, as a weaker alternative.
- Needs decision: no

### energy/05#F5 · Low · Customs value without a reference to the invoice it comes from
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000`
- XPath: `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`
- Why: The declared customs value is exactly the amount of Kelpstone's invoice KG-INV-26-0157 (06), i.e. a transaction value, but the declaration does not name the invoice. ImportCustomsDeclaration offers AdditionalDocumentReference ("A reference to additional documents related to or relevant for this customs declaration") for this; customs authorities ask for the commercial invoice behind a transaction value.
- Condition: The commercial invoice behind the customs value can be identified from the declaration.
- Options: (a) preferred: cac:AdditionalDocumentReference with ID KG-INV-26-0157 and a type code for a commercial invoice; (b) leave it if the world's customs profile does not reference invoices (then say so in the profile).
- Needs decision: no

## Checked and consistent
- Customs value: 36800 MWh × 3600 XUF = 132480000 XUF, equal to invoice 06 (line, total, payable).
- Physics: 2760000 kg / 36800 MWh = 75 kg/MWh (13.3 kWh/kg), the same ratio as in 04 and plausible for natural gas.
- Parties: ImporterParty and ConsigneeParty both Montebrio Power (importer and receiver of the gas, as in 06); ConsignorParty Kelpstone Gas (the seller of 06).
- Transport: mode 7 and means type 71 (pipeline) agree with each other and with 04.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`: suspected a repetition of ImporterParty without a reason — refuted because the definitions differ (the declarant/owner vs. "The Party who receives the goods") and both are relevant to customs; the short form (ID and name only) avoids repeating the detail.
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`: suspected copied master data — refuted because the consignor's dispatch site is relevant to an import declaration.
