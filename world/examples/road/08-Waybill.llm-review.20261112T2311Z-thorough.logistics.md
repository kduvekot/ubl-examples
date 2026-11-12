# LLM review: 08-Waybill.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/08-Waybill.xml`, Git blob `72164dc3855513c969135349f0d20e5d5cef08c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### road/08#F1 · High · Waybill issued in the morning, reporting events of that afternoon and the next two days as done
- XPath: `/Waybill/cbc:IssueTime` = `08:16:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceDate` = `2026-03-24`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransitPeriod/cbc:EndDate` = `2026-03-25`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cac:FuelConsumption/cbc:FuelConsumptionMeasure` = `61`
- Why: The waybill is issued on 2026-03-23 at 08:16, but it states as facts: the actual pickup at 15:05 and the actual departure at 16:20 the same day, the examination (seal check) on 2026-03-24 at 07:45, a TransitPeriod defined as "the period during which this shipment stage actually took place" ending on 2026-03-25, the carrier's reservation "received in apparent good order" with the seal numbers (made when the goods are taken over), and the fuel consumed by the whole delivery. None of these can be known at 08:16 on the first day. A CMR consignment note is made out when the carrier takes over the goods; the actual examination, transit end and fuel belong in later status reports (`09-TransportationStatus.xml`) or a later version of the waybill.
- Condition: every "actual" event, the transit period and the remarks made on taking over are not later than the waybill's issue date and time; later events are given as estimates or left to later documents.
- Options: (a) preferred: issue the waybill at the pickup (e.g. 2026-03-23 15:10, after loading and sealing) with pickup and remarks, the departure as estimated, and without the examination, transit end and fuel consumption; (b) keep the morning issue time and turn every later event into a planned/estimated one.
- Needs decision: no

### road/08#F2 · High · Gross volume smaller than the handling units it is made of
- XPath: `/Waybill/cac:Shipment/cbc:GrossVolumeMeasure` = `41.5`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[1]/cbc:Measure` = `1850`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[2]/cbc:Measure` = `650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[1]/cbc:Measure` = `1200`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[2]/cbc:Measure` = `800`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:MeasurementDimension[3]/cbc:Measure` = `900`
- Why: GrossVolumeMeasure is "the total volume of the goods in this shipment, including packaging". The 24 identical bench pallets (TransportHandlingUnit[1]–[24]) measure 1.85 × 0.65 × 1.65 m = 1.984 m³ each, 47.62 m³ together; the side-frame pallet (TransportHandlingUnit[25]) measures 1.2 × 0.8 × 0.9 m = 0.864 m³. The packed goods therefore occupy 48.48 m³, 7 m³ more than the stated 41.5 m³.
- Condition: GrossVolumeMeasure equals the sum of the handling units' volumes (or the handling unit dimensions are changed so that they sum to the stated volume).
- Options: (a) preferred: correct whichever value is wrong once F4/F5 (load fit, pallet height) are settled, since the pallet height drives both; (b) set the volume to 48.5 m³ if the dimensions stay.
- Needs decision: no

### road/08#F3 · High · Customs instructions say the 3PL declares the export; the export declaration is the exporter's own
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.`
- Why: The export declaration of this consignment is numbered, issued and signed by Valdara Industries, with no declarant or representative other than the exporter (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`); Castrano Logistics appears there only as Valdara's warehousing service provider. The import half of the sentence agrees with `10-ImportCustomsDeclaration.xml` (declared by Lumeway).
- Condition: the waybill and the export declaration agree on who declares the export.
- Options: (a) preferred: name the exporter as declarant in the waybill text; (b) show Castrano as the declaring agent in the export declaration.
- Needs decision: yes (who acts as declarant is part of the story)

### road/08#F4 · Medium · The load does not fit the trailer as described
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MeasurementDimension/cbc:Measure` = `13.6`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:LoadingLengthMeasure` = `9.3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:HandlingCode` = `STACK2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- Why: Calculated with the document's values and, where stated, my own knowledge of road equipment. Single-high, the 24 bench pallets (1.85 × 0.65 m) need at least 14.8 m of a 2.45 m wide trailer (three side by side lengthwise, 1.95 m of the width, in 8 rows of 1.85 m; crosswise only one fits per 0.65 m, 15.6 m), more than the 13.6 m loading length. The stated 9.3 m therefore assumes stacking two high (12 floor positions: 4 rows × 1.85 m = 7.4 m plus 0.8 m for the side-frame pallet, 8.2 m, plausible with gaps). Two units of 1.65 m make a 3.30 m stack, but a curtain-side trailer within the usual 4.0 m vehicle height has an internal height of about 2.7 m, a "mega" trailer about 3.0 m (own knowledge). The trailer can carry the goods neither single nor double stacked.
- Condition: the handling unit dimensions, the stacking rule and the trailer's loading length (and height, if stated) are such that all 25 units fit, and LoadingLengthMeasure follows from that arrangement.
- Options: (a) preferred: lower the bench pallets (e.g. benches knocked down or laid flat, so that a pallet of 4 is at most about 1.3 m high and two fit within 2.7 m); (b) fewer benches per pallet and a second truck, which changes the story (one full truck, `04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `24 pallets of 4 benches: one full truck.`).
- Needs decision: yes (how the benches are packed is part of the story; see also F5)

