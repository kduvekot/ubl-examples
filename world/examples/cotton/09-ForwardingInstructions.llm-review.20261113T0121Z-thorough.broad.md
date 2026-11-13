# LLM review: 09-ForwardingInstructions.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/09-ForwardingInstructions.xml`, Git blob `f8e65d13a83ffc42dbb2cdb364ae14e78a2f0b46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/09#F1 · Medium · Forwarding instructions that do not say what to carry, from where or to where
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- Why: Forwarding Instructions give "instructions regarding the action to be taken for the forwarding of goods described therein". The shipment here has only an identifier, a gross weight and a consignee: no goods item (lint, HS 5201, 27 bales), no packages or container, no place of loading (port of Selanu, the FOB point of the order 08) and no destination. The description ("Instructions for the bales to Bayvarra") and the order reference are the only hints. The forwarder cannot book the carriage from this document.
- Condition: the shipment states the goods (description and quantity or packages), the place where the forwarder takes over or loads them, and the destination.
- Options: (preferred) add a goods item (description, 27 bales, gross weight), the port of loading Selanu and the delivery place Lumeport (mill); or add at least goods item and route through `ShipmentStage`/`Delivery`.
- Needs decision: no

### cotton/09#F2 · Medium · The shipment number given as the shipping-order number
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `SCG-SH-26-0200`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: `ShippingOrderID` is the "Reference number to identify a Shipping Order", i.e. a booking order to a carrier. The value is the shipment's identifier (assigned by the ginnery, SCG-…), used the same way in 10, 11, 12, 13 and 15. A shipment identifier is not the number of a shipping order, and the instructions come from the mill, not from the ginnery.
- Condition: `ShippingOrderID` is absent or holds the number of an actual shipping order, different from the shipment ID.
- Options: (preferred) drop `ShippingOrderID`, because no shipping order exists in the flow; or give the carrier's booking number if the forwarder's booking is meant.
- Needs decision: no

### cotton/09#F3 · Medium · Shipment gross weight without the container
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment". 6190.29 kg is the goods with their bale packaging (the goods item's gross weight in 10, 11 and 15, "excluding the carrier's equipment"); the shipment moves in a container of 3750 kg tare, so the shipment gross weight by definition is 9940.29 kg (12). The same value is used for the shipment in 11, 13 and 15.
- Condition: the shipment's gross weight includes the transport equipment, or the cargo gross weight is carried at goods-item level only.
- Options: (preferred) move 6190.29 kg to a goods item (see F1) and leave the shipment gross weight out until the container is known; or state 9940.29 kg once the container is assigned.
- Needs decision: no

### cotton/09#F4 · Medium · Language code in `LocaleCode`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2: an ISO 639 language code in an element for a locale.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/09#F5 · Low · Exchange rate with nothing to convert
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the only amount is the declared carriage value in coral; no amount is in Lume. The exchange rate has no use in the instructions.
- Condition: an exchange rate appears only if an amount in the document is converted with it.
- Options: (preferred) drop it; or, if the carrier's liability is in Lume, state that and keep the rate.
- Needs decision: no

### cotton/09#F6 · Low · Distribution of the document to its own recipient
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `DocumentDistribution` lists "interested parties to whom this document is distributed". The only entry is the forwarder, to whom the instructions are addressed anyway; it adds nobody (filler).
- Condition: document distribution names parties other than the addressee, or is absent.
- Options: (preferred) drop it; or distribute a copy to the ginnery (consignor), which must hand over the goods.
- Needs decision: no

### cotton/09#F7 · Low · The consignee's contact is its purchasing desk in sales
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: a consignee's contact receives goods (goods-in, warehouse); here it is "Purchasing", placed in the sales department.
- Condition: the consignee's contact is a receiving function whose name and department agree.
- Options: (preferred) a goods-in / warehouse contact of the mill.
- Needs decision: no

### cotton/09#F8 · Low · The ginnery's English address tagged as Bayvarran English
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: as cotton/02#F4: `en-XB` here, `en-XL` in the ginnery's own documents for the same rendering.
- Condition: the same rendering carries the same tag everywhere.
- Options: (preferred) `en-XL`.
- Needs decision: no

## Checked and consistent
- Declared carriage value 6055.452 XLC equals the order value (08) and the commercial invoice (16); with `AdValoremIndicator` true it raises the carrier's liability to the goods' value. The bill of lading 13 repeats both.
- Order reference LTM-PO-26-0198 resolves to the mill's order 08; FOB Selanu makes the mill the party that instructs the forwarder.
- Consignee, consignment ID and shipment ID are the same as in 10, 11, 13 and 15; `ToOrderIndicator` false agrees with a straight consignment to the mill.
- 6190.29 − 6129 = 61.29 kg packing for 27 bales, about 2.3 kg per bale (1 %), plausible for bale wrap and ties (own knowledge).

## Considered and refuted
- `/ForwardingInstructions/cac:ConsignorParty`: consignor without a document role for the mill — refuted: the mill signs as the instructing party; the consignor is the ginnery that hands over the goods FOB.
- `/ForwardingInstructions/cbc:OtherInstruction`: free text where a structured element exists — refuted: no UBL element says where to send the bill of lading.
