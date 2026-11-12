# LLM review: 06-Waybill.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/06-Waybill.xml`, Git blob `98b3edab06331ce10e3457361c14ccae3bf60af1` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/06#F1 · High · "Actual" despatch after the waybill was issued
- XPath: `/Waybill/cbc:IssueDate` = `2026-04-19`
- XPath: `/Waybill/cbc:IssueTime` = `09:38:00`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchDate` = `2026-04-19`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `13:30:00`
- Why: ActualDespatchDate/Time are "the actual despatch (pickup)". The waybill is issued on 2026-04-19 at 09:38 and states as actual a despatch at 15:10 the same day, five and a half hours later, and after the loading at 13:30, which is also after the issue time. Only the takeover (09:00) precedes the issue. An actual event cannot lie after the issue time of the document that reports it. Under the CMNI (own knowledge) the consignment note is made out after the carrier has taken over the goods; the note "Original, with the goods" in the distribution fits an issue at departure. Verified in the merge: the export declaration (`05-ExportCustomsDeclaration.xml`, 16:08) and the despatch advice (`08-DespatchAdvice.xml`, 17:57) are issued after 15:10, so a later issue time would still precede them.
- Condition: every actual date and time in the waybill is at or before its issue date and time; events still planned at issue are not stated as actual.
- Options: (a) issue the waybill after loading and despatch (e.g. about 15:30 on 2026-04-19) (preferred: it fits the CMNI practice and the "original with the goods", and the later documents still follow); (b) keep the morning issue and state the despatch as planned (pickup window or estimate) instead of actual. Broad preferred (b); logistics and context preferred (a).
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### plastics/06#F2 · High · CO2e emission about a hundredth of what the stated diesel energy produces
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cbc:EnergySourceTypeCode` = `DIESEL`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cbc:AllocatedEnergyMeasure` = `5400`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cac:EnvironmentalEmission/cbc:ValueMeasure` = `14.3`
- Why: Recalculated in the merge (own knowledge, EN 16258 default factors for diesel: 2.67 kg CO2e per litre tank-to-wheel, 3.24 kg CO2e per litre well-to-wheel, 35.9 MJ = 9.97 kWh per litre): 0.268 kg CO2e/kWh TTW, 0.325 kg CO2e/kWh WTW. 5 400 kWh × 0.268 = 1 447 kg (TTW); 5 400 × 0.325 = 1 755 kg (WTW). The stated 14.3 kg implies 14.3 / 5 400 = 0.0026 kg/kWh, about 1/100 of any diesel factor, so emission × factor = energy does not hold. 5 400 kWh is about 540 l (about 455 kg) of diesel, 45 kWh per tonne of cargo, plausible for an inland barge voyage of a few hundred km over about three days (`EstimatedTransitPeriod` 3 DAY; 0.05–0.15 kWh per tonne-km, own knowledge). The emission is the value that does not fit. The parts counted this as the only energy allocation in the world.
- Condition: `ValueMeasure` = `AllocatedEnergyMeasure` × a diesel emission factor (about 0.27 kg CO2e/kWh TTW or 0.32 kg CO2e/kWh WTW, i.e. about 1 450 or 1 750 kg for 5 400 kWh), with the scope clear; or both values change together so that the factor is in that range.
- Options: (a) keep 5 400 kWh and set the emission to about 1 450 kg (TTW) or 1 750 kg (WTW), stating which (preferred: the energy fits the voyage); (b) keep 14.3 kg and reduce the energy to about 45–55 kWh, which no longer fits 120 t over three days.
- Needs decision: no
- From: broad (F1), logistics (F2)

### plastics/06#F3 · High · The note says three originals, the distribution gives the consignor only an electronic copy
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Rivermouth Packaging`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`
- Why: `DocumentDistribution` is "a list of interested parties to whom this document is distributed". The note says the consignment note is made out in three originals, for consignor, consignee and carrier (as the CMNI provides, own knowledge). The distribution gives an original only to the consignee (with the goods); the consignor (Rinova, `/Waybill/cac:ConsignorParty`) receives an electronic copy. Free text and the structured values next to it contradict each other (section 6: High). The carrier keeping its own original needs no distribution entry.
- Condition: the note and the distribution agree on who receives an original and who a copy.
- Options: (a) give Rinova the consignor's original in the distribution (preferred: it is what the note and CMNI practice describe); (b) change the note to what the distribution says.
- Needs decision: no
- From: parties (F1, High), logistics (F3, High), broad (F7, Medium), context (F10, Low)

