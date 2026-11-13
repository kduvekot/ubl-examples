# LLM review: 10-PackingList.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/10-PackingList.xml`, Git blob `aef1ab21426bbd03022aba54b057f406aeb46b61` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/10#F1 · High · Shipment gross weight smaller than the gross weight of its own container
- XPath: `/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:TareWeightMeasure` = `3750`
- Why: In Shipment, GrossWeightMeasure is "the total gross weight of a shipment; the weight of the
  goods plus packaging plus transport equipment". The same document gives the container
  TWLU4120872 a gross weight of 7,856.4 kg with a tare of 3,750 kg. The shipment that includes that
  container cannot weigh 4,106.4 kg; 4,106.4 kg is goods plus pallets (the sum of the goods items,
  3,984 + 122.4).
- Condition: the shipment's gross weight includes the container (7,856.4 kg), or the 4,106.4 kg is
  given in an element whose definition excludes transport equipment.
- Options: (a) preferred: 7,856.4 kg as the shipment's gross weight; the goods items already carry
  the weight without the container; (b) drop the shipment's gross weight.
- Needs decision: no

### sea/10#F2 · High · Emission value does not follow from its factor and base
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: 0.82 × a base of 1 each = 0.82, not 96 kg CO2e ("a numeric factor used to calculate the value
  measurement").
- Condition: factor × base = value, or factor and base absent.
- Options: (a) preferred: drop factor and base (and, see F6, the emission from the packing list).
- Needs decision: no

### sea/10#F3 · Medium · A packing list that does not say how the goods are packed
- XPath: `/PackingList/cbc:Note` = `25 pallets.`
- XPath: `/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- Why: A PackingList is "a document describing how goods are packed". It has two goods items without
  any package or handling unit, a single TransportHandlingUnit that holds only the container, and
  the pallets only as a count and a note. Which pallet holds what (24 pallets of four benches and one
  pallet of 12 side frames, as the bill of lading shows with its packaged handling units of four,
  `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity`
  = `4`) is missing from the one document whose purpose it is.
- Condition: the packing list describes the 25 pallets (type, contents per pallet, and which goods
  item each holds), consistent with the bill of lading.
- Options: (a) preferred: 25 TransportHandlingUnits of type pallet (or two with counts) with their
  goods items and quantities, inside or alongside the container; (b) packages per goods item.
- Needs decision: no

### sea/10#F4 · Medium · An emission boundary code in FullnessIndicationCode
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The element is "a code signifying whether a piece of transport equipment is full, partially
  full, or empty"; in a packing list, the container's fullness would be a meaningful value, but this
  code is the footprint boundary of the bench.
- Condition: no boundary code in FullnessIndicationCode.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/10#F5 · Medium · A language code in LocaleCode
- XPath: `/PackingList/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PackingList/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; both are the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/10#F6 · Low · Catalogue content of the item copied into the packing list
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:EmissionStandardReference` = `Greenhouse Gas Protocol Product Standard`
- Why: The packing list describes packing; keywords, warranty, maintenance, repairability and the
  product footprint are catalogue content with no use for the forwarder or carrier. Goods item 2
  shows the item without them.
- Condition: the goods items' Item carries identification, description, origin and classification
  only (what packing, handling and customs use).
- Options: (a) preferred: reduce goods item 1's Item to the form of goods item 2.
- Needs decision: no

### sea/10#F7 · Low · Reference to the purchase order with only an ID
- XPath: `/PackingList/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: The reference does not say what the document is (the buyer's order, 05-Order).
- Condition: type code or description on the reference.
- Options: (a) preferred: add a DocumentTypeCode for an order.
- Needs decision: no

### sea/10#F8 · Low · Consignor's and consignee's contacts are sales customer service
- XPath: `/PackingList/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The consignor's contact for a packing list is whoever packed or despatched; the consignee's
  receives the goods. Both are a sales customer-service officer.
- Condition: despatch and goods-inwards contacts, or none.
- Options: (a) preferred: functions that fit.
- Needs decision: no

### sea/10#F9 · Low · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/PackingList/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- ISO 6346 check digit of TWLU4120872 passes; GTINs and GLN pass (`check_ids.py`).
- Goods items: 3,984 + 122.4 = 4,106.4 kg; net 3,762 kg; the difference of 344.4 kg over 25 pallets is
  13.8 kg per pallet, plausible for a wooden pallet with straps and film. 7,856.4 − 3,750 = 4,106.4.
- Declared values 49,920.00 and 768.00 match the order lines.
- Consignment, shipment, consignee and the 3PL in the delivery instructions agree with 09.

## Considered and refuted
- `/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount`: a customs value in a
  packing list — refuted: packing lists accompany export declarations, and the value is the one 11
  declares.
- `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure`:
  34 kg steel + 22.5 kg hardwood consumed per bench, against about 38 kg per packed bench in the
  goods item — refuted for this lens: consumption includes casting and sawing losses; the weight
  plausibility is for the logistics lens.
