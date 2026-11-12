# LLM review: 04-ExportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### energy/04#F1 · High · The whole export is consigned to Montebrio Power, but 2400 MWh of it are sold to Ferrano Energy
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `07-Invoice.xml:/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- Why: the declaration has one goods item of 39200 MWh with one consignee, Montebrio Power. Kelpstone Gas invoices the March gas in two parts: 36800 MWh to Montebrio Power (`06-Invoice.xml`) and 2400 MWh to Ferrano Energy (`07-Invoice.xml`), both "measured at the border station" and both zero-rated as "Export outside Bayvarra"; 36800 + 2400 = 39200. The 2400 MWh of Ferrano Energy are thus declared as consigned to Montebrio Power, which `07-Invoice.xml` contradicts, and `05-ImportCustomsDeclaration.xml` imports only Montebrio's 36800 MWh. The consignee of the export does not agree with the buyers of the same gas.
- Condition: the export declaration's consignees agree with the parties the exported gas is delivered to in the flow: either each buyer's quantity is declared with that buyer as consignee, or the story says why Montebrio Power receives Ferrano Energy's gas.
- Options: (a) preferred: declare two consignments or goods items, 36800 MWh to Montebrio Power and 2400 MWh to Ferrano Energy, each with its own weight and value, because it matches the two invoices; (b) limit this declaration to Montebrio's 36800 MWh and add a separate export (and import) for Ferrano Energy's 2400 MWh; (c) keep one consignee and change the story so that Ferrano Energy's gas is delivered through Montebrio Power (then `07-Invoice.xml` needs to say so).
- Needs decision: yes

### energy/04#F2 · High · Shipment KG-SH-26-0154 has another quantity and weight in the import declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2940000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2760000`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: `Shipment/cbc:ID` is "an identifier for this shipment"; the same identifier names the same shipment in both declarations, but the export gives 39200 MWh and 2 940 000 kg, the import 36800 MWh and 2 760 000 kg (the difference, 2400 MWh and 180 000 kg, is Ferrano Energy's gas, see F1). One shipment cannot have two quantities. Both have the same weight per energy (2 940 000 / 39200 = 2 760 000 / 36800 = 75 kg per MWh), so the difference is a part of the shipment, not a measuring difference.
- Condition: a shipment identifier used in both declarations stands for the same quantity and weight in both, or the declarations use different shipment identifiers for different quantities.
- Options: (a) preferred, together with F1: split the export into the two buyers' parts, so that the import's shipment (or consignment) is exactly the part Montebrio Power imports; (b) give the import its own shipment identifier and refer to the export shipment as the larger whole.
- Needs decision: yes

### energy/04#F3 · Medium · Natural gas in a pipeline is declared as dry bulk cargo
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: the world's CargoTypeCode list defines BULK as "Dry bulk: loose dry goods such as ore or grain, poured into the hold". The goods are natural gas carried by pipeline (`TransportModeCode` 7, `TransportMeansTypeCode` 71). Gas is neither dry nor poured into a hold; the code's meaning does not fit the goods. The list has no code for gas, and LIQUID ("liquids in tanks") does not fit either. The same code occurs in `05-ImportCustomsDeclaration.xml` (counted over `world/examples/*/*.xml`: BULK with natural gas only in these two examples).
- Condition: the cargo type code of the gas means gaseous bulk or pipeline cargo, or there is no cargo type code.
- Options: (a) preferred: add a code for gaseous bulk (pipeline gas) to the world's CargoTypeCode list and use it here and in `05-ImportCustomsDeclaration.xml`, because cargo type is meaningful for a customs declaration; (b) leave `CargoTypeCode` out, since mode and means of transport already say it is a pipeline.
- Needs decision: no

### energy/04#F4 · Medium · The declaration does not say for which period the pipeline gas was exported, nor where it left Bayvarra
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description` = `Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.`
- Why: the declaration, issued 2026-04-02, declares 39200 MWh that flowed through a pipeline; it only makes sense as a declaration of the flow of a period (March 2026, the period of `06-Invoice.xml` and `07-Invoice.xml`). Nothing in it states that period: no `ShipmentStage/cac:TransitPeriod`, no validity period; only the identifier KG-P1-2603 hints at it. Nor does it say where the gas leaves Bayvarra: the item text names a border station, but there is no `CustomsDeclaration/cac:CustomsExitOfficeLocation` or other location for it, and the customs party is the office at Marrowdale without anything tying it to the pipeline. Without period and exit point the declared quantity cannot be checked against the border station's metering.
- Condition: the declaration states the period of the declared flow and the place (border station or exit office) where the gas leaves the country.
- Options: (a) preferred: `ShipmentStage/cac:TransitPeriod` 2026-03-01 → 2026-03-31 and `CustomsDeclaration/cac:CustomsExitOfficeLocation` (or the border station as a location of the stage), because these are the dedicated elements; (b) at least the period, with the exit point in the stage's description.
- Needs decision: no

### energy/04#F5 · Low · JourneyID carries a month's flow, not a service schedule
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: UBL defines `TransportMeans/JourneyID` as "an identifier for the regular service schedule of this means of transport". The value reads as pipeline 1, March 2026 (the suffix 2603 follows the convention of the flow's other period identifiers, e.g. `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:ConsumptionID` = `FG-CP-4120-G1-2603`), i.e. one month's flow, which is what the shipment is, not a schedule of the pipeline. It is also the only place where the period appears (F4). The same value is in `05-ImportCustomsDeclaration.xml`.
- Condition: `JourneyID` identifies a regular schedule of the pipeline (e.g. a nomination or flow schedule), or is absent; the period of the flow is stated where F4 asks.
- Options: (a) preferred: leave `JourneyID` out and identify the pipeline itself (`TransportMeans` with its name or an identifier), with the period per F4; (b) keep it if the story gives the pipeline a monthly flow schedule with this number.
- Needs decision: no

### energy/04#F6 · Low · The field's coordinates are 6.1 km from the plant, the text says four kilometres
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `18.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `16.20`
- Why: calculated: plant 39°52.80′ S 15°18.00′ W, field (the region of production in `Shipment/cac:OriginAddress`) 39°49.80′ S 15°16.20′ W. Δ latitude 3.00′ = 5.56 km; Δ longitude 1.80′ × cos 39.85° = 1.38′ = 2.56 km; distance √(5.56² + 2.56²) = 6.1 km to the north-north-east. The description says the platform lies four kilometres out. A perpendicular distance from a coast running obliquely could be smaller than the straight line, but with the plant "on the coast" the gap of 2 km is large for a value given to one significant figure. The same description is in `05-ImportCustomsDeclaration.xml`, the same field coordinates in `06-Invoice.xml` and `07-Invoice.xml`.
- Condition: the distance in the description agrees with the coordinates of plant and field (within the rounding of the description).
- Options: (a) preferred: say "about six kilometres out" (keeps the map coordinates); (b) move the field's coordinates to about 4 km from the plant, if the map allows.
- Needs decision: no

## Checked and consistent
- Weight against energy, calculated: 2 940 000 kg / 39200 MWh = 75 kg per MWh, i.e. 13.33 MWh per tonne = 48.0 MJ/kg. A typical pipeline natural gas (e.g. 90 % methane, 5 % ethane, 5 % nitrogen by mole: 17.3 g/mol, gross calorific value 879 kJ/mol) has about 50.8 MJ/kg; pure methane 55.5 MJ/kg (own knowledge). 48 MJ/kg is plausible for gas with some inerts. Goods item and shipment weight agree (one goods item); for gas in a pipeline gross weight = net weight.
- Quantity against the invoices: 36800 MWh (`06-Invoice.xml`) + 2400 MWh (`07-Invoice.xml`) = 39200 MWh.
- Value, calculated: 39200 MWh × 36 XBL = 1 411 200 XBL; the invoices' price 3600 XUF per MWh at 100 XUF per XBL is 36 XBL; (132 480 000 + 8 640 000) XUF / 100 = 1 411 200 XBL.
- Capacity: 39200 MWh in 744 h is an average flow of 52.7 MW, at about 10.5 kWh/m³ some 3.7 million m³ in the month (about 120 000 m³ a day), a small export pipeline; no capacity is stated in the document.
- Codes: `TransportModeCode` 7 (Rec. 19 fixed transport installations) and `TransportMeansTypeCode` 71 (Rec. 28 pipeline) fit; HS 271121 (natural gas, gaseous), section V and CPC 12020 fit the goods; MWH and KGM fit their measures.
- Parties for the transport: the carrier, Kelpstone Gas, is the exporter running its own export pipeline; consignor and consignee agree with `05-ImportCustomsDeclaration.xml` (Montebrio Power, F1 aside).
- Dates: issued 2026-04-02 16:41, before the import declaration (16:55) and the invoices (2026-04-03).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelpstone Gas`: suspected that a gas producer (ISIC 0620) is not the carrier — refuted because a producer operating the pipeline from its own treatment plant to the border is common, and no other party in the flow is said to run the pipeline.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00`: suspected that the value is declared before the invoices exist (issued 2026-04-03) — refuted because the price per MWh is fixed by contract and the quantity by the border metering, so the value is known when the declaration is made.
