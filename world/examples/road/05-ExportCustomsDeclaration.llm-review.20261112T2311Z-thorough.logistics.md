# LLM review: 05-ExportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/05-ExportCustomsDeclaration.xml`, Git blob `0fa315bd3a963ac3f8916911094b6904a7e60fbf` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### road/05#F1 · High · Declared by the exporter itself, while the waybill says the 3PL declares the export
- XPath: `/ExportCustomsDeclaration/cbc:ID` = `VI-EX-26-0155`
- XPath: `/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: This declaration is numbered by Valdara (VI- prefix), signed by Valdara and names no declarant, agent or representative other than the exporter; Castrano Logistics appears only as Valdara's service provider for "Warehousing and despatch". The waybill, issued by the carrier for the same consignment, states the opposite: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.` One of the two statements is wrong.
- Condition: the export declaration and the waybill agree on who declares the export: either the declaration shows Castrano Logistics as the party lodging it on Valdara's behalf, or the waybill names Valdara as declarant.
- Options: (a) preferred: correct the waybill text to the exporter declaring (the declaration is complete as it stands); (b) if the 3PL is meant to be the customs agent, show it as such in the declaration (sender, signature and a representative party) and keep the waybill text.
- Needs decision: yes (who acts as declarant is part of the story)

### road/05#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated. No other reading fits: 96 / 0.82 = 117.1, which is neither a count in the flow, nor the bench's materials (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg net). The same three values are in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) preferred: relate the factor to the activity it really measures (e.g. per kg of steel, base in KGM), so the value can be recalculated; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep the total.
- Needs decision: no

### road/05#F3 · Low · Exit office and border transport given only as a name
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: An export declaration is cleared against the office of exit and the means of transport that will cross the border. The exit office is a free-text description without an identifier, and the declaration names the carrier but not the vehicle (UR 4160 KT with trailer UR 4160 TR in `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `UR 4160 KT`). The same border post is again only described in `10-ImportCustomsDeclaration.xml` and as "Land border crossing Urvania–Bayvarra" in `09-TransportationStatus.xml`, so the three documents cannot be linked to one place.
- Condition: the exit office is identified (a customs office identifier or a location identifier used consistently in the flow), and the border means of transport is stated if the declaration's purpose needs it.
- Options: (a) preferred: give the exit office an ID (and use the same ID in 09 and 10); (b) add the means of transport to the declared shipment.
- Needs decision: no

### road/05#F4 · Low · Reference to the order without saying what it is
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: An AdditionalDocumentReference in a customs declaration can be any supporting document (invoice, contract, licence, certificate). This one has only an ID; nothing says it is the buyer's purchase order (`01-Order.xml`), and a customs officer would expect the commercial invoice (`15-Invoice.xml`, VI-INV-26-0166, issued only the next day) rather than the order.
- Condition: the reference states its document type, and it refers to a document that exists when the declaration is issued.
- Options: (a) preferred: add DocumentTypeCode (order) to the reference; (b) if customs requires the invoice, issue it before the declaration and reference it instead.
- Needs decision: no

## Checked and consistent
- Goods item weights 3984 + 122.4 = 4106.4 kg = shipment gross weight, and the same in `06-`/`07-CertificateOfOrigin.xml`, `08-Waybill.xml` and `10-ImportCustomsDeclaration.xml`.
- Physics: 3984 kg for 96 benches = 41.5 kg gross per bench (with pallet share and film), 122.4 kg for 12 castings = 10.2 kg gross each (with box and pallet share); with the waybill net weight of 3762 kg the tare is 344.4 kg for 25 pallets, 96 films (0.4 kg each = 38.4 kg) and 12 boxes, about 12 kg per pallet. Plausible.
- Quantities 96 and 12 and declared values 4790400 and 71760 XUF equal the order lines.
- Issue time 13:25 precedes the pickup (15:05) and departure (16:20) in the waybill; the note "declared electronically before the goods leave" holds.
- Shipment and consignment IDs resolve to the despatch advice and waybill; the declaration number VI-CD-26-0156 is the one quoted by `08-Waybill.xml` and `10-ImportCustomsDeclaration.xml`.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure`: shipment gross weight defined as including transport equipment but equal to the goods' gross weight — refuted because the goods are not containerised and the trailer belongs to the means of transport.
