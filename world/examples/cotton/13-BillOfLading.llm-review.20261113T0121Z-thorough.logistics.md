# LLM review: 13-BillOfLading.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/13-BillOfLading.xml`, Git blob `c90a3571519a90b3221ab1bd12b871dc2751864d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### cotton/13#F1 · High · Distribution contradicts the forwarding instructions
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `/BillOfLading/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/BillOfLading/cac:DocumentReference/cbc:ID` = `LTM-FI-26-0199`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- Why: The bill of lading refers to the forwarding instructions `LTM-FI-26-0199` (09), which say "Send the bill of lading to the forwarder". The bill sends the original by courier to the Bank of Selanu (also named as mortgage holder of the consignment) and a scanned copy to the mill; the forwarder Bayforth Forwarding, named in the bill, receives nothing. The bank's role does not appear in the payment documents either: the gin's invoice 16 is paid by credit transfer straight to the gin (18), with no documentary collection.
- Condition: the bill's distribution and the instruction in 09 agree on who receives the bill; if a bank holds the original, the flow shows why.
- Options: (preferred) decide the story: either the forwarder receives the original (clearing at Lumeport), and the bank is removed as recipient (and as mortgage holder unless it finances the gin's stock); or the original goes to the bank under a documentary collection, and 09's instruction and the payment documents say so.
- Needs decision: yes (whether a bank holds the bill is part of the payment story)

### cotton/13#F2 · Medium · A "shipped on board" bill without goods, container, vessel, ports or date
- XPath: `/BillOfLading/cbc:Description` = `Shipped on board.`
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- Why: A bill of lading states "the details of the transportation" and evidences the carrier's receipt of the goods; a shipped bill states the goods (marks, number and kind of packages, description, weight), the vessel, the ports of loading and discharge and the date of shipment on board (Hague-Visby Art. III(3) and III(7), own knowledge). This bill has only a shipment ID, a gross weight and a consignment with consignee and mortgage holder: no goods item (27 bales of cotton lint, HS 5201), no container `TWLU4123110` (12), no vessel (the feeder `Tidewell Reef` of 14, if that is the ship), no ports (Selanu `XLSEL`, Lumeport `XBLMP`) and no on-board date. The document's purpose depends on these; without them the bill also cannot be linked to the vessel report 14.
- Condition: the bill states the goods (description, bale count, gross weight), the container, the vessel and voyage, the ports of loading and discharge, and the date shipped on board, consistently with 10, 11, 12 and 14.
- Options: (preferred) add a goods item and a transport handling unit with the container (and seal), a main-carriage shipment stage with the vessel (`Tidewell Reef`, journey `TR-26-09W`), the loading and discharge ports and the loading date.
- Needs decision: no

### cotton/13#F3 · Low · "Freight collect", but the forwarder invoices the sea freight
- XPath: `/BillOfLading/cbc:Note` = `Freight collect.`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- Why: "Freight collect" on the bill means the carrier collects the freight at destination, from the consignee (the mill). The forwarder's invoice 17, which refers to this bill, charges the mill for the same port-to-port sea freight. Either the forwarder pays the carrier (then the freight is not collect from the carrier's side, or the forwarder collects as the carrier's agent, which 17 does not say) or the mill would pay the freight twice. Under FOB (08) the buyer bears the main carriage, so both readings are possible; the documents do not say which one applies.
- Condition: the freight payment term on the bill and the forwarder's invoice describe one way in which the mill pays the sea freight.
- Options: (preferred) keep "freight collect" and let 17 say that the forwarder collects on the carrier's behalf (or pays it at destination and recharges it); or mark the bill freight prepaid by the forwarder.
- Needs decision: yes (who pays the carrier is part of the story)

### cotton/13#F4 · Low · Shipment gross weight excludes the transport equipment
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment"; 6190.29 kg leaves out the container (tare 3750 kg, 12). On bills of lading the cargo gross weight is customarily given without the container; under the agreed rule of semantic conformance the definition applies.
- Condition: the shipment gross weight includes the transport equipment, or the goods' gross weight is stated in a goods item (see F2), whose definition fits 6190.29 kg.
- Options: (preferred) give 6190.29 kg as goods item gross weight and drop or correct the shipment gross weight.
- Needs decision: no

## Checked and consistent
- Issued 2026-03-02 09:37, after the export declaration (11, 2026-03-01 13:33) and the VGM (12, 2026-03-01 15:19), and before the pre-arrival report (14, 2026-03-03).
- Consignor (Selanu Cotton Ginnery), consignee (Lumeport Textile Mill), carrier (Tidewell Ocean Lines, receiver of 12) and forwarder (Bayforth Forwarding, recipient of 09) agree with 09, 10 and 12.
- Shipment `SCG-SH-26-0200` and consignment `LTM-CS-26-0201` agree with 09, 11 and 17; 15 and 17 reference this bill by `TOL-BL-26-0206`.
- `DeclaredCarriageValueAmount` 6055.452 XLC equals the value declared in 09 and the order value (08).