### road/08#F5 · Medium · Four assembled benches do not fit the bench pallet
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:PackagingType` = `Bench in stretch film`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[2]/cbc:Measure` = `650`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[3]/cbc:Measure` = `1650`
- Why: The bench is 1800 mm long, 620 mm deep and 780 mm high (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`). On a pallet 1850 × 650 mm only the 620 mm depth fits across the 650 mm width, so each bench stands 780 mm high; four of them need 3120 mm, not 1650 mm. By volume, four bench envelopes are 4 × 1.8 × 0.62 × 0.78 = 3.48 m³ against 1.98 m³ for the whole handling unit. Nothing in the flow says the benches travel knocked down (the item is "for bolting to the ground", "supplied with four ground anchors"), which would be the only way to fit.
- Condition: the packaging description and the handling unit dimensions are consistent with the item dimensions (the benches are stated to travel knocked down or nested, or the pallet is high enough for what it carries).
- Options: (a) preferred: state that the benches travel knocked down (e.g. in PackagingType or the item's additional information) with a pallet height that fits, which also resolves F4; (b) change the pallet dimensions and count.
- Needs decision: yes (packing of the goods)

### road/08#F6 · Medium · Consignment ID given as the shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0152`
- Why: ShippingOrderID is "an identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". LD-CS-26-0152 is the consignment identifier (`/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0152`), not an order. The instruction the carrier received is the transport execution plan request `03-TransportExecutionPlanRequest.xml`, ID LD-TR-26-0151. The same value is used in `09-TransportationStatus.xml`.
- Condition: ShippingOrderID, if present, is the identifier of the shipping order or forwarding instruction (LD-TR-26-0151), or the element is absent.
- Options: (a) preferred: LD-TR-26-0151; (b) remove ShippingOrderID, since the consignment is already identified.
- Needs decision: no

### road/08#F7 · Medium · Despatch advice number given as the consignor's consignment identifier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `CL-DA-26-0153`
- Why: ConsignorAssignedID is "an identifier for this consignment, assigned by the consignor". CL-DA-26-0153 is the number of a document, the despatch advice of the 3PL (`04-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `CL-DA-26-0153`), and the consignor named in the waybill is Valdara Industries, not Castrano. The despatch advice is moreover issued at 15:15, seven hours after this waybill (08:16).
- Condition: ConsignorAssignedID is a consignment identifier assigned by the consignor (Valdara, or its 3PL on its behalf if stated), not a document number; a reference to the despatch advice, if wanted, is a document reference.
- Options: (a) preferred: the consignor's own consignment or shipment number (e.g. the shipment ID CL-SH-26-0154 the 3PL assigns, if the 3PL acts for Valdara); (b) remove the element.
- Needs decision: no

### road/08#F8 · Medium · Customs as the issuer of the export declaration
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cbc:ID` = `VI-CD-26-0156`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: CustomsDeclaration/IssuerParty is "the Party who issues this Customs Declaration". The declaration VI-CD-26-0156 is issued by the exporter Valdara (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `VI-CD-26-0156`, signed by Valdara); the Customs Administration of Urvania is the authority that processes it (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`).
- Condition: IssuerParty names the party that issued the declaration (Valdara Industries), or is absent.
- Options: (a) preferred: Valdara Industries as IssuerParty; (b) remove IssuerParty.
- Needs decision: no

### road/08#F9 · Medium · Origin address is the 3PL's warehouse, not where the goods were made
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:CityName[2]` = `Ferrano`
- Why: Shipment/OriginAddress is "the region in which the goods have been produced or manufactured, according to criteria laid down for the purposes of application of the customs tariff…". Via del Magazzino 24 is Castrano Logistics' warehouse (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress/cbc:StreetName[2]` = `Via del Magazzino`); the benches are made by Valdara, whose works are at Via delle Officine 17 (`01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). The warehouse is where the goods are picked up, which the waybill already gives as the pickup location and ReturnAddress.
- Condition: OriginAddress, if present, is the region (or site) of manufacture, not the despatch warehouse.
- Options: (a) preferred: remove OriginAddress (origin is stated as country XU in the goods documents and the certificate of origin; a waybill has no use for it); (b) give Valdara's works or the region of manufacture.
- Needs decision: no

### road/08#F10 · Medium · The pallet listed as a package contained in itself
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `KXU104411490000015`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:ID` = `KXU104411490000015`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:Quantity` = `1`
- Why: ActualPackage is "a package contained in this transport handling unit". In all 25 handling units it is the pallet itself, with the handling unit's own ID and type PX, and Quantity 1, while Quantity is "the quantity of items contained in this package" (the pallet holds 4 benches, or 12 boxes on TransportHandlingUnit[25]). The handling unit already is the pallet (TransportHandlingUnitTypeCode PX); the packages contained in it are the four film-wrapped benches given in cac:Package.
- Condition: no ActualPackage repeats the handling unit itself; what the pallet contains is described once, in Package or ActualPackage.
- Options: (a) preferred: remove ActualPackage from all 25 handling units; (b) use ActualPackage for the contained packages (benches in film, boxes) instead of Package, if a distinction between planned and actual packing is meant.
- Needs decision: no

### road/08#F11 · Medium · Package quantity used as the number of packages
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package/cbc:Quantity` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:Package/cbc:Quantity` = `12`
- Why: Package/Quantity is "the quantity of items contained in this package". Package 001-1 is described as "Bench in stretch film" (one bench per package), and the handling unit's TotalPackageQuantity is 4; so the value 4 is the number of packages, not the content of one package (which is 1 bench). On TransportHandlingUnit[25] the 12 is the number of cardboard boxes, each holding one side frame (the receipt advice speaks of "a box of side frames" as one unit, `11-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[2]/cbc:OversupplyQuantity` = `1`). The same holds for all 24 bench pallets.
- Condition: each Package aggregate describes one package (or packages of one kind) with Quantity = items in one package, and the number of packages is carried where UBL counts them (TotalPackageQuantity, or one Package per package).
- Options: (a) preferred: Quantity 1 (one bench per film package, one frame per box) and keep TotalPackageQuantity 4 and 12; (b) repeat the Package aggregate per package.
- Needs decision: no

### road/08#F12 · Low · Pallet places too small for the floor space the bench pallets take
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:FloorSpaceMeasurementDimension/cbc:Measure` = `1.2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:PalletSpaceMeasurementDimension/cbc:Measure` = `0.5`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:PalletSpaceMeasurementDimension/cbc:Measure` = `1`
- Why: Floor space 1.85 × 0.65 = 1.20 m² is correct. A pallet place is the floor space of one standard pallet (1.2 × 0.8 = 0.96 m², as TransportHandlingUnit[25] shows: 0.96 m², 1 place). Each bench pallet covers 1.25 such places; stacked two high, half of that is 0.625, not 0.5. In total the stated places (24 × 0.5 + 1 = 13) understate the 16 places that the 12 stacks and the side-frame pallet occupy.
- Condition: pallet places per handling unit follow from its floor space and stacking (0.625 per stacked bench pallet, or 1.25 per position), or the convention used is stated.
- Options: (a) preferred: 0.625 per bench pallet (after F4/F5 are settled); (b) remove PalletSpaceMeasurementDimension and keep floor space and loading length.
- Needs decision: no

### road/08#F13 · Low · Trailer seal only in a remark
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:Description` = `Seal check, no inspection of the goods.`
- Why: The seal is what customs checks at the border (also `09-TransportationStatus.xml`, condition SEAL "Intact, as checked by customs"), but it exists only as text; the trailer carries no TransportEquipment with a TransportEquipmentSeal (seal ID, issuer, condition), so the seal number cannot be checked by a receiving system.
- Condition: the seal number appears in a structured seal element of the equipment it is fixed to.
- Options: (a) preferred: add the trailer as TransportEquipment (plate UR 4160 TR) with TransportEquipmentSeal XU-CL-77310; (b) leave the remark as the only record if the trailer is not modelled as equipment.
- Needs decision: no

### road/08#F14 · Low · Required delivery time and latest delivery time differ
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:RequiredDeliveryTime` = `10:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cbc:LatestDeliveryTime` = `12:00:00`
- Why: The stage gives "the delivery time required by the buyer" as 10:00 on 2026-03-25, the shipment's Delivery gives "the latest time of delivery allowed by the buyer" as 12:00 on the same day. If 10:00 is required, 12:00 is not allowed; if 12:00 is allowed, 10:00 is not required. The transport request asked for 10:00 (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceTime` = `10:00:00`).
- Condition: the required and the latest allowed delivery times agree (or one of them is absent).
- Options: (a) preferred: LatestDeliveryTime 10:00 (as requested); (b) remove one of the two.
- Needs decision: no

### road/08#F15 · Low · Examination event without a place
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceTime` = `07:45:00`
- Why: The examination is given with date, time and description but no location or authority; from the transportation status it is the border crossing (`09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Land border crossing Urvania–Bayvarra`). An examination event without a place does not say where the shipment was examined (see also F1 on its timing).
- Condition: the examination event, if kept, names its location (the border crossing) consistently with the transportation status.
- Options: (a) preferred: remove it from the waybill (F1) and leave it to the status report; (b) add the location.
- Needs decision: no

### road/08#F16 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- Why: IssueLocation is "the location where this waybill was issued"; its name should be the place (a CMR gives "place and date of issue"). "Castrano Logistics" is the company, and the place is identified elsewhere in the document (UN/LOCODE XUFER, Ferrano).
- Condition: IssueLocation names or identifies the place of issue.
- Options: (a) preferred: Name "Ferrano" with ID XUFER (or the warehouse as a place, e.g. "Castrano warehouse, Ferrano"); (b) remove IssueLocation.
- Needs decision: no

### road/08#F17 · Low · Goods items counted but not described
- XPath: `/Waybill/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:TotalGoodsItemQuantity` = `1`
- Why: The shipment says it has 2 goods items and each handling unit 1, but the waybill contains no GoodsItem, so the counts cannot be linked to anything and the nature of the goods per item (benches, side frames), their quantities and gross weights (3984 and 122.4 kg in `05-ExportCustomsDeclaration.xml`) are absent from the transport document. A consignment note states the nature of the goods and weight per item.
- Condition: either the waybill carries the two goods items (description, quantity, gross weight) to which the counts refer, or the counts are absent.
- Options: (a) preferred: add GoodsItem 1 and 2 with the values of the export declaration; (b) remove the TotalGoodsItemQuantity values.
- Needs decision: no

### road/08#F18 · Low · Three originals announced, one distributed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: The note names three originals (consignor, consignee, carrier, as in the CMR), but DocumentDistribution lists only the consignee's original and an electronic copy to the same consignee; the consignor's original (Valdara or its 3PL) is not distributed to anyone.
- Condition: the distribution list and the note agree on the originals and their holders.
- Options: (a) preferred: add a distribution of the consignor's original to Valdara Industries (the carrier keeps its own); (b) change the note.
- Needs decision: no

## Checked and consistent
- Weights: gross 4106.4 kg = 3984 + 122.4 kg (goods items in `05-ExportCustomsDeclaration.xml`); net 3762 kg as shipment NetNetWeight and consignment NetWeight; tare 344.4 kg for 25 pallets, 96 films (0.4 kg each, 38.4 kg) and 12 boxes, about 12 kg per pallet: plausible. 4.1 t is far below the payload of a truck with trailer.
- Package counts: 24 × 4 + 12 = 108 = TotalPackagesQuantity; 25 handling units = TotalTransportHandlingUnitQuantity; shipping marks 001–025 of 025 are consecutive.
- Floor space 1.85 × 0.65 = 1.2025 m² (stated 1.2) and 1.2 × 0.8 = 0.96 m² are correct.
- Handling unit IDs KXU104411490000015 … 0251: the last digit is the GS1 mod-10 check digit of the numeric part (computed for units 1, 2, 3 and 25).
- Fuel: 61 l of diesel for the 186 km invoiced (`14-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `186`) is 32.8 l/100 km, plausible for a loaded truck with trailer.
- Pickup and departure at XUFER, unloading at XBMRW; required delivery 2026-03-25 10:00 equals the request; estimated delivery 09:00 lies in the estimated period 09:00–11:00; actual delivery 09:40 (`11-ReceiptAdvice.xml`) within it.
- FCA with risk passing on loading at the 3PL's warehouse, and freight paid by the consignee, agree with the order and with the carrier's invoice to Lumeway (`14-Invoice.xml`).
- Shipment ID, consignment ID and journey/tracking number TH-26-04471 agree with `09-TransportationStatus.xml`.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID`: the carrier's consignment number equals the journey ID and the tracking ID (TH-26-04471) — refuted because for a full truck load with one consignment one trip number serving all three purposes is normal practice and contradicts nothing.
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportMeansTypeCode`: code 395 "Truck, with trailer" for a 13.6 m loading length, which is a semi-trailer length — refuted because Rec. 28 defines 395 as an "automotive vehicle designed to pull a trailer, with a trailer attached", which covers a tractor with semi-trailer; the plates (truck and trailer) fit.
- `/Waybill/cac:Shipment/cbc:GrossWeightMeasure`: shipment gross weight defined as including transport equipment, equal to the consignment's — refuted because the goods are loose on the haulier's trailer, with no transport equipment of the shipment.
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:HandlingCode`: stacking two high on a curtain-sider loaded "from the side by forklift" — not a problem of handling in itself; the height problem is F4.
