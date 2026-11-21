# LLM review: 02-DespatchAdvice.xml

Flow: lpg (9924528384) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/lpg/02-DespatchAdvice.xml`, Git blob `c07eecf78f14f330062fe3e39d3ca57eafdeeb0b` (committed)
- Last commit changing the example: d34fe695 2026-11-21 O277 (3): UBL's spelling "despatch" for UBL concepts, and a published-text rule for it
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### lpg/02#F1 · Low · The delivery customer's contact is customer service, not the plant that receives the propane
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- Why: the Contact of `DeliveryCustomerParty` is the one to call about the arriving delivery. The propane is pumped into the storage of the district heating plant, where "the water company's operator reads the storage level" (`03-Waybill.xml:/Waybill/cbc:OtherInstruction`); the company's customer service for its own customers is not that contact. The same contact appears in every role of the party in the flow, which suggests master data.
- Condition: the delivery customer's contact is the receiving function at the district heating plant (for example its control room or boiler-house operator), or there is no contact.
- Options: (a, preferred) the plant's operations contact; (b) leave out the contact.
- Needs decision: no

### lpg/02#F2 · Low · Gullhaven telephone prefix "38522" overlaps Lumeport's "38"
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38522 68330`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Telephone` = `+999 2 38522 41906`
- Why: as in `01-Order.xml` (lpg/01#F2): Gullhaven (postal zone 90540) numbers begin with `38522`, while Lumeport numbers begin with `38` and an eight-digit number; the two codes are not prefix-free.
- Condition: one prefix-free numbering plan for Gullhaven and Lumeport.
- Options: as lpg/01#F2.
- Needs decision: yes

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` resolves to `01-Order.xml`; order line 1 is referenced by `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID`.
- Quantity: 20.18 TNE despatched for 20 TNE ordered, explained by the line note (a full tanker load, weighed); equals the consignment gross weight 20180 KGM here and in `03-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:GrossWeightMeasure`, and the invoiced quantity in `04-Invoice.xml`.
- Shipment ID `7400034654` and consignment ID `7300034654` are the same as in `03-Waybill.xml`; the carrier is the waybill's carrier.
- Dangerous goods: UN 1965, class 2.1, no packing group, technical name "Mixture C", ERG guide 115 all agree with each other and with the waybill (own knowledge of the UN Model Regulations and the ERG).
- Times: issued 07:05 on 2026-06-10, after the planned departure at 07:00 in the waybill; actual despatch date the same day; estimated delivery the same day as the waybill's planned arrival.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Warehouse`: a "warehouse" department at a gas plant's loading bay looked odd — refuted as a plausible name for the plant's despatch function; the contact (despatch office, despatch coordinator) fits the role of despatch party.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:HazardousItem/cbc:HazardousCategoryCode` = `2.1` next to `HazardClassID` `2.1`: suspected duplication — refuted, both elements exist for this purpose and agree.