### plastics/06#F4 · Medium · ShippingOrderID holds the consignment ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `RR-CS-26-0885`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's own ID, repeated two levels down. The shipper's instruction for this carriage is the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `RR-TR-26-0884`), which the plan 04 answers. One kind of identifier is used as another (section 4.5).
- Condition: `ShippingOrderID` holds the ID of the shipper's instruction of the flow, or is absent.
- Options: (a) `RR-TR-26-0884` (preferred: the request is the shipper's instruction); (b) remove it, since the plan is referenced.
- Needs decision: no
- From: broad (F3), logistics (F4), context (F3)

### plastics/06#F5 · Medium · Province of Ferrano in Region instead of CountrySubentity
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "The political or administrative division of a country …, such as the name of its county, province, or state". The Bayvarran addresses of the flow put their state in CountrySubentity with a code. The parts counted 219 occurrences in 104 example files (`grep -rho --include='*.xml'`).
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; the province is in `cbc:CountrySubentity` (with a code if Urvania has a list).
- Options: (a) move to `CountrySubentity` (preferred: it is what the element is for, and matches the Bayvarran addresses); (b) keep in Region only if the world defines it as an economic region.
- Needs decision: no
- From: broad (F8), parties (F2), context (F5)

### plastics/06#F6 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language in `Language/ID`. The parts counted 362 LocaleCode elements in 213 example files, all `en`.
- Condition: every LocaleCode holds a locale from a list its listID names (e.g. `en-XB`), or is absent.
- Options: (a) drop LocaleCode where the locale has no use in the document (preferred, aligned with the wood flow's merges; parties preferred it too); (b) a locale such as `en-XB` with a locale list as listID (broad and context preferred this).
- Needs decision: no
- From: broad (F9), parties (F3), context (F6)

### plastics/06#F7 · Medium · Freight rate per tonne carried as base amount, without a multiplier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:BaseAmount` = `1495`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`
- Why: BaseAmount is "The monetary amount to which the multiplier factor is applied in calculating the amount of this allowance or charge". 179 400 = 1 495 × 120 t, so 1 495 is the rate per tonne (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `1495`), and no MultiplierFactorNumeric is given: by its definition a base of 1 495 cannot give 179 400. UBL has `PerUnitAmount` for this ("the total allowance or charge is calculated by multiplying the per unit amount by the quantity of items").
- Condition: the charge's amount follows from its stated basis (a per-unit amount × the chargeable quantity, or base amount × multiplier); Amount stays 179 400 XUF.
- Options: (a) move 1 495 to `PerUnitAmount` (preferred: the dedicated element; the quantity is in `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableQuantity` = `120`); (b) drop BaseAmount and leave the rate to the freight invoice (broad, context); (c) BaseAmount 1 495 with MultiplierFactorNumeric 120.
- Needs decision: no
- From: broad (F6), money (F1), context (F4)

### plastics/06#F8 · Medium · Net volume is the volume of solid polyethylene, not of the granulate in the bags
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:NetVolumeMeasure` = `130`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:NetWeightMeasure` = `120000`
- Why: NetVolumeMeasure is "The volume contained by a goods item, excluding the volume of any packaging material". Recalculated in the merge: 120 000 kg ÷ 920 kg/m³ (the item's density, `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[1]/cbc:ValueQuantity` = `0.92` g/cm³) = 130.4 m³: the volume of the polymer as a solid block. PE granulate and regranulate pour at a bulk density of about 0.50–0.60 t/m³ (own knowledge), so 120 t fill about 200–240 m³ (1.67–2.0 m³ per one-tonne bag). The gross volume of 204 m³ (1.70 m³ per bag, 0.59 t/m³) is consistent with that. The difference gross − net would be 74 m³ of packaging material; 120 bags × 4 kg = 480 kg of woven PP (gross − net weight) occupy about 0.5 m³ at about 0.9 t/m³. Net and gross volume therefore do not fit each other.
- Condition: the net volume is the volume of the granulate as packed (its bulk volume, just below the gross volume), or the element is absent.
- Options: (a) set it to about 200–203 m³ (preferred: consistent with the gross volume and the bulk density); (b) drop it: the gross volume is what the barge needs.
- Needs decision: no
- From: broad (F10, Low), logistics (F8, Low, first part)

### plastics/06#F9 · Medium · ReturnableQuantity counts the bags, not returnable goods
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ReturnableQuantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ReturnableMaterialIndicator` = `true`
- Why: GoodsItem/ReturnableQuantity is "The number of units in the goods item that may be returned". The goods item is 120 t of granulate sold outright (`/Waybill/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`, unit TNE); the granulate is not returned. What is returnable are the jumbo bags, which the package already states. The value (unit EA) counts the bags in an element about the goods.
- Condition: `ReturnableQuantity` is absent, or counts units of the goods that may be returned; returnable packaging is stated on the package.
- Options: (a) remove it and keep the package's indicator (preferred); (b) count returnable bags on the package or a handling unit.
- Needs decision: no
- From: broad (F4), logistics (F6), context (F2)

### plastics/06#F10 · Medium · One package said to contain 120 items stands for 120 one-tonne bags
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ID` = `RR-JB-0416`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:Quantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingType` = `Jumbo bag of one tonne with four lifting loops`
- Why: Package/Quantity is "The quantity of items contained in this package". As encoded there is one package, a jumbo bag "of one tonne", containing 120 items (EA). What is meant is 120 bags each holding 1 t. A single package ID for all 120 bags identifies none of them. The waybill has no package count (no `TotalPackagesQuantity` on the consignment, verified in the merge), so the number of packages, a basic entry of a consignment note, is not stated in its own element.
- Condition: the number of packages (120 JB) is stated in a package-count element; where a package is described, its quantity is what one bag contains (1 t); a package ID identifies one bag (or is absent).
- Options: (a) `Consignment/TotalPackagesQuantity` = 120 (or a TransportHandlingUnit with its package count) and `ContainingPackage/Quantity` = 1 TNE (preferred: both facts in their own elements); (b) describe the bags as transport handling units.
- Needs decision: no
- From: broad (F5), logistics (F5)

### plastics/06#F11 · Low · Value for duties in a transport document
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ValueAmount` = `9984000`
- Why: GoodsItem/ValueAmount is "The amount on which a duty, tax, or fee will be assessed". The waybill assesses nothing; the customs values are declared in 05 and 09, and the carrier's liability is covered by `DeclaredForCarriageValueAmount`. Money checked that the value equals the customs values (99 840.00 XBL at 100 XUF = 1 XBL in 09); it is consistent, but has no purpose here.
- Condition: the waybill carries no value for duties unless a duty or fee is assessed on it in this document.
- Options: remove it (preferred).
- Needs decision: no
- From: context (F7)

### plastics/06#F12 · Low · Value declared for carriage without a valuation charge
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:DeclaredForCarriageValueAmount` = `9984000`
- XPath: `/Waybill/cbc:AdValoremIndicator` = `false`
- Why: The element is "The value of this goods item, declared by the shipper or his agent solely for the purpose of varying the carrier's level of liability from that provided in the contract of carriage". Declaring the full goods value raises the carrier's liability far above the CMNI limits (own knowledge: 666.67 SDR per package or 2 SDR per kg), for which carriers usually charge a valuation surcharge. Neither the plan (04) nor the freight invoice (07, one freight line) has one. A reason for the declared value exists: the goods are uninsured (`09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:InsuranceValueAmount` = `0.00`). Whether its cost is part of the story is a decision. (The AdValoremIndicator itself does not contradict the declared value; see "Considered and refuted".)
- Condition: the declared value is agreed in the transport contract and its cost is billed or stated as included in the freight, or the element is absent.
- Options: (a) keep it and add a valuation charge to the plan, the waybill and the freight invoice (preferred by money: the goods travel uninsured); (b) drop it and rely on the CMNI limits.
- Needs decision: yes
- From: money (F2)

### plastics/06#F13 · Low · Height of one bag given as dimension of the whole goods item
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:MeasurementDimension/cbc:Measure` = `1300`
- Why: MeasurementDimension is "a measurable dimension of this goods item". The goods item is 120 bags (204 m³); 1 300 mm is the height of one bag (1.70 m³ per bag at 1.3 m gives a footprint of 1.31 m², about 1.14 m × 1.14 m, a full, bulging FIBC: plausible, recalculated in the merge). As a dimension of the goods item it describes neither the stowed cargo nor a package.
- Condition: the dimension is on the package it measures, or describes the goods item as a whole.
- Options: (a) move it to `ContainingPackage/MeasurementDimension` (preferred); (b) drop it.
- Needs decision: no
- From: broad (F13), logistics (F8, second part)

### plastics/06#F14 · Low · Lot identifier differs from the despatch advice
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416`
- Why: TraceID is "An identifier for use in tracing this goods item". The despatch advice gives the lot of the same goods as `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `RR-PE-0416`. Two strings that look like the same lot make tracing from the consignment note to the despatch advice uncertain. Logistics argued that a TraceID need not equal the lot number, which is true; but nothing in the flow links the two, and a contradiction with another example describing the same object is a finding of this review (section 4).
- Condition: the waybill and the despatch advice use the same lot identifier, or the relationship between the two identifiers is explicit.
- Options: (a) one lot number in both (preferred); (b) keep a separate trace ID and add the lot number.
- Needs decision: no
- From: broad (F21); logistics considered and refuted it (see below)

### plastics/06#F15 · Low · Origin "region" is the plant's business street address
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:AddressTypeCode` = `BUSINESS`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:BuildingNumber` = `31`
- Why: GoodsItem/OriginAddress is "The region in which the goods have been produced or manufactured, according to criteria laid down for the purposes of application of the customs tariff …". A business street address is a postal address, not a region of origin in the tariff sense. Logistics refuted this (an address is a valid, precise rendering of the region of production); the merge keeps the finding at Low because the definition ties the region to tariff criteria, which a street and building number do not serve, and the address type BUSINESS says it is a business address.
- Condition: the origin address names the region of production (province and country), or is absent.
- Options: (a) reduce it to province and country (preferred); (b) drop it, the items of 05 and 09 give the country of origin.
- Needs decision: no
- From: broad (F12), context (F8); logistics considered and refuted it

### plastics/06#F16 · Low · Latest delivery date "allowed by the buyer" has no source in the flow
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23`
- Why: LatestDeliveryDate is "The latest date of delivery allowed by the buyer". The buyer's order states no delivery date (verified in the merge: `01-Order.xml` has only its issue date and a validity end 2029-12-31), and the plan requires completion by `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-04-22`. The 23rd comes from nowhere in the flow. Context refuted a contradiction between the 23rd and the plan's 22nd (one is the buyer's limit, the other the carrier's commitment); the merge agrees that they do not contradict, but the missing source stands.
- Condition: the latest delivery date can be traced to the buyer (order) and is consistent with the plan, or is absent.
- Options: (a) add the buyer's delivery date to the order and keep 2026-04-23 (preferred by logistics); (b) drop it and rely on the plan's service end.
- Needs decision: no
- From: broad (F11), logistics (F9)

### plastics/06#F17 · Low · Issue location names the carrier, not a place
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Fiumella Barges`
- Why: IssueLocation is "The location where this waybill was issued"; the value is the company with no address or identifier. The place of issue is a standard entry of a consignment note; with F1 it would be the loading quay (`/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`) or the carrier's office.
- Condition: IssueLocation names or locates a place.
- Options: (a) name the place of issue (the quay, or Ferrano) (preferred); (b) drop it.
- Needs decision: no
- From: broad (F14), parties (F9), logistics (F10), context (F9)

### plastics/06#F18 · Low · The plan is referenced twice, both times with an ID only
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ShipmentDocumentReference/cbc:ID` = `FB-TEP-26-0886`
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FB-TEP-26-0886`
- Why: The same transport execution plan (04) is referenced on the goods item and on the document, neither with a document type, so neither says what it refers to; the second adds nothing.
- Condition: the plan is referenced once, with a document type.
- Options: (a) keep the document-level reference with `DocumentTypeCode` (preferred); (b) keep both, each with a type.
- Needs decision: no
- From: broad (F15), logistics (F11)

### plastics/06#F19 · Low · Voyage number in the element for a regular service schedule
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031`
- Why: TransportMeans/JourneyID is "An identifier for the regular service schedule of this means of transport". `FB4-26-031` reads as voyage 31 of 2026 of Fiumella IV, a one-off voyage number, not a schedule. The same value is in 04.
- Condition: JourneyID identifies a regular service, or the voyage number is carried in an element for a voyage (e.g. the stage's or consignment's carrier-assigned ID, as `CarrierAssignedID` `FB4-26-031/2` already does).
- Options: (a) carry the voyage number in the carrier-assigned ID only (preferred); (b) keep it if Fiumella runs a scheduled liner service with that number.
- Needs decision: no
- From: broad (F16, first part)

### plastics/06#F20 · Low · Exportation event without a place; completion indicator only on the discharge
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false`
- Why: The exportation event has no location; the river border customs post is named only in `05-ExportCustomsDeclaration.xml`. Only the discharge carries a completion indicator, although loading and exportation also lie after the issue time; the indicator implies by absence that the others are complete (IND6).
- Condition: the exportation event has its place; CompletionIndicator is used for every event whose status matters, or for none.
- Options: border location on the exportation event and indicator dropped (preferred).
- Needs decision: no
- From: broad (F16, second and third part)

### plastics/06#F21 · Low · Rivermouth's bank account in a document that does not use it
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". The consignee pays nothing under the waybill: the freight is invoiced to Rinova (`07-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`). The account is copied master data (section 4.8). Money counted it in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml'`); it has a purpose in `11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
- Condition: the consignee party in the waybill carries no financial account unless the waybill uses it (e.g. freight collect or cash on delivery).
- Options: drop it (preferred).
- Needs decision: no
- From: broad (F17, first part), money (F3), parties (F5), context (F11)

### plastics/06#F22 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: PartyAuthorization is "An authorization issued to this party"; this is Rinova's permit to recover plastic waste (Basel Annex IV R3). The goods are recycled PE granulate classified as a product (HS 390110, not HS 3915 waste); nothing in the waybill depends on the permit. Context counted it in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311`): master data copied into every document (IND5).
- Condition: the permit appears only in documents that act on it, or the document says why it is relevant.
- Options: (a) drop it here (preferred: the goods are a product); (b) if the recycled-content claim is to rest on it, link it to the item's environmental certificate instead.
- Needs decision: no (parties said yes because option (b) would keep it as evidence; removing it changes no story, so the merge, like context, says no)
- From: broad (F17, second part), parties (F6), context (F12)

### plastics/06#F23 · Low · Contacts do not fit the role the party has in this document
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Rinova is here the consignor that hands over the goods (shipping), yet its contact is sales customer service; the consignee's contact signs for the goods (`/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`), yet it is an "Order desk" with a customer-service job title in Sales (a buyer's order desk is not a sales department). The parties carry one generic contact in every document of the flow.
- Condition: each contact handles the task the party has in this document, or is absent where the document needs none.
- Options: (a) role-specific contacts per party (preferred); (b) drop contacts the document does not need.
- Needs decision: no
- From: broad (F18), parties (F4), context (F13)

### plastics/06#F24 · Low · Signature ID repeats the carrier prefix before the waybill number
- XPath: `/Waybill/cac:Signature/cbc:ID` = `FB-SIG-FB-WB-26-0890`
- Why: The ID is `FB-SIG-` before the full waybill number, which already starts with `FB-`; it reads as a generator pattern. Other signatures of the flow use other patterns (`FB-SIG-882` in 04, `RR-SIG-EX-plastics` in 05, with the flow name).
- Condition: signature IDs follow a numbering the signing party would use.
- Options: e.g. `FB-SIG-26-0890` (preferred).
- Needs decision: no
- From: broad (F19)

### plastics/06#F25 · Low · All three companies registered on 1 January 1996
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Three companies in two registers are registered on New Year's Day 1996, a day registers are normally closed; the parts counted 271 occurrences in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01'`), while some parties have specific dates. It reads as a default value (IND5).
- Condition: each company's RegistrationDate belongs to its own history, or the shared date is explained in the world's story, or the element is absent.
- Options: (a) individual dates from each company's history (preferred); (b) record a 1996 (re-)registration in the story; (c) drop it.
- Needs decision: yes (it depends on the world's company histories; parties said no, broad and context yes; aligned with the wood flow's merges)
- From: broad (F20), parties (F7), context (F14)

### plastics/06#F26 · Low · Italian text tagged as English
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:StreetName[2]` = `Via del Riciclo`
- Why: Each repeated rendering must be in the language its `languageID` names. The second renderings of Urvanian street names are Italian ("Via del Riciclo", "Banchina del Fiume") and the English legal form is Italian with an English gloss, while tagged `en-XU`/`en-XB` (or untagged in an English document). Bayvarran streets of the flow are English (`Estuary Road`). If the world uses Italianate exonyms for Urvanian places (as `Ferrano` for `Ruldraz`), that convention is not visible in the documents; for the legal form, which is not a proper name, the case is stronger. Parties counted the pattern in 101 of 250 examples.
- Condition: every rendering tagged `en-…` is English or a proper name used as such in English, and the convention is recorded.
- Options: (a) record the convention in the world's story and keep the street names, and render the legal form in English (preferred, aligned with the wood flow); (b) translate the renderings ("Recycling Street", "River Quay"); (c) drop the second rendering.
- Needs decision: yes
- From: parties (F8)

## Checked and consistent
- Weights (recalculated in the merge): gross 120 480 kg − net 120 000 kg = 480 kg = 120 bags × 4 kg, plausible for a one-tonne woven-PP FIBC with four loops (about 2.5–5 kg, own knowledge); net = net-net = chargeable weight, as the bags are the only packaging (broad, logistics).
- Gross volume: 204 m³ / 120 = 1.70 m³ per bag, 0.59 t/m³ including the bag, at the dense end of PE granulate bulk density (0.50–0.60 t/m³, own knowledge); see F8 for the net volume. The 1 210 GT dry barge carries 120 t / 204 m³ easily (broad, logistics).
- Emission factor recalculated: see F2 (TTW 0.268, WTW 0.325 kg CO2e/kWh for diesel; stated 0.0026).
- Freight: 1 495 XUF/t × 120 t = 179 400 XUF, equal to the line of `07-Invoice.xml` and to the freight deducted for the FOB value in 09 ((99 840 − 98 046) × 100 = 179 400) (broad, money, logistics, context).
- Declared value for carriage and ValueAmount 9 984 000 XUF = the goods' invoice value (10) and the customs values of 05 and 09 at 100 XUF = 1 XBL (broad, money).
- Reason code `FC` (UNCL 7161 "Freight service") fits the freight charge (money).
- Pickup window 08:00–16:00 contains takeover 09:00, loading 13:30 and despatch 15:10; vessel, journey, master, events and transit period agree with 04 (broad, logistics, context). Loading 120 bags in 100 minutes (0.8 min per bag) is feasible with several bags per lift (logistics, own knowledge).
- References: order `RP-PO-26-0882` line 1 resolves to 01; `FB-TEP-26-0886` to 04; shipment `RR-SH-26-0889` and consignment `RR-CS-26-0885` match 05, 08 and 09 (broad, logistics, context; flow index re-run in the merge).
- Parties: sender, carrier and signatory Fiumella; receiver and consignor Rinova; consignee Rivermouth match 04; identifiers, names, tax registrations and addresses agree across the flow apart from the language renderings in F26; ISIC codes fit (3830, 2220, 5022) (parties).
- `check_ids.py`: IBAN-like account passes (parties). `ConsolidatedIndicator` false fits a single shipper's consignment (logistics).

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false` next to a value declared for carriage: suspected contradiction — refuted because UBL defines the indicator by ad valorem duties, and a declared value raises the carrier's liability (CMNI art. 20) without making the freight ad valorem; the freight is per tonne (from broad, money, context; the missing valuation charge is F12).
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:NetNetWeightMeasure`: equal to the net weight — refuted because the jumbo bag is the only packaging (from broad).
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableWeightMeasure` = `120000`: the net, not the gross weight — refuted because the freight is agreed and invoiced per tonne of product, and the chargeable weight is what the contract makes it (from money).
- No statement who pays the freight (prepaid/collect) — refuted: nothing is implied by absence; the plan names Rinova as bill-to party and the freight is invoiced to Rinova (from money).
- `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` could be a real ISO 6523 ICD — refuted because the real register's ICDs stay far below 0990 (own knowledge) (from parties).
- `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BIC-shaped `BLUMXBLX` could be real — refuted because positions 5–6 carry the user-assigned code of a fictional country (from parties).
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416` differs from the lot of 08 — logistics refuted it (a TraceID need not equal the lot number); the merge disagrees and keeps it as F14 (from logistics).
- `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:BuildingNumber` = `31`: a business address as origin region — logistics refuted it (an address is a precise rendering of the region of production); the merge disagrees and keeps it as F15 (from logistics).
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TakeoverTransportEvent/cbc:OccurrenceTime` = `09:00:00`: takeover meaning the consignee's — refuted because in the main carriage the party taking over from the consignor is the carrier, and 09:00 fits the pickup window (from logistics).
- `/Waybill/cbc:CarrierAssignedID` = `FB-CMNI-26-0882`: reuses the order number 0882 — refuted as a finding: the carrier's numbering may coincide, nothing links them (from logistics).
- `/Waybill/cbc:CarrierAssignedID` and `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID`: duplicates — refuted: one identifies the waybill's shipment, the other the consignment on the voyage (from context).
- `/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23` contradicting the plan's end 2026-04-22 — refuted as a contradiction: one is the buyer's limit, the other the carrier's commitment (from context); the missing source is F16.

## Refuted in the merge
### logistics/F7 · Medium · Quantity and chargeable quantity are a weight, not a number of units
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableQuantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableWeightMeasure` = `120000`
- Why (logistics): `Quantity` is "the number of units making up this goods item" and `ChargeableQuantity` "the number of units in the goods item to which charges apply". Both are 120 TNE, a mass, repeating the net and chargeable weights; the units of the goods item are the 120 bags. The same use of `Quantity` is in 05 and 09.
- Condition (logistics): `Quantity` and `ChargeableQuantity` count units (bags) or are absent; weights stay in the weight elements.
- Options (logistics): drop `ChargeableQuantity` and make `Quantity` a count of bags or drop it.
- Refuted because: a UBL Quantity is "a counted number of non-monetary units, possibly including fractions" with a unit code, and the tonne is a legitimate unit for a bulk commodity sold and carried by the tonne. The freight is charged per tonne (07: 120 TNE × 1 495), so 120 TNE is exactly the number of units to which the charge applies, and it is the quantity the per-unit freight rate of F7 multiplies. That the same mass is also given in kg in the weight elements is a redundancy between elements of different meaning, not a misuse; the bag count belongs to the package (F10).

## Changed in the merge
- broad/F2, logistics/F1, context/F1 → F1: combined; logistics' and context's option (issue after despatch) preferred over broad's because the later documents of the flow still follow and the CMNI note fits; issue times of 05 and 08 checked.
- broad/F1, logistics/F2 → F2: combined; emission recalculated with EN 16258 per-litre factors (1 447 kg TTW / 1 755 kg WTW).
- parties/F1, logistics/F3, broad/F7, context/F10 → F3: combined at High (broad Medium, context Low) because free text contradicts the structured values next to it (section 6).
- broad/F6, money/F1, context/F4 → F7: combined; money's PerUnitAmount option preferred (dedicated element) over the others' "drop BaseAmount", which is kept as option (b).
- broad/F10, logistics/F8 (first part) → F8: raised from Low to Medium because gross − net volume would be 74 m³ of packaging material for 480 kg of bags (recalculated in the merge), so the element does not carry its definition's meaning; not High because the reading of "net volume" as solid volume is the point at issue.
- logistics/F8 → F8 and F13: split, because the net volume and the bag height are different problems.
- broad/F5, logistics/F5 → F10: combined; added that the waybill has no package count at all (checked in the merge).
- broad/F17 → F21 and F22: split into the bank account and the permit (different objects, different arguments); combined with money/F3, parties/F5, context/F11 and parties/F6, context/F12.
- parties/F6 → F22: Needs decision changed from yes to no (removal changes no story; aligned with context and the wood flow's merges).
- broad/F16 → F19 and F20: split, because the journey ID and the events/indicator are different problems.
- broad/F20, parties/F7, context/F14 → F25: combined; Needs decision yes (parties said no), aligned with the wood flow's merges.
- broad/F9, parties/F3, context/F6 → F6: preferred option set to dropping LocaleCode (as parties and the wood merges), broad's and context's en-XB kept as option (b).
- parties/F8 → F26: preferred option aligned with the wood flow (record the convention; English legal form).
- broad/F21 → F14: kept against logistics' refutation, with its argument added.
- broad/F12, context/F8 → F15: kept against logistics' refutation, with its argument added.
- All other findings combined without change of severity: broad/F3, logistics/F4, context/F3 → F4; broad/F8, parties/F2, context/F5 → F5; broad/F4, logistics/F6, context/F2 → F9; context/F7 → F11; money/F2 → F12; broad/F11, logistics/F9 → F16; broad/F14, parties/F9, logistics/F10, context/F9 → F17; broad/F15, logistics/F11 → F18; broad/F18, parties/F4, context/F13 → F23; broad/F19 → F24.
