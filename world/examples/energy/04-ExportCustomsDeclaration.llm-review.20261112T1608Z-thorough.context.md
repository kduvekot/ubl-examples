# LLM review: 04-ExportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/04-ExportCustomsDeclaration.xml`, Git blob `d23054c9c05d2dbe62a877d4d23f4891f2983d71` (committed)
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

### energy/04#F1 · High · Whole export consigned to Montebrio, but the flow sells part of it to Ferrano Energy and imports a smaller quantity under the same shipment
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `2940000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- Why: ConsigneeParty is "The Party who receives the goods." The export declaration consigns 39200 MWh to Montebrio Power alone. The flow sells 36800 MWh of this gas to Montebrio (06) and 2400 MWh to Ferrano Energy (07): 36800 + 2400 = 39200, so 2400 MWh of the declared quantity are received by a party the declaration does not name. The import declaration 05 uses the same shipment identifier KG-SH-26-0154 for 36800 MWh and 2760000 kg, so one shipment has two different contents in the flow. (Weights are proportional: 75 kg/MWh in both.)
- Condition: The quantity and consignee(s) of the export declaration match the sales of the flow, and every shipment identifier describes the same goods in every example that carries it.
- Options: (a) preferred: declare two consignments (or goods items) under the shipment, 36800 MWh to Montebrio and 2400 MWh to Ferrano Energy, and give each import its own declaration (Ferrano Energy's import of 2400 MWh is then a new document); (b) declare only the 36800 MWh for Montebrio here and give the 2400 MWh for Ferrano Energy its own export and import declarations; (c) if Montebrio imports the whole 39200 MWh and resells 2400 MWh to Ferrano Energy, the invoices 06/07 must show that chain instead. Option (a) keeps the single pipeline movement.
- Needs decision: yes (documents of the flow and who receives the gas)

### energy/04#F2 · Medium · Cargo type "Dry bulk" for natural gas in a pipeline
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: CargoTypeCode is "A mutually agreed code signifying the type of cargo for purposes of commodity classification." The world list defines BULK as "Dry bulk: Loose dry goods such as ore or grain, poured into the hold". The goods are natural gas in gaseous state (HS 271121) moved by pipeline (transport mode 7, means 71); there is no hold and nothing dry or loose. The code exists but does not mean what is carried. The list has no code for gas.
- Condition: The commodity classification carries no cargo type, or a cargo type whose meaning covers gas in a pipeline.
- Options: (a) preferred: leave CargoTypeCode out for pipeline gas (HS code and transport mode already describe it); (b) add a code for gaseous bulk to the world's CargoTypeCode list, if a cargo type is wanted.
- Needs decision: no

### energy/04#F3 · Medium · A language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID ISO 639 is a language, the same value as Language/ID; it says nothing about the locale (Bayvarra). The element carries a code other than the one its definition names. The same value occurs 362 times in 213 of 250 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: LocaleCode is absent or holds a locale (language and region, e.g. a BCP 47 tag such as en-XB, with a matching listID).
- Options: (a) preferred: a locale such as `en-XB`, which matches the languageID used for English renderings in the world; (b) leave LocaleCode out where the locale adds nothing.
- Needs decision: no

### energy/04#F4 · Medium · No period or date of the pipeline movement
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: The declaration covers a quantity of gas (39200 MWh) that flowed through a pipeline over time, yet nothing states when: no ShipmentStage/TransitPeriod ("The period during which this shipment stage actually took place"), no Note. Only the JourneyID suggests March 2026. A customs declaration of a continuous flow depends on its period (it is what makes the quantity meaningful and what links it to the March invoices 06 and 07).
- Condition: The declaration states the period of the declared flow (2026-03-01 to 2026-03-31 if the invoices are right) in a structured element.
- Options: (a) preferred: ShipmentStage/cac:TransitPeriod with StartDate and EndDate; (b) a Note stating the period, as a weaker alternative.
- Needs decision: no

## Checked and consistent
- Customs value: 1411200 XBL / 39200 MWh = 36 XBL/MWh; at the rate of 06 (1 XBL = 100 XUF) this is 3600 XUF/MWh, the price of `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600`.
- Physics: 2940000 kg for 39200 MWh is 13.3 kWh/kg, within the range of natural gas (about 13–15 kWh/kg gross calorific value; own knowledge).
- Transport: mode 7 (fixed transport installations) and means type 71 (pipeline) agree with each other and with the item description ("measured at the border station").
- HS 271121 (natural gas, gaseous), section V and CPC 12020 agree with each other and with the item.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelpstone Gas`: suspected that the exporter is not the carrier of a pipeline — refuted because a producer can operate its own export pipeline; whether it does is a question for the logistics part.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`: suspected data the declaration does not use, and a distance that does not fit the origin coordinates (39°49.80'S 15°16.20'W vs. 39°52.80'S 15°18.00'W, about 6.1 km) — refuted because in an export declaration the plant is the place the goods leave the producer, and the OriginAddress is a grid cell reference whose coordinates need not be the platform itself.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `KG-CD-26-0153`: suspected confusion with the document ID — refuted because the definition ("An identifier associated with customs related procedures") allows a separate procedure number.
