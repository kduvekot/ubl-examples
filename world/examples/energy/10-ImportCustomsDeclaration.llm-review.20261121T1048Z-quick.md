# LLM review: 10-ImportCustomsDeclaration.xml

Flow: energy (9909904601) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/energy/10-ImportCustomsDeclaration.xml`, Git blob `5cefc7ad09d3dcb26484089ec0a7f692aa7a41bd` (committed)
- Last commit changing the example: 658c912e 2026-11-20 Four mechanical fixes: distances, gas proof of origin, calendar waits, town streets
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 9fd37c8e 2026-11-21 Encyclopedia: the sweep's remaining points (Tallowford, the Bank of Selanu, the ore bridge, Hartsedge and Fleecewell, Harrowmead's orchards, place lists by description, locality names, varied village and river sentences); no parity review has changed a rate (O52)
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

## Checked and consistent
- `/ImportCustomsDeclaration/cac:AdditionalDocumentReference[1]/cbc:ID` = `7600006841` resolves to 04-ExportCustomsDeclaration.xml with the same issue date; `/ImportCustomsDeclaration/cac:AdditionalDocumentReference[2]/cbc:ID` = `9000034210` resolves to 07-Invoice.xml (Kelpstone Gas to Ferrano Energy).
- Shipment `7400034203` and consignment `7300034204` are 04's shipment and its second consignment ("2,400 MWh … fed into the grid at the city gate for the retail company's gas customers"); 05 declares the first consignment of the same shipment for the power station.
- Amounts: 2,400 MWh × 3,600 ferra = 8,640,000 ferra = 07's line and payable amount = `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `8640000`; 04 declares 86,400.00 lume, which is 8,640,000 ferra at the rate of 100 the world uses (wood/08-Invoice.xml, tax exchange rate); 20 % of 8,640,000 = 1,728,000, as both language versions of the note say.
- Weight: 180,000 kg for 2,400 MWh is 75 kg/MWh (13.3 kWh/kg, about 48 MJ/kg, close to the heating value of natural gas, own knowledge), the same ratio as 04 and 05 (2,760,000 kg for 36,800 MWh).
- Origin Bayvarra with criterion `P` (wholly obtained) agrees with 07's origin statement ("criterion P") and fits gas extracted from the Kelpstone field; HS 271121 and CPC 12020 fit gas in the gaseous state; transport mode 7 and means type 71 (pipeline) fit.
- TransitPeriod 1–31 March: the month of flow, declared after it ends (3 April), consistent with 07's invoice period "March 2026".
- FirstArrivalPortLocation is the border metering station, where 07's item says the gas is measured; the definition allows a border post for land crossings.
- The importer's customs contact fits the role; the customs authority's party data agree with 05.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:ID` = `7700000100` and 05's `7700000926`, both issued on 2026-04-03 by different declarants in what looks like one number series (100 at 15:35, 926 at 16:55) — refuted: the shared prefix can be the customs system's declaration series, which numbers per declarant or per office; nothing in the document says the series is sequential across declarants.
- `/ImportCustomsDeclaration/cbc:ProfileExecutionID` = `9909904601` follows no pattern of the flow's other ProfileExecutionIDs — refuted: the declaration is Ferrano Energy's own collaboration with customs, numbered by it.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `S` while no tax amount is stated in a structured element — refuted: it is the category of the import VAT, whose amount the note states (20 %, 1,728,000 ferra).

## Outside this review
- Geography across documents: the gas treatment plant "on the north coast" lies at 28°15.95′ S (04, 07), the border metering station at 28°40.54′ S, south of it, and the delivery point at the city gate (07) at 27°30.54′ S, north of both. The pipeline would run south to the border and then about 130 km north again, past the latitude of the north coast. Whether this fits the map is a location question for the map, not for this declaration.
