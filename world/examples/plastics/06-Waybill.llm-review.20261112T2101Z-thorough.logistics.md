# LLM review: 06-Waybill.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/06-Waybill.xml`, Git blob `98b3edab06331ce10e3457361c14ccae3bf60af1` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/06#F1 · High · The waybill reports an actual despatch that happens after it was issued
- XPath: `/Waybill/cbc:IssueTime` = `09:38:00`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchDate` = `2026-04-19`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `13:30:00`
- Why: The waybill is issued on 2026-04-19 at 09:38, yet records "the actual despatch (pickup)" at 15:10 the same day, five and a half hours later. An actual event must lie in the past at issue. The loading at 13:30 is also after issue; only the takeover (09:00) precedes it. Under the CMNI the carrier issues the consignment note once it has taken over the goods, and here it describes the goods as loaded and despatched, so the issue time and the event times cannot all be right.
- Condition: Every actual event in the waybill lies before its issue date and time; events that are still planned at issue are not stated as actual.
- Options: (a) preferred: issue the waybill after loading and despatch (e.g. 2026-04-19 around 15:30), because the note describes a document that goes with the goods ("Original, with the goods"), which fits issue at departure; also check the export declaration (16:08) and despatch advice (17:57) still follow; (b) keep the morning issue and change the despatch to an estimate (e.g. `Pickup` only) and the loading to a planned event.
- Needs decision: no

### plastics/06#F2 · High · CO2e emission is about a hundredth of what the stated diesel energy produces
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cbc:EnergySourceTypeCode` = `DIESEL`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cbc:AllocatedEnergyMeasure` = `5400`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cac:EnvironmentalEmission/cbc:ValueMeasure` = `14.3`
- Why: Burning diesel emits about 0.267 kg CO2 per kWh of fuel energy tank-to-wheel, about 0.32 kg CO2e per kWh well-to-wheel (EN 16258 / ISO 14083 default factors, own knowledge). 5400 kWh therefore gives about 5400 × 0.267 ≈ 1440 kg (TTW) to 5400 × 0.32 ≈ 1730 kg (WTW) CO2e. The stated 14.3 kg implies 14.3 / 5400 = 0.0026 kg/kWh, about one hundredth of any diesel factor. The energy itself is plausible: 5400 kWh for 120 t is 45 kWh/t, which at a typical 0.05–0.15 kWh per tonne-km for inland barges (own knowledge) is a voyage of roughly 300–900 km, compatible with about 2.75 days downstream. The emission figure is the one that does not fit.
- Condition: `ValueMeasure` = `AllocatedEnergyMeasure` × a stated or standard diesel emission factor (about 1440 kg for TTW, about 1730 kg for WTW for 5400 kWh), or both figures are changed together so that the factor is about 0.27–0.32 kg/kWh.
- Options: (a) preferred: keep 5400 kWh and set the emission to about 1440 kg (TTW) or 1730 kg (WTW), stating which, because the energy fits the voyage; (b) if 14.3 kg is wanted, reduce the energy to about 45–55 kWh, which would no longer fit a multi-day voyage of 120 t.
- Needs decision: no

