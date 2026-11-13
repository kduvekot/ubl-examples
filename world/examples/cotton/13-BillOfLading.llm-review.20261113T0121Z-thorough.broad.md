# LLM review: 13-BillOfLading.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/13-BillOfLading.xml`, Git blob `c90a3571519a90b3221ab1bd12b871dc2751864d` (committed)
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

### cotton/13#F1 · Medium · A shipped-on-board bill of lading without vessel, ports, goods or container
- XPath: `/BillOfLading/cbc:Description` = `Shipped on board.`
- XPath: `/BillOfLading/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- Why: a bill of lading states "the details of the transportation" under which the carrier carries the goods; as a shipped-on-board receipt for goods it identifies the vessel, the ports of loading and discharge, the goods (description, number of packages) and, for containerised cargo, the container and seal (own knowledge of the Hague-Visby rules on what a B/L must show). This one has only a shipment ID, a gross weight and the consignee. The vessel (Tidewell Reef, voyage TR-26-09W in 14), the port of Selanu, the port of Lumeport, the 27 bales of lint and container TWLU4123110 (12) are all missing; the consignee could not claim the goods with it.
- Condition: the bill of lading names the vessel and voyage, the ports of loading and discharge, the goods with their number of packages and gross weight, and the container.
- Options: (preferred) add a shipment stage (main carriage, vessel, ports, loading date), a goods item (27 bales of cotton lint, 6190.29 kg) and a transport handling unit with the container; the 40-foot container in 17 and 12 gives the equipment.
- Needs decision: no

### cotton/13#F2 · Medium · Shipment gross weight without the container
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment". The carrier received the VGM of 9940.29 kg for this shipment the day before; 6190.29 kg is the cargo without the container.
- Condition: the shipment gross weight includes the container, or the cargo weight is given at goods-item level.
- Options: (preferred) the cargo gross weight on a goods item (F1) and no shipment gross weight, or 9940.29 kg.
- Needs decision: no

### cotton/13#F3 · Medium · Language code in `LocaleCode`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/13#F4 · Low · A bank as mortgage holder on a straight bill under an open-account sale
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MortgageHolderParty/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ToOrderIndicator` = `false`
- XPath: `16-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: the ginnery's bank holds a security interest in the consignment and receives the original bill by courier, as under a documentary collection or credit. But the bill is consigned straight to the mill (not to order), which can usually take delivery without presenting it, and the sale is paid by plain credit transfer 30–45 days after the invoice (16, paid in 18). Nothing in the flow gives the bank a reason to hold the goods as security or the originals.
- Condition: either the payment terms of the sale explain the bank's role (e.g. documents against payment through Bank of Selanu, an order bill), or the bank is not named.
- Options: (preferred) drop the mortgage holder and send the originals to the forwarder or the mill (09 asks to send the bill to the forwarder); or make the sale a documentary collection through Bank of Selanu, with an order bill and matching payment terms in 16.
- Needs decision: yes

### cotton/13#F5 · Low · Exchange rate with nothing to convert
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the only amount is the declared value in coral; the Lume rate converts nothing.
- Condition: an exchange rate only where an amount is converted.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/13#F6 · Low · Originals to the bank although the instructions ask for the forwarder
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- Why: the instructions the bill refers to (`DocumentReference` LTM-FI-26-0199) ask for the bill to go to the forwarder; the distribution sends the original to the ginnery's bank and a scan to the mill, and nothing to the forwarder.
- Condition: the distribution follows the forwarding instructions, or the bill says why it departs from them.
- Options: (preferred) original to Bayforth Forwarding; or adapt the instructions if the bank route (F4) is kept.
- Needs decision: no

### cotton/13#F7 · Low · The consignee's contact is its purchasing desk in sales
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- Why: as cotton/09#F7.
- Condition: a receiving contact whose name and department agree.
- Options: (preferred) goods-in / import desk.
- Needs decision: no

### cotton/13#F8 · Low · The ginnery's English address tagged as Bayvarran English
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: as cotton/02#F4.
- Condition: the same rendering carries the same tag everywhere.
- Options: (preferred) `en-XL`.
- Needs decision: no

## Checked and consistent
- Issued 2 March 09:37, after the VGM (1 March) and the export declaration (1 March), before the pre-arrival report (3 March) and the import declaration (6 March).
- Declared carriage value 6055.452 XLC with `AdValoremIndicator` true as in 09; "Freight collect" agrees with the FOB order 08.
- Reference to the forwarding instructions 09 resolves; consignor, consignee, consignment ID and forwarder agree with 09.
- Cited as the transport document by the import declaration 15 and the forwarder's invoice 17.

## Considered and refuted
- `/BillOfLading/cbc:DocumentStatusCode`: `Confirmed` on a first issue — refuted: a status value, not implied by absence; acceptable.
