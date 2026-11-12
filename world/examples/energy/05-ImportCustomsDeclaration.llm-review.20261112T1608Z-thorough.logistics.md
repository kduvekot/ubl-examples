# LLM review: 05-ImportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### energy/05#F1 · High · Shipment KG-SH-26-0154 has another quantity and weight in the export declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2760000`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2940000`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- Why: `Shipment/cbc:ID` is "an identifier for this shipment". The import declares shipment KG-SH-26-0154 with 36800 MWh and 2 760 000 kg; the export declaration gives the same shipment 39200 MWh and 2 940 000 kg, with Montebrio Power as sole consignee. The difference, 2400 MWh and 180 000 kg (75 kg per MWh in both), is the gas Kelpstone Gas sells to Ferrano Energy (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`). The importer's quantity agrees with its own invoice (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`), but the shared shipment identifier makes the two declarations contradict each other.
- Condition: the shipment identifier in this declaration stands for exactly the quantity and weight imported here, in this declaration and in every other example that uses it.
- Options: (a) preferred: split the export in `04-ExportCustomsDeclaration.xml` into the two buyers' parts, so that this declaration's shipment or consignment is Montebrio's part; (b) give this import its own shipment identifier and relate it to the export shipment as part of it.
- Needs decision: yes

### energy/05#F2 · Medium · Natural gas in a pipeline is declared as dry bulk cargo
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: the world's CargoTypeCode list defines BULK as "Dry bulk: loose dry goods such as ore or grain, poured into the hold". The goods are natural gas carried by pipeline (`TransportModeCode` 7, `TransportMeansTypeCode` 71); the code's meaning does not fit. The list has no code for gas, and LIQUID ("liquids in tanks") does not fit either. The same code is in `04-ExportCustomsDeclaration.xml` (counted over `world/examples/*/*.xml`: BULK with natural gas only in these two examples).
- Condition: the cargo type code of the gas means gaseous bulk or pipeline cargo, or there is no cargo type code.
- Options: (a) preferred: add a code for gaseous bulk to the world's CargoTypeCode list and use it in both declarations; (b) leave `CargoTypeCode` out.
- Needs decision: no

### energy/05#F3 · Medium · The declaration does not say for which period the gas was imported, nor where it entered Urvania
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description` = `Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.`
- Why: issued 2026-04-02, the declaration covers 36800 MWh that already flowed through the pipeline, i.e. the flow of March 2026 (the period of `06-Invoice.xml`). Nothing states that period (no `ShipmentStage/cac:TransitPeriod`), and nothing states where the gas entered Urvania, although the item text names the border station as the measuring point; the only hint is the identifier KG-P1-2603. Without period and entry point the declared quantity cannot be checked against the border metering.
- Condition: the declaration states the period of the imported flow and the place of entry (border station).
- Options: (a) preferred: `ShipmentStage/cac:TransitPeriod` 2026-03-01 → 2026-03-31 and the border station as a location of the stage or as `Shipment/cac:FirstArrivalPortLocation`, because these are the dedicated elements; (b) at least the period.
- Needs decision: no

### energy/05#F4 · Low · JourneyID carries a month's flow, not a service schedule
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: UBL defines `TransportMeans/JourneyID` as "an identifier for the regular service schedule of this means of transport". The value reads as pipeline 1, March 2026 (suffix 2603 as in the flow's other monthly identifiers), one month's flow rather than a schedule of the pipeline. The same value is in `04-ExportCustomsDeclaration.xml`.
- Condition: `JourneyID` identifies a regular schedule of the pipeline, or is absent; the period is stated where F3 asks.
- Options: (a) preferred: leave `JourneyID` out and identify the pipeline itself; (b) keep it if the story gives the pipeline a monthly flow schedule with this number.
- Needs decision: no

### energy/05#F5 · Low · The consignor's location text says four kilometres to the field; the field's coordinates are 6.1 km away
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- Why: calculated: plant 39°52.80′ S 15°18.00′ W (this example), field 39°49.80′ S 15°16.20′ W (`04-ExportCustomsDeclaration.xml`, `06-Invoice.xml`, `07-Invoice.xml`): Δ latitude 5.56 km, Δ longitude 1.80′ × cos 39.85° = 2.56 km, distance 6.1 km. The description says four kilometres.
- Condition: the distance in the description agrees with the coordinates of plant and field.
- Options: (a) preferred: "about six kilometres out"; (b) move the field's coordinates.
- Needs decision: no

## Checked and consistent
- Weight against energy: 2 760 000 kg / 36800 MWh = 75 kg per MWh = 48.0 MJ/kg, plausible for pipeline natural gas (pure methane 55.5 MJ/kg gross; with ethane and some nitrogen about 50 MJ/kg; own knowledge); goods item and shipment weights agree.
- Value: 36800 MWh × 3600 XUF = 132 480 000 XUF = `06-Invoice.xml` payable amount and the declared customs value.
- Quantity against `06-Invoice.xml`: 36800 MWh, same item (KG-NG, HS 271121, origin XB).
- Parties for the transport: consignor Kelpstone Gas and consignee/importer Montebrio Power agree with `04-ExportCustomsDeclaration.xml`.
- Codes: `TransportModeCode` 7 and `TransportMeansTypeCode` 71 (pipeline) fit; HS 271121, section V and CPC 12020 fit natural gas.
- Physics downstream: 36800 MWh of gas against 18400 MWh of electricity sold in `03-Invoice.xml` = 50 % efficiency, plausible for a combined-cycle plant.
- Dates: issued 2026-04-02 16:55, after the export declaration (16:41).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000`: suspected that the value is taken from an invoice not yet issued (`06-Invoice.xml`, 2026-04-03 11:25) — refuted because price and quantity are fixed by contract and border metering before the invoice is written.
- `/ImportCustomsDeclaration/cac:Shipment`: suspected a missing reference to the export declaration KG-EX-26-0152 — refuted because an import declaration does not need to cite the other country's export declaration; the shared shipment identifier already links them (with the contradiction of F1).
