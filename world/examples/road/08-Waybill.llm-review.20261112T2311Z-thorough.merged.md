# LLM review: 08-Waybill.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/08-Waybill.xml`, Git blob `72164dc3855513c969135349f0d20e5d5cef08c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/08#F1 · High · Waybill issued in the morning reports the afternoon pickup, departure, next-day border check and the trip's fuel as done
- XPath: `/Waybill/cbc:IssueDate` = `2026-03-23`
- XPath: `/Waybill/cbc:IssueTime` = `08:16:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceDate` = `2026-03-24`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceTime` = `07:45:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransitPeriod/cbc:EndDate` = `2026-03-25`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cac:FuelConsumption/cbc:FuelConsumptionMeasure` = `61`
- Why: issued 2026-03-23 at 08:16, the waybill states as facts the actual pickup at 15:05 and departure at 16:20 that day, the seal check on 2026-03-24 at 07:45, a `TransitPeriod` ("the period during which this shipment stage actually took place") ending 2026-03-25, the takeover remark with the seal number, and the fuel consumed by the whole delivery; nothing in the waybill uses the fuel figure (no emission). A CMR consignment note is made out when the carrier takes over the goods (own knowledge); the issue location is Castrano's warehouse, where the truck arrives only at 15:05. Merge check: none of these is marked as planned or estimated.
- Condition: every actual event, the transit period, the takeover remark and any consumption lie before the issue date and time; later events are absent or given as estimates.
- Options: (a, preferred) issue the waybill at takeover (after loading and sealing, before 16:20, e.g. 15:20 so that it also follows the despatch advice, see F3), with pickup and remark, the departure as estimated, and without examination, transit end and fuel, which belong in the status report or the freight invoice; (b) a later version of the waybill issued after delivery (after 2026-03-25 09:40) with its own `VersionID`; (c) keep 08:16 and make every later event planned.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1, F12)

### road/08#F2 · High · Gross volume smaller than the handling units it is made of
- XPath: `/Waybill/cac:Shipment/cbc:GrossVolumeMeasure` = `41.5`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[1]/cbc:Measure` = `1850`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[2]/cbc:Measure` = `650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[1]/cbc:Measure` = `1200`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[2]/cbc:Measure` = `800`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[3]/cbc:Measure` = `900`
- Why: `GrossVolumeMeasure` is "The total volume of the goods in this shipment, including packaging". Redone in the merge: units 1–24 (identical dimensions in all 24) are 1.85 × 0.65 × 1.65 = 1.984 m³ each, 47.62 m³ together; unit 25 is 1.2 × 0.8 × 0.9 = 0.864 m³; total 48.48 m³, 7.0 m³ more than stated. Refutation attempt: even without the pallets' own height (about 0.15 m, own knowledge), the goods take 24 × 1.85 × 0.65 × 1.50 + 1.2 × 0.8 × 0.75 = 44.0 m³, still more than 41.5.
- Condition: the gross volume is at least the sum of the handling units' volumes as given by their dimensions.
- Options: (a, preferred) settle the pallet height first (F12, F17), then set the gross volume to the sum of the units (48.5 m³ with the present dimensions); (b) change the dimensions if 41.5 m³ is right.
- Needs decision: no
- From: broad (F2), logistics (F2)

### road/08#F3 · High · Waybill refers to documents issued after it
- XPath: `/Waybill/cbc:IssueTime` = `08:16:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cbc:ID` = `VI-CD-26-0156`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `CL-DA-26-0153`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:IssueTime` = `13:25:00`
- XPath: `04-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `15:15:00`
- Why: the waybill (2026-03-23 08:16) cites the export declaration VI-CD-26-0156, which is part of `05-ExportCustomsDeclaration.xml`, issued the same day at 13:25, and carries the number of Castrano's despatch advice, issued at 15:15 (logistics noted the second inside its F7). A document cannot refer to documents that do not yet exist. The waybill's own haulage instruction ("Wait at the warehouse until customs has released the export declaration") also places the waybill after the declaration. Added by the merge as a finding of its own, as rail did for its waybill; it is resolved by option (a) of F1 if the new issue time is after 15:15.
- Condition: every document the waybill refers to or whose number it carries is issued before the waybill.
- Options: (a, preferred) issue the waybill after 15:15 (F1 option a); (b) drop the references that cannot exist yet (and fix F11).
- Needs decision: no
- From: merge (logistics F7 noted the despatch advice timing)

