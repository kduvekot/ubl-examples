# LLM review: 11-TransportExecutionPlanRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/11-TransportExecutionPlanRequest.xml`, Git blob `43f5b79071571e3db0185c905bab61bd7c25ec4c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/11#F1 · Medium · The transport request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `996`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- Why: A Transport Execution Plan Request asks a transport service provider to plan a transport of goods; the forwarder needs to know what goods, how many handling units and of what size, to plan loading. The only consignment data are an ID and a gross weight. There is no goods item, no description of the goods, no number or type of handling units (the despatch advice 12 shows six pallets of four benches, `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[6]/cbc:ShippingMarks` = `BRIGHTMARKET LUMEPORT / 006 of 006`), and no loading length or volume. Benches of 1800 mm (02-Catalogue) need pallets longer than a standard 1200 mm pallet, which matters for the loading plan.
- Condition: the consignment says what is carried: goods description (or goods items), the number and type of handling units (six pallets), and their weight; dimensions where the pallets are not standard.
- Options: (a, preferred) Consignment/TotalTransportHandlingUnitQuantity 6 and a GoodsItem "Park benches, 24 pieces on 6 pallets" with gross weight 996 kg (and the pallet dimensions); (b) Consignment/ConsignmentQuantity plus a goods description in a note, if the items are not known yet.
- Needs decision: no

### retail/11#F2 · Medium · A gate in the street-name element of the pick-up location
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". `Gate 3` is not a street but the gate of the distribution centre where the truck is loaded. For a transport location that is useful information, but it belongs in an element for a place within the site (e.g. the Location's own name or description, or a sub-location), not in a street name. The same value is in the party's postal address in this and other examples (a postal address holds nothing that only matters for vehicles), which is the parties lens.
- Condition: the gate is not held in a street-name element of the pick-up address.
- Options: (a, preferred) FromLocation/Name or Description "Lumeway distribution centre, gate 3", and the address without the gate; (b) a SubsidiaryLocation for the gate.
- Needs decision: no

### retail/11#F3 · Low · Pick-up and delivery locations named after the companies, without the GLNs the flow uses
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Lumeway Distribution`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Brightmarket Stores`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Goods-in, garden department`
- Why: A Location's name should name the place, not the company. The order 08 asks for delivery at a specific goods-in, GLN `9522610900019`; the transport request sends the forwarder to the store's business address (Market Street 50) without that goods-in, so the driver does not know where to unload. The note speaks of the "distribution centre", which is the place to name.
- Condition: From/To locations name the places (distribution centre, store goods-in), and the ToLocation carries the goods-in GLN of the order.
- Options: (a, preferred) ToLocation/ID `9522610900019`, name "Brightmarket Lumeport, goods-in, garden department"; FromLocation named "Lumeway distribution centre, Marrowdale" (with a GLN if one exists).
- Needs decision: no

## Checked and consistent
- Physics: 996 kg for 24 benches on 6 pallets. With about 30 kg per long wooden pallet (own estimate) the benches weigh (996 − 180) / 24 = 34 kg each; the catalogue's material consumption per bench, 34 kg steel + 22.5 kg hardwood = 56.5 kg (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`), includes casting and sawing losses, so a finished bench of about 34 kg is plausible. The same 996 kg is in 12 and 13.
- Service period 2026-04-29 to 2026-05-02 is after the request (2026-04-25), after the catalogue's earliest delivery date (2026-04-27), before the promotion (2026-05-11); the despatch on 2026-04-29 and the receipt on 2026-04-30 (17) lie within it.
- Consignment ID `LD-CS-26-0228` is the same in 12, 13, 14, 15 and 16.
- Parties: transport user and bill-to Lumeway, provider Bayforth, consignee Brightmarket at Market Street 50, consignor Lumeway — as in 13 and 16.
- Response deadline 2026-04-26 is after the issue date.
- FTL for 6 pallets: a dedicated truck for a time-critical promotion delivery is a legitimate choice; the invoice 16 bills it per loaded kilometre.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: suspected an implausible full truck load for 996 kg — refuted because FTL describes the booking (the whole vehicle for this consignment), not the fill rate; nothing in the flow says the truck carried other goods.
