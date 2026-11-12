# LLM review: 06-Waybill.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

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

### plastics/06#F1 · High · Emissions a hundred times too low for the stated diesel energy
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cbc:AllocatedEnergyMeasure` = `5400`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:EnergyConsumptionAllocation/cac:EnvironmentalEmission/cbc:ValueMeasure` = `14.3`
- Why: 5 400 kWh of diesel are about 454 kg of fuel (lower heating value about 11.9 kWh/kg) and emit about 0.27 kg CO2 per kWh tank-to-wheel, about 0.32 kg CO2e per kWh well-to-wheel (own knowledge, EN 16258 / ISO 14083 order of magnitude). That gives 1.4–1.7 t CO2e, not 14.3 kg. The stated values imply 2.6 g CO2e per kWh, about a hundredth of any diesel factor. Either the energy or the emission is wrong by a factor of about 100. This is the only energy allocation in the world (counted with a script over `world/examples/*/*.xml`).
- Condition: emission = energy × a diesel emission factor that is stated or can be traced (about 0.27–0.32 kg CO2e/kWh), with the scope (TTW or WTW) clear.
- Options: (a) keep 5 400 kWh (about 0.11 kWh per tonne-km over some 400 km, plausible for inland waterway) and set the emission to about 1 440 kg TTW or 1 730 kg WTW (preferred); (b) keep 14.3 kg and reduce the energy to about 54 kWh, which would be implausibly low for 120 t on a 3-day voyage.
- Needs decision: no

### plastics/06#F2 · High · "Actual" despatch after the waybill was issued
- XPath: `/Waybill/cbc:IssueTime` = `09:38:00`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`
- Why: The waybill is issued on 2026-04-19 at 09:38; it states as actual a despatch at 15:10 the same day (`ActualDespatchDate` `2026-04-19`), five and a half hours in the future, after the loading planned for 13:30. An actual event cannot lie after the issue time of the document reporting it.
- Condition: every actual time in the waybill is before its issue time, or the despatch time is given as planned/estimated.
- Options: (a) state the planned departure as an estimate (e.g. latest pickup or the shipment stage's departure) and drop the actual despatch (preferred: the waybill is issued at takeover); (b) move the issue time after 15:10 if the consignment note is issued at departure, and check the other documents' times against it.
- Needs decision: no

### plastics/06#F3 · Medium · Consignment ID given as shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `RR-CS-26-0885`
- Why: ShippingOrderID is "An identifier … of the Shipping Order or Forwarding Instruction associated with this shipment". `RR-CS-26-0885` is the consignment's ID (`/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `RR-CS-26-0885`). The instruction to the carrier in this flow is the transport request `RR-TR-26-0884` (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `RR-TR-26-0884`). One kind of identifier is used as another (section 4.5).
- Condition: `ShippingOrderID` holds the ID of the shipper's instruction (the transport request), or is absent.
- Options: (a) `RR-TR-26-0884` (preferred); (b) remove it, since the plan is referenced.
- Needs decision: no

### plastics/06#F4 · Medium · Returnable quantity counts the bags, not the goods
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ReturnableQuantity` = `120`
- Why: ReturnableQuantity is "The number of units in the goods item that may be returned". The goods item is 120 t of granulate (`/Waybill/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`, unit TNE); the granulate is not returned. What is returnable are the 120 jumbo bags (`/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ReturnableMaterialIndicator` = `true`), so the element is used with a meaning other than its definition; its unit (EA) also differs from the goods item's unit.
- Condition: `ReturnableQuantity` is absent, or counts units of the goods item that may be returned; the returnable packaging is expressed on the package.
- Options: (a) drop it and rely on the package's returnable indicator (preferred); (b) keep it only if part of the goods may be sent back.
- Needs decision: no

### plastics/06#F5 · Medium · One package with a quantity of 120 stands for 120 bags
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:Quantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ID` = `RR-JB-0416`
- Why: Package/Quantity is "The quantity of items contained in this package". Each jumbo bag holds one tonne (item description: "in jumbo bags of 1 tonne"), so a package containing 120 items does not exist; the value is the number of bags. A single package ID for all 120 bags also identifies none of them.
- Condition: the waybill states the number of packages as a count of packages (e.g. on the consignment or goods item) and, where a package is described, its quantity is what one bag contains (1 t).
- Options: (a) package quantity 1 TNE per bag with the number of packages (120 JB) in a package-count element of the consignment or goods item (preferred); (b) describe the 120 bags as transport handling units.
- Needs decision: no

