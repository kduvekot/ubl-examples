# LLM review: 09-ForwardingInstructions.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/09-ForwardingInstructions.xml`, Git blob `f8e65d13a83ffc42dbb2cdb364ae14e78a2f0b46` (committed)
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

### cotton/09#F1 · High · "Send the bill of lading to the forwarder", but the bill goes to the bank and the mill
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: The instructions tell the forwarder that the bill of lading is to go to the forwarder (Bayforth Forwarding). The bill of lading 13, issued under these instructions (it references `LTM-FI-26-0199`), sends the original by courier to the Bank of Selanu and a scanned copy to the mill, and nothing to the forwarder. The two documents contradict each other on who receives the bill.
- Condition: the instruction on where the bill of lading goes and the bill's distribution list agree.
- Options: (preferred) decide who holds the original (the bank, if the story is a documentary collection; the forwarder, if it clears the goods at Lumeport) and make the instruction and the distribution say the same; or drop the instruction.
- Needs decision: yes (whether a bank holds the original bill is part of the payment story)

### cotton/09#F2 · Medium · Instructions do not say what is to be carried, from where, to where or when
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the bales to Bayvarra.`
- Why: Forwarding Instructions give "instructions regarding the action to be taken for the forwarding of goods described therein". The shipment here has only an ID, a gross weight and a consignment with a consignee. It has no goods item (no description, no commodity code, no number of bales), no transport handling unit or container (the goods go in one 40-foot container, 12 and 17), no place of loading or discharge, no delivery or pickup place and no requested date. The forwarder cannot book the carriage from this document ("Please confirm the booking"); everything it needs is only implied by the order 08 it references and by the description "bales to Bayvarra".
- Condition: the document states the goods (description, bale count, gross weight), the equipment requested, the places (port of loading Selanu, port of discharge Lumeport, or pickup and delivery places) and the requested timing, consistently with 12, 13 and 17.
- Options: (preferred) add a goods item (27 bales of cotton lint, HS 5201, 6190.29 kg), a transport handling unit or equipment request for one 40-foot container, a main-carriage shipment stage with the loading and discharge ports, and a requested pickup or loading date; or, if the instructions really only cover the booking, say so and keep at least the goods and ports.
- Needs decision: no

### cotton/09#F3 · Medium · Shipping order ID is the shipment ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `SCG-SH-26-0200`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: `ShippingOrderID` is a "reference number to identify a Shipping Order", a document by which the shipper orders carriage (or a carrier's booking). `SCG-SH-26-0200` is the identifier of the shipment itself, used as `Shipment/ID` here and in 10, 11, 12, 13 and 15. An identifier of one kind is used as another; a shipping order with this number appears nowhere in the flow, and the ID prefix is the gin's, while these instructions are the mill's (signed by Lumeport Textile Mill, ID `LTM-FI-…`).
- Condition: `ShippingOrderID`, if present, identifies a shipping order (or booking) that is not the shipment ID; otherwise it is absent.
- Options: (preferred) drop `ShippingOrderID`; or give it the forwarder's or carrier's booking number if the story has one (then use the same number where 13 refers to the booking).
- Needs decision: no

### cotton/09#F4 · Low · Shipment gross weight excludes the transport equipment
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment". 6190.29 kg is the goods with packaging only (6129 kg lint + 61.29 kg bale wrapping, = goods item gross in 10); the container (tare 3750 kg, 12) is not included, so by the UBL definition the shipment weighs 9940.29 kg. Shipping practice usually reports cargo gross weight without the container; under the agreed rule of semantic conformance the definition applies. (At the time of these instructions the container may not yet be known, which would rather argue for giving the goods' gross weight in a goods item.)
- Condition: the shipment's gross weight includes the transport equipment, or the weight of goods plus packaging is carried where the definition fits (goods item or consignment gross weight).
- Options: (preferred) move 6190.29 kg to a goods item's `GrossWeightMeasure` (see F2) and leave the shipment gross weight out until the container is known; or state 9940.29 kg.
- Needs decision: no

## Checked and consistent
- Gross weight arithmetic: 27 bales × 227 kg = 6129 kg; 6190.29 − 6129 = 61.29 kg packaging, 2.27 kg per bale, i.e. 1 % of the lint, plausible for bale wrapping and ties (own knowledge: about 1.5–2.5 kg per bale).
- `DocumentReference` `LTM-PO-26-0198` resolves to the order 08; the consignee (Lumeport Textile Mill) and consignor (Selanu Cotton Ginnery) agree with 08, 10 and 13.
- `DeclaredCarriageValueAmount` 6055.452 XLC equals the order value (08) and the declared customs value (10).
- Consignment ID `LTM-CS-26-0201` is the same in 11, 13 and 17; shipment ID `SCG-SH-26-0200` is the same in 10, 11, 12, 13 and 15.
- The mill issuing the forwarding instructions fits FOB (08): the buyer arranges main carriage.

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `false`: checked against 13 — the bill of lading names the mill as consignee and has no to-order indication, so it is a straight bill as requested; no contradiction on this point.