### plastics/06#F3 · High · The note says three originals, the distribution gives the consignor only an electronic copy
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`
- Why: The note says the consignment note is made out in three originals, for consignor, consignee and carrier. The distribution list, "a list of interested parties to whom this document is distributed", gives the consignee an original with the goods and the consignor (Rinova) an electronic copy; no original for the consignor is distributed. The text and the structured distribution contradict each other. The carrier keeping its own original needs no distribution entry.
- Condition: The note and the distribution agree on who receives an original and who a copy.
- Options: (a) preferred: make Rinova's entry an original (a distribution type for the consignor's original), because the CMNI consignment note's consignor original is what the note describes; (b) change the note to "originals for consignee and carrier, electronic copy for the consignor".
- Needs decision: no

### plastics/06#F4 · Medium · ShippingOrderID holds the consignment ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `RR-CS-26-0885`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- Why: `ShippingOrderID` is "an identifier ... of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's own identifier ("an identifier assigned to a collection of goods"), repeated in the consignment two levels down. The instruction Rinova gave the carrier is the transport execution plan request `RR-TR-26-0884` (03), which the plan 04 answers. An identifier of one kind is used as another.
- Condition: `ShippingOrderID` is the identifier of the instruction the shipper gave (the request 03, `RR-TR-26-0884`, or another shipping order that exists in the flow), or the element is absent.
- Options: (a) preferred: `RR-TR-26-0884`, because that request is the shipper's instruction for this carriage; (b) remove the element, since the plan 04 is referenced already.
- Needs decision: no

### plastics/06#F5 · Medium · One package said to contain 120 items, instead of 120 one-tonne bags
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ID` = `RR-JB-0416`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:Quantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingType` = `Jumbo bag of one tonne with four lifting loops`
- Why: `Package/Quantity` is "the quantity of items contained in this package". As encoded, there is one package with ID `RR-JB-0416`, a jumbo bag "of one tonne", that contains 120 items (EA). What is meant is 120 jumbo bags each containing 1 t. One one-tonne bag cannot hold 120 tonnes; the encoding contradicts the packaging type text and the item description ("in jumbo bags of 1 tonne"). The single package ID for 120 bags has the same problem.
- Condition: The waybill expresses 120 packages of type JB, each holding 1 t (e.g. a package count on the goods item, consignment or handling unit, or the content per bag in `Package/Quantity` = 1 TNE), with any package ID identifying one bag or a lot of bags, not a single package.
- Options: (a) preferred: `Consignment/TotalPackagesQuantity` = 120 (or a `TransportHandlingUnit` with `TotalPackageQuantity` 120) and `ContainingPackage/Quantity` = 1 TNE per bag, because that states both facts in their own elements; (b) keep 120 in a package-count element and drop the package ID.
- Needs decision: no

### plastics/06#F6 · Medium · ReturnableQuantity counts the goods as returnable
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ReturnableQuantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ReturnableMaterialIndicator` = `true`
- Why: `GoodsItem/ReturnableQuantity` is "the number of units in the goods item that may be returned". The goods item is 120 t of granulate sold outright; the granulate is not returnable. What is returnable is the packaging, and the package already says so (`ReturnableMaterialIndicator` = true). The value 120 EA counts the bags as units of the goods item, which mixes the goods and their packaging.
- Condition: `ReturnableQuantity` is absent (the bags' returnability stays on the package), or it counts units of the goods that may in fact be returned, if the story has such a case.
- Options: (a) preferred: remove it, because the package indicator already carries the business fact; (b) if returnable bags must be counted, do it on the package or handling unit (e.g. `ReturnableQuantity` on a `TransportHandlingUnit`).
- Needs decision: no

### plastics/06#F7 · Medium · Quantity and chargeable quantity are a weight, not a number of units
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableQuantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableWeightMeasure` = `120000`
- Why: `Quantity` is "the number of units making up this goods item" and `ChargeableQuantity` "the number of units in the goods item to which charges apply". Both are 120 TNE, a mass, and repeat the net weight and the chargeable weight already given in their own elements (`NetWeightMeasure` and `ChargeableWeightMeasure` = 120000 KGM). The units of the goods item are the 120 jumbo bags. The same use of `Quantity` is in 05 and 09.
- Condition: `Quantity` and `ChargeableQuantity` count units (bags) or are absent; weights stay in the weight elements.
- Options: (a) preferred: drop `ChargeableQuantity` (the freight is per tonne and `ChargeableWeightMeasure` says so) and make `Quantity` a count of bags or drop it; (b) keep both as counts of bags if the carrier charges per bag (it does not: 07 charges per tonne).
- Needs decision: no

### plastics/06#F8 · Low · Net volume is the volume of solid polyethylene, and the goods item's height is that of one bag
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:NetVolumeMeasure` = `130`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:MeasurementDimension/cbc:Measure` = `1300`
- Why: Calculated: 120 t ÷ 0.92 t/m³ (the item's density property) = 130.4 m³, so `NetVolumeMeasure` ("the volume contained by a goods item, excluding the volume of any packaging material") is the volume of the polymer as a solid block. Granulate in a bag fills its volume at bulk density, about 0.50–0.60 t/m³ for PE pellets and regranulate (own knowledge), i.e. 200–240 m³ for 120 t, or 1.67–2.0 m³ per tonne bag. The gross volume of 204 m³ (1.70 m³ per bag) is at the low end of that range and consistent with it only for a bulk density of about 0.59 t/m³ or more. With a bag height of 1.3 m, 1.70 m³ means a footprint of 1.31 m², about 1.14 m × 1.14 m, which is a large but possible filled bag (bulging). The net volume below the contents' bulk volume is the inconsistency. Further, `MeasurementDimension` is "a measurable dimension of this goods item", and 1300 mm is the height of one bag, not of a goods item of 120 bags.
- Condition: `NetVolumeMeasure` is the volume of the granulate as packed (bulk volume, not above the gross volume), or absent; any dimension on the goods item describes the goods item, or a per-bag dimension is put on the package.
- Options: (a) preferred: set the net volume to about 200 m³ (bulk density about 0.6 t/m³, just under the gross 204 m³), or drop it, and move the 1.3 m height to the package (`ContainingPackage/cac:MeasurementDimension`); (b) keep 130 m³ but say in the goods description that it is the solid volume (not the element's meaning, so less good).
- Needs decision: no

### plastics/06#F9 · Low · A "latest delivery date allowed by the buyer" that neither the buyer nor the plan states
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23`
- Why: `LatestDeliveryDate` is "the latest date of delivery allowed by the buyer". The buyer's order (01) states no delivery date at all, and the transport plan this waybill refers to requires the service to be completed by `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-04-22`. The waybill gives a later date, from a source the flow does not show.
- Condition: The latest delivery date comes from the buyer's order (01) and is consistent with the plan's end date, or the element is absent.
- Options: (a) preferred: add the requested delivery period to the order (01#F1) and keep 2026-04-23 here; (b) remove it from the waybill and rely on the plan's service end.
- Needs decision: no

### plastics/06#F10 · Low · Issue location is the carrier's name only
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Fiumella Barges`
- Why: `IssueLocation` is "the location where this waybill was issued"; the name is the company, not a place, and no address or identifier says where that is (the carrier's office in Ferrano, or the loading quay). The place of issue is a standard entry of a consignment note.
- Condition: `IssueLocation` names or locates a place (e.g. "Ferrano" with an address or location identifier).
- Options: (a) preferred: the loading quay or the city of Ferrano, according to where the note is made out (with F1: at the quay on departure); (b) the carrier's office address.
- Needs decision: no

### plastics/06#F11 · Low · The plan is referenced twice, both times without a document type
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ShipmentDocumentReference/cbc:ID` = `FB-TEP-26-0886`
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FB-TEP-26-0886`
- Why: The same transport execution plan (04) is referenced at document level and at goods item level, each time with an ID only. Neither says that it is a transport execution plan, so a reader cannot tell whether either is a booking, a shipping instruction or a contract; and the second reference adds nothing to the first.
- Condition: The plan is referenced once (where it applies) and the reference says what it refers to.
- Options: (a) preferred: keep the document-level `DocumentReference` with a `DocumentTypeCode` (`TransportExecutionPlan` from the world's UBL document type list, already used in this waybill for `Waybill`), drop the goods-item reference; (b) keep both, each with a type.
- Needs decision: no

## Checked and consistent
- Weights: gross 120480 kg − net 120000 kg = 480 kg packaging = 4 kg per bag, plausible for a 1 t woven-PP jumbo bag with four loops (about 2.5–5 kg, own knowledge). Net = net-net = chargeable = 120000 kg; there is no inner packaging, so net and net-net are equal.
- Freight: `FreightAllowanceCharge/Amount` 179400 XUF = 120 t × 1495 XUF/t, the same as the carrier's invoice (07 line 120 TNE × 1495).
- Loading time: 120 bags between loading 13:30 and despatch 15:10 is 100 minutes, about 0.8 minutes per bag; feasible with several bags per crane lift (own knowledge), tight with one.
- Vessel, journey, master, stage, events and estimated transit are identical to 04; the barge capacity is far above 120 t and 204 m³ (see 04).
- Pickup window 08:00–16:00 on 2026-04-19 contains takeover (09:00), loading (13:30) and despatch (15:10).
- References: order `RP-PO-26-0882` line 1 (01), plan `FB-TEP-26-0886` (04); the shipment `RR-SH-26-0889` and consignment `RR-CS-26-0885` match 05, 08 and 09.
- `ConsolidatedIndicator` false fits a single shipper's consignment; `CarrierAssignedID` `FB4-26-031/2` builds on the journey ID.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416`: suspected a mismatch with the lot in the despatch advice — not a finding here because `TraceID` need not equal the lot number; the difference is raised in the despatch advice review (08) as a cross-document point.
- `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:BuildingNumber` = `31`: suspected a business address misused as an origin region — refuted because the goods are produced at Rinova's plant at that address, and an address is a valid, if precise, rendering of the region of production.
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TakeoverTransportEvent/cbc:OccurrenceTime` = `09:00:00`: suspected that "the receiver's takeover" means the consignee — refuted because in the main carriage stage the receiver of the goods from the consignor is the carrier, and 09:00 fits the pickup window.
- `/Waybill/cbc:CarrierAssignedID` = `FB-CMNI-26-0882`: suspected that the carrier's number reuses the buyer's order number 0882 — refuted as a finding because the carrier's own numbering may coincide; nothing in the flow says the numbers are linked.