### plastics/06#F6 · Medium · Freight rate per tonne carried as base amount
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:BaseAmount` = `1495`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`
- Why: BaseAmount is "The monetary amount to which the multiplier factor is applied in calculating the amount". 179 400 = 1 495 × 120, so 1 495 is the rate per tonne and the 120 t are the multiplier; no `MultiplierFactorNumeric` is given, so Amount cannot be derived from BaseAmount. A rate per unit is not a base amount.
- Condition: the charge's amount follows from its stated basis (base amount × multiplier, or a per-unit rate stated in text or price form), and nothing implies that 1 495 is the amount the charge is calculated on.
- Options: (a) drop `BaseAmount` and state the rate in the reason text ("1 495 XUF per tonne") (preferred); (b) keep `BaseAmount` 1 495 with `MultiplierFactorNumeric` 120 if the world accepts a multiplier that is not a percentage.
- Needs decision: no

### plastics/06#F7 · Medium · Distribution list contradicts the note on three originals
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`
- Why: The note says the consignor receives an original; the distribution list gives the consignor (Rinova) an electronic copy and names an original only for the consignee. The carrier's original is not listed either (it keeps it, which may be fine), so the structured list and the note disagree about the consignor.
- Condition: the distribution list and the note agree on who receives which original or copy.
- Options: (a) give Rinova the consignor's original in the distribution list (preferred); (b) change the note if the consignor only receives a copy.
- Needs decision: no

### plastics/06#F8 · Medium · Province of Urvanian addresses in Region
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/06#F9 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/06#F10 · Low · Net volume is the volume of solid polymer, not of the granulate
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:NetVolumeMeasure` = `130`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`
- Why: NetVolumeMeasure is "The volume contained by a goods item, excluding the volume of any packaging material". 120 000 kg ÷ 0.92 g/cm³ (the item's density) = 130.4 m³ is the volume of solid PE. Granulate has voids: at a bulk density of about 0.55–0.6 t/m³ (own knowledge) 120 t of granulate fill about 200–218 m³, which is what the gross volume (204 m³, 1.7 m³ per bag) shows. The volume contained by the bags is therefore close to 200 m³, not 130 m³.
- Condition: the net volume is the volume of granulate in the bags (consistent with its bulk density and with the gross volume), or it is absent.
- Options: (a) set it to the bulk volume (about 200 m³) (preferred); (b) drop it; the gross volume is what the barge needs.
- Needs decision: no

### plastics/06#F11 · Low · Latest delivery date "allowed by the buyer" has no source
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23`
- Why: LatestDeliveryDate is "The latest date of delivery allowed by the buyer". The buyer's order states no delivery date (`01-Order.xml`), and the plan requires completion by 2026-04-22 (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-04-22`), so the 23rd is neither the buyer's stated date nor the agreed service end. The penalty per day late in the plan needs one clear deadline.
- Condition: the latest delivery date in the waybill can be traced to the buyer (order) or to the agreed plan, and the documents agree on it.
- Options: (a) use 2026-04-22 from the plan, or give the buyer's date in the order (preferred); (b) drop it.
- Needs decision: no

### plastics/06#F12 · Low · Origin "region" is the plant's business address
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:AddressTypeCode` = `BUSINESS`
- Why: GoodsItem/OriginAddress is "The region in which the goods have been produced or manufactured, according to criteria laid down for … the customs tariff …". A full business street address (Via del Riciclo 31) is a postal address, not a region of origin; the origin country is already given on the item.
- Condition: the origin address names the region of production (e.g. province and country), not a postal business address.
- Options: (a) reduce it to province and country (preferred); (b) drop it.
- Needs decision: no

### plastics/06#F13 · Low · Height of one bag given as dimension of the whole goods item
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:MeasurementDimension/cbc:Measure` = `1300`
- Why: The goods item is 120 bags (204 m³); a height of 1 300 mm is the height of one bag (1.7 m³ per bag at 1.3 m height gives a footprint of 1.31 m², about 1.14 m × 1.14 m, plausible). As a dimension of the goods item it describes neither the stowed cargo nor a package.
- Condition: the dimension is stated on the package it measures, or describes the goods item as a whole.
- Options: (a) move it to the package (preferred); (b) drop it.
- Needs decision: no