### road/08#F4 · High · Customs instruction says the 3PL declares the export; the export declaration is Valdara's
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: the export declaration is numbered (`VI-…`), made and signed by Valdara as exporter, with no declarant or representative besides it; Castrano appears there only as Valdara's warehousing provider. The import half of the sentence agrees with `10-ImportCustomsDeclaration.xml` (Lumeway). Under FCA, export clearance is the seller's (own knowledge of Incoterms 2020).
- Condition: the waybill and the export declaration agree on who declares the export.
- Options: (a, preferred) "The export is declared by the seller in Ferrano; …" (matches 05 and FCA); (b) make Castrano the declaring agent in the export declaration, which changes 05.
- Needs decision: no
- From: broad (F3, High, yes; combined with the issuer), logistics (F3, High, yes), context (F2, High, no)

### road/08#F5 · High · Customs administration named as issuer of the exporter's declaration
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `VI-CD-26-0156`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: `CustomsDeclaration/IssuerParty` is "The Party who issues this Customs Declaration". In `05-ExportCustomsDeclaration.xml` the same declaration is made and signed by Valdara, and the customs administration is the `CustomsParty` that receives it. The waybill therefore contradicts the declaration it cites (High, as rail did for the same case; the parts had Medium, broad had it inside its High).
- Condition: `IssuerParty` names the party that made the declaration in 05 (Valdara), or is absent.
- Options: (a, preferred) Valdara as issuer; (b) drop `IssuerParty`, the ID already resolves to 05.
- Needs decision: no
- From: logistics (F8, Medium), context (F5, Medium), parties (F4, Medium), broad (F3)

