# LLM review: 08-Waybill.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/08-Waybill.xml`, Git blob `72164dc3855513c969135349f0d20e5d5cef08c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 60500a8 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/08#F1 · High · Waybill issued in the morning but reports the afternoon pickup, departure and next-day border check
- XPath: `/Waybill/cbc:IssueDate` = `2026-03-23`
- XPath: `/Waybill/cbc:IssueTime` = `08:16:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceDate` = `2026-03-24`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceTime` = `07:45:00`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cac:FuelConsumption/cbc:FuelConsumptionMeasure` = `61`
- Why: The consignment note is issued on 2026-03-23 at 08:16. It already states that the goods were "Received in apparent good order" with seals on the trailer, an actual pickup at 15:05 and an actual departure at 16:20 that day, an examination (seal check) on 2026-03-24 at 07:45, and the fuel consumed on the delivery (61 l), which is known only after the trip. Actual events must lie before the issue time; the border examination is a day in the future.
- Condition: Every actual event, receipt remark and consumption reported in the waybill lies before its issue date and time; events after issue are absent or given as planned/estimated.
- Options: (a, preferred) issue the waybill at loading (after 15:05, before 16:20) with pickup and receipt remarks only, and leave the departure, examination and fuel consumption to the transportation status or a later version; (b) make this a later version of the waybill issued after delivery, with a `VersionID` and issue time after 2026-03-25 09:40.
- Needs decision: no

### road/08#F2 · High · Gross volume smaller than the volume of the handling units
- XPath: `/Waybill/cac:Shipment/cbc:GrossVolumeMeasure` = `41.5`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[1]/cbc:Measure` = `1850`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[2]/cbc:Measure` = `650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[1]/cbc:Measure` = `1200`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[2]/cbc:Measure` = `800`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[3]/cbc:Measure` = `900`
- Why: `GrossVolumeMeasure` is "The total volume of the goods in this shipment, including packaging". Handling units 1–24 each measure 1.85 × 0.65 × 1.65 m = 1.984 m³, together 47.62 m³; unit 25 measures 1.2 × 0.8 × 0.9 m = 0.864 m³. The units add up to 48.48 m³, but the shipment states 41.5 m³, 7 m³ less than its own packaging.
- Condition: The gross volume is at least the sum of the handling units' volumes as given by their dimensions (48.48 m³ with the present dimensions).
- Options: (a, preferred) correct the gross volume to the units' volume; (b) correct the units' dimensions if 41.5 m³ is right.
- Needs decision: no

### road/08#F3 · High · Waybill says the 3PL declares the export and the customs administration issues the declaration; the declaration is Valdara's
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:ID` = `VI-EX-26-0155`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The instruction says "The export is declared by the 3PL in Ferrano" (Castrano). `CustomsDeclaration/IssuerParty` is "The Party who issues this Customs Declaration" and names the Customs Administration of Urvania, which receives declarations and does not issue them. The export declaration VI-CD-26-0156 itself is part of Valdara's export declaration, numbered and signed by Valdara with no agent or declarant named. Three statements, three different declarants.
- Condition: The waybill names as declarant (in the instruction and as issuer of the referenced declaration) the same party that the export declaration names and that signs it.
- Options: (a, preferred) decide who declares (Valdara, or Castrano as its agent) and align the instruction, the issuer party and the export declaration; (b) if the customs administration is meant as the authority that registered the declaration, move it to an authority role and name the declarant as issuer.
- Needs decision: yes

### road/08#F4 · Medium · Consignment ID used as shipping order ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0152`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0152`
- XPath: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0151`
- Why: `ShippingOrderID` is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's own ID. The order to the carrier in this flow is Lumeway's transport execution plan request LD-TR-26-0151, a different identifier and document.
- Condition: `ShippingOrderID` holds the number of the shipping order or transport request (LD-TR-26-0151), or is absent.
- Options: (a, preferred) set it to the transport request's ID; (b) remove it and reference the request in a document reference.
- Needs decision: no