### plastics/06#F14 · Low · Issue location is a company name
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Fiumella Barges`
- Why: IssueLocation is "The location where this waybill was issued"; the value names the carrier, not a place (the checklist: "the name is the place, not the company").
- Condition: the issue location names a place (e.g. Ferrano, or the quay).
- Options: name the place (preferred).
- Needs decision: no

### plastics/06#F15 · Low · The plan is referenced twice, both times with only an ID
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ShipmentDocumentReference/cbc:ID` = `FB-TEP-26-0886`
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FB-TEP-26-0886`
- Why: The same transport execution plan is referenced on the goods item and on the document, neither with a type; the second reference adds nothing.
- Condition: the plan is referenced once, with its document type.
- Options: keep the document-level reference with `DocumentTypeCode` (preferred).
- Needs decision: no

### plastics/06#F16 · Low · Voyage number in the element for a regular service; exportation event without a place
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false`
- Why: JourneyID is "An identifier for the regular service schedule"; this is a one-off voyage. The exportation event has no location (the customs post at the river border is only in `05-ExportCustomsDeclaration.xml`). Only the discharge carries a completion indicator, although the loading and exportation are also still in the future at issue time; the indicator implies something about the others by absence.
- Condition: `JourneyID` identifies a regular service (or the voyage number is carried elsewhere); the exportation event has its place; `CompletionIndicator` is used consistently or not at all.
- Options: as in `04-TransportExecutionPlan.xml`; preferred: border location on the exportation event, indicator dropped.
- Needs decision: no

### plastics/06#F17 · Low · Copied master data: consignee's bank account and the waste permit
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The consignee pays nothing under the waybill (freight is for the consignor's account, CPT), and a waste-recovery permit has no role in carrying a product; both are master data the waybill does nothing with.
- Condition: neither appears in the waybill.
- Options: remove both (preferred).
- Needs decision: no

### plastics/06#F18 · Low · Contacts do not fit the roles
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- Why: The consignor's contact for the consignment note is sales customer service, and the consignee's contact, who signs for the goods (`/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`), is a sales order desk rather than goods receipt.
- Condition: contacts fit the transport roles.
- Options: role-specific contacts (preferred) or neutral general contacts.
- Needs decision: no

### plastics/06#F19 · Low · Signature ID repeats the carrier prefix
- XPath: `/Waybill/cac:Signature/cbc:ID` = `FB-SIG-FB-WB-26-0890`
- Why: The ID is the prefix `FB-SIG-` placed before the full waybill number, which already starts with `FB-`; it reads as a generator pattern, not an identifier the carrier would assign. Other signatures of the flow use other patterns (`FB-SIG-882` in `04`, `RR-SIG-EX-plastics` in `05`).
- Condition: signature IDs follow one convention the signing party would use.
- Options: e.g. `FB-SIG-26-0890` (preferred).
- Needs decision: no

### plastics/06#F20 · Low · All three companies registered on 1 January 1996
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for three companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

### plastics/06#F21 · Low · Lot identifier differs from the despatch advice
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416`
- Why: TraceID is "An identifier for use in tracing this goods item". The despatch advice gives the lot of the same goods as `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `RR-PE-0416`. Two different strings for the same lot make tracing from the consignment note to the despatch advice impossible, unless they are deliberately different identifiers, which nothing says.
- Condition: the waybill and the despatch advice use the same lot identifier for the goods, or the relationship between the two identifiers is explicit.
- Options: (a) use one lot number in both (preferred); (b) keep a separate trace ID and add the lot number too.
- Needs decision: no

## Checked and consistent
- Weights: gross 120 480 kg = net 120 000 kg + 120 bags × 4 kg; net = net-net because the bags are the only packaging; chargeable weight 120 000 kg and chargeable quantity 120 t agree with the freight 120 × 1 495 = 179 400 XUF, which is also the freight invoiced in `07-Invoice.xml`.
- Volume and bags: 204 m³ / 120 = 1.7 m³ per bag, i.e. 0.59 t/m³ bulk density for 1 t, plausible for PE granulate; 4 kg tare per woven-PP FIBC is usual (own knowledge). The barge (1 210 GT dry barge) carries 120 t / 204 m³ easily.
- Pickup window 08:00–16:00 contains takeover 09:00 and loading 13:30; events and vessel data agree with `04-TransportExecutionPlan.xml`.
- References: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OrderLineReference/cac:OrderReference/cbc:ID` = `RP-PO-26-0882` resolves to `01-Order.xml` line 1; `FB-TEP-26-0886` resolves to `04-TransportExecutionPlan.xml`.
- Declared value for carriage 9 984 000 XUF = the goods' invoice value (`10-Invoice.xml`).

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator`: `false` although a value is declared for carriage — refuted: declaring a value raises the carrier's liability (CMNI art. 20(4)) but does not make the freight ad valorem; the freight here is per tonne.
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:NetNetWeightMeasure`: equal to the net weight — refuted: the jumbo bag is the only packaging and is excluded from both.