### road/08#F6 · Medium · Consignment ID given as shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0152`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0152`
- XPath: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0151`
- Why: `ShippingOrderID` is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's ID; the order to the carrier is Lumeway's transport request LD-TR-26-0151. The same value is in `09-TransportationStatus.xml`. Medium, not High: no example states a different shipping-order ID (as rail).
- Condition: `ShippingOrderID` holds the transport request's ID, or is absent.
- Options: (a, preferred) LD-TR-26-0151; (b) drop it.
- Needs decision: no
- From: broad (F4), logistics (F6), context (F3)

### road/08#F7 · Medium · Province in Region instead of CountrySubentity
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:ReturnAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity` ("The political or administrative division of a country …, such as the name of its county, province, or state"), which the Bayvarran address uses (`/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 104 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: no Urvanian address holds the province in `Region`; it is in `CountrySubentity`.
- Options: (a, preferred) move it to `CountrySubentity`; (b) define Urvanian provinces as economic regions in the world's address rules.
- Needs decision: no
- From: broad (F5), context (F6), parties (F1)

### road/08#F8 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 occurrences in 213 files (counted over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad (F6), context (F7), parties (F2, yes)

### road/08#F9 · Medium · Gate number in AdditionalStreetName of the consignee's postal address
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance. The waybill has its own delivery instruction (`/Waybill/cac:Shipment/cac:Consignment/cbc:DeliveryInstructions` = `Unload at dock 4; report to the gatehouse first.`), which is where an entrance belongs.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop it from the address; if the gate matters for this delivery, add it to the delivery instruction or the delivery location.
- Needs decision: no
- From: broad (F7), parties (F3)

### road/08#F10 · Medium · Origin address is the 3PL's warehouse, not where the goods were made
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: `Shipment/OriginAddress` is "the region in which the goods have been produced or manufactured, according to criteria laid down for the purposes of application of the customs tariff…". Via del Magazzino is Castrano's warehouse, the pickup place; Valdara's works are in Via delle Officine.
- Condition: `OriginAddress`, if present, is the region or site of manufacture.
- Options: (a, preferred) drop it (origin XU is stated in the goods documents and the certificate; the waybill has no use for it); (b) Valdara's works or the region of manufacture.
- Needs decision: no
- From: logistics (F9)

### road/08#F11 · Medium · Despatch advice number given as the consignor's consignment ID
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `CL-DA-26-0153`
- XPath: `04-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `CL-DA-26-0153`
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: `ConsignorAssignedID` is "An identifier for this consignment, assigned by the consignor". The consignor is Valdara; the value is the number of Castrano's despatch advice, a document number of another party (and issued after the waybill, F3).
- Condition: `ConsignorAssignedID` is a consignment identifier of the consignor (or of its agent, if the story says so), or is absent.
- Options: (a, preferred) drop it (context); (b) the shipment ID CL-SH-26-0154, if Castrano acts for the consignor (logistics).
- Needs decision: no
- From: broad (F8), logistics (F7), context (F4)

### road/08#F12 · Medium · The load does not fit the trailer, single or double stacked
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MeasurementDimension/cbc:Measure` = `13.6`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:LoadingLengthMeasure` = `9.3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:HandlingCode` = `STACK2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- Why: redone in the merge with the document's values and, for the trailer's inner width (about 2.45 m) and height (about 2.7 m for a curtain-sider, 3.0 m for a mega trailer), own knowledge. Lengthwise, three 0.65 m units stand abreast (1.95 m); crosswise a 1.85 m unit leaves 0.60 m, too little for a second. Single high: 24 units in 8 rows of 1.85 m = 14.8 m plus the side-frame pallet, more than 13.6 m. Two high: 12 positions in 4 rows = 7.4 m plus the side-frame pallet in a fifth row = 9.25 m, which is the stated 9.3 m; but the stack is 2 × 1.65 = 3.30 m high, above either trailer height. The trailer's height is not in the document, so the contradiction rests on own knowledge: Medium, not High. Weight is no limit: 4106.4 kg, a stack of two bench pallets about 2 × 180 kg.
- Condition: the handling units' dimensions, the stacking rule and the trailer's length (and height, if stated) are such that all 25 units fit, and the loading length follows from that arrangement.
- Options: (a, preferred) lower the bench pallets (benches knocked down or laid flat, F17) so that two fit within about 2.7 m, keeping 9.3 m; (b) fewer benches per pallet and a second truck, which changes the story (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `24 pallets of 4 benches: one full truck.`).
- Needs decision: yes (depends on how the benches are packed, F17; option b changes the story)
- From: broad (F11, no), logistics (F4, yes)

### road/08#F13 · Medium · Journey ID for a one-off full-truck trip
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `TH-26-04471`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `TH-26-04471`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cbc:TrackingID` = `TH-26-04471`
- Why: `TransportMeans/JourneyID` is "An identifier for the regular service schedule of this means of transport". A truck booked for one full load runs no regular schedule; the value is the carrier's trip or booking number. Logistics and context refuted the equality of the three IDs (one job number for consignment, trip and tracking is normal); that refutation stands for `CarrierAssignedID` and `TrackingID`, but not for `JourneyID`, whose definition is about a schedule.
- Condition: `JourneyID` is absent, or identifies a regular scheduled service.
- Options: (a, preferred) drop `JourneyID`, keeping the job number as carrier-assigned ID and tracking ID; (b) a scheduled line service, if the story wants one.
- Needs decision: no
- From: broad (F10)

### road/08#F14 · Medium · Required and latest delivery times disagree
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:RequiredDeliveryTime` = `10:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cbc:LatestDeliveryTime` = `12:00:00`
- XPath: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceTime` = `10:00:00`
- Why: `RequiredDeliveryTime` is "The delivery time required by the buyer in this shipment stage" (10:00, as requested in 03); `LatestDeliveryTime` "The latest time of delivery allowed by the buyer" (12:00), the same day. A target with a tolerance is a possible reading, but the definitions say "required" and "latest allowed", which cannot both hold. Medium (broad) rather than Low (logistics): two values of one buyer contradict each other unless one is reinterpreted.
- Condition: the required and the latest allowed delivery times agree, or one of them is absent.
- Options: (a, preferred) `LatestDeliveryTime` 10:00, as requested; (b) drop one of the two.
- Needs decision: no
- From: broad (F9, Medium), logistics (F14, Low)

### road/08#F15 · Medium · The pallet listed as a package contained in itself
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `KXU104411490000015`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:ID` = `KXU104411490000015`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:Quantity` = `1`
- Why: `ActualPackage` is "a package contained in this transport handling unit". In all 25 handling units it is the pallet itself (same ID, type PX, Quantity 1), while the handling unit already is that pallet (`TransportHandlingUnitTypeCode` PX).
- Condition: no `ActualPackage` repeats its handling unit; what the pallet contains is described once.
- Options: (a, preferred) drop `ActualPackage` from all 25 units; (b) use it for the contained packages instead of `Package`, if planned and actual packing are meant to differ.
- Needs decision: no
- From: logistics (F10)

### road/08#F16 · Medium · Package quantity used as the number of packages
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:Quantity` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:Package/cbc:Quantity` = `12`
- Why: `Package/Quantity` is "the quantity of items contained in this package". Package 001-1 is "Bench in stretch film", one bench per package; 4 is the number of packages (the unit's `TotalPackageQuantity`). On unit 25, 12 is the number of boxes, one side frame each. The same in all 24 bench pallets.
- Condition: `Package/Quantity` is the number of items in one package; the number of packages is in `TotalPackageQuantity` or one `Package` per package.
- Options: (a, preferred) Quantity 1, keeping `TotalPackageQuantity` 4 and 12; (b) one `Package` per package.
- Needs decision: no
- From: logistics (F11)

### road/08#F17 · Medium · Four assembled benches do not fit the bench pallet
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[2]/cbc:Measure` = `650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:PackagingType` = `Bench in stretch film`
- XPath: `/Waybill/cac:Shipment/cbc:HandlingCode` = `UPRIGHT`
- XPath: `01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`
- Why: the bench is 1800 × 620 × 780 mm (length, depth, height; 01, 04). Redone in the merge: on a 1850 × 650 mm pallet only the 620 mm depth fits across, so a bench stands 780 mm high (on its back, 780 mm would not fit the 650 mm width; on its end, 1800 mm exceeds 1650 mm). Two layers are already 1560 mm plus the pallet (about 150 mm, own knowledge) = 1710 mm > 1650 mm; four need 3120 mm. By envelope, 4 × 1.8 × 0.62 × 0.78 = 3.48 m³ against 1.98 m³ for the whole unit. Only knocked-down or deeply nested benches fit, which neither the packaging ("Bench in stretch film", one bench per package) nor the item ("for bolting to the ground", "supplied with four ground anchors") says, and the shipment's `UPRIGHT` handling code suggests assembled goods. Rail lowered a similar case (benches in a container) to Low because it rests on the assumption "assembled"; here the gap is a factor of two in height and the waybill's own packaging text describes whole benches, so Medium is kept.
- Condition: the packaging description and the unit's dimensions are consistent with the item dimensions (the benches are stated to travel knocked down or nested, or the pallet is high enough).
- Options: (a, preferred) state that the benches travel knocked down (packaging type or item information) with a pallet height that fits, which also resolves F12; (b) change the pallet dimensions or the number per pallet.
- Needs decision: yes (how the goods are packed is part of the story)
- From: broad (F12, yes), logistics (F5, yes)

### road/08#F18 · Low · Document description narrates the example
- XPath: `/Waybill/cbc:Description` = `The truck the distributor booked, from the 3PL's warehouse across the border.`
- XPath: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:Note` = `The truck the distributor booked, from the 3PL's warehouse across the border.`
- Why: `Description` is "Textual description of the document instance"; the text speaks of the parties in the third person and is the same sentence as the transport request's note: a caption of the example rather than the carrier's description. Broad refuted it because the element allows a textual description; the merge keeps it as Low, since the text describes the story, not the waybill.
- Condition: the description describes the waybill as the carrier would, or is absent.
- Options: (a, preferred) drop it (`Name` already says it is a CMR consignment note); (b) a carrier's description of route and consignment.
- Needs decision: no
- From: context (F8); broad considered and refuted it

### road/08#F19 · Low · Three originals announced, one distributed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: the note names three originals (as under the CMR), but the distribution lists only the consignee, for the original with the goods and an electronic copy; the consignor's original is not distributed.
- Condition: the distribution list and the note agree on who receives which original.
- Options: (a, preferred) add the consignor's original to Valdara (the carrier keeps its own); (b) change the note.
- Needs decision: no
- From: broad (F13), logistics (F18), context (F13), parties (F5)

### road/08#F20 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- Why: `IssueLocation` is "The location where this waybill was issued"; the name is the warehouse operator, not a place; the CMR's "established in" is a place (Ferrano, `XUFER`, used for the pickup in the same document).
- Condition: the issue location names or identifies a place.
- Options: (a, preferred) Name `Ferrano` with ID `XUFER`; (b) "Castrano warehouse, Ferrano".
- Needs decision: no
- From: broad (F14), logistics (F16), context (F9), parties (F6)

### road/08#F21 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday; the date occurs 271 times as `RegistrationDate` across the examples for at least 25 companies (parties' count over `*.xml`), while Lumeway (1988-10-03) and Valdara (1962-04-12) have their own dates. It reads as a filler (IND5).
- Condition: each party's registration date is its own plausible date, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) leave it out where the world has none.
- Needs decision: yes (each company's history is story; aligned with rail and air)
- From: parties (F7, no)

### road/08#F22 · Low · Consignee and consignor contacts are sales desks
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the consignee's contact takes delivery and signs for it; Lumeway gives its customer service in Sales. The consignor's contact deals with the loading, which happens at Castrano's warehouse; Valdara gives its order desk.
- Condition: the consignee's contact receives goods; the consignor's (or the loading place's) contact handles the loading.
- Options: (a, preferred) goods-in for Lumeway and the warehouse office for the loading; (b) drop job titles and departments that do not fit.
- Needs decision: no
- From: broad (F15), context (F10), parties (F8)

### road/08#F23 · Low · Consignor's stock-exchange listing in a consignment note
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: the listing of Valdara's shares plays no part in the contract of carriage (section 4.8, IND5).
- Condition: the waybill carries no `SecurityListing`.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: context (F11), parties (F9)

### road/08#F24 · Low · Net-net weight equal to net weight although the goods are packed
- XPath: `/Waybill/cac:Shipment/cbc:NetNetWeightMeasure` = `3762`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:NetWeightMeasure` = `3762`
- Why: `NetNetWeightMeasure` is "The total net weight of this shipment, excluding packaging and transport equipment"; the benches are in stretch film (0.4 kg each in the item data, 38.4 kg for 96) and the side frames in boxes, so net-net cannot equal the net weight.
- Condition: net-net weight is the net weight minus film and boxes, or only one of the two is given.
- Options: (a, preferred) subtract the packaging; (b) drop `NetNetWeightMeasure`.
- Needs decision: no
- From: broad (F16)

### road/08#F25 · Low · Goods items counted but not described
- XPath: `/Waybill/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:TotalGoodsItemQuantity` = `1`
- Why: the shipment counts 2 goods items and each unit 1, but the waybill has no `GoodsItem`; the nature, quantity and gross weight per item (3984 and 122.4 kg in `05-ExportCustomsDeclaration.xml`), which a consignment note states, are only in the summary description. Broad refuted the count without goods items (the definition allows a count, the summary description is the CMR's goods description); the merge keeps the incompleteness as Low.
- Condition: the waybill carries the two goods items the counts refer to, or the counts are absent.
- Options: (a, preferred) add goods items 1 and 2 with the export declaration's values; (b) drop the counts.
- Needs decision: no
- From: logistics (F17); broad considered and refuted the count

### road/08#F26 · Low · Trailer seal only in a remark
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- Why: the seal is what customs checks at the border (`09-TransportationStatus.xml` reports its condition), but it exists only as text; the trailer has no `TransportEquipment` with a `TransportEquipmentSeal`.
- Condition: the seal number appears in a structured seal of the equipment it is fixed to.
- Options: (a, preferred) the trailer as transport equipment with the seal; (b) keep the remark only, if the trailer is not modelled as equipment.
- Needs decision: no
- From: logistics (F13)

### road/08#F27 · Low · Examination event without a place
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:Description` = `Seal check, no inspection of the goods.`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Land border crossing Urvania–Bayvarra`
- Why: the examination has date, time and description but no location; the status report places it at the border crossing.
- Condition: the examination event, if kept, names its location as the status report does.
- Options: (a, preferred) drop it from the waybill (F1); (b) add the location.
- Needs decision: no
- From: broad (F14), logistics (F15)

### road/08#F28 · Low · Pallet places do not follow from the floor space
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:FloorSpaceMeasurementDimension/cbc:Measure` = `1.2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:PalletSpaceMeasurementDimension/cbc:Measure` = `0.5`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:FloorSpaceMeasurementDimension/cbc:Measure` = `0.96`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:PalletSpaceMeasurementDimension/cbc:Measure` = `1`
- Why: unit 25 (0.96 m²) counts as 1 place, so a place is 0.96 m². A bench unit (1.2 m²) is 1.25 places, 0.625 when stacked two high, not 0.5. The stated total (24 × 0.5 + 1 = 13 places) understates the 16 the 12 stacks and the side-frame pallet take.
- Condition: pallet places follow from floor space and stacking in the same way for all units.
- Options: (a, preferred) 0.625 per stacked bench unit, after F12/F17 are settled; (b) drop the pallet places.
- Needs decision: no
- From: broad (F17), logistics (F12)

### road/08#F29 · Low · Package level "inner" for the only packaging level
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:PackageLevelCode` = `1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:Package/cbc:PackageLevelCode` = `1`
- Why: code 1 is "Inner" (UN/EDIFACT 7075). The film-wrapped benches and the boxes are the only packaging, placed directly on the pallets: the outer packages inside the handling unit.
- Condition: the package level fits the packages' place in the hierarchy, or is absent.
- Options: (a, preferred) 3 (outer); (b) drop the code.
- Needs decision: no
- From: broad (F18)

### road/08#F30 · Low · ISO 15459 issuing agency code "K" could not be verified
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `KXU104411490000015`
- Why: the handling unit IDs are given under scheme `ISO 15459`; their first character `K` would be the issuing agency code, which the review could not check against the ISO/IEC 15459 register. If `K` is assigned to a real agency, a fictional licence plate would be mistakable for a real one; if it is not assigned, the ID is not an ISO 15459 identifier. Broad recorded it as not verifiable and made no finding; aligned with rail, which kept the same question as Low with a decision. The trailing digit is a valid GS1 mod-10 check digit of the numeric part (logistics, units 1, 2, 3, 25).
- Condition: the issuing agency code is one the world's sources record as safe for fictional use, or the IDs use a world scheme.
- Options: (a, preferred) verify against the register and record it in the sources; (b) a world scheme for the licence plates.
- Needs decision: yes
- From: broad (Considered and refuted, not verifiable)

## Checked and consistent
- Counts: 25 handling units = `TotalTransportHandlingUnitQuantity`; 24 × 4 + 12 = 108 = `TotalPackagesQuantity`; shipping marks 001–025 of 025 (broad, logistics, context).
- Weights (redone in the merge): gross 4106.4 = 3984 + 122.4 kg (goods items of `05-ExportCustomsDeclaration.xml`), as in 03, 04, 05 and 10; tare 4106.4 − 3762 = 344.4 kg for 25 pallets, 96 films (38.4 kg) and 12 boxes, about 12 kg per pallet: light for a returnable pallet of 1.2 m² (a euro pallet of 0.96 m² weighs 20–25 kg, own knowledge), but within what a light timber pallet weighs, so no finding. 3984 / 96 = 41.5 kg gross per bench. 4.1 t is far below a truck's payload.
- Floor space 1.85 × 0.65 = 1.2025 m² (stated 1.2) and 1.2 × 0.8 = 0.96 m² correct.
- Loading length: 9.25 m for 4 rows of two-high stacks plus a row for the side-frame pallet (F12 for the height).
- Fuel 61 l for the 186 km invoiced in `14-Invoice.xml` = 32.8 l/100 km, plausible for a loaded truck (timing in F1).
- FCA, risk passing on loading at the 3PL's warehouse and freight paid by the consignee agree with the order, the transport request and the carrier's invoice.
- Pickup and departure at XUFER, unloading at XBMRW; estimated delivery 09:00 within 09:00–11:00; actual delivery 09:40 (`11-ReceiptAdvice.xml`) within it; departure 16:20 = actual despatch of `04-DespatchAdvice.xml`.
- Shipment, consignment and job number TH-26-04471 agree with `09-TransportationStatus.xml`.
- `WaybillTypeCode` CMR, the name and the three-originals note agree; `AdValoremIndicator` false fits a CMR without declared value; the operating permit fits international haulage (context).
- Party identity the same across the flow; GLN 9520610900008 and ISIN XU0001042501 correct (`check_ids.py`); roles agree with 03 and 09 (parties).

## Considered and refuted
- `/Waybill/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2` without any `GoodsItem` — refuted as a contradiction because the definition counts the goods items and the summary description is the CMR's goods description (from broad); the incompleteness is F25.
- `/Waybill/cbc:Description` as a story note — refuted because the element allows a textual description (from broad); the merge keeps it as F18.
- `/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00` vs the actual despatch 16:20 in 04 — refuted because loading starts at 15:05 and the truck leaves at 16:20 (from broad).
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:DriverPerson/cbc:ID` = `XU-DL-0417722` without schemeID — refuted because a licence number is no code from a list (from broad).
- Handling unit IDs under ISO 15459 — not verifiable (from broad); made F30 in the merge.
- `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` equal to journey and tracking ID — refuted because one job number for a full truck load is normal (from logistics and context); `JourneyID`'s definition is F13.
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportMeansTypeCode`: 395 "Truck, with trailer" for a semi-trailer length — refuted because Rec. 28's 395 covers a tractor with semi-trailer (from logistics).
- `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` defined as including transport equipment, equal to the consignment's — refuted because the goods are loose on the haulier's trailer (from logistics).
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:HandlingCode`: stacking on a side-loaded curtain-sider — not a problem in itself; the height is F12 (from logistics).
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation` for a road place — refuted because UBL defines it as "The location of loading for a shipment stage" (from context).
- `/Waybill/cac:Shipment/cac:ReturnAddress` without a use — refuted because the pallets are returnable (from context).
- `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]`: Italian name tagged `en-XU` — refuted because English keeps foreign street names and the subtag follows the sender (from parties).
- `/Waybill/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN could be real — refuted, prefix 952 is for demonstrations, check digit correct (from parties).
- `/Waybill/cac:SenderParty/cac:Contact/cbc:Telephone`: could be real — refuted, +999 is reserved (from parties).
- `/Waybill/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01` as a contract number — refuted, the definition does not say who assigns it (from parties).
- `/Waybill/cac:ConsignorParty` = Valdara while the goods leave Castrano's warehouse — refuted because the consignor is the party responsible for sending the goods, Castrano its service provider (from parties).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 and context/F12 (fuel) → F1: combined; options of all parts kept.
- New F3 (references to documents issued after the waybill): added by the merge from logistics/F7's remark on the despatch advice and the 13:25 export declaration, as rail did for its waybill.
- broad/F3 split into F4 (instruction) and F5 (issuer); F5 raised from Medium (logistics/F8, context/F5, parties/F4) to High because it contradicts the declaration it cites in 05 (as rail). F4: Needs decision no (broad and logistics yes), because the preferred option only aligns the text with 05.
- parties/F2 → F8: Needs decision no, aligned with the other parts and earlier flows.
- broad/F11, logistics/F4 → F12: Needs decision yes (broad no), because it follows the packing decision of F17; physics redone.
- broad/F12, logistics/F5 → F17: kept Medium/yes; reason for not following rail's Low given in the finding.
- logistics/F14 → F14: Medium as broad (logistics Low).
- parties/F7 → F21: Needs decision changed from no to yes, aligned with rail and air.
- broad/F14 split into F20 (issue location, with three other parts) and F27 (examination location, with logistics/F15).
- broad's two refutations (Description, goods items count) not followed as refutations of the incompleteness: F18 and F25 kept Low.
- broad's unverifiable ISO 15459 note → F30 (Low, yes), aligned with rail.

## Outside this review
- Whether a truck can be at Castrano's warehouse at 15:05 and still cross the border by the next morning, and the 186 km against the map's route, are timeline and route questions across documents.