### road/08#F5 · Medium · Province in Region instead of CountrySubentity
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:ReturnAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/08#F6 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/08#F7 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/08#F8 · Medium · Despatch advice number used as the consignor's consignment ID
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `CL-DA-26-0153`
- XPath: `04-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `CL-DA-26-0153`
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: `ConsignorAssignedID` is "An identifier for this consignment, assigned by the consignor". The consignor is Valdara; the value is the ID of Castrano's despatch advice, a document number of another party, not an identifier of the consignment.
- Condition: `ConsignorAssignedID` is an identifier Valdara assigns to the consignment, or is absent; the despatch advice, if needed, is referenced as a document.
- Options: (a, preferred) remove it, or use a consignment number of Valdara's; (b) reference the despatch advice through a document reference.
- Needs decision: no

### road/08#F9 · Medium · Required delivery time and latest delivery time disagree
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:RequiredDeliveryTime` = `10:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cbc:LatestDeliveryTime` = `12:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cac:EstimatedDeliveryPeriod/cbc:EndTime` = `11:00:00`
- Why: `RequiredDeliveryTime` is "The delivery time required by the buyer in this shipment stage" (10:00, also the transport request's requested delivery time); `LatestDeliveryTime` is "The latest time of delivery allowed by the buyer" (12:00). The same buyer cannot both require delivery by 10:00 and allow it until 12:00; the estimated delivery window (09:00–11:00) runs past the required time without comment.
- Condition: The required and latest delivery times express one consistent deadline (or a target and a tolerance stated as such), and the estimate fits it.
- Options: (a, preferred) set the latest delivery time to 10:00 or drop it; (b) keep 12:00 as a tolerance and make the required time a requested time.
- Needs decision: no

### road/08#F10 · Medium · Journey ID for a one-off full-truck trip
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `TH-26-04471`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `TH-26-04471`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cbc:TrackingID` = `TH-26-04471`
- Why: `TransportMeans/JourneyID` is "An identifier for the regular service schedule of this means of transport". A truck booked for one full load (`FTL` in the transport request) runs no regular service schedule; the value is the same as the carrier's consignment number and the tracking ID, i.e. the trip or booking number.
- Condition: `JourneyID` is absent, or identifies a regular scheduled service of the truck.
- Options: (a, preferred) remove `JourneyID`, keeping the trip number as carrier-assigned ID and tracking ID; (b) model a scheduled line service if the story wants one.
- Needs decision: no

### road/08#F11 · Medium · Handling units stacked two high exceed the height of a curtain-side trailer
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:HandlingCode` = `STACK2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:LoadingLengthMeasure` = `9.3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MeasurementDimension/cbc:Measure` = `13.6`
- Why: The 9.3 m loading length fits the 25 units only if the 1.85 × 0.65 m units stand three abreast (1.95 m of the trailer width) and two high: 5 rows of 6 = 9.25 m. Two units of 1650 mm stacked are 3.30 m high; the internal height of a curtain-side trailer is about 2.7 m, at most 3.0 m for a mega trailer (own knowledge of European road vehicles). Stacked singly, the units would need about 9 rows (16.7 m) or a different arrangement, more than the stated 9.3 m and, with 3 abreast, more than the 13.6 m of the trailer.
- Condition: The stacking instruction, the units' height, the loading length and the trailer's dimensions are consistent: stacked loads fit the trailer's internal height, and the loading length matches the arrangement.
- Options: (a, preferred) lower the units (e.g. knocked-down benches, see the previous finding) so that two-high stacking fits, keeping 9.3 m; (b) drop the stacking and raise the loading length to what a single layer needs (and check it fits 13.6 m).
- Needs decision: no

### road/08#F12 · Medium · Four benches per handling unit do not fit the unit's dimensions
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[2]/cbc:Measure` = `650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:Quantity` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:PackagingType` = `Bench in stretch film`
- XPath: `01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`
- Why: An assembled bench measures 1800 × 620 × 780 mm (length, depth, height; `01-Order.xml`). A handling unit of 650 mm width and 1650 mm overall height (pallet included, about 150 mm) takes one bench across and at most one layer of 780 mm plus about 720 mm of a second: two assembled benches already need 1560 mm plus the pallet, more than 1650 mm, and four need 3120 mm. Four benches per unit (24 units for 96 benches, as in `04-DespatchAdvice.xml`) fit only if the benches are shipped knocked down or nest deeply, which neither the packaging ("Bench in stretch film") nor the item description says.
- Condition: The number and form of the benches per handling unit fit the unit's dimensions (assembled, nested or knocked down, as stated in the packaging or item description).
- Options: (a, preferred) state that the benches ship knocked down (frames and slats packed flat) and keep 4 per unit; (b) change the units' dimensions or the number of benches per unit.
- Needs decision: yes

### road/08#F13 · Low · Three originals announced, one original distributed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: The note says there are three originals (consignor, consignee, carrier), as the CMR requires, but the distribution lists only the consignee's original with the goods and an electronic copy to the same consignee; the consignor's original is not distributed.
- Condition: The distribution list and the note describe the same originals and copies.
- Options: (a, preferred) add the consignor's original (and the carrier's, if listed) to the distribution; (b) shorten the note.
- Needs decision: no

### road/08#F14 · Low · Locations given by company name or not at all
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:Description` = `Seal check, no inspection of the goods.`
- Why: `IssueLocation` is "The location where this waybill was issued"; its name is the company Castrano Logistics, not a place. The examination ("Seal check") on the main carriage has no location, although it is meaningful only at a place (the border post, cf. `CustomsExitOfficeLocation` in `05-ExportCustomsDeclaration.xml`).
- Condition: The issue location names a place (e.g. Ferrano, with UN/LOCODE XUFER), and the examination event has its location.
- Options: (a, preferred) give the issue location as Ferrano and the examination location as the border crossing; (b) drop the issue location.
- Needs decision: no

### road/08#F15 · Low · Consignee and consignor contacts are sales desks
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: The waybill's receiver is the consignee, whose contact receives the goods; Lumeway gives its `Customer service` desk in `Sales`. The consignor's contact is Valdara's `Order desk` in `Sales`, while the goods are handed over at Castrano's warehouse.
- Condition: The consignee's contact is a goods-in contact and the consignor's contact is reachable for the handover.
- Options: (a, preferred) give the parties logistics contacts; (b) omit JobTitle/Department.
- Needs decision: no

### road/08#F16 · Low · Net-net weight equal to net weight although the goods are packed
- XPath: `/Waybill/cac:Shipment/cbc:NetNetWeightMeasure` = `3762`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:NetWeightMeasure` = `3762`
- Why: `NetNetWeightMeasure` is "The total net weight of this shipment, excluding packaging and transport equipment". The benches are wrapped in stretch film and the side frames in cardboard boxes; the item data put the film at 0.4 kg per bench (38.4 kg for 96 benches). Net-net weight equal to the net weight (3762 kg) means no packaging at all.
- Condition: Net-net weight is the net weight minus the packaging (film and boxes), or only one of the two weights is given.
- Options: (a, preferred) subtract the packaging from the net-net weight; (b) drop `NetNetWeightMeasure`.
- Needs decision: no

### road/08#F17 · Low · Pallet places per unit do not match the floor space
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:FloorSpaceMeasurementDimension/cbc:Measure` = `1.2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:PalletSpaceMeasurementDimension/cbc:Measure` = `0.5`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:FloorSpaceMeasurementDimension/cbc:Measure` = `0.96`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:PalletSpaceMeasurementDimension/cbc:Measure` = `1`
- Why: Unit 25 (1.2 × 0.8 m, 0.96 m²) counts as 1 pallet place, so one place is 0.96 m². Units 1–24 cover 1.2 m² each, i.e. 1.25 places, or 0.625 when stacked two high, not 0.5. With 0.5, the 25 units need 13 places (about 5.4 m of a 33-place, 13.6 m trailer), which contradicts the 9.3 m loading length.
- Condition: The pallet places per unit follow from its floor space (and stacking) in the same way for all units, and agree with the loading length.
- Options: (a, preferred) set 0.625 (stacked) or 1.25 (single) for units 1–24; (b) remove the pallet places if they are not used.
- Needs decision: no

### road/08#F18 · Low · Package level "inner" for the outer packages on the pallets
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:PackageLevelCode` = `1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:Package/cbc:PackageLevelCode` = `1`
- Why: `PackageLevelCode` 1 means "Inner" (UN/EDIFACT 7075). The stretch-wrapped benches and the cardboard boxes are the only packaging of the goods, placed directly on the pallets: they are the outer packages of the goods inside the handling unit, not an inner level of a larger package.
- Condition: The package level fits the packages' place in the packaging hierarchy (outer, code 3, or no level if only one level exists).
- Options: (a, preferred) use 3 (outer); (b) remove the level code.
- Needs decision: no

## Checked and consistent
- Counts: 25 handling units = `TotalTransportHandlingUnitQuantity`; 24 × 4 benches + 12 boxes = 108 packages = `TotalPackagesQuantity`; shipping marks 001 to 025 of 025.
- Weights: gross 4106.4 kg as in `03`, `04`, `05`, `10`; tare 4106.4 − 3762 = 344.4 kg for 25 pallets plus film and boxes (about 14 kg per pallet), plausible.
- Floor space 1.85 × 0.65 = 1.2 m² and 1.2 × 0.8 = 0.96 m² agree with the units' dimensions.
- Loading length 9.3 m fits 5 rows of 1.85 m with units three abreast and two high (computed); it is below the truck's 13.6 m.
- Fuel: 61 l of diesel for the 186 loaded km invoiced in `14-Invoice.xml` is about 33 l/100 km, plausible for a truck with trailer at about 4 t payload (own knowledge).
- FCA delivery terms, risk passing on loading at the 3PL and freight paid by the consignee agree with the order and the transport request (bill-to Lumeway).
- Departure 16:20 = actual despatch in `04-DespatchAdvice.xml`; pickup and delivery locations XUFER/XBMRW as in the transport request.

## Considered and refuted
- `/Waybill/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2` without any `GoodsItem` — refuted: the definition counts the goods items of the shipment (benches and side frames), which the waybill may state without listing them; the CMR's goods description is the summary description.
- `/Waybill/cbc:Description` = `The truck the distributor booked, from the 3PL's warehouse across the border.` reads like a story note — refuted: it is a textual description of the document instance, which the element allows.
- `/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00` vs the despatch advice's actual despatch 16:20 — refuted: loading starts at 15:05 and the truck leaves at 16:20 (departure event).
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:DriverPerson/cbc:ID` = `XU-DL-0417722` without schemeID — refuted: a driving licence number is not a code from a list, and the rule on schemeIDs for codes does not apply.
- Handling unit IDs under schemeID ISO 15459 (`KXU104411490000015` …): the issuing agency code `K` could not be verified against the ISO/IEC 15459 register, so no finding is made (see the report).
